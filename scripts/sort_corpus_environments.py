#!/usr/bin/env python3
"""Harvest, classify, and sort all formal environments and proofs across the 32-paper Markdown corpus + Volume I."""

from __future__ import annotations

import json
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_CORPUS_DIR = Path("/home/yzk/.cache/duan-hofas/corpus")
DEFAULT_VOL1_DB = Path("/home/yzk/.cache/duan-hofas/volume1.sqlite")

START_LM = re.compile(
    r"^\*\*(Definition|Assumption|Condition|Problem|Lemma|Proposition|Theorem|Corollary|Remark|定义|假设|条件|问题|引理|命题|定理|推论|说明)\b"
)
PROOF_LINE_RE = re.compile(
    r"^(?:###\s+(?:\d+(?:\.\d+)*\.?\s+)?)?(?:\*\*)?"
    r"(Proof(?:\s+of\s+(?:Theorem|Lemma|Proposition|Corollary|conclusion)\s*[A-Za-z0-9.()\-]+)?|证明)"
    r"(?:\*\*)?(?:\s*[.:：]\s*.*|\s*$|\s+[\u4e00-\u9fa5A-Z].*)"
)
STOP_FOR_LM = re.compile(
    r"^(?:\*\*(?:Definition|Assumption|Condition|Problem|Lemma|Proposition|Theorem|Corollary|Remark|定义|假设|条件|问题|引理|命题|定理|推论|说明)\b"
    r"|###\s+|(?:Example|例)\s*[0-9.]+|\d+\)\s+[A-Z][A-Za-z\s\-]+:)"
)
DEF_POST_PROSE_STOP_RE = re.compile(
    r"^(?:Based on\b|With (?:the|𝔽|this)\b|Regarding\b|Consider\b|Now,\b|Next,\b|In this article\b|"
    r"In general,\b|To (?:implement|describe|introduce|conclude|characterize)\b|It (?:is|follows|can be)\b|"
    r"The (?:following|above)\b|Denoting\b|If the term\b|Similarly,\b|Obviously,\b|Clearly,\b|"
    r"For convenience, a\b|Parallel to\b|Corresponding to\b|Correspondingly,\b|Let 𝕊 be\b|Let us\b|"
    r"Convention C\d+\b|Therefore,\b|According to\b|By definition,\b|When the system\b|For a particularly\b|"
    r"Recall Proposition\b|In the context of\b|"
    r"基于(?:此|上述)|在此基础上|由定义\s*\d+|与文献|二阶亚|高阶亚|具有时变|现在考虑|类似地|特别地,\s*对于下述|进一步地,\s*称)"
)
STOP_FOR_PROOF = re.compile(
    r"^(?:\*\*(?:Definition|Assumption|Condition|Problem|Lemma|Proposition|Theorem|Corollary|Remark|定义|假设|条件|问题|引理|命题|定理|推论|说明)\b"
    r"|###\s+(?!.*Proof\b)|(?:Example|例)\s*[0-9.]+|(?:References|参考文献|Acknowledgements|Acknowledgment)\b)"
)

ZH_MAP = {
    "定义": "Definition",
    "假设": "Assumption",
    "条件": "Condition",
    "问题": "Problem",
    "引理": "Lemma",
    "命题": "Proposition",
    "定理": "Theorem",
    "推论": "Corollary",
    "说明": "Remark",
}


def norm_one_line(text: str) -> str:
    text = re.sub(r"-\s*\n\s*", "", text)
    return re.sub(r"\s+", " ", text).strip()


def classify_theorem_opening(flat: str) -> str:
    body = re.sub(r"^(?:Theorem|定理)\s*[A-Za-z0-9.\-′']+\s*[:.：]?\s*", "", flat)
    if body.startswith(("Suppose ", "Suppose that", "设 ", "假设")):
        return "Suppose/Assume-first"
    if body.startswith(("Let ", "令 ", "记 ")):
        return "Let-first"
    if body.startswith(("Consider ", "For ", "对于", "给定", "针对")):
        return "For/Consider-first"
    if body.startswith(("Under ", "If ", "When ", "当 ", "如果", "若 ")):
        return "Under/If/When-first"
    if body.startswith(("The ", "System ", "A ", "An ", "There ")):
        return "Direct-claim-with-inline-if"
    return "Other"


def classify_proof_type(flat: str) -> list[str]:
    tags = []
    fl = flat.lower()
    if any(k in fl for k in ("contradiction", "矛盾")):
        tags.append("Contradiction")
    if any(k in fl for k in ("induction", "归纳")):
        tags.append("Induction")
    if "sufficiency" in fl and "necessity" in fl or ("充分性" in flat and "必要性" in flat):
        tags.append("Sufficiency-Necessity")
    if any(k in fl for k in ("step 1", "the first step", "four steps", "three steps", "two steps")):
        tags.append("Multi-Step")
    if any(k in fl for k in ("first conclusion", "second conclusion", "first two conclusions", "it remains to show", "need only to show")):
        tags.append("Multi-Conclusion")
    if any(k in fl for k in ("substituting", "applying controller", "applying the control", "代入")):
        tags.append("Direct-Substitution")
    if any(k in fl for k in ("lyapunov", "李雅普诺夫", "v̇", "dot v")):
        tags.append("Lyapunov")
    if any(k in fl for k in ("state-space form", "状态空间形式")):
        tags.append("State-Space-Conversion")
    if any(k in fl for k in ("stationary point", "monoton", "驻点")):
        tags.append("Stationary-Point-Reduction")
    if any(k in fl for k in ("observer", "observation error", "观测器")):
        tags.append("Observer/Error-Dynamics")
    if any(k in fl for k in ("one-to-one", "conversely", "可逆性", "diffeomorphism", "homeomorphism")):
        tags.append("Equivalence/Homeomorphism")
    if not tags:
        tags.append("Direct-Algebraic/Citation")
    return tags


def classify_proof_closer(flat: str) -> str:
    if "The proof is finished" in flat:
        return "The proof is finished."
    if "The proof is completed" in flat or "The proof is complete" in flat:
        return "The proof is completed."
    if "This completes the proof" in flat or "which completes the proof" in flat:
        return "This completes the proof."
    if "Thus the conclusion follows" in flat or "the conclusion follows" in flat or "conclusion of the" in flat:
        return "Thus the conclusion follows."
    if "Combining the above two aspects" in flat:
        return "Combining the above two aspects..."
    if "证毕" in flat:
        return "证毕。"
    if "可得定理结论" in flat or "得证" in flat:
        return "可得定理结论 / 得证"
    if "□" in flat or "▪" in flat or "■" in flat:
        return "QED-symbol-only (□/▪)"
    return "Direct-final-equation/sentence (no verbal closer)"


def main() -> None:
    papers_dir = DEFAULT_CORPUS_DIR / "papers"
    sorted_dir = DEFAULT_CORPUS_DIR / "sorted"
    sorted_dir.mkdir(parents=True, exist_ok=True)

    buckets: dict[str, list[dict]] = defaultdict(list)
    proofs: list[dict] = []

    for md_file in sorted(papers_dir.glob("*.md")):
        doc_id = md_file.stem
        lines = md_file.read_text(encoding="utf-8").splitlines()
        sep_indices = [idx for idx, l in enumerate(lines) if l.strip() == "---"]
        body_start = sep_indices[2] + 1 if len(sep_indices) >= 3 else 0
        cur_page = 1
        i = body_start
        while i < len(lines):
            s = lines[i].strip()
            mp = re.match(r"^<!--\s*PDF\s+p\.(\d+)/(\d+)\s*-->$", s)
            if mp:
                cur_page = int(mp.group(1))
                i += 1
                continue
            ml = START_LM.match(s)
            if ml:
                raw_k = ml.group(1)
                kind = ZH_MAP.get(raw_k, raw_k)
                start_ln = i + 1
                start_pg = cur_page
                blk = [s.strip("*")]
                j = i + 1
                while j < len(lines):
                    sj = lines[j].strip()
                    mp2 = re.match(r"^<!--\s*PDF\s+p\.(\d+)/(\d+)\s*-->$", sj)
                    if mp2:
                        cur_page = int(mp2.group(1))
                        j += 1
                        continue
                    if sj.startswith("## [Page "):
                        j += 1
                        continue
                    if STOP_FOR_LM.match(sj) or PROOF_LINE_RE.match(sj):
                        break
                    if kind == "Definition" and sj and DEF_POST_PROSE_STOP_RE.match(sj):
                        non_empty_prev = [x for x in blk if x]
                        joined_so_far = " ".join(non_empty_prev)
                        if non_empty_prev and non_empty_prev[-1].endswith((".", "。", "）", ")")) and any(
                            kw in joined_so_far for kw in ("called", "said to be", "belong to class", "称为", "定义为", "全驱", "能控", "能观")
                        ):
                            break
                    if sj:
                        blk.append(sj)
                    elif blk and blk[-1] != "":
                        blk.append("")
                    if len(blk) > 65:
                        break
                    j += 1
                text_blk = "\n".join(blk).strip()
                buckets[kind].append(
                    {
                        "doc_id": doc_id,
                        "page": start_pg,
                        "line": start_ln,
                        "text": text_blk,
                        "flat": norm_one_line(text_blk),
                    }
                )
                i = j
                continue

            if PROOF_LINE_RE.match(s) and not s.startswith(("Proofs of", "Proof is", "Proof that", "Proof of Some")):
                if re.match(
                    r"^(?:###\s+(?:\d+(?:\.\d+)*\.?\s+)?)?(?:\*\*)?(?:Proof(?:\s+of\b|\s*[.:]|\s+[A-Z]|\s*$)|证明\s*(?:[.:：]|$|[\u4e00-\u9fa5]))",
                    s,
                ):
                    start_ln = i + 1
                    start_pg = cur_page
                    blk = [s]
                    j = i + 1
                    while j < len(lines):
                        sj = lines[j].strip()
                        mp2 = re.match(r"^<!--\s*PDF\s+p\.(\d+)/(\d+)\s*-->$", sj)
                        if mp2:
                            cur_page = int(mp2.group(1))
                            j += 1
                            continue
                        if sj.startswith("## [Page "):
                            j += 1
                            continue
                        if STOP_FOR_PROOF.match(sj) or (
                            j > i + 1
                            and re.match(r"^(?:###\s+(?:\d+(?:\.\d+)*\.?\s+)?)?(?:Proof\s+of\b|Proof\s*[.:]|证明\s*[.:：])", sj)
                        ):
                            break
                        if sj:
                            blk.append(sj)
                        elif blk and blk[-1] != "":
                            blk.append("")
                        if len(blk) > 110:
                            break
                        j += 1
                    text_blk = "\n".join(blk).strip()
                    flat = norm_one_line(text_blk)
                    proofs.append(
                        {
                            "doc_id": doc_id,
                            "page": start_pg,
                            "line": start_ln,
                            "text": text_blk,
                            "flat": flat,
                            "types": classify_proof_type(flat),
                            "closer": classify_proof_closer(flat),
                        }
                    )
                    i = j
                    continue
            i += 1

    # Also harvest Volume I (2026 Springer monograph) landmarks and proofs if available
    if DEFAULT_VOL1_DB.is_file():
        def _clean_vol1_dots(s: str) -> str:
            s = s.replace("\ufb01", "fi").replace("\ufb02", "fl").replace("\ufb00", "ff")
            s = re.sub(r"^\.\s*", "", s)
            s = re.sub(r"(?<=\s)\.\s*(?=[A-Za-z0-9α-ωΑ-Ω(\[¯ˆ˜˙¨‖])", "", s)
            s = re.sub(r"(?<=[a-z])\.(?=[a-zA-Z(])", " ", s)
            return s

        vconn = sqlite3.connect(f"file:{DEFAULT_VOL1_DB}?mode=ro", uri=True)
        v_pages = vconn.execute("SELECT pdf_page, printed_page, chapter, text FROM pages ORDER BY pdf_page").fetchall()
        page_text_map = {pdf_p: txt for pdf_p, _, _, txt in v_pages}
        full_vol1_lines = []
        for pdf_p, pr_p, chap, txt in v_pages:
            for ln in txt.splitlines():
                full_vol1_lines.append((pdf_p, pr_p or pdf_p, _clean_vol1_dots(ln.strip())))

        for kind, label, pdf_p, pr_p, chap, stmt in vconn.execute(
            "SELECT kind, label, pdf_page, printed_page, chapter, statement_start FROM landmarks"
        ):
            # Reconstruct full untruncated block from pages table (spanning pdf_p and pdf_p+1)
            combined_txt = page_text_map.get(pdf_p, "") + "\n" + page_text_map.get(pdf_p + 1, "")
            c_lns = [_clean_vol1_dots(x.strip()) for x in combined_txt.splitlines()]
            lbl_norm = label.replace("\ufb01", "fi")
            s_idx = next((idx for idx, x in enumerate(c_lns) if x.startswith(lbl_norm)), None)
            if s_idx is not None:
                v_env_blk = [c_lns[s_idx]]
                for k_i in range(s_idx + 1, min(len(c_lns), s_idx + 45)):
                    vk = c_lns[k_i]
                    if not vk or re.fullmatch(r"\d{1,3}", vk) or vk.startswith("Chapter ") or "Models of Global FASs" in vk or "Robust Stabilization of Type I" in vk or "Control of FASs" in vk:
                        continue
                    if re.match(r"^(?:Theorem|Lemma|Proposition|Corollary|Definition|Assumption|Remark|Problem|Proof)\b", vk):
                        break
                    if kind == "Definition" and DEF_POST_PROSE_STOP_RE.match(vk):
                        joined_v = " ".join(v_env_blk)
                        if v_env_blk[-1].endswith(".") and any(w in joined_v for w in ("called", "said to be", "belong to class", "fixed")):
                            break
                    v_env_blk.append(vk)
                full_stmt = "\n".join(v_env_blk).strip()
            else:
                full_stmt = _clean_vol1_dots(stmt)
            buckets[kind].append(
                {
                    "doc_id": "book_2026_volume1",
                    "page": pdf_p,
                    "line": pr_p or pdf_p,
                    "text": full_stmt,
                    "flat": norm_one_line(full_stmt),
                }
            )
        vi = 0
        while vi < len(full_vol1_lines):
            pdf_p, pr_p, vs = full_vol1_lines[vi]
            if (
                re.match(r"^Proof(?:\s+of\s+(?:Theorem|Lemma|Proposition|Corollary)\s+[0-9A-Z.]+|\s+[A-Z]|\s*$)", vs)
                and not vs.startswith(("Proofs of", "Proof is", "Proof that"))
            ):
                vblk = [vs]
                vj = vi + 1
                while vj < len(full_vol1_lines) and len(vblk) < 95:
                    _, _, vsj = full_vol1_lines[vj]
                    if re.match(
                        r"^(?:Theorem|Lemma|Proposition|Corollary|Definition|Assumption|Remark|Problem|Chapter|Appendix)\s+[0-9A-Z]",
                        vsj,
                    ) or re.match(r"^Proof(?:\s+of\b|\s+[A-Z])", vsj):
                        break
                    if vsj:
                        vblk.append(vsj)
                    vj += 1
                vtxt = "\n".join(vblk).strip()
                vflat = norm_one_line(vtxt)
                proofs.append(
                    {
                        "doc_id": "book_2026_volume1",
                        "page": pdf_p,
                        "line": pr_p,
                        "text": vtxt,
                        "flat": vflat,
                        "types": classify_proof_type(vflat),
                        "closer": classify_proof_closer(vflat),
                    }
                )
                vi = vj
                continue
            vi += 1
        vconn.close()

    # Save sorted Markdown banks in ~/.cache/duan-hofas/corpus/sorted/
    PLURALS = {"Corollary": "corollaries"}
    for kind, items in sorted(buckets.items()):
        out = [f"# Sorted {kind} Corpus Across 32 Duan First-Author Papers + Volume I ({len(items)} items)\n"]
        for idx, it in enumerate(items, 1):
            out.append(f"## [{idx}] `{it['doc_id']}` (PDF p.{it['page']}, L{it['line']})\n\n{it['text']}\n")
        fname = PLURALS.get(kind, f"{kind.lower()}s") + ".md"
        (sorted_dir / fname).write_text("\n".join(out), encoding="utf-8")

    out_p = [f"# Sorted Proof Corpus Across 32 Duan First-Author Papers ({len(proofs)} items)\n"]
    for idx, it in enumerate(proofs, 1):
        t_str = ", ".join(it["types"])
        out_p.append(
            f"## [{idx}] `{it['doc_id']}` (PDF p.{it['page']}, L{it['line']}) | Types: `{t_str}` | Closer: `{it['closer']}`\n\n{it['text']}\n"
        )
    (sorted_dir / "proofs.md").write_text("\n".join(out_p), encoding="utf-8")

    # Compute summary statistics
    thm_openings = Counter(classify_theorem_opening(it["flat"]) for it in buckets["Theorem"])
    lem_openings = Counter(classify_theorem_opening(it["flat"].replace("Lemma", "Theorem", 1).replace("引理", "定理", 1)) for it in buckets["Lemma"])
    prop_openings = Counter(classify_theorem_opening(it["flat"].replace("Proposition", "Theorem", 1).replace("命题", "定理", 1)) for it in buckets["Proposition"])
    cor_openings = Counter(classify_theorem_opening(it["flat"].replace("Corollary", "Theorem", 1).replace("推论", "定理", 1)) for it in buckets["Corollary"])

    thm_numbered_items = sum(1 for it in buckets["Theorem"] if re.search(r"(?:\b1\)|\(1\)|\b1\.\s)", it["flat"]))
    proof_types_cnt = Counter(t for it in proofs for t in it["types"])
    proof_closers_cnt = Counter(it["closer"] for it in proofs)

    stats = {
        "counts_32_papers": {k: len(v) for k, v in sorted(buckets.items())} | {"Proof": len(proofs)},
        "theorem_openings": dict(thm_openings.most_common()),
        "theorem_numbered_conclusions": f"{thm_numbered_items}/{len(buckets['Theorem'])}",
        "lemma_openings": dict(lem_openings.most_common()),
        "proposition_openings": dict(prop_openings.most_common()),
        "corollary_openings": dict(cor_openings.most_common()),
        "proof_types": dict(proof_types_cnt.most_common()),
        "proof_closers": dict(proof_closers_cnt.most_common()),
    }
    (sorted_dir / "summary_stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build a clean, verified thematic bank of Duan's classic definitions (formal Definition environments + unnumbered prose/theorem definitions)."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

DEFAULT_CORPUS_DIR = Path("/home/yzk/.cache/duan-hofas/corpus")

TOPICS = [
    ("T1_fas_subfas_models", "1. 高阶全驱系统（Global FAS）与亚全驱系统（sub-FAS）基础定义"),
    ("T2_singular_feasible_sets", "2. 奇异点、奇异集与可行点、可行集（Singular & Feasible Points/Sets）"),
    ("T3_singularity_functions_types", "3. 奇异函数（φ₀, φ_∞, φ）与奇异类型分类（0/∞/Mixed & Rational/Critical/Irrational）"),
    ("T4_substability_roea", "4. 亚稳定性（Substability）、亚镇定与指数吸引域（ROEA / RoEA / REA）"),
    ("T5_controllability_observability_types", "5. 能控/能观/平坦输出、Type I/II 系统与非线性稳定性预备定义"),
    ("T6_subsfs_chained_ucfas", "6. 亚严反馈（sub-SFS）、广义链式（Sub-normal）与单向连接全驱系统（UC-FAS）"),
    ("T7_odfas_output_feedback", "7. 输出依赖全驱系统（OD-FAS / sub-OD-FAS）与输出反馈 RoEA"),
    ("T8_discrete_and_delay", "8. 离散时间（前进步/后退步、可行轨迹集）与时滞全驱/亚全驱系统"),
]


def classify_topic(doc_id: str, lbl: str, flat: str) -> str:
    fl = flat.lower()
    # Explicit overrides for exact precision
    if doc_id == "aas_2020_part2" and lbl.startswith("定义 1"):
        return "T1_fas_subfas_models"
    if doc_id == "aaas_2024_subsfs":
        if any(lbl.startswith(x) for x in ("定义 1", "定义 2")):
            return "T6_subsfs_chained_ucfas"
        if any(lbl.startswith(x) for x in ("定义 3", "定义 4", "定义 7")):
            return "T3_singularity_functions_types"
        if lbl.startswith("定义 5"):
            return "T2_singular_feasible_sets"
        if lbl.startswith("定义 6"):
            return "T1_fas_subfas_models"
        if lbl.startswith("定义 8"):
            return "T4_substability_roea"
    if doc_id == "tcyb_2024_overview":
        if lbl in ("Definition 1",):
            return "T1_fas_subfas_models"
        if lbl in ("Definition 2", "Definition 10"):
            return "T3_singularity_functions_types"
        if lbl in ("Definition 3", "Definition 4", "Definition 5", "Definition 6", "Definition 7"):
            return "T5_controllability_observability_types"
        if lbl in ("Definition 8", "Definition 9"):
            return "T6_subsfs_chained_ucfas"
    if doc_id == "odfas_2026_part4":
        if lbl.startswith("Definition 2.1"):
            return "T7_odfas_output_feedback"
        return "T5_controllability_observability_types"
    if doc_id in ("odfas_2026_part1", "odfas_2026_part2"):
        return "T7_odfas_output_feedback"
    if doc_id.startswith("ucfas_"):
        return "T6_subsfs_chained_ucfas"
    if doc_id in ("tcyb_2023_robustdelay", "book_2026_volume1"):
        if any(k in fl for k in ("class k", "k∞-bounded", "input-to-state stable", "finite-time stability", "feedback lineariz", "controllability indices", "equivalent")):
            return "T5_controllability_observability_types"
        if "pmd" in fl or "fully actuated" in fl:
            return "T1_fas_subfas_models"
    if doc_id in ("ijss_2022_part10", "scis_2022_discdelay1", "scis_2022_discdelay2", "scis_2023_delay1", "scis_2023_delay2"):
        return "T8_discrete_and_delay"
    if doc_id in ("scis_2024_chained1", "scis_2024_chained2", "scis_2025_chained3"):
        return "T6_subsfs_chained_ucfas"
    if any(k in fl for k in ("function of normal singularity", "function of abnormal singularity", "function of singularity", "0-type", "∞-type", "mixed-type", "rational sub-fas", "critically rational", "critical rational")):
        return "T3_singularity_functions_types"
    if any(k in fl for k in ("substable", "substabilizable", "substability", "roea", "region of exponential attraction")):
        return "T4_substability_roea"
    if any(k in fl for k in ("controllab", "observab", "type i", "type ii", "stabilisable", "coprime", "mfd", "能控", "能观", "全量测")):
        return "T5_controllability_observability_types"
    if any(k in fl for k in ("singular point", "singular set", "feasible point", "feasible set", "set of singularity", "set of feasibility", "feasibility set")):
        if "called (global) hofa" in fl or "called fully actuated" in fl or "globally fully actuated" in fl:
            return "T1_fas_subfas_models"
        return "T2_singular_feasible_sets"
    return "T1_fas_subfas_models"


def extract_prose_window(papers_dir: Path, doc_id: str, start_needle: str, end_needle: str, label: str, topic_key: str) -> dict:
    md_path = papers_dir / f"{doc_id}.md"
    lines = md_path.read_text(encoding="utf-8").splitlines()
    cur_page = 1
    s_idx = None
    s_page = 1
    for idx, ln in enumerate(lines):
        mp = re.match(r"^<!--\s*PDF\s+p\.(\d+)/(\d+)\s*-->$", ln.strip())
        if mp:
            cur_page = int(mp.group(1))
        if s_idx is None and start_needle in ln:
            s_idx = idx
            s_page = cur_page
            break
    if s_idx is None:
        raise ValueError(f"Start needle not found in {doc_id}: {start_needle}")
    out = []
    for j in range(s_idx, min(len(lines), s_idx + 45)):
        sj = lines[j].strip()
        if j > s_idx and end_needle and end_needle in sj:
            break
        if re.match(r"^<!--\s*PDF\s+p\.\d+/\d+\s*-->$", sj) or sj.startswith("## [Page "):
            continue
        if sj or (out and out[-1] != ""):
            out.append(sj)
    text = "\n".join(out).strip()
    return {
        "kind": "Prose/Theorem-Embedded Definition",
        "label": label,
        "doc_id": doc_id,
        "page": s_page,
        "line": s_idx + 1,
        "topic": topic_key,
        "text": text,
    }


def main() -> None:
    papers_dir = DEFAULT_CORPUS_DIR / "papers"
    sorted_dir = DEFAULT_CORPUS_DIR / "sorted"
    defs_md = sorted_dir / "definitions.md"
    if not defs_md.is_file():
        raise FileNotFoundError(f"Run sort_corpus_environments.py first: {defs_md}")

    raw_defs = defs_md.read_text(encoding="utf-8")
    chunks = re.split(r"^## \[(\d+)\]\s+`([^`]+)`\s+\(PDF p\.(\d+),\s+L(\d+)\)\s*$", raw_defs, flags=re.M)
    items: list[dict] = []
    for k in range(1, len(chunks), 5):
        _, doc_id, pno, lno, body = chunks[k : k + 5]
        body_clean = body.strip()
        first_ln = body_clean.splitlines()[0] if body_clean else "Definition"
        m_lbl = re.match(r"^((?:Definition|定义)\s*[A-Za-z0-9.\-′'’]*)", first_ln)
        lbl = m_lbl.group(1).strip().rstrip(".:：") if m_lbl else first_ln[:32]
        flat = re.sub(r"\s+", " ", body_clean)
        tkey = classify_topic(doc_id, lbl, flat)
        items.append(
            {
                "kind": "Formal Definition",
                "label": lbl,
                "doc_id": doc_id,
                "page": int(pno),
                "line": int(lno),
                "topic": tkey,
                "text": body_clean,
            }
        )

    prose_specs = [
        (
            "tcyb_2023_subfas",
            "1) Singular Sets of Sub-FASs: Regarding the sub-FAS (18)",
            "**Definition 3:",
            "§III-B1 Singular Set, Normal/Abnormal Singular Sets & Feasible Set (Prose)",
            "T2_singular_feasible_sets",
        ),
        (
            "tcyb_2023_subfas",
            "Furthermore, with the above notations, the feasible set",
            "Example 3:",
            "§III-B2 Zero-Product Expression of Feasible Set 𝔽 (Prose)",
            "T2_singular_feasible_sets",
        ),
        (
            "tcyb_2023_subfas",
            "Of course, we can also define the function of singularity",
            "C. Generality of FASs",
            "§III-B2 Overall Function of Singularity φ(X, t) (Prose)",
            "T3_singularity_functions_types",
        ),
        (
            "tcyb_2023_subfas",
            "**Theorem 1: Let 𝔽 ⊂ ℝm",
            "Proof: The first two conclusions",
            "Theorem 1(3) Single-Order Sub-FAS ROEA R_s Definition (Theorem-Embedded)",
            "T4_substability_roea",
        ),
        (
            "tcyb_2023_subfas",
            "**Theorem 3: Let AE",
            "Obviously, when AE is particularly chosen",
            "Theorem 3 Multi-Order Sub-FAS ROEA R_m Definition (Theorem-Embedded)",
            "T4_substability_roea",
        ),
        (
            "tcyb_2024_overview",
            "B. Sets of Singularity and Feasibility",
            "**Definition 1:",
            "§II-B Sets of Singularity/Feasibility & Singular/Feasible Points (Prose)",
            "T2_singular_feasible_sets",
        ),
        (
            "tcyb_2024_overview",
            "Regarding the sub-FAS (2), let us divide its set of singularity",
            "**Definition 2:",
            "§II-B Division into Normal and Abnormal Singular Sets (Prose)",
            "T2_singular_feasible_sets",
        ),
        (
            "ijss_2021_part7",
            "Let 𝕊 be the set of all singular points of system (8)",
            "Based on the above notations",
            "§2.2 Eq. (14)–(15) Set of Singular Points 𝕊 & Set of Feasible Points 𝔽 (Prose)",
            "T2_singular_feasible_sets",
        ),
        (
            "ijss_2022_part8",
            "Let 𝕊t be the set of all singular points of system (1)",
            "### 5.2. Optimal output regulation",
            "§5.1 Time-Indexed Singular/Feasible Sets 𝕊_t, 𝕊_0, 𝔽_t, 𝔽_0 (Prose)",
            "T2_singular_feasible_sets",
        ),
        (
            "ijss_2024_underactuated4",
            "Otherwise, a sub-FAS with a feasible set is produced",
            "### 1. Introduction",
            "Abstract Region of Exponential Attraction (REA) Introduction (Prose)",
            "T4_substability_roea",
        ),
        (
            "ucfas_2025_part2",
            "Define the feasibility set of the single-order FAS (1) as",
            "Noting that the state-space form",
            "§2.1 Eq. (5) Internal Feasibility Set 𝔽^in & Controller on 𝔽^in (Prose)",
            "T6_subsfs_chained_ucfas",
        ),
        (
            "ucfas_2025_part2",
            "Denoting X0 ≜ x(0∼n−1)(0), we have the following",
            "**Definition 2.2:",
            "§2.1 Eq. (13)–(14) Internal and External RoEAs R^in & R^ex (Prose)",
            "T6_subsfs_chained_ucfas",
        ),
        (
            "odfas_2026_part1",
            "Convention C1 For simplicity",
            "**Proposition 2.1.",
            "§2.1 Convention C1 Output-Dependent Shorthand f_y(·, t), B(·, t) (Prose)",
            "T7_odfas_output_feedback",
        ),
        (
            "odfas_2026_part1",
            "Further denote",
            "### 4.3. A Benchmark Example",
            "§4.2 Dynamic Output-Feedback Augmented-State RoEA R & Theorem 4.2 (Prose + Theorem)",
            "T7_odfas_output_feedback",
        ),
        (
            "fasta_2026_roea",
            "To characterize the feasible set of the system initial value",
            "### 2.2 Internal feasibility conditions",
            "§2.1 Eq. (5)–(6) Initial-Value RoEA Decomposition R = R₁ ∩ R₂ (Prose)",
            "T4_substability_roea",
        ),
    ]

    prose_items: list[dict] = []
    for doc_id, s_ndl, e_ndl, lbl, tkey in prose_specs:
        prose_items.append(extract_prose_window(papers_dir, doc_id, s_ndl, e_ndl, lbl, tkey))

    grouped: dict[str, list[dict]] = defaultdict(list)
    for it in items + prose_items:
        grouped[it["topic"]].append(it)

    out_lines = [
        f"# Duan 全集经典定义主题原文库（{len(items)} 条正式 `Definition` + {len(prose_items)} 处正文/定理内核心定义 = {len(items) + len(prose_items)} 条）",
        "",
        "- **覆盖范围**：32 篇段广仁一作中英文论文 + 2026 年 Springer 专著 *Volume I* 全部正式 `Definition` 环境 + 正文/定理内无编号核心概念定义。",
        "- **用途**：核查段广仁逐字原话、区分“正式编号 `Definition` 环境”与“正文直接引入记号”、按概念主题直接调取原文。",
        "",
        "## 主题统计总览",
        "",
        "| 主题 | 正式 `Definition` 数 | 正文/定理内定义数 | 合计 |",
        "|---|---:|---:|---:|",
    ]
    for tkey, ttitle in TOPICS:
        grp = grouped[tkey]
        n_f = sum(1 for x in grp if x["kind"] == "Formal Definition")
        n_p = sum(1 for x in grp if x["kind"] != "Formal Definition")
        out_lines.append(f"| {ttitle} | {n_f} | {n_p} | {len(grp)} |")
    out_lines.append(f"| **合计** | **{len(items)}** | **{len(prose_items)}** | **{len(items) + len(prose_items)}** |")
    out_lines.append("")

    global_counter = 1
    for tkey, ttitle in TOPICS:
        out_lines.append("---")
        out_lines.append("")
        out_lines.append(f"## {ttitle}")
        out_lines.append("")
        for it in sorted(grouped[tkey], key=lambda x: (x["doc_id"], x["page"], x["line"])):
            tag = "Formal" if it["kind"] == "Formal Definition" else "Prose/Theorem"
            loc = f"PDF p.{it['page']}, L{it['line']}"
            out_lines.append(f"### [{global_counter}] `{it['doc_id']}` — {it['label']} ({tag} | {loc})")
            out_lines.append("")
            out_lines.append(it["text"])
            out_lines.append("")
            global_counter += 1

    target_md = sorted_dir / "classic_definitions_by_topic.md"
    target_md.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Wrote {len(items)} formal + {len(prose_items)} prose = {len(items) + len(prose_items)} classic definitions to {target_md}")


if __name__ == "__main__":
    main()

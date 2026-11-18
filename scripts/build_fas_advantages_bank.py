#!/usr/bin/env python3
"""Harvest, clean, and categorize all passages describing the advantages, method comparisons, and objective boundaries of the FAS approach across the 32-paper corpus + Volume I."""

from __future__ import annotations

import re
import sqlite3
from collections import defaultdict
from pathlib import Path

DEFAULT_CORPUS_DIR = Path("/home/yzk/.cache/duan-hofas/corpus")
DEFAULT_VOL1_DB = Path("/home/yzk/.cache/duan-hofas/volume1.sqlite")

THEMES = [
    ("D1_modeling_philosophy", "1. 建模哲学：面向响应的一阶状态空间法 vs 面向控制的高阶全驱法（增元降阶 vs 消元升阶）"),
    ("D2_lti_closedloop_dofs", "2. 定常线性闭环与完整特征结构参数化设计自由度（LTI Closed-Loop & Parametric DOFs）"),
    ("D3_vs_backstepping", "3. 对比经典反步法：克服“微分爆炸 / 复杂性爆炸”与多阶严反馈归约"),
    ("D4_vs_feedback_linearization_subfas", "4. 对比反馈线性化并延伸至亚全驱（sub-FAS）、奇异陷阱与非完整临界有理系统"),
    ("D5_controllability_observability", "5. 高阶能控性、能观性与控制器显式求解的统一（突破 Kalman 线性状态空间局限）"),
    ("D6_disturbance_delay_ucfas_odfas", "6. 天然抗扰、时变/输入时滞超前对消、单向连接（UC-FAS）与输出依赖输出反馈（OD-FAS）"),
    ("D7_objective_boundaries", "7. 客观适用边界与防夸大红线表述（肯定状态空间滤波/观测优势，区分更好求解 vs 求解新问题）"),
]

NOISE_PREFIXES = (
    "This work is supported by",
    "G. R. Duan is with",
    "shenzhen",
    "KQTD",
    "CONTACT Guang-Ren Duan",
    "Technology, Harbin, People",
    "收稿日期",
    "Manuscript received",
    "国家自然科学",
    "基金 (",
    "Supported by",
    "Foundation of China",
    "段广仁: 高阶系统方法",
)


def _clean_vol1(txt: str) -> str:
    txt = txt.replace("\ufb01", "fi").replace("\ufb02", "fl").replace("\ufb00", "ff")
    out = []
    for ln in txt.splitlines():
        s = ln.strip()
        if not s or re.fullmatch(r"\d{1,3}", s):
            continue
        if re.match(
            r"^(?:\d{1,3}\s{2,}\d+(?:\.\d+)*\s+.+|\d+(?:\.\d+)*\s+.+\s{2,}\d{1,3}|Preface\s+[ivx]+|Fig\.\s*\d+\.\d+\s+.+)$",
            s,
        ):
            continue
        s = re.sub(r"^\.\s*", "", s)
        s = re.sub(r"(?<=\s)\.\s*(?=[A-Za-z0-9α-ωΑ-Ω∞(\[])", "", s)
        out.append(s)
    return "\n".join(out).strip()


def extract_md_window(
    papers_dir: Path,
    doc_id: str,
    start_ndl: str,
    end_ndl: str,
    title: str,
    theme: str,
    trim_lead: str = "",
) -> dict:
    md_path = papers_dir / f"{doc_id}.md"
    lines = md_path.read_text(encoding="utf-8").splitlines()
    cur_p = 1
    s_idx = None
    s_p = 1
    for i, ln in enumerate(lines):
        mp = re.match(r"^<!--\s*PDF\s+p\.(\d+)/(\d+)\s*-->$", ln.strip())
        if mp:
            cur_p = int(mp.group(1))
        if s_idx is None and start_ndl in ln:
            s_idx = i
            s_p = cur_p
            break
    if s_idx is None:
        raise ValueError(f"Needle not found in {doc_id}: {start_ndl}")
    buf = []
    skipped_noise = False
    for j in range(s_idx, min(len(lines), s_idx + 85)):
        sj = lines[j].strip()
        if j > s_idx and end_ndl and end_ndl in sj:
            break
        if re.match(r"^<!--\s*PDF\s+p\.\d+/\d+\s*-->$", sj) or sj.startswith("## [Page "):
            skipped_noise = True
            continue
        if re.match(r"^(?:46\s*卷|7\s*期|8\s*期|9\s*期|Fig\.\s*\d+\.|###\s+\d+\s+DUAN\s+GUANG-REN)", sj):
            skipped_noise = True
            continue
        if sj.startswith(NOISE_PREFIXES):
            skipped_noise = True
            continue
        if not sj and skipped_noise:
            continue
        skipped_noise = False
        # Clean inline bold markers injected by landmark detector
        sj = sj.replace("**", "")
        if sj == "### 2 可见, 控制系统的高阶全驱模型则为求解控制问":
            sj = "2 可见, 控制系统的高阶全驱模型则为求解控制问"
        if doc_id == "odfas_2026_part1" and "Convert system (100) into state-space form" in sj:
            sj = sj.replace(" Convert system (100) into state-space form", "")
        if j == s_idx and trim_lead and sj.startswith(trim_lead):
            sj = sj[len(trim_lead):].lstrip()
        if sj or (buf and buf[-1] != ""):
            buf.append(sj)
    return {
        "doc_id": doc_id,
        "page": s_p,
        "line": s_idx + 1,
        "title": title,
        "theme": theme,
        "text": "\n".join(buf).strip(),
    }


def extract_vol1_window(vconn: sqlite3.Connection, pdf_p: int, start_ndl: str, end_ndl: str, title: str, theme: str) -> dict:
    rows = vconn.execute(
        "SELECT pdf_page, printed_page, text FROM pages WHERE pdf_page IN (?, ?, ?) ORDER BY pdf_page",
        (pdf_p, pdf_p + 1, pdf_p + 2),
    ).fetchall()
    combined = "\n".join(_clean_vol1(r[2]) for r in rows)
    pr_p = rows[0][1] or pdf_p
    lns = combined.splitlines()
    s_i = next((i for i, x in enumerate(lns) if start_ndl in x), None)
    if s_i is None:
        raise ValueError(f"Needle not found in Volume I PDF p.{pdf_p}: {start_ndl}")
    buf = []
    for j in range(s_i, min(len(lns), s_i + 85)):
        if j > s_i and end_ndl and end_ndl in lns[j]:
            break
        buf.append(lns[j])
    return {
        "doc_id": "book_2026_volume1",
        "page": pdf_p,
        "line": pr_p,
        "title": title,
        "theme": theme,
        "text": "\n".join(buf).strip(),
    }


def main() -> None:
    papers_dir = DEFAULT_CORPUS_DIR / "papers"
    sorted_dir = DEFAULT_CORPUS_DIR / "sorted"
    sorted_dir.mkdir(parents=True, exist_ok=True)

    md_specs = [
        # D1: Modeling philosophy (State-space vs FAS, variable extension vs elimination)
        ("aas_2020_part1", "### 1.2 利与弊", "本文中采用了下述一些记号", "§1.2 一阶系统方法的利与弊及高阶全驱出发点", "D1_modeling_philosophy", ""),
        ("aas_2020_part1", "定理 2 和 3 说明", "4 参数化设计方法", "§3 反对先化一阶再转高阶（“画蛇添足”论断）", "D1_modeling_philosophy", ""),
        ("aas_2020_part1", "从而丧失了本有的全驱性", "由命题 1 可见", "§4 物理定律天然二阶全驱性与一阶降阶局限", "D1_modeling_philosophy", ""),
        ("aaas_2024_subsfs", "值得注意的是，在严反馈系统的研究中", "作为高阶全驱系统方法的推广应用", "§1 一阶状态空间方法在控制律求解上的束缚", "D1_modeling_philosophy", ""),
        ("tcyb_2024_overview", "A. The State-Space Approach", "B. The Fully Actuated System Approach", "§I-A State-Space Approach Origin & Control Bottlenecks", "D1_modeling_philosophy", ""),
        ("tcyb_2024_overview", "B. The Fully Actuated System Approach", "The purpose of this paper", "§I-B Explicit Control Solvability & Birth of the FAS Approach", "D1_modeling_philosophy", ""),
        ("tcyb_2024_overview", "D. FAS Models vs State-Space Models", "### III. EXISTENCE OF FASS", "§II-D & Table I Comparison of Two Extreme Dynamical Models", "D1_modeling_philosophy", ""),
        ("tcyb_2024_overview", "**Remark 1:", "D. FAS Models vs State-Space Models", "Remark 1 From Mechanical FASs to General Dynamical Models", "D1_modeling_philosophy", ""),
        ("ijss_2021_part5", "**Remark 2.1:", "**Remark 2.2:", "Remark 2.1 Generality of HOFA Models Beyond Mechanical Systems", "D1_modeling_philosophy", ""),
        ("ijss_2024_underactuated4", "**Remark 3.1:", "The treatment in this section requires", "Remark 3.1 Physical vs Mathematical FAS Conversion of UASs", "D1_modeling_philosophy", ""),
        ("tcyb_2023_subfas", "C. Generality of FASs", "### IV.", "§III-C Generality of Single- and Multi-Order FASs", "D1_modeling_philosophy", ""),
        # D2: LTI closed-loop & complete parametric DOFs
        ("tcyb_2024_overview", "**Remark 4:", "E. A Basic Procedure", "Remark 4 Wide Scope Reduced to a Single Eigenstructure Assignment Pair", "D2_lti_closedloop_dofs", ""),
        ("ijss_2021_part1", "**Remark 3.2:", "To end this section, we give", "Remark 3.2 Complete Parametric Freedom in Closed-Loop Matrix F", "D2_lti_closedloop_dofs", ""),
        ("ijss_2021_part7", "**Remark 5.1:", "### 6. Examples", "Remark 5.1 Decoupled Simplicity vs Coupled Parametric DOFs", "D2_lti_closedloop_dofs", ""),
        ("ijss_2022_part8", "**Remark 4.3:", "### 5.", "Remark 4.3 Global Stabilization & Infinite-Horizon Optimal Control via FAS", "D2_lti_closedloop_dofs", ""),
        ("ijss_2022_part9", "**Remark 3.1:", "### 3.3. Decoupled design", "Remark 3.1 Generalized PID Advantages & Parametric Tracking", "D2_lti_closedloop_dofs", ""),
        ("ijss_2022_part10", "**Remark 5.2:", "**Remark 5.3:", "Remark 5.2 Decoupled and Decentralized Structure of Discrete FAS Control", "D2_lti_closedloop_dofs", ""),
        ("scis_2022_discdelay1", "**Remark 2.", "### 5.2 FASs with input delays", "Remarks 2–3 Decentralized Design & Complete Parameterization for Delay FAS", "D2_lti_closedloop_dofs", ""),
        # D3: Comparison with Backstepping (avoiding differential explosion + LTI closed loop)
        ("aas_2020_part1", "**说明 1.", "### 3.4 可反馈线性化的系统", "说明 1 对比反步法与滑模控制（非线性闭环 vs 定常线性闭环）", "D3_vs_backstepping", ""),
        ("aaas_2024_subsfs", "**说明 由本节结果可见", "### 4", "说明 对比传统反步法的三大优势（无微分爆炸、普适亚严反馈、线性闭环）", "D3_vs_backstepping", ""),
        ("ijss_2021_part1", "**Remark 4.2:", "### 5.", "Remark 4.2 Applicability Beyond Triangular Strict-Feedback Structure", "D3_vs_backstepping", ""),
        ("ijss_2021_part2", "**Remark 2.3:", "**Remark 2.4:", "Remark 2.3 Two Core Advantages of HOFA Over Backstepping", "D3_vs_backstepping", ""),
        ("ijss_2021_part3", "**Remark 5.3:", "### 6.", "Remarks 5.3–5.4 Why High-Order Backstepping Needs Fewer Steps Than First-Order", "D3_vs_backstepping", ""),
        ("ijss_2021_part3", "**Remark 6.1:", "### 6.2", "Remark 6.1 4-Step First-Order Backstepping vs Direct High-Order Design", "D3_vs_backstepping", ""),
        ("ijss_2021_part4", "**Remark 5.2:", "### 6.", "Remark 5.2 Avoiding Differential Explosion in Adaptive High-Order Backstepping", "D3_vs_backstepping", ""),
        ("ucfas_2025_part1", "**Remark 6.2:", "### 7. Conclusion", "Remarks 6.2–6.3 Avoiding Doubled Layers & Differential Explosion in SFSs", "D3_vs_backstepping", ""),
        ("scis_2024_chained2", "**Remark 3.", "### 4", "Remark 3 FAS vs Backstepping on Generalized Chained Systems", "D3_vs_backstepping", ""),
        # D4: Comparison with Feedback Linearization & extension to sub-FAS / nonholonomic
        ("tcyb_2024_overview", "**Remark 2:", "C. Strict-Feedback Systems", "Remark 2 Why FAS Approach Is Much More Than Feedback Linearization", "D4_vs_feedback_linearization_subfas", ""),
        ("tcyb_2023_subfas", "the FAS approach. More specifically, for nonlinear", "For completeness, the control", "§I Motivation of Sub-FAS & Substabilization for Non-Linearizable Systems", "D4_vs_feedback_linearization_subfas", "the FAS approach."),
        ("jssc_2022_casestudy", "**Remark 2.3", "### 3 Sub-Stabilization", "Remark 2.3 Sub-FAS Handling Singular Sets Passing Through the Origin", "D4_vs_feedback_linearization_subfas", ""),
        ("jssc_2022_casestudy", "**Remark 3.3", "### 4 Global Stabilization", "Remark 3.3 Overcoming Smooth Feedback-Linearization Obstruction on Irregular Feasible Set", "D4_vs_feedback_linearization_subfas", ""),
        ("scis_2024_chained1", "When the initial values are inevitably chosen", "### 7 Extension to time-delay systems", "§6.2 Pre-Controller Ease, Nonholonomic Systems as Sub-FASs & State/Derivative Constraints", "D4_vs_feedback_linearization_subfas", ""),
        # D5: Controllability & Observability unified with explicit control
        ("aas_2020_part2", "Abstract In this paper, development in controllability", "Key words", "Abstract Critique of Kalman State-Space Controllability & FAS Necessary/Sufficient Criterion", "D5_controllability_observability", ""),
        ("aas_2020_part2", "**说明 2.", "现在考虑含有两个附加项", "说明 2–3 以控制变量为核心的全驱能控性及高阶导数可测性等价", "D5_controllability_observability", ""),
        ("ijss_2021_part7", "Definition 3 in Duan (2020b)", "Now let us consider again", "§3.2 Consistency Between Controllability Verification and Control Design", "D5_controllability_observability", "Definition 3 in Duan (2020b) as a special case."),
        ("scis_2023_delay1", "**Remark 4.", "Like controllability, stabilizability", "Remark 4 Extending Controllability Beyond State-Space Representations", "D5_controllability_observability", ""),
        # D6: Natural anti-disturbance, time-delay cancellation, UC-FAS & OD-FAS
        ("ijss_2021_part6", "**Remark 2.1:", "### 2.3. HOFA models", "Remark 2.1 Natural Anti-Disturbance Property of HOFA Controllers", "D6_disturbance_delay_ucfas_odfas", ""),
        ("ijss_2021_part6", "**Remark 4.1:", "### 4.3. Case of dynamical", "Remark 4.1 Complete Parametric Freedom in Disturbance Decoupling", "D6_disturbance_delay_ucfas_odfas", ""),
        ("tcyb_2023_robustdelay", "**Remark 1:", "B. Type I Systems", "Remark 1 Generality of Time-Delay FAS Models", "D6_disturbance_delay_ucfas_odfas", ""),
        ("tcyb_2023_robustdelay", "**Remark 3:", "B. Case of Multiorder FASs", "Remark 3 Dynamic Input-Delay Compensation Within FAS Framework", "D6_disturbance_delay_ucfas_odfas", ""),
        ("ucfas_2025_part3", "features and external constraints. In spite of the fact", "Model 1:", "§1 Extending Beyond Single FAS/sub-FAS via Unidirectionally Connected FASs", "D6_disturbance_delay_ucfas_odfas", "features and external constraints."),
        ("odfas_2026_part1", "**Remark 4.1.", "Under the feasibility condition", "Remark 4.1 Finer Substabilization Perspective on Khalil/Isidori Benchmark System", "D6_disturbance_delay_ucfas_odfas", ""),
        ("odfas_2026_part4", "**Remark 7.1.", "### 8.", "Remark 7.1 Position vs Velocity Output-Feedback Observability & Error Dynamics", "D6_disturbance_delay_ucfas_odfas", ""),
        # D7: Objective boundaries & anti-exaggeration red lines
        ("ijss_2022_part10", "**Remark 5.4:", "**Remark 5.5:", "Remark 5.4 Distinct Roles of State-Space Response Analysis vs FAS Control", "D7_objective_boundaries", ""),
        ("tcyb_2024_overview", "Regarding the above procedure, we have the following", "To conclude this section", "§IV-E Scope Conditions & Necessary Modifications for Uncertainties/Parameters", "D7_objective_boundaries", ""),
    ]

    items: list[dict] = []
    for doc_id, s_ndl, e_ndl, title, theme, trim_lead in md_specs:
        items.append(extract_md_window(papers_dir, doc_id, s_ndl, e_ndl, title, theme, trim_lead))

    if DEFAULT_VOL1_DB.is_file():
        vconn = sqlite3.connect(f"file:{DEFAULT_VOL1_DB}?mode=ro", uri=True)
        vol1_specs = [
            (7, "The present Volume I focuses on global FASs", "Audience", "Preface: Objective Distinction Between Global FAS ('Better Way') and Volumes II–III ('Problems State-Space Cannot Solve') & Delay Superiority", "D7_objective_boundaries"),
            (24, "1.1.2 Deficiencies of the State-Space Approach", "1.1.3 Decline of the State-Space Approach", "§1.1.2 Deficiencies of the State-Space Approach (Response Analysis vs Control Vector)", "D1_modeling_philosophy"),
            (25, "1.1.3 Decline of the State-Space Approach", "1.2 FAS Approach", "§1.1.3 Historical Bottlenecks of First-Order Nonlinear MIMO Control (Casti & Isidori Quotes)", "D1_modeling_philosophy"),
            (27, "Fortunately, besides the state-space models", "Technically and mathematically speaking", "§1.2.1–1.2.2 Eliminating Complicated Nonlinearities & Physical-to-Mathematical HOFAS", "D2_lti_closedloop_dofs"),
            (30, "The FAS approach, owing to its distinct", "In response to the growing", "§1.2.3 Summary of Resolved Nonlinear Control Areas & Extensions", "D6_disturbance_delay_ucfas_odfas"),
            (57, "Both Chaps. 9 and 10 propose high-order backstepping", "Part IV.", "§1.4 Preview: High-Order Backstepping Greatly Reduces Differential Explosion", "D3_vs_backstepping"),
            (227, "Remark 6.4 The proposed FAS approach", "Remark 6.5", "Remark 6.4 Two Core Advantages of FAS Approach Over Backstepping", "D3_vs_backstepping"),
            (251, "Remark 7.2 As pointed out in Duan", "7.1.2 Case of State-Dependent Gains", "Remark 7.2 Canonical Two-Point Summary of FAS Advantages Over Backstepping", "D3_vs_backstepping"),
        ]
        for pdf_p, s_ndl, e_ndl, title, theme in vol1_specs:
            items.append(extract_vol1_window(vconn, pdf_p, s_ndl, e_ndl, title, theme))
        vconn.close()

    grouped: dict[str, list[dict]] = defaultdict(list)
    for it in items:
        grouped[it["theme"]].append(it)

    out = [
        f"# Duan 全集关于 FAS 方法优势、方法对比与客观边界的原文分拣库（共 {len(items)} 段）",
        "",
        "- **覆盖范围**：从 32 篇段广仁一作中英文论文（引言、`R3` 类方法对比 `Remark`、结论）及 2026 专著 *Volume I*（前言、第 1 章 `§1.1–1.2`、第 6–7 章 `Remark 6.4 / 7.2` 等）中逐字提取。",
        "- **核心用途**：撰写英文小论文 `Introduction`、中文博士论文绪论/开题报告、基金申请书以及回复审稿人关于状态空间法 / 反馈线性化 / 反步法的对比质询。",
        "",
        "## 七大维度统计总览",
        "",
        "| 维度 | 原文段落数 |",
        "|---|---:|",
    ]
    for tkey, ttitle in THEMES:
        out.append(f"| {ttitle} | {len(grouped[tkey])} |")
    out.append(f"| **合计** | **{len(items)}** |")
    out.append("")

    g_idx = 1
    for tkey, ttitle in THEMES:
        out.append("---")
        out.append("")
        out.append(f"## {ttitle}")
        out.append("")
        for it in grouped[tkey]:
            loc = f"PDF p.{it['page']}, L{it['line']}"
            out.append(f"### [{g_idx}] `{it['doc_id']}` — {it['title']} ({loc})")
            out.append("")
            out.append(it["text"])
            out.append("")
            g_idx += 1

    target = sorted_dir / "fas_advantages_by_theme.md"
    target.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {len(items)} curated primary-source advantage & boundary passages to {target}")


if __name__ == "__main__":
    main()

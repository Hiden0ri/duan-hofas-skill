#!/usr/bin/env python3
"""Build a copyright-safe catalog of physical backgrounds & simulation examples across primary (36) + backup (3-5 score) FAS papers."""

from __future__ import annotations

import collections
import re
import sqlite3
from pathlib import Path

PRIMARY_PAPERS_DIR = Path("/home/yzk/.cache/duan-hofas/corpus/papers")
BACKUP_DB = Path("/home/yzk/fas-library/fas_library.sqlite")
OUT_CACHE = Path("/home/yzk/.cache/duan-hofas/corpus/sorted/physical_examples_catalog.md")

DOMAINS: list[tuple[str, str, re.Pattern[str]]] = [
    (
        "D1_spacecraft_aerospace",
        "1. 航天器与空天飞行器（姿态 / 交会 / 轨姿一体 / 编队 / 高超声速）",
        re.compile(
            r"\b(?:spacecraft|satellite|rendezvous|space\s+probe|space\s+manipulator|flexible\s+spacecraft|"
            r"hypersonic|missile|reentry|re-entry|launch\s+vehicle|flying\s+vehicle|attitude[- ]orbit|orbit[- ]attitude)\b|"
            r"航天器|卫星|交会|高超声速|飞行器",
            re.I,
        ),
    ),
    (
        "D2_uav_aerial",
        "2. 无人机与空中平台（四旋翼 / 直升机 / 倾转旋翼 / 空中机械臂）",
        re.compile(
            r"\b(?:quadrotor|uav|uavs|unmanned\s+aerial|helicopter|tilt-rotor|fixed-wing|multirotor|"
            r"drone|vtol|airship|aerial\s+manipulator|coaxial)\b|四旋翼|无人机|直升机",
            re.I,
        ),
    ),
    (
        "D3_manipulator_stage",
        "3. 机械臂与精密运动平台（刚/柔性关节 / 绳驱 / 水下 / 龙门平台）",
        re.compile(
            r"\b(?:manipulator|robotic\s+arm|robot\s+arm|flexible[- ]joint|cable-driven|tendon-driven|"
            r"exoskeleton|continuum\s+robot|gantry\s+stage|dual-linear-motor)\b|机械臂",
            re.I,
        ),
    ),
    (
        "D4_underactuated_mech",
        "4. 欠驱动机械系统（吊车 / 倒立摆 / 惯性轮摆 / TORA / 球杆 / Acrobot / 弹簧质量）",
        re.compile(
            r"\b(?:inverted\s+pendulum|inertia\s+wheel\s+pendulum|pendulum|overhead\s+crane|tower\s+crane|"
            r"ship-mounted\s+crane|crane|tora|acrobot|pendubot|cart-pole|ball[- ]and[- ]beam|ball-beam|"
            r"furuta|rotary\s+pendulum|spring[- ]mass)\b|倒立摆|吊车|球杆|弹簧",
            re.I,
        ),
    ),
    (
        "D5_marine_underwater",
        "5. 水面/水下无人艇与船舶（USV / AUV / 船舶 / 气垫船）",
        re.compile(
            r"\b(?:usv|usvs|auv|auvs|surface\s+vessels?|surface\s+vehicles?|underwater\s+vehicles?|"
            r"unmanned\s+surface|hovercraft|submersible|surface\s+ships?|underactuated\s+ships?|marine\s+craft|ship\s+control)\b|无人艇|水面艇|水下航行器|船舶",
            re.I,
        ),
    ),
    (
        "D6_mobile_nonholonomic",
        "6. 移动机器人、智能车辆与非完整/链式系统（Unicycle / Brockett / 广义链式 / 车队）",
        re.compile(
            r"\b(?:mobile\s+robot|wheeled\s+robot|nonholonomic|unicycle|brockett|chained\s+form|"
            r"chained\s+system|autonomous\s+vehicle|ground\s+vehicle|ugv|car-like|platoon|"
            r"tractor-trailer|omni-directional)\b|移动机器人|非完整|链式|车辆队列|无人车",
            re.I,
        ),
    ),
    (
        "D7_motor_power_maglev",
        "7. 电机、电力电子、微电网与磁悬浮伺服（PMSM / LSRM / 微电网 / 磁悬浮 / 柔性伺服）",
        re.compile(
            r"\b(?:pmsm|permanent\s+magnet\s+synchronous|induction\s+motor|switched\s+reluctance|lsrm|"
            r"dc-dc|boost\s+converter|buck\s+converter|inverter|microgrid|power\s+system|"
            r"magnetic\s+levitation|maglev|magnetic\s+bearing|flexible\s+servo|servo\s+system|rolling\s+mill)\b|"
            r"永磁同步|开关磁阻|微电网|磁悬浮|伺服",
            re.I,
        ),
    ),
    (
        "D8_process_hydraulic_suspension",
        "8. 工业过程、液压/气动执行器与车辆主动悬架（CSTR / 气动 / 液压 / 悬架）",
        re.compile(
            r"\b(?:cstr|chemical\s+reactor|tank\s+system|hydraulic|pneumatic|active\s+suspension|"
            r"quarter-car|vehicle\s+suspension|thermal\s+process|bioreactor)\b|悬架|液压|气动|反应釜",
            re.I,
        ),
    ),
    (
        "D9_switched_ftc_benchmarks",
        "9. 切换系统、脉冲/混合控制、主动容错与经典非线性基准（Switched / Impulsive / FTC / Lorenz / Isidori）",
        re.compile(
            r"\b(?:switched\s+(?:systems?|nonlinear|linear|sub-fas|filter|safe|mas|high-order)|"
            r"hybrid\s+impulsive|fault[- ]toleran(?:t|ce)|lorenz|duffing|van\s+der\s+pol|chua)\b|切换系统|容错控制",
            re.I,
        ),
    ),
]

PRIMARY_EX_RE = re.compile(r"^(?:\*\*)?(?:Example|例)\s*([0-9A-Za-z.]+)?\s*[:.：]?(.*)$")
PRIMARY_SEC_RE = re.compile(
    r"^#{2,3}\s+.*(?:Application|Example|Simulation|Spacecraft|Manipulator|Pendulum|Crane|Quadrotor|Underactuated|Brockett|Ship|Vehicle|应用|算例|仿真)",
    re.I,
)


def extract_primary_examples() -> list[tuple[str, list[tuple[int, str]]]]:
    out: list[tuple[str, list[tuple[int, str]]]] = []
    for p in sorted(PRIMARY_PAPERS_DIR.glob("*.md")):
        lines = p.read_text(encoding="utf-8").splitlines()
        hits: list[tuple[int, str]] = []
        for idx, ln in enumerate(lines, 1):
            s = ln.strip()
            if s.startswith("|") or s.startswith("- "):
                continue
            if PRIMARY_EX_RE.match(s) and len(s) >= 12:
                # Skip reference list false positives
                if idx > len(lines) * 0.90 and re.search(r"\(\d{4}\)", s):
                    continue
                preview = re.sub(r"\s+", " ", s.replace("**", ""))[:135]
                hits.append((idx, preview))
            elif PRIMARY_SEC_RE.match(s) and not re.match(r"^###\s+\d+\s+[A-Z][a-z]+", s):
                hits.append((idx, re.sub(r"^#+\s*", "[Section] ", s)[:120]))
        if hits:
            out.append((p.stem, hits))
    return out


def extract_backup_by_domain() -> dict[str, list[dict]]:
    conn = sqlite3.connect(BACKUP_DB)
    rows = conn.execute(
        """
        SELECT doc_id, score, score_reason, year, authors,
               COALESCE(NULLIF(canonical_venue, ''), venue) AS venue,
               title, abstract, doi
        FROM documents
        WHERE score >= 3
        ORDER BY score DESC, year DESC, doc_id
        """
    ).fetchall()
    conn.close()

    by_domain: dict[str, list[dict]] = {k: [] for k, _, _ in DOMAINS}
    for doc_id, score, reason, year, authors, venue, title, abstract, doi in rows:
        blob = f"{title} {(abstract or '')[:500]}"
        for dkey, _, rx in DOMAINS:
            if rx.search(blob):
                by_domain[dkey].append({
                    "doc_id": doc_id,
                    "score": score,
                    "reason": reason,
                    "year": year,
                    "authors": authors,
                    "venue": venue,
                    "title": title,
                    "doi": doi,
                })
    return by_domain


def main() -> None:
    primary_hits = extract_primary_examples()
    by_domain = extract_backup_by_domain()

    lines = [
        "# FAS 物理背景与仿真算例全量目录（36 篇一级权威库 + 二级 3–5 分高分期刊库）",
        "",
        "> 本目录由 `scripts/build_physical_examples_catalog.py` 自动生成，版权安全（仅含结构化目录与元数据索引，不含整篇受版权保护全文）。",
        "> 详细动力学方程、HOFAS/sub-FAS/UC-FAS/OD-FAS 具体转化形式、奇异集/可行集、仿真参数及各背景专属优势分析，见 `references/physical-examples-and-advantages.md`。",
        "",
        "## 一、高分期刊库（Score 3–5）按物理背景分布统计",
        "",
        "| 物理背景 / 基准类别 | Score 5 | Score 4 | Score 3 | 3–5 分合计 |",
        "|---|---:|---:|---:|---:|",
    ]

    for dkey, dlabel, _ in DOMAINS:
        items = by_domain[dkey]
        sc = collections.Counter(x["score"] for x in items)
        lines.append(f"| {dlabel} | {sc[5]} | {sc[4]} | {sc[3]} | **{len(items)}** |")

    lines.extend([
        "",
        f"## 二、36 篇 Duan 一级权威库 `Example` 与应用章节速查（覆盖 {len(primary_hits)} 篇）",
        "",
    ])
    for doc_id, hits in primary_hits:
        lines.append(f"### `{doc_id}` ({len(hits)})")
        for lno, prev in hits:
            lines.append(f"- `L{lno}`: {prev}")
        lines.append("")

    lines.extend([
        "## 三、二级高分期刊库（Score 3–5）按背景分类索引",
        "",
        "> 注：跨领域论文（如空间机械臂、切换容错飞行器）可在多个相关背景中同时出现；排序严格按分值降序（5 → 4 → 3），再按年份降序。",
        "",
    ])
    for dkey, dlabel, _ in DOMAINS:
        items = by_domain[dkey]
        lines.append(f"### {dlabel}（共 {len(items)} 篇）")
        lines.append("")
        for it in items:
            doi_s = f" | DOI: `{it['doi']}`" if it["doi"] else ""
            lines.append(
                f"- `[S{it['score']}]` `{it['doc_id']}` ({it['year']}, *{it['venue']}*): "
                f"{it['authors']} — {it['title']}{doi_s}"
            )
        lines.append("")

    OUT_CACHE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_CACHE} ({len(lines)} lines).")
    for dkey, dlabel, _ in DOMAINS:
        items = by_domain[dkey]
        sc = collections.Counter(x["score"] for x in items)
        print(f"  {dkey:32s}: S5={sc[5]:2d}, S4={sc[4]:2d}, S3={sc[3]:2d}, total={len(items):3d}")


if __name__ == "__main__":
    main()

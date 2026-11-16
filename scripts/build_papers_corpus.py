#!/usr/bin/env python3
"""Build structured Markdown full-text corpus and unified SQLite FTS5 index for Duan's FAS papers."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import unicodedata
from pathlib import Path
import fitz  # PyMuPDF

DEFAULT_CACHE = Path("/home/yzk/.cache/duan-hofas")
DEFAULT_CORPUS_DIR = DEFAULT_CACHE / "corpus"
DEFAULT_DB = DEFAULT_CACHE / "duan_corpus.sqlite"
DEFAULT_VOL1_DB = DEFAULT_CACHE / "volume1.sqlite"

PAPERS = [
    ("aas_2020_part1", "aas", 2020, "自动化学报 46(7):1333-1345", "高阶系统方法——I. 全驱系统与参数化设计", "/home/yzk/Zotero/storage/NMGKR9I3/高阶系统方法——I.全驱系统与参数化设计_段广仁.pdf"),
    ("aas_2020_part2", "aas", 2020, "自动化学报 46(8):1571-1581", "高阶系统方法——II. 能控性与全驱性", "/home/yzk/Zotero/storage/8XV48JSP/高阶系统方法——Ⅱ.能控性与全驱性_段广仁.pdf"),
    ("aas_2020_part3", "aas", 2020, "自动化学报 46(9):1885-1895", "高阶系统方法——III. 能观性与观测器设计", "/home/yzk/Zotero/storage/24R9X8VZ/高阶系统方法—Ⅲ.能观性与观测器设计.pdf"),
    ("aaas_2024_subsfs", "aas", 2024, "航空学报 45(1):629552", "亚严反馈系统镇定的全驱系统方法", "/home/yzk/Zotero/storage/W5MMR888/控制理论与制导技术研究中心和深圳市控制理论与智能系统重点实验室 - 亚严反馈系统镇定的全驱系统方法.pdf"),
    ("ijss_2021_part1", "ijss", 2021, "IJSS 52(2):422-435", "High-order fully actuated system approaches: Part I. Models and basic procedure", "/home/yzk/Zotero/storage/69Y4IU52/Duan - 2021 - High-order fully actuated system approaches Part I. Models and basic procedure.pdf"),
    ("ijss_2021_part2", "ijss", 2021, "IJSS 52(3):437-454", "High-order fully actuated system approaches: Part II. Generalized strict-feedback systems", "/home/yzk/Zotero/storage/NJSYE45L/Duan - 2021 - High-order fully actuated system approaches Part II. Generalized strict-feedback systems.pdf"),
    ("ijss_2021_part3", "ijss", 2021, "IJSS 52(5):952-971", "High-order fully actuated system approaches: Part III. Robust control and high-order backstepping", "/home/yzk/Zotero/storage/3KHRZRV6/Duan - 2021 - High-order fully actuated system approaches Part III. Robust control and high-order backstepping.pdf"),
    ("ijss_2021_part4", "ijss", 2021, "IJSS 52(5):972-989", "High-order fully actuated system approaches: Part IV. Adaptive control and high-order backstepping", "/home/yzk/Zotero/storage/WD52SSXY/Duan - 2021 - High-order fully actuated system approaches Part IV. Adaptive control and high-order backstepping.pdf"),
    ("ijss_2021_part5", "ijss", 2021, "IJSS 52(10):2129-2143", "High-order fully actuated system approaches: Part V. Robust adaptive control", "/home/yzk/Zotero/storage/99R6VIN8/Duan - 2021 - High-order fully actuated system approaches Part V. Robust adaptive control.pdf"),
    ("ijss_2021_part6", "ijss", 2021, "IJSS 52(10):2161-2181", "High-order fully-actuated system approaches: Part VI. Disturbance attenuation and decoupling", "/home/yzk/Zotero/storage/CNMZZVUF/Duan - 2021 - High-order fully-actuated system approaches Part VI. Disturbance attenuation and decoupling.pdf"),
    ("ijss_2021_part7", "ijss", 2021, "IJSS 52(14):3091-3114", "High-order fully actuated system approaches: Part VII. Controllability, stabilisability and parametric designs", "/home/yzk/Zotero/storage/3DW7D44I/Duan - 2021 - High-order fully actuated system approaches part VII. Controllability, stabilisability and parametr.pdf"),
    ("ijss_2022_part8", "ijss", 2022, "IJSS 53(1):54-73", "High-order fully actuated system approaches: Part VIII. Optimal control with application in spacecraft attitude stabilisation", "/home/yzk/Zotero/storage/X5CNKQ5P/Duan - 2022 - High-order fully actuated system approaches Part VIII. Optimal control with application in spacecra.pdf"),
    ("ijss_2022_part9", "ijss", 2022, "IJSS 53(3):652-674", "High-order fully-actuated system approaches: Part IX. Generalised PID control and model reference tracking", "/home/yzk/Zotero/storage/D2BFDTAG/Duan - 2022 - High-order fully-actuated system approaches Part IX. Generalised PID control and model reference tr.pdf"),
    ("ijss_2022_part10", "ijss", 2022, "IJSS 53(4):810-832", "High-order fully actuated system approaches: Part X. Basics of discrete-time systems", "/home/yzk/Zotero/storage/AQK6DM8X/Duan - 2022 - High-order fully actuated system approaches Part X. Basics of discrete-time systems.pdf"),
    ("ijss_2024_underactuated4", "ijss", 2024, "IJSS 55(12):2421-2441", "Stabilisation of four types of underactuated systems: a FAS approach", "/home/yzk/Zotero/storage/EEP2V6CR/Duan - 2024 - Stabilisation of four types of underactuated systems a FAS approach.pdf"),
    ("scis_2022_discdelay1", "scis", 2022, "Sci. China Inf. Sci. 65(8)", "Discrete-time delay systems: part 1. Global fully actuated case", "/home/yzk/Zotero/storage/82ML8UK4/Duan_Discrete-time delay systems.pdf"),
    ("scis_2022_discdelay2", "scis", 2022, "Sci. China Inf. Sci. 65(9)", "Discrete-time delay systems: part 2. Sub-fully actuated case", "/home/yzk/Zotero/storage/YHJBTQ4W/Duan - 2022 - Discrete-time delay systems part 2. Sub-fully actuated case.pdf"),
    ("scis_2023_delay1", "scis", 2023, "Sci. China Inf. Sci. 66(1):112201", "Fully actuated system approaches for continuous-time delay systems: part 1. Systems with state delays only", "/home/yzk/Zotero/storage/M9ZXXY5Z/Duan - 2023 - Fully actuated system approaches for continuous-time delay systems part 1. Systems with state delay.pdf"),
    ("scis_2023_delay2", "scis", 2023, "Sci. China Inf. Sci. 66(2):122201", "Fully actuated system approaches for continuous-time delay systems: part 2. Systems with input delays", "/home/yzk/Zotero/storage/YLYCAVMD/Duan - 2023 - Fully actuated system approaches for continuous-time delay systems part 2. Systems with input delay.pdf"),
    ("scis_2024_chained1", "scis", 2024, "Sci. China Inf. Sci. 67(2):122201", "A FAS approach for stabilization of generalized chained forms: part 1. Discontinuous control laws", "/home/yzk/Zotero/storage/BU6HCI62/Duan - 2024 - A FAS approach for stabilization of generalized chained forms part 1. Discontinuous control laws.pdf"),
    ("scis_2024_chained2", "scis", 2024, "Sci. China Inf. Sci. 67(3):132201", "A FAS approach for stabilization of generalized chained forms: part 2. Continuous control laws", "/home/yzk/Zotero/storage/4YCHUTBI/Duan - 2024 - A FAS approach for stabilization of generalized chained forms part 2. Continuous control laws.pdf"),
    ("jssc_2022_casestudy", "core", 2022, "J. Syst. Sci. Complex. 35(3):731-747", "Stabilization via Fully Actuated System Approach: A Case Study", "/home/yzk/Zotero/storage/7JN4ERB3/Duan_2022_Journal of Systems Science and Complexity_Stabilization via Fully Actuated System Approach.pdf"),
    ("jssc_2022_freq", "core", 2022, "J. Syst. Sci. Complex. 35(6):2046-2061", "Fully Actuated System Approach for Linear Systems Control: A Frequency-Domain Solution", "/home/yzk/Zotero/storage/P928LSUN/Duan和Zhou - 2022 - Fully Actuated System Approach for Linear Systems Control A Frequency-Domain Solution.pdf"),
    ("tcyb_2023_subfas", "core", 2023, "IEEE TCYB 53(11):7309-7322", "Substability and Substabilization: Control of Subfully Actuated Systems", "/home/yzk/Zotero/storage/GJ9C5BWS/Duan_2023_IEEE Transactions on Cybernetics_Substability and Substabilization.pdf"),
    ("tcyb_2023_robustdelay", "core", 2023, "IEEE TCYB 53(12):7455-7468", "Robust Stabilization of Time-Varying Nonlinear Systems With Time-Varying Delays: A Fully Actuated System Approach", "/home/yzk/Zotero/storage/FWHDATKP/Duan - 2023 - Robust Stabilization of Time-Varying Nonlinear Sys.pdf"),
    ("tcyb_2024_overview", "core", 2024, "IEEE TCYB 54(12):7285-7306", "Fully Actuated System Approach for Control: An Overview", "/home/yzk/Zotero/storage/VIE465YI/Duan - 2024 - Fully Actuated System Approach for Control An Ove.pdf"),
    ("fasta_2026_roea", "core", 2026, "FASTA / Coauthored Landmark (2026)", "Characterization of Region of Exponential Attraction for Substabilization of FASs", "/home/yzk/Zotero/storage/JLSFEAEK/Duan和Wang - 2026 - Characterization of Region of Exponential Attraction for Substabilization of FASs.pdf"),
    ("ucfas_2025_part1", "ucfas", 2025, "IJSS (2025)", "Constrained unidirectionally connected FASs: part I. Models", "/home/yzk/Zotero/storage/WRZJEN64/Duan - 2025 - Constrained unidirectionally connected FASs part I. Models.pdf"),
    ("ucfas_2025_part2", "ucfas", 2025, "IJSS (2025)", "Constrained unidirectionally connected FASs: Part II. Sub-stabilisation", "/home/yzk/Zotero/storage/7GDZPDA2/Duan - 2025 - Constrained unidirectionally connected FASs Part II. Sub-stabilisation.pdf"),
    ("ucfas_2025_part3", "ucfas", 2025, "IJSS (2025)", "Constrained unidirectionally connected FASs: Part III. Applications", "/home/yzk/Zotero/storage/E2JQ66GB/Duan - 2025 - Constrained unidirectionally connected FASs Part III. Applications.pdf"),
    ("odfas_2026_part1", "odfas", 2026, "IJSS (2026)", "Output-Dependent FASs and Output Feedback Control, Part 1: Case of Single-order FASs", "/home/yzk/Zotero/storage/DFWNZ4EW/Duan - Output-Dependent FASs and Output Feedback Control, Part 1 Case of Single-order FASs.pdf"),
    ("odfas_2026_part4", "odfas", 2026, "Preprint Manuscript (2026)", "Output Dependent FASs and Output Feedback Control, Part 4: Second-Order Dynamical Systems", "/home/yzk/Zotero/storage/Q3K6XVEF/Duan - Output Dependent FASs and Output Feedback Control, Part 4 Second-Order Dynamical Systems.pdf"),
]


GLYPH_UNICODE = {
    "Gamma": 0x0393, "Gamma1": 0x0393, "Delta": 0x0394, "Delta1": 0x0394,
    "Theta": 0x0398, "Theta1": 0x0398, "Lambda": 0x039B, "Lambda1": 0x039B,
    "Xi": 0x039E, "Xi1": 0x039E, "Pi": 0x03A0, "Pi1": 0x03A0,
    "Sigma": 0x03A3, "Sigma1": 0x03A3, "Upsilon": 0x03A5, "Upsilon1": 0x03A5,
    "Phi": 0x03A6, "Phi1": 0x03A6, "Psi": 0x03A8, "Psi1": 0x03A8,
    "Omega": 0x03A9, "Omega1": 0x03A9,
    "alpha": 0x03B1, "beta": 0x03B2, "gamma": 0x03B3, "delta": 0x03B4,
    "epsilon": 0x03F5, "epsilon1": 0x03B5, "varepsilon": 0x03B5,
    "zeta": 0x03B6, "eta": 0x03B7, "theta": 0x03B8, "theta1": 0x03D1,
    "iota": 0x03B9, "kappa": 0x03BA, "lambda": 0x03BB, "mu": 0x03BC,
    "nu": 0x03BD, "xi": 0x03BE, "pi": 0x03C0, "pi1": 0x03D6,
    "rho": 0x03C1, "rho1": 0x03F1, "sigma": 0x03C3, "sigma1": 0x03C2,
    "tau": 0x03C4, "upsilon": 0x03C5, "phi": 0x03D5, "phi1": 0x03C6,
    "chi": 0x03C7, "psi": 0x03C8, "omega": 0x03C9, "omega1": 0x03D6,
    "parenleft": 0x0028, "parenleftbig": 0x0028, "parenleftBig": 0x0028, "parenleftbigg": 0x0028, "parenleftBigg": 0x0028,
    "parenright": 0x0029, "parenrightbig": 0x0029, "parenrightBig": 0x0029, "parenrightbigg": 0x0029, "parenrightBigg": 0x0029,
    "bracketleft": 0x005B, "bracketleftbig": 0x005B, "bracketleftBig": 0x005B, "bracketleftbigg": 0x005B, "bracketleftBigg": 0x005B,
    "bracketright": 0x005D, "bracketrightbig": 0x005D, "bracketrightBig": 0x005D, "bracketrightbigg": 0x005D, "bracketrightBigg": 0x005D,
    "braceleft": 0x007B, "braceleftbig": 0x007B, "braceleftBig": 0x007B, "braceleftbigg": 0x007B, "braceleftBigg": 0x007B, "braceleftmid": 0x007B,
    "braceright": 0x007D, "bracerightbig": 0x007D, "bracerightBig": 0x007D, "bracerightbigg": 0x007D, "bracerightBigg": 0x007D, "bracerightmid": 0x007D,
    "vextendsingle": 0x007C, "vextenddouble": 0x2016, "bar": 0x007C, "bardbl": 0x2016,
    "summationdisplay": 0x2211, "summationtext": 0x2211, "productdisplay": 0x220F, "producttext": 0x220F,
    "integraldisplay": 0x222B, "integraltext": 0x222B,
    "mapsto": 0x21A6, "mapstochar": 0x21A6, "backslash": 0x005C, "setminus": 0x2216,
    "comma": 0x002C, "period": 0x002E, "less": 0x003C, "greater": 0x003E, "slash": 0x002F,
}
EXTENSION_SPACE_PREFIXES = (
    "bracelefttp", "braceleftbt", "bracerighttp", "bracerightbt", "braceex",
    "bracketlefttp", "bracketleftex", "bracketleftbt", "bracketrighttp", "bracketrightex", "bracketrightbt",
    "parenlefttp", "parenleftex", "parenleftbt", "parenrighttp", "parenrightex", "parenrightbt",
)


def patch_pdf_tounicode(doc: fitz.Document) -> None:
    """Repair broken/incomplete Type-1 ToUnicode CMaps in memory using PDF /Encoding /Differences."""
    seen: set[int] = set()
    for pno in range(len(doc)):
        for f in doc.get_page_fonts(pno):
            xref = f[0]
            if xref in seen:
                continue
            seen.add(xref)
            obj = doc.xref_object(xref)
            m_enc = re.search(r"/Encoding\s+(\d+)\s+0\s+R", obj)
            m_tu = re.search(r"/ToUnicode\s+(\d+)\s+0\s+R", obj)
            if not (m_enc and m_tu):
                continue
            enc_obj = doc.xref_object(int(m_enc.group(1)))
            m_diff = re.search(r"/Differences\s*\[(.*?)\]", enc_obj, re.S)
            if not m_diff:
                continue
            diff_map: dict[int, int] = {}
            cur_code = 0
            for tok in re.findall(r"\d+|/[A-Za-z0-9_.]+", m_diff.group(1)):
                if tok.isdigit():
                    cur_code = int(tok)
                else:
                    gname = tok[1:]
                    if gname in GLYPH_UNICODE:
                        diff_map[cur_code] = GLYPH_UNICODE[gname]
                    elif gname.startswith(EXTENSION_SPACE_PREFIXES):
                        diff_map[cur_code] = 0x0020
                    elif len(gname) == 1 and "A" <= gname <= "Z":
                        diff_map[cur_code] = ord(gname)
                    cur_code += 1
            if not diff_map:
                continue
            tu_xref = int(m_tu.group(1))
            old_tu = doc.xref_stream(tu_xref).decode("latin1", errors="ignore")
            merged: dict[int, int] = {}
            for rng_blk in re.findall(r"beginbfrange(.*?)endbfrange", old_tu, re.S):
                for lo_h, hi_h, dst_h in re.findall(r"<([0-9A-Fa-f]{2})>\s*<([0-9A-Fa-f]{2})>\s*<([0-9A-Fa-f]{4,6})>", rng_blk):
                    lo_i, hi_i, dst_i = int(lo_h, 16), int(hi_h, 16), int(dst_h, 16)
                    for offset_i, c_i in enumerate(range(lo_i, hi_i + 1)):
                        u_i = dst_i + offset_i
                        if u_i != 0xFFFD and not is_pua(u_i):
                            merged[c_i] = u_i
            for chr_blk in re.findall(r"beginbfchar(.*?)endbfchar", old_tu, re.S):
                for hc, hu in re.findall(r"<([0-9A-Fa-f]{2})>\s*<([0-9A-Fa-f]{4,6})>", chr_blk):
                    c_i, u_i = int(hc, 16), int(hu, 16)
                    if u_i != 0xFFFD and not is_pua(u_i):
                        merged[c_i] = u_i
            for c_i, u_i in diff_map.items():
                if c_i not in merged:
                    merged[c_i] = u_i
            entries = "\n".join(
                f"<{c:02X}> <{u:04X}>" if u <= 0xFFFF else f"<{c:02X}> <{0xD800 + ((u - 0x10000) >> 10):04X}{0xDC00 + ((u - 0x10000) & 0x3FF):04X}>"
                for c, u in sorted(merged.items())
            )
            cmap = (
                "/CIDInit /ProcSet findresource begin 12 dict begin begincmap\n"
                "/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def\n"
                "/CMapName /PatchedToUnicode def /CMapType 2 def\n"
                "1 begincodespacerange <00> <FF> endcodespacerange\n"
                f"{len(merged)} beginbfchar\n{entries}\nendbfchar\n"
                "endcmap CMapName currentdict /CMap defineresource pop end end\n"
            ).encode("latin1")
            doc.update_stream(tu_xref, cmap)


def yandy_slot(code: int) -> int:
    if 0xF000 <= code <= 0xF0FF:
        code -= 0xF000
    if 0xA1 <= code <= 0xAA:
        return code - 0xA1
    if 0xAD <= code <= 0xCC:
        return code - 0xAD + 10
    return code


OML_MAP = {
    0x00: "Γ", 0x01: "Δ", 0x02: "Θ", 0x03: "Λ", 0x04: "Ξ", 0x05: "Π", 0x06: "Σ", 0x07: "Υ", 0x08: "Φ", 0x09: "Ψ", 0x0A: "Ω",
    0x0B: "α", 0x0C: "β", 0x0D: "γ", 0x0E: "δ", 0x0F: "ϵ", 0x10: "ζ", 0x11: "η", 0x12: "θ", 0x13: "ι", 0x14: "κ", 0x15: "λ",
    0x16: "μ", 0x17: "ν", 0x18: "ξ", 0x19: "π", 0x1A: "ρ", 0x1B: "σ", 0x1C: "τ", 0x1D: "υ", 0x1E: "ϕ", 0x1F: "χ", 0x20: "ψ",
    0x21: "ω", 0x22: "ε", 0x23: "ϑ", 0x24: "ϖ", 0x25: "ϱ", 0x26: "ς", 0x27: "φ",
    0x3A: ".", 0x3B: ",", 0x3C: "<", 0x3D: "/", 0x3E: ">", 0x7E: "⃗",
}
OMS_MAP = {
    0x00: "−", 0x01: "⋅", 0x02: "×", 0x03: "∗", 0x04: "÷", 0x06: "±", 0x08: "⊕", 0x0A: "⊗", 0x0E: "∘", 0x0F: "∙",
    0x11: "≡", 0x12: "⊆", 0x13: "⊇", 0x14: "≤", 0x15: "≥", 0x18: "∼", 0x19: "≈", 0x1A: "⊂", 0x1B: "⊃", 0x1C: "≪", 0x1D: "≫",
    0x20: "←", 0x21: "→", 0x28: "⇐", 0x29: "⇒", 0x2C: "⇔",
    0x30: "′", 0x31: "∞", 0x32: "∈", 0x33: "∋", 0x36: "̸", 0x37: "↦", 0x38: "∀", 0x39: "∃", 0x3B: "∅",
    0x66: "{", 0x67: "}", 0x68: "⟨", 0x69: "⟩", 0x6A: "|", 0x6B: "‖", 0x6E: "\\", 0x70: "√", 0x79: "†",
}
OT1_MAP = {
    0x00: "Γ", 0x01: "Δ", 0x02: "Θ", 0x03: "Λ", 0x04: "Ξ", 0x05: "Π", 0x06: "Σ", 0x07: "Υ", 0x08: "Φ", 0x09: "Ψ", 0x0A: "Ω",
    0x5E: "ˆ", 0x5F: "˙", 0x7E: "˜",
}
CMEX_SLOT_MAP = {
    0x00: "(", 0x01: ")", 0x02: "[", 0x03: "]", 0x04: "⌊", 0x05: "⌋", 0x06: "⌈", 0x07: "⌉", 0x08: "{", 0x09: "}",
    0x10: "(", 0x11: ")", 0x12: "(", 0x13: ")", 0x14: "[", 0x15: "]", 0x16: "⌊", 0x17: "⌋", 0x18: "⌈", 0x19: "⌉", 0x1A: "{", 0x1B: "}",
    0x20: "(", 0x21: ")", 0x22: "[", 0x23: "]", 0x24: "⌊", 0x25: "⌋", 0x26: "⌈", 0x27: "⌉", 0x28: "{", 0x29: "}",
    0x3C: "{", 0x3D: "}",
    0x50: "∑", 0x51: "∏", 0x52: "∫", 0x58: "∑", 0x59: "∏", 0x5A: "∫", 0x68: "⌊", 0x69: "⌋", 0x6A: "⌈", 0x6B: "⌉",
}


APPLE_PUA_BRACES = {
    0xF8EB: "⎛", 0xF8EC: "⎜", 0xF8ED: "⎝",
    0xF8EE: "⎡", 0xF8EF: "⎢", 0xF8F0: "⎣",
    0xF8F1: "⎧", 0xF8F2: "⎨", 0xF8F3: "⎩", 0xF8F4: "⎪",
    0xF8F6: "⎞", 0xF8F7: "⎟", 0xF8F8: "⎠",
    0xF8F9: "⎤", 0xF8FA: "⎥", 0xF8FB: "⎦",
    0xF8FC: "⎫", 0xF8FD: "⎬", 0xF8FE: "⎭",
}


def is_pua(code: int) -> bool:
    return (0xE000 <= code <= 0xF8FF) or (code >= 0xF0000)


def detect_yandy_doc(doc: fitz.Document) -> bool:
    """Detect Scientific Workplace / Y&Y TeX encoding (Cmmi in 0xF000..0xF0FF or Dcr10 fonts)."""
    for pno in range(min(5, len(doc))):
        for b in doc[pno].get_text("dict")["blocks"]:
            if b["type"] != 0:
                continue
            for ln in b["lines"]:
                for sp in ln["spans"]:
                    fl = sp["font"].lower().split("+")[-1]
                    if fl.startswith(("dcr", "dcti")):
                        return True
                    if fl.startswith("cmmi") and any(0xF000 <= ord(c) <= 0xF0FF for c in sp["text"]):
                        return True
    return False


def decode_span(font: str, text: str, is_yandy: bool = False) -> str:
    fl = font.lower()
    if "+" in fl:
        fl = fl.split("+", 1)[1]
    if fl.startswith(("dcr", "dcti", "dcbx", "dcss")):
        return unicodedata.normalize("NFKC", text.replace("\u2026", "fi").replace("¤", "ff").replace("¢", "ffi"))
    if fl.startswith("msbm"):
        return "".join({"R": "ℝ", "N": "ℕ", "Z": "ℤ", "C": "ℂ", "Q": "ℚ", "F": "𝔽", "S": "𝕊", "B": "𝔹"}.get(c, c) for c in text)
    if is_yandy:
        if fl.startswith("cmmi"):
            return "".join(
                " " if ord(c) == 0x20 else (
                    OML_MAP.get(yandy_slot(ord(c)), chr(yandy_slot(ord(c))) if 0x21 <= yandy_slot(ord(c)) <= 0x7E else "")
                    if (is_pua(ord(c)) or ord(c) > 126) else OML_MAP.get(ord(c), c)
                )
                for c in text
            )
        if fl.startswith("cmsy"):
            return "".join(
                " " if ord(c) == 0x20 else OMS_MAP.get(
                    yandy_slot(ord(c)) if (is_pua(ord(c)) or ord(c) > 126) else ord(c),
                    "" if is_pua(ord(c)) else c,
                )
                for c in text
            )
        if fl.startswith("cmr"):
            return "".join(
                "¨" if ord(c) == 0xC4 else OT1_MAP.get(
                    yandy_slot(ord(c)) if (is_pua(ord(c)) or ord(c) > 126) else ord(c),
                    "" if is_pua(ord(c)) else c,
                )
                for c in text
            )
        if fl.startswith("cmex"):
            out = []
            for c in text:
                if ord(c) == 0x20:
                    out.append(" ")
                    continue
                s = yandy_slot(ord(c)) if (is_pua(ord(c)) or ord(c) > 126) else ord(c)
                if s in CMEX_SLOT_MAP:
                    out.append(CMEX_SLOT_MAP[s])
            return "".join(out)
    # Modern Unicode LaTeX PDFs: convert Apple Symbol PUA big delimiters (0xF8EB..0xF8FE) to Unicode box-drawing braces, strip remaining PUA/FFFD
    out_chars = []
    for c in text:
        code = ord(c)
        if code in APPLE_PUA_BRACES:
            out_chars.append(APPLE_PUA_BRACES[code])
        elif not is_pua(code) and c != "\ufffd":
            out_chars.append(c)
    return unicodedata.normalize("NFKC", "".join(out_chars))


# Strict case-sensitive landmark matcher: rejects lowercase prose wraps ('problem for', 'condition is') and comma-references ('Corollary 5.2, we...')
EN_LANDMARK_RE = re.compile(
    r"^(Definition|Assumption|Condition|Problem|Lemma|Proposition|Theorem|Corollary|Remark)\s+"
    r"([A-Z]?\d+(?:\.\d+)*[′']?|[IVX]+|[A-Z][A-Za-z0-9ϕφψθτΔΓ′']{0,6})(?!\.\d|[A-Za-z0-9],|,)"
    r"(?:[:.]|\s+\(|\s+[A-Z\u4e00-\u9fa5(]|$)"
)
ZH_LANDMARK_RE = re.compile(
    r"^(定义|假设|条件|问题|引理|命题|定理|推论|说明)\s*([A-Z]?\d+(?:\.\d+)*|[A-Z]{1,4}\d*|\d+|)"
    r"(?:[.:：.\s\[]|$)"
)
BAD_ID_WORDS = {"is", "are", "for", "of", "in", "on", "to", "and", "or", "with", "that", "statement", "statements", "formulation", "reformulation", "conversion"}

SEC_HEADING_RE = re.compile(
    r"^(?:[IVX]+\.\s+[A-Z][A-Za-z0-9\s,\-–—:()]{2,85}"
    r"|\d+(?:\.\d+){0,2}\.?\s+[A-Z\u4e00-\u9fa5][^\n]{1,85})$"
)


def match_landmark(line: str) -> tuple[str, str] | None:
    s = line.strip()
    m_en = EN_LANDMARK_RE.match(s)
    if m_en:
        kind = m_en.group(1)
        num_tok = m_en.group(2).rstrip(".:")
        if num_tok.lower() in BAD_ID_WORDS:
            return None
        rest = s[len(m_en.group(1)) + 1 + len(m_en.group(2)) :].lstrip()
        if rest.startswith((",", ";", "and ", "or ", "in ", "is ", "can ", "gives ", "still ", "holds")):
            return None
        return kind, f"{kind} {num_tok}"
    m_zh = ZH_LANDMARK_RE.match(s)
    if m_zh:
        zh_k = m_zh.group(1)
        num_tok = (m_zh.group(2) or "").rstrip(".:：")
        rest = s[m_zh.end(2) :].lstrip()
        if not num_tok and zh_k != "说明":
            return None
        if not num_tok and zh_k == "说明" and not rest.startswith((".", "：", ":", "由", "上")):
            return None
        if rest.startswith(("指出", "表明", "说明", "给出", "的证明", "和")):
            return None
        kind = {"定义": "Definition", "假设": "Assumption", "条件": "Condition", "问题": "Problem", "引理": "Lemma", "命题": "Proposition", "定理": "Theorem", "推论": "Corollary", "说明": "Remark"}[zh_k]
        label = f"{zh_k} {num_tok}".strip()
        return kind, label
    return None


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def get_unmapped_cm_fonts(doc: fitz.Document) -> set[str]:
    unmapped: set[str] = set()
    seen: set[int] = set()
    for pno in range(len(doc)):
        for f in doc.get_page_fonts(pno):
            xref, _, _, basefont, _, encoding = f[:6]
            if xref in seen:
                continue
            seen.add(xref)
            obj = doc.xref_object(xref)
            fl = basefont.lower()
            if "+" in fl:
                fl = fl.split("+", 1)[1]
            if "/ToUnicode" not in obj and fl.startswith(("cmmi", "cmsy", "cmex", "cmr")):
                unmapped.add(fl)
    return unmapped


def spans_to_lines(spans: list[tuple[float, float, float, float, float, str]]) -> list[str]:
    if not spans:
        return []
    spans = sorted(spans, key=lambda s: (s[4], s[0]))
    rows: list[list[tuple[float, float, float, float, float, str]]] = []
    for sp in spans:
        if not rows:
            rows.append([sp])
            continue
        row_yb = sum(x[4] for x in rows[-1]) / len(rows[-1])
        if abs(sp[4] - row_yb) <= 5.6:
            rows[-1].append(sp)
        else:
            rows.append([sp])
    out_lines: list[str] = []
    prev_yb: float | None = None
    for row in rows:
        row.sort(key=lambda s: s[0])
        cur_yb = sum(x[4] for x in row) / len(row)
        parts: list[str] = []
        prev_x1: float | None = None
        for x0, y0, x1, y1, yb, txt in row:
            if prev_x1 is not None and (x0 - prev_x1) > 2.4 and not (parts and parts[-1].endswith(" ")) and not txt.startswith(" "):
                parts.append(" ")
            parts.append(txt)
            prev_x1 = max(prev_x1 or x1, x1)
        line = "".join(parts)
        line = line.replace("̸=", "≠").replace("̸ =", "≠").replace("↦−→", "↦").replace("↦→", "↦").replace("−↦", "↦")
        line = re.sub(r"[ \t]+", " ", line).strip()
        if not line:
            continue
        if prev_yb is not None and (cur_yb - prev_yb) > 17.5:
            out_lines.append("")
        out_lines.append(line)
        prev_yb = cur_yb
    return out_lines


def extract_page_ordered_lines(page: fitz.Page, is_yandy: bool) -> list[str]:
    W = page.rect.width
    H = page.rect.height
    mid = W * 0.5
    line_items = []  # (lx0, ly0, lx1, ly1, spans_list)

    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for ln in b["lines"]:
            lx0, ly0, lx1, ly1 = ln["bbox"]
            ln_spans = []
            raw_joined = []
            for sp in ln["spans"]:
                fl = sp["font"].lower()
                if "+" in fl:
                    fl = fl.split("+", 1)[1]
                t = decode_span(sp["font"], sp["text"], is_yandy=is_yandy)
                if not t.strip():
                    continue
                raw_joined.append(t.strip())
                sx0, sy0, sx1, sy1 = sp["bbox"]
                yb = (0.5 * (sy0 + sy1) + 3.0) if fl.startswith(("cmex", "mtex")) else sp["origin"][1]
                ln_spans.append((sx0, sy0, sx1, sy1, yb, t))
            if not ln_spans:
                continue
            joined_s = "".join(raw_joined).strip()
            # Drop isolated running page numbers in top/bottom margins
            if (ly0 < 0.088 * H or ly1 > 0.915 * H) and re.fullmatch(r"\d{1,4}", joined_s):
                continue
            line_items.append((lx0, ly0, lx1, ly1, ln_spans))

    left_col_lines = sum(
        1 for lx0, ly0, lx1, ly1, _ in line_items
        if lx0 < W * 0.20 and W * 0.36 <= lx1 <= W * 0.52 and 0.08 * H < ly0 < 0.92 * H
    )
    right_col_lines = sum(
        1 for lx0, ly0, lx1, ly1, _ in line_items
        if W * 0.48 <= lx0 <= W * 0.62 and lx1 > W * 0.80 and 0.08 * H < ly0 < 0.92 * H
    )
    full_width_lines = sum(
        1 for lx0, ly0, lx1, ly1, _ in line_items
        if lx0 < W * 0.22 and lx1 > W * 0.76 and 0.12 * H < ly0 < 0.88 * H
    )
    is_two_col = (
        left_col_lines >= 4
        and right_col_lines >= 4
        and full_width_lines < (left_col_lines + right_col_lines) * 0.35
    )

    if not is_two_col:
        all_sp = [sp for _, _, _, _, sps in line_items for sp in sps]
        return ["\n".join(spans_to_lines(all_sp))]

    # Two-column page: sort lines vertically, split into bands at full-width spanning lines (title/authors/wide eqs)
    sorted_lns = sorted(line_items, key=lambda item: (round(item[1], 1), round(item[0], 1)))
    sections_out: list[str] = []
    cur_left: list = []
    cur_right: list = []
    for lx0, ly0, lx1, ly1, sps in sorted_lns:
        is_wide = (lx0 < W * 0.38 and lx1 > W * 0.62 and (lx1 - lx0) > W * 0.48)
        if is_wide:
            if cur_left:
                sections_out.append("\n".join(spans_to_lines(cur_left)))
                cur_left = []
            if cur_right:
                sections_out.append("\n".join(spans_to_lines(cur_right)))
                cur_right = []
            sections_out.append("\n".join(spans_to_lines(sps)))
        else:
            if 0.5 * (lx0 + lx1) < mid:
                cur_left.extend(sps)
            else:
                cur_right.extend(sps)
    if cur_left:
        sections_out.append("\n".join(spans_to_lines(cur_left)))
    if cur_right:
        sections_out.append("\n".join(spans_to_lines(cur_right)))
    return [s for s in sections_out if s.strip()]


def build_all(corpus_dir: Path, db_path: Path, vol1_db: Path) -> None:
    papers_dir = corpus_dir / "papers"
    papers_dir.mkdir(parents=True, exist_ok=True)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.executescript(
        """
        DROP TABLE IF EXISTS documents;
        DROP TABLE IF EXISTS pages;
        DROP TABLE IF EXISTS pages_fts;
        DROP TABLE IF EXISTS landmarks;
        DROP TABLE IF EXISTS landmarks_fts;
        CREATE TABLE documents (
            doc_id TEXT PRIMARY KEY,
            series TEXT NOT NULL,
            year INTEGER NOT NULL,
            venue TEXT NOT NULL,
            title TEXT NOT NULL,
            source_pdf TEXT NOT NULL,
            md_path TEXT,
            sha256 TEXT NOT NULL,
            pdf_pages INTEGER NOT NULL
        );
        CREATE TABLE pages (
            page_uid INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_id TEXT NOT NULL,
            series TEXT NOT NULL,
            pdf_page INTEGER NOT NULL,
            md_line INTEGER,
            text TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE pages_fts USING fts5(
            doc_id,
            series,
            text,
            content='pages',
            content_rowid='page_uid',
            tokenize='unicode61 remove_diacritics 2'
        );
        CREATE TABLE landmarks (
            landmark_id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_id TEXT NOT NULL,
            series TEXT NOT NULL,
            kind TEXT NOT NULL,
            label TEXT NOT NULL,
            pdf_page INTEGER NOT NULL,
            md_line INTEGER,
            statement_start TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE landmarks_fts USING fts5(
            doc_id,
            series,
            kind,
            label,
            statement_start,
            content='landmarks',
            content_rowid='landmark_id',
            tokenize='unicode61 remove_diacritics 2'
        );
        """
    )

    manifest = []
    index_rows = []

    for doc_id, series, year, venue, title, pdf_str in PAPERS:
        pdf_path = Path(pdf_str)
        if not pdf_path.is_file():
            raise FileNotFoundError(f"Missing PDF for {doc_id}: {pdf_path}")
        digest = sha256_file(pdf_path)
        probe = fitz.open(pdf_path)
        is_yandy = detect_yandy_doc(probe)
        probe.close()
        doc = fitz.open(pdf_path)
        if not is_yandy:
            patch_pdf_tounicode(doc)
        num_pages = len(doc)

        body_pages: list[tuple[int, str]] = []
        for pno in range(1, num_pages + 1):
            blocks = extract_page_ordered_lines(doc[pno - 1], is_yandy)
            page_text = "\n\n".join(blocks)
            page_text = page_text.replace("\\[", "[").replace("\\]", "]").replace("$$", "$")
            body_pages.append((pno, page_text))

        body_lines: list[str] = []
        page_anchor_rel_idx: dict[int, int] = {}  # 0-based index into body_lines of '<!-- PDF p.X/N -->'
        body_landmarks: list[tuple[str, str, int, int, str]] = []  # kind, label, pno, 0-based body_idx, snippet

        for pno, ptext in body_pages:
            page_anchor_rel_idx[pno] = len(body_lines)
            body_lines.append(f"<!-- PDF p.{pno}/{num_pages} -->")
            body_lines.append(f"## [Page {pno}]")
            p_lns = ptext.splitlines()
            for idx, ln in enumerate(p_lns):
                s = ln.strip()
                lm = match_landmark(s)
                if lm is not None:
                    kind, label = lm
                    snippet = " ".join(x.strip() for x in p_lns[idx : min(len(p_lns), idx + 6)] if x.strip())[:240]
                    body_landmarks.append((kind, label, pno, len(body_lines), snippet))
                    body_lines.append(f"**{s}**" if not s.startswith("**") else s)
                elif SEC_HEADING_RE.match(s) and len(s) < 88 and not s[0].islower():
                    body_lines.append(f"### {s}")
                else:
                    body_lines.append(ln)
            body_lines.append("")

        header_prefix = [
            "---",
            f'doc_id: "{doc_id}"',
            f'series: "{series}"',
            f"year: {year}",
            f'venue: "{venue}"',
            f'title: "{title}"',
            f'source_pdf: "{pdf_path}"',
            f'sha256: "{digest}"',
            f"pdf_pages: {num_pages}",
            "---",
            "",
            f"# {title}",
            "",
            f"- **Doc ID**: `{doc_id}` | **Series**: `{series}` | **Year**: {year} | **Venue**: {venue}",
            f"- **Primary PDF**: `{pdf_path}` ({num_pages} pages)",
            "",
            "## Formal Landmarks Index",
            "",
            "| Label | Kind | PDF Page | MD Line | Opening Preview |",
            "|---|---|---:|---:|---|",
        ]
        table_row_count = max(1, len(body_landmarks))
        header_suffix = ["", "---", ""]
        # Exact number of lines before body_lines[0]:
        header_total_lines = len(header_prefix) + table_row_count + len(header_suffix)

        table_rows: list[str] = []
        if body_landmarks:
            for kind, label, pno, body_idx, snippet in body_landmarks:
                abs_ln = header_total_lines + body_idx + 1  # 1-based line number
                safe_snip = snippet.replace("|", "\\|")[:120]
                table_rows.append(f"| `{label}` | {kind} | p.{pno} | L{abs_ln} | {safe_snip} |")
        else:
            table_rows.append("| *(none detected)* | - | - | - | - |")

        all_md_lines = header_prefix + table_rows + header_suffix + body_lines
        # Hard invariant check on EVERY landmark and EVERY page anchor
        for kind, label, pno, body_idx, _ in body_landmarks:
            abs_ln = header_total_lines + body_idx + 1
            assert all_md_lines[abs_ln - 1].startswith("**"), f"Line mismatch in {doc_id} {label}: L{abs_ln} -> {all_md_lines[abs_ln - 1]}"
        for pno, anchor_idx in page_anchor_rel_idx.items():
            abs_p_ln = header_total_lines + anchor_idx + 1
            assert all_md_lines[abs_p_ln - 1] == f"<!-- PDF p.{pno}/{num_pages} -->", f"Page anchor mismatch in {doc_id} p.{pno}"

        md_path = papers_dir / f"{doc_id}.md"
        md_path.write_text("\n".join(all_md_lines), encoding="utf-8")

        conn.execute(
            "INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?)",
            (doc_id, series, year, venue, title, str(pdf_path), str(md_path), digest, num_pages),
        )
        for pno, ptext in body_pages:
            abs_p_ln = header_total_lines + page_anchor_rel_idx[pno] + 1
            conn.execute(
                "INSERT INTO pages(doc_id, series, pdf_page, md_line, text) VALUES (?,?,?,?,?)",
                (doc_id, series, pno, abs_p_ln, ptext),
            )
        for kind, label, pno, body_idx, snippet in body_landmarks:
            abs_ln = header_total_lines + body_idx + 1
            conn.execute(
                "INSERT INTO landmarks(doc_id, series, kind, label, pdf_page, md_line, statement_start) VALUES (?,?,?,?,?,?,?)",
                (doc_id, series, kind, label, pno, abs_ln, snippet),
            )

        manifest.append(
            {
                "doc_id": doc_id,
                "series": series,
                "year": year,
                "venue": venue,
                "title": title,
                "pdf_pages": num_pages,
                "landmarks": len(body_landmarks),
                "md_file": f"papers/{doc_id}.md",
                "source_pdf": str(pdf_path),
                "sha256": digest,
            }
        )
        index_rows.append(
            f"| `{doc_id}` | `{series}` | {year} | {venue} | {num_pages} | {len(body_landmarks)} | [{title}](papers/{doc_id}.md) |"
        )

    if vol1_db.is_file():
        vconn = sqlite3.connect(f"file:{vol1_db}?mode=ro", uri=True)
        meta = dict(vconn.execute("SELECT key, value FROM metadata").fetchall())
        conn.execute(
            "INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?)",
            (
                "book_2026_volume1",
                "volume1",
                2026,
                "Springer Monograph (DOI 10.1007/978-981-96-8395-6)",
                meta.get("title", "Fully Actuated System Approach, Volume I"),
                meta.get("source_pdf", ""),
                None,
                meta.get("source_sha256", ""),
                int(meta.get("pdf_pages", "513")),
            ),
        )
        for pdf_page, printed_page, chapter, text in vconn.execute("SELECT pdf_page, printed_page, chapter, text FROM pages"):
            conn.execute(
                "INSERT INTO pages(doc_id, series, pdf_page, md_line, text) VALUES (?,?,?,?,?)",
                ("book_2026_volume1", "volume1", pdf_page, printed_page, f"[{chapter}]\n{text}"),
            )
        for kind, label, pdf_page, printed_page, statement_start in vconn.execute(
            "SELECT kind, label, pdf_page, printed_page, statement_start FROM landmarks"
        ):
            conn.execute(
                "INSERT INTO landmarks(doc_id, series, kind, label, pdf_page, md_line, statement_start) VALUES (?,?,?,?,?,?,?)",
                ("book_2026_volume1", "volume1", kind, label, pdf_page, printed_page, statement_start),
            )
        vconn.close()

    conn.execute("INSERT INTO pages_fts(pages_fts) VALUES ('rebuild')")
    conn.execute("INSERT INTO landmarks_fts(landmarks_fts) VALUES ('rebuild')")
    conn.commit()
    conn.close()

    (corpus_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    index_md = "\n".join(
        [
            "# Duan First-Author Full-Text Corpus Index",
            "",
            f"- **Total papers converted**: {len(manifest)} Markdown full-text files (`papers/*.md`) + 2026 Springer *Volume I* indexed in `{db_path}`",
            "",
            "| Doc ID | Series | Year | Venue | Pages | Landmarks | Structured Markdown |",
            "|---|---|---:|---|---:|---:|---|",
            *index_rows,
            "",
        ]
    )
    (corpus_dir / "INDEX.md").write_text(index_md, encoding="utf-8")
    print(f"Built {len(manifest)} structured Markdown papers in {papers_dir} (all line-number invariants verified)")
    print(f"Built unified FTS5 database at {db_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus-dir", type=Path, default=DEFAULT_CORPUS_DIR)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--vol1-db", type=Path, default=DEFAULT_VOL1_DB)
    args = parser.parse_args()
    build_all(args.corpus_dir, args.db, args.vol1_db)


if __name__ == "__main__":
    main()

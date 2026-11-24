# Duan HOFAS Skill

English | [简体中文](README_zh-CN.md)

A unified skill (for **Antigravity**, **Claude Code**, and **Codex**) for checking, drafting, and polishing HOFAS / FAS / sub-FAS / switched sub-FAS Markdown files and LaTeX manuscripts using **Guang-Ren Duan's authentic vocabulary, sentence patterns, notation, article organization, formal environments, and proof templates**. It also provides a compilable IEEEtran-compatible Duan-style LaTeX manuscript skeleton.

## Core capabilities

- **Corpus-backed Duan-style drafting & polishing** ([duan-writing-corpus.md](references/duan-writing-corpus.md), [duan-series-templates.md](references/duan-series-templates.md)): Write and revise manuscripts using verbatim `[E]` expressions and series-specific structural templates distilled from **all 32 local first-author Duan FAS papers** (28 English + 4 Chinese across *Acta Automatica Sinica*, *IJSS*, *SCIS*, *IEEE TCYB*, *UC-FAS*, and *OD-FAS*) plus the 2026 monograph *Fully Actuated System Approach, Volume I*, preserving Duan's signature phrasing (`"the feasible set clearly has the following expression:"`, `"we construct the following controller:"`, `"is equivalent to the following state-space form:"`, `"The above result converts/reveals..."`) while eliminating AI-flavored `"not X, but Y"` defensive disclaimers and single-claim meta-previews.
- **Duan-first concept & notation alignment** ([duan-style-quick-guide.md](references/duan-style-quick-guide.md), [concepts-and-notation.md](references/concepts-and-notation.md)): Prioritize Duan's established concepts and symbols ($\varphi_0,\varphi_\infty,\varphi$, $|\varphi_i|$, $\mathbb{S}/\mathcal{S}$, $\mathbb{F}/\mathcal{F}$, substability, ROEA/RoEA, $X_0=x^{(0\sim n-1)}(0)$, end-of-Introduction `Notations:` with `=` and unnumbered `equation*`, no `:=` or `\col`), introducing new `[D]` objects only where Duan has no counterpart.
- **Strict provenance discipline (`[E]` / `[D]` / `[U]`)** ([model-definition-registry.md](references/model-definition-registry.md)): Keep Duan's original definitions/assumptions strictly separate from paper-added `[D]` conditions and `[U]` unverified items; never read unstated smoothness or topological assumptions into Duan's texts.
- **Formal environment templates & explicit-goal rule** ([theorem-writing-template.md](references/theorem-writing-template.md)): Standardize `Problem`, `Definition`, `Assumption`/`Condition`, `Lemma`, `Proposition`, `Theorem` (6-part structure + `Then 1)...; 2)...`), `Corollary`, and `Remark` (6 roles), enforcing that **every `Theorem`, `Lemma`, `Proposition`, and `Corollary` states its final purpose directly inside its own statement**.
- **Canonical & series-specific Duan proof structures** ([proof-templates.md](references/proof-templates.md), [duan-series-templates.md](references/duan-series-templates.md)):
  1. Direct substitution + state-space form + Lyapunov decay;
  2. SUB-FAS substabilization & exact ROEA characterization (`Duan 2023 TCYB`);
  3. Proof by contradiction (`Duan & Zhou 2022`, Lemma 4.4: `"Suppose that … Then it follows from … On the other side, … This yields a contradiction. Thus … The proof is finished."`);
  4. High-order backstepping (`Part III` §4 / `Volume I` §9.2 with $\tilde P_i(A_i^{0\sim m_i-1})=\mathring{I}P_i$ and telescoping Lyapunov sum);
  5. Sufficiency & necessity (`Sufficiency:` / `Necessity:` / `"Combining the above two aspects..."`), multi-conclusion, and mathematical induction;
  6. Monotonic-interval splitting & finite stationary-point ROEA reduction (`Duan & Wang 2026`);
  7. OD-FAS reduced-order observer ($\dot y$-free $z$-variable), 4-block output-feedback compensator, $T A_E T^{-1}$ block-triangular / cascade ISS proof, and augmented $[X_0^\top\ z_0^\top]^\top$ RoEA (`OD-FAS Part 1 & Part 4`);
  8. Constrained UC-FAS internal/external feasibility decomposition ($\mathbb{F}^{\mathrm{in}}\cap\mathbb{F}^{\mathrm{ex}}$) and 3-step cascade substabilization (`UC-FAS Parts I–III`), plus delay-predictor (`SCIS 2023`) and generalized chained-form scaling/perturbation (`SCIS 2024`).
- **Examples, captions, tables & MATLAB figure conventions** ([simulation-patterns.md](references/simulation-patterns.md)): Short noun-phrase captions, `"… are shown in Fig. X. It can be observed that …"` body narration, `booktabs` three-line tables, and `matlab/p1ot.m` figure styling.
- **Ready-to-compile IEEEtran LaTeX skeleton**: `assets/duan-hofas-paper-template.tex`.

## Project structure

```text
duan-hofas/
├── SKILL.md                           # Main skill instructions, 4 modes & alignment rules
├── README.md                          # Documentation (English)
├── README_zh-CN.md                    # Documentation (Simplified Chinese)
├── package.json                       # @hiden0ri/duan-hofas-skill package manifest
├── agents/
│   └── openai.yaml                    # Codex UI display metadata & default prompt
├── assets/                            # Compilable manuscript template assets
│   └── duan-hofas-paper-template.tex  # IEEEtran-compatible Duan-style LaTeX skeleton
├── references/                        # 28 distilled knowledge, corpus & template handbooks
│   ├── duan-writing-corpus.md         # Verbatim Duan writing corpus & phrasebook
│   ├── fas-advantages-corpus.md       # FAS advantages, method comparisons & objective boundaries (53 passages)
│   ├── canonical-definitions-index.md # Thematic index & verbatim templates of 109 classic Duan definitions
│   ├── duan-series-templates.md       # 5-series structural templates (AAS/IJSS/SCIS/UC-FAS/OD-FAS)
│   ├── theorem-writing-template.md    # 867-environment template bank (T1–T6, L1–L6, P1–P5, C1–C4...)
│   ├── proof-templates.md             # 3 proof modes (M1–M3) & 12 proof skeletons (PT-1 to PT-12)
│   ├── corpus-conflict-resolution.md  # Empirical audit of 10 cross-corpus conflicts (Check vs Draft)
│   ├── corpus-guide.md                # Guide to local full-text MD corpus, sorted banks & FTS5 DB
│   ├── backup-fas-library.md          # Graded secondary backup FAS library (1,041 papers, 0–5 tiers) guide
│   └── ...                            # +19 specialized notation, model, lemma & audit references
├── scripts/                           # 13 corpus, sorter, search, packager & validator tools
│   ├── build_papers_corpus.py         # PDF -> column-ordered, lossless font-decoded MD + SQLite FTS5
│   ├── sort_corpus_environments.py    # 984-block environment & proof sorter
│   ├── build_classic_definitions_bank.py # 109-definition (94 formal + 15 prose) thematic sorter
│   ├── build_fas_advantages_bank.py   # 53-passage FAS advantages, comparisons & boundaries sorter
│   ├── search_corpus.py               # Primary canonical FTS5 & landmark search (32 papers + Vol. I)
│   ├── search_backup_fas.py           # Graded secondary backup FAS library search (1,041 papers, 0–5 tiers)
│   ├── build_release_packages.py      # Builds .skill, .zip, .tar.gz, npm .tgz & SHA256SUMS
│   ├── validate_distillation.py       # Structural link, math delimiter & file validator
│   └── ...                            # +5 Volume I indexing/extraction & Zotero inventory scripts
├── reports/                           # [Gitignored local historical distillation & audit logs]
└── corpus/                            # Corpus directory (sorted/ tracked; papers/ & backup_fas/ gitignored)
    ├── sorted/*.md & summary_stats.json # [Tracked] 13 sorted banks (984 blocks + 109 defs + 53 advantages)
    ├── INDEX.md & manifest.json       # [Gitignored] Local 32-paper catalog symlinks
    ├── papers/*.md                    # [Gitignored] Local 32 full-text paper symlinks
    └── backup_fas/                    # [Gitignored] Local 1,041-paper graded backup FAS library symlink
```

## Asset & knowledge libraries

### 1. Manuscript Template Assets (`assets/`)
- `assets/duan-hofas-paper-template.tex`: Ready-to-compile LaTeX manuscript skeleton (`IEEEtran` journal class with automatic `article` fallback). Preconfigures `Definition`, `Assumption`, `Problem`, `Lemma`, `Proposition`, `Theorem`, `Corollary`, `Remark`, and `Example` environments; macros `\xstack`, `\Arow`, `\Phic`; a 5-part Duan abstract; an ~1.5-page Introduction layout ending with an italic `Notations:` paragraph (unnumbered `equation*` using `=`); a `booktabs` three-line table (`\toprule`/`\midrule`/`\bottomrule`); and standard HOFAS/sub-FAS controller and state-space closed-loop sections.

### 2. Distilled Reference & Template Library (`references/` — 28 files)
| Module | Files & Scope |
|---|---|
| **Writing Corpus, Advantages & Series Templates** | [duan-writing-corpus.md](references/duan-writing-corpus.md) (verbatim `[E]` sentences, connector phrasebook, Anti-AI table), [fas-advantages-corpus.md](references/fas-advantages-corpus.md) (7-dimension FAS advantages, method comparisons vs backstepping/feedback linearization/state-space, & anti-exaggeration boundaries), [duan-series-templates.md](references/duan-series-templates.md) (*Acta Automatica Sinica* `I–III`, *IJSS* `I–X`, *SCIS* Delay/Chained, *UC-FAS* `I–III`, *OD-FAS* `1 & 4`), [duan-style-quick-guide.md](references/duan-style-quick-guide.md), [duan-first-author-habits.md](references/duan-first-author-habits.md), [writing-style.md](references/writing-style.md) |
| **Formal Environment & Proof Banks** | [theorem-writing-template.md](references/theorem-writing-template.md) (`T1–T6`, `L1–L6`, `P1–P5`, `C1–C4`, `D1–D2`, `Pr1–Pr3`, `R1–R5` distilled from 867 environments), [proof-templates.md](references/proof-templates.md) (`M1–M3` placement modes & `PT-1` to `PT-12` proof skeletons), [corpus-conflict-resolution.md](references/corpus-conflict-resolution.md) (10 cross-corpus conflicts & Check-vs-Draft table), [derivation-patterns.md](references/derivation-patterns.md), [canonical-theorems.md](references/canonical-theorems.md), [common-assumptions.md](references/common-assumptions.md), [common-lemmas.md](references/common-lemmas.md) |
| **Classic Definitions, Symbols & Models** | [canonical-definitions-index.md](references/canonical-definitions-index.md) (9-theme index & verbatim templates of 109 classic definitions), [concepts-and-notation.md](references/concepts-and-notation.md), [symbol-dictionary.md](references/symbol-dictionary.md), [model-definition-registry.md](references/model-definition-registry.md) (regularity of $f,B$ by control objective), [concept-lineage.md](references/concept-lineage.md), [coauthored-comparison.md](references/coauthored-comparison.md) |
| **Examples, Plots & Rigor Audit** | [example-library.md](references/example-library.md), [simulation-patterns.md](references/simulation-patterns.md) (`matlab/p1ot.m` plotting & short captions), [frequently-cited-references.md](references/frequently-cited-references.md), [rigor-audit.md](references/rigor-audit.md), [adversarial-tests.md](references/adversarial-tests.md) |
| **Source, Corpus & Backup Library Guides** | [corpus-guide.md](references/corpus-guide.md), [backup-fas-library.md](references/backup-fas-library.md), [source-catalog.md](references/source-catalog.md), [volume1-authority.md](references/volume1-authority.md) |

### 3. Automation, Packaging & Retrieval Scripts (`scripts/` — 13 tools)
- **Full-Text Corpus & Thematic Sorters**: `scripts/build_papers_corpus.py` (converts 32 PDFs to column-ordered, losslessly font-decoded `.md` + unified FTS5 DB), `scripts/sort_corpus_environments.py` (sorts all 867 environments + 117 proofs into 10 verbatim banks), `scripts/build_classic_definitions_bank.py` (sorts 109 classic definitions across 9 themes), `scripts/build_fas_advantages_bank.py` (sorts 53 FAS advantage/comparison/boundary passages across 7 dimensions), `scripts/search_corpus.py` (primary canonical CLI search by `--query`, `--literal`, `--label`, `--kind`, `--series`), `scripts/search_backup_fas.py` (secondary graded backup library search by `--score`, `--min-score`, `--sort-by-score`, `--kind`, `--literal`).
- **Monograph & Zotero Utilities**: `scripts/build_volume1_index.py`, `scripts/search_volume1.py`, `scripts/extract_volume1_pages.py` (513-page *Volume I* SQLite FTS5 indexing & page extraction); `scripts/inventory_duan_first_author.py`, `scripts/inventory_local_sources.py` (local Zotero PDF cataloging).
- **Skill Validator & Release Packager**: `scripts/validate_distillation.py` (verifies all 29 required knowledge files, internal Markdown links, and `$...$`/`$$...$$` math delimiters); `scripts/build_release_packages.py` (builds copyright-safe `.skill`, `.zip`, `.tar.gz`, npm `.tgz`, and `SHA256SUMS.txt`).

### 4. Bundled Sorted Banks (`corpus/sorted/`) & Gitignored Full-Text Cache (`~/.cache/duan-hofas/`)
Balancing out-of-the-box completeness with publisher copyright compliance:
- **Shipped in Git & Release Archives (`corpus/sorted/`, 13 files, 981 KB)**: Ready out of the box with all **984 sorted formal-environment & proof blocks** (`theorems.md` [198], `assumptions.md` [165], `remarks.md` [155], `proofs.md` [117], `definitions.md` [94], `lemmas.md` [80], `propositions.md` [76], `corollaries.md` [65], `problems.md` [24], `conditions.md` [10], `summary_stats.json`), **109 classic definitions** (`classic_definitions_by_topic.md`), and **53 FAS advantage/boundary passages** (`fas_advantages_by_theme.md`).
- **Local Copyright-Isolated Cache (`~/.cache/duan-hofas/`, gitignored)**: Complete full-text papers (`corpus/papers/*.md`) and SQLite FTS5 databases (`duan_corpus.sqlite`, `volume1.sqlite`) stay strictly local via gitignored symlinks.

## Installation

### Ubuntu / Linux

Clone into Codex's skill directory and (optionally) link into Claude Code and Antigravity so all three assistants share a single source of truth:

```bash
sudo apt update && sudo apt install -y git
mkdir -p "$HOME/.codex/skills" "$HOME/.claude/skills" "$HOME/.gemini/config/skills"
git clone https://github.com/Hiden0ri/duan-hofas-skill.git "$HOME/.codex/skills/duan-hofas"
ln -s "$HOME/.codex/skills/duan-hofas" "$HOME/.claude/skills/duan-hofas"
ln -s "$HOME/.codex/skills/duan-hofas" "$HOME/.gemini/config/skills/duan-hofas"
```

### macOS

```bash
brew install git
mkdir -p "$HOME/.codex/skills" "$HOME/.claude/skills" "$HOME/.gemini/config/skills"
git clone https://github.com/Hiden0ri/duan-hofas-skill.git "$HOME/.codex/skills/duan-hofas"
ln -s "$HOME/.codex/skills/duan-hofas" "$HOME/.claude/skills/duan-hofas"
ln -s "$HOME/.codex/skills/duan-hofas" "$HOME/.gemini/config/skills/duan-hofas"
```

If Homebrew is unavailable, run `xcode-select --install` first.

### Windows 11 (PowerShell)

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/Hiden0ri/duan-hofas-skill.git "$env:USERPROFILE\.codex\skills\duan-hofas"
```

Restart your agent session after installation.

## Update & validation

Ubuntu and macOS:

```bash
git -C "$HOME/.codex/skills/duan-hofas" pull
python3 "$HOME/.codex/skills/duan-hofas/scripts/validate_distillation.py"
```

Windows PowerShell:

```powershell
git -C "$env:USERPROFILE\.codex\skills\duan-hofas" pull
python "$env:USERPROFILE\.codex\skills\duan-hofas\scripts\validate_distillation.py"
```

## Usage examples

Invoke `duan-hofas` (e.g., `$duan-hofas` in Codex or direct invocation in Claude Code / Antigravity), then state your goal directly. Note that by default the skill **provides a concrete revision scheme first** and modifies files only when you explicitly say `"改"` / `"动手"` (or give a direct edit command such as `"去掉…"` / `"调整…"`).

### 1. Draft or polish prose in Duan's authentic voice

```text
按 Duan 的原文语料库润色这一节，保留或改用 Duan 常用句式，去掉 AI 味的防御性否定句。
```

### 2. Check symbols, concepts, and mathematical formulas

```text
检查这篇稿件的符号、Notations 段和模型变量交代是否符合 Duan 的习惯。
```

Expected review format:

```text
位置 → 当前写法 → 推荐的 Duan 写法 → 理由 → [E]/[D]/[U]
```

### 3. Check or write Theorems, Lemmas, Propositions, and Corollaries

```text
检查文中所有 Theorem、Lemma、Proposition、Corollary 是否在陈述本身直接写出了最终目的，并符合 Duan 的六段式结构。
```

### 4. Draft or audit a proof (substitution, ROEA, contradiction, high-order backstepping)

```text
按 Duan & Zhou (2022) Lemma 4.4 的反证法模板重写这个引理的证明。
```

```text
按 Duan 高阶反步法（Part III / Volume I 第 9 章）的标准分步结构起草这一节的推导与主定理。
```

### 5. Check Definitions, Assumptions, and Remarks

```text
检查这里的 Definition、Assumption 和 Remark 边界是否清晰，有没有把本文新增条件混进 Duan 原始定义里。
```

### 6. Check Examples, captions, and MATLAB figure conventions

```text
检查仿真章节的引图句式、短图题、三线表以及 MATLAB 画图脚本是否符合 Duan 习惯和 p1ot.m 规范。
```

### 7. Create a Duan-style IEEEtran LaTeX template

```text
创建一个 Duan 风格的单阶切换 sub-FAS 论文 LaTeX 模板。
```

### 8. Verify a disputed expression or equation against primary sources

```text
核对这句话或这个正则性条件出自 Duan 的哪篇原文，给出准确出处标注 [E]/[D]/[U]。
```

## Optional local full-text corpus & FTS5 search (Plan A)

To respect publisher copyright on public GitHub, the repository does not distribute copyrighted PDFs, converted full-text `.md` papers, or prebuilt SQLite databases. Instead, on a machine with local Zotero PDFs, run:

```bash
python3 scripts/build_papers_corpus.py
python3 scripts/sort_corpus_environments.py
python3 scripts/build_classic_definitions_bank.py
python3 scripts/build_fas_advantages_bank.py
ln -sfn "$HOME/.cache/duan-hofas/corpus" corpus
python3 scripts/search_corpus.py --list-docs
```

This generates column-ordered, losslessly font-decoded structured Markdown full texts (`~/.cache/duan-hofas/corpus/papers/*.md`), 10 exhaustively sorted formal-environment and proof banks totaling 984 blocks plus 109 classic definitions and 53 FAS advantage/boundary passages (`~/.cache/duan-hofas/corpus/sorted/*.md`, gitignored via `corpus` symlink), and a unified SQLite FTS5 index (`~/.cache/duan-hofas/duan_corpus.sqlite`) across all 32 Duan first-author papers plus the 513-page *Volume I* monograph; see [references/corpus-guide.md](references/corpus-guide.md) and [references/corpus-conflict-resolution.md](references/corpus-conflict-resolution.md). Routine checking, drafting, and template generation work out of the box without building the local full-text cache.

## Important boundary

For source-faithful definitions of original-system variables, dimensions, and objective-dependent conditions on $f$ and $B$, read [references/model-definition-registry.md](references/model-definition-registry.md). Select the model family and control objective first; never promote one paper's smoothness or nonsingularity condition to a universal HOFAS assumption, and never attribute paper-specific `[D]` extensions to Duan.


## Update history & maintenance notes

### Changelog

- **2026-11-24 (`v1.2.0`) — Primary Corpus Expanded to 36 Papers (`OD-FAS Part 2` + 3 Solo-Duan Papers) & Graded Secondary Backup FAS Library (1,041 Papers, 0–5 Tiers)**
  - Expanded the primary canonical corpus from 32 to **36 first-author Duan papers** (+ *Volume I*) by adding 4 sole-authored journal papers: `odfas_2026_part2` (*IJSS* 2026, completing *OD-FAS* multi-order output feedback), `scis_2025_chained3` (*SCIS* 2025, generalized chained systems: multi-vector case), `jssc_2022_brockett1`, and `jssc_2023_brockett2` (*JSSC* 2022/2023, Brockett's first & second examples). Rebuilt all sorted banks to **1,065 verbatim blocks** (939 formal environments + 126 explicit `Proof` blocks, +81 blocks) and **114 classic definitions** (99 formal + 15 prose), verified 0 PUA, 0 `U+FFFD`, and 0 line-number mismatches.
  - Added `scripts/search_backup_fas.py` and [backup-fas-library.md](references/backup-fas-library.md), establishing a two-tier retrieval architecture in [SKILL.md](SKILL.md) and [corpus-guide.md](references/corpus-guide.md) (primary Duan canonical corpus + secondary graded FAS backup library).
  - Mounted the local graded FAS library via gitignored `corpus/backup_fas/` symlink (1,041 deduplicated journal & conference papers, 10,097 pages, 7,673 landmarks): Score 5 (33 solo-Duan journal papers + 1 *IEEE TAC* + 6 *Automatica*), Score 4 (191 papers across 24 flagship IEEE/ASME & CAS-Q1-Top journals), Score 3 (212 mainstream control SCI / *Acta Automatica Sinica* / *Acta Aeronautica*), Score 2 (45 general journals), Score 1 (541 conference papers + 8 MDPI), Score 0 (4 *IEEE Access*), with `--score` / `--min-score` / `--sort-by-score` filtering while strictly prohibiting non-Duan papers from overriding primary Duan canonical conventions.
- **2026-11-18 (`v1.1.0`) — 109-Definition Index, 53-Passage FAS Advantages Corpus & Lossless Math Font Decoding**
  - Added `scripts/build_classic_definitions_bank.py` and [canonical-definitions-index.md](references/canonical-definitions-index.md), indexing and distilling **109 classic Duan definitions** (94 formal `Definition`s + 15 prose/theorem definitions, including primary-source verification of discrete step-forward $x^{\lfloor i\rfloor}(k)=x(k+i)$ vs step-backward $x^{\lceil i\rceil}(k)=x(k-i)$).
  - Added `scripts/build_fas_advantages_bank.py` and [fas-advantages-corpus.md](references/fas-advantages-corpus.md), categorizing **53 primary-source passages** `[E]` across 7 dimensions covering FAS modeling philosophy, LTI DOFs, comparisons with backstepping and feedback linearization, controllability unification, anti-disturbance/delay/UC-FAS/OD-FAS, and anti-exaggeration objective boundaries.
  - Upgraded `scripts/build_papers_corpus.py` and `scripts/sort_corpus_environments.py` with lossless multi-codepoint ligatures, fallback `CMEX` big operators (`∑, ∏, ∫`), `EuclidMathTwo` blackboard bold (`𝔾, 𝕏, ℚ, 𝔽`), Founder `FZS_Extra_S92` braces, and preserved Greek math variants (`ϖ, ϑ, ϕ`), bringing the sorted corpus to **984 blocks** (867 formal environments + 117 `Proof` blocks, 0 uncaptured landmarks, 0 header/footnote leaks).
- **2026-11-17 (`b4107c3` – `f1a59d2`, `v1.0.0`) — 940-Block Sorted Template Banks, Conflict Reconciliation & Bilingual Docs**
  - Added `scripts/sort_corpus_environments.py` to exhaustively extract and sort **940 verbatim blocks** (823 formal environments + 117 explicit `Proof` blocks) across all 32 first-author papers + *Volume I* into 10 local category banks (`corpus/sorted/*.md`).
  - Rebuilt [theorem-writing-template.md](references/theorem-writing-template.md) (`T1–T6`, `L1–L6`, `P1–P5`, `C1–C4`, `D1–D2`, `Pr1–Pr3`, `R1–R5`) and [proof-templates.md](references/proof-templates.md) (`M1–M3` placement modes + `PT-1` to `PT-12` canonical proof skeletons) from the full sorted banks.
  - Added [corpus-conflict-resolution.md](references/corpus-conflict-resolution.md) auditing and resolving **10 cross-corpus variations** with empirical counts and Check-vs-Draft rules (`:=` `0/32` vs `\triangleq`/`=`, `Let` `63.7%` vs `Suppose` `12.1%`, bare vs verbal proof closers, `ROEA`/`RoEA`, `Hurwitz`/`stable`/`Schur`, etc.).
  - Added switchable Chinese documentation ([README_zh-CN.md](README_zh-CN.md)), visual project tree, and 4-layer asset library documentation.
- **2026-11-16 (`8b39b3d` – `b42a7cb`) — 32-Paper Full-Series Distillation, Full-Text Markdown Corpus & Unified FTS5 Search**
  - Added [duan-writing-corpus.md](references/duan-writing-corpus.md) and [duan-series-templates.md](references/duan-series-templates.md), completing verbatim & structural distillation across all 5 major Duan FAS series: Chinese *Acta Automatica Sinica* (`I–III`) / *Acta Aeronautica*, *IJSS* (`Part I–X` + Underactuated), *SCIS* Discrete/Continuous Delay & Generalized Chained series, *UC-FAS* (`Part I–III`), and *OD-FAS* (`Part 1 & Part 4`).
  - Added `scripts/build_papers_corpus.py`, `scripts/search_corpus.py`, and [corpus-guide.md](references/corpus-guide.md) featuring two-column layout reconstruction, Computer Modern / Y&Y Type-1 math font decoding (verified 0 PUA, 0 `U+FFFD`, and 0-offset landmark line numbers), and unified SQLite FTS5 search across 32 papers + *Volume I*.
  - Unified multi-agent configuration across **Antigravity**, **Claude Code**, and **Codex**.
- **2026-09-09 – 2026-09-10 (`c245800` – `d81fa43`) — Objective-Specific Model Registry & Editing Protocol**
  - Added [model-definition-registry.md](references/model-definition-registry.md) distinguishing original-system variables, dimensions, and objective-dependent regularity of $f$ and $B$ (`unspecified` vs `piecewise continuous` vs `smooth`).
  - Refined `Notations:` vs paper-local symbol placement rules and safe LaTeX backup/compile workflows.
- **2026-09-08 (`790833f` – `0bee51e`) — Initial Release & *Volume I* Foundation**
  - Initial release of `duan-hofas` with 513-page *Volume I* SQLite FTS5 indexing (`scripts/build_volume1_index.py`, `scripts/search_volume1.py`), core concept/symbol dictionaries, recurring assumptions/lemmas/citations guides, `assets/duan-hofas-paper-template.tex`, and Linux/macOS/Windows setup guides.

### Maintenance & coverage notes

1. **Routine updates vs. local cache rebuilds**: Pulling new skill updates (`git pull` + `python3 scripts/validate_distillation.py`) updates all 28 required knowledge files, templates, and rules immediately across linked agents. Re-running `build_papers_corpus.py` and the sorter scripts is needed **only** when new Duan PDFs are added to local Zotero storage.
2. **Current source coverage & pending PDFs**: The primary canonical corpus now indexes **36 local Duan first-author FAS papers** (32 English + 4 Chinese, 2020–2026) plus the 2026 Springer monograph *Volume I* (513 pp.), yielding **1,065 sorted blocks** (939 formal environments + 126 `Proof` blocks) and **114 classic definitions**. Within the 2026 *OD-FAS* series, `Part 1`, `Part 2`, and `Part 4` are now included locally (only `Part 3` remains pending). The secondary graded backup library covers **1,041** community FAS journal & conference papers (0–5 tiers).
3. **Copyright & repository hygiene**: `corpus/sorted/` ships with the repository, whereas full-text papers (`corpus/papers/`, `corpus/INDEX.md`, `corpus/manifest.json`) and `*.sqlite` databases remain strictly gitignored. Never force-add full-text `.md` papers or publisher PDFs to public commits, and always run `scripts/validate_distillation.py` before pushing.

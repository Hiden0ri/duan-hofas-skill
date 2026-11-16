# Duan HOFAS Skill

A unified skill (for **Antigravity**, **Claude Code**, and **Codex**) for checking, drafting, and polishing HOFAS / FAS / sub-FAS / switched sub-FAS Markdown files and LaTeX manuscripts using **Guang-Ren Duan's authentic vocabulary, sentence patterns, notation, article organization, formal environments, and proof templates**. It also provides a compilable IEEEtran-compatible Duan-style LaTeX manuscript skeleton.

## Core capabilities

- **Corpus-backed Duan-style drafting & polishing** ([duan-writing-corpus.md](references/duan-writing-corpus.md)): Write and revise manuscripts using verbatim `[E]` expressions distilled from 22 first-author Duan papers and the 2026 monograph *Fully Actuated System Approach, Volume I*, preserving Duan's signature phrasing (`"the feasible set clearly has the following expression:"`, `"we construct the following controller:"`, `"is equivalent to the following state-space form:"`, `"The above result converts/reveals..."`) while eliminating AI-flavored `"not X, but Y"` defensive disclaimers and single-claim meta-previews.
- **Duan-first concept & notation alignment** ([duan-style-quick-guide.md](references/duan-style-quick-guide.md), [concepts-and-notation.md](references/concepts-and-notation.md)): Prioritize Duan's established concepts and symbols ($\varphi_0,\varphi_\infty,\varphi$, $|\varphi_i|$, $\mathbb{S}/\mathcal{S}$, $\mathbb{F}/\mathcal{F}$, substability, ROEA/RoEA, $X_0=x^{(0\sim n-1)}(0)$, end-of-Introduction `Notations:` with `=` and unnumbered `equation*`, no `:=` or `\col`), introducing new `[D]` objects only where Duan has no counterpart.
- **Strict provenance discipline (`[E]` / `[D]` / `[U]`)** ([model-definition-registry.md](references/model-definition-registry.md)): Keep Duan's original definitions/assumptions strictly separate from paper-added `[D]` conditions and `[U]` unverified items; never read unstated smoothness or topological assumptions into Duan's texts.
- **Formal environment templates & explicit-goal rule** ([theorem-writing-template.md](references/theorem-writing-template.md)): Standardize `Problem`, `Definition`, `Assumption`/`Condition`, `Lemma`, `Proposition`, `Theorem` (6-part structure + `Then 1)...; 2)...`), `Corollary`, and `Remark` (6 roles), enforcing that **every `Theorem`, `Lemma`, `Proposition`, and `Corollary` states its final purpose directly inside its own statement**.
- **Eight canonical Duan proof structures** ([proof-templates.md](references/proof-templates.md)):
  1. Direct substitution + state-space form + Lyapunov decay;
  2. SUB-FAS substabilization & exact ROEA characterization (`Duan 2023 TCYB`);
  3. Proof by contradiction (`Duan & Zhou 2022`, Lemma 4.4: `"Suppose that … Then it follows from … On the other side, … This yields a contradiction. Thus … The proof is finished."`);
  4. High-order backstepping (`Part III` §4 / `Volume I` §9.2 with $\tilde P_i(A_i^{0\sim m_i-1})=\mathring{I}P_i$ and telescoping Lyapunov sum);
  5. Sufficiency & necessity (`Sufficiency:` / `Necessity:` / `"Combining the above two aspects..."`);
  6. Multi-conclusion & multi-step proofs;
  7. Order-raising elimination & mathematical induction (both forward and inverse directions);
  8. Monotonic-interval splitting & finite stationary-point ROEA reduction (`Duan & Wang 2026`).
- **Examples, captions, tables & MATLAB figure conventions** ([simulation-patterns.md](references/simulation-patterns.md)): Short noun-phrase captions, `"… are shown in Fig. X. It can be observed that …"` body narration, `booktabs` three-line tables, and `matlab/p1ot.m` figure styling.
- **Ready-to-compile IEEEtran LaTeX skeleton**: `assets/duan-hofas-paper-template.tex`.

## Repository layout

| Path | Role |
|---|---|
| [SKILL.md](SKILL.md) | Skill entry point, operating modes, non-negotiable alignment rules, and LaTeX edit/compile protocol |
| [references/duan-writing-corpus.md](references/duan-writing-corpus.md) | **Flagship verbatim Duan writing corpus**: section templates, 7 formal environments, 8 proof structures, connector phrasebook, and Anti-AI Do-vs-Don't table |
| [references/duan-series-templates.md](references/duan-series-templates.md) | **Series-specific structural templates & verbatim corpus**: OD-FAS (`Part 1 & 4`), UC-FAS (`Part I–III`), IJSS (`Part VI & X`), SCIS Delay/Chained series, and Chinese *Acta Automatica Sinica* (`I–III`) / *Acta Aeronautica* norms |
| [references/duan-style-quick-guide.md](references/duan-style-quick-guide.md) | Fast checklist for notation, article organization, switched sub-FAS extensions, and plotting |
| [references/theorem-writing-template.md](references/theorem-writing-template.md) | Six-part Theorem structure plus `Lemma`, `Proposition`, `Corollary`, and `Problem` templates |
| [references/proof-templates.md](references/proof-templates.md) | Executable fill-in skeletons for Duan's canonical proof types |
| [references/model-definition-registry.md](references/model-definition-registry.md) | Objective-specific original-system variables, dimensions, and regularity of $f$ and $B$ |
| [references/concepts-and-notation.md](references/concepts-and-notation.md) & [references/symbol-dictionary.md](references/symbol-dictionary.md) | Canonical terminology, symbols, and scope collision checks |
| [references/duan-first-author-habits.md](references/duan-first-author-habits.md) & [references/writing-style.md](references/writing-style.md) | Empirical statistics and style discipline across Duan's first-author corpus |
| [references/common-assumptions.md](references/common-assumptions.md), [references/common-lemmas.md](references/common-lemmas.md), [references/canonical-theorems.md](references/canonical-theorems.md) | Indexed recurring assumptions, lemmas, and landmark theorems |
| `assets/duan-hofas-paper-template.tex` | Compilable IEEEtran LaTeX template following Duan's layout and `Notations:` standard |
| `scripts/validate_distillation.py` | Structural validator checking links, math delimiters, and required reference files |

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

## Optional local source search

The repository does not distribute copyrighted PDFs or prebuilt SQLite databases. Paths in [references/source-catalog.md](references/source-catalog.md) and defaults in `scripts/search_volume1.py` / `scripts/build_volume1_index.py` reflect the author's local research environment. On another machine, pass your local PDF/database paths via CLI flags if you need full-text monograph search; routine checking, drafting, and template generation work out of the box without any local PDF database.

## Important boundary

For source-faithful definitions of original-system variables, dimensions, and objective-dependent conditions on $f$ and $B$, read [references/model-definition-registry.md](references/model-definition-registry.md). Select the model family and control objective first; never promote one paper's smoothness or nonsingularity condition to a universal HOFAS assumption, and never attribute paper-specific `[D]` extensions to Duan.

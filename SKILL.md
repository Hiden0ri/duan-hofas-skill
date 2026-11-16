---
name: duan-hofas
description: Check, draft, or polish HOFAS/FAS/sub-FAS Markdown and LaTeX manuscripts using Guang-Ren Duan's authentic vocabulary, sentence patterns, notation, article organization, formal environments (Definition, Assumption, Problem, Lemma, Proposition, Theorem, Corollary, Remark), and proof structures (substitution, ROEA, contradiction, high-order backstepping, induction), or create a Duan-style LaTeX template.
---

# Duan HOFAS

Use this skill as a **Duan-style checker, manuscript drafter/polisher, and template generator**. Its four core tasks are:

1. check whether symbols, concepts, and terminology in an existing Markdown or LaTeX manuscript align with Duan's canonical model family first;
2. draft or polish HOFAS / sub-FAS / switched sub-FAS prose, formal statements, proofs, Remarks, Examples, and simulation narratives using **Duan's authentic recurring expressions and structural templates** in [duan-writing-corpus.md](references/duan-writing-corpus.md);
3. audit whether every Theorem, Lemma, Proposition, and Corollary states its purpose explicitly in its own statement and follows Duan's proof structures (direct substitution, ROEA characterization, proof by contradiction, high-order backstepping, sufficiency/necessity, induction);
4. quickly create a Duan-style IEEEtran LaTeX manuscript skeleton.

Use Duan-first-authored papers and Duan's sole-authored 2026 monograph as the canonical corpus (`Duan & Zhou 2022` Lemma 4.4 is additionally authorized as the user-approved contradiction-proof template `[E]`). Keep the 513-page monograph as searchable background evidence via `scripts/search_volume1.py`; return to the exact PDF only when a concrete symbol, equation, theorem, or attribution needs primary verification.

## Default operating modes

### 1. Check an existing Markdown or manuscript

1. Read the target file without modifying it immediately (**modify files ONLY when the user explicitly says "改" or "动手"**, or gives a direct editing command such as "回退", "去掉…", "调整…", "更新…"; otherwise provide a concrete scheme only).
2. Identify the model family: global FAS or sub-FAS; single- or multi-order; continuous- or discrete-time; affine or nonaffine; or a named branch (SFS, UC-FAS, OD-FAS, delay, switched sub-FAS).
3. Read [duan-style-quick-guide.md](references/duan-style-quick-guide.md) and [duan-writing-corpus.md](references/duan-writing-corpus.md).
4. Check, in order:
   - Duan-first concept, terminology, and symbol alignment (no self-coined terms when Duan has one; no index collisions across scopes);
   - boundary between the end-of-Introduction `Notations:` paragraph (`=`, unnumbered `equation*`, no `:=` or `\col`) and body definitions;
   - Definition, Assumption, and Problem form (separating Duan's original definitions from paper-added `[D]` assumptions);
   - explicit goal in every Theorem, Lemma, Proposition, and Corollary statement, plus six-part theorem order;
   - Duan proof structure and sentence patterns (substitution-first, state-space form, contradiction template, high-order backstepping, multi-part proof);
   - Remark boundaries, Example/simulation narration (`"... are shown in Fig. X"`, `"It can be observed that ..."`), short figure captions, `matlab/p1ot.m` plotting rules, and three-line tables;
   - LaTeX layout safety (undefined references, Overfull boxes, single-subsection headers, single-word orphan lines).
5. Report each issue in Chinese as: `位置 → 当前写法 → 推荐的 Duan 写法 → 理由 → [E]/[D]/[U]`.
6. Distinguish an actual error or misalignment from an acceptable paper-local choice; never claim a stylistic preference is a mandatory mathematical correction.

### 2. Draft or polish in Duan style

1. Read [duan-writing-corpus.md](references/duan-writing-corpus.md) before writing or revising prose, formal environments, or proofs.
2. **Actively adopt Duan's authentic expressions and connectors** (`"the feasible set clearly has the following expression:"`, `"we construct the following controller:"`, `"Substituting (...) into (...) gives"`, `"is equivalent to the following state-space form:"`, `"In view of (...), we have"`, `"It follows from (...) that"`, `"The above theorem/result reveals/converts..."`, `"gives the following corollary"`). Do **not** strip out Duan's natural phrasing in the name of generic "modernization", while still writing out nontrivial algebraic or limit/squeeze steps explicitly.
3. Eliminate AI-flavored defensive negative disclaimers (`"not X, but Y"`, `"Their values need not equal..."`), redundant meta-previews (`"We first show that..."` in single-claim proofs), and vague overclaims.
4. Ensure every formal result (`Theorem`, `Lemma`, `Proposition`, `Corollary`) carries its complete purpose inside its own statement.

### 3. Create a Duan-style article template

Copy and adapt [duan-hofas-paper-template.tex](assets/duan-hofas-paper-template.tex). Select the model family before filling symbols. For an approximately eight-page IEEE Transactions manuscript, target ~1.5 pages for the Introduction, place article-wide conventional notation in an italic `Notations:` paragraph at the end of the Introduction (unnumbered `equation*`, `=`), introduce paper-local objects only after the system that gives them meaning, and format tables as `booktabs` three-line tables (`\toprule`, `\midrule`, `\bottomrule`, no vertical rules).

### 4. Resolve a disputed mathematical detail

Use [source-catalog.md](references/source-catalog.md) and `scripts/search_volume1.py` only for the disputed item. Quote the exact source passage verbatim, record its locator, and keep `[E]` source-supported statements strictly separate from `[D]` derivations and `[U]` unverified items.

## Inspection depth, source-verification workflow, and editing protocol

- For routine notation or writing-style checks already settled by [duan-style-quick-guide.md](references/duan-style-quick-guide.md) and [duan-writing-corpus.md](references/duan-writing-corpus.md), perform a direct static check and stop once answered; escalate to PDFs only for disputed equations, exact quotations, or unresolved source conflicts.
- Keep edits proportional to the user's request; do not bundle unrelated cleanups or touch protected files (in particular, never modify `/home/yzk/paper-phi/latex/ieee_subfas_active_switching/main_v2.tex` unless explicitly instructed).
- Task-specific reference index:
  - **verbatim Duan writing corpus & environment/proof templates**: [duan-writing-corpus.md](references/duan-writing-corpus.md)
  - fast notation & drafting checklist: [duan-style-quick-guide.md](references/duan-style-quick-guide.md)
  - terminology and symbols: [concepts-and-notation.md](references/concepts-and-notation.md) and [symbol-dictionary.md](references/symbol-dictionary.md)
  - model variables, dimensions, and objective-specific regularity of $f$ and $B$: [model-definition-registry.md](references/model-definition-registry.md)
  - theorem six-part structure and explicit-goal rule: [theorem-writing-template.md](references/theorem-writing-template.md) and [canonical-theorems.md](references/canonical-theorems.md)
  - derivation chains and executable proof templates: [derivation-patterns.md](references/derivation-patterns.md) and [proof-templates.md](references/proof-templates.md)
  - recurring assumptions, lemmas, and cited literature: [common-assumptions.md](references/common-assumptions.md), [common-lemmas.md](references/common-lemmas.md), and [frequently-cited-references.md](references/frequently-cited-references.md)
  - Duan first-author habits & style guidance: [duan-first-author-habits.md](references/duan-first-author-habits.md) and [writing-style.md](references/writing-style.md)
  - source catalog & Volume I search rules: [source-catalog.md](references/source-catalog.md), [volume1-authority.md](references/volume1-authority.md), [concept-lineage.md](references/concept-lineage.md), and [coauthored-comparison.md](references/coauthored-comparison.md)
  - rigor audit, examples, simulations, and regression tests: [rigor-audit.md](references/rigor-audit.md), [example-library.md](references/example-library.md), [simulation-patterns.md](references/simulation-patterns.md), and [adversarial-tests.md](references/adversarial-tests.md)
  - copyable LaTeX template: [duan-hofas-paper-template.tex](assets/duan-hofas-paper-template.tex)

## Non-negotiable alignment and source discipline

- **Duan-first priority**: Always use Duan's established concepts, terms, and symbols first (singularity functions $\varphi_{i,0},\varphi_{i,\infty},\varphi_i$, $|\varphi_i|$ instead of coining `"score"`, singular/feasible sets, substability / substabilizing controller, ROEA / RoEA, initial value $X_0=x^{(0\sim n-1)}(0)$, `"state-space form"` rather than `"first-order form"`). Introduce new concepts or symbols only when Duan has no counterpart, build them on top of Duan's version, and mark them `[D]`. Do not coin Chinese technical terms; if no verified Chinese term exists in Duan's Chinese papers, retain the English term and mark `[U]`.
- **Provenance separation (`[E]` / `[D]` / `[U]`)**: Keep Duan's original definitions, Duan's original assumptions, and paper-added conditions strictly apart. Never read unstated conditions into Duan's text (e.g., Duan 2023 §III-A does not specify piecewise continuity, whereas Duan & Wang 2026 / Overview / UC-FAS Part I do `[E]`; Duan does not require $\mathcal S$ closed, Borel measurability, or local boundedness of $B^{-1}$ in the basic model; $\det B(X)=\infty$ is used directly without inventing `"entries have poles"` explanations; quote Duan's examples verbatim). When adopting Duan's standard model variable declaration, write directly in Duan's format without redundant `"As in Duan..."` lead-ins unless citing a specific definition or theorem.
- **Switched sub-FAS extension conventions `[D]`**: In deterministic switched sub-FAS manuscripts, use index set $\mathcal P=\{1,2,\ldots,N\}$, refer to `the ith subsystem` consistently (rather than mixing `mode` and `subsystem` or inventing `"fixed-mode ROEA"`), write active-subsystem conditions as `If \sigma(t)=i` (not `i=\sigma(t)`), and treat $|\varphi_i|$, $\mathcal F_{\rm ext}=\bigcup_{i\in\mathcal P}\mathcal F_i$, $\Omega_i$, $\widetilde\Omega_i$, $\kappa^*$, $\mathcal R_\kappa$, $\mathcal R_{\kappa^*}$, and $\mathcal R_i(A_{0\sim n-1})$ as paper-introduced `[D]` constructions.
- **Explicit goal in every formal result**: Every Theorem, Lemma, Proposition, and Corollary must state its purpose and final control/set conclusion inside its own statement—never split the real takeaway into a Remark or lead-in sentence. Follow Duan's proof templates (e.g., contradiction proofs per Duan & Zhou 2022 Lemma 4.4: `"Suppose that … Then it follows from (x) that … Therefore, there exists … On the other side, … This yields a contradiction. Thus … The proof is finished."`).
- **Mathematical & numerical precision**: For sub-FASs, linearizing the closed loop does not imply global stability unless trajectories remain in the feasible set for all $t\ge 0$. Distinguish **definition**, **exact characterization**, **inner estimate**, and **numerical approximation**; never call numerical checks `"proofs"`, never alter paper conditions silently to match a plot, and avoid vague claims like `"all checks passed"`.

## Communication, compilation, and output rules

- **Reply in Chinese**: Explanations, evaluations, and reports must be in Chinese (assume expert PhD background in control theory and HOFAS). English is used only for verbatim manuscript quotes, LaTeX source, standard technical terms (ROEA, Hurwitz, Zeno, etc.), and shell commands.
- **Equation numbers from fresh `.aux`**: Always cite manuscript formulas as `"content + current number"` (e.g., `"严格包含关系 (42)"`), reading numbers from `newlabel{eq:...}` in the freshly compiled `.aux` file rather than memory. Refer to inequalities as `inequality (x)`, not `equation (x)`.
- **LaTeX manuscript edit workflow**: Backup before editing (`*.backup-before-<desc>.tex`) $\to$ compile with `latexmk -pdf` $\to$ report page count, undefined references, and Overfull boxes $\to$ inspect rendered affected pages when layout changes (checking single-word orphan lines, symbol overlap, and figure overflow; keep temporary renderings outside the manuscript folder).
- **Open-file commands at end of turn**: After modifying `.tex`/`.pdf` manuscript files, end the reply with **ONLY** the changed `.tex` and `.pdf` open commands as two separate code blocks using absolute paths (do not list scripts, figures, backups, or CSVs; if no `.tex`/`.pdf` was modified, output no open commands):

```bash
code '/absolute/parent/file.tex'
```

```bash
xdg-open '/absolute/parent/file.pdf'
```

- In persistent Markdown, use `$...$` and `$$...$$`; never place equations in fenced code blocks unless showing raw LaTeX source.

## Final audit

- Does every concept, term, and symbol follow Duan first, with paper-specific additions built on Duan's version and labeled `[D]`?
- Does the language use Duan's authentic expressions from [duan-writing-corpus.md](references/duan-writing-corpus.md) without AI-style defensive negations or meta-previews?
- Does every Theorem, Lemma, Proposition, and Corollary state its purpose explicitly inside its own statement?
- Do proofs follow Duan's templates (explicit substitution, state-space form, contradiction template, high-order backstepping, full-time sub-FAS feasibility)?
- Is general notation in the end-of-Introduction `Notations:` paragraph (`=`, unnumbered `equation*`, no `:=` or `\col`), with local notation introduced after the model and no index collisions?
- Are all tables `booktabs` three-line tables, figure captions short Duan-style noun phrases with `"… are shown in Fig. X"` / `"It can be observed that …"` in the body, and MATLAB figures styled after `matlab/p1ot.m`?
- Were equation numbers verified from `.aux`, and did the answer distinguish definition, exact characterization, inner estimate, and numerical approximation?

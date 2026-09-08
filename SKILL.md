---
name: duan-hofas
description: Check HOFAS Markdown and manuscripts against Guang-Ren Duan's notation, terminology, article organization, and theorem-writing habits, or quickly create a Duan-style LaTeX paper template. Use when the user asks whether symbols or writing conform to Duan, requests Duan-style revision, or starts a FAS/HOFAS/SUB-FAS manuscript.
---

# Duan HOFAS

Use this skill primarily as a **Duan-style checker and template generator**. Its three normal tasks are:

1. check whether symbols and terminology in an existing Markdown or manuscript agree with the relevant Duan model family;
2. check whether article organization, theorem statements, proofs, Remarks, Examples, and simulations follow Duan's recurring writing habits;
3. quickly create a Duan-style LaTeX manuscript skeleton.

Use Duan-first-authored papers and Duan's sole-authored book as the canonical corpus. Keep the monograph as searchable background evidence; do not decompose it into theorem or proof cards. Return to the exact source only when a concrete symbol, equation, theorem, or attribution needs verification.

## Default operating modes

### Check an existing Markdown or manuscript

1. Read the target file without rewriting it immediately.
2. Identify the model family: global or sub-FAS; single- or multi-order; continuous- or discrete-time; affine or nonaffine; or a named branch.
3. Read [duan-style-quick-guide.md](references/duan-style-quick-guide.md).
4. Check, in order:
   - symbol consistency and dimensions;
   - terminology and capitalization;
   - definition and assumption form;
   - theorem six-part structure;
   - proof organization;
   - Remark, Example, and simulation organization;
   - Markdown/LaTeX rendering safety.
5. Report each issue as: location → current form → recommended Duan form → reason → confidence/source status.
6. Distinguish an actual inconsistency from an acceptable paper-local choice. Do not mechanically replace every symbol merely because another Duan paper uses a different branch convention.
7. Edit the target only when the user asks for correction.

### Create a Duan-style article template

Copy and adapt [duan-hofas-paper-template.tex](assets/duan-hofas-paper-template.tex). Select the model family before filling symbols. Preserve the six-part theorem order and substitution-first proof order. Leave explicit placeholders rather than inventing assumptions, conditions, or results.

### Resolve a disputed mathematical detail

Use the source catalog and monograph search backend only for the disputed item. Quote or transcribe only the minimum source passage needed, record its locator, and keep source-supported statements separate from new derivations.

## Inspection depth and stopping rule

For routine notation or writing-style checks, when the target Markdown/LaTeX source and the relevant skill references already provide the needed rule, perform a direct static comparison and stop once the requested audit is answered.

- Do not reopen, browse, or render Duan source PDFs merely to reconfirm notation, typography, or definitions already settled by this skill.
- Escalate to the original source only when the skill references do not settle the point, authoritative sources conflict, an exact quotation, equation locator, or typographic distinction materially affects the answer, or the user explicitly asks for primary-source verification.
- When escalation is necessary, search or extract source text first. Render PDF page images only when visual layout or glyph form is itself disputed, or reliable text extraction is unavailable.
- Do not expand a notation check into a source-history, mathematical-rigor, or full-manuscript audit unless the user requests that broader scope.

## Source-verification workflow

When the quick guide cannot settle a concrete issue:

1. Open [source-catalog.md](references/source-catalog.md) and select the primary source. Prefer the 2026 open-access monograph for consolidated global-FAS notation, then the original paper for a branch-specific result. For the 513-page monograph, follow [volume1-authority.md](references/volume1-authority.md) and inspect only relevant pages.
2. Read only the task-specific reference:
   - fast default for notation and writing: [duan-style-quick-guide.md](references/duan-style-quick-guide.md)
   - terminology and symbols: [concepts-and-notation.md](references/concepts-and-notation.md)
   - full symbol dictionary and scope rules: [symbol-dictionary.md](references/symbol-dictionary.md)
   - modeling and proof chain: [derivation-patterns.md](references/derivation-patterns.md)
   - theorem statements and hypotheses: [canonical-theorems.md](references/canonical-theorems.md)
   - recurring source-indexed assumptions: [common-assumptions.md](references/common-assumptions.md)
   - recurring lemma families: [common-lemmas.md](references/common-lemmas.md)
   - references repeatedly cited across the local Duan corpus: [frequently-cited-references.md](references/frequently-cited-references.md)
   - manuscript drafting: [writing-style.md](references/writing-style.md) and [duan-first-author-habits.md](references/duan-first-author-habits.md)
   - theorem drafting from the user's “Duan规范” note: [theorem-writing-template.md](references/theorem-writing-template.md)
   - MATLAB reproduction or examples: [simulation-patterns.md](references/simulation-patterns.md)
   - concept origin or evolution: [concept-lineage.md](references/concept-lineage.md)
   - theorem derivation or proof checking: [proof-templates.md](references/proof-templates.md)
   - rigor review or TAC/Automatica adaptation: [rigor-audit.md](references/rigor-audit.md)
   - selection of a structurally similar example: [example-library.md](references/example-library.md)
   - behavioral regression testing after skill edits: [adversarial-tests.md](references/adversarial-tests.md)
   - comparison with coauthored or later community usage: [coauthored-comparison.md](references/coauthored-comparison.md); do not use this file to infer Duan-first-author habits
   - copyable LaTeX drafting skeleton: [duan-hofas-paper-template.tex](assets/duan-hofas-paper-template.tex)
3. Separate every claim as `[E]` source-supported, `[D]` derived or newly proposed, or `[U]` unresolved. Never attribute `[D]` or `[U]` to Duan.
4. Preserve the selected source's variables, dimensions, quantifiers, assumptions, equation order, and terminology.
5. Produce separate **Duan-faithful** and **rigor-enhancement** layers when modern rigor adds requirements absent from the source.

## Non-negotiable source discipline

- Do not coin Chinese technical terms. Use Duan's established terminology; if no verified Chinese term exists, retain the English original in parentheses and mark `[U]`.
- Keep source provenance separate from notation consistency. A paper may introduce symbols for a new extension without pretending that they are Duan's original symbols or definitions. Mark such paper-local constructions as `[D]`; retain them when they are explicitly defined, dimensionally valid, and internally consistent, but never describe them as "following," "inheriting," or "using" Duan's definition unless the cited source actually contains that definition.
- For the current switched SUB-FAS extension, $\mathcal F_{\rm ext}$, $\beta_i$, $h$, $q_i$, $\pi$, $\kappa$, $\mathscr K$, $\mathcal R_s(\kappa)$, and $\mathcal R_s^{\max}$ are paper-introduced notation `[D]`. They may remain in the manuscript, but a Duan-style audit must not replace them merely because they are absent from Duan's notation, and must not attribute them to Duan.
- Distinguish the physical state, elementary state vector, $x^{(0\sim n)}$, external vector, and dummy variables used in set definitions.
- “Controller makes the closed loop linear” does not by itself prove global stabilization for a sub-FAS. The trajectory must remain in the feasible set.
- Do not state that an ROEA has a closed-form expression unless the source proves one. A trajectory-defined characterization is valid.
- Do not alter paper conditions merely to reproduce a plot. State why any modification is necessary before making it.
- Do not treat later community extensions as Duan's original result merely because they use the FAS approach.
- Volume I is authoritative for global FASs, but it does not replace the dedicated SUB-FAS, substability, ROEA, delay, or later-volume sources.
- Distinguish **core notation** repeated across the corpus from **branch-local notation** introduced for uncertainty, delay, constraints, output feedback, or a single example. Never promote a branch-local symbol to a universal HOFAS convention.

## Output rules

- In Codex CLI explanations, use Unicode/plain-text formulas because display LaTeX may not render.
- In persistent Markdown, use `$...$` and `$$...$$`; never use LaTeX commands outside math delimiters and never place equations in fenced code blocks.
- In the Codex graphical client or LaTeX manuscript, use normal LaTeX.
- Give every created or modified file as a copy-safe two-line command:

```bash
cd '/absolute/parent'
code 'filename'
```

## Final audit

- Is the exact model class stated?
- Are dimensions of $x$, $u$, $B(\cdot)$, and each parameter matrix consistent?
- Is invertibility asserted only on the proper domain or feasible set?
- Is the control law substituted explicitly into the plant?
- For a sub-FAS, is the controller's well-definedness checked along the whole trajectory?
- Are stability and attraction-region claims separated?
- Are source claims locatable by paper and equation/theorem, with uncertain locators marked `[U]`?
- Is every research extension labeled `[D]` and compared with the nearest original result?
- Does every assumption have an explicit use-site in the proof?
- Is the chosen example structurally similar rather than merely sharing an application name?
- Did the answer distinguish definition, exact characterization, inner estimate, and numerical approximation?

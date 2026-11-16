# Duan-style technical writing guide

For verbatim Duan sentences, section openings, formal environment skeletons, and proof architectures, always consult [duan-writing-corpus.md](duan-writing-corpus.md) alongside this guide.

## Reusable organization

Duan's foundational papers typically proceed as follows:

1. motivate why first-order state-space augmentation obscures direct solution of the control vector or induces differential explosion;
2. place article-wide matrix and derivative-stack conventions in an unnumbered italic `Notations:` paragraph at the end of the Introduction (`=`, explicit stacks, no `:=` or `\col`);
3. define the FAS / HOFAS / sub-FAS model directly (declaring dimensions and piecewise continuity / smoothness in the `where` clause without redundant `"As in Duan..."` tags) and introduce singular/feasible sets and singularity functions;
4. construct the controller on the feasible set **before** presenting the closed-loop equation (`"When \mathcal{F} is not empty, B^{-1} exists on \mathcal{F}. Hence, we construct the following controller:"`), then substitute to obtain the constant linear closed-loop system;
5. state formal results (`Lemma`, `Proposition`, `Theorem`, `Corollary`) with **each result's purpose explicitly stated inside its own statement**, exposing parametric design freedom $(F, Z)$ or exact ROEA characterizations;
6. prove results using Duan's canonical proof templates (direct substitution + `"state-space form"`, trajectory-feasibility ROEA proof, `Duan & Zhou 2022` Lemma 4.4 contradiction template, or `Part III` / `Volume I` high-order backstepping);
7. illustrate on theoretical and/or physical examples with three-line tables, short noun-phrase figure captions, `"… are shown in Fig. X. It can be observed that …"`, and `matlab/p1ot.m` plotting conventions.

## Terminology and language discipline

- Follow [concepts-and-notation.md](concepts-and-notation.md) and [duan-writing-corpus.md](duan-writing-corpus.md).
- **Use Duan's concepts and expressions first**: write $|\varphi_i|$ instead of coining `"feasibility score"`; write `"the ROEA of the ith subsystem"` instead of `"fixed-mode ROEA"`; in deterministic switched systems use `the ith subsystem` consistently and write `If \sigma(t)=i` rather than `i=\sigma(t)`.
- **Preserve Duan's authentic academic phrasing**: retain natural Duan expressions such as `"the feasible set clearly has the following expression:"`, `"we construct the following controller:"`, `"is equivalent to the following state-space form:"` (never `"first-order form"`), `"In view of (...), we have"` (never `"In the view of"`), `"It follows from (...) that"`, `"The above theorem/result reveals/converts..."`, and `"gives the following corollary"`.
- **Eliminate AI-flavored prose**: remove defensive negative disclaimers (`"not X, but Y"`, `"Their values need not equal..."`), single-claim proof previews (`"We first show that..."`), and vague claims (`"all checks passed"`). Still write out nontrivial algebraic, squeeze-theorem, or continuation steps explicitly.
- In Chinese discussions, prefer “$\Phi(A_{0\sim n-1})$ 稳定（Hurwitz）”，称 $e^{\Phi t}X_0$ 为“闭环系统的状态响应”，称显式控制公式为“控制律”（不自造“反演控制器”“环路泛函”等词；无确定译名时保留英文并标 `[U]`）。

## Formal-result and equation-citation discipline

- **Explicit goal in statement**: Every `Theorem`, `Lemma`, `Proposition`, and `Corollary` must state what it establishes for the paper directly inside its own statement—never bury the real takeaway in surrounding prose or a `Remark`. Read [theorem-writing-template.md](theorem-writing-template.md) and [duan-writing-corpus.md](duan-writing-corpus.md).
- **Equation citations**: In manuscript prose, distinguish `equation (25)` from `inequality (34)` rather than using vague nouns like `"the estimate (34)"`. In discussions with the user, always quote `"content + current number"` verified from `newlabel{eq:...}` in the freshly compiled `.aux`.

## Invalid patterns

- Coining new English or Chinese terms where Duan already has established terminology.
- Reading unstated assumptions (e.g., closed singular set, Borel measurability, local boundedness of $B^{-1}$, or `"entries have poles"` for $\det B=\infty$) into Duan's original definitions.
- Claiming global stability from a Hurwitz linear closed loop for a sub-FAS without proving full-time trajectory feasibility.
- Calling a numerical check or sampled grid plot an `"exact ROEA"` or `"proof"`.
- Attributing `[D]` extensions or `[U]` items to Duan, or quoting Duan without a verified locator.

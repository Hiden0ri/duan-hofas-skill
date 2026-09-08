# Common assumptions in Duan-first-author FAS/HOFAS papers

## Scope and use

This is a source-indexed synthesis of the Duan-first-author PDFs in the user's Zotero library. It is not a list of assumptions that may be copied into every paper. Select the model family first, then reopen the cited source and copy its exact variables, domain, and quantifiers.

- `[E]`: the displayed mathematical role is verified in the cited primary PDF;
- `[D]`: the grouping or interpretation is synthesized across papers;
- “Condition” is preserved when the source calls an item a Condition rather than an Assumption.

## 1. Global affine full actuation `[E]`

### Recurring mathematical role

For a square affine input matrix, the recurring requirement is global nonsingularity on the declared domain:

$$
\det B(X,\zeta,t)\ne 0,
$$

or, in branches that explicitly admit abnormal singularity notation,

$$
\det B(X,\zeta,t)\ne 0\ \text{or}\ \infty.
$$

### Why it is imposed

It makes the input transformation or explicit control law involving $B^{-1}$ well defined. It is used at the control-substitution step, not as a standalone stability condition.

### Representative locations

- Part III, Assumption A1, model (1): $\det L(x^{(0\sim n-1)})\ne0$.
- Part VI, Assumption A1: $\det B(x^{(0\sim n-1)},\zeta,t)\ne0$.
- Part VIII, Assumption A1: multi-order global full actuation.
- Part IX, Assumption A1: multi-order global full actuation.
- Continuous-time delay Part 1, Assumptions A1, A3, and A5: single-order, multi-order, and mixed-delay variants.

### Do not overgeneralize

Part I, Assumption 3.1 uses $\operatorname{rank}B=r<n$ for an underactuated starting model. That assumption supports decomposition; it is not the square-HOFAS inversion condition.

## 2. Full actuation of each strict-feedback interconnection `[E]`

### Recurring mathematical role

For each cascade level,

$$
\det G_k(\cdot)\ne0,
\qquad k=1,\ldots,n.
$$

Scalar branches write $g_k(\cdot)\ne0$.

### Why it is imposed

It permits recursive variable elimination/order elevation or recursive control recovery. Every occurrence has its own derivative arguments and quantifiers.

### Representative locations

- Part II, Assumption A3, following system (18).
- Part III, Assumptions A2 and A3, for second- and mixed-order uncertain strict-feedback systems.
- Part IV, Assumption A2, scalar adaptive/backstepping branch.
- Part I, Assumption 3.3, pseudo strict-feedback decomposition.

## 3. Nonaffine input map is a differential homeomorphism `[E]`

### Recurring mathematical role

For fixed state/history variables and time, the mapping

$$
u\longmapsto \widetilde u=g(X,t,u)
$$

is assumed to be a differential homeomorphism on the declared domain.

### Why it is imposed

It replaces matrix inversion in a nonaffine FAS and justifies an equivalent standard-FAS input transformation.

### Representative locations

- Continuous-time delay Part 1, Assumption A2 and transformation (33)–(34).
- The same paper, Assumptions A4 and A6, for its multi-order/delay variants.
- Part I, nonaffine HOFAS definition and corresponding input-map condition.

## 4. Stable target matrices or a prescribed spectral margin `[E]`

### Recurring mathematical role

The selected parameter matrices must make the companion matrix stable, often with an explicit margin:

$$
\operatorname{Re}\lambda_j\!\left(\Phi(A_{0\sim n-1})\right)
< -\frac{\mu}{2}.
$$

### Why it is imposed

It supplies the Lyapunov inequality and the desired decay property after the HOFAS control law has produced the constant linear closed loop.

### Representative locations

- Part III, Lemmas 3.1–3.2 and Theorem 3.4.
- Part V, Lemmas 2.2–2.3 and inequality (9).
- OD-FAS Part 1, Lemma 5.1, where $a_{0\sim3}$ makes $\Phi(a_{0\sim3})$ Hurwitz.

This is sometimes stated inside a theorem rather than numbered as an Assumption.

## 5. Known bound on nonlinear uncertainty `[E]`

### Recurring mathematical role

An uncertain nonlinear term is bounded by a known nonnegative function, for example

$$
\lVert\Delta f(X)\rVert\le \rho(X).
$$

### Why it is imposed

The function $\rho$ determines the robust compensation term and bounds the cross term in the Lyapunov derivative.

### Representative locations

- Part III, Condition 1, immediately before Section 3.1.
- Part V, uncertainty and parameter-bound assumptions in Section 2.
- Robust/adaptive branches of the 2026 monograph.

Do not reuse $\rho$ as a distance-to-singularity symbol without explicitly redefining it; in these sources it is an uncertainty-bound function.

## 6. Parameter and parameter-rate bounds `[E]`

### Recurring mathematical role

The unknown parameter and a pre-estimate are related through bounded errors, typically represented by constants such as $\delta_0$ and $\delta_1$.

### Why it is imposed

It yields inequalities for parameter-error cross terms and supports boundedness or practical-convergence conclusions in robust adaptive control.

### Representative locations

- Part V, Assumption A3 and Lemma 2.1.
- Part IV–V adaptive/robust-adaptive theorem hypotheses.

This assumption is branch-local and must not be added to a nominal HOFAS theorem.

## 7. Stabilizability, detectability, and regulator-equation solvability `[E]`

### Recurring mathematical role

Linear design stages impose standard structural conditions such as

$$
(A,B)\ \text{stabilizable},
\qquad
(\widetilde A,\widetilde C)\ \text{detectable},
$$

or require matrices solving regulator equations.

### Why it is imposed

These conditions are used only after the nonlinear HOFAS has been converted into a constant linear design problem. They justify feedback, observer, output-regulation, or tracking constructions.

### Representative locations

- Part VI, Conditions C1–C2 preceding Lemma 4.1.
- Part IX, Assumption A2, regulator equations (35).
- Part VII, controllability/stabilizability sections for complete parameterized design.

## 8. Existence and uniqueness of predictor dynamics `[E]`

### Recurring mathematical role

The predictor or shifted auxiliary system is assumed to have a unique solution for arbitrary admissible initial histories and external inputs.

### Why it is imposed

It makes the future-state identity used by predictor feedback mathematically meaningful.

### Representative locations

- Continuous-time delay Part 2, Assumption A3 before Lemma 1.
- The same paper, Assumption A4 before Lemma 2.

This is a delay-branch assumption; it is not automatically required in a delay-free HOFAS statement.

## 9. Solvability of elimination equations and coordinate transformations `[E]`

### Recurring mathematical role

An algebraic/differential relation is required to admit a solution on a declared simply connected set, followed by a stated homeomorphism or diffeomorphism.

### Why it is imposed

It establishes that the original plant can be represented by the proposed HOFAS/sub-FAS and that eliminated variables can be recovered.

### Representative locations

- *Stabilisation of Four Types of Underactuated Systems*, Assumption A2 and equations (66)–(67).
- The same paper, Assumption A4 and equations (138)–(139).
- Generalized chained-form Parts 1–2, Assumptions A/B/C for branch-specific transformations and feasibility neighborhoods.

## 10. Restricted dependence of a singular input matrix `[E]`

### Recurring mathematical role

For a decoupled multi-order sub-FAS design, the singularity-bearing input matrix is assumed to depend only on the state group treated by the constrained closed-loop subsystem.

### Why it is imposed

It permits the ROEA/feasibility condition to be expressed through that group while the remaining groups are unconstrained linear subsystems.

### Representative location

- *Substability and Substabilization*, Assumption 2 following the state-grouping construction around equation (46).

## Selection checklist `[D]`

Before copying an assumption, answer:

1. Is the model affine or nonaffine?
2. Is it global FAS or sub-FAS?
3. Is the assumption used for model equivalence, controller well-definedness, stability, robustness, prediction, or output feedback?
4. Does the source require the condition globally, locally, pointwise, or uniformly?
5. Is it called an Assumption or a Condition in the source?
6. Where is it used in the proof?


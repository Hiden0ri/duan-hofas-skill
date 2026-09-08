# Common lemmas in Duan-first-author FAS/HOFAS papers

## Scope and use

This file organizes recurring lemma families found in the user's Zotero collection of Duan-first-author papers. “Common” means repeatedly reused mathematics or a recurring role in several FAS branches; it does not mean that the same numbering or wording appears everywhere. Reopen the cited PDF before quoting a lemma verbatim.

## 1. Spectral margin implies a Lyapunov inequality `[E]`

If

$$
\operatorname{Re}\lambda_i(A)\le-\frac{\gamma}{2},
$$

then there exists $P=P^\top>0$ such that

$$
A^\top P+PA\le-\gamma P.
$$

### Role

Converts a desired eigenvalue margin into the matrix inequality used in the Lyapunov derivative.

### Sources

- Part III, Lemma 3.1, equations (7)–(8).
- Part V, Lemma 2.2, equations (5)–(6), with parameter $\mu$.

## 2. HOFAS coefficient matrices can assign a stable companion spectrum `[E]`

For any prescribed decay margin $\mu>0$, matrices $A_i$ can be selected so that

$$
\operatorname{Re}\lambda_j\!\left(\Phi(A_{0\sim n-1})\right)
< -\frac{\mu}{2}.
$$

### Role

Connects the HOFAS parameter matrices with an arbitrarily selected stable constant linear closed loop.

### Sources

- Part III, Lemma 3.2, equation (9).
- Part V, Lemma 2.3, equation (7).
- Related complete parameterization is developed in Part VII rather than being reduced to this existence statement.

## 3. Completing-the-square scalar inequality `[E]`

For $a\in\mathbb R$ and $b>0$,

$$
a-\frac{a^2}{4b}\le b.
$$

Equivalently,

$$
-\frac{(a-2b)^2}{4b}\le0.
$$

### Role

Bounds a scalar cross/robust-compensation term in Lyapunov analysis.

### Sources

- Part III, Lemma 3.3, equation (13).
- Part V, Lemma 2.4, equation (8).

Copy the exact variables used by the selected theorem; the abstract $a,b$ form is only the reusable mathematical core.

## 4. Parameter-error decomposition inequalities `[E]`

With the paper's parameter errors

$$
\widetilde\theta=\theta-\widehat\theta,
\qquad
\widetilde\theta_{e0}=\widehat\theta-\theta_0,
\qquad
\widetilde\theta_{r0}=\theta-\theta_0,
$$

the source derives the decomposition and quadratic bounds needed in the adaptive Lyapunov proof.

### Role

Separates estimation error from pre-estimation error and bounds terms involving the unknown parameter and its derivative.

### Source

- Part V, Lemma 2.1, following definition (4).

This is robust-adaptive branch notation, not a universal HOFAS lemma.

## 5. Generalized Sylvester equation parameterization `[E]`

For the generalized Sylvester equation

$$
\Phi(0_{0\sim n-1})V+B_cW=VF,
$$

the solution is parameterized by a free matrix $Z$ through

$$
V(Z,F)=
\begin{bmatrix}
Z^\top&(ZF)^\top&\cdots&(ZF^{n-1})^\top
\end{bmatrix}^\top,
\qquad
W(Z,F)=ZF^n.
$$

### Role

Provides the algebraic engine for complete parameterization, eigenstructure assignment, disturbance decoupling, and tracking designs.

### Sources

- Part VI, Lemma 3.1, equations (25)–(26).
- Part VI, Lemma 4.2, equations (54)–(55), for a nonhomogeneous form.
- Part VII, Lemma 5.2, right-coprime-factor/generalized-Sylvester formulation.
- These papers trace the underlying result to Duan's earlier parametric-design work.

## 6. $H_2$ norm represented by Lyapunov equations `[E]`

For Hurwitz $A$, the $H_2$ norm of

$$
C(sI-A)^{-1}B
$$

is expressed through the controllability or observability Gramian satisfying the corresponding Lyapunov equations.

### Role

Turns disturbance-attenuation performance into a computable matrix expression after HOFAS closed-loop linearization.

### Source

- Part VI, Lemma 3.2, Section 3.2.

The source explicitly points to Duan and Yu's LMI text for the underlying linear-system result.

## 7. Explicit solution of a Lyapunov equation `[E]`

For Hurwitz $\Phi$ and $Q=Q^\top>0$, the equation

$$
\Phi^\top P+P\Phi=-Q
$$

has a unique solution, for which Part VI gives a polynomial expression in $\Phi$.

### Role

Makes the Lyapunov matrix explicit in the HOFAS coefficient matrices rather than leaving it as an implicit equation.

### Source

- Part VI, Lemma 3.3, equations (27)–(28).

## 8. Predictor reproduces the future state `[E]`

Under the full-actuation and unique-solution assumptions, the shifted predictor satisfies

$$
Z(s)=x^{(0\sim n-1)}(t+s),
\qquad s\in[0,h],
$$

and therefore $Z(h)$ gives the state required to compensate the input delay.

### Role

Justifies using the computed predictor value in a causal delay-compensating controller.

### Sources

- Continuous-time delay Part 2, Lemma 1, equations (46)–(50).
- The same paper, Lemma 2, for the multi-order counterpart.

## 9. A coordinate transformation transfers convergence `[E]`

A stated diffeomorphism and its inverse are used to show that exponential convergence of the transformed HOFAS variables implies convergence of the original physical variables.

### Role

Closes the reverse direction of model equivalence; stability of transformed coordinates alone is not silently identified with stability of the original plant.

### Representative source

- OD-FAS Part 1, Lemma 3.3, following transformations (68)–(69).

## 10. Feasibility condition converted into an initial-value region `[E]`

For a selected stable second-order closed loop, an all-time sign/nonzero constraint is converted into algebraic inequalities on the initial values.

### Role

Produces an explicit external feasibility region or ROEA component from the closed-loop response.

### Representative source

- Constrained unidirectionally connected FASs Part II, Lemma 4.1, equations (122) onward.
- The SUB-FAS and ROEA papers use the same broader logic, although not always under a numbered Lemma.

## 11. Time-varying Lyapunov/observability stability criterion `[E]`

For $\dot z=A(t)z$, OD-FAS Part 1 gives a sufficient condition involving a positive matrix $P(t)$, a differential Lyapunov equation, and pointwise uniform observability of $(A(t),C(t))$.

### Role

Supports output-feedback stability for a time-varying linear system obtained from an OD-FAS construction.

### Source

- OD-FAS Part 1, Appendix A, Lemma 8.1, equations (140) and following.

## Selection rule `[D]`

For a new paper, use only the lemma families needed by the proof:

- nominal global HOFAS: Sections 1–2;
- robust/adaptive HOFAS: Sections 1–4;
- parameterized linear design: Sections 5–7;
- delay compensation: Section 8;
- transformed/OD-FAS models: Sections 9 and 11;
- SUB-FAS or constrained feasibility: Section 10.

Do not cite this synthesis as the mathematical source; cite the original paper or the underlying standard reference named there.


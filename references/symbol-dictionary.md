# Duan first-author symbol dictionary

## How to use this dictionary

This dictionary is distilled only from the selected Duan-first-author corpus. Symbols are divided into:

- **core**: repeatedly used across the Part I–X series, overview, SUB-FAS, and later first-author branches;
- **branch-local**: meaningful only in a named paper family;
- **paper-local**: must be recopied from the exact theorem/example and must not be treated as a general convention.

When two papers use the same letter differently, follow the paper currently being discussed. Never merge meanings merely because the glyph is identical.

## 1. Sets, spaces, indices, and elementary matrices — core `[E]`

| Symbol | Meaning |
|---|---|
| $\mathbb R$ | real numbers |
| $\mathbb R^n$ | $n$-dimensional real vector space |
| $\mathbb R^{m\times n}$ | real $m\times n$ matrix space |
| $\mathbb N$ | natural numbers, when declared by the paper |
| $\varnothing$ | null/empty set |
| $\Omega\setminus\Theta$ | complement of $\Theta$ in $\Omega$ |
| $I_n$ | identity matrix of order $n$ |
| $0_{m\times n}$ | $m\times n$ zero matrix |
| $i\sim j$ | integer sequence $i,i+1,\ldots,j$ |

Do not replace $i\sim j$ with an interval of real numbers. In Duan's notation it is an integer-index shorthand.

## 2. Matrix operations — core or recurring `[E]`

| Symbol | Meaning | Scope note |
|---|---|---|
| $A^\top$ | transpose | recurring |
| $\det A$ | determinant | core |
| $A^{-1}$ | inverse, when it exists | core |
| $\operatorname{adj}(A)$ | adjoint/adjugate used in the source | SUB-FAS, delay, robust branches |
| $\operatorname{eig}(A)$ | set of eigenvalues | output-dependent branch |
| $\lambda_i(A)$ | $i$th eigenvalue | robust/adaptive branches |
| $\operatorname{Re}(s)$ | real part of $s\in\mathbb C$ | robust/adaptive branches |
| $\lambda_{\max}(P)$, $\lambda_{\min}(P)$ | largest/smallest eigenvalue of a symmetric matrix | optimal-control branch |
| $\operatorname{blockdiag}(A_i,i=1,\ldots,n)$ | block diagonal matrix with diagonal blocks $A_i$ | multi-order branches |
| $\nu(P)=\lVert P\rVert\lVert P^{-1}\rVert$ | condition number used in Part VIII/IX | not the universal notation of every paper |

If the paper says “adjoint matrix,” check whether its formula requires the classical adjugate rather than the conjugate transpose. Preserve the source formula.

## 3. Norms — recurring `[E]`

For a symmetric positive definite $P$,

$$
\lVert x\rVert_P=(x^\top Px)^{1/2}.
$$

The Euclidean norm is

$$
\lVert x\rVert=\lVert x\rVert_I=(x^\top x)^{1/2}.
$$

Some output-dependent papers explicitly use $\lVert A\rVert$ for the spectral norm. Never assume an unspecified matrix norm in a proof that needs a numerical bound; state the norm used by the source.

## 4. Consecutive variables and derivatives — core `[E]`

### 4.1 Consecutive variables

For $i\le j$,

$$
x_{i\sim j}
=
\begin{bmatrix}
x_i^\top&x_{i+1}^\top&\cdots&x_j^\top
\end{bmatrix}^\top.
$$

### 4.2 Derivative stack of one variable

For $n_1\le n_2$,

$$
x^{(n_1\sim n_2)}
=
\begin{bmatrix}
(x^{(n_1)})^\top&(x^{(n_1+1)})^\top&\cdots&(x^{(n_2)})^\top
\end{bmatrix}^\top.
$$

In particular,

$$
x^{(0\sim n)}
=
\begin{bmatrix}
x^\top&\dot x^\top&\cdots&(x^{(n)})^\top
\end{bmatrix}^\top.
$$

### 4.3 Same derivative range for consecutive variables

$$
x_{i\sim j}^{(n_1\sim n_2)}
=
\left.
x_k^{(n_1\sim n_2)}
\right\rvert_{k=i\sim j}.
$$

The vertical bar means “stack the indexed objects for $k=i,\ldots,j$”; it is not a conditioning bar or restriction of a function.

### 4.4 One derivative order assigned to each variable

$$
\left.x_k^{(n_k)}\right\rvert_{k=i\sim j}
=
\begin{bmatrix}
(x_i^{(n_i)})^\top&\cdots&(x_j^{(n_j)})^\top
\end{bmatrix}^\top.
$$

### 4.5 Common lower order and variable upper orders

$$
\left.x_k^{(n_0\sim n_k)}\right\rvert_{k=i\sim j}
=
\begin{bmatrix}
(x_i^{(n_0\sim n_i)})^\top&\cdots&(x_j^{(n_0\sim n_j)})^\top
\end{bmatrix}^\top.
$$

These heterogeneous-order stacks are fundamental in multi-order FASs. Do not flatten them into $X$ unless $X$ is explicitly defined.

## 5. Parameter-matrix and companion-matrix notation — core `[E]`

$$
A_{0\sim n-1}
=
\begin{bmatrix}
A_0&A_1&\cdots&A_{n-1}
\end{bmatrix}.
$$

The continuous-time state-space matrix is

$$
\Phi(A_{0\sim n-1})
=
\begin{bmatrix}
0&I&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&I\\
-A_0&-A_1&\cdots&-A_{n-1}
\end{bmatrix}.
$$

For a multi-order block $x_k\in\mathbb R^{r_k}$ of order $\mu_k$, use

$$
A_{k,0\sim\mu_k-1}
=
\begin{bmatrix}
A_{k,0}&A_{k,1}&\cdots&A_{k,\mu_k-1}
\end{bmatrix},
$$

and

$$
\Phi\!\left(A_{k,0\sim\mu_k-1}\right)
$$

for its block companion matrix.

The index $k$ identifies the subsystem; the second index identifies derivative order. Do not rewrite $A_{k,j}$ as a single gain $K$ if comparing with Duan's theorem.

## 6. Standard input-injection matrices — recurring `[E]`

For the state-space realization of an $n$th-order block,

$$
B_c
=
\begin{bmatrix}
0&\cdots&0&I_r
\end{bmatrix}^\top,
$$

and the zero-dynamics shift matrix is written as

$$
\Phi(0_{0\sim n-1}).
$$

For a multi-order system,

$$
B_{cE}=\operatorname{blockdiag}(B_{ci},i=1,\ldots,\eta),
$$

$$
\Phi_E
=
\operatorname{blockdiag}
\left(
\Phi_i(0_{0\sim\mu_i-1}),
i=1,\ldots,\eta
\right).
$$

These forms recur in prediction, optimal control, tracking, and delay papers. Check the paper's exact subscript capitalization.

## 7. Complete parameterization symbols — core design branch `[E]`

For an $m$th-order block, Duan's complete parametric solution uses a selected matrix $F$ and a free parameter matrix $Z$:

$$
V(Z,F)
=
\begin{bmatrix}
Z\\ZF\\\vdots\\ZF^{m-1}
\end{bmatrix},
\qquad
\det V(Z,F)\ne0,
$$

$$
A_{0\sim m-1}
=
-ZF^mV^{-1}(Z,F),
$$

so that

$$
\Phi(A_{0\sim m-1})
=
VFV^{-1}.
$$

| Symbol | Meaning |
|---|---|
| $F$ | selected target matrix carrying the desired closed-loop eigenstructure |
| $Z$ | free parameter matrix |
| $V(Z,F)$ | stacked matrix formed from $Z,ZF,\ldots,ZF^{m-1}$ |
| $\det V(Z,F)\ne0$ | admissibility condition for the parameter choice |

The letter $F$ here is a matrix and is not the feasible set $\mathcal F$. Preserve calligraphic $\mathcal F$ for feasibility to avoid collision.

## 8. Single- and multi-order FAS variables — core `[E]`

| Symbol | Meaning |
|---|---|
| $n$ | order of a single-order FAS |
| $x\in\mathbb R^r$ | state/basic variable of the FAS equation |
| $u\in\mathbb R^r$ | control vector in a square affine FAS |
| $f(\cdot)$ | known nonlinear vector function unless another uncertainty split is declared |
| $B(\cdot)\in\mathbb R^{r\times r}$ | input coefficient matrix |
| $\zeta$ | external vector; may collect parameters, delayed states, or unmodeled dynamics only as declared |
| $\eta$ | number of blocks in a multi-order FAS |
| $x_k\in\mathbb R^{r_k}$ | $k$th state block |
| $\mu_k$ | differential order of $x_k$ |
| $r=\sum_{k=1}^{\eta}r_k$ | total input/output block dimension |
| $\kappa=\sum_{k=1}^{\eta}r_k\mu_k$ | dimension of the stacked multi-order state used in the overview |

The letter $r$ usually describes control-vector dimension in the square FAS model. The original state-space plant may have dimension $n$ with input dimension $r$; do not confuse plant dimension with FAS differential order.

## 9. Transformed strict-feedback symbols — core transformation branch `[E]`

| Symbol | Meaning |
|---|---|
| $x_{1\sim n}$ | consecutive state blocks of the original strict-feedback system |
| $f_i(\cdot)$ | $i$th original drift term |
| $G_i(\cdot)$ | $i$th interconnection/input matrix |
| $\breve h_i(\cdot)$ | recursively produced transformed nonlinear term |
| $\breve B_i(\cdot)$ | recursively produced transformed input coefficient |
| $\breve h_e$, $\breve B_e$ | stacked transformation quantities in the Chinese paper |
| $\widehat{\mathcal S}$, $\widehat{\mathcal F}$ | singular/feasible sets defined for the original strict-feedback coordinates |

The hats distinguish sets in the original strict-feedback description; the breve marks transformed functions. Duan proves equality of the corresponding singular and feasible sets under the stated transformation. Do not erase hats/breves before that equivalence is established.

## 10. Full actuation, singularity, and feasibility — SUB-FAS core `[E]`

| Symbol | Meaning |
|---|---|
| $\mathcal S$ | singular set |
| $\mathcal F$ | feasible set |
| $\mathcal S_0$ | normal singular set, based on $\det B=0$ |
| $\mathcal S_\infty$ | abnormal singular set, based on $\det B=\infty$ |
| $\varphi_0(X,t)$ | function of normal singularity |
| $\varphi_\infty(X,t)$ | function of abnormal singularity |
| $\varphi(X,t)$ | combined function of singularity when defined by the source |
| $R_s$ or source-specific $R$ | region of exponential attraction; copy exact notation from the selected paper |
| $X_0$ | initial value of the stacked state-space realization |

Do not normalize every paper's ROEA symbol to one glyph. The 2023 SUB-FAS paper and later ROEA work may use different superscripts/subscripts for single- and multi-order cases.

## 11. Uncertain-system notation — branch-local `[E]`

| Symbol | Typical meaning |
|---|---|
| $\Delta f(\cdot)$ | uncertain nonlinear term |
| $\theta(t)$ | unknown time-varying parameter vector |
| $\theta_0(t)$ | pre-estimate of $\theta(t)$ |
| $\rho(\cdot)$ | known/nonnegative bounding function in the paper's assumption |
| $\delta_0,\delta_1$ | parameter and derivative error bounds in Part V |
| $d(t)$ | external disturbance |
| $E$ or another declared matrix | disturbance-distribution matrix |

$\rho$ is not universally a distance-to-singularity measure. In robust/adaptive papers it is often an uncertainty-bound function. The user's switching project uses $\rho_i$ differently; that usage must be marked `[D]` or renamed to prevent collision.

## 12. Delay-system notation — branch-local `[E]`

| Symbol | Meaning |
|---|---|
| $\tau_j(t)$ | state delay in the declared channel |
| $\sigma_j(t)$ | another delay family, commonly associated with $B(\cdot)$ arguments |
| $h$ | input delay in the input-delay paper |
| $x(t-\tau_j(t))\vert_{j=1\sim\zeta}$ | stack of delayed copies |
| $x^{\lceil\tau_{1\sim\zeta}(t)\rceil}$ | source shorthand for the delayed stack |
| $Y$ | predicted state in the input-delay construction |
| $Z(s)=Y(s+t)$ | shifted predictor variable |

Copy delay ranges and history intervals exactly. A solution requires an initial history, not only $x(0)$.

## 13. Discrete-time notation — branch-local `[E]`

The backward and forward shift operators satisfy

$$
q^{-i}x(k)=x(k-i),
\qquad
q^ix(k)=x(k+i).
$$

Duan then introduces bracketed shorthand for step-backward and step-forward values. PDF text extraction may corrupt the bracket glyphs, so copy these symbols from the rendered Part X PDF, not from OCR text.

The discrete-time companion matrix differs from the continuous-time one: its coefficient blocks occur in the top row and the identity blocks shift downward. Never reuse the continuous-time $\Phi$ matrix by appearance.

## 14. Constraint and unidirectionally connected notation — branch-local `[E]`

| Symbol | Meaning |
|---|---|
| $C_s$ | declared state/control constraint set in the constrained FAS model |
| $n_c$ | highest control-derivative order appearing in a constraint |
| $\mathcal F_I$, $\mathcal F_E$ or paper-specific forms | internal/external feasibility sets; copy exact glyphs from Part II |
| $(x,y)^{(i)}$ | pair $(x^{(i)},y^{(i)})$ |
| $(x,y)^{(i_1\sim i_2)}$ | paired derivative stack |

Internal/external feasibility is a feature of the constrained unidirectionally connected branch, not the definition of ordinary SUB-FAS feasibility.

## 15. Output-dependent FAS notation — branch-local `[E]`

| Symbol | Typical meaning |
|---|---|
| $y$ | measured/system output |
| $h(\cdot,t)$ | output map |
| $f_x$, $f_y$ | state-side and output-side nonlinear terms when the paper introduces the split |
| $F_{i,0\sim n-1}$ | output-dependent parameter-matrix functions in Part 1 |
| $\Xi_s(t,0)$ | state-transition matrix in a stated linear time-varying construction |
| $\Pi_s(t)$ | paper-defined output/state mapping |

Output-dependent papers deliberately change the available-information pattern. Do not use full-state feedback symbols when the theorem assumes only position or velocity output.

## 16. End markers and exposition conventions `[E]`

The constrained unidirectionally connected series explicitly declares separate symbols for the end of a proof and the end of an example. OCR may render these as indistinguishable boxes. Preserve the journal PDF glyphs when typesetting, or use the target journal's standard proof environment rather than guessing.

## 17. Collision audit before writing

Before using a symbol, check:

1. Does it already have a core meaning?
2. Does the selected branch redefine it?
3. Is the user's project using the same symbol differently?
4. Are its dimension and dependence on $(x,t,\zeta)$ explicit?
5. Is it a matrix stack, derivative stack, or indexed family?

If any answer is uncertain, retain the source symbol with a locator and mark `[U]`; do not “clean up” the notation from memory.

## 18. HOFAS standard-representation discipline `[E/D]`

The user's Zotero note “HOFAS标准表示” collects instances from Wang et al. 2025, Li et al. 2025, and Zhang and Duan 2025. Together with the Duan-first-author corpus, they support the following two-level rule.

### 18.1 Stable structural skeleton `[E]`

Across the checked HOFAS papers, introduce symbols in this order:

1. state, input, order, dimensions, and external variables;
2. derivative or multi-order state stack;
3. coefficient/parameter row;
4. companion-type matrix $\Phi$;
5. HOFAS model and full-actuation condition;
6. control law and auxiliary input;
7. resulting constant linear closed-loop equation.

For the affine single-order case, the recurring algebraic skeleton is

$$
x^{(n)}=f\!\left(x^{(0\sim n-1)},\zeta\right)
+B\!\left(x^{(0\sim n-1)},\zeta\right)u,
$$

followed by a control law that yields

$$
x^{(n)}+A_{0\sim n-1}x^{(0\sim n-1)}=v.
$$

The model class and selected paper determine the exact letters, dimensions, signs, and placement of $f$; never reconstruct them from this skeleton alone.

### 18.2 Paper-local layer `[E]`

The following are verified variants, not interchangeable conventions:

- state dimension/order: $(r,n)$, $(m,n)$, or $(n,m)$ depending on the paper;
- input matrix: $B$, $L$, $G_i$, and branch-specific perturbed forms;
- parameter row: $A_{0\sim n-1}$, $A^{0\sim n-1}$, or $A_{*,0\sim n-1}$;
- companion matrix: $\Phi(A_{0\sim n-1})$ and paper-local subscripted variants;
- multi-order indices: $m_i$ or $\mu_k$;
- auxiliary-control split: $u=-B^{-1}(Ax+u^*)$ or $u=-B^{-1}(f+u^*)$, with signs fixed by direct substitution.

Use [coauthored-comparison.md](coauthored-comparison.md) when the task specifically concerns the three papers collected in note 307. Use the Duan-first-author source selected from [source-catalog.md](source-catalog.md) to determine the canonical notation for a new Duan-style derivation.

### 18.3 Complete expression inventory from Zotero note 307 `[E/U]`

The following inventory prevents visually highlighted notation from being lost during text-only extraction.

#### Wang et al. 2025, p. 5003 `[E]`

The note records the conventional declaration

$$
I_m:\text{ the }m\text{-dimensional identity matrix},
$$

and, for a symmetric matrix $R$,

$$
\lambda_{\min}(R),\qquad \lambda_{\max}(R),
$$

as its minimum and maximum eigenvalues. It then defines

$$
x^{(0\sim n-1)}
=
\begin{bmatrix}
x^\top&\dot x^\top&\cdots&(x^{(n-1)})^\top
\end{bmatrix}^\top
\in\mathbb R^{nm},
$$

and the paper-local scalar parameter row

$$
A_{*,0\sim n-1}
=
\begin{bmatrix}
a_{*,0}&a_{*,1}&\cdots&a_{*,n-1}
\end{bmatrix}
\in\mathbb R^{1\times n}.
$$

Its companion matrix is written as

$$
\Phi_{*a}(A_{*,0\sim n-1})
=
\begin{bmatrix}
0&1&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&1\\
-a_{*,0}&-a_{*,1}&\cdots&-a_{*,n-1}
\end{bmatrix}.
$$

The precise referent represented by $*$ must be checked in the selected paper before reuse.

#### Li et al. 2025, p. 1086 `[E]`

The note records a horizontal block selector and a vertical parameter stack:

$$
\mathring I_{0\sim n-1}
=
\begin{bmatrix}
0_m&I_m&\cdots&0_m\\
\vdots&\vdots&\ddots&\vdots\\
0_m&0_m&\cdots&I_m\\
0_m&0_m&\cdots&0_m
\end{bmatrix},
$$

$$
\mathring A_{0\sim n-1}
=
\begin{bmatrix}
A_0^\top&A_1^\top&\cdots&A_{n-1}^\top
\end{bmatrix}^\top,
$$

together with

$$
\Phi(A_{0\sim n-1})
=
\begin{bmatrix}
0_m&I_m&\cdots&0_m\\
\vdots&\vdots&\ddots&\vdots\\
0_m&0_m&\cdots&I_m\\
-A_0&-A_1&\cdots&-A_{n-1}
\end{bmatrix}.
$$

The ring accent is part of the printed symbol. Do not silently replace $\mathring I$ or $\mathring A$ by an undotted symbol when quoting this paper.

#### Zhang and Duan 2025, p. 2 `[E]`

For the $i$th order group, the note records

$$
[A_i]_{0\sim m_i-1}
=
\begin{bmatrix}
A_{i,0}&A_{i,1}&\cdots&A_{i,m_i-1}
\end{bmatrix},
$$

and

$$
\Phi([A_i]_{0\sim m_i-1})
=
\begin{bmatrix}
0&I&\cdots&0\\
\vdots&\vdots&\ddots&\vdots\\
0&0&\cdots&I\\
-A_{i,0}&-A_{i,1}&\cdots&-A_{i,m_i-1}
\end{bmatrix}.
$$

Here the blocks have dimensions determined by $r_i$; $0$ and $I$ are not necessarily scalars.

#### Two pasted expressions with unresolved paper locators `[E: note image; U: original source]`

The note also contains

$$
A_i^{0\sim m_i}=[A_i]_{0\sim m_i},
\qquad i=1,2,\ldots,n,
$$

and the displayed definition

$$
I_n^\circ
=
\begin{bmatrix}
0&0&I\\
0&\iddots&0\\
I&0&0
\end{bmatrix}
\in\mathbb R^{n\times n}.
$$

The image shows a reverse-order identity/block-identity pattern. Its exact English name and originating paper have not been identified, so retain the source symbol $I_n^\circ$ and its displayed matrix rather than assigning a new technical name.

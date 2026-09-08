# Duan HOFAS notation and writing quick guide

## Purpose

Use this file by default to check an existing Markdown/manuscript or to create a Duan-style paper skeleton. It distills recurring notation and organization; it does not replace the source theorem. For an exact mathematical claim, search the monograph or open the relevant original paper.

Default review order:

1. identify the model family;
2. check symbols and dimensions;
3. check terminology;
4. check definitions and assumptions;
5. check the theorem's six-part structure;
6. check the substitution-first proof sequence;
7. check Remark, Example, simulation, and Markdown rendering.

## 1. Symbol quick reference

### 1.1 Core stacked notation

| Purpose | Preferred form | Meaning |
|---|---|---|
| derivatives from order $i$ to $j$ | $x^{(i\sim j)}$ | $[(x^{(i)})^\top\ (x^{(i+1)})^\top\ \cdots\ (x^{(j)})^\top]^\top$ |
| consecutive variables | $x_{i\sim j}$ | $[x_i^\top\ x_{i+1}^\top\ \cdots\ x_j^\top]^\top$ |
| indexed family stack | $\left.x_k^{(0\sim\mu_k-1)}\right\rvert_{k=1\sim\eta}$ | stacks heterogeneous-order state blocks |
| parameter row | $A_{0\sim n-1}$ | $[A_0\ A_1\ \cdots\ A_{n-1}]$ |
| companion matrix | $\Phi(A_{0\sim n-1})$ | first-order realization of a high-order linear equation |
| input injection | $B_c$ | normally $[0\ \cdots\ 0\ I_r]^\top$ |

Always define the stack before its first use. Do not alternate between an expanded stack and a newly invented state symbol without a reason.

### 1.2 Matrix notation

| Symbol | Use |
|---|---|
| $I_n$, $0_n$, $0_{m\times n}$ | identity, zero vector, zero matrix |
| $A^{-1}$, $A^\top$, $A^H$ | inverse, transpose, conjugate transpose |
| $\det A$, $\operatorname{rank}A$, $\operatorname{cond}A$ | determinant, rank, condition number |
| $\lambda_i(A)$, $\lambda_{\min}(A)$, $\lambda_{\max}(A)$ | eigenvalue notation; min/max require the source's matrix conditions |
| $\sigma_i(A)$, $\sigma_{\min}(A)$, $\sigma_{\max}(A)$ | singular values |
| $\lVert A\rVert_2$, $\lVert A\rVert_F$ | spectral and Frobenius norms |

The 2026 monograph's front-matter notation list is the first authority for these meanings. A branch paper may introduce decorated or indexed variants.

## 2. Choose symbols by model class

| Model class | Standard skeleton | Main design symbols | Do not mix with |
|---|---|---|---|
| single-order affine global FAS | $x^{(n)}=f(x^{(0\sim n-1)},t)+B(x^{(0\sim n-1)},t)u$ | $A_{0\sim n-1}$, $\Phi(A_{0\sim n-1})$, $B_c$ | multi-order $A_{k,0\sim\mu_k-1}$ |
| single-order nonaffine global FAS | $x^{(n)}=f(x^{(0\sim n-1)},t)+g(x^{(0\sim n-1)},u,t)$ | inverse input mapping $g^{-1}$ | affine $B^{-1}$ unless affine specialization is stated |
| multi-order FAS | $\left.x_k^{(\mu_k)}\right\rvert_{k=1\sim\eta}=f(\cdot)+B(\cdot)u$ | $r_k$, $\mu_k$, $\eta$, $\kappa_0$ | single-order dimension $nr$ |
| decoupled multi-order design | one parameter row $A_{k,0\sim\mu_k-1}$ for each $k$ | $\Phi(A_{k,0\sim\mu_k-1})$, $B_{ck}$ | coupled matrix $A_E$ |
| coupled multi-order design | one overall stacked closed loop | $A_E$ | a claim of $\eta$ independent closed loops |
| uncertain FAS | add $\Delta f$, $H^\top\theta$, disturbance, or perturbed input map exactly as the source does | $\rho$, $P$, $P_L$, adaptive/robust terms | symbols from another uncertainty model |
| SUB-FAS | same local model, but inversion only on the feasible set | singular set, feasible set, substability, RoEA | global-FAS conclusions without trajectory feasibility |
| strict-feedback conversion | retain the original cascade variables until the conversion is proved | transformation and recovered variables | declaring a HOFAS without the elimination chain |

Source notation wins over this table. The table selects a family; it does not authorize reconstructing a formula from memory.

## 3. Definition and assumption templates

### Definition

Recommended logical order:

```text
Define the system or mapping → give all dimensions and domains → state the decisive rank/invertibility/mapping property → name the system class.
```

LaTeX skeleton:

```latex
\begin{definition}
Consider system~\eqref{eq:model}, where ... . If ... holds for all ... ,
then system~\eqref{eq:model} is called a ... FAS.
\end{definition}
```

### Assumption

State one mathematical role per assumption when possible:

```latex
\begin{assumption}\label{ass:full-actuation}
The matrix $B(X,t)$ satisfies ... for all $X\in\mathcal D$ and $t\ge 0$.
\end{assumption}
```

Do not write “all functions are sufficiently smooth” unless the required derivative order is clear from the derivation.

## 4. Six-part theorem template

The user's Zotero note “Duan规范”, based on Duan's Part III, Theorem 3.5, identifies this recurring order:

$$
\boxed{
\text{system}
\to
\text{assumptions}
\to
\text{given parameters and conditions}
\to
\text{control law}
\to
\text{auxiliary definitions}
\to
\text{performance}
}
$$

Use:

```latex
\begin{theorem}\label{thm:main}
Suppose that system~\eqref{eq:model} satisfies Assumptions~...
Let ... be arbitrarily given, and let ... satisfy ... .
Then, the following control law
\begin{equation}
  u=\cdots
\end{equation}
where ... , guarantees that ... .
\end{theorem}
```

The conclusion must name the controlled quantity, convergence type, domain of initial conditions, and exact set or performance bound.

## 5. Proof organization

Duan's recurring proof order is:

$$
\text{control substitution}
\to
\text{closed-loop high-order equation}
\to
\text{state-space form if needed}
\to
\text{matrix/Lyapunov condition}
\to
\text{inequality or eigenstructure argument}
\to
\text{performance conclusion}.
$$

Useful paragraph openings:

```text
Substituting control law (...) into system (...) gives ...
In view of (...), we have ...
It follows from Assumption ... that ...
Combining the above relations gives ...
Therefore, ...
The proof is completed.
```

For a SUB-FAS, add a separate feasibility layer after deriving the closed loop: prove that the whole response remains in the feasible set.

## 6. Verified high-frequency language

Counts below come from the main text and appendices of the 2026 Volume I extraction and are corpus indicators, not mandatory phrases.

| Phrase | Count | Function |
|---|---:|---|
| `Substituting` | 70 | begin direct algebraic substitution |
| `Therefore` | 74 | state a derived consequence |
| `It follows from` | 65 | cite the basis of a step |
| `In view of` | 41 | combine a prior equation or assumption |
| `Let us consider` | 33 | introduce a model or case |
| `Suppose that` | 20 | introduce theorem hypotheses |
| `guarantees that` | 14 | introduce the performance conclusion |
| `Please note that` | 13 | emphasize interpretation or a special case |
| `For convenience` | 12 | explain a notation or scope simplification |
| `Remark` | 84 occurrences | interpretation, comparison, limitation, or special case |
| `Example` | 71 occurrences | model, procedure, or numerical illustration |

`Clearly` occurs frequently in the corpus, but a new TAC manuscript should replace it with the actual implication whenever the step is nontrivial.

## 7. Remark and Example patterns

### Remark

Use a Remark for one of these jobs:

1. interpret why a theorem matters;
2. give a special case or limiting case;
3. identify remaining design freedom;
4. distinguish coupled and decoupled designs;
5. state realizability or feasibility restrictions;
6. compare with state-space, feedback-linearization, or backstepping approaches.

Do not hide an assumption required for correctness inside a Remark.

### Example

Preferred sequence:

$$
\text{physical/original equations}
\to
\text{variable elimination or transformation}
\to
\text{FAS model}
\to
\text{controller}
\to
\text{closed-loop equation}
\to
\text{parameter selection}
\to
\text{plots and interpretation}.
$$

If an example is continued across sections, keep the same numbering and explicitly state which earlier equations are reused.

## 8. Simulation-writing template

Report in this order:

1. model parameters and their source;
2. initial condition and reference/disturbance signals;
3. controller parameters and why they satisfy the theorem;
4. solver, step size, tolerances, and simulation horizon;
5. state or tracking response;
6. control input;
7. branch-specific quantities such as uncertainty estimates or feasibility margins;
8. what the plots demonstrate—and what they do not prove.

Never change a source parameter merely to reproduce a desired curve without first documenting the necessity and effect.

## 9. Duan style versus TAC style

| Duan corpus tendency | Recommended TAC adaptation |
|---|---|
| long motivation comparing FAS and state space | shorten to the precise obstruction addressed by the paper |
| `Clearly` or `It can be easily observed` | show the algebraic implication |
| repeated explanation of the FAS philosophy | state it once, then focus on the new theorem |
| broad statements of advantage | compare assumptions, domain, controller, and conclusion explicitly |
| theorem followed by several interpretive remarks | retain only remarks that affect novelty, implementation, or limitations |
| simulation after a long analytic example | keep traceability but state the comparison baseline and metrics |

Preserve Duan's terminology, notation, and logical chain. Do not copy promotional rhetoric or grammatical idiosyncrasies mechanically.

## 10. Final drafting check

- model family identified;
- symbols selected from the correct branch;
- dimensions stated;
- stacks defined before use;
- theorem follows the six-part order;
- proof begins with explicit substitution;
- exact performance conclusion stated;
- global FAS and SUB-FAS conclusions not mixed;
- source formula reopened when mathematical correctness matters;
- TAC adaptation applied without changing the mathematics.

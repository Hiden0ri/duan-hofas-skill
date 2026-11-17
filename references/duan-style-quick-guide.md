# Duan HOFAS notation and writing quick guide

## Purpose

Use this file together with [duan-writing-corpus.md](duan-writing-corpus.md) by default to check, draft, or polish an existing Markdown/manuscript or to create a Duan-style paper skeleton. It distills recurring notation, authentic phrasing, and structural organization; for an exact mathematical claim, search the monograph or open the relevant original paper.

Default review order:

1. identify the model family;
2. check Duan-first concepts, symbols, dimensions, and absence of index collisions;
3. check the boundary between the unnumbered `Notations:` paragraph and model-specific definitions;
4. check that each paper-local shorthand follows the mathematical object on which it depends, and that controllers are constructed before closed-loop equations;
5. check terminology (`the ith subsystem` in switched systems, $|\varphi_i|$ instead of invented `"score"`, `"state-space form"` instead of `"first-order form"`);
6. check definitions, assumptions, and problems (separating Duan `[E]` from paper-added `[D]`);
7. check that every Theorem, Lemma, Proposition, and Corollary states its purpose inside its own statement, and check the six-part theorem structure;
8. check Duan proof templates (substitution-first, trajectory-feasibility ROEA, `Duan & Zhou 2022` Lemma 4.4 contradiction, `Part III` / `Volume I` high-order backstepping);
9. check Introduction ~1.5-page scale, three-line tables, Remark boundaries, Example/simulation narration (`"… are shown in Fig. X"`, `"It can be observed that …"`), short figure captions, `matlab/p1ot.m` plot rules, and orphan-word/Overfull layout safety.

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

Define the general convention $x^{(i\sim j)}$ in `Notations` before relying on it. This does not mean that a model-specific shorthand such as $X$ should also be defined there: introduce $X$ in the body after the relevant model has supplied its meaning, normally near first use. Do not alternate between an expanded stack and a newly invented state symbol without a reason.

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

The conclusion must name the controlled quantity, convergence type, domain of initial conditions, and exact set or performance bound. Across all 190 Theorems in the 32-paper + *Volume I* corpus, **`Let ...` openings (`63.7%`, e.g., `"Let Assumptions A1–A2 be met, and F_{0\sim n-1} be a matrix making \Phi(F_{0\sim n-1}) Hurwitz. Then..."`) and referencing a pre-constructed numbered controller (`is given by (30)`) are just as canonical as `Suppose that...` (`12.1%`) and inline controller displays**; see [theorem-writing-template.md](theorem-writing-template.md) (`T1–T6`, `L1–L6`, `P1–P5`, `C1–C4`) and [corpus-conflict-resolution.md](corpus-conflict-resolution.md). **Every Theorem, Lemma, Proposition, and Corollary must state its purpose explicitly inside its own statement** (never relegate the real goal—such as strict ROEA enlargement or Zeno exclusion—to a surrounding sentence or Remark).

## 5. Proof organization

Duan's recurring constructive proof order is:

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

Open proofs directly with the deduction or object definition (do not start single-conclusion proofs with `"We first show that..."`). Useful verified paragraph openings and templates (full verbatim templates in [duan-writing-corpus.md](duan-writing-corpus.md)):

```text
Substituting control law (...) into system (...) gives ...
The closed-loop system (...) is equivalent to the following state-space form: ...
In view of (...), we have ...
It follows from (...) and Assumption ... that ...
Combining (...) and (...), we obtain ...
The first conclusion is then proven. / It remains to show that ...
The proof is finished. / This completes the proof. / The proof is completed.
```

- **Proof by contradiction (`Duan & Zhou 2022` Lemma 4.4 `[E]`)**: `"Suppose that [negation]. Then it follows from (x) that … Therefore, there exists … such that …, which means that [A]. On the other side, … implies that [not A]. This yields a contradiction. Thus [conclusion]. The proof is finished."` (Do not write `"We prove by contradiction"` or `"on the contrary"`.)
- **High-order backstepping (`Part III` §4 / `Volume I` §9.2 `[E]`)**: Pre-compute $\tilde P_i(A_i^{0\sim m_i-1})$ $\to$ `The First Step` ($\tilde P_2 z_2^{(0\sim 1)} = x_2^{(0\sim 1)} - [\alpha_1^\top\ 0]^\top$, $\alpha_1$) $\to$ `The Second / k-th Step` ($\dot\alpha_{k-1} = h_{k-1} + \Delta h_{k-1}$, $\alpha_k$ with $+v_{k-1}$) $\to$ `The n-th Step` ($u$) $\to$ `The Conclusion` ($V=\sum V_i$ telescoping to $\dot V\le -\mu V+n\varepsilon$, ending with `"The above process clearly proves the following result."` before `Theorem`).
- For a SUB-FAS, always prove full-time trajectory feasibility ($X(t)\in\mathcal F$ for all $t\ge 0$) in addition to closed-loop linear stability.

## 6. Verified high-frequency language

Counts below come from the main text and appendices of the 2026 Volume I extraction (supplemented by the 22-paper verbatim corpus in [duan-writing-corpus.md](duan-writing-corpus.md)). **Actively prefer Duan's authentic expressions** when drafting or polishing, while writing out nontrivial algebraic steps explicitly and avoiding AI-flavored defensive `"not X, but Y"` disclaimers:

| Phrase | Count | Function |
|---|---:|---|
| `Substituting` | 70 | begin direct algebraic substitution |
| `Therefore` | 74 | state a derived consequence |
| `It follows from` | 65 | cite the basis of a step at sentence start |
| `In view of` | 41 | combine prior equations or assumptions (`In view of`, never `In the view of`) |
| `The above result / theorem` | 58 (papers) | interpret what a proved result reveals or converts |
| `Let us consider` / `Consider` | 33+ | introduce a model, subsystem, or example |
| `Suppose that` | 20+ | introduce theorem hypotheses or contradiction negation |
| `guarantees that` | 14 | introduce the performance conclusion |
| `clearly has the following expression:` | verified `[E]` | introduce an explicit feasible/ROEA set expression |
| `construct the following controller:` | verified `[E]` | introduce controller on the feasible set before closed loop |
| `Remark` | 84 occurrences | interpretation, comparison, DOFs, or special case (never hide proof-bearing main claims here) |
| `Example` | 71 occurrences | model, procedure, or numerical illustration |

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

## 8. Simulation, figure captions, and `matlab/p1ot.m` template

Report in this order:

1. model parameters and their exact provenance (separating cited plant parameters `[E]` from paper-assumed terms `[D]`);
2. initial value $X_0$ and reference/disturbance signals;
3. controller parameters $A_{0\sim n-1}$, resulting Hurwitz $\Phi(A_{0\sim n-1})$, controller expression, and assigned closed-loop equation;
4. numerical integration method, step size, tolerances, and event-handling rule;
5. figure references using Duan's sentence pattern: `"The simulation results are shown in Fig. X. It can be observed that …"` / `"… are illustrated in Fig. X."` (never `"To illustrate …, Fig. X presents …"`);
6. short figure captions (2–6 word noun phrases, e.g., `"State variables."`, `"Closed-loop response and switching signal."`, `"Singular sets and the state trajectory."`, without repeating proved theorems or multi-sentence explanations);
7. MATLAB plotting rules per user's `matlab/p1ot.m`: solid `'b-'`/`'r-'`/`'m-'` with `'linewidth', 1`, LaTeX legend `'FontSize', 12`, dashed reference lines `[0.15, 0.15, 0.15]` at `'LineWidth', 1.5`, no grid, no figure title, `axis square`, explicit `xlim`/`ylim`, `'Time(s)'` x-label, Duan variable-symbol y-labels (`'$x$ and $\dot x$'`, never `'States'`), and red vertical dashed lines `'r--'` with x-tick timestamps at switching instants;
8. accurate scope of numerical evidence—never call a finite-horizon simulation or sampled plot a proof or exact ROEA.

Never change a source parameter merely to reproduce a desired curve without first documenting the necessity and effect.

## 9. Duan style alignment vs. AI-prose pitfalls

| Pitfall to avoid | Duan-aligned practice |
|---|---|
| stripping out Duan's natural phrases (`clearly has the following expression`, `construct the following controller`) | retain and use Duan's authentic expressions from [duan-writing-corpus.md](duan-writing-corpus.md) |
| defensive `"not X, but Y"` disclaimers scattered across sections | state definitions and scope conditions positively once |
| hiding a proposition/corollary's true goal in a Remark | state the exact goal inside the Proposition/Corollary/Lemma/Theorem itself |
| single-claim proof opening `"We first show that..."` | start directly with `"Let ... By (...), ..."` or `"It follows from (...) that..."` |
| long multi-sentence figure captions + `"To illustrate ..., Fig. X presents..."` | 2–6 word noun-phrase caption + `"… are shown in Fig. X. It can be observed that …"` |
| skipping a nontrivial squeeze/continuity step behind `"Clearly"` | keep Duan's connector rhythm while writing out the explicit mathematical inequality |

## 10. IEEE Transactions opening, Notations, and tables

### 10.1 Introduction scale

For an approximately eight-page IEEE Transactions manuscript, use about one and a half pages for the Introduction as the default editing target. This is a proportional drafting rule rather than a source theorem or an inflexible venue limit. The Introduction should normally contain the motivation, focused literature gap, contributions, organization, and the compact `Notations:` paragraph without crowding out the technical sections.

### 10.2 What belongs in `Notations`

Place an italic `Notations:` paragraph at the end of the Introduction for conventions used throughout the article, for example:

```latex
\emph{Notations:} The arguments $(t)$ of variables are omitted when no
confusion arises. For any $x\in\mathbb R^r$,
\begin{equation*}
x^{(0\sim n-1)}=
\begin{bmatrix}
x^\top & \dot x^\top & \cdots & (x^{(n-1)})^\top
\end{bmatrix}^{\top}.
\end{equation*}
```

Use `=` for these notation conventions. Do not use `:=`, `\operatorname{col}`, or `\col`; display the row or column stack explicitly in the form used by Duan. The same rule applies to notation-only displays for parameter rows and companion matrices.

Keep model-specific constructions out of this paragraph. In particular, a convenience state $X$, a feasible set, a singularity margin, a switching map, or an ROEA belongs in the body where its mathematical role first appears. New switching-extension symbols are legitimate paper-local notation, but they must not be presented as Duan's original notation.

### 10.3 Model before dependent notation

State the mathematical object being studied before introducing any paper-local abbreviation derived from it. For example, when a single-order affine HOFAS is the selected model family, one may write

```latex
\begin{equation}
x^{(n)}=f_i\!\left(x^{(0\sim n-1)}\right)
+B_i\!\left(x^{(0\sim n-1)}\right)u_i,
\end{equation}
For convenience, define
\begin{equation}
X=x^{(0\sim n-1)}.
\end{equation}
```

Retain time arguments when the selected Duan model family is time varying, and replace this example with the correct single-order, multi-order, affine, nonaffine, global-FAS, or SUB-FAS form. The reusable rule is only the dependency order: the model must precede a shorthand defined from that model. It does not prescribe a fixed order for feasible sets, assumptions, controllers, switching quantities, or later results; arrange those items according to the mathematical argument of the manuscript.

In Duan's 32 first-author papers, `:=` appears `0/32` times `[E]`: body definitions use `=` (`8/32` papers, e.g., `Duan 2023 TCYB`) or `\triangleq` (`24/32` papers, e.g., `Overview 2024`, `OD-FAS 2026`), whereas `:=` comes from coauthored papers such as `Yang & Duan 2026`. Prefer `=` or `\triangleq` in pure Duan style (see [corpus-conflict-resolution.md](corpus-conflict-resolution.md)).

### 10.4 Tables

Use the IEEE three-line table form by default. Load `booktabs`, use `\toprule`, `\midrule`, and `\bottomrule`, and omit vertical rules and fully boxed grids:

```latex
\begin{table}[t]
\caption{...}
\label{tab:...}
\centering
\begin{tabular}{lll}
\toprule
Item & Condition & Meaning \\
\midrule
... & ... & ... \\
\bottomrule
\end{tabular}
\end{table}
```

Use `table*` only when the content genuinely requires both columns; do not replace the three-line structure with dense cell borders.

## 11. Final drafting check

- Introduction is proportionate to the manuscript; for an eight-page Transactions draft, about one and a half pages is the default target;
- article-wide conventions are in the end-of-Introduction `Notations:` paragraph;
- notation displays use `=` and explicit matrix stacks, not `:=`, `\operatorname{col}`, or `\col`;
- each paper-local shorthand follows the model or object on which it depends, while the remaining definitions follow the manuscript's own logic;
- tables use `\toprule`, `\midrule`, and `\bottomrule` without vertical rules;
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

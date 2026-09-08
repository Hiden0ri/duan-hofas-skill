# Distilled habits from Duan-first-author FAS papers

## Corpus boundary

This file describes recurring habits in the selected Duan-first-author core: Chinese High-Order System Approach I–III; English HOFAS Parts I–X; SUB-FAS; continuous-time delay Parts 1–2; generalized chained forms Parts 1–2; constrained unidirectionally connected FASs Parts I–III; four types of underactuated systems; output-dependent FAS Parts 1 and 4; the overview; and the sole-authored 2026 Volume I.

It does not infer habits from papers with another first author.

## 1. Modeling habit: control-oriented representation `[E]`

Duan repeatedly contrasts two operations:

- variable extension and order reduction → more first-order state equations;
- variable elimination and order elevation → fewer, higher-order equations that expose the control vector.

The characteristic research move is therefore:

$$
\text{original equations}
\longrightarrow
\text{eliminate intermediate variables}
\longrightarrow
\text{HOFAS/FAS model}
\longrightarrow
\text{solve explicitly for }u.
$$

When analyzing a new plant, do not begin by declaring it HOFAS. Show the elimination/transformation and its domain.

## 2. Definition habit: define the class through the input map `[E]`

For affine models, the decisive object is the square input coefficient $B(\cdot)$. For nonaffine models, it is the map from $u$ to the generalized input $w=g(\cdot,u)$. The classification is stated only after dimensions and domains are declared.

For SUB-FAS work, Duan defines singular and feasible sets before defining substability or giving the controller.

## 3. Notation habit: define compact stacks early `[E]`

Most papers devote an early paragraph or section to:

- spaces, identity matrices, empty sets, and complements;
- derivative stacks $x^{(n_1\sim n_2)}$;
- consecutive-variable stacks $x_{i\sim j}$;
- heterogeneous-order stacks $x_k^{(n_k)}\vert_{k=i\sim j}$;
- parameter rows $A_{0\sim n-1}$;
- companion matrices $\Phi(A_{0\sim n-1})$.

Later equations rely heavily on those shorthands. A faithful manuscript should define them once and then use them consistently rather than alternating between expanded and abbreviated forms.

## 4. Controller habit: separate cancellation from desired dynamics `[E]`

A recurring decomposition is

$$
u=-B^{-1}(\cdot)\,[f(\cdot)+u^*],
$$

with $u^*$ then selected from parameter matrices, an external command, robust/adaptive terms, or a tracking objective. Sign conventions differ by paper, so this is a structural pattern, not a formula to paste blindly.

The explanation normally distinguishes:

1. cancellation/model transformation;
2. choice of the linear closed-loop relation;
3. parameter design for eigenstructure or performance.

## 5. Proof habit: substitute first, analyze second `[E]`

The canonical proof step is direct substitution:

$$
\text{plant} + \text{control law}
\Longrightarrow
\text{constant linear closed-loop equation}.
$$

Only then are stability, tracking, optimality, robustness, or feasibility invoked. For SUB-FAS, a second proof layer checks that the closed-loop response remains inside the feasible set.

## 6. Parameterization habit: expose design freedom `[E]`

Duan frequently presents $A_{0\sim n-1}$ or its multi-order blocks as design variables, then uses eigenstructure assignment or generalized Sylvester equations to parameterize solutions. Remaining free matrices are explicitly advertised for additional performance requirements.

Do not reduce a parametric result to one numerical gain unless the task is solely an example. Retain:

- the free parameter;
- its admissibility/nonsingularity condition;
- the property it can tune.

## 7. Coupled/decoupled habit `[E]`

For multi-order systems, Duan often gives:

- a coupled design producing one overall linear system;
- a decoupled or block-decoupled design producing smaller independent linear systems.

The paper then explains how grouping or reordering variables affects feasibility and degrees of freedom. Do not call a block-diagonal target “decoupled” unless the plant transformation and feasibility conditions support the claim.

## 8. Assumption habit `[E]`

Assumptions are commonly labeled A1, A2, and so on. Typical roles are:

- full actuation or nonsingularity;
- smoothness/differentiability sufficient for repeated differentiation;
- uncertainty bounds;
- availability of delayed histories or predictor uniqueness;
- rank/nonsingularity of transformation matrices;
- stable target parameter matrices.

Every assumption must be traced to the exact step where it is used. Avoid writing a generic “all functions are sufficiently smooth” if the proof needs a particular derivative order.

## 9. Theorem habit `[E]`

A common theorem contains three layers:

1. a control law is given;
2. the resulting closed-loop equation is stated explicitly;
3. the performance or attraction-region conclusion follows under named matrix/feasibility conditions.

Many SUB-FAS theorems also state the ROEA as a set of initial conditions whose matrix-exponential response satisfies a singularity-function inequality for every $t\ge0$.

Theorem 3.5 of Duan's Part III gives a more granular sentence-level order, also captured by the user's Zotero note “Duan规范”:

$$
\boxed{
\text{system}
\to
\text{named assumptions}
\to
\text{given parameters}
\to
\text{parameter conditions}
\to
\text{control law}
\to
\text{guaranteed performance}
}
$$

This order is stronger than a generic “assume–then” template because it keeps fixed data, design freedom, admissibility conditions, and the final guarantee logically separate. Apply [theorem-writing-template.md](theorem-writing-template.md) when drafting or auditing a theorem.

## 10. Remark habit `[E]`

Remarks commonly serve to:

- answer the objection that the FAS model looks too special;
- explain relation to state-space, feedback linearization, flatness, or strict-feedback systems;
- distinguish physical full actuation from generalized full actuation;
- identify remaining design freedom;
- point out special cases and model reductions;
- explain feasibility restrictions after a theorem.

When adapting this habit, keep only claims supported by a theorem or transformation. Do not reproduce broad promotional claims without evidence.

## 11. Example habit `[E]`

Duan often uses a chain of examples:

1. introduce a system as motivation;
2. revisit it after the general model is defined;
3. revisit it again after controller synthesis;
4. add numerical simulation only after the analytic transformation and controller are complete.

The delay papers explicitly use “Continuation of Example …” to connect modeling, control, and constraint analysis. Preserve that traceability in a reproduction notebook.

## 12. Simulation habit `[E]`

Recurring choices include:

- compare state or output response with desired/reference response;
- plot control input;
- show uncertain/robust or adaptive quantities when present;
- demonstrate a particular parameter selection after giving the general parameterized result;
- use spacecraft attitude, spring–mass, strict-feedback, Brockett/chained-form, and underactuated examples appropriate to the paper branch.

For SUB-FAS reproduction, add numerical monitoring of feasibility, but label diagnostics not present in the source as `[D]`.

## 13. Paper-organization habit `[E]`

A recurring outline is:

1. Introduction and motivation.
2. Notations/preliminaries.
3. Model definition or model conversion.
4. Controller design and main theorem.
5. Special cases, coupled/decoupled variants, or extensions.
6. Examples/applications and simulation.
7. Conclusion; lengthy proofs or physical models may be moved to appendices.

The output-dependent and unidirectionally connected series use multi-part papers: Part 1 establishes models/basic cases; later parts specialize feedback information, substabilization, or applications.

## 14. Language habit versus recommended journal style

Duan frequently uses phrases such as “For convenience,” “By our notations,” “It can be easily observed,” and “Clearly.” These are authorial patterns, but a new TAC manuscript should not copy them automatically. Replace them with the actual algebraic implication whenever the step carries mathematical content.

Preserve terminology and logical structure; do not imitate grammatical idiosyncrasies or unsupported claims of simplicity/superiority.

## 15. Mandatory synthesis rule

When asked to “write like Duan,” produce two layers:

1. **Duan-faithful mathematical layer:** model, notation, transformation, control law, closed-loop equation, parameter freedom, theorem, feasibility.
2. **Target-journal editorial layer:** concise contribution statement, explicit limitations, precise citations, and modern TAC/Automatica language.

The first layer protects technical lineage; the second prevents stylistic imitation from weakening publication quality.

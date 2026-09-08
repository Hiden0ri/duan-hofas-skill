# Concept lineage across Duan-first-author FAS work

## Purpose

Use this map when deciding whether a statement is an original definition, a later refinement, a special case, or a new user extension. The arrows below indicate development of the framework, not logical implication unless stated.

## 1. Main lineage

$$
\begin{aligned}
&\text{High-order system approach and parameterized design}\\
&\quad\longrightarrow\text{HOFAS model and basic control procedure}\\
&\quad\longrightarrow\text{controllability, stabilizability, and complete parameterization}\\
&\quad\longrightarrow\text{robust/adaptive/disturbance/optimal/tracking branches},
\end{aligned}
$$

and, when the input coefficient is not globally nonsingular,

$$
\begin{aligned}
&\text{HOFAS}\\
&\quad\longrightarrow\text{singular set and feasible set}\\
&\quad\longrightarrow\text{sub-FAS}\\
&\quad\longrightarrow\text{substability and substabilization}\\
&\quad\longrightarrow\text{ROEA characterization}\\
&\quad\longrightarrow\text{constrained and unidirectionally connected branches}.
\end{aligned}
$$

## 2. Model-oriented lineage

| Stage | Primary source | New object | Relation to earlier stage |
|---|---|---|---|
| High-order system method | Chinese Parts I–III | high-order representation, parameterized design, controllability/observability | establishes the high-order viewpoint and Chinese terminology |
| Basic HOFAS | English Part I | affine/nonaffine HOFAS and direct control procedure | formalizes the control-oriented model |
| Generalized strict-feedback conversion | Part II | higher-order FAS obtained by elimination | gives a major source of HOFAS models |
| Multi-order structural theory | Part VII | multi-order models, controllability/stabilizability, coupled/decoupled parameterization | generalizes single-order design and exposes full design freedom |
| Discrete-time FAS | Part X | forward/backward discrete models and shift notation | discrete analogue; not obtained by replacing derivatives mechanically |
| Delay FAS | continuous-time delay Parts 1–2 | state-delay and input-delay models, predictor constructions | adds histories and delay-dependent feasibility |
| Output-dependent FAS | OD-FAS Parts 1 and 4 | FAS representations/control using declared output information | changes the information structure of feedback |
| Constrained UC-FAS | UC-FAS Parts I–III | constraints and unidirectional connection | decomposes feasibility and design across connected subsystems |

## 3. Control-objective lineage

| Source | Objective added to the basic FAS backbone | Invariant backbone |
|---|---|---|
| Part III | robust control and high-order backstepping | expose input, transform/cancel known dynamics, close stability proof |
| Part IV | adaptive control and high-order backstepping | same model-first workflow with parameter adaptation |
| Part V | robust adaptive control | explicit uncertainty-bound and parameter-error assumptions |
| Part VI | disturbance attenuation and decoupling | constant linear target plus parameterized disturbance-channel design |
| Part VIII | optimal control and spacecraft attitude stabilization | select parameter matrices through a stated cost/performance problem |
| Part IX | generalized PID and model-reference tracking | embed tracking/reference dynamics in the high-order formulation |

These are not interchangeable controller formulas. “Same backbone” means the research organization recurs; each theorem retains its own information and uncertainty assumptions.

## 4. SUB-FAS lineage

### 4.1 Qualitative full actuation

For the affine system, global nonsingularity gives a global FAS. Once singular points exist but feasible points remain, the object becomes a sub-FAS.

### 4.2 Singularity classification

The 2023 SUB-FAS paper and overview distinguish

$$
\mathcal S=\mathcal S_0\cup\mathcal S_\infty,
$$

leading to 0-type, $\infty$-type, and mixed-type sub-FASs.

### 4.3 Origin–feasible-set relation

The Chinese sub-strict-feedback paper classifies rational, critically rational, and irrational sub-FASs by the position of the origin relative to the feasible set. This classification is different from the $0/\infty$ singularity classification; neither replaces the other.

### 4.4 Substability and ROEA

The stable target matrix determines a candidate exponentially convergent linear response. Feasibility of that entire response selects admissible initial values. Hence the ROEA depends jointly on:

$$
\text{open-loop feasible set}
+
\text{chosen closed-loop parameter matrices}.
$$

Later ROEA characterization work refines how this set is described or computed; it does not make the feasible set controller-dependent.

## 5. Underactuated and chained-form lineage

The four-type underactuated paper and the generalized chained-form series use transformation to obtain FAS/sub-FAS-related control problems. Preserve the distinction:

$$
\text{original plant is underactuated}
\not\Rightarrow
\text{original plant is physically fully actuated}.
$$

The method constructs an equivalent higher-order or connected representation under stated structural conditions.

## 6. User's switched SUB-FAS project `[D]`

The following is a proposed extension rather than a Duan definition:

$$
\{\text{multiple sub-FAS modes}\}
+
\{\text{state-dependent switching law}\}
\longrightarrow
\text{switching feasibility and extended ROEA}.
$$

Use the Duan lineage only up to each subsystem's $\mathcal F_i$, controller, and ROEA. Mark union-based feasibility, maximum-margin switching, non-Zeno arguments, and extended ROEA as `[D]` unless another primary source is cited.

## 7. Lineage audit questions

Before claiming novelty, answer:

1. Where did the concept first appear in the selected corpus?
2. Is the present form a definition, theorem, corollary, or example?
3. Did a later Duan-first-author paper change its domain, quantifier, or information pattern?
4. Is the new work adding a mechanism, or only renaming an existing set/controller?
5. Which exact earlier theorem becomes a special case of the proposed result?


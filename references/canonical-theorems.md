# Canonical theorem families

This is a theorem map, not verbatim theorem text. Reopen the primary source before quoting or numbering a theorem.

## 1. Full actuation and assignable linear dynamics `[E]`

For an affine global FAS with square nonsingular $B(\cdot)$, the explicit control law cancels the nonlinear term and produces a designer-selected constant linear closed-loop system.

Proof obligation: establish the inverse on the whole declared domain and substitute the controller exactly.

Primary sources: Part I, Proposition 2.2; 2026 monograph, Chapter 3.

## 2. Controllability and equivalent FAS representation `[E]`

A controllable linear system can be transformed equivalently into a multi-order global FAS, with the converse under the theorem's stated transformation conditions.

Proof obligation: preserve input dimension, nonsingularity, and equivalence; do not infer that every arbitrary nonlinear system is globally FAS.

Primary sources: Chinese Part II; Part VII; 2024 overview, Theorem 1.

## 3. Feedback linearizability and FAS conversion `[E]`

The overview relates feedback linearizability to conversion into an FAS under smoothness and rank conditions.

Proof obligation: retain the exact domain and local/global quantifier. A local diffeomorphism cannot justify a global conclusion.

Primary source: 2024 overview, Theorems 2–4.

## 4. Multi-order coupled and decoupled control `[E]`

Parameter matrices yield either a coupled constant linear closed-loop system or decoupled constant linear closed-loop systems.

Proof obligation: verify $r_k$, $\mu_k$, grouping, and common $B(\cdot)$ invertibility.

Primary sources: Part VII; constrained counterparts in the SUB-FAS paper; overview, Theorem 6.

## 5. Substabilization and ROEA `[E]`

For a sub-FAS, stable $\Phi(A_{0\sim n-1})$ and an initial value whose linear response remains in $\mathcal F$ produce exponential convergence while the controller remains defined. These initial values form the ROEA.

Proof obligation: prove both stability of $\Phi$ and full-time feasibility. Neither implies the other.

Primary sources: “Substability and Substabilization,” Theorems 1–4; overview, Theorems 7–8; 2026 ROEA paper for later characterization.

## 6. Robust/adaptive high-order backstepping `[E]`

These theorems establish boundedness and convergence/performance under explicitly structured uncertainties and robust/adaptive laws.

Proof obligation: retain every bound, regressor, sign, gain, and differentiability assumption. Do not transfer a result to unknown control directions or unmodeled dynamics without proof.

Primary sources: Parts III–V and the corresponding 2026 monograph chapters.

## 7. Disturbance attenuation and decoupling `[E]`

Part VI uses the FAS representation and parameter freedom to formulate disturbance attenuation or decoupling.

Proof obligation: distinguish exact decoupling, almost decoupling, and attenuation; retain performance output and disturbance channels.

## 8. Optimal, generalized PID, tracking, and discrete time `[E]`

- Part VIII: optimal control with spacecraft attitude stabilization.
- Part IX: generalized PID and model-reference tracking.
- Part X: forward/backward discrete-time models and control.

Proof obligation: do not reuse continuous-time derivatives in discrete time; retain shift operators and initial histories.

## 9. Underactuated-system conversion `[E]`

Duan treats four types of underactuated systems by transformation to FAS-related forms. This does not mean the original plant is physically fully actuated.

Proof obligation: give the transformation, its domain, the remaining subsystem, and control recovery.

Primary source: “Stabilisation of four types of underactuated systems: a FAS approach.”

## 10. Caution checklist

- “Arbitrarily assignable eigenstructure” requires the source's controllability/parameterization conditions.
- Stable closed-loop matrices do not give global stabilization for a sub-FAS if a response meets the singular set.
- $\det B\ne0$ gives qualitative invertibility; bounded input or conditioning normally needs a quantitative margin such as $\sigma_{\min}(B)$.
- A simulation supports one configuration; it does not prove a theorem.
- Retain “if and only if” only when the source proves both directions.

## 11. Canonical theorem statement order `[E]`

Duan's Part III, Theorem 3.5, provides a verified theorem-writing sequence:

$$
\text{system and named assumptions}
\to
\text{arbitrarily given parameters}
\to
\text{matrix parameters satisfying a cited condition}
\to
\text{control law and auxiliary definitions}
\to
\text{explicit performance set}.
$$

This is a statement-organization pattern, not a theorem that can be reused without its original hypotheses. For the exact roles of each clause and a drafting form, use [theorem-writing-template.md](theorem-writing-template.md).

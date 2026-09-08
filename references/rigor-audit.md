# Duan-faithful and modern-rigor audit

## Two-layer rule

Never silently rewrite the source theorem. Present:

### Layer 1 — Duan-faithful reconstruction `[E]`

- original model and notation;
- assumptions exactly as stated;
- original controller;
- original derivation and conclusion;
- precise locator;
- any ambiguity preserved and marked `[U]`.

### Layer 2 — rigor enhancement `[D]`

- missing regularity conditions needed for the claimed solution concept;
- local/global and pointwise/uniform distinctions;
- quantitative conditioning or input-bound conditions;
- constraint, robustness, and implementability checks;
- a corrected or strengthened theorem, clearly separated from the source.

Do not modify Layer 1 to absorb Layer 2.

## Audit A: well-posedness

Check:

1. What is the state of the equivalent first-order system?
2. Is the closed-loop right-hand side continuous in time?
3. Is it locally Lipschitz in the state, or is another solution concept declared?
4. Does the control law remain finite on its domain?
5. Is the solution unique?
6. What prevents finite escape?
7. For delays, is a complete initial history supplied?
8. For switching, what happens on switching surfaces and at ties?

If the paper assumes “sufficiently smooth,” identify the derivative and Lipschitz consequences actually used instead of inventing a stronger global condition.

## Audit B: full actuation versus conditioning

The qualitative condition

$$
\det B(X,t)\ne0
$$

guarantees pointwise invertibility. It does not by itself give a uniform bound on $B^{-1}$ over a noncompact domain.

For a quantitative enhancement, examine

$$
\sigma_{\min}(B(X,t))
$$

and, on the relevant set, seek

$$
\sigma_{\min}(B(X,t))\ge\underline\beta>0.
$$

This is a rigor enhancement `[D]` unless the selected source explicitly uses it. Do not replace Duan's singular/feasible-set definition by this stronger condition.

## Audit C: stability vocabulary

Keep these conclusions separate:

- Lyapunov stability;
- asymptotic stability;
- exponential stability;
- global versions of the above;
- substability on a stated attraction region;
- practical or ultimate boundedness;
- finite-/fixed-/prescribed-time convergence.

Never infer a stronger item from a weaker one. For SUB-FAS, state both the attraction region and whether the origin is an interior or boundary point when relevant.

## Audit D: ROEA claim type

Classify every ROEA result as one of:

1. **definition** — specifies which initial values qualify;
2. **exact characterization** — proves an equivalent condition;
3. **inner estimate** — proves a computable subset;
4. **outer estimate** — proves a containing set;
5. **numerical approximation** — samples or optimizes a boundary;
6. **visualization only** — illustrates selected trajectories.

Do not call a trajectory-defined exact characterization an “analytic closed-form solution.” Do not call a finite sampled plot an exact ROEA.

## Audit E: model equivalence

For elimination/order elevation, check:

- forward transformation;
- reverse reconstruction;
- invertibility/rank of every transformation matrix;
- excluded singular points;
- preservation of initial conditions;
- preservation of control dimension;
- whether differentiation introduces compatibility requirements.

Without both directions, write “derived representation” rather than “equivalent transformation.”

## Audit F: information and implementability

Check whether the controller requires:

- unmeasured state derivatives;
- unknown parameters without an estimator;
- future delayed inputs;
- exact disturbance values;
- inversion of a near-singular matrix;
- discontinuous switching with no solution convention;
- unbounded control.

Separate theoretical existence from implementable realization.

## Audit G: assumptions and quantifiers

For each assumption, record:

| Assumption | Mathematical content | Used in proof step | Local/global | Pointwise/uniform |
|---|---|---|---|---|

Red flags:

- “for every initial value” becomes “for selected initial values” without notice;
- a matrix is nonsingular at $t=0$ but treated as nonsingular for all $t$;
- compactness is invoked for an unbounded set;
- pointwise positive quantities are treated as uniformly bounded away from zero;
- a parameter is selected separately for each initial value but described as one fixed controller.

## Audit H: simulation evidence

Confirm:

- original parameters and initial conditions were used;
- solver tolerances and events are reported;
- no state/control saturation was silently introduced;
- singularity/feasibility is monitored for SUB-FAS;
- numerical stopping is not interpreted as mathematical convergence;
- the plot supports only the conclusion claimed.

## Required audit verdict

End a rigor audit with:

- **Source-faithful conclusion:** what Duan's stated result establishes.
- **Verified derivation:** what was independently checked.
- **Open gap:** what remains `[U]`.
- **Enhancement:** any added assumption/result `[D]` and why it is necessary.
- **Effect on the user's theorem:** unchanged, weakened, strengthened, or invalidated.


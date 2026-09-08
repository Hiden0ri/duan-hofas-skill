# Structural example library

## Selection principle

Choose an example by mathematical structure, not application name. Match, in order:

1. continuous/discrete time;
2. global FAS/sub-FAS;
3. single/multi-order;
4. affine/nonaffine input;
5. state/output/delayed information;
6. uncertainty and constraints;
7. control objective;
8. physical application.

## Example record schema

For every reproduced example, create:

| Field | Required content |
|---|---|
| Source | title, example/section, equation locator |
| Original plant | equations and physical variables |
| Model class | exact FAS/HOFAS/SUB-FAS branch |
| Elementary state | retained variable(s) |
| Eliminated variables | variables removed and recovery formulas |
| Input map | $B(\cdot)$ or nonaffine $g(\cdot,u)$ |
| Domain | transformation and inversion domain |
| Singular/feasible set | when applicable |
| Target dynamics | parameter matrices and $\Phi$ |
| Control law | exact source formula |
| Initial data | point or history |
| Numerical method | MATLAB solver, tolerances, horizon |
| Evidence | plots/numerical quantities tied to each claim |
| Deviations | necessity, approval, expected effect |

## Family A: physical global FAS

### Typical structure

$$
M(x,\dot x,t)\ddot x+D(x,\dot x,t)\dot x+K(x,\dot x,t)x=u.
$$

Best use: explaining physical versus generalized full actuation and direct second-order design.

Do not use when the research issue is singularity crossing or underactuation.

## Family B: strict-feedback conversion

Sources: Part II and the Chinese sub-strict-feedback paper.

Best use: demonstrating recursive elimination, $\breve h_i$, $\breve B_i$, transformation domain, and reduction of backstepping layers.

Required diagnostic: verify transformed and original trajectories agree after reverse reconstruction.

## Family C: parameterized multi-order design

Sources: Part VII, including multiple spring–mass examples.

Best use: controllability, coupled/decoupled target dynamics, and $F$–$Z$ design freedom.

Required diagnostic:

$$
\lVert\Phi(A_{0\sim n-1})-VFV^{-1}\rVert
$$

and $\det V(Z,F)$ or a numerically stable equivalent.

## Family D: robust/adaptive high-order backstepping

Sources: Parts III–V.

Best use: structured uncertainty, robust terms, adaptation, and comparison with conventional first-order backstepping.

Required plots: tracking/state error, input, uncertainty/adaptive quantity, and the theorem-specific Lyapunov or bound diagnostic where computable.

## Family E: disturbance attenuation/decoupling

Source: Part VI.

Best use: disturbance channel, output channel, generalized Sylvester equations, and parameterized attenuation.

Required diagnostic: the exact transfer/performance quantity used by the theorem, not merely a state plot.

## Family F: optimal spacecraft attitude

Source: Part VIII, spacecraft application section.

Best use: optimal selection of target dynamics and physical second-order FAS modeling.

Required checks: units, inertia, attitude representation, quaternion normalization if used, actuator assumptions, and cost value.

## Family G: generalized PID/model-reference tracking

Source: Part IX.

Best use: reference-model embedding and tracking rather than stabilization alone.

Required plots: reference/output, tracking error, input, and internal reference-model state if relevant.

## Family H: discrete-time FAS

Source: Part X and Duan-first-author discrete-delay papers.

Best use: step-forward/backward models, initial sequences, and discrete controllers.

Required checks: sampling index, history length, shift convention, and discrete companion matrix.

## Family I: SUB-FAS and ROEA

Sources: 2023 SUB-FAS paper, Chinese sub-strict-feedback paper, later Duan-first-author ROEA paper.

Best use: separating stable target dynamics from feasibility of the complete response.

Required diagnostics:

- singular/feasible-set plot when dimension permits;
- $\det B(X(t),t)$ as the source quantity;
- $\sigma_{\min}(B(X(t),t))$ only as an explicitly labeled enhancement `[D]`;
- inside/outside-ROEA initial conditions;
- control growth near the boundary.

## Family J: delays and prediction

Sources: continuous-time delay Parts 1–2.

Best use: delayed state stacks, initial histories, predictor equality, and input-delay compensation.

The papers' “Continuation of Example” chains are valuable: preserve the same plant and parameter data across modeling and control stages.

## Family K: generalized chained forms

Sources: generalized chained forms Parts 1–2.

Best use: Brockett-type obstruction, discontinuous versus continuous laws, and generalized nonholonomic structure.

Do not transfer smooth-stabilization conclusions between the two parts without checking topology and controller class.

## Family L: four types of underactuated systems

Source: “Stabilisation of four types of underactuated systems: a FAS approach.”

Best use: testing which transformation class a new underactuated plant belongs to.

Required record: type number, dimension/rank relation, transformed FAS/sub-FAS, leftover dynamics, and recovered physical input.

## Family M: constrained unidirectionally connected FASs

Sources: UC-FAS Parts I–III.

Best use: internal/external feasibility, subsystem connection, and constraints on state/control derivatives.

Do not replace the UC connection with an arbitrary switched or bidirectionally coupled interconnection.

## Family N: output-dependent FASs

Sources: OD-FAS Part 1 and Part 4.

Best use: control when only declared output positions/velocities are available.

Representative applications in Part 4 include flying-vehicle pitch and a two-DOF coupled underwater manipulator.

Required check: every controller signal must be constructible from the allowed output information and its declared dynamic extension.

## Nearest-example decision

Report the selection in one sentence:

> The nearest Duan example is ___ because both problems share ___, ___, and ___; it differs in ___, so formula ___ cannot be transferred without a new proof.


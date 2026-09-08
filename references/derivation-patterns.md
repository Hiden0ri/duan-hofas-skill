# Canonical derivation patterns

## A. Direct control of a global affine FAS `[E]`

Start from

$$
x^{(n)}=f\!\left(x^{(0\sim n-1)},t\right)+B\!\left(x^{(0\sim n-1)},t\right)u.
$$

Verify $\det B(\cdot)\ne0$ on the stated domain. Choose $A_0,\ldots,A_{n-1}$ and, if required, $v$. Write

$$
u
=
-B^{-1}(\cdot)
\left[A_{0\sim n-1}x^{(0\sim n-1)}+f(\cdot)-v\right].
$$

Substitute without skipping:

$$
\begin{aligned}
x^{(n)}
&=f(\cdot)+B(\cdot)u\\
&=f(\cdot)-A_{0\sim n-1}x^{(0\sim n-1)}-f(\cdot)+v\\
&=-A_{0\sim n-1}x^{(0\sim n-1)}+v.
\end{aligned}
$$

Therefore,

$$
x^{(n)}+A_{0\sim n-1}x^{(0\sim n-1)}=v.
$$

Only then infer stability, tracking, decoupling, eigenstructure, or optimality from the selected linear closed-loop system.

## B. Parameter-matrix design `[E]`

1. Select the desired closed-loop property.
2. Solve for $A_{0\sim n-1}$ by pole/eigenstructure assignment or the complete parametric method used in the source.
3. Insert the parameter matrices into the FAS control law.
4. Use remaining design freedom for secondary objectives.

Do not call arbitrary pole selection “optimal”. Part VIII adds an explicit optimal-control construction.

## C. Variable elimination and order elevation `[E]`

1. Partition variables according to input dimension and structural order.
2. Differentiate selected elementary variables only as often as required.
3. Recursively substitute lower equations to eliminate intermediate variables.
4. Collect the input in the highest-order equation.
5. Verify the resulting input coefficient or map satisfies the full-actuation condition.
6. Design the controller in HOFAS coordinates.
7. Recover eliminated variables and verify equivalence on the stated domain.

Uniform-dimension, increasing-dimension, generalized strict-feedback, and underactuated systems require different transformations. Never reuse one paper's formula without its structural hypotheses.

## D. High-order backstepping `[E]`

Duan's Parts III and IV treat a high-order subsystem as one design layer rather than decomposing every subsystem into scalar first-order equations:

1. specify a desired high-order virtual-control relation;
2. construct the layer error;
3. differentiate the Lyapunov function along the high-order error dynamics;
4. select robust or adaptive terms for the stated uncertainty model;
5. proceed layer by layer and close the final actual-input equation.

Read the relevant source theorem before reproducing a formula. “High-order backstepping” does not license invented compensating terms.

## E. Sub-FAS and ROEA `[E]`

Use the algebraic control law only on $\mathcal F$:

$$
u=-B^{-1}(\cdot)\left[A_{0\sim n-1}x^{(0\sim n-1)}+f(\cdot)\right].
$$

Then:

1. choose $A_{0\sim n-1}$ such that $\Phi(A_{0\sim n-1})$ is stable;
2. calculate $e^{\Phi t}X_0$;
3. impose feasibility along the complete response;
4. define the ROEA from initial values satisfying that condition;
5. conclude exponential convergence only for those initial values.

The order is controller/parameter choice → response → trajectory feasibility → ROEA. An ROEA can guide redesign, but is not independent of the chosen closed loop.

## F. Coupled and decoupled multi-order designs `[E]`

- Coupled design: group all high-order variables and assign one full-dimensional linear closed-loop system.
- Decoupled design: group blocks and choose block parameter matrices to obtain lower-dimensional linear closed-loop systems.

Variables entering $B(\cdot)$ remain subject to feasibility. Algebraic decoupling does not remove that constraint unless a theorem proves it.

## G. Major design branches `[E]`

- Part III: robust control and high-order backstepping.
- Part IV: adaptive control and high-order backstepping.
- Part V: robust adaptive control.
- Part VI: disturbance attenuation and decoupling.
- Part VIII: optimal control and spacecraft attitude stabilization.
- Part IX: generalized PID control and model-reference tracking.
- Part X: discrete-time analogues.

For each, copy its uncertainty model, measurable signals, objective, and hypotheses before adopting the controller.

## H. User's switched SUB-FAS extension `[D]`

1. Open-loop subsystem data determine each $\mathcal F_i$.
2. $\mathcal F_{\mathrm{ext}}=\bigcup_i\mathcal F_i$ is determined by the subsystem family.
3. Subsystem controls and one state-dependent switching law determine the closed-loop switched system.
4. That fixed closed-loop system determines its extended ROEA.
5. Theorems characterize or inner-estimate that ROEA.

Label this switched extension `[D]` unless a precise Duan source is cited.


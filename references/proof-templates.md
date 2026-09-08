# Executable proof templates

## Required proof ledger

For every nontrivial proof, maintain a five-column ledger:

| Step | Formula/conclusion | Basis | Assumption used | Status |
|---|---|---|---|---|
| 1 | … | definition/equation/theorem | A1 | `[E]`, `[D]`, or `[U]` |

No assumption may remain unused. No proof step may cite “obvious” when an algebraic substitution, domain argument, or quantifier change is involved.

## Template A: global affine FAS control

1. State the model and dimensions.
2. State the domain $\mathcal D$.
3. Verify $B(X,t)$ is square and $\det B(X,t)\ne0$ for every $(X,t)\in\mathcal D\times\mathbb R_{\ge0}$.
4. Define $A_{0\sim n-1}$ and $v$.
5. Give the complete control law.
6. Substitute it into the plant line by line.
7. obtain the target high-order linear equation;
8. convert it to $\dot X=\Phi X+B_cv$ if a stability/response theorem is needed;
9. invoke the appropriate linear-system result;
10. translate the conclusion back to the original variables and domain.

Failure condition: if invertibility holds only on a proper subset, stop calling the model globally fully actuated and route to Template C.

## Template B: model conversion by elimination and order elevation

1. Write every original subsystem and declare dimensions.
2. Select the elementary state to retain.
3. Differentiate one order at a time.
4. At each differentiation, state the required differentiability.
5. Substitute intermediate variables using previously derived equations.
6. Record the recursive transformed terms, such as $\breve h_i$ and $\breve B_i$.
7. prove the coordinate/transformation formula is defined on its domain;
8. obtain the final HOFAS/sub-FAS equation;
9. prove forward equivalence: an original-system solution maps to a transformed-system solution;
10. prove reverse recovery: transformed variables determine the eliminated variables;
11. identify any points excluded by inversion or division.

Failure condition: a formal differentiated equation without reverse recovery is not yet an equivalent model.

## Template C: SUB-FAS substabilization and ROEA

1. Define $\mathcal S$ and $\mathcal F$ from the open-loop input matrix/map.
2. If using $\varphi$, prove its zero set represents the singular set claimed.
3. State the sub-FAS control law on $\mathcal F$ only.
4. Select $A_{0\sim n-1}$ with stable $\Phi(A_{0\sim n-1})$.
5. Substitute to obtain the constrained linear closed-loop system.
6. Define $X_0=x^{(0\sim n-1)}(0)$.
7. Derive

$$
X(t)=e^{\Phi(A_{0\sim n-1})t}X_0.
$$

8. Substitute $X(t)$ into the feasibility condition.
9. Quantify it for every $t\ge0$.
10. Define the ROEA from precisely those $X_0$ satisfying full-time feasibility.
11. Use stability of $\Phi$ to prove exponential convergence.
12. Conclude both: controller well-definedness and convergence.

Failure conditions:

- $X_0\in\mathcal F$ alone is insufficient;
- stable $\Phi$ alone is insufficient;
- a finite simulation horizon does not prove the all-time condition;
- a trajectory-defined ROEA need not have a closed-form boundary.

## Template D: complete parameterized design

1. Choose a target matrix $F$ with the desired eigenstructure.
2. Introduce free $Z$ with its exact dimension.
3. Construct

$$
V(Z,F)=\begin{bmatrix}Z^\top&(ZF)^\top&\cdots&(ZF^{m-1})^\top\end{bmatrix}^\top.
$$

4. Impose $\det V(Z,F)\ne0$.
5. Define $A_{0\sim m-1}=-ZF^mV^{-1}(Z,F)$.
6. Verify by block multiplication that $\Phi(A_{0\sim m-1})V=VF$.
7. infer $\Phi(A_{0\sim m-1})=VFV^{-1}$;
8. separate eigenstructure selected through $F$ from remaining freedom in $Z$;
9. state any secondary objective imposed on $Z$.

Failure condition: a numerical $Z$ with singular $V(Z,F)$ is inadmissible even if a simulation happens to run.

## Template E: uncertain/robust/adaptive branch

1. Split known and uncertain terms exactly as the source does.
2. List measurable signals and known bounds.
3. map each uncertainty assumption to the compensation term using it;
4. state the Lyapunov function and all positive-definiteness conditions;
5. compute its derivative without suppressing cross terms;
6. apply each inequality with its constants visible;
7. distinguish asymptotic, exponential, ultimate-bounded, practical, and finite-time conclusions;
8. show all closed-loop signals required by the theorem remain bounded;
9. verify the implemented controller uses no unavailable quantity.

## Template F: delay and predictor branch

1. Declare every delay and bound, and specify the initial-history interval.
2. State the existence/uniqueness assumption for the original delay system.
3. construct the predictor with the source's $Y$ and shifted $Z$ variables;
4. prove predictor equality on its declared horizon;
5. substitute predicted current/future variables into the delayed input channel;
6. derive the delay-compensated closed loop;
7. verify causality: the controller uses only available history and computed prediction;
8. carry feasibility conditions over the required delayed stack.

## Template G: output-feedback/OD-FAS branch

1. State exactly which outputs and derivatives are measured.
2. define the OD-FAS representation without introducing unavailable states into the controller;
3. derive any dynamic extension/observer equation;
4. prove its solution exists and its estimation/reconstruction error has the claimed property;
5. insert the available-information control law;
6. derive the joint plant–controller closed loop;
7. state whether the result is local/global and uniform/nonuniform.

## Template H: new switched SUB-FAS theorem `[D]`

1. Define every mode $i\in\mathcal M$ and its $\mathcal F_i$.
2. Define $\mathcal F_{\mathrm{ext}}=\bigcup_i\mathcal F_i$ independently of the switching law.
3. give each $\mu_i$ and one fixed state-dependent switching law $\kappa$;
4. specify memory, hysteresis, tie breaking, and initial mode;
5. prove each active control law is defined along flows;
6. prove switching preserves membership in $\mathcal F_{\mathrm{ext}}$;
7. prove existence and uniqueness of the hybrid/switched solution under stated regularity;
8. prove finite escape is excluded or give a continuation argument;
9. prove non-Zeno behavior on every finite interval;
10. derive convergence under the fixed closed loop $(\{\mu_i\},\kappa)$;
11. define its extended ROEA after the closed loop is fixed;
12. prove equality or inclusion claims with explicit quantifiers.

This template is not a Duan theorem. It is the user's research extension and must remain `[D]`.


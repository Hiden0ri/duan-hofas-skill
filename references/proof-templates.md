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

## Template H: switched SUB-FAS relative-margin theorem `[D]`

1. Declare index set $\mathcal P=\{1,2,\ldots,N\}$ and each subsystem (`the ith subsystem`) with piecewise continuous $f_i, B_i$; assume $x^{(0\sim n-1)}$ does not jump at switching instants.
2. Define $\mathcal S_{i,0}, \mathcal S_{i,\infty}, \mathcal S_i$, feasible set $\mathcal F_i=\mathbb R^{nr}\setminus\mathcal S_i$, and singularity functions $\varphi_{i,0}, \varphi_{i,\infty}, \varphi_i$ following Duan (2023) Definitions 5–6 `[E]`.
3. State Assumption 1 `[D]`: each $\varphi_i:\mathbb R^{nr}\to\mathbb R$ is fixed and continuous on $\mathbb R^{nr}$.
4. Define $\mathcal F_{\rm ext}=\bigcup_{i\in\mathcal P}\mathcal F_i=\{X:\max_{i\in\mathcal P}|\varphi_i(X)|>0\}$ and origin feasibility $\max_{i\in\mathcal P}|\varphi_i(0)|>0$.
5. Construct subsystem controller $u_i=-B_i^{-1}(x^{(0\sim n-1)})[A_{0\sim n-1}x^{(0\sim n-1)}+f_i(x^{(0\sim n-1)})]$ on $\mathcal F_i$ first, then substitute to obtain the common linear closed-loop equation $x^{(n)}+A_{0\sim n-1}x^{(0\sim n-1)}=0$.
6. Define the extended ROEA $\mathcal R_\kappa$ from the unique closed-loop response on $[0,\infty)$ under switching law $\kappa$ with initial value $X_0=x^{(0\sim n-1)}(0)$.
7. Construct holding/switching regions $\Omega_i, \widetilde\Omega_i$ using $|\varphi_i(X)|$ vs. $\gamma\max_{j\in\mathcal P}|\varphi_j(X)|$ ($\gamma\in(0,1)$), deterministic `min(argmax)` tie-breaking, and switching law $\kappa^*$.
8. Prove Lemma 1 (on $[0,T)$ with feasible limit at $T^-$: finitely many switches via uniform continuity on compact $K_T$ + unique continuation beyond $T$).
9. Prove Theorem 1 (active controller well-defined when $\sigma(t)=i$, common state-space response $e^{\Phi(A_{0\sim n-1})t}X_0$, common Lyapunov decay, origin neighborhood in $\mathcal R_{\kappa^*}$, and exact characterization $\mathcal R_{\kappa^*}=\{X_0:e^{\Phi(A_{0\sim n-1})t}X_0\in\mathcal F_{\rm ext},\ \forall t\ge0\}$).
10. Prove Proposition 1 (parameter-independent strict enlargement $X_0\in\mathcal R_{\kappa^*}\setminus\bigcup_{i\in\mathcal P}\mathcal R_i(A_{0\sim n-1})$ via Template I contradiction) and Corollary 1 (finite total switches on $[0,\infty)$ on compact $K_\infty$, excluding Zeno behavior).

This template is the user's switched extension and must remain labeled `[D]`.

## Template I: proof by contradiction (`Duan & Zhou 2022` Lemma 4.4 `[E]`)

1. Start directly with `"Suppose that [negation of conclusion]."` (never write `"We prove by contradiction"` or `"Suppose, on the contrary"`).
2. Deduce consequences using `"Then it follows from (x) that [display]."`
3. Construct the witnessing object deduced from the negation: `"Therefore, there exists … such that [display], which means that [Property A]."`
4. Establish the opposing fact: `"On the other side, [hypothesis / plant equation] implies that [not Property A]."`
5. Close with the exact three-sentence cadence: `"This yields a contradiction. Thus [original conclusion]. The proof is finished."`

## Template J: high-order backstepping (`Part III` §4; `2026 Volume I` §9.2 `[E]`)

1. **Preparations**: Select $A_i^{0\sim m_i-1}$ with $\operatorname{Re}\lambda_k(\Phi(A_i^{0\sim m_i-1}))\le -\mu/2$, solve $\Phi^\top P_i+P_i\Phi\le -\mu P_i$ for $P_i=[P_{iF}\ P_{iL}]$, define $\tilde P_i=\mathring{I}P_i$ and $\tilde P_i^{-1}=[Q_{i1}^\top\ Q_{i2}^\top]^\top$, and verify $Q_{iL}\ne 0$.
2. **`The First Step`**: Set $z_1^{(0\sim m_1-1)}=x_1^{(0\sim m_1-1)}$ and $\tilde P_2 z_2^{(0\sim m_2-1)}=x_2^{(0\sim m_2-1)}-[\alpha_1^\top\ 0]^\top$; design first virtual control $\alpha_1=-L_1^{-1}(A_1^{0\sim m_1-1}z_1^{(0\sim m_1-1)}+\alpha_1^*)$ to get $z_1^{(m_1)}+A_1^{0\sim m_1-1}z_1^{(0\sim m_1-1)}=\varphi_1+w_1$.
3. **`The Second / k-th Step`**: Differentiate $\alpha_{k-1}$ only $m_k-1$ times and split certain/uncertain parts ($h_{k-1}+\Delta h_{k-1}$); express $z_k^{(m_k)}$ via $\tilde P_k^{-1}$; introduce $\tilde P_{k+1}z_{k+1}^{(0\sim m_{k+1}-1)}$; design $\alpha_k$ including coupling cancellation $+v_{k-1}$ ($v_{k-1}=L_{k-1}^\top P_{k-1,L}z_{k-1}^{(0\sim m_{k-1}-1)}$) to obtain $z_k^{(m_k)}+A_k^{0\sim m_k-1}z_k^{(0\sim m_k-1)}=\varphi_k+w_k-v_{k-1}$.
4. **`The n-th Step`**: Design actual control law $u=-L_n^{-1}(A_n^{0\sim m_n-1}z_n^{(0\sim m_n-1)}+u^*)$ with $+v_{n-1}$, yielding $z_n^{(m_n)}+A_n^{0\sim m_n-1}z_n^{(0\sim m_n-1)}=\varphi_n-v_{n-1}$.
5. **`The Conclusion`**: Define $V=\sum_{i=1}^n (z_i^{(0\sim m_i-1)})^\top P_i z_i^{(0\sim m_i-1)}$, cancel cross terms via $(z_i)^\top P_{iL}w_i=(z_{i+1})^\top P_{i+1,L}v_i$ (`"Adding the equations in (...) side by side, and using (...), give \dot V\le -\mu V+n\varepsilon"`), and introduce the formal theorem with `"The above process clearly proves the following result."`

## Template K: sufficiency/necessity, multi-conclusion, and induction proofs `[E]`

- **Sufficiency & Necessity**: Label paragraphs `"Sufficiency: …"` and `"Necessity: …"`, closing with `"Combining the above two aspects gives the complete proof of the result."` `[E: Duan 2023 Proposition 2]`.
- **Multi-conclusion**: Prove in stated order (`"The first two conclusions are obvious. To show the third condition, …"`, `"The first conclusion is then proven."`, `"It remains to show that …"`).
- **Mathematical induction**: Open with `"We prove the theorem via the n-step induction. Step 1: …"` or `"We use mathematical induction to prove this result."` `[E: Volume I Ch. 7–8]`.

See [duan-writing-corpus.md](duan-writing-corpus.md) §7 for verbatim Duan proof passages.


# Duan theorem-writing template

## 1. Evidence and scope

Primary evidence: Guang-Ren Duan, *High-order fully actuated system approaches: Part III. Robust control and high-order backstepping* (2021), Theorem 3.5, pp. 958–959 `[E]`.

User knowledge source: Zotero note “Duan规范”, item 877, attached to the above Duan-first-author paper. The user's summary—“针对什么系统，满足什么假设，给定什么参数，使用什么控制律，如果满足什么条件，最终满足什么性能”—is retained as the operational reading guide `[E: user note]`.

## 2. Source-verified logical chain `[E]`

### 2.1 Identify the system and imported hypotheses

The theorem begins by identifying the exact numbered system and named premises:

> Suppose that system (2) satisfies Assumption A1 and Condition 1.

Logical role:

$$
\text{object of theorem}
+
\text{previously defined admissibility assumptions}.
$$

Do not replace the names by an untraceable phrase such as “under standard assumptions.”

### 2.2 Declare the freely selected design quantities

The theorem next introduces arbitrary positive scalars $\mu$ and $\epsilon$, followed by matrices $A_i\in\mathbb R^{r\times r}$, $i=0,1,\ldots,n-1$.

Logical role:

$$
\text{designer's freedom}
=
\{\mu,\epsilon,A_0,\ldots,A_{n-1}\}.
$$

Dimensions and quantifiers belong here; they must not be postponed until the proof.

### 2.3 State admissibility conditions on the design quantities

The matrices are required to satisfy the previously numbered condition (9). Thus “arbitrarily chosen design quantity” and “admissible design quantity” are not conflated:

$$
A_{0\sim n-1}\in\mathcal A_{\mathrm{adm}}.
$$

### 2.4 Give the complete control law

The theorem then states the control law and defines $u^*$ and $u_0(x^*)$ before making the performance claim. This ordering makes the controller reproducible from the theorem statement itself.

The form captured in the user's note is

$$
u=-L^{-1}\!\left(x^{(0\sim n-1)}\right)
\left(
A^{0\sim n-1}x^{(0\sim n-1)}+u^*
\right),
$$

$$
\begin{aligned}
u^*={}&
\frac{1}{4\epsilon}
\rho^2\!\left(x^{(0\sim n-1)}\right)
P_L^\top\!\left(A^{0\sim n-1}\right)
x^{(0\sim n-1)}\\
&+f\!\left(x^{(0\sim n-1)}\right)-u_0(x^*),
\end{aligned}
$$

where

$$
\begin{aligned}
u_0(x^*)={}&(x^*)^{(n)}
-A^{0\sim n-1}(x^*)^{(0\sim n-1)}\\
&-\frac{1}{4\epsilon}
\rho^2\!\left(x^{(0\sim n-1)}\right)
P_L^\top\!\left(A^{0\sim n-1}\right)
(x^*)^{(0\sim n-1)}.
\end{aligned}
$$

When transcribing the source, retain its exact $L$, $A^{0\sim n-1}$, $P_L^\top$, $\rho$, $\mu$, and $\epsilon$ notation. Do not normalize superscripts/subscripts from memory.

### 2.5 State the guaranteed performance explicitly

The conclusion does not end with a vague “the system is stable.” It identifies the converging state stack, the global character of convergence, the center of the target region, and the target set itself:

$$
\Theta_{\mu,\epsilon}\!\left((x^*)^{(0\sim n-1)}\right)
=
\left\{
x^{(0\sim n-1)}:
(x-x^*)^{(0\sim n-1)\top}
P
(x-x^*)^{(0\sim n-1)}
\le \frac{\epsilon}{\mu}
\right\}.
$$

## 3. Reusable drafting form `[D]`

Use the following only after replacing every placeholder with a source-defined object:

> **Theorem.** Suppose that system (...) satisfies Assumptions (...) and Conditions (...). Let (...) be arbitrarily given parameters, and let (...) be matrices/functions of the stated dimensions satisfying (...). Then the following control law (...) guarantees that (...), for every admissible initial condition, has the performance (...), where the performance set/bound is (...).

The corresponding recurring language roles are:

| Source-style connector | Function in the theorem |
|---|---|
| `Suppose that ... satisfies ...` | system and hypotheses |
| `Let ... be arbitrarily given ...` | free design parameters |
| `let ... be a set of ... satisfying ...` | constrained design objects |
| `Then, the following control law ...` | controller declaration |
| `where ...` | immediate auxiliary definitions |
| `guarantees that ...` | exact performance conclusion |

Preserve the logical roles, but adapt capitalization and punctuation to the target journal instead of copying surface wording mechanically.

The corresponding proof should follow:

$$
\text{substitute the control law}
\to
\text{derive the closed-loop equation}
\to
\text{apply each named condition at its use-site}
\to
\text{derive the performance inequality}
\to
\text{identify the stated set or convergence property}.
$$

## 4. Audit questions

1. Which numbered system is governed by the theorem?
2. Which assumptions concern the plant, uncertainty, domain, or solution existence?
3. Which quantities are given by the designer, and which are plant data?
4. What admissibility condition restricts each design quantity?
5. Is the complete control law present, including auxiliary terms?
6. Can direct substitution reproduce the claimed closed-loop equation with the printed signs?
7. Does the conclusion state the exact state/output, convergence type, domain, and performance set?
8. Is every symbol in the conclusion defined before use?

## 5. Common failures

- stating “choose suitable matrices” without dimensions or the numbered condition;
- placing a necessary assumption only inside the proof;
- giving a controller but omitting an auxiliary signal used in it;
- claiming stability when the theorem proves convergence to a nonzero set;
- omitting “global,” “local,” “uniform,” “exponential,” or “ultimate” when it changes the result;
- changing a sign while converting between two auxiliary-control decompositions;
- treating the theorem-writing order as evidence that an unrelated theorem is true.

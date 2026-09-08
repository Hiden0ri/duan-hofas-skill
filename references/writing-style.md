# Duan-style technical writing guide

## Reusable organization

Duan's foundational papers typically proceed as follows:

1. motivate why state-space treatment obscures direct solution of the control vector;
2. define the FAS/HOFAS model and classify full actuation;
3. derive the model physically or by variable elimination;
4. present a control law producing a selected constant linear closed-loop system;
5. expose parameterized design freedom and additional performance uses;
6. organize theorem, proof, remarks, and examples;
7. verify the procedure on a concrete dynamical system.

## Terminology discipline

- Follow [concepts-and-notation.md](concepts-and-notation.md).
- In Chinese, prefer “$\Phi(A_{0\sim n-1})$ 稳定”; add “其全部特征值具有负实部” when needed.
- Call $e^{\Phi t}X_0$ “闭环系统的状态响应”.
- Call the explicit formula a “控制律”, not an invented “反演控制器”.

## Theorem drafting template

Use the source-verified chain distilled from Duan's Theorem 3.5:

1. **System:** “Suppose that system (...) ...” identifies the exact model.
2. **Named assumptions:** “satisfies Assumption ... and Condition ...” imports only previously defined hypotheses.
3. **Given parameters:** introduce arbitrary positive scalars and matrix parameters with dimensions.
4. **Design conditions:** state the numbered equation, inequality, rank, or stability condition those parameters satisfy.
5. **Control law:** introduce the complete law with “Then, the following control law ...”; define every auxiliary term immediately after it.
6. **Guaranteed performance:** use “guarantees that ...” and give the terminal set, convergence property, tracking claim, or robustness bound explicitly.
7. **Proof:** substitute first; invoke stability only after establishing the closed-loop equation.

For the exact source example, drafting checklist, and anti-patterns, read [theorem-writing-template.md](theorem-writing-template.md).

## TAC/Automatica adaptation

Do not imitate rhetoric mechanically:

- state one precise problem and a short contribution chain;
- identify which Duan theorem is reused and the new obstruction;
- separate `[E]` citations from `[D]` claims;
- compare assumptions, controller, domain, and conclusion;
- avoid “obviously”, “clearly”, “easy”, and broad superiority claims unless demonstrated;
- do not call a renamed definition a contribution;
- state limitations such as singular contact, input constraints, non-Zeno switching, and robustness.

## Invalid patterns

- “The method solves all nonlinear systems.”
- “Global stability follows from the stable linear closed loop” for a sub-FAS.
- “Control design enlarges the feasible set” when open-loop $B(\cdot)$ is fixed.
- “Duan proved …” without a source locator.

## Citation pattern

> Duan's Part I shows that, for the affine global FAS under its full-actuation condition, the stated control law produces a constant linear closed-loop system [E, Part I, Proposition 2.2].

If the locator is not checked:

> The overview attributes this conversion result to the early FAS series [E; exact theorem locator U].

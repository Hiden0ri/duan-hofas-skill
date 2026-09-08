# Duan HOFAS concepts and notation

`[E]` means verified from a primary source in the catalog. Recheck source-specific equation numbers before publication because numbering differs between the English series, Chinese papers, overview, and 2026 book.

## Canonical terms

| Chinese | English | Avoid |
|---|---|---|
| 高阶系统方法 | high-order system approach | 高阶状态方法 |
| 高阶全驱系统 | high-order fully actuated system (HOFA/HOFAS) | 高阶完全驱动系统 |
| 全驱系统方法 | fully actuated system approach (FAS approach) | 全驱动方法 |
| 亚全驱系统 | sub-fully actuated system (sub-FAS) | 子全驱系统 |
| 大范围全驱系统（简称全驱系统） | (global) fully actuated system | 未经说明的“全局全驱” |
| 标准全驱系统 | standard fully actuated system | — |
| 基础状态向量 | elementary state vector | 广义状态（指 $x$ 时） |
| 控制律 | control law | FAS 反演控制器 |
| 线性定常闭环系统 | linear time-invariant closed-loop system | Hurwitz 线性闭环流 |
| 奇异集 / 可行集 | singular set / feasible set | 失效集 / 有效域 |
| 亚稳定性 / 亚镇定 | substability / substabilization | 子稳定 / 协同镇定 |
| 指数吸引域 | region of exponential attraction (ROEA) | 未经区分的指数收敛域 |
| 有理亚全驱系统 | rational sub-FAS | 自造译名 |
| 临界有理亚全驱系统 | critically rational sub-FAS `[U: verify exact English]` | 自造译名 |
| 无理亚全驱系统 | irrational sub-FAS `[U: verify exact English]` | 自造译名 |
| 消元升阶 | variable elimination and order elevation | 高阶提升 |
| 增元降阶、变量增广 | variable extension and order reduction | 状态提升 |

## Basic stacked notation `[E]`

For $x\in\mathbb R^r$,

$$
x^{(0\sim n)}
=
\begin{bmatrix}
x^\top&\dot x^\top&\cdots&(x^{(n)})^\top
\end{bmatrix}^\top.
$$

For parameter matrices,

$$
A_{0\sim n}
=
\begin{bmatrix}
A_0&A_1&\cdots&A_n
\end{bmatrix}.
$$

The associated block companion matrix is

$$
\Phi(A_{0\sim n})
=
\begin{bmatrix}
0&I&\cdots&0\\
\vdots&\vdots&&\vdots\\
0&0&\cdots&I\\
-A_0&-A_1&\cdots&-A_n
\end{bmatrix}.
$$

When the source uses $A_{0\sim n-1}$, the final block is $-A_{n-1}$. Do not mix index ranges.

## Single-order affine FAS `[E]`

$$
x^{(n)}
=
f\!\left(x^{(0\sim n-1)},t\right)
+B\!\left(x^{(0\sim n-1)},t\right)u,
$$

where $x,u\in\mathbb R^r$ and $B(\cdot)\in\mathbb R^{r\times r}$. It is globally fully actuated when $B(\cdot)$ is nonsingular on the whole stated domain. It is a sub-FAS when singular points exist and the feasible set is nonempty. The standard FAS has $B(\cdot)\equiv I_r$.

## Nonaffine FAS `[E]`

$$
Ex^{(n)}
=
f\!\left(x^{(0\sim n-1)},\zeta\right)
+g\!\left(x^{(0\sim n-1)},\zeta,u\right).
$$

Full actuation is formulated through the map from $u$ to $w=g(\cdot,u)$ being a differential homeomorphism on the stated domain. Do not replace this by $\det B\ne0$ because a matrix $B$ need not exist.

## Multi-order affine FAS `[E]`

For $k=1,\ldots,\eta$, let $x_k\in\mathbb R^{r_k}$ have order $\mu_k$ and $\sum_{k=1}^{\eta}r_k=r$:

$$
\left.x_k^{(\mu_k)}\right\rvert_{k=1\sim\eta}
=
f\!\left(\left.x_k^{(0\sim\mu_k-1)}\right\rvert_{k=1\sim\eta},t\right)
+B(\cdot)u.
$$

Keep Duan's vertical-bar indexing when reproducing multi-order statements.

## Singular and feasible sets `[E]`

Let $X\in\mathbb R^\kappa$ denote a value of the derivatives entering $B$:

$$
\mathcal S
=
\{X:\det B(X,t)=0\ \text{or}\ \infty,\ t\ge0\},
$$

$$
\mathcal F
=
\mathbb R^\kappa\setminus\mathcal S.
$$

The normal and abnormal parts are

$$
\mathcal S_0=\{X:\det B(X,t)=0\},
\qquad
\mathcal S_\infty=\{X:\det B(X,t)=\infty\}.
$$

A sub-FAS may be 0-type, $\infty$-type, or mixed-type. If a study restricts itself to the 0-type case, state this before using continuity or closed-set arguments.

The Chinese sub-strict-feedback paper further classifies a sub-FAS by the relation between the origin and $\mathcal F$: rational when the feasible set contains the origin, critically rational when the origin is a boundary point, and irrational when the origin is an exterior point. Recheck the corresponding English names before writing an English manuscript.

## Transformed sub-strict-feedback notation `[E]`

The Chinese paper uses breve-marked quantities for the transformed HOFAS:

$$
x^{(n)}
=
\breve h_n\!\left(x^{(0\sim n-1)},t\right)
+\breve B_n\!\left(x^{(0\sim n-1)},t\right)u.
$$

The breve is meaningful: $\breve h_n$ and $\breve B_n$ are recursively obtained after model transformation. Do not silently replace them by the original strict-feedback functions $f_i$ and $G_i$.

## Substability, substabilization, and ROEA `[E]`

For selected $A_{0\sim n-1}$, the designed closed loop is

$$
x^{(n)}+A_{0\sim n-1}x^{(0\sim n-1)}=0.
$$

Its state-space representation and response are

$$
\dot x^{(0\sim n-1)}
=
\Phi(A_{0\sim n-1})x^{(0\sim n-1)},
$$

$$
x^{(0\sim n-1)}(t)
=
e^{\Phi(A_{0\sim n-1})t}X_0,
\qquad X_0=x^{(0\sim n-1)}(0).
$$

The ROEA is the set of initial values for which this response remains in $\mathcal F$ for all $t\ge0$ and converges exponentially to the origin. Use the exact paper definition when delays or multi-order states are present.

## User-project extensions

“扩展可行集”, “扩展 ROEA”, “最大裕量切换律”, and “切换亚全驱系统的指数吸引域” are research extensions `[D]`. Do not present them as Duan's definitions.

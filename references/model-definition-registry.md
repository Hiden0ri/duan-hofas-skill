# Duan 原始模型变量与条件表

## 1. 使用原则

本文件用于检查 HOFAS/FAS/SUB-FAS 原始系统中的变量定义、维数和约束条件。`[E]` 表示已由所列 Duan 原文核对。

不存在适用于 Duan 全部论文的单一 $f$、$B$ 条件。必须先确定模型分支和控制目标，再采用对应原文的条件。“原文条件”与为解存在唯一等目的所加的严谨性增强必须分开；后者不得归于 Duan。

## 2. 名义单阶仿射全驱系统

*High-order fully actuated system approaches: Part III. Robust control and high-order backstepping* 第 2.1 节式 (1) 给出 `[E]`

$$
x^{(n)}=f\bigl(x^{(0\sim n-1)}\bigr)+L\bigl(x^{(0\sim n-1)}\bigr)u.
$$

其中 `[E]`

$$
x,u\in\mathbb R^r,
\qquad
f\bigl(x^{(0\sim n-1)}\bigr)\in\mathbb R^r,
\qquad
L\bigl(x^{(0\sim n-1)}\bigr)\in\mathbb R^{r\times r}.
$$

$f$ 是连续向量函数，$L$ 是连续矩阵函数；Assumption A1 为 `[E]`

$$
\det L\bigl(x^{(0\sim n-1)}\bigr)\ne0,
\quad
\forall x^{(j)}\in\mathbb R^r,
\quad j=0,1,\ldots,n-1.
$$

| 符号 | 含义 | 维数或条件 |
|---|---|---|
| $n$ | 微分阶数 | 正整数 |
| $x$ | 状态向量 | $\mathbb R^r$ |
| $u$ | 控制输入向量 | $\mathbb R^r$ |
| $f$ | 非线性向量函数 | $\mathbb R^r$，连续 |
| $L$ | 控制系数矩阵函数 | $\mathbb R^{r\times r}$，连续且全局非奇异 |

全局非奇异性保证控制变换 $\widetilde u=L(\cdot)u$ 在整个状态空间有定义。它是对输入通道的全驱性要求，不是对 $f$ 的要求。

## 3. 含外部变量、时间与不确定项的单阶模型

*Part VI. Disturbance attenuation and decoupling* 第 2 节式 (1) 写为 `[E]`

$$
\begin{aligned}
x^{(n)}={}&f\bigl(x^{(0\sim n-1)},\zeta,t\bigr)
+\Delta f\bigl(x^{(0\sim n-1)},\zeta,t\bigr)\\
&+B\bigl(x^{(0\sim n-1)},\zeta,t\bigr)u.
\end{aligned}
$$

原文规定 `[E]`

$$
x,u\in\mathbb R^r,
\qquad \zeta\in\mathbb R^p,
$$

$$
f(\cdot),\Delta f(\cdot)\in\mathbb R^r,
\qquad B(\cdot)\in\mathbb R^{r\times r}.
$$

$\zeta$ 可表示参数向量、外部变量、时滞状态或未建模动态状态等；$f$ 是已知的充分光滑向量函数，$\Delta f$ 是未知项，$B$ 是充分光滑矩阵函数。Assumption A1 要求 `[E]`

$$
\det B\bigl(x^{(0\sim n-1)},\zeta,t\bigr)\ne0
$$

对任意 $\zeta\in\mathbb R^p$ 及任意 $x^{(j)}\in\mathbb R^r$，$j=0,1,\ldots,n-1$ 成立。

这里的“充分光滑”服务于后续变量变换、求导和扰动衰减或解耦推导。若原文未给固定的 $C^k$ 阶数，就不能擅自补成某个统一阶数；应根据实际证明中最高阶求导逐项核查。

## 4. 多阶仿射全驱系统

*Part VIII. Optimal control with application in spacecraft attitude stabilisation* 第 2 节式 (1) 可压缩写为 `[E]`

$$
\left.x_k^{(\mu_k)}\right\rvert_{k=1\sim\eta}
=f\left(\left.x_k^{(0\sim\mu_k-1)}\right\rvert_{k=1\sim\eta},\zeta,t\right)+B(\cdot)u.
$$

其中 `[E]`

$$
x_k\in\mathbb R^{r_k},
\quad f_k(\cdot)\in\mathbb R^{r_k},
\quad k=1,2,\ldots,\eta,
$$

$$
u\in\mathbb R^r,
\quad \zeta\in\mathbb R^p,
\quad \sum_{k=1}^{\eta}r_k=r,
\quad B(\cdot)\in\mathbb R^{r\times r}.
$$

$\mu_k$ 是各子状态的微分阶数，原文在此处取为一组互不相同的整数。记 `[E]`

$$
\kappa=\sum_{k=1}^{\eta}r_k\mu_k,
$$

则

$$
\left.x_k^{(0\sim\mu_k-1)}\right\rvert_{k=1\sim\eta}\in\mathbb R^\kappa.
$$

该文称 $f_k$ 为非线性向量函数，称 $B$ 为充分光滑矩阵函数，并要求 `[E]`

$$
\det B\left(\left.x_k^{(0\sim\mu_k-1)}\right\rvert_{k=1\sim\eta},\zeta,t\right)
\ne0\ \text{or}\ \infty
$$

对所有相应状态、$\zeta$ 和 $t>0$ 成立。原文的“$\ne0$ or $\infty$”意为行列式既不为零也不为无穷；引用时不能误读成“非零或者等于无穷”。

若研究输出或最优控制，系统之后还定义 `[E]`

$$
y=C\left.x_k^{(0\sim\mu_k-1)}\right\rvert_{k=1\sim\eta},
\qquad C\in\mathbb R^{m\times\kappa}.
$$

$C$、可观测性与 Riccati 方程等是控制目标附加结构，不属于基础多阶 FAS 定义。

## 5. SUB-FAS

在 *Substability and Substabilization: Control of Subfully Actuated Systems* 中，$f_k$ 是分段连续非线性向量函数，$B(\cdot)\in\mathbb R^{r\times r}$ 是关于相应状态和时间的分段连续矩阵函数 `[E]`。该文允许 $B$ 有奇异点，并定义 `[E]`

$$
\mathcal S=\mathcal S_0\cup\mathcal S_\infty,
$$

$$
\mathcal S_0=\{X:\det B(X,t)=0,\ X\in\mathbb R^m,\ t\ge0\},
$$

$$
\mathcal S_\infty=\{X:\det B(X,t)=\infty,\ X\in\mathbb R^m,\ t\ge0\},
$$

$$
\mathcal F=\mathbb R^m\setminus\mathcal S.
$$

$X$ 不一定等于完整状态堆叠。原文利用结构分布矩阵提取真正影响 $B$ 的变量，故 $m$ 可小于完整堆叠的维数。必须先定义本论文的 $X$，再定义 $\mathcal S$ 和 $\mathcal F$。

SUB-FAS 应满足：$\mathcal F\ne\varnothing$；$B^{-1}(X,t)$ 只在 $X\in\mathcal F$ 时有定义；镇定结论还须证明相应闭环轨迹全过程留在 $\mathcal F$。若把 $\det B\ne0$ 重新假设为在整个 $\mathbb R^m$ 成立，研究对象就变回全局 FAS。

## 6. 状态时滞模型

*Fully actuated system approaches for continuous-time delay systems: Part 1. Systems with state delays* 第 3.1.1 节式 (26) 给出 `[E]`

$$
\begin{aligned}
x^{(n)}(t)={}&f\left(\left.x^{(0\sim n-1)}(t-\tau_j(t))\right\rvert_{j=1\sim\zeta},t\right)\\
&+B\left(\left.x^{(0\sim n-1)}(t-\sigma_j(t))\right\rvert_{j=1\sim\gamma},t\right)u(t).
\end{aligned}
$$

其中 $x,u\in\mathbb R^r$；$\tau_j(t)$ 与 $\sigma_j(t)$ 是两组非负标量时滞函数；$f(\cdot,t)\in\mathbb R^r$；$B(\cdot,t)\in\mathbb R^{r\times r}$ `[E]`。全局模型要求 `[E]`

$$
\det B(X,t)\ne0\ \text{or}\ \infty,
\quad \forall X\in\mathbb R^{\gamma nr},
\quad t>0.
$$

此处 $f$ 与 $B$ 依赖两组不同的时滞状态，不能因都简写成“$(\cdot)$”就认为自变量完全相同。输入时滞或预测器设计还需初始历史、时滞范围和预测系统解存在唯一等附加条件；这些不是无时滞 FAS 的通用条件。

## 7. 按控制目标区分 $f$ 与 $B$ 的要求

| 控制目标 | $f$ 或未知项 | $B$ 或输入通道 | 代表性原文 |
|---|---|---|---|
| 名义反馈配置或镇定 | 单阶基准模型中 $f$ 连续 | $L$ 连续且全局非奇异 | Part III，第 2.1 节式 (1)、A1 |
| 鲁棒控制 | 将 $\Delta f$ 与已知 $f$ 分开；存在非负连续 $\rho$，使 $\lVert\Delta f\rVert\le\rho$ | 输入矩阵保持全局非奇异 | Part III，式 (2)、Condition 1 |
| 自适应控制 | 参数项写成 $H^\top(x^{(0\sim n-1)})\theta$；$q$、$H$ 充分光滑；相应模型中 $\theta$ 为未知常向量 | $L$ 充分光滑且全局非奇异 | Part IV，第 2.1 节式 (1)、A1 |
| 鲁棒自适应控制 | $f$、$H$、$L$ 连续；$\Delta f$ 有连续上界；时变参数及其导数相对预估计满足给定界 | $L$ 连续且全局非奇异 | Part V，第 2 节式 (3)、A1–A3 |
| 扰动衰减或解耦 | 已知 $f$ 充分光滑；未知项、外部变量和动态扰动分别建模 | $B$ 充分光滑、全局非奇异；再附加输出或增广系统条件 | Part VI，第 2 节式 (1)、A1 |
| 最优控制或输出反馈 | 先定义基础 $f_k$；再按目标加入输出、性能指标、可观测性或 Riccati 条件 | $B$ 充分光滑且全局非奇异 | Part VIII，第 2–3 节 |
| 广义 PID 或模型参考跟踪 | $f_k$ 为非线性向量函数；另定义参考信号及其所需导数 | $B$ 为方阵并满足全驱性条件 | Part IX，第 2.1–2.2 节 |
| SUB-FAS 亚镇定与 ROEA | 相应模型中 $f_k$、$B$ 分段连续；允许奇异集存在 | 仅在可行集内可逆；同时验证轨迹可行性与收敛性 | *Substability and Substabilization*；ROEA 论文 |
| 状态时滞控制 | $f$ 依赖由 $\tau_j$ 确定的时滞状态 | $B$ 可依赖由 $\sigma_j$ 确定的另一组时滞状态 | Delay systems Part 1，第 3.1.1 节 |

## 8. 论文检查清单

1. 系统是单阶或多阶、连续或离散、仿射或非仿射、全局 FAS 或 SUB-FAS？
2. $n$、$\mu_k$、$x$、$x_k$、$u$、$\zeta$ 的含义和空间是否齐全？
3. $f$、$f_k$、$B$ 的值域与全部自变量是否明确？哪些量已知，哪些量不确定？
4. 原文要求连续、分段连续还是充分光滑？证明具体在哪一步使用？
5. $B$ 是否为方阵？行列式条件在全空间还是仅在可行集成立？
6. $\Delta f$、参数、扰动、时滞、输出或约束是否分别定义了维数和条件？
7. 对 SUB-FAS，影响 $B$ 的变量 $X$、奇异集、可行集和全过程可行性是否齐全？

## 9. 已核对来源

- Duan, *Part III. Robust control and high-order backstepping*, Section 2.1, equations (1)–(2), Assumption A1, Condition 1.
- Duan, *Part IV. Adaptive control and high-order backstepping*, Section 2.1, equation (1), Assumption A1.
- Duan, *Part V. Robust adaptive control*, Section 2, equation (3), Assumptions A1–A3.
- Duan, *Part VI. Disturbance attenuation and decoupling*, Section 2, equation (1), Assumption A1.
- Duan, *Part VIII. Optimal control with application in spacecraft attitude stabilisation*, Section 2, equations (1)–(6), Assumption A1.
- Duan, *Part IX. Generalised PID control and model reference tracking*, Sections 2.1–2.2, equations (1)–(4), Assumption A1.
- Duan, *Substability and Substabilization: Control of Subfully Actuated Systems*, Section II, equations (2)–(3), Definitions 2–6.
- Duan, *Fully actuated system approaches for continuous-time delay systems: Part 1. Systems with state delays*, Section 3.1.1, equations (26)–(31), Assumption A1.
- Duan and Wang, *Characterization of Region of Exponential Attraction for Substabilization of FASs*, Section 3, equations (14)–(16).

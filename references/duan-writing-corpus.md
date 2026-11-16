# Duan 原文写作语料库与环境/证明结构模板

本文件从段广仁（Guang-Ren Duan）第一作者英文论文与 2026 年专著 *Fully Actuated System Approach, Volume I: Global Fully Actuated Systems* 中提取**逐字核对的原句（`[E]`）**与**固定结构模板**。使用 `duan-hofas` 撰写或润色 HOFAS / sub-FAS 稿件时，**优先沿用本语料库中的原句搭配与段落骨架**，避免改写为生造名词或防御性否定句。

---

## 1. 文章宏观结构与各节首尾句式 `[E]`

### 1.1 Abstract 五段式结构
1. **研究背景或已有局限**（1 句）
2. **本文研究对象、核心概念或模型类**（1–2 句）
3. **控制器/切换律构造与闭环转化机制**（1–2 句）
4. **核心理论性质**（收敛性、ROEA 精确刻画或有限约束约化，1–2 句）
5. **算例与仿真验证**（1 句）

**原句示例 `[E: Duan 2023 TCYB, Abstract]`：**
- `"In this article, the concept of substability is proposed, which allows 'gaps' and 'holes' in the region of attraction of the Lyapunov exponential stability, and also allows the origin to be a boundary point of the region of attraction."`
- `"Specifically, the singular set of a sub-FAS is first defined, and a substabilizing controller is then designed such that the closed-loop system is a constant linear one with an arbitrarily assignable eigen-polynomial, but with its initial values restricted within a so-called region of exponential attraction (ROEA)."`
- `"Consequently, the substabilizing controller drives all the state trajectories starting from the ROEA exponentially to the origin."`
- `"Several examples are given to demonstrate the proposed theories."`

**原句示例 `[E: Duan & Wang 2026 FASTA, Abstract]`：**
- `"This paper addresses the explicit characterization of the region of exponential attraction (RoEA) for sub-fully actuated systems (sub-FASs)."`
- `"This transformation provides an exact finite-dimensional representation of the RoEA, converting the original infinite-horizon characterization problem into a tractable finite constraint description."`
- `"Numerical examples, including a pendulum system and a Lorenz system, demonstrate that the proposed method accurately captures practically meaningful attraction regions..."`

### 1.2 Introduction 五步推进与常用衔接句
对于约 8 页的 IEEE Transactions 论文，引言默认控制在 **1.5 页左右**，依次包含：问题背景与状态空间瓶颈 $\to$ HOFAS/sub-FAS 文献脉络与精确缺口 $\to$ 本文核心思路 $\to$ 贡献列表 $\to$ 章节安排 $\to$ 斜体 `Notations:` 段。

- **指出状态空间或现有方法局限 `[E: Duan 2023 TCYB / 2025 UC-FAS Part III]`：**
  - `"In spite of the fact that numerous dynamical systems can be converted into FASs and their control can be more effectively solved by the FAS approach, there are still systems which cannot be converted into a single FAS or sub-FAS."` `[E: UC-FAS Part III, §1]`
  - `"More specifically, for nonlinear systems which are not completely controllable (or not globally feedback linearizable in the state-space representation), a sub-FAS model of such a system is often obtained, which defines, when designing the controller of the system using the FAS approach, a singular set on which the controller is not well defined. This naturally leads to a problem of substabilization of the system."` `[E: Duan 2023 TCYB, §I]`
- **概括主要贡献（接 `enumerate` 列表）：**
  - `"The main results of this paper are summarized as follows."`
  - `"The main contributions of this work are summarized in the following aspects."`
- **章节安排（Organization）原句 `[E]`：**
  - `"This article is divided into seven sections. Section II provides ... Section III introduces ..., while Sections IV and V consider ..., respectively. A complicated example is further treated in Section VI, followed by some concluding remarks in Section VII."` `[E: Duan 2023 TCYB, §I]`
  - `"The remainder of this paper is organized as follows. Section II introduces ... Section III presents ... The main theoretical results are established in Section V. Section VI gives numerical examples, and Section VII concludes the paper."` `[E/D: IEEE Transactions 标准组织句]`

### 1.3 Conclusion / Concluding Remarks 结构 `[E]`
先回顾所提概念/控制律如何将受约束或非线性控制问题转化为常系数线性闭环与初值集合刻画，再点明算例验证，最后如实说明尚未覆盖的边界条件（如模型误差、输入限幅、公共奇异点）。
- `" substabilizing controllers can be designed for sub-FASs such that the closed-loop system becomes a constant linear one subject to a state constraint determined by the singular set. Eventually, using the solutions of linear systems, the state constraint is converted into a constraint on the system initial values, and this finally gives the ROEA."` `[E: Duan 2023 TCYB, §VII]`

---

## 2. `Notations:` 段落与系统模型变量交代 `[E]`

### 2.1 引言末尾 `Notations:` 规范与原句
**铁律**：只放全文通用约定；使用 `=` 和显式分块矩阵，**严禁编号**（用 `equation*`），**严禁用 `:=`、`\operatorname{col}` 或 `\col`**；局部对象（可行集、裕度、切换律、ROEA）一律留到正文模型出现之后再定义；注意阶次下标与子系统下标不撞车（若正文 $i\in\mathcal P$ 表子系统，则 `Notations:` 与正文中参数矩阵统一用 $A_j, j=0,1,\ldots,n-1$）。

**原句模板 `[E: Duan 2023 TCYB §I; Duan 2025 UC-FAS Part I §2]`：**
```latex
\emph{Notations:} For simplicity, the argument \(t\) of a time-dependent
variable is omitted when no confusion arises. For positive integers \(p\) and
\(q\), \(\mathbb{R}^p\) and \(\mathbb{R}^{p\times q}\) denote the
\(p\)-dimensional real vector space and the set of all \(p\times q\) real
matrices, respectively. The symbols \(I_p\) and \(0_{p\times q}\) denote the
identity and zero matrices of the indicated dimensions, \(\emptyset\) denotes
the null set, and \(\Omega\setminus\Gamma\) represents the complement of the
set \(\Gamma\) in \(\Omega\). For \(x\in\mathbb{R}^r\), \(x^{(j)}\) denotes its
\(j\)th derivative, and
\begin{equation*}
    x^{(0\sim n-1)}
    =\begin{bmatrix}
        x^{\mathrm{T}} & \dot x^{\mathrm{T}} & \cdots & \bigl(x^{(n-1)}\bigr)^{\mathrm{T}}
    \end{bmatrix}^{\mathrm{T}}\in\mathbb{R}^{nr}.
\end{equation*}
For matrices \(A_j\in\mathbb{R}^{r\times r}\), \(j=0,1,\ldots,n-1\), define
\begin{equation*}
    A_{0\sim n-1}=[\,A_0\ A_1\ \cdots\ A_{n-1}\,]
\end{equation*}
and
\begin{equation*}
    \Phi(A_{0\sim n-1})
    =\begin{bmatrix}
        0_{r\times r}&I_r&\cdots&0_{r\times r}\\
        0_{r\times r}&0_{r\times r}&\ddots&\vdots\\
        \vdots&\vdots&\ddots&I_r\\
        -A_0&-A_1&\cdots&-A_{n-1}
    \end{bmatrix}.
\end{equation*}
```

### 2.2 模型引出与函数正则性交代原句 `[E]`
直接仿照段广仁原文在系统方程后紧接 `where ...` 交代阶次、状态维数、输入维数与 $f,B$ 的性质，无需生硬添加 `"As in Duan..."`（除非引用特定定理或定义）：
- **单阶 sub-FAS / 约束 FAS `[E: Duan 2025 UC-FAS Part I §3.1; Duan & Wang 2026 §3.1]`：**
  > `"where n >= 1 is an integer, x \in \mathbb{R}^r and u \in \mathbb{R}^r are the state vector and the system input vector, respectively, f(x^{(0\sim n-1)}, t) \in \mathbb{R}^r is a piecewise continuous vector function, and B(x^{(0\sim n-1)}, t) \in \mathbb{R}^{r\times r} is a piecewise continuous matrix function."`
- **多阶 sub-FAS `[E: Duan 2023 TCYB §III-A; Underactuated 2024 §2.2]`：**
  > `"where \mu_k, k = 1, 2, \ldots, \eta, are a set of positive integers; x_k \in \mathbb{R}^{r_k}, k = 1, 2, \ldots, \eta, are the state vectors, with r_k satisfying r_1 + r_2 + \cdots + r_\eta = r; f_k(\cdot, t) \in \mathbb{R}^{r_k} are piecewise continuous nonlinear vector functions, and B(\cdot, t) \in \mathbb{R}^{r\times r} is a piecewise continuous matrix function."`
- **切换单阶仿射 sub-FAS `[D: 对齐 Duan + Yang–Duan 2026]`：**
  > `"Consider a continuous-time autonomous single-order affine switched sub-FAS described by the following equation: [eq], where n \geq 1 is an integer and x \in \mathbb{R}^r denotes the system state. The switching signal \sigma(t) is a piecewise constant and right-continuous function, whose value is chosen from an index set \mathcal{P}:=\{1,2,\ldots,N\}. The positive integer N denotes the total number of subsystems. The vector u_{\sigma(t)}(t)\in\mathbb{R}^r is the control input, and f_i(\cdot)\in\mathbb{R}^r and B_i(\cdot)\in\mathbb{R}^{r\times r}, i\in\mathcal{P}, are piecewise continuous vector and matrix functions of the ith subsystem, respectively. The switching sequence is denoted as \{t_0,t_1,\ldots,t_k,\ldots\}, where t_0=0 is the initial time and t_k is the kth switching instant. It is assumed that x^{(0\sim n-1)} does not jump at the switching instants."`

---

## 3. `Problem`（问题陈述）结构与原句 `[E]`

**结构**：`引导句` $\to$ `给定系统与所满足假设` $\to$ `Find / Design + 待求变换或控制律形式` $\to$ `such that + 闭环目标（等价转换/指数稳定/鲁棒 GUA 镇定/指标最优）`。

- **引导句 `[E: Volume I, pp. 42, 133, 351, 384]`：**
  - `"Based on the above formulation, we state the problem to be solved in this section as follows."`
  - `"According to the above Theorem 1, Problem 1 is clearly equivalently converted into the following one."` `[E: Chained Forms Part 1, §3]`
- **原句模板 `[E: Volume I, Problems 2.3, 3.1, 11.1, 12.1]`：**
  - `"Problem 2.3: Design a controller based on the FAS model (2.115) such that the resulting closed-loop system of the original LTV system (2.109) is exponentially stable."`
  - `"Problem 3.1 (The elementary problem): For an arbitrarily chosen Hurwitz matrix F \in \mathbb{R}^{nr\times nr}, find the parameter matrix A_{0\sim n-1} such that the following equation holds: \Phi(0_{0\sim n-1}) - B_c A_{0\sim n-1} = V F V^{-1}, where V \in \mathbb{R}^{nr\times nr} is nonsingular."`
  - `"Problem 11.1: Under Assumptions 11.1–11.3, find a dynamical output controller in the form of (11.3) such that the closed-loop system (11.7)–(11.8) is uniformly exponentially stable."`

---

## 4. `Definition`（定义）结构与原句 `[E]`

**结构**：`前置过渡句（交代为何引入该定义）` $\to$ `设集合/函数/系统及维数` $\to$ `if / 集合表达式` $\to$ `is called / is said to be ...` $\to$ `紧接等价改写或极端情形说明`。

- **奇异集、可行集与奇异函数完整原句链 `[E: Duan 2023 TCYB, §III-B, Defs. 5–6]`：**
  - **过渡句**：`"Regarding the ith subsystem of system (1), we introduce the following definition presented in [Duan 2023]."` / `"In order to better describe the singular set of a sub-FAS, let us now define two types of functions."`
  - **定义原句**：
    > `"Definition 5: A scalar function \varphi_0(X, t) is called a function of normal singularity for the sub-FAS (18) or (25) if \varphi_0(X, t) = 0, t \geq 0 \Longleftrightarrow \det B(X, t) = 0, t \geq 0."`
    > `"Based on the above function of normal singularity, we can further describe the normal singular set \mathbb{S}_0 as follows: \mathbb{S}_0 = \{X \mid \varphi_0(X, t) = 0, X \in \mathbb{R}^m, t \geq 0\}. Parallelly, we have the following definition."`
    > `"Definition 6: A scalar function \varphi_\infty(X, t) is called a function of abnormal singularity for the sub-FAS (18) or (25) if \varphi_\infty(X, t) = 0, t \geq 0 \Longleftrightarrow \det B(X, t) = \infty, t \geq 0."`
    > `"Similarly, the abnormal singular set \mathbb{S}_\infty for the sub-FAS (18) or (25) can be re-expressed as \mathbb{S}_\infty = \{X \mid \varphi_\infty(X, t) = 0, X \in \mathbb{R}^m, t \geq 0\}. Furthermore, with the above notations, the feasible set clearly has the following expression: \mathbb{F} = \mathbb{R}^m \setminus \mathbb{S} = \{X \mid \varphi_0(X, t)\varphi_\infty(X, t) \neq 0, X \in \mathbb{R}^m, t \geq 0\}."`
    > `"Of course, we can also define the function of singularity \varphi(X, t) for the sub-FAS (18) or (25) in the same way. Clearly, 1) \varphi(X, t) = \varphi_0(X, t) when the abnormal singularity condition is absent; 2) \varphi(X, t) = \varphi_\infty(X, t) when the normal singularity condition is absent; 3) \varphi(X, t) = \varphi_0(X, t)\varphi_\infty(X, t) when both normal and abnormal singularity conditions are present."`
- **子系统奇异分类定义 `[E: Duan 2023 TCYB, Defs. 3–4]`：**
  - `"Definition 3: The sub-FAS (18) or (25) is called a 0-type sub-FAS if \mathbb{S} = \mathbb{S}_0; is called a \infty-type sub-FAS if \mathbb{S} = \mathbb{S}_\infty; and is called a mixed-type sub-FAS if none of \mathbb{S}_0 and \mathbb{S}_\infty is empty."`
  - `"Definition 4: The sub-FAS (18) or (25) is called: 1) a rational sub-FAS if \mathbb{S} does not contain the origin; 2) a critical rational sub-FAS if \mathbb{S} contains the origin as a boundary point; 3) an irrational sub-FAS if \mathbb{S} contains the origin as an inner point."`
- **亚稳定（Substability）定义 `[E: Duan 2023 TCYB, Def. 1]`：**
  - `"Definition 1: Let \mathcal{Q} \subset \mathbb{R}^n be nonempty. If for any initial value x_0 \in \mathcal{Q}, the solution of system (16), x(t, x_0), exponentially converges to zero, then system (16) is called substable with respect to the ROEA \mathcal{Q}."`
  - **紧接说明**：`"Clearly, when the ROEA \mathcal{Q} = \mathbb{R}^n, system (16) is globally exponentially stable in the Lyapunov sense."`

---

## 5. `Assumption` 与 `Condition` 结构与原句 `[E]`

**原则**：每个假设承担单一、可定位到证明使用点的数学职责；Duan 原文已有的定义/条件（如奇异函数零集等价）放回 `Definition`，**本文新增的分析前提**（如 $\varphi_i$ 在 $\mathbb{R}^{nr}$ 上固定且连续）单独列为 `Assumption` 并明示用途 `[D]`；不写空泛的 `"all functions are sufficiently smooth"` 除非后续高阶消元求导需要。

- **全局全驱假设 `[E: Volume I, Assumption 2.1 / Part III, Assumption A1]`：**
  - `"Assumption 2.1: \det B(X, t) \neq 0\text{ or }\infty,\ \forall X \in \mathbb{R}^{nr},\ t \geq 0."`
- **不确定项连续界条件 `[E: Volume I, Assumption 5.2 / Part III, Condition 1]`：**
  - `"Assumption 5.2: There exists a non-negative continuous scalar function \rho(x^{(0\sim n-1)}) such that the nonlinear uncertainty \Delta f(x^{(0\sim n-1)}) \in \mathbb{R}^r satisfies \|\Delta f(x^{(0\sim n-1)})\| \leq \rho(x^{(0\sim n-1)})."`
- **切换 sub-FAS 新增连续奇异函数假设 `[D: main_v2.tex Assumption 1]`：**
  - 引导句：`"The switching analysis requires the following additional condition."`
  - 陈述：`"Assumption 1: For each i \in \mathcal{P}, the singularity function \varphi_i : \mathbb{R}^{nr} \to \mathbb{R} is fixed and continuous on \mathbb{R}^{nr}."`

---

## 6. 正式结论的铁律：陈述本身必须显式体现目标 `[E/D]`

> **核心原则**：每一个 **Theorem、Lemma、Proposition、Corollary** 都必须在**陈述本身**中直接写出它在文中的最终目的与控制/几何结论，绝不能只写一个中间关系（如仅写 $X_0\notin\mathcal R_i$）而把真正目的（如扩展 ROEA 对子系统 ROEA 并集的严格扩大）藏在前后引导句或 `Remark` 里。

### 6.1 `Lemma`（引理）结构与原句
**结构**：`Let / Suppose + 前提与对象` $\to$ `Then + 可直接被主定理调用的明确结论（多结论用 1) ...; 2) ... 分列）`。

- **谱裕度转 Lyapunov 矩阵不等式 `[E: Part III, Lemma 3.1]`：**
  - `"Lemma 3.1: Let A \in \mathbb{R}^{n\times n} satisfy \operatorname{Re}\lambda_i(A) \leq -\gamma/2, i = 1, 2, \ldots, n, where \gamma > 0, then there exists a positive definite matrix P \in \mathbb{R}^{n\times n} satisfying A^{\mathrm{T}}P + PA \leq -\gamma P."`
- **伴随矩阵特征值配置存在性 `[E: Part III, Lemma 3.2]`：**
  - `"Lemma 3.2: For any \mu > 0, there exist a set of matrices A_i \in \mathbb{R}^{r\times r}, i = 0, 1, \ldots, n-1, satisfying \operatorname{Re}\lambda_i(\Phi(A_{0\sim n-1})) < -\mu/2, i = 1, 2, \ldots, nr."`
- **受约束响应化为初值不等式区域 `[E: UC-FAS Part II, Lemma 4.1]`：**
  - `"Lemma 4.1: Let s_1 and s_2 (s_2 > s_1) be two positive scalars satisfying s_1 + s_2 = b_1, s_1 s_2 = b_0, and define R_b^{\mathrm{ex}} = \{(x_{30}, x_{3d}) \mid x_{3d} + s_2 x_{30} > 0,\ x_{30} > 0\}. Then constraint (96) is equivalent to (x_{30}, x_{3d}) \in R_b^{\mathrm{ex}}."`
- **频域多项式矩阵非奇异引理 `[E: Duan & Zhou 2022, Lemma 4.4]`：**
  - `"Lemma 4.4: Suppose that (A, B) is controllable. Let (N(s), D(s)) be right coprime and satisfy (11), and D(s) be column reduced. Then the matrix \check{N} defined in (21) is nonsingular."`
- **切换 sub-FAS 有限区间切换次数与唯一延拓引理 `[D: main_v2.tex Lemma 1，用户审定范本]`：**
  - `"Lemma 1: Suppose that system (1) satisfies Assumption 1, and consider the control laws (9) and the switching law \kappa^* specified by (15)–(16). Let T > 0 be finite, and suppose that a solution is defined on [0, T) and that its state x^{(0\sim n-1)}(t) has a limit in \mathcal{F}_{\mathrm{ext}} as t \to T^-. Then 1) the switching signal has finitely many switching instants on [0, T); 2) the solution can be uniquely continued beyond T."`

### 6.2 `Proposition`（命题）结构与原句
**职责**：承载模型等价转换、参数化通解、不可能性判据或集合严格包含等结构性结论。

- **特征结构配置参数化通解 `[E: Volume I, Proposition 1.1]`：**
  - `"Proposition 1.1: For an arbitrarily chosen F \in \mathbb{R}^{mn\times mn}, all the matrices A_{0\sim m-1} and the nonsingular matrices V \in \mathbb{R}^{mn\times mn} satisfying \Phi(A_{0\sim m-1}) = V F V^{-1} are given by ..."`
- **反馈线性化与 0-type 有理 sub-FAS 等价性 `[E: Duan 2023 TCYB, Proposition 2]`：**
  - `"Proposition 2: A nonlinear time-varying system is locally feedback linearizable if and only if it can be equivalently converted into a 0-type rational sub-FAS."`
- **严反馈系统化为 HOFAS `[E: Volume I, Proposition 6.1]`：**
  - `"Proposition 6.1: Let Condition 6.1 be satisfied, then the generalized SFS (6.94) can be transformed into the following FAS model: z^{(n)} = h(z^{(0\sim n-1)}, \zeta, t) + \Delta h(z^{(0\sim n-1)}, \zeta, t) + L_n(z^{(0\sim n-1)}, \zeta, t)u, with ..."`
- **驻点有限性命题 `[E: Duan & Wang 2026, Proposition 1]`：**
  - `"Proposition 1: Suppose \Phi(A_{0\sim n-1}) possesses different stable real eigenvalues. Then 1) \varphi_i(t), i = 1, 2, \ldots, m, are smooth if c(t) is smooth; 2) \varphi_i(t), i = 1, 2, \ldots, m, are bounded and tend to zero if c(t) is bounded; and 3) \varphi_i(t), i = 1, 2, \ldots, m, have a finite number of stationary points on [0, +\infty) if c(t) \equiv c."`
- **与参数无关的严格 ROEA 扩大命题 `[D: main_v2.tex Proposition 1，用户审定范本]`：**
  - `"Proposition 1: Suppose that switched sub-FAS (1) satisfies Assumption 1 and \mathcal{F}_{\mathrm{ext}} = \mathbb{R}^{nr}. Let \gamma \in (0, 1) be an arbitrarily given number, and X_0 \in \mathbb{R}^{nr} be an initial state such that, for every i \in \mathcal{P}, the set \mathcal{S}_i \setminus \{0\} intersects every continuous curve \Gamma : [0, 1] \to \mathbb{R}^{nr} whose endpoints satisfy \Gamma(0) = X_0, \Gamma(1) = 0. Consider the control laws (9) and the switching law \kappa^* specified by (15)–(16). Then, for every set of matrices A_j \in \mathbb{R}^{r\times r}, j = 0, 1, \ldots, n-1, such that \Phi(A_{0\sim n-1}) is Hurwitz, X_0 lies in the extended ROEA but outside the ROEA of every subsystem, that is, X_0 \in \mathcal{R}_{\kappa^*} \setminus \bigcup_{i\in\mathcal{P}} \mathcal{R}_i(A_{0\sim n-1})."`

### 6.3 `Theorem`（定理）六段式结构、分条结论与定理后评述句 `[E]`
**六段式顺序 `[E: Part III Theorem 3.5 / 用户“Duan规范”笔记]`**：
$$\text{针对什么系统} \to \text{满足什么假设} \to \text{任意给定什么自由参数} \to \text{设计矩阵满足什么条件} \to \text{采用什么控制律（含辅助项）} \to \text{保证什么闭环性能与吸引域/椭球集}$$

- **鲁棒跟踪六段式标准范本 `[E: Part III, Theorem 3.5]`：**
  > `"Theorem 3.5: Suppose that system (2) satisfies Assumption A1 and Condition 1. Let \mu and \varepsilon be two arbitrarily given positive numbers, and A_i \in \mathbb{R}^{r\times r}, i = 0, 1, \ldots, n-1, be a set of matrices satisfying (9). Then, the following control law u = -L^{-1}(x^{(0\sim n-1)})(A^{0\sim n-1}x^{(0\sim n-1)} + u^*), u^* = \cdots, with u_0(x^*) = \cdots, guarantees that the state x^{(0\sim n-1)} converges globally into the following ellipsoidal belt-shaped region centred at (x^*)^{(0\sim n-1)}: \Theta_{\mu,\varepsilon}((x^*)^{(0\sim n-1)}) = \{x^{(0\sim n-1)} \mid (x - x^*)^{(0\sim n-1)\mathrm{T}} P (x - x^*)^{(0\sim n-1)} \leq \varepsilon / \mu\}."`
- **sub-FAS 亚镇定与 ROEA 三条结论式范本 `[E: Duan 2023 TCYB, Theorem 1]`：**
  > `"Theorem 1: Let \mathbb{F} \subset \mathbb{R}^m, m \leq \gamma nr, be the feasible set of the single-order affine sub-FAS (18), and A_{0\sim n-1} \in \mathbb{R}^{r\times nr} be an arbitrarily given matrix which makes \Phi(A_{0\sim n-1}) stable. Then 1) a substabilizing controller for the single-order affine sub-FAS (18) is given by (30); 2) the resulting closed-loop system is given by x^{(n)}(t) + A_{0\sim n-1}x^{(0\sim n-1)}(t) = 0, Tx^{(0\sim n-1)}(t - \sigma_j(t))\vert_{j=1\sim\gamma} \in \mathbb{F}, t \geq 0; 3) the ROEA of the system is given by R_s = \{X_0 \mid \varphi(Te^{\Phi(A_{0\sim n-1})(t-\sigma_j(t))}X_0\vert_{j=1\sim\gamma}, t) \neq 0, X_0 \in \mathbb{R}^{nr}\text{ and }t \geq 0\}, where \varphi(\cdot) is the singularity function of the sub-FAS (18)."`
- **定理/结果之后的标志性点睛句 `[E: 全语料出现 58 次]`：**
  - `"The above result converts the infinite time RoEA characterization problem into a finite dimensional one."` `[E: Duan & Wang 2026, p. 239]`
  - `"The above results reveal the nature of a (global) FAS."` `[E: Duan 2023 TCYB, p. 7314]`
  - `"The above theorem clearly establishes a general parametric solution of controller (4.19), which arbitrarily assigns the desired eigenstructure of the closed-loop system (4.23)."` `[E: Volume I, Remark 4.3]`

### 6.4 `Corollary`（推论）引导句与陈述结构 `[E]`
- **常用引导句 `[E]`：**
  - `"Taking \mu_0 = 2 and \theta = 1/2 in the above lemma, immediately gives the following corollary."` `[E: Chained Forms Part 2, p. 8]`
  - `"Parallelly, letting \hat{\psi}(\cdot) = -\beta in the above Theorem 6 gives the following corollary."` `[E: Chained Forms Part 1, p. 20]`
  - `"The above result clearly has the following two corollaries."` `[E: Duan 2023 TCYB, p. 7313]`
- **条件句合并与 `which` 从句点明目标 `[E/D]`：**
  - 引用前文定理条件时，优先写 `"Let the conditions in Theorem 1 be met."` 或分清对象条件与参数条件并列在同一个 `Let` 下：`"Let switched sub-FAS (1) satisfy Assumption 1 and (8), and A_j, j=0,1,\ldots,n-1, be a set of matrices such that \Phi(A_{0\sim n-1}) is Hurwitz. Furthermore, let \gamma \in (0,1) be an arbitrarily given number."`（注意 `Let ... satisfy ...` 用动词原形，且不把参数矩阵条件写成系统本身的性质）。
  - 句末可用非限制性定语从句直接点出控制意义：`"... which drives all the state variables x_i, i=0,1,2, to zero exponentially."` `[E: Chained Forms Part 1, Corollary 3]`；`"... generates a switching signal \sigma with a finite number of switches on [0,\infty), which excludes Zeno behavior."` `[D: main_v2.tex Corollary 1]`。

### 6.5 `Remark`（注记）六类标准用途与原句开口 `[E]`
**边界纪律**：`Remark` 只用于解释、特例、自由度、方法对比或实现有界性补充；**需要十余行证明的独立主结论必须升格为 `Lemma`/`Proposition`/`Corollary`，不得塞入 `Remark`；定理成立所必需的假设不得藏在 `Remark` 中**。

1. **揭示设计自由度（DOFs）**：`"It is seen from the above result that as long as the matrix F is chosen stable, the closed-loop system is stable. Clearly, there are quite some DOFs in the selection of F, while on the other hand we also have the parameter matrix Z, which provides ..."` `[E: Volume I, Remark 1.5]`
2. **退化/特例检验（如不确定项消失或 $N=1$）**：`"When the nonlinear uncertainty is removed, we can choose \rho(x^{(0\sim n-1)}) = 0. In this case the closed-loop system is in the following constant linear form: ..."` `[E: Part III, Remark 3.3]`
3. **与状态空间、反馈线性化、反步法对比**：`"Some readers who are not yet familiar with the FAS approach might be mistaken that the FAS approach is nothing but feedback linearization. The above result can only tell that feedback linearization is a special case of the FAS approach, but not vice versa."` `[E: Volume I, Remark 2.6]`；`"The proposed HOFA system approach is generally more effective than the method of backstepping because of the following two facts: ..."` `[E: Part II, Remark 2.3]`
4. **亚稳定与 Lyapunov 局部指数稳定的关系 `[E: Duan 2023 TCYB, §IV]`**：`"1) When the ROEA \mathcal{Q} contains the origin as an inner point, the derived substabilizing controller is also at least a local exponentially stabilizing controller in the Lyapunov sense. 2) When the origin is only a boundary point of the largest ROEA \mathcal{Q}, the derived substabilizing controller does not exponentially stabilize the system in the Lyapunov sense."`
5. **结构分布矩阵 $T$ 降维说明**：`"In many cases, the matrix B(\cdot, t) involves only a few of the elements in the generalized state vector ..., while the function of the structural distribution matrix T allows us to 'recognize' those variables really affecting the matrix B(\cdot, t)."` `[E: Duan 2023 TCYB, Remark 1]`
6. **参数调节方向与实现有界性**：`"In applications, the radii of the ellipsoids ... can be comprehensively adjusted through two ways ..."` `[E: Part III, Remark 3.1]`

---

## 7. 八大经典证明结构与原句模板 `[E]`

**段广仁证明开篇总原则 `[E: 65 个证明首句统计]`**：
- **默认第一句直接进入推理或引入变换/集合对象**，不写 `"We first show that ..."` 之类先预告内容的废话（除非证明很长且确需分步，此时也只交代结构：`"The proof is composed of four steps."` / `"For the sake of clarity, we divide the proof into three steps."`）。
- 证明采用**“文字—公式—文字—公式”**节奏：关键中间关系单独列为展示式（Duan 习惯对证明中的主要展示式编号，或在同一证明内保持编号策略统一），文字只负责交代依据与承接。

### 7.1 直接代入与状态空间/Lyapunov 证明（Direct Substitution & Lyapunov Proof）`[E]`
**骨架**：`代入控制律` $\to$ `高阶常系数闭环方程` $\to$ `化为 state-space form（不说 first-order form）` $\to$ `选取 Lyapunov 函数` $\to$ `In view of (...) 求导放缩` $\to$ `收敛性/椭球结论`。

**原句链 `[E: Part III §3.2; Overview 2024 §IV-A]`：**
- `"Substituting the control law (14) into system (2), gives the following closed-loop system: ..."`
- `"The closed-loop system (15) is equivalent to / can be written in the following state-space form: \dot x^{(0\sim n-1)} = \Phi(A_{0\sim n-1})x^{(0\sim n-1)} + B_c v."`
- `"Since A_i, i=0,1,\ldots,n-1, satisfy the condition (9), there exists a positive definite matrix P(A_{0\sim n-1}) satisfying (10). Then the following Lyapunov function can be chosen for the system (17): V = \frac{1}{2} (x^{(0\sim n-1)})^{\mathrm{T}} P(A_{0\sim n-1}) x^{(0\sim n-1)}."`
- `"In view of (10), (12) and (17), we have \dot V = \cdots"`
- `"Combining (...) and (...), we obtain ..."`

### 7.2 SUB-FAS 亚镇定与 ROEA 刻画证明 `[E: Duan 2023 TCYB, Theorem 1]`
**原句链：**
- `"Proof: The first two conclusions are obvious. To show the third condition, we first convert system (32) into the following state-space form: \dot x^{(0\sim n-1)} = \Phi(A_{0\sim n-1})x^{(0\sim n-1)}, whose solution is clearly given by x^{(0\sim n-1)}(t) = e^{\Phi(A_{0\sim n-1})t}X_0, where X_0 = x^{(0\sim n-1)}(0) is the initial value."`
- `"Substituting (33) into the matrix B(\cdot), gives the following feasibility conditions: ... where t \geq 0. These are obviously constraints on the system initial value X_0."`
- `"Further, by definitions of normal and abnormal singularity functions of the sub-FAS (18), the above feasibility condition (34), (35) can also be written into ..., which is clearly equivalent to (36). This proves R_a = R_s."`

### 7.3 反证法（Proof by Contradiction）标准模板 `[E: Duan & Zhou 2022, Lemma 4.4]`
**严禁写 `"We prove the result by contradiction"` 或 `"Suppose, on the contrary"`**（`on the contrary` 在 Duan 论文中仅用于正文对比论述，不用于反证法开头）。直接假设结论的否定，由假设必然推出某对象的存在，再构造正面碰撞的两面矛盾，最后固定三句收尾：

**标准骨架：**
```text
Suppose that [结论的否定].
Then it follows from (x) that [展示式].
...
Therefore, there exists [由反设推出的对象] such that [展示式],
which means that [性质 A].
On the other side, [由定理前提或系统方程] implies that [非 A].
This yields a contradiction. Thus [原结论]. The proof is finished.
```

**原文逐字范本 `[E: Duan & Zhou 2022, Lemma 4.4, p. 2055]`：**
> `"Suppose that \check{N} is singular. Then there exists an elementary (nonsingular) matrix T such that [eq]. Let \bar{X}(s) = TX(s). Then it follows from (22) that [eq], from which it follows that [eq], in which \bar{x}_1(t) \in \mathbb{R}. Therefore, \bar{x}_1(t) cannot be controlled by u. On the other side, it follows from \bar{x}(t) = Tx(t) and (1) that \dot{\bar{x}}(t) = T(Ax(t) + Bu(t)) = TAT^{-1}\bar{x}(t) + TBu(t), which means that \bar{x}_1(t) can indeed be controlled by u. This yields a contradiction. Thus \check{N} is nonsingular. The proof is finished."`

**变体（方程直接导出矛盾）`[E: Chained Forms Part 1, eq. (10)]`：**
> `"Recall that \varepsilon is a positive scalar. The above equation (10) gives a contradiction which states that ... Therefore, by the well-known Brockett Theorem [1], ..."`

### 7.4 高阶反步法（High-Order Backstepping）标准结构 `[E: Part III §4; Part IV §3; Volume I §9.2]`
**核心特征**：Duan 的高阶反步法**不把**各高阶子系统降为一阶方程，而是借助反单位阵置换后的 Lyapunov 矩阵 $\tilde P_i(A_i^{0\sim m_i-1}) = \mathring{I}_{m_i} P_i(A_i^{0\sim m_i-1})$ 构造高阶误差变换，使得虚拟控制律 $\alpha_{i-1}$ 在第 $i$ 步只需微分 $m_i - 1$ 次（二阶子系统仅求一阶导数！），并在完整分步构造之后用 `"The above process clearly proves the following result."` 引出主定理：

1. **Preparations（与被控对象无关的预备矩阵）`[E: Volume I, pp. 306–307]`：**
   - 选取满足 $\operatorname{Re}\lambda_k(\Phi(A_i^{0\sim m_i-1})) \leq -\mu/2$ 的矩阵组及满足 $\Phi^\top P_i + P_i \Phi \leq -\mu P_i$ 的正定矩阵 $P_i(A_i^{0\sim m_i-1}) = [P_{iF}\ P_{iL}]$；
   - 定义 $\tilde P_i = \mathring{I} P_i$ 及其逆分块 $\tilde P_i^{-1} = [Q_{i1}^\top\ Q_{i2}^\top]^\top$，验证 $Q_{iL} \neq 0$；
   - 原句：`"It is worth pointing out that all the variables defined above are independent of system (9.1), and can all be easily obtained beforehand."`
2. **`The First Step`（第一步）`[E: Volume I, §9.2.1]`：**
   - 令 $z_1^{(0\sim m_1-1)} = x_1^{(0\sim m_1-1)}$，引入高阶误差变换：
     $$\tilde P_2(A_2^{0\sim 1})z_2^{(0\sim 1)} = x_2^{(0\sim 1)} - \begin{bmatrix}\alpha_1 \\ 0\end{bmatrix},$$
     利用 $P_2$ 对称性等价分解为 $P_{2L}^\top z_2^{(0\sim 1)} = x_2 - \alpha_1$ 与 $P_{2F}^\top z_2^{(0\sim 1)} = \dot x_2$；
   - 代入第一子系统，设计第一虚拟控制律 $\alpha_1 = -L_1^{-1}(A_1^{0\sim 1}z_1^{(0\sim 1)} + \alpha_1^*)$；
   - 原句：`"The closed-loop subsystem resulted in by this control law is \ddot z_1 + A_1^{0\sim 1}z_1^{(0\sim 1)} = \varphi_1 + w_1, with ... and w_1 = L_1 P_{2L}^\top z_2^{(0\sim 1)}."`
3. **`The Second Step` / `The k-th Step`（递推中间步）`[E: Volume I, §9.2.2–9.2.3]`：**
   - 对 $\alpha_{k-1}$ 求导并分离确定项与不确定项：`"Similar to the second step, taking derivative of the above equation, and further separating its certain part and uncertain part, yield \dot\alpha_{k-1} = h_{k-1}(\cdot) + \Delta h_{k-1}(\cdot)"`；
   - 由 $\tilde P_k^{-1}$ 写出 $z_k^{(m_k)}$，引入下一步变换 $\tilde P_{k+1} z_{k+1}^{(0\sim 1)} = x_{k+1}^{(0\sim 1)} - [\alpha_k^\top\ 0]^\top$；
   - 设计含层间耦合抵消项 $+v_{k-1}$（其中 $v_{k-1} = L_{k-1}^\top P_{k-1,L} z_{k-1}^{(0\sim 1)}$）的虚拟控制律 $\alpha_k$，得到闭环子系统 $\ddot z_k + A_k^{0\sim 1}z_k^{(0\sim 1)} = \varphi_k + w_k - v_{k-1}$。
4. **`The n-th Step`（末步实际控制律）`[E: Volume I, §9.2.4]`：**
   - `"Continue the above process, and suppose that the expressions of \alpha_{n-1}, \dot\alpha_{n-1}, h_{n-1} and \Delta h_{n-1} have all been obtained. Then, similar to the previous treatment, we can obtain ..."`
   - 设计实际控制律 $u = -L_n^{-1}(A_n^{0\sim 1}z_n^{(0\sim 1)} + u^*)$（含 $+v_{n-1}$），得到末级闭环 $\ddot z_n + A_n^{0\sim 1}z_n^{(0\sim 1)} = \varphi_n - v_{n-1}$。
5. **`The Conclusion`（总 Lyapunov 函数叠缩与引出定理）`[E: Volume I, §9.2.5]`：**
   - 定义 $V = \sum_{i=1}^n V_i$，$V_i = (z_i^{(0\sim 1)})^\top P_i z_i^{(0\sim 1)}$；
   - 验证交叉项恒等式 $(z_i^{(0\sim 1)})^\top P_{iL} w_i = (z_{i+1}^{(0\sim 1)})^\top P_{i+1,L} v_i$；
   - 原句：`"Adding the equations in (9.56) side by side, and using the relations in (9.58), give \dot V \leq -\mu V + n\varepsilon. The above process clearly proves the following result."`（紧接 `Theorem`）。

### 7.5 充要条件证明（Sufficiency & Necessity）`[E: Duan 2023 TCYB, Proposition 2]`
- `"Proof: Sufficiency: Once a system is equivalently converted into ..., a controller can be immediately constructed by a standard procedure such that ..."`
- `"Necessity: Suppose that ..., then, as proven in [...], the system can be converted equivalently into ..."`
- `"Combining the above two aspects gives the complete proof of the result."`

### 7.6 多结论逐条证明与多步骤证明 `[E]`
- **逐条证明**：`"The first two conclusions are obvious. To show the third condition, ..."` `[E: Duan 2023, Theorem 1]`；`"The first conclusion is then proven. The second conclusion can be shown similarly to that of ..."` `[E: Duan 2023, p. 7311; Part IX]`；待证剩余部分用 `"It remains to show that ..."` `[E: Duan & Zhou 2022, Theorem 4.5]`。
- **分步证明**：`"The proof is composed of four steps. Step 1. The Lyapunov Function: ... Step 2. Dealing with \dot V_r: ..."` `[E: Volume I, Appendix B, p. 421]`。

### 7.7 消元升阶与数学归纳法证明 `[E: Part II; Volume I, Ch. 7–8]`
- `"Proof: We prove the theorem via the n-step induction. Step 1: For the first subsystem, we already have that ..."` `[E: Volume I, p. 229]`
- `"We use mathematical induction to prove this result. Step 1 (Case of n = 2 and 3): Firstly, let us consider the case of n = 2. In this case, the system takes the form of ..."` `[E: Volume I, p. 450]`
- **注意**：证明等价转换时，必须同时给出正向消元与逆向恢复（diffeomorphism / homeomorphism）两个方向。

### 7.8 ROEA 单调区间分割与驻点有限化证明 `[E: Duan & Wang 2026, Theorem 1]`
- 按基函数驻点划分 $0 = t_0 < t_1 < \cdots < t_p = +\infty$ $\to$ 构造 $g(t, X_0)$ 并求导 $g'(t, X_0)$ $\to$ 证明每个子区间至多一个内驻点 $t^*$ $\to$ `"Therefore, the maximum of g(t, x, y) over [t_{i-1}, t_i) can only be attained either at the endpoints t_{i-1} and t_i, or at the unique interior stationary point t^*, if it exists."` $\to$ 分 `Case 1`–`Case 4` 写出显式代数边界 $\to$ `"This completes the proof."`。

---

## 8. 控制器构造、算例、图表与高频句式库 `[E/D]`

### 8.1 控制器先于闭环的标准引出顺序 `[E: Duan 2023 TCYB §IV-A; Underactuated 2024 §2.1]`
**绝不先凭空写出闭环再倒推控制器**。固定顺序为：说明可行集非空使 $B^{-1}$ 存在 $\to$ 构造控制律 $\to$ 代入原系统得到常系数线性闭环：
- `"When the feasible set, \mathbb{F} \subset \mathbb{R}^m, of the single-order affine sub-FAS (18) is not empty, it is obvious that B^{-1}(\cdot) exists on \mathbb{F}. Hence, we can immediately construct the following controller: [eq] under the following feasibility condition: [eq]."` `[E: Duan 2023 TCYB, p. 7314]`
- 切换子系统版本：`When \mathcal{F}_i \neq \emptyset, B_i^{-1} exists on \mathcal{F}_i. Hence, for the ith subsystem, we construct the following controller on \mathcal{F}_i: [eq], where A_j \in \mathbb{R}^{r\times r}, j=0,1,\ldots,n-1, are design matrices. Substituting (x) into the ith subsystem of (1) gives, on \mathcal{F}_i, the closed-loop system common to all subsystems: [eq].` `[D: main_v2_idea.tex]`

### 8.2 算例、仿真引图句式与短图题规范 `[E]`
- **引出算例 `[E]`**：`"Consider a system in the following state-space form: ..."` / `"Let us consider two practical backgrounds. One is ..."` / `"Consider the scalar second-order switched sub-FAS ..."`
- **正文引图与观察句式（禁用 `"To illustrate ..., Fig. X presents ..."`）`[E]`**：
  - `"the simulation of the system is carried out and the results are shown in Figs. 2 and 3."` `[E: Duan 2023 TCYB, p. 7320]`
  - `"This region is illustrated in Fig. 1."` / `"The RoEA \mathcal{R}' of the Lorenz system (7) is given in Fig. 2."` `[E: Duan 2023; Duan & Wang 2026]`
  - `"The simulation results are shown in Figures 1 and 2. It can be observed that the simulation results are consistent with the theoretical indications."` `[E: Part V, p. 987]`
  - `"The response and the switching signal are shown in Fig. 1. It can be observed that the state converges to the origin while ..."` `[D: main_v2_idea.tex]`
- **短图题（Figure Captions）规范 `[E]`**：
  - 采用 **2–6 个词的精炼名词短语**，不重复正文已证结论，不写长串解释性括号：
  - 原文示例：`"Region of attraction."` / `"State variables."` / `"Input variables."` `[E: Duan 2023 TCYB]`；`"RoEA R for the pendulum system (1)."` `[E: Duan & Wang 2026]`；`"Simulation results for Case A."` `[E: Part IV / Part V]`；`"Closed-loop response and switching signal."` / `"Singular sets and the state trajectory."` `[D: main_v2_idea.tex]`。
- **MATLAB 绘图规范（对齐 Duan 坐标轴习惯与用户 `matlab/p1ot.m`）`[D: 用户规范]`**：
  - 曲线用纯色实线 `'b-'`、`'r-'`、`'m-'`，`'linewidth', 1`（相平面轨迹若与同色奇异集区分可取 `'linewidth', 2`）；
  - 图例用 LaTeX 符号：`legend(..., 'interpreter', 'latex', 'FontSize', 12)`；
  - 参考线用虚线 `'--'`，颜色 `[0.15, 0.15, 0.15]`，`'LineWidth', 1.5`；
  - **无网格**（不启用 `grid on`）、**无图内标题**（`title` 留空，交给 LaTeX `\caption`）、`axis square`、显式指定 `xlim` / `ylim`；
  - 横轴 `'Time(s)'`（多子图堆叠时仅最底子图标横轴），纵轴用**具体变量符号加 `and`**（如 `'$x$ and $\dot x$'`，`[E: Duan 2023 Figs. 2–3]`，绝不笼统写 `'States'`）；
  - 切换时刻用红色竖虚线 `xline(ax, events, 'r--', 'LineWidth', 1)`，并在横轴刻度上标出切换时刻数值。
- **三线表规范**：一律使用 `booktabs` 的 `\toprule`、`\midrule`、`\bottomrule`，无竖线、无封闭网格。

### 8.3 Duan 高频衔接词与证明收尾词速查表 `[E]`

| 功能 | Duan 原文高频句式 `[E]` | 说明与注意事项 |
|---|---|---|
| 代入控制律/变换 | `Substituting control law (x) into system (y) gives / yields ...` | 证明标准起手式 |
| 引用前式/假设 | `It follows from (x) and Assumption A1 that ...` | 把依据放在句首，优于句尾悬挂 `by (x)` |
| 综合多式求导 | `In view of (x) and (y), we have ...` | 注意固定搭配是 `In view of`，绝不写 `In the view of` |
| 合并上下界/分步结果 | `Combining (x) and (y), we obtain ...` / `Combining the above two aspects gives ...` | 常用于 Lyapunov 上下界或充要性汇总 |
| 引出定义/集合显式式 | `... clearly has the following expression:` / `can be re-expressed as` | Duan 原文地道句式，润色时**不得**误删 |
| 构造控制器 | `Hence, we can immediately construct the following controller:` / `we construct the following controller:` | 置于可行性说明之后 |
| 高阶转状态空间 | `is equivalent to / can be written in the following state-space form:` | 不说 `first-order form` |
| 反证对立面 | `On the other side, ...` / `On the other hand, ...` | 反证法中引出与前文正面冲突的另一面 |
| 证明收尾 | `The proof is finished.` / `The proof is completed.` / `This completes the proof.` | 同一篇稿件内建议保持一致；反证法经典收尾为 `The proof is finished.` |
| 引用不等式与方程 | `inequality (34)` vs `equation (25)` / `\eqref{...}` | 不把不等式称为 `equation`，少用模糊名词 `the estimate (34)` |

### 8.4 写作与润色正反对照表（杜绝 AI 腔与偏离 Duan 习惯）

| 常见 AI 腔 / 偏离写法（禁止） | Duan 对齐写法（推荐） | 原因 |
|---|---|---|
| `"Their values need not equal geometric distances, and no identity is assumed..."` | 直接写定义与所用假设，删去无必要的防御性否定句 `"not X, but Y"` | 过多防御性免责声明 AI 味极重；仅保留真正影响定理适用边界的限定 |
| 把 Duan 原句 `"clearly has the following expression:"` 改成 `"is given by"` | 保留 `"has the following expression:"` 或 `"clearly has the following expression:"` | 属于 Duan 2023 原文自然句式 `[E]`，无需过度清理 |
| 自造 `"feasibility score"`、`"fixed-mode ROEA"`、`"continuous-state origin"` | 直接用 `$|\varphi_i|$`、`"the ROEA of the ith subsystem"`、`"the origin"` | 优先使用 Duan 原有概念与记号，不生造新名词 |
| 在确定性切换系统中混用 `mode i` 与 `subsystem i` 指代被控子系统 | 统一用 `the ith subsystem`（如 `the feasible set of the ith subsystem`），切换条件写 `If \sigma(t)=i`（不写 `i=\sigma(t)`） | 对齐切换系统文献与 Yang–Duan (2026) |
| 模型段写 `"As in Duan and Wang (2026), f_i and B_i are piecewise continuous..."` | 直接在 `where` 段写 `f_i(\cdot)\in\mathbb{R}^r and B_i(\cdot)\in\mathbb{R}^{r\times r} are piecewise continuous vector and matrix functions...` | 标准模型变量交代直接按 Duan 格式写，无需额外挂 `"As in..."` |
| 命题只写 `$X_0 \notin \mathcal{R}_i$`，把严格包含留给后面的 `Remark` | 在命题陈述内直接写出 `$X_0 \in \mathcal{R}_{\kappa^*} \setminus \bigcup_i \mathcal{R}_i$`（严格扩大） | 正式结论必须在陈述本身写明目标 |
| 证明首句写 `"We first show that switching ceases..."`（单结论证明） | 首句直接进入对象与依据：`"Let X_0 \in \mathcal{R}_{\kappa^*}. By Definition 3, ..."` | Duan 65 个证明首句几乎不写空洞预告 |
| 引图写 `"To illustrate strict enlargement, Fig. 2 presents..."` + 8 行长图题 | 正文写 `"... are shown in Fig. 2. It can be observed that ..."` + 3–6 词短图题 | 对齐 Duan 仿真叙述习惯，避免正文与图题重复 |


---

## 9. 五大专题系列专属结构标准范本索引 `[E]`

针对具体分支或中文稿件/开题报告撰写，请直接查阅 **[duan-series-templates.md](duan-series-templates.md)** 中的分系列结构范本与逐字原句库：
1. **最新 OD-FAS 输出依赖全驱系列（2026 `Part 1` 单阶 & `Part 4` 二阶动力学系统）**：$f_x + f_y$ 可测分离与控制变换降维、消去 $\dot y$ 的降阶观测器（$z = \hat q_2 + L y$）、理想全状态律替换化为 $(K_{11},K_{12},K_{21},K_{22})$ 动态补偿器、$T A_E T^{-1}$ 分块三角化与级联 ISS 证明、纯位置 vs 纯速度对偶 `Remark`、增广初值 $[X_0^\top\ z_0^\top]^\top$ 输出反馈 RoEA；
2. **UC-FAS 受约束单向连接全驱系列（2025 `Part I–III`）**：强/弱单向连接定义、内部/外部可行集 $\mathbb{F}^{\mathrm{in}}\cap\mathbb{F}^{\mathrm{ex}}$ 与内外 RoEA、三级自然递推亚镇定构造及直和吸引域 $\mathcal{R}_{xyz} = \mathcal{R}_x\oplus\mathcal{R}_y\oplus\mathcal{R}_z$、单侧不穿零约束实根半平面扇区引理；
3. **IJSS 抗扰解耦（`Part VI`）与离散时间系统（`Part X`）**：HOFAS 天然抗扰 `Remark`、GSE 参数化 $H_2$ 衰减与非齐次 GSE/RCF 渐近解耦；离散后退步 $x^{\lfloor 0\sim n\rfloor}(k)$ 与前进步 $x^{\lceil 0\sim n\rceil}(k)$ 反向堆叠记号、Schur 伴随矩阵 $\Psi(A_{0\sim n-1})$；
4. **SCIS 三大双篇系列（离散时滞 `Part 1–2`、连续时滞 `Part 1–2`、广义链式系统 `Part 1–2`）与 TCYB Type I 时滞鲁棒系列**：逐时刻可行点集 $\mathbb{F}_k$ 与亚能控性、状态时滞包络球内估计、输入时滞区间预测器 $Z(s)$ 两步证明、链式非完整指数缩放与二阶主导模态分离；
5. **《自动化学报》中文奠基系列（`I–III`）与《航空学报》（2024 亚严反馈）中文写作规范**：中文正式环境名（`定义/假设/问题/引理/命题/定理/推论/说明`）、中文权威术语与亚镇定证明原句模板。

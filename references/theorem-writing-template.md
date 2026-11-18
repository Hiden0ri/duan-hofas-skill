# Duan 正式数学环境标准模板库（基于 32 篇一作论文 + *Volume I* 共 867 个环境全量分拣）

本文件并非基于单篇论文抽样，而是对本地全集语料库（32 篇段广仁一作中英文论文 + 2026 专著 *Volume I*，共提取分拣 **867 个正式环境**：`Theorem` 198、`Assumption` 165、`Remark` 155、`Definition` 94、`Lemma` 80、`Proposition` 76、`Corollary` 65、`Problem` 24、`Condition` 10；分类原文见本地缓存 `corpus/sorted/*.md`）逐一归类与冲突复核后提炼出的**标准结构模板库**。

---

## 0. 全局铁律与全量统计纠偏 `[E/D]`

1. **陈述内显式写明目标（用户审定铁律 `[D]` + >95% 原文主流 `[E]`）**：
   - 撰写或润色时，每一个 **`Theorem`、`Lemma`、`Proposition`、`Corollary`** 都必须在**陈述本身**直接写出它在文中的最终目的与控制/集合结论，严禁只写中间技术关系而把真正结论拆入引导句或 `Remark`。（注：段广仁极少数中文短命题如 `AAAS 2024` 命题 2 仅写 `$S=\hat S, F=\hat F$` 属原文特例 `[E]`，审查原文时不判错，但撰写新稿一律写完整自包含陈述。）
2. **开头句式真实分布（纠正旧版仅以 `Suppose` 为唯一模板的偏差 `[E]`）**：
   - 在全部 190 个 `Theorem` 中：**`Let ...` 开头占 121/190（63.7%，绝对主力）**，`Suppose that ...` 占 23/190（12.1%），直接主语陈述配 `if / if and only if` 占 14/190（7.4%），`For / Consider / Under` 占 12/190。2023–2026 年近期论文最地道的假设引入句式是 **`"Let Assumptions A1–A2 be met / satisfied, and let F_{0\sim n-1} \in \mathbb{R}^{r\times nr} be a matrix making \Phi(F_{0\sim n-1}) Hurwitz. Then ..."`**。
3. **控制器在定理中的两种合法呈现方式（纠正旧版强制要求内联展开的冲突 `[E]`）**：
   - 在含控制器的定理中，**引用前文已构造的编号控制律**（62 处，如 `Duan 2023` Theorem 1 `"is given by (30)"`、`OD-FAS Part 1` `"is given in the form of (13) with..."`）与**在定理内部直接展开控制律公式**（53 处，如 `Part III` Theorem 3.5、`OD-FAS Part 1` Theorem 2.1）几乎各占一半。判断准则：若前文小节已完成逐步推导并编号，定理内直接写 `is given by (x)` 避免重复；若定理独立给出控制律，则在定理内完整写出主式及辅助项。
4. **分条标号随目标期刊统一 `[E]`**：190 个定理中有 **144 个（75.8%）** 使用分条结构；IEEE 期刊统一用 `1) ...; 2) ...; 3) ...`，Taylor & Francis（IJSS）与 SCIS 多用 `(1) ...; (2) ...; (3) ...`，单篇稿件内部严禁混用。

---

## 1. `Theorem`（定理）六大标准模板（`T1`–`T6`，共 190 例）`[E]`

### 模板 T1：镇定 / 鲁棒 / 自适应 / 输出反馈控制器主定理（68/190）
- **逻辑六要素顺序**：`受控系统与所满足假设` $\to$ `任意给定标量参数` $\to$ `满足 Hurwitz/谱裕度条件的设计矩阵` $\to$ `控制律（内联展开或引用编号 + 辅助矩阵）` $\to$ `闭环方程/收敛性质` $\to$ `明确的目标集合或性能指标`。
- **子型 T1a（`Let` 开头 + 控制律内联/分块赋值，2023–2026 主流）`[E: OD-FAS Part 4, Theorem 4.1]`**：
  > **Theorem X.** `Let Assumptions [...] be satisfied / met, and` $F_{0\sim n-1}\in\mathbb{R}^{r\times nr}$ `be a matrix making` $\Phi(F_{0\sim n-1})$ `Hurwitz. Then a [GUA / GUE] stabilizing [output feedback] controller for system (x) is given by / in the form of` [eq], `with` [gain definitions], `where` [auxiliary matrices]. `Furthermore, the corresponding closed-loop system is given by (...) with [...]`.
- **子型 T1b（`Suppose` 开头 + 鲁棒椭球收敛，经典六段式）`[E: IJSS Part III, Theorem 3.5]`**：
  > **Theorem X.** `Suppose that system (2) satisfies Assumption A1 and Condition 1. Let` $\mu$ `and` $\varepsilon$ `be two arbitrarily given positive numbers, and` $A_i\in\mathbb{R}^{r\times r},\ i=0,1,\ldots,n-1$, `be a set of matrices satisfying (9). Then, the following control law` $u = \cdots$, `with` $u_0(x^*) = \cdots$, `guarantees that the state` $x^{(0\sim n-1)}$ `converges globally into the following ellipsoidal belt-shaped region centred at` $(x^*)^{(0\sim n-1)}$`:` $\Theta_{\mu,\varepsilon} = \{\cdots\}$.

### 模板 T2：sub-FAS 亚镇定与 ROEA / RoEA 刻画定理（17/190）
- **子型 T2a（分条同时给出控制器、受约束线性闭环与 ROEA 精确刻画）`[E: Duan 2023 TCYB, Theorem 1]`**：
  > **Theorem X.** `Let` $\mathbb{F}\subset\mathbb{R}^m$ `be the feasible set of the single-order affine sub-FAS (18), and` $A_{0\sim n-1}\in\mathbb{R}^{r\times nr}$ `be an arbitrarily given matrix which makes` $\Phi(A_{0\sim n-1})$ `Hurwitz [or stable]. Then 1) a substabilizing controller for system (18) is given by (30); 2) the resulting closed-loop system is given by` $x^{(n)}(t)+A_{0\sim n-1}x^{(0\sim n-1)}(t)=0,\ x^{(0\sim n-1)}(t)\in\mathbb{F},\ t\ge 0$`; 3) the ROEA of the system is given by` $\mathcal{R} = \{X_0 \mid \varphi(\mathrm{e}^{\Phi(A_{0\sim n-1})t}X_0, t)\neq 0,\ X_0\in\mathbb{R}^{nr},\ t\ge 0\}$`, where` $\varphi(\cdot)$ `is the singularity function of system (18).`
- **子型 T2b（初值限制在 RoEA 内推出全时域可行与指数收敛）`[E: Overview 2024, Theorem 7; UC-FAS Part II, Theorem 2.1]`**：
  > **Theorem X.** `Let` $\emptyset\neq\mathbb{F}\subset\mathbb{R}^{nr}$ `be the set of feasibility of constrained FAS (1)–(2), and` $A_{0\sim n-1}\in\mathbb{R}^{r\times nr}$ `be an arbitrarily given matrix making` $\Phi(A_{0\sim n-1})$ `Hurwitz. Then, when the system initial value` $X_0 = x^{(0\sim n-1)}(0)$ `is restricted within the RoEA` $\mathcal{R}$`, the controller (6) produces the time-invariant linear closed-loop system (7), whose response satisfies` $x^{(0\sim n-1)}(t)\in\mathbb{F},\ \forall t\ge 0$`, and converges exponentially to the origin.`

### 模板 T3：充要条件（`if and only if`）判据定理（10/190）`[E: IJSS Part VI Theorem 4.4; Part X Theorem 3.4; AAS II 定理 1]`
- > **Theorem X.** `The system / matrix pair (...) is controllable [or observable / detectable / solvable] if and only if it can be equivalently converted into a high-order fully actuated system in the form of (...) [or condition (...) holds].`

### 模板 T4：模型等价转换与一对一同胚定理（28/190）`[E: SCIS Chained Part 1 Theorems 1–3; UC-FAS Part I Theorem 6.1]`
- > **Theorem X.** `Let Assumptions [...] be satisfied, and [...] be differentiable with respect to all variables. Then, under the transformation (x), 1) the transformation is one-to-one and keeps the origin unmoved; 2) system (y) is equivalently transformed into the FAS / sub-FAS` [eq] `on` $\mathbb{F}$`; and 3)` $\lim_{t\to\infty} z^{(0\sim n-1)}(t)=0 \Longrightarrow \lim_{t\to\infty} x_{1\sim n}(t)=0$.

### 模板 T5：完全参数化通解与性能解析表达式定理（13/190）`[E: IJSS Part VI Theorems 3.4–3.5, 4.5; AAS I 定理 4]`
- > **Theorem X.** `For an arbitrarily selected Hurwitz matrix` $F\in\mathbb{R}^{nr\times nr}$`, all the parameter matrices` $A_{0\sim n-1}$ `and nonsingular matrices` $V\in\mathbb{R}^{nr\times nr}$ `satisfying` $\Phi(A_{0\sim n-1}) = V F V^{-1}$ `are given by` [parametric formula in $(Z, F)$]`, where` $Z\in\mathbb{R}^{r\times nr}$ `is any parameter matrix satisfying` $\det V(Z, F)\neq 0$.

### 模板 T6：独立系统稳定性 / 级联 ISS / 有限维约化判据定理（54/190）`[E: OD-FAS Part 1 Theorem 8.1; Part 4 Theorems 3.1–3.2; Duan & Wang 2026 Theorem 1]`
- > **Theorem X.** `The origin of system (x) is globally uniformly asymptotically (GUA) stable if 1) [...]; 2) [...]; and 3) [...].`
- **定理后点睛评述句**：`"The above theorem/result clearly reveals / converts / establishes ..."` `[E]`。

---

## 2. `Lemma`（引理）六大标准模板（`L1`–`L6`，共 79 例）`[E]`

- **L1（矩阵谱裕度 / Lyapunov / 时变稳定引理，32/79）`[E: Part III Lemmas 3.1–3.2; OD-FAS Part 4 Lemmas 3.1, 5.1, 5.4]`**：
  > `Let` $A\in\mathbb{R}^{n\times n}$ `satisfy` $\operatorname{Re}\lambda_i(A)\le -\gamma/2$ `[or be Hurwitz]. Then there exists a symmetric positive definite matrix` $P\in\mathbb{R}^{n\times n}$ `satisfying` $A^\top P + P A \le -\gamma P$.
- **L2（广义 Sylvester 方程 / 多项式互质 / 正交矩阵性质引理，12/79）`[E: Part VI Lemmas 3.1, 4.2; Duan & Zhou 2022 Lemma 4.4; OD-FAS Part 4 Lemma 8.1]`**：
  > `Suppose that` $(A,B)$ `is controllable, and let` $(N(s), D(s))$ `be right coprime ... Then the matrix` $\check N$ `defined in (21) is nonsingular.`
- **L3（预测器 / 辅助系统轨迹恒等引理，2/79）`[E: SCIS Delay Part 2, Lemmas 1–2]`**：
  > `Let Assumptions A1 and A3 be met, and` $x^{(0\sim n-1)}(s),\ s\le t$`, be available and satisfy FAS (21). Then there holds` $x^{(0\sim n-1)}(t+s) = Z(s),\ s\in[0,h]$`, where` $Z(s)$ `is given by the predictor (46).`
- **L4（全时域可行约束化为初值区域等价引理，3/79）`[E: UC-FAS Part II Lemma 4.1; Part III Lemma 5.1]`**：
  > `Let` $s_1$ `and` $s_2$ ($s_2 > s_1 > 0$) `satisfy` $s_1+s_2=b_1,\ s_1s_2=b_0$`, and define` $\mathcal{R}_b^{\mathrm{ex}} = \{\cdots\}$. `Then constraint (96) is equivalent to` $(x_{30}, x_{3d})\in\mathcal{R}_b^{\mathrm{ex}}$.
- **L5（配方法不等式 / 受扰衰减积分 / 同胚收敛传递引理，7/79）`[E: Part III Lemma 3.3; SCIS Chained Part 2 Lemma 1; OD-FAS Part 1 Lemma 3.3]`**：
  > `Under diffeomorphism (69), global uniform exponential convergence of` $x^{(0\sim 3)}$ `to zero implies that of` $\theta^{(0\sim 1)}$ `and` $\varphi^{(0\sim 1)}$.
- **L6（模型分块降维 / 有限区间切换与唯一延拓引理，23/79 + `[D]`）**：
  > `Suppose that system (1) satisfies Assumption 1, and consider control laws (9) and switching law` $\kappa^*$`. Let` $T>0$ `be finite, and suppose that a solution on` $[0,T)$ `has a limit in` $\mathcal{F}_{\mathrm{ext}}$ `as` $t\to T^-$`. Then 1) the switching signal has finitely many switching instants on` $[0,T)$`; 2) the solution can be uniquely continued beyond` $T$. `[D: main_v2.tex Lemma 1]`

---

## 3. `Proposition`（命题）五大标准模板（`P1`–`P5`，共 74 例）`[E]`

- **P1（模型等价转换 / 能控能观充要规范型命题，25/74）`[E: Duan 2023 Prop. 2; Part X Prop. 6.4; OD-FAS Part 1 Prop. 3.2]`**：
  > `Under diffeomorphism (68), system (65) is equivalent to the following OD-FAS: [eq].` / `A nonlinear time-varying system is locally feedback linearizable if and only if it can be equivalently converted into a 0-type rational sub-FAS.`
- **P2（约化模型 / 中间子系统控制器命题，19/74）`[E: AAS I 命题 1; OD-FAS Part 1 Props. 2.1, 3.3; Part 4 Props. 6.2, 8.2]`**：
  > `Let system (6) be a global OD-FAS, and let reduced system (7) possess an output feedback stabilizing controller` $u_0=\alpha(\cdot, t)$`. Then the output feedback controller` $u=-B^{-1}(\cdot, t)(f_y(\cdot, t)-u_0)$ `stabilizes global OD-FAS (6) in the same sense.`
- **P3（降阶观测器 / 扰动联合估计器构造命题，8/74）`[E: OD-FAS Part 4 Props. 4.1, 5.1, 5.2, 6.1, 7.1]`**：
  > `Let Assumptions [...] be met, and` $A_{o1}\in\mathbb{R}^{r\times r}$ `be an arbitrary Hurwitz matrix. Then an observer giving the estimate of` $q_2$ `[and` $d$ `simultaneously] is given as follows: [eq], where [...]. Furthermore, the observation error` $e=q_2-\hat q_2$ `is governed by` $\dot e = A_{o1}e$.
- **P4（光滑镇定阻碍 / 不存在性判据命题，2/74）`[E: SCIS Chained Parts 1–2, Prop. 1]`**：
  > `The nonlinear system (6)–(8) does not have a smooth [time-invariant] exponentially stabilizing controller.`
- **P5（解析响应分解 / 驻点有限性 / 严格包含结构性质命题，20/74 + `[D]`）`[E: Duan & Wang 2026 Prop. 1; Chained Part 2 Props. 2–3]`**。

---

## 4. `Corollary`（推论）四大标准模板（`C1`–`C4`，共 65 例）`[E]`

- **常用前置引导句 `[E]`**：`"Taking / Letting [...] in the above Theorem X, immediately gives the following corollary."` / `"The above theorem clearly has the following corollary."`
- **C1（参数/非线性项退化特例，17/65）`[E: AAS I 推论 1–2; OD-FAS Part 4 Corollaries 4.1–4.2, 6.1–6.2]`**：令 $E=I_n$ 或 $A_1(\varphi^{(0\sim 1)})=A_1(\varphi)$ 为常值/仅依赖位置，消去高阶导数量测需求。
- **C2（维数或基准对象特化，8/65）`[E: Part II Corollaries 3.3, 3.5; Chained Part 1 Corollaries 2–3; UC-FAS Part III Corollary 5.1]`**：从一般 $n$ 阶或多阶特化到 $n=2,3$、单输入、Brockett 积分器或 PVTOL，句末常用 `, which drives all the state variables ... to zero exponentially.` 点明目标。
- **C3（直接等价判据 / 有限交集约化，11/65）`[E: Chained Part 1 Corollary 4; Duan & Wang 2026 Corollary 1]`**：`"Under Condition 1, the infinite constraint set defining R can be reduced to a finite intersection: R = \bigcap_{i=1}^p R_i..."`
- **C4（定理直接导出的闭环性质推论，29/65 + `[D]`）**：如有限总切换次数与排除 Zeno 行为（`", which excludes Zeno behavior"`）。

---

## 5. `Definition`、`Assumption / Condition`、`Problem` 与 `Remark` 标准模板 `[E]`

- **`Definition`（94 例：单概念型 vs 分条分类学型，全集主题索引见 [canonical-definitions-index.md](canonical-definitions-index.md)）**：
  - **D1 单概念型**：`"Let / Denote [...]. Then [...] is called / is said to be [...]."`（或 `"If [condition], then [...] is called [...]."`）
  - **D2 分条分类学型**：`"The sub-FAS (18) is called: 1) a rational sub-FAS if ...; 2) a critical rational sub-FAS if ...; 3) an irrational sub-FAS if ..."`
- **`Assumption`（155 例）vs `Condition`（10 例）边界**：93.9% 使用 `Assumption`（全驱性、可微性、可测性、伴随子系统稳定性）；仅在需将“不确定性界或线性可检测条件”与主全驱假设区分时才偶用 `Condition`。奇异集/可行集永远属于 `Definition`，本文新增条件单独列为 `Assumption` `[D]`。
- **`Problem`（24 例）三类模板**：
  - **Pr1 基本镇定/输出反馈问题**：`"Under Assumptions ..., find a [dynamical output / state feedback] controller in the form of (...) such that the closed-loop system (...) is [UGE / GUA] stable."`
  - **Pr2 代数特征结构配置（Elementary Problem / ESA）**：`"For an arbitrarily chosen Hurwitz matrix F, find parameter matrix A_{0\sim n-1} and nonsingular V such that \Phi(0_{0\sim n-1})-B_c A_{0\sim n-1}=VFV^{-1}."`
  - **Pr3 最优 / $H_2$ / 受约束指标问题（`Part VI`, `Part VIII`）**：`"Given HOFA system (3) and weighting matrices Q, R, find a feedback controller in the form of (8) such that 1) performance index J is minimised; and 2) feasibility condition (...) is met."`
- **`Remark`（155 例，中文对应 `说明`）五类合法职责**：`R1` 设计自由度 DOFs 与调参（28 例）、`R2` 退化特例与可推广情形（45 例）、`R3` 与状态空间/反馈线性化/反步法对比及澄清误解（22 例）、`R4` 亚稳定与 Lyapunov 关系及坐标平移/预控制器说明（9 例）、`R5` 原坐标逆变换恢复与实现说明（51 例）。**严禁将需十余行证明的核心新结论或隐藏假设塞入 `Remark`。**

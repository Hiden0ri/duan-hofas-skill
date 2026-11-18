# Duan 五大核心系列专属结构标准范本与原句语料库

本文件按段广仁（Guang-Ren Duan）五大核心论文系列，逐篇梳理**模型结构、正式环境骨架、证明套路与高频原句（`[E]`）**，与通用语料库 [duan-writing-corpus.md](duan-writing-corpus.md) 配套使用。本地 Zotero 馆藏的 **32 篇段广仁一作 FAS 论文**（含英文 28 篇、中文 4 篇）及 2026 年专著 *Volume I* 已全部完成逐篇核对（注：2026 年最新 OD-FAS 系列本地含 `Part 1` 与 `Part 4` 原文，`Part 2: Multi-order FASs` 与 `Part 3` 本地暂无 PDF，已按核实边界如实标注）。

---

## 1. 最新 OD-FAS 系列：输出依赖全驱系统与输出反馈控制（2026 `Part 1` & `Part 4`）`[E]`

**来源**：
- `Part 1: Case of Single-order FASs`（IJSS 2026，单阶 OD-FAS/sub-OD-FAS、静态/动态输出反馈、降阶观测器与输出反馈 RoEA）；
- `Part 4: Second-Order Dynamical Systems`（2026 预印手稿，一般二阶非线性系统纯位置反馈 vs 纯速度反馈、外扰同时观测补偿、时变二阶系统稳定性）。

### 1.1 OD-FAS 核心建模分解与控制变换降维结构 `[E: OD-FAS Part 1, §2.1]`
1. **漂移项可测/不可测分解**：将单阶 FAS 漂移项拆分为不可测全状态部分与仅依赖可测输出部分，且输入矩阵仅依赖可测输出：
   $$x^{(n)}(t) = f_x\bigl(x^{(0\sim n-1)}(t-\tau_i(t))\vert_{i=1\sim p}, t\bigr) + f_y\bigl(y(t-\tau_i(t))\vert_{i=1\sim p}, t\bigr) + B\bigl(y(t-\sigma_j(t))\vert_{j=1\sim q}, t\bigr)u(t),\quad y(t)=h(x^{(0\sim n-1)},t).$$
2. **缩写约定（`Convention C1`）原句**：
   - `"Convention C1: For simplicity, in the subsequent content of this paper, f_y(y(t-\tau_i(t))\vert_{i=1\sim p}, t) and B(y(t-\sigma_j(t))\vert_{j=1\sim q}, t) are simply denoted by f_y(\cdot, t) and B(\cdot, t), respectively."` `[E: Part 1, §2.1]`
3. **输出反馈等价归约命题（`Proposition 2.1`）原句**：
   - `"Proposition 2.1: Let system (6) be a global OD-FAS, and the system x^{(n)}(t) = f_x(\cdot, t) + u_0, y(t) = h(x^{(0\sim n-1)}, t) possesses an output feedback stabilizing controller u_0 = \alpha(y(t-\tau_i(t))\vert_{i=1\sim p}, t) in certain sense. Then the following output feedback controller u(t) = -B^{-1}(\cdot, t)(f_y(\cdot, t) - u_0), u_0 = \alpha(\cdot, t) stabilizes the global OD-FAS (6) (in the same sense)."` `[E: Part 1, §2.1]`

### 1.2 降阶观测器构造（消去不可测输出导数 $\dot y$）标准范本 `[E: OD-FAS Part 4, §4.1 & §6.1; Part 1, §9.1.1]`
**核心套路**：先写出形式上含 $\dot y$ 的全阶观测器 $\to$ 引入辅助变量 $z = \hat q_2 + L(\varphi^{(0\sim 1)})y$ 对消 $\dot y$ $\to$ 导出仅依赖 $(y, u_0)$ 的可实现降阶观测器 $\to$ 验证误差方程 $\dot e = A_{o1}e$（或相似 LTV 方程 $\dot e = R_E(\varphi)A_L R_E^{-1}(\varphi)e$）。

- **观测器命题标准陈述 `[E: Part 4, Proposition 4.1]`**：
  > `"Proposition 4.1: Let Assumptions A1 and A_{\varphi 1} be met, and A_{o1} \in \mathbb{R}^{r\times r} be an arbitrary Hurwitz matrix. Then an observer giving the estimate of q_2 can be given as follows: \dot z = A_{o1} z + \Theta_{\mathrm{Ia}}(\varphi^{(0\sim 2)})y + u_0,\ \hat q_2 = z - L(\varphi^{(0\sim 1)})y, where \Theta_{\mathrm{Ia}}(\varphi^{(0\sim 2)}) = \dot L(\varphi^{(0\sim 1)}) - A_{o1}L(\varphi^{(0\sim 1)}), L(\varphi^{(0\sim 1)}) = A_{o1} - R(\varphi)A_1(\varphi^{(0\sim 1)}). Furthermore, the observation error e = q_2 - \hat q_2 is governed by the following equation: \dot e = A_{o1} e."`
- **观测器证明原句链 `[E: Part 4, §4.1]`**：
  - `"Proof: Design a full-order observer for system (4.6) as \dot{\hat q}_2 = R(\varphi)A_1(\varphi^{(0\sim 1)})\hat q_2 + u_0 + L(\varphi^{(0\sim 1)})(\hat q_2 - \dot y), where L(\varphi^{(0\sim 1)}) is the observer gain given by (4.9)."`
  - `"Let z = \hat q_2 + L(\varphi^{(0\sim 1)})y. We further obtain \dot z = \cdots = A_{o1}z + \Theta_{\mathrm{Ia}}(\varphi^{(0\sim 2)})y + u_0, and \hat q_2 = z - L(\varphi^{(0\sim 1)})y. Combining (4.12) and (4.13), gives the observer (4.7)."`
  - `"Next, using (4.6), (4.7) and (4.11), we obtain \dot e = \dot q_2 - \dot{\hat q}_2 = \cdots = A_{o1}e. This gives equation (4.10)."`
- **状态与外扰同时观测陈述 `[E: Part 4, Proposition 5.1 / 7.1]`**：
  - `"Then an observer producing simultaneously the estimates of q_2 and d is given by ..."`

### 1.3 基于观测器的动态输出反馈四步标准推导链 `[E: OD-FAS Part 4, §4.2; Part 1, §2.2 & §9.1.2]`
1. **写出理想全状态反馈基准律**：
   - `"If both x and \dot x are measured, we can design a full-state feedback controller for system (4.4) as u_0 = -F_0 x - (F_1 + R(\varphi)A_1(\varphi^{(0\sim 1)}))\dot x, where F_{0\sim 1} \in \mathbb{R}^{r\times 2r} makes \Phi(F_{0\sim 1}) Hurwitz. The closed-loop system is given by \ddot x + F_1\dot x + F_0 x = 0."` `[E: Part 4, §4.2]`
2. **用观测值替换不可测状态并整理为标准四分块动态补偿器 $(K_{11},K_{12},K_{21},K_{22})$**：
   - `"Now, since q_2 = \dot x in (4.18) is unknown, let us substitute \dot x with \hat q_2, and get the following observer-based controller: u_0 = -F_0 y - (F_1 + R(\varphi)A_1(\varphi^{(0\sim 1)}))\hat q_2. Based on this idea, we further obtain the following result."` `[E: Part 4, §4.2]`
   - 标准输出反馈控制器形式：
     $$u(t) = -B^{-1}(\cdot, t)\bigl(f_y(\cdot, t) - u_0\bigr),\quad \begin{cases} u_0 = K_{11}(\cdot)y + K_{12}(\cdot)z, \\ \dot z = K_{21}(\cdot)y + K_{22}(\cdot)z. \end{cases}$$
3. **两类闭环稳定性证明模板**：
   - **定常分块上三角相似变换模板 `[E: Part 1, Lemma 2.1]`**：写出增广矩阵 $A_E$ $\to$ `"Define T = \begin{bmatrix}I_r&0&0\\0&I_r&0\\-L&-I_r&I_r\end{bmatrix}. It can be verified that T A_E T^{-1} = \begin{bmatrix}0&I_r&0\\-F_0&-F_1&-F_1\\0&0&L\end{bmatrix}. This gives \operatorname{eig}(A_E) = \operatorname{eig}(\Phi(F_{0\sim 1})) \cup \operatorname{eig}(L). Thus the conclusion follows."`
   - **时变/非线性级联 ISS 稳定性模板 `[E: Part 4, Theorem 3.2, Corollary 3.2, Theorem 4.1]`**：利用 $z = q_2 + L y - e$ 将闭环化为单向级联系统 $\dot x^{(0\sim 1)} = \Phi(F_{0\sim 1})x^{(0\sim 1)} + G(\cdot)e,\ \dot e = A_o(t)e$，验证耦合增益满足一致有界或次线性增长（sublinear growth），调用级联 ISS 引理得全局一致渐近（GUA）稳定。
4. **纯位置反馈与纯速度反馈对偶比较 `Remark` 原句 `[E: Part 4, Remark 7.1]`**：
   - `"By comparing the results in this section and Section 4, we can find the following differences between the two cases: 1. the position information automatically can ensure the observability of the velocity and the disturbance, but the velocity information cannot unless extra assumptions, namely, Assumptions A_{v1} and A_{v2}, are added; 2. once Assumptions A_{v1} and A_{v2} are met, the case of velocity feedback admits an LTI observation error equation, but the case of position feedback needs the observation error to obey an LTV system whose stability requires an extra assumption, namely, Assumption A_{p2}."`

### 1.4 输出依赖亚全驱系统（sub-OD-FAS）与增广初值 RoEA 刻画 `[E: OD-FAS Part 1, §4.1–4.2]`
- **静态输出反馈 RoEA**：利用状态转移矩阵 $\Xi_s(t,0)$ 与输出映射 $\Pi_s(t)=C(t)\Xi_s(t,0)$ 将 $\det B(y(t-\sigma_j(t))\vert_{j=1\sim q}, t)\neq 0$ 化为 $X_0\in\mathbb{R}^{nr}$ 的约束集 $\mathcal{R}$；
- **动态输出反馈增广 RoEA（极其关键的结构特征）`[E: Part 1, Theorem 4.2]`**：因动态补偿器状态 $z(t)\in\mathbb{R}^\nu$ 共同决定输出轨迹 $y(t, z_0, X_0) = C(t)[\,I_{nr}\ 0\,]\Xi_d(t,0)[X_0^\top\ z_0^\top]^\top$，**动态输出反馈的 RoEA 定义在增广初值空间 $[X_0^\top\ z_0^\top]^\top \in \mathbb{R}^{nr+\nu}$ 上**：
  > `"Theorem 4.2: Let (87) be a stabilizing controller for linear system (81). Then, under the feasibility condition [X_0^\top\ z_0^\top]^\top \in \mathcal{R}, the following output feedback controller ... makes sense and drives the closed-loop response [x^{(0\sim n-1)}(t)^\top\ z(t)^\top]^\top exponentially to zero."`
- **同胚逆向恢复说明原句 `[E: Part 1, §3.3.2; Part 4, Remark 8.1]`**：
  - `"Please note that once the state x^{(0\sim 3)} is obtained, the state of the original system (65) ... can be obtained through diffeomorphism (69). Furthermore, it follows from Lemma 3.3 that ... also converge to zero uniformly exponentially."`

---

## 2. UC-FAS 系列：受约束单向连接全驱系统（IJSS 2025 `Part I–III`）`[E]`

**来源**：`Part I. Models`（强/弱单向连接与多阶/严反馈连接建模）、`Part II. Sub-stabilisation`（内外可行集分解、三级级联亚镇定与非完整系统）、`Part III. Applications`（一般机动运动体 MMO 五类模型等价与 PVTOL 亚镇定）。

### 2.1 强/弱单向连接定义与建模动机原句 `[E: UC-FAS Part I, §1, Def. 4.1, Remark 4.1]`
- **引出动机**：`"In spite of the fact that numerous dynamical systems can be converted into FASs and their control can be more effectively solved by the FAS approach, there are still systems which cannot be converted into a single FAS or sub-FAS."` `[E: Part III, §1]`
- **强/弱单向连接定义（`Definition 4.1`）**：
  > `"Definition 4.1: The above system (8)–(11) is generally called a UC-FAS. It is also called a strongly (unidirectionally) connected FAS in its general form, and is called a weakly (unidirectionally) connected FAS if f_x(\cdot, t) = f_x(X_\dagger, t),\ f_y(\cdot, t) = f_y(X_\dagger, Y_\dagger, U_x^a, t),\ f_z(\cdot, t) = f_z(X_\dagger, Y_\dagger, Z_\dagger, U_x^b, U_y, t),"`（且 $B_x, B_y, B_z$ 具有同等单向依赖结构，其中 $U_x^a = u_x^{(0\sim\alpha_x^1)}$ 为上游控制输入及其导数栈）。
- **强连接转弱连接 `Remark 4.1`**：`"Let us point out that often a strongly UC-FAS can be converted into a weakly UC-FAS by certain control transformations."`

### 2.2 内外可行集（Internal & External Feasibility Sets）与内外 RoEA 分解 `[E: UC-FAS Part II, Defs. 2.1–2.2]`
当系统同时存在输入矩阵奇异性与状态—控制高阶导数联合约束 $[x^{(0\sim n-1)\top},\ u^{(0\sim\omega-1)\top}]^\top \in \mathbb{S}_s$ 时，采用标准双层分解：
- **定义原句（`Definition 2.1 & 2.2`）**：
  > `"Definition 2.1: Let \mathbb{F}^{\mathrm{in}} and \mathbb{F}^{\mathrm{ex}} be defined by (5) and (10), respectively. Then, the two sets \mathbb{F}^{\mathrm{in}} and \mathbb{F}^{\mathrm{ex}} are called the internal and external feasibility sets for the constrained FAS (1) and (2), respectively. Furthermore, the following set \mathbb{F} = \mathbb{F}^{\mathrm{in}} \cap \mathbb{F}^{\mathrm{ex}} is called the (overall) feasibility set."`
  > `"Definition 2.2: Let \mathcal{R}^{\mathrm{in}} and \mathcal{R}^{\mathrm{ex}} be defined by (13) and (14), respectively. Then, the two sets \mathcal{R}^{\mathrm{in}} and \mathcal{R}^{\mathrm{ex}} are called the internal and external RoEAs ... \mathcal{R} = \mathcal{R}^{\mathrm{in}} \cap \mathcal{R}^{\mathrm{ex}}."`

### 2.3 弱单向连接 UC-FAS 三步自然递推亚镇定结构（先分步推导、末段引出主定理）`[E: UC-FAS Part II, §3]`
- **总起过渡句**：`"The procedure is divided into three natural steps."`
1. **第一级子系统（`3.1. Sub-stabilising subsystem (22)`）**：
   - 写出内部可行集 $\mathbb{F}_x^{\mathrm{in}}$，在其上设计 $u_x = u_{x0}^{\mathrm{d}}(x^{(0\sim n_x-1)}, t) = -B_x^{-1}(\cdot)(A_{0\sim n_x-1}^x x^{(0\sim n_x-1)} + f_x(\cdot))$；
   - 写出闭环响应 $X_\dagger(X_{\dagger 0}, t) = \exp(\Phi(A_{0\sim n_x-1}^x)t)X_{\dagger 0}$ 及控制导数函数 $u_x^{(i)} = u_{xi}^{\mathrm{d}}(x^{(0\sim n_x-1)}, t)$；
   - 定义外部可行集 $\mathbb{F}_x^{\mathrm{ex}}$、总可行集 $\mathbb{F}_x = \mathbb{F}_x^{\mathrm{in}}\cap\mathbb{F}_x^{\mathrm{ex}}$ 与第一级吸引域 $\mathcal{R}_x$。
2. **第二级子系统（`3.2. Sub-stabilising subsystem (23)`）**：
   - 将 $X_\dagger(X_{\dagger 0}, t)$ 代入 $u_x$ 及其导数，记为初值与时间的显式函数 $u_x^{(i)} = \xi_i^x(X_{\dagger 0}, t)$；
   - 代入第二级子系统，得到**以上游初值 $X_{\dagger 0}\in\mathcal{R}_x$ 为参数**的时变 sub-FAS：
     $$y^{(n_y)} = \tilde f_y(y^{(0\sim n_y-1)}, X_{\dagger 0}, t) + \tilde B_y(y^{(0\sim n_y-1)}, X_{\dagger 0}, t)u_y;$$
   - 定义依赖 $X_{\dagger 0}\in\mathcal{R}_x$ 的 $\mathbb{F}_y^{\mathrm{in}}$、$\mathbb{F}_y^{\mathrm{ex}}$、$\mathbb{F}_y = \mathbb{F}_y^{\mathrm{in}}\cap\mathbb{F}_y^{\mathrm{ex}}$ 与 $\mathcal{R}_y$。
3. **第三级子系统与直和汇总定理（`3.3. Sub-stabilising subsystem (24)`）**：
   - 同理代入 $(X_{\dagger 0}, Y_{\dagger 0})$ 得第三级时变 sub-FAS、$\mathbb{F}_z$ 与 $\mathcal{R}_z$；
   - 定义直和集合 $\mathbb{F}_{xyz} = \mathbb{F}_x \oplus \mathbb{F}_y \oplus \mathbb{F}_z$，$\mathcal{R}_{xyz} = \mathcal{R}_x \oplus \mathcal{R}_y \oplus \mathcal{R}_z$，引出主定理：
   > `"Theorem 3.1: The UC-FAS (22)–(24) has a substabilising controller if \mathcal{R}_{xyz} is not empty, and in this case, the controller is given by (33), (43), and (52), with (X_{\dagger 0}, Y_{\dagger 0}, Z_{\dagger 0}) \in \mathcal{R}_{xyz}. Furthermore, the closed-loop system is composed of linear systems (34), (44) and (53), with responses satisfying (x^{(0\sim n_x-1)}(t), y^{(0\sim n_y-1)}(t), z^{(0\sim n_z-1)}(t)) \in \mathbb{F}_{xyz}."`
- **单侧过零约束化为实根半平面扇区引理 `[E: Part II, Lemma 4.1; Part III, Lemma 5.1]`**：对二阶过阻尼实特征根 $s_2 > s_1 > 0$（$s_1+s_2=b_1,\ s_1s_2=b_0$），轨迹永不触碰奇异面 $x_3(t)=0$（或推力通道 $u_1(t)\neq 0$）充要等价于线性半平面扇区 $\mathcal{R}_b^{\mathrm{ex}} = \{(x_{30}, x_{3d}) \mid x_{3d} + s_2 x_{30} > 0,\ x_{30} > 0\}$。
- **RoEA 覆盖性与坐标平移/预控制说明原句 `[E: Part II, §3.3; Part III, Remark 5.1]`**：
  - `"In the case that an initial value must be chosen from the complement of \mathcal{R}_{xyz}, often a coordinate translation can solve the problem ... Otherwise, a state regional transfer problem, which is usually easy to handle, needs to be solved to find a pre-controller to drive the trajectory into \mathcal{R}_{xyz}."`

---

## 3. IJSS 基础系列补全篇目：`Part VI`（抗扰与解耦）与 `Part X`（离散时间系统）`[E]`

### 3.1 `Part VI`：参数化扰动衰减（$H_2$ 优化）与动态扰动渐近解耦 `[E: IJSS 2021, Part VI]`
1. **HOFAS 天然抗扰特性 `Remark 2.1` 原句**：
   - `"It is clearly seen from (11) that some constant disturbances, slope disturbances, etc., may automatically disappear when the HOFA system method is used for design. Therefore, the HOFA system approach itself has certain 'natural' anti-disturbance characteristics."`
2. **$H_2$ 扰动衰减参数化优化三步结构（`§3.1–3.3 & §5.2`）**：
   - **Step 1（问题陈述 `Problem 3.1`）**：对确定性扰动模型 $x^{(n)} + A_{0\sim n-1}x^{(0\sim n-1)} = v + Ed$，求 $A_{0\sim n-1}$ 使闭环稳定且传递函数 $G_{dy}(s) = C(sI - \Phi(A_{0\sim n-1}))^{-1}B_c E$ 的 $\|G_{dy}(s)\|_2$ 最小；
   - **Step 2（广义 Sylvester 方程显式参数化 `Theorem 3.4` & `Theorem 3.5`）**：利用齐次 GSE 通解给出所有满足 $\Phi(A_{0\sim n-1}) = V F V^{-1}$ 的 $(V(Z,F), A_{0\sim n-1}(Z,F))$，进而由 Lyapunov 方程解析解导出 $\|G_{dy}(s)\|_2^2$ 关于自由参数 $(Z, F)$ 的闭式函数 $J(Z, F)$；
   - **Step 3（非奇异约束参数优化）**：求解 $\min J(Z, F)\ \text{s.t.}\ \det V(Z, F) \neq 0,\ a_i^{\min} \le a_i \le a_i^{\max}$。
3. **外系统动态扰动渐近解耦结构（`§4.1–4.3`）**：
   - 外系统扰动 $d^{(k)} = S_{0\sim k-1}d^{(0\sim k-1)}$，验证增广可检测性（`Theorem 4.4`：$(\Phi_E, C_I)$ 可观/可检 $\Longleftrightarrow$ $(\Phi(S_{0\sim k-1}), E)$ 可观/可检）；
   - 用非齐次 GSE 通解 $(\Pi, \Gamma) = (\Pi_0 + V, \Gamma_0 + W)$（`Lemma 4.2`）与右互质分解（RCF，`Theorem 4.5`）给出观测器增益 $(L_x, L_d)$ 及反馈矩阵的完整参数化通解（自由度由 $F_1, Z_1, Z_2$ 显式承载）。

### 3.2 `Part X`：离散时间高阶全驱系统基础与移位记号 `[E: IJSS 2022, Part X; Overview 2024, Eq. (7)]`
1. **前进步（Step-Forward）与后退步（Step-Backward）记号的严格区分（上下括号与分量排列顺序相反！）**：
   - **前进步算子（下取整括号 `floor`）** $x^{\lfloor i\rfloor}(k) = x(k+i)$，堆叠向量**从最高超前步往当前排**：
     $$x^{\lfloor 0\sim n\rfloor}(k) = \begin{bmatrix} x^\top(k+n) & \cdots & x^\top(k+1) & x^\top(k) \end{bmatrix}^\top;$$
   - **后退步算子（上取整括号 `ceiling`）** $x^{\lceil i\rceil}(k) = x(k-i)$，堆叠向量**从当前时刻往过去排**：
     $$x^{\lceil 0\sim n\rceil}(k) = \begin{bmatrix} x^\top(k) & x^\top(k-1) & \cdots & x^\top(k-n) \end{bmatrix}^\top.$$
2. **前进步与后退步模型的控制本质差异（`Definition 3.2` & `Remark 3.1–3.2`）**：
   - 前进步模型 $x(k+n) = \sum_{i=0}^{n-1}A_{n-i-1}x(k+i) + Bu(k)$ **本质上是含输入时滞的离散系统**；
   - 后退步模型 $x(k+1) = f(x^{\lceil 0\sim n-1\rceil}(k), k) + B(x^{\lceil 0\sim n-1\rceil}(k), k)u(k)$ 可直接由当前及历史状态因果求解 $u(k)$，获得定常线性闭环 $x(k+1) = A_{0\sim \varpi-1}x^{\lceil 0\sim\varpi-1\rceil}(k) + v(k)$。
3. **离散伴随矩阵与 Schur 镇定归约（`Remark 5.3`）**：
   - 离散伴随矩阵记为 $\Psi(A_{0\sim n-1}) = \Psi(0_{0\sim n-1}) + \Gamma_c A_{0\sim n-1}$，反馈增益设计归结为选取**Schur 稳定矩阵** $F$（特征值位于单位圆内）进行特征结构参数化配置；
   - 可行轨迹集定义在有界离散序列空间 $\mathbb{B}_N^\kappa$ 上（`Definition 4.1–4.2`）。

---

## 4. SCIS 三大双篇系列与 TCYB 时滞/非完整扩展系列 `[E]`

*注：段广仁一作在国内英文旗舰刊的三大双篇连载均发表于 **SCIENCE CHINA Information Sciences（SCIS，《中国科学：信息科学》英文版）**；在 **IEEE/CAA Journal of Automatica Sinica（JAS）** 上的相关论文（如 `Xu & Duan 2024`、`Zhang & Duan 2024`）均为合作者一作单篇。*

### 4.1 离散时滞系列（SCIS 2022 `Discrete-time delay systems: Part 1 & Part 2`）`[E]`
- **模型特征**：同时含时变状态时滞栈 $x^{\lceil\tau_{1\sim\zeta}(k)\rceil}(k)$ 与常值输入时滞 $u(k-h)$；当 $h>0$ 时，先通过状态一步递推预估未来 $h$ 步状态实现因果控制，使 $k>h$ 后闭环仍为无时滞常系数线性系统。
- **逐时刻可行点集与亚能控性定义（`Part 2, Defs. 1–4`）**：
  - `"Definition 1: A vector X \in \mathbb{R}^{\kappa(k)} is called a feasible point of system (27) at time k if it satisfies \det B(X, k) \neq 0\text{ or }\infty. Furthermore, the following set \mathbb{F}_k = \{X \mid \det B(X, k) \neq 0\text{ or }\infty\} is called the set of feasible points at time k ..."`
  - `"Definition 4: The dynamical system (64) is called completely controllable if it can be equivalently converted into a globally FAS ..., and is called sub-controllable if it can be equivalently converted into a sub-FAS ..."`

### 4.2 连续时滞系列（SCIS 2023 `Part 1` 状态时滞 & `Part 2` 输入时滞）与 Type I 时滞鲁棒镇定（TCYB 2023）`[E]`
1. **状态时滞 sub-FAS 包络球内估计证明结构（`SCIS 2023 Part 1, §6 Theorems 3–7`）**：
   - 控制律直接对消全部时变状态时滞非线性项，闭环化为 $\dot y = A_c y$；
   - 由 Lyapunov 方程 $A_c^\top P + P A_c = -I_n$（得 $\kappa = \sqrt{\|P\|\|P^{-1}\|}$）或特征结构谱分解求出瞬态包络常数 $\kappa > 0$，使 $\|T e^{A_c t}y(0)\| \le \kappa\|y(0)\|$；
   - 若球域 $B = \{z \mid \|z\| \le d\} \subset \mathbb{F}$，则初值球 $B_0 = \{y \mid \|y\| \le d/\kappa\}$ 保证全时域时滞状态 $T y(t-\sigma(t)) \in B \subset \mathbb{F},\ \forall t \ge 0$。
2. **输入时滞微分预估器（Predictor）两步证明结构（`SCIS 2023 Part 2, §4 Lemma 1 & Theorem 1`）**：
   - **Step 1（构造区间 $s\in[0,h]$ 预估器引理 `Lemma 1`）**：构造辅助微分系统 $\dot Z(s) = \Phi(0_{0\sim n-1})Z(s) + B_c[f(\cdot) + B(\cdot)u(s+t-h)],\ s\in[0,h]$，初值段取历史测量轨迹 $Z(\theta)=x^{(0\sim n-1)}(\theta+t),\ \theta\in[-\tau(t),0]$，由解的唯一性（`Assumption A3`）证明 $Z(s) = x^{(0\sim n-1)}(t+s)$；
   - **Step 2（超前对消主定理 `Theorem 1`）**：将预测值 $Z(h-\sigma_j(t+h))$ 与 $Z(h-\tau_j(t+h))$ 代入 $u(t) = -B^{-1}(Z(h-\sigma_j(t+h))\vert_{j=1\sim\gamma}, t+h)[f(Z(h-\tau_j(t+h))\vert_{j=1\sim\zeta}, t+h) + A_{0\sim n-1}Z(h) - v(t)]$，使 $t \ge h$ 时闭环精确化为 $x^{(n)}(t) + A_{0\sim n-1}x^{(0\sim n-1)}(t) = v(t-h)$。
3. **含不可控伴随动态（Type I 系统）鲁棒镇定结构（`TCYB 2023, §II–IV`）**：
   - 系统由高阶全驱受控子系统与不可控但自身 GUA 稳定的伴随子系统 $z^{(m)} = g(z^{(0\sim m-1)}, t)$ 组成，耦合项满足 $\mathcal{K}_\infty$-有界条件（`Definition 3`：$\|h(z)\| \le \kappa_h(\|z\|)$），仅对全驱通道设计鲁棒控制律实现全系统 GUA 镇定。

### 4.3 广义链式非完整系统系列（SCIS 2024 `Part 1` 不连续律 & `Part 2` 连续律）`[E]`
1. **标准前置命题（Brockett 阻碍判据 `Proposition 1`）**：先证明原非完整系统不存在光滑（或时不变连续）指数镇定控制律，交代引入不连续缩放或动态扩展的必要性。
2. **`Part 1` 不连续控制律“问题逐级等价转化”链（`§3–4`）**：
   - 设第一通道 $u_0 = -\beta x_0$（$x_0(0)\neq 0$，即 `Assumption X`：$x_0(t)=x_0(0)e^{-\beta t}$），引出 `Problem 1`；
   - `Theorem 1`：引入时变状态缩放变换 $z_i = x_{n-i+1}/x_0^{n-i}$，将链式系统等价化为严反馈系统（SFS），并用 `"According to the above Theorem 1, Problem 1 is clearly equivalently converted into the following one."` 引出 `Problem 2`；
   - `Theorem 2 & 3`：将 SFS 递推化为单阶 FAS/sub-FAS，双向验证变换的一一对应性（`one-to-one`）、保原点性与收敛等价性（`"For each z_{1\sim n}, Eq. (50) clearly gives a unique z^{(0\sim n-1)}. Conversely, let z^{(0\sim n-1)} be given; then we have ..."`）。
3. **`Part 2` 连续动态控制律“主导指数模态分离 + 可积衰减扰动”链（`§3–4`）**：
   - 将 $\dot x_0 = u_0$ 动态扩展为二阶常系数系统 $\ddot x_0 + a_1\dot x_0 + a_0 x_0 = 0$（两不等负实根 $-\alpha < -\beta < 0$），在初值非退化条件 `Assumption B`（$\eta_0 = \dot x_0(0) \neq -\alpha x_0(0)$）下分解出永不为零的主导指数项 $\sigma_0(t) = c_2 e^{-\beta t} \neq 0$ 与快衰减余项 $\omega(t) = (c_1/c_2)e^{-(\alpha-\beta)t}$；
   - 用无奇异缩放 $z_i = x_{n-i+1}/\sigma_0^{n-i}$ 将系统化为含指数衰减扰动 $\Delta f_i$（正比于 $e^{-(\alpha-\beta)t}$）的受扰 SFS/FAS；
   - 调用受扰系统可积增益引理（`Lemma 1 & Corollary 2`：验证 $\int_0^\infty \rho_\Delta(s)\mathrm{d}s < \infty$）完成全局一致指数稳定（UGE）证明。

---

## 5. 《自动化学报》中文奠基系列（`I–III`）与《航空学报》亚严反馈中文写作规范 `[E]`

**来源**：
- 段广仁，《高阶系统方法——I. 全驱系统与参数化设计》，《自动化学报》，2020，46(7): 1333–1345；
- 段广仁，《高阶系统方法——II. 能控性与全驱性》，《自动化学报》，2020，46(8): 1571–1581；
- 段广仁，《高阶系统方法——III. 能观性与观测器设计》，《自动化学报》，2020，46(9): 1885–1895；
- 段广仁，《亚严反馈系统镇定的全驱系统方法》，《航空学报》，2024，45(1): 629552。

### 5.1 中文正式环境命名与标准术语（撰写中文论文/博士开题报告必遵）`[E]`
- **中文正式环境名**：`定义 1`、`假设 A1`（或 `假设 1`）、`问题 PD` / `问题 ESA`、`引理 1`、`命题 1`、`定理 1`、`推论 1`、**`说明 1`**（注意：段广仁中文论文中 `Remark` 统一用 **`说明`** 而非“注”！证明以 `证明.` 开头，以 `$\Box$` 或 `证毕。` 收尾）。
- **已核实的中文权威术语 `[E]`**：
  - `高阶全驱系统`、`标准全驱系统`（$B\equiv I_n$）、`大范围全驱的（简称全驱的）`、`亚全驱系统`、`几乎全驱系统`；
  - `基础状态向量`、`奇异集`、`可行集`、`正常奇异函数`（$\varphi_0$）、`非正常奇异函数`（$\varphi_\infty$）、`奇异函数`（$\varphi$）；
  - `有理亚全驱系统`、`临界有理亚全驱系统`、`无理亚全驱系统`；
  - `亚稳定`、`亚镇定控制器`、`指数吸引域`、`预设控制律`（对应英文 `pre-controller`）；
  - `完全能控性`、`高阶全量测系统`、`完全能观性`、`串联系统`、`严反馈系统` / `亚严反馈系统`。
  - *（凡段广仁中文原文未出现的新概念，一律保留英文原词并标注 `[U]`，绝不自行生造中文译名。）*

### 5.2 中文各部分标准原句与结构模板 `[E]`
1. **引言评述一阶状态空间方法与高阶全驱优势 `[E: 自动化学报 I & II]`**：
   - `"一阶系统方法的一个最大问题是破坏了许多系统原有的全驱特性。"`
   - `"全驱特性允许我们对消掉开环系统的所有动态特性（无论是线性还是非线性的），同时建立全新的希望的闭环动态特性。即使在非线性系统的情况，也能给出一个希望的定常线性闭环系统。"`
   - `"并不建议在应用中先获得系统的一阶状态空间模型，然后再将其化为高阶全驱系统……可能的话，我们提倡在系统建模的过程中直接获得系统的高阶全驱模型。"`
2. **中文 `定义` 标准句式 `[E: 自动化学报 I 定义 1; 航空学报 2024 定义 3–8]`**：
   - `"定义 1. 给定系统 (8) 和上述集合 \Omega，如果 \det B(x,\dot x,\cdots,x^{(m-1)},t)\neq 0,\ t>0：1) 在 \Omega 上成立，则称系统 (8) 在 \Omega 上是全驱的；2) 只在 \Omega 上的某个超曲面上不成立，则称系统 (8) 在 \Omega 上是亚全驱的；3) 只在 \Omega 中的有限个点上不成立，则称系统 (8) 在 \Omega 上是几乎全驱的；4) 对于任何 x^{(i)}\in\mathbb{R}^n,\ i=0,1,\cdots,m-1 均成立，则称系统 (8) 是大范围全驱的，简称全驱的；特别地，当 B(\cdot)\equiv I_n 时，则称系统 (8) 是一个标准全驱系统。"`
   - `"定义 8. 考虑某具有 n 个状态变量的非线性系统 \Sigma 和一个非空集合 Q\subset\mathbb{R}^n。如果系统 \Sigma 从集合 Q 中出发的所有状态轨迹都以指数方式收敛到原点，那么集合 Q 就称为系统 \Sigma 的指数吸引域。"`
3. **中文控制器构造、`定理/命题` 与 `问题` 陈述句式 `[E: 自动化学报 I; 航空学报 2024]`**：
   - **问题归约**：`"问题归结为下述代数问题：问题 ESA. 对于任意选取的矩阵 F\in\mathbb{R}^{n_c\times n_c}，求取矩阵 V\in\mathbb{R}^{mn\times n_c} 和 K\in\mathbb{R}^{n\times mn} 使得 (A_{c0}+B_c K)V = E_c V F 且式 (53) 成立。"`
   - **全局全驱控制命题**：`"命题 1. 对于任何给定的定常矩阵 A_i,\ i=0,1,\cdots,m-1，都可以选取全驱系统 (8) 的下述控制律 [式] 获得如下的线性定常闭环系统 [式]。"`
   - **亚镇定主定理**：`"定理 2. 假设 1 成立，A_{0\sim n-1}\in\mathbb{R}^{r\times nr} 是保证 \Phi(A_{0\sim n-1}) 稳定的参数矩阵。那么，当 x^{(0\sim n-1)}\in\mathbb{F} 时，式 (39) 是亚全驱系统式 (20) 的一个亚镇定控制器，其对应的闭环系统为 [式]，对应的指数吸引域为 [式]，式中 \varphi(\cdot) 是亚全驱系统式 (20) 的奇异函数。"`
4. **中文亚镇定证明与 `说明` 标准模板 `[E: 航空学报 2024, §3.1]`**：
   - **证明模板**：`"证明. 基于前述分析，定理 2 的结论式 (41) 显然成立。为了证明对应的指数吸引域，首先将系统式 (41) 转化为如式 (43) 所示的状态空间形式：\dot x^{(0\sim n-1)}=\Phi(A_{0\sim n-1})x^{(0\sim n-1)}，其解为 x^{(0\sim n-1)}(t)=\mathrm{e}^{\Phi(A_{0\sim n-1})t}X_0。将式 (44) 代入矩阵 \breve B_n(x^{(0\sim n-1)},t)，可得如式 (45) 所示的可行性条件……上述约束可以转化为对系统初始值 X_0 的约束……因此 \breve R_a = \breve R_s。证毕。"`
   - **`说明` 模板**：`"说明. 由上述定理可见，当系统初值取自指数吸引域 \breve R_s 时，亚全驱系统式 (20) 在所设计的亚镇定控制器驱动下的闭环系统响应便指数收敛到原点。一般说来，问题的指数吸引域都是比较大的，能够满足实际应用问题的需要。如果一定要将初值取在指数吸引域之外，可以设计一个预设控制律，先将系统的响应驱动到指数吸引域内，然后再由所设计的亚镇定控制律接管。"`

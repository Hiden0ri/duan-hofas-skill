# Duan 证明结构标准模板库（基于 32 篇一作论文 + *Volume I* 全量分拣）

本文件对本地全集语料库中的 **408 条正式结论**（190 `Theorem`、79 `Lemma`、74 `Proposition`、65 `Corollary`）及其全部 **117 个显式 `Proof` 块**（分类原文见 `corpus/sorted/proofs.md`）与 **~290 处定理前构造性推导**进行全量分拣与冲突核查后提炼而成。

---

## 0. 证明组织方式与首尾句式的真实语料规律 `[E]`

### 0.1 三种合法的证明位置（纠正“每个定理后必跟 `Proof.`”的单一假设）
1. **模式 M1——先分步构造推导、末段直接引出定理（占构造性控制定理约 60%）`[E]`**：
   - 在全局全驱控制、高阶反步法（`Part III` §4；*Volume I* §9.2）、UC-FAS 三级级联亚镇定（`UC-FAS Part II` §3）、OD-FAS 观测器替换（`OD-FAS Part 4` §4.2）等章节，段广仁先在正文中按自然步骤推完变换、控制律与闭环/Lyapunov 不等式，最后用一句总结语直接引出 `Theorem`/`Corollary`，**定理后不再重复写 `Proof.`**：
     - `"Based on the above analysis, we can immediately give the following result."` `[E: SCIS Delay 2]`
     - `"The above process clearly proves the following result."` `[E: Part III §4; Volume I §9.2]`
     - `"Applying Proposition 2.1 and Lemma 2.1 to the above system (11), immediately produces the following result."` `[E: OD-FAS Part 1]`
2. **模式 M2——定理/引理后紧接内联 `Proof`（117 处中的主体）`[E]`**：
   - 开头格式随期刊排版而定：IEEE / SCIS 用 `Proof.`，Taylor & Francis（IJSS）用 `Proof:`，Springer（JSSC / *Volume I*）用无标点粗体 `Proof `，中文刊用 `证明.`。
   - **首句铁律**：单结论证明直接进入变换、代入或引用前式（如 `"Substituting the control law (14) into system (2), gives ..."`、`"In view of (10), we have ..."`），**绝不写 `"We first show that ..."` 之类空洞预告**。
3. **模式 M3——长代数/观测器推导移入附录（Appendix Deferred Proof）`[E]`**：
   - 当等价消元、参数化或降阶观测器误差推导超过 1 页时（如 `Part X` Appendix、`SCIS Delay 1` Appendix A、`OD-FAS Part 1` §9 `9.1. Proof of Proposition 3.3`、*Volume I* Appendix B），正文写 `"For a proof of the above proposition, one can refer to the appendix."`，附录中按小节标题 `Proof of Theorem X.Y` 分步展开。

### 0.2 证明收尾方式统计（117 个显式 `Proof` 块核查结果 `[E]`）
- **直接以最终推导式或结论句 + 证毕符号（`□`/`■`）收尾：98 / 117（83.8%，绝对主流！）**：
  - 例：`"This gives (157)."`、`"This proves R_a = R_s."`、`"Therefore, system (163) is GUA stable."`——无需每段证明强加英文套话收尾！
- **使用显式英文/中文收尾句：19 / 117（16.2%，用于特定证明类型）**：
  - 反证法固定收尾：`"This yields a contradiction. Thus [...]. The proof is finished."` `[E: Duan & Zhou 2022 Lemma 4.4]`；
  - 较长分步/鲁棒证明收尾：`"The proof is (then) completed."` / `"Then the proof is completed."`（5 处，`Part III`, `Part VI`, `Chained 1`）或 `"This completes the proof."`（`Duan & Wang 2026`）；
  - 简短推论/特征值分离收尾：`"Thus the conclusion follows."`（4 处，`OD-FAS Part 1 & Part 4`）；
  - 充要性证明收尾：`"Combining the above two aspects gives the complete proof of the result."` `[E: Duan 2023 Prop. 2]`；
  - 中文证明收尾：`证毕。`（《航空学报》）或 `注意到上述过程的可逆性，可得定理结论. \Box`（《自动化学报》）。

---

## 1. 十二类标准证明执行模板（`PT-1` 至 `PT-12`）

### PT-1：直接代入 + 状态空间转换（Nominal Global HOFAS）`[E]`
1. 核验所声明定义域上 $\det B(\cdot, t)\neq 0$（或 $\neq 0\text{ or }\infty$），保证 $B^{-1}$ 良定。
2. 代入起手句：`"Substituting the control law (x) into system (y), gives the following closed-loop system:"` $x^{(n)} + A_{0\sim n-1}x^{(0\sim n-1)} = v$（核对括号内外正负号！）。
3. 转状态空间句（**一律写 `state-space form`，不写 `first-order form`**）：`"The closed-loop system (z) is equivalent to the following state-space form:"` $\dot x^{(0\sim n-1)} = \Phi(A_{0\sim n-1})x^{(0\sim n-1)} + B_c v$。
4. 由 $\Phi(A_{0\sim n-1})$ 为 Hurwitz（离散情形 $\Psi(A_{0\sim n-1})$ 为 Schur）或特征结构关系 $\Phi(A_{0\sim n-1}) = V F V^{-1}$ 直接得出指数稳定、解耦或跟踪结论。

### PT-2：Lyapunov 导数 + 配方法有界椭球证明（Robust / Adaptive HOFAS）`[E: Part III Theorem 3.5; Part V]`
1. 代入鲁棒/自适应控制律得含不确定项 $\Delta f$ 与补偿项 $u^*$ 的高阶闭环及状态空间形式。
2. 引用谱裕度引理：`"Since A_i, i=0,1,\ldots,n-1, satisfy condition (9), there exists a positive definite matrix P(A_{0\sim n-1}) satisfying (10). Then the following Lyapunov function can be chosen: V = \frac{1}{2}(x^{(0\sim n-1)})^\top P x^{(0\sim n-1)}."`（自适应情形加参数误差二次项 $\frac{1}{2\gamma}\tilde\theta^\top\tilde\theta$）。
3. 求导放缩：`"In view of (10), (12) and (17), we have \dot V \le -\frac{\mu}{2}V + \|P_L^\top x^{(0\sim n-1)}\|\rho(\cdot) - \frac{1}{4\varepsilon}\rho^2(\cdot)\|P_L^\top x^{(0\sim n-1)}\|^2 \le -\frac{\mu}{2}V + \varepsilon"`（调用配方法引理 $a - a^2/(4\varepsilon) \le \varepsilon$）。
4. 由比较原理或 $\dot V < 0$（椭球外部）导出全局一致最终有界并收敛至椭球集 $\Theta_{\mu,\varepsilon}$。

### PT-3：sub-FAS 亚镇定与 ROEA 精确刻画证明 `[E: Duan 2023 TCYB, Theorem 1]`
1. 对分条定理先处理显然项：`"Proof: The first two conclusions are obvious. To show the third condition, we first convert system (32) into the following state-space form: \dot x^{(0\sim n-1)} = \Phi(A_{0\sim n-1})x^{(0\sim n-1)}, whose solution is clearly given by x^{(0\sim n-1)}(t) = \mathrm{e}^{\Phi(A_{0\sim n-1})t}X_0, where X_0 = x^{(0\sim n-1)}(0) is the initial value."`
2. 代入可行性条件：`"Substituting (33) into the matrix B(\cdot), gives the following feasibility conditions: \det B(T\mathrm{e}^{\Phi(A_{0\sim n-1})t}X_0, t) \neq 0\text{ or }\infty,\ t \ge 0. These are obviously constraints on the system initial value X_0."`
3. 改写为奇异函数零集：`"Further, by definitions of normal and abnormal singularity functions, the above feasibility conditions can be written into \varphi(\mathrm{e}^{\Phi(A_{0\sim n-1})t}X_0, t)\neq 0,\ t\ge 0, which is clearly equivalent to (36). This proves R_a = R_s."`

### PT-4：反证法标准证明（Proof by Contradiction）`[E: Duan & Zhou 2022, Lemma 4.4]`
1. **直接反设起手**（严禁写 `"We prove by contradiction"` 或 `"Suppose, on the contrary"`）：`"Suppose that [结论的否定]."`
2. 正向推导存在性对象：`"Then it follows from (x) that [展示式]. Therefore, there exists [对象] such that [展示式], which means that [性质 A]."`
3. 引出对立面：`"On the other side, it follows from [前提/原系统方程] that [展示式], which implies / means that [非 A]."`
4. **固定三句收尾**：`"This yields a contradiction. Thus [原结论]. The proof is finished."`

### PT-5：高阶反步法五步构造与叠缩证明（High-Order Backstepping）`[E: Part III §4; Volume I §9.2]`
1. **Preparations**：选取满足 $\operatorname{Re}\lambda_k(\Phi(A_i^{0\sim m_i-1}))\le -\mu/2$ 的矩阵组及 Lyapunov 矩阵 $P_i=[P_{iF}\ P_{iL}]$，定义反单位阵置换矩阵 $\tilde P_i = \mathring{I}P_i$ 及其逆分块，声明 `"all the variables defined above are independent of system (...) and can all be easily obtained beforehand."`
2. **The First Step**：设 $z_1^{(0\sim m_1-1)}=x_1^{(0\sim m_1-1)}$，引入高阶误差变换 $\tilde P_2 z_2^{(0\sim m_2-1)} = x_2^{(0\sim m_2-1)} - [\alpha_1^\top\ 0]^\top$，设计 $\alpha_1$ 得第一级闭环 $z_1^{(m_1)} + A_1^{0\sim m_1-1}z_1^{(0\sim m_1-1)} = \varphi_1 + w_1$。
3. **The $k$-th Step**：对 $\alpha_{k-1}$ 仅求 $m_k-1$ 阶导并分离确定项与不确定项 $h_{k-1}+\Delta h_{k-1}$，引入 $\tilde P_{k+1}z_{k+1}^{(0\sim m_{k+1}-1)}$，在 $\alpha_k$ 中加入层间耦合抵消项 $+v_{k-1}$（$v_{k-1}=L_{k-1}^\top P_{k-1,L}z_{k-1}^{(0\sim m_{k-1}-1)}$），得 $z_k^{(m_k)} + A_k^{0\sim m_k-1}z_k^{(0\sim m_k-1)} = \varphi_k + w_k - v_{k-1}$。
4. **The $n$-th Step**：设计实际控制律 $u$（含 $+v_{n-1}$），得末级闭环 $z_n^{(m_n)} + A_n^{0\sim m_n-1}z_n^{(0\sim m_n-1)} = \varphi_n - v_{n-1}$。
5. **The Conclusion**：取总 Lyapunov 函数 $V = \sum_{i=1}^n (z_i^{(0\sim m_i-1)})^\top P_i z_i^{(0\sim m_i-1)}$，利用恒等式 $(z_i)^\top P_{iL}w_i = (z_{i+1})^\top P_{i+1,L}v_i$ 逐项相消：`"Adding the equations in (...) side by side, and using (...), give \dot V \le -\mu V + n\varepsilon. The above process clearly proves the following result."`（紧接主定理）。

### PT-6：双向同胚等价消元与数学归纳法证明 `[E: Part II; Chained Part 1 Theorem 3; Volume I Ch. 7–8]`
1. 归纳起手句：`"We prove the theorem via the n-step induction. Step 1: ..."` 或 `"We use mathematical induction to prove this result."`
2. **必须双向验证**：
   - 正向（`one-to-one` 正推）：`"For each z_{1\sim n}, Eq. (50) clearly gives a unique z^{(0\sim n-1)}."`
   - 逆向（消元变量显式恢复）：`"Conversely, let z^{(0\sim n-1)} be given; then we have z_1 = z,\ z_2 = B_1^{-1}(\cdot)[\dot z - f_1(\cdot)], \ldots"`，并验证零平衡点不动与收敛等价传递。

### PT-7：充要条件（Sufficiency & Necessity）证明 `[E: Duan 2023 TCYB, Proposition 2]`
- 分段标明 `"Sufficiency: ..."` 与 `"Necessity: ..."`，末句汇总：`"Combining the above two aspects gives the complete proof of the result."`

### PT-8：多结论逐条证明与多步骤长证明 `[E: Delay 1 Theorem 3; Volume I Appendix B]`
- 多结论按陈述顺序逐一证完：`"Proof of conclusion (1). ... Proof of conclusion (2). ..."` 或 `"The first conclusion is then proven. It remains to show that ..."`。
- 长证明在段首仅交代步骤骨架：`"The proof is composed of four steps. Step 1. ... Step 2. ..."`。

### PT-9：ROEA 单调区间分割与有限驻点约化证明 `[E: Duan & Wang 2026, Theorem 1]`
1. 按指数基函数驻点将 $[0,+\infty)$ 划分为有限个单调子区间 $[t_{i-1}, t_i)$；
2. 在每个子区间上求 $g'(t, X_0)$，证明至多存在唯一内驻点 $t^*$；
3. `"Therefore, the maximum of g(t, x, y) over [t_{i-1}, t_i) can only be attained either at the endpoints t_{i-1} and t_i, or at the unique interior stationary point t^*, if it exists."` 分 `Case 1–4` 化为有限代数不等式交集。

### PT-10：OD-FAS 降阶观测器 + 分块上三角 / 级联 ISS 输出反馈证明 `[E: OD-FAS Part 1 & Part 4]`
1. **观测器证明**：写出形式上含 $\dot y$ 的全阶观测器 $\to$ 令 $z = \hat q_2 + L(\varphi^{(0\sim 1)})y$ 消去 $\dot y$ $\to$ 证得 $\dot e = A_{o1}e$（或 $\dot e = R_E(\varphi)A_L R_E^{-1}(\varphi)e$）。
2. **闭环稳定性证明**：
   - 定常情形：构造非奇异分块矩阵 $T$ 使 $T A_E T^{-1}$ 为分块上三角矩阵，直接给出 $\operatorname{eig}(A_E) = \operatorname{eig}(\Phi(F_{0\sim 1}))\cup\operatorname{eig}(L)$；
   - 时变/非线性情形：代入 $z = q_2 + L y - e$ 化为单向级联系统 $\dot x^{(0\sim 1)} = \Phi(F_{0\sim 1})x^{(0\sim 1)} + G(\cdot)e,\ \dot e = A_o(t)e$，验证 $G(\cdot)$ 一致有界或次线性增长，调用级联 ISS 定理证得 GUA 稳定；
   - sub-OD-FAS 情形：将输出轨迹表示为增广初值 $[X_0^\top\ z_0^\top]^\top\in\mathbb{R}^{nr+\nu}$ 的函数刻画增广 RoEA。

### PT-11：受约束 UC-FAS 内外可行集与三级级联亚镇定证明 `[E: UC-FAS Part II, §3]`
1. 总起句 `"The procedure is divided into three natural steps."`；
2. 对第 1 级求 $\mathbb{F}_x = \mathbb{F}_x^{\mathrm{in}}\cap\mathbb{F}_x^{\mathrm{ex}}$、闭环指数解 $X_\dagger(X_{\dagger 0}, t)$、控制高阶导数 $u_x^{(i)} = \xi_i^x(X_{\dagger 0}, t)$ 及 $\mathcal{R}_x$；
3. 将 $(X_\dagger, \xi_i^x)$ 代入下游子系统构造以 $X_{\dagger 0}\in\mathcal{R}_x$ 为外参的时变 sub-FAS，递推定义 $\mathbb{F}_y, \mathcal{R}_y, \mathbb{F}_z, \mathcal{R}_z$，取直和 $\mathcal{R}_{xyz} = \mathcal{R}_x \oplus \mathcal{R}_y \oplus \mathcal{R}_z$，在推导末尾引出主定理。

### PT-12：时滞预测器与广义链式系统缩放/受扰证明 `[E: SCIS 2023 Delay 2; SCIS 2024 Chained 1–2]`
- **输入时滞预测器**：在 $s\in[0,h]$ 上由初值历史与唯一解假设证 $Z(s) = x^{(0\sim n-1)}(t+s)$，代入超前对消律使 $t\ge h$ 后闭环化为常系数线性系统。
- **广义链式非完整系统**：先由 Brockett 必要条件证光滑律不存在（`Prop. 1`）；不连续分支用 $x_0(t)=x_0(0)\mathrm{e}^{-\beta t}\neq 0$ 做 $z_i=x_{n-i+1}/x_0^{n-i}$ 缩放转 SFS/FAS；连续分支将 $x_0$-通道升为二阶系统提取非零主导实模态 $\sigma_0(t)=c_2\mathrm{e}^{-\beta t}\neq 0$，缩放后利用可积指数衰减扰动 $\int_0^\infty \rho_\Delta(s)\mathrm{d}s < \infty$ 证 UGE 稳定。

---

## 2. 用户切换 sub-FAS 相对裕度扩展证明链 `[D: main_v2.tex]`

1. 声明指标集 $\mathcal{P}=\{1,2,\ldots,N\}$ 与 `the ith subsystem`，按 `Duan 2023` 定义 $\mathcal{S}_i,\mathcal{F}_i,\varphi_i$ `[E]`，单列 `Assumption 1`（$\varphi_i$ 在 $\mathbb{R}^{nr}$ 上固定且连续 `[D]`）。
2. 在 $\mathcal{F}_i$ 上先构造子系统控制器 $u_i$，再代入得公共常系数线性闭环 $x^{(n)}+A_{0\sim n-1}x^{(0\sim n-1)}=0$，构造基于 $|\varphi_i(X)|$ 与 $\gamma\max_j|\varphi_j(X)|$ 的滞环保持/切换集 $\Omega_i,\widetilde\Omega_i$ 及切换律 $\kappa^*$ `[D]`。
3. **Lemma 1 `[D]`**：在 $[0,T)$ 极限落入 $\mathcal{F}_{\mathrm{ext}}$ 前提下，用紧集 $K_T$ 上一致连续性反证有限切换次数并唯一延拓过 $T$。
4. **Theorem 1 `[D]`**：证全时域可行、公共状态空间响应 $\mathrm{e}^{\Phi(A_{0\sim n-1})t}X_0$ 指数收敛、原点邻域包含及扩展 ROEA 精确刻画 $\mathcal{R}_{\kappa^*} = \{X_0 \mid \mathrm{e}^{\Phi(A_{0\sim n-1})t}X_0\in\mathcal{F}_{\mathrm{ext}},\ \forall t\ge 0\}$。
5. **Proposition 1 & Corollary 1 `[D]`**：套 `PT-4` 反证模板证与增益无关的严格扩大 $X_0\in\mathcal{R}_{\kappa^*}\setminus\bigcup_{i\in\mathcal{P}}\mathcal{R}_i(A_{0\sim n-1})$，并在紧集 $K_\infty$ 上证 $[0,\infty)$ 总切换次数有限、排除 Zeno 行为。

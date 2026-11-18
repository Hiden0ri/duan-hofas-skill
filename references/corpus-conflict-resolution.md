# Duan 全集语料库跨篇冲突核查与统一裁定指南（984 条环境/证明分拣复核）

在对全部 **32 篇本地段广仁一作中英文论文 + 2026 专著 *Volume I***（合计 **867 个正式环境 + 117 个显式 `Proof` 块**，分拣结果存于 `corpus/sorted/*.md` 与 `corpus/sorted/summary_stats.json`）做横向比对时，段广仁本人从 2020 年至 2026 年不同系列/不同出版社论文之间，以及旧版技能归纳与全量统计之间，存在 **10 处真实差异或潜在冲突**。本文件逐条给出全库实证数据与统一裁定准则，供**核查原文（Check）**与**起草新稿（Draft/Polish）**时严格区分。

---

## 冲突 1：定义符号 `:=` vs `\triangleq`（`≜`）vs `=`

- **全库实证统计 `[E]`**：
  - `:=` 在 32 篇段广仁一作论文中出现次数为 **`0 / 32`（零次！）**；
  - `\triangleq`（`≜`）在 **24 / 32** 篇一作论文的正文局部缩写/集合定义中使用（如 `Overview 2024` Theorem 7 `X_0 \triangleq x^{(0\sim n-1)}(0)`、`OD-FAS Part 1`）；
  - 普通等号 `=` 在全部论文的引言 `Notations:` 段及另外 8 篇论文的正文定义中使用（如 `Duan 2023 TCYB` `X_0 = x^{(0\sim n-1)}(0)`）。
- **裁定准则**：
  1. **引言末尾 `Notations:` 段**：一律只用 `=`（配不编号 `equation*`），严禁用 `:=` 或 `\triangleq`；
  2. **正文局部定义**：纯 Duan 一作风格优先用 `=` 或 `\triangleq`；`:=` 仅在合作者一作论文（如 `Yang & Duan 2026` 切换系统 `\mathcal{P}:=\{1,\ldots,N\}`）中出现，不能把 `:=` 称为 Duan 个人习惯。

## 冲突 2：定理开头句式（`Suppose` 唯一论 vs `Let` 主导）与控制律内联 vs 编号引用

- **冲突来源**：旧版 `theorem-writing-template.md` 仅以 `IJSS Part III` Theorem 3.5 为单一样本，将 `"Suppose that system (x) satisfies ..."` 及“定理内必须完整展开控制律公式”当作唯一标准。
- **全库 190 个 `Theorem` 实证统计 `[E]`**：
  - 开头句式：**`Let ...` 占 121/190（63.7%）**，`Suppose / Assume ...` 仅占 23/190（12.1%），直接主语陈述 + `if / if and only if` 占 14/190（7.4%）；2023–2026 年最常用开头为 `"Let Assumptions A1–A2 be met / satisfied, and F_{0\sim n-1}\in\mathbb{R}^{r\times nr} be a matrix making \Phi(F_{0\sim n-1}) Hurwitz. Then ..."`；
  - 控制律位置：**引用前文编号公式（62 处，如 `given by (30)`）**与**定理内直接展开控制律（53 处）**并存。
- **裁定准则**：两种开头与两种控制律呈现均属纯正 `[E]`；若定理前已在小节内逐步构造出控制律并编号，定理内直接写 `is given by (x)` 更紧凑；绝不将编号引用误判为“定理要素缺失”。

## 冲突 3：证明位置（定理前推导 vs 定理后 `Proof` vs 附录）与证明收尾语

- **冲突来源**：容易误以为每个定理后都必须紧跟 `Proof.` 且结尾必写 `"The proof is finished."`。
- **全库 408 条正式结论与 117 个显式 `Proof` 块实证统计 `[E]`**：
  - **约 60% 的构造性控制定理无定理后 `Proof` 块**：段广仁习惯先在正文中完成分步构造与 Lyapunov 叠缩，再用 `"Based on the above analysis, we immediately have the following result."` / `"The above process clearly proves the following result."` 引出定理；超长推导则移入附录（`Proof of Proposition 3.3`）；
  - **证明开头排版**：IEEE / SCIS 用 `Proof.`，IJSS 用 `Proof:`，Springer（JSSC / *Volume I*）用无标点粗体 `Proof `，中文刊用 `证明.`；
  - **证明收尾统计**：**98 / 117（83.8%）直接停在最终推导式或结论句 + `□`/`■`**（无套话收尾句）；显式收尾句仅占 16.2%（其中反证法经典收尾为 `"The proof is finished."`，长分步证明常用 `"The proof is (then) completed."`，短特征值分离常用 `"Thus the conclusion follows."`，中文用 `证毕。`）。
- **裁定准则**：不强行给每段短证明硬塞收尾套话；反证法严格沿用 `Duan & Zhou 2022` 的 `"This yields a contradiction. Thus ... The proof is finished."`，同一篇稿件内部收尾风格保持统一。

## 冲突 4：分条序号格式 `1)` vs `(1)` vs `1.`

- **全库实证统计 `[E]`**：分条标号完全服从目标期刊体例——IEEE 期刊（`TCYB 2023`, `Overview 2024`）与 `Part X` / `DiscDelay` 用 `1), 2), 3)`；Taylor & Francis（`IJSS` 各篇、`UC-FAS 2025`、`OD-FAS Part 1`）与 `SCIS` 多用 `(1), (2), (3)`；`OD-FAS Part 4` 与 *Volume I* 用 `1., 2., 3.`。
- **裁定准则**：投 IEEE 期刊统一用 `1), 2), 3)`，投 IJSS / SCIS 统一用 `(1), (2), (3)`，单篇稿件内严禁混用。

## 冲突 5：参数矩阵栈上下标 `A^{0\sim n-1}` vs `A_{0\sim n-1}` 及控制律括号内正负号

- **全库实证统计 `[E]`**：
  - `IJSS Part II–V`（2021）及 *Volume I* 第 5、9、10 章（高阶反步法中下标 $i$ 已被子系统层号占用时）写上标 **`A^{0\sim n-1}` / `A_i^{0\sim m_i-1}`**；其余大部分论文（`Part I, VI–X`, `Duan 2023`, `Overview 2024`, `UC-FAS 2025`, `OD-FAS 2026`）写下标 **`A_{0\sim n-1}`**（多通道用 $A_{k,0\sim\mu_k-1}$ 或 $A_{0\sim n_x-1}^x$）；
  - 控制律括号内符号存在分支差异：常规镇定写 $u = -B^{-1}[f + A_{0\sim n-1}x^{(0\sim n-1)} - v] \implies x^{(n)}+A_{0\sim n-1}x^{(0\sim n-1)}=v$；而 **OD-FAS 输出抵消变换**写 $u = -B^{-1}[f_y - u_0] \implies x^{(n)} = f_x + u_0$；**离散时间后退步 `Part X`** 写 $u(k) = B^{-1}[-f + A_{0\sim\varpi-1}x^{\lceil 0\sim\varpi-1\rceil}(k) + v(k)] \implies x(k+1) = A_{0\sim\varpi-1}x^{\lceil 0\sim\varpi-1\rceil}(k) + v(k)$。
- **裁定准则**：单阶系统默认优先用下标 `A_{0\sim n-1}`（若子系统下标占用了 $i$，内部哑指标改用 $j=0,1,\ldots,n-1$）；每次引用控制律必须现场代入验算闭环正负号，严禁跨分支盲抄符号。

## 冲突 6：全驱非奇异条件 `\det B \ne 0` vs `\det B \ne 0 \text{ or } \infty`

- **全库实证统计 `[E]`**：
  - 全域光滑/多项式模型（`0-type`，无极点发散）只写 `\det B(\cdot)\ne 0`（如 `IJSS Part I` Def. 2.2、`OD-FAS Part 1` Def. 2.1–2.2）；
  - 允许分式有理项或极点发散的一般亚全驱/输出驱动模型写 `\det B(\cdot)\ne 0\text{ or }\infty`（对应奇异集 `\det B(\cdot)=0\text{ or }\infty`，如 `Duan 2023 TCYB` Def. 1–2、`Overview 2024` Def. 2、`SCIS Chained`、`OD-FAS Part 4` Def. 2.2）。
- **裁定准则**：若模型 $B(\cdot)$ 在考察域内处处连续有限（如多项式或光滑函数），写 `\det B(\cdot)\ne 0` 更精确；若包含分式有理函数或一般亚全驱定义，保留 `or \infty`；在引用原定义时严格照搬原论文写法，不擅自增删 `or \infty`。

## 冲突 7：缩写与术语演化（`ROEA` / `feasible set` vs `RoEA` / `feasibility set`）及英美拼写

- **全库实证统计 `[E]`**：
  - **吸引椭球缩写**：`Duan 2023 TCYB` 与 `SCIS Chained 1 (2024)` 全大写写 **`ROEA`**（*region of ellipsoid attraction*）；`Overview 2024`、`UC-FAS Part I–III (2025)`、`Duan & Wang 2026`、`OD-FAS Part 4 (2026)` 改为大小写混合 **`RoEA`**；
  - **可行集/奇异集命名**：`Duan 2023 TCYB`、`Overview 2024`、`UC-FAS` 写 **`feasible set`** / **`singular set`**；`OD-FAS Part 1 & Part 4 (2026)` 与 *Volume I* 部分章节写 **`set of feasibility` / `feasibility set`** 与 **`set of singularity` / `singularity set`**；
  - **英美拼写**：投 IEEE 期刊（`TCYB`, `Overview`）用美式 `-ize/-izing`（`stabilizing`, `utilizing`）；投英国 Taylor & Francis 期刊（`IJSS`, `UC-FAS`, `OD-FAS`）由编辑部统一排为英式 `-ise/-ising`（`stabilising`, `utilising`, `parametrisation`）。
- **裁定准则**：以上成对写法均属 `[E]` 原文正统；投 IEEE 期刊统一采用 `ROEA` + `feasible set` + 美式 `-izing`（与 `Duan 2023 TCYB` 完全对齐），投 IJSS 统一采用英式拼写，单篇稿件内严禁混写。

## 冲突 8：闭环矩阵稳定性谓词 `Hurwitz` vs `stable` vs `Schur`

- **全库实证统计 `[E]`**：
  - 连续时间论文中，**20 / 32 篇**（含 `IJSS Part I–IX`, `Overview 2024`, `UC-FAS 2025`, `OD-FAS 2026`）写 **`"makes \Phi(A_{0\sim n-1}) Hurwitz"`** 或 `"is a Hurwitz matrix"`；而 `Duan 2023 TCYB`（Thm. 1–4）与中文 `AAAS 2024`（“使得 $\Phi(A_{0\sim n-1})$ 稳定”）写 **`"makes \Phi(A_{0\sim n-1}) stable"`**；
  - 离散时间论文（`IJSS Part X`, `SCIS DiscDelay 1–3`）统一写 **`"makes \Psi(A_{0\sim\varpi-1}) Schur"`**（或 `"all the eigenvalues of \Psi(\cdot) lie inside the unit circle"`）。
- **裁定准则**：核查原文时承认 `stable`（连续时间矩阵语境下指 Hurwitz）为 `[E]`；起草新英文稿件时，**连续时间统一推荐写 `Hurwitz`、离散时间统一写 `Schur`**，彻底消除 Lyapunov 临界稳定与渐近稳定之间的歧义。

## 冲突 9：`Assumption`（155 处）vs `Condition`（10 处）的职能边界

- **全库实证统计 `[E]`**：全库 165 条前置条件中 **`Assumption` 占 155 处（93.9%）**，编号为 `Assumption 1` 或分节/前缀编号 `Assumption 2.1` / `Assumption A1`；`Condition` 仅出现 **10 处（6.1%）**，专用于在已有 `Assumption A1` 之外单独剥离一条“参数不确定性范数界”（`IJSS Part V` Condition 1）或“线性辅助镇定/可检测条件”（`SCIS Chained 2` Condition 1、`UC-FAS Part I` Condition 1）。**可行集与奇异集在全库中 100% 归入 `Definition`，从不放进 `Assumption`。**
- **裁定准则**：新稿默认一律用 `Assumption`；仅当需要区分“物理对象固有假设”与“设计者附加检验条件”时才启用 `Condition`；集合定义一律用 `Definition`。

## 冲突 10：$f, B$ 正则性声明随目标变化，以及极少数极简命题写法 vs 目的写进陈述铁律

- **全库实证统计 `[E]`**：
  - **非线性项正则性按证明所需精确声明**：纯代数相消的 ROEA 镇定（`Duan 2023 TCYB` §III-A）不额外声明光滑性；需要 Carathéodory / 局部解存在性的篇目（`Overview 2024`, `UC-FAS 2025`, `Duan & Wang 2026`, `OD-FAS 2026`）写 **`piecewise continuous`**（或 locally Lipschitz）；需要求导升阶或高阶反步法的篇目（`IJSS Part III–V`, `JSSC SFS`）写 **`sufficiently differentiable`** 或 **`smooth ($C^m$)`**。**严禁往 `Duan 2023` 原话里强读出他没写的连续/光滑假设！**
  - **命题陈述详略**：全库 >98% 的定理/命题在陈述句内写明具体目的，但个别中文综述/短文存在极简记号式命题（如 `AAAS 2024` 命题 2 仅写 `$S=\mathbb{S}, F=\mathbb{F}$`）。
- **裁定准则**：核查 Duan 原文时尊重其原始措辞 `[E]`，把本文为跨模态切换或奇异集闭性另加的“$\varphi_i$ 连续”等条件明确标为本文新增 `[D]`；**在起草或修改用户稿件时，严格执行“每个定理/引理/命题/推论都必须在陈述本身写明目的”的写作规则 `[D]`**，不模仿极简记号式短句。

---

## 核查模式（Check）与起草模式（Draft/Polish）速查总表

| 维度 | Check 原文/文献核查（承认 `[E]` 多样性） | Draft / Polish 新稿统一标准（推荐默认） |
| :--- | :--- | :--- |
| 定义符号 | `=` 与 `\triangleq` 均为 `[E]`；`:=` 为合作者写法（一作 `0/32`） | `Notations:` 只用 `=`；正文局部定义用 `=` 或 `\triangleq`，不用 `:=` |
| 定理开头与控制律 | `Let`（63.7%）与 `Suppose`（12.1%）、内联公式与编号引用并存 | 结构紧凑处用 `Let ... given by (x)`；核心主定理可内联展开控制律 |
| 证明位置与收尾 | 定理前构造（~60%）、定理后 `Proof`（83.8% 无收尾套话）、附录并存 | 常规证明直接停在末式 + `\qedhere`；反证法保留 `"The proof is finished."` |
| 分条标号 | IEEE `1)`、IJSS/SCIS `(1)`、专著 `1.` 随刊变化 | IEEE 稿件统一用 `1), 2)`；IJSS/SCIS 统一用 `(1), (2)` |
| 矩阵栈与控制律符号 | `A^{0\sim n-1}`（2021 反步）与 `A_{0\sim n-1}` 并存；OD-FAS 用 $-u_0$ | 默认用下标 `A_{0\sim n-1}`；每次代入原方程核验控制律正负号 |
| 奇异判据 `or \infty` | 光滑模型省去 `or \infty`，有理/一般模型保留 `or \infty` | 按 $B(\cdot)$ 是否含分式极点如实选择；引用原定义照原文 |
| 术语与英美拼写 | `ROEA`/`RoEA`、`feasible set`/`set of feasibility`、英美拼写并存 | IEEE 稿件统一 `ROEA` + `feasible set` + 美式 `-izing` |
| 矩阵稳定性谓词 | `Hurwitz`（主流）、`stable`（`Duan 2023`）、`Schur`（离散） | 连续时间一律写 `Hurwitz`，离散时间一律写 `Schur` |
| 正则性与额外条件 | 原文按需写未声明 / `piecewise continuous` / `smooth` | 原文条件标 `[E]`，本文附加条件（如 $\varphi_i$ 连续、跨模态比较 $|\varphi_i|$）标 `[D]` |

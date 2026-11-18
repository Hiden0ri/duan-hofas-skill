# Duan 经典定义全集主题索引与原句速查库

本文件与本地缓存全量原文库 `corpus/sorted/definitions.md`（**94 条正式 `Definition`**）及 `corpus/sorted/classic_definitions_by_topic.md`（**94 条正式 `Definition` + 15 处正文/定理内核心定义 = 109 条**，由 `scripts/build_classic_definitions_bank.py` 生成）一一对应，所有编号、页码与原句均已对照原始 PDF 核准 `[E]`。

> **体例核查核心警示 `[E]`**：段广仁原文中并非所有经典概念都放在编号 `Definition` 环境内——例如 `Duan 2023 TCYB` 与 `Duan 2024 Overview` 中的奇异集 $\mathbb{S}$、可行集 $\mathbb{F}$ 是在正文中直接引入的，ROEA 是在 `Theorem 1`（或定理前正文）首次给出的；而在 `IJSS Part VII`、`SCIS Chained Part 1`、`AAAS 2024`、`UC-FAS Part II`、`OD-FAS Part 1` 中，奇异点/可行集则放入了正式 `Definition` 环境。引用时务必区分 **`[Formal Def.]`** 与 **`[Prose / Thm.]`**，切勿把正文记号写成 `"Definition X in Duan (2023)"`。

---

## 1. 高阶全驱系统（Global FAS）与亚全驱系统（sub-FAS）基础定义（10 条）`[E]`

- **中文首篇定义**（`aas_2020_part1` 定义 1, PDF p.3；`aas_2020_part2` 定义 1, PDF p.4 & 定义 2, PDF p.8）`[Formal Def.]`：
  - 针对 $E x^{(m)}=f(\cdot)+B(\cdot)u$（其中左端 $E\in\mathbb{R}^{n\times n}$ 为常值矩阵、可奇异，`aas_2020_part1` 中 $\Omega_i$ 为紧集，`part2` 定义 2 中为开集），若 $\det B(x,\dot x,\dots,x^{(m-1)},t)\neq 0,\ t>0$：1) 在 $\Omega$ 上成立，称为**在 $\Omega$ 上是全驱的**；2) 只在 $\Omega$ 上某超曲面上不成立，称为**在 $\Omega$ 上是亚全驱的**；3) 只在有限个点不成立，称为**几乎全驱的**；4) 对任意 $x^{(i)}\in\mathbb{R}^n$ 成立，称为**大范围全驱的（简称全驱的）**；当 $B(\cdot)\equiv I_n$ 时称为**标准全驱系统**（注：原文无“局部全驱系统”一词）。
- **英文单阶与多阶仿射全驱原始定义**`[Formal Def.]`：
  - `ijss_2021_part1` Def. 2.1 (PDF p.5)：*"Given system (3) and the above sets $\Omega_i\subset\mathbb{R}^n,\ i=0,1,\ldots,m-1$ and $\Omega$, if $\operatorname{rank} B(x^{(0\sim m-1)},\zeta)=r=n,\ \forall t\ge 0$, holds for all $x^{(i)}\in\Omega_i$, then the system (3) is called fully actuated on $\Omega$; does not hold only on a hyperplane in $\Omega$, then the system (3) is called sub-fully actuated on $\Omega$..."*
  - `ijss_2021_part7` Def. 2.2 (PDF p.7)：用 $\mathbb{S}\cap\Omega=\emptyset$ 定义 `completely fully actuated on \Omega`，用 $\mathbb{S}=\emptyset$ 定义 `(globally) fully actuated`。
- **非仿射微分同胚可行/奇异集定义**（`ijss_2021_part7` Def. 2.3, PDF p.8）`[Formal Def.]`：
  > *"Let $\mathbb{F}\subset\mathbb{R}^\kappa$ be the largest set such that the following mapping $\tilde u = g(x_k^{(0\sim\mu_k-1)}\vert_{k=1\sim\eta},\zeta,t,u)$ forms a differential homeomorphism from $u$ to $\tilde u$ for all $x_k^{(0\sim\mu_k-1)}\vert_{k=1\sim\eta}\in\mathbb{F}$, and $\zeta\in\mathbb{R}^p,\ t\ge 0$. Then the set $\mathbb{F}$ is called the set of feasible points of system (19)..."*
- **综述与频域 PMD 二分法标准定义**`[Formal Def.]`：
  - `tcyb_2024_overview` Def. 1 (PDF p.3)：*"The multi-order FAS (2) is called 1) a (global) FAS if $\mathbb{S}=\emptyset$ or equivalently $\mathbb{F}=\mathbb{R}^\kappa$; 2) a sub-FAS if $\mathbb{S}\neq\emptyset$ or equivalently $\mathbb{F}\neq\mathbb{R}^\kappa$."*（另见 `aaas_2024_subsfs` 定义 6, PDF p.6；频域 PMD 全驱/欠驱定义见 `jssc_2022_freq` Def. 2.2, PDF p.4 及 `book_2026_volume1` Def. 2.1, PDF p.92。）

---

## 2. 奇异点、奇异集与可行点、可行集（11 条：5 条正式 + 6 处正文）`[E]`

| 出处 | 体例形态 | 核心定义逐字原句 |
|---|---|---|
| `ijss_2021_part7` Def. 2.1 & §2.2 (p.7) | `Def. 2.1` 定奇异点 + 正文式 (14)–(15) 定 $\mathbb{S},\mathbb{F}$ | *"If $x_k^{(0\sim\mu_k-1)}\vert_{k=1\sim\eta}\in\mathbb{R}^\kappa$ satisfies $\det B(x_k^{(0\sim\mu_k-1)}\vert_{k=1\sim\eta},\zeta,t)=0\text{ or }\infty,\ \exists\zeta\in\mathbb{R}^p,\ t\ge 0$, then it is called a singular point of system (8)."*（另见 `ijss_2022_part9` Def. 6.1, p.13） |
| `ijss_2022_part8` Def. 5.1 & §5.1 (pp.9–10) | `Def. 5.1` + 正文定 $\mathbb{F}_t, \mathbb{F}_0$ | 区分全时域可行点集 $\mathbb{F}$、$t$ 时刻可行点集 $\mathbb{F}_t=\mathbb{R}^\kappa\setminus\mathbb{S}_t$ 与可行初值点集 $\mathbb{F}_0=\mathbb{R}^\kappa\setminus\mathbb{S}_0$，并指出 $\dim\mathbb{F}\ge 1$ 时称为 `sub-fully actuated system`。 |
| `tcyb_2023_subfas` §III-B1 (p.5) | **`[Prose]` 正文直接引入** | *"Regarding the sub-FAS (18) or (25), we can naturally introduce the following singular set: $\mathbb{S}=\mathbb{S}_0\cup\mathbb{S}_\infty$, where $\mathbb{S}_0=\{X\mid\det B(X,t)=0,\ X\in\mathbb{R}^m\text{ and }t\ge 0\}$, $\mathbb{S}_\infty=\{X\mid\det B(X,t)=\infty,\ X\in\mathbb{R}^m\text{ and }t\ge 0\}$... For convenience, we call $\mathbb{S}_0$ the normal singular set and $\mathbb{S}_\infty$ the abnormal singular set."* |
| `tcyb_2024_overview` §II-B (p.3) | **`[Prose]` 正文直接引入** | *"Then, as defined in [11], $\mathbb{S}$ is called the set of singularity for the multi-order FAS (2), and $\mathbb{F}=\mathbb{R}^\kappa\setminus\mathbb{S}$ is called the set of feasibility for the multi-order FAS (2). Furthermore, we call an $X\in\mathbb{S}$ (or $\mathbb{F}$) a singular point (or a feasible point) of FAS (2)."* |
| `scis_2024_chained1` Def. 3 (p.7) & `aaas_2024_subsfs` 定义 5 (p.6) | **`[Formal Def.]` 正式定义环境** | *"Consider the nonlinear system in the form of (6). Let $\hat{\mathbb{S}}_x=\{\cdots\}$. Then $\hat{\mathbb{S}}_x$ is called the singular set of system (6), and $\hat{\mathbb{F}}_x=\mathbb{R}^{n+2}\setminus\hat{\mathbb{S}}_x$ is called the feasible set of system (6)."* |

---

## 3. 奇异函数（$\varphi_0,\varphi_\infty,\varphi$）与奇异分类（10 条：9 条正式 + 1 处正文）`[E]`

1. **正常与异常奇异函数**（`tcyb_2023_subfas` Defs. 5–6, p.6；`aaas_2024_subsfs` 定义 3–4, p.6，针对变换后矩阵 $\breve{B}_n(X,t)$）`[Formal Def.]`：
   - *"A scalar function $\varphi_0(X,t)$ is called a function of normal singularity for the sub-FAS (18) or (25) if $\varphi_0(X,t)=0,\ t\ge 0\Longleftrightarrow\det B(X,t)=0,\ t\ge 0$."*
   - *"A scalar function $\varphi_\infty(X,t)$ is called a function of abnormal singularity for the sub-FAS (18) or (25) if $\varphi_\infty(X,t)=0,\ t\ge 0\Longleftrightarrow\det B(X,t)=\infty,\ t\ge 0$."*
2. **总奇异函数 $\varphi(X,t)$**（`tcyb_2023_subfas` §III-B2, p.6 `[Prose]`）：单类奇异时取 $\varphi=\varphi_0$ 或 $\varphi_\infty$，两类并存时取 $\varphi(X,t)=\varphi_0(X,t)\varphi_\infty(X,t)$，可行集写为 $\mathbb{F}=\{X\mid\varphi_0(X,t)\varphi_\infty(X,t)\neq 0,\ X\in\mathbb{R}^m,\ t\ge 0\}$（连续性非 Duan 原始定义要求，属切换分析新增假设 `[D]`）。
3. **两套正交分类体系**`[Formal Def.]`：
   - **按奇异成因**（`tcyb_2023_subfas` Def. 3, p.5；`tcyb_2024_overview` Def. 2, p.3）：`0-type sub-FAS`（$\mathbb{S}=\mathbb{S}_0$）、`\infty-type sub-FAS`（$\mathbb{S}=\mathbb{S}_\infty$）、`mixed-type sub-FAS`（$\mathbb{S}_0,\mathbb{S}_\infty$ 均非空）；
   - **按原点拓扑位置**（`tcyb_2023_subfas` Def. 4, p.5；`aaas_2024_subsfs` 定义 7, p.6；`tcyb_2024_overview` Def. 10, p.14）：`rational sub-FAS`（$0\notin\mathbb{S}$）、`critical(ly) rational sub-FAS`（$0\in\partial\mathbb{S}$ 为边界点）、`irrational sub-FAS`（$0\in\operatorname{int}\mathbb{S}$ 为内点）。

---

## 4. 亚稳定性（Substability）、亚镇定与指数吸引域（ROEA / RoEA / REA，7 条）`[E]`

- **亚稳定性与亚可镇定性原始定义**（`tcyb_2023_subfas` Defs. 1–2, p.4；中文对应 `aaas_2024_subsfs` 定义 8, pp.6–7；注：`tcyb_2024_overview` 仅在 p.8 Theorem 8 后以正文复述，无编号定义）`[Formal Def.]`：
  > *"Definition 1: Let $\mathbb{Q}\subset\mathbb{R}^n$ be nonempty. If for any initial value $x_0\in\mathbb{Q}$, the solution of system (16), $x(t,x_0)$, exponentially converges to zero, then system (16) is called substable with respect to the ROEA $\mathbb{Q}$."*
  > *"Definition 2: The system (17) is called substabilizable if there exists a control law $u=u(x,t)$, defined on some nonempty domain in $\mathbb{R}^n$, such that the closed-loop system is substable with respect to some ROEA $\mathbb{Q}\subset\mathbb{R}^n$."*
- **sub-FAS 闭环 ROEA 精确刻画定义**（`tcyb_2023_subfas` Thm. 1(3) & Thm. 3, pp.7–8 `[Thm.-Embedded]`；`tcyb_2024_overview` p.8 Thm. 7 前 `[Prose]`）：
  - 单阶无时滞情形：$\mathcal{R}_s=\{X_0\mid\varphi(\mathrm{e}^{\Phi(A_{0\sim n-1})t}X_0, t)\neq 0,\ X_0\in\mathbb{R}^{nr}\text{ and }t\ge 0\}$（`Overview` p.8 写为 $\mathcal{R}_0=\{X_0\mid\exp[\Phi(A_{0\sim n-1})t]X_0\in\mathbb{F},\ \forall t\ge 0\}$）。
- **初值约束交集与驻点分解表示**（`fasta_2026_roea` §2.1 式 (5)–(6) & §4.2 式 (22) `[Prose]`；另注：`ijss_2024_underactuated4` 摘要曾短暂用缩写 `REA`）。

---

## 5. 能控/能观/平坦输出、Type I/II 系统与非线性稳定性预备定义（30 条）`[E]`

- **高阶能控性系列**`[Formal Def.]`：
  - `ijss_2021_part7` Def. 3.2 (p.11)：四级分类——`completely controllable`、`almost completely controllable`、`basically completely controllable`、`controllable on a set \Omega`（中文首篇见 `aas_2020_part2` 定义 3, p.8）；
  - `scis_2022_discdelay2` Def. 4 (p.14) & `scis_2023_delay1` Def. 6 (p.20)：引入 `sub-controllable`：
    > *"The dynamical system (64) is called completely controllable if it can be equivalently converted into a globally FAS in the form of (27) or (32), and is called sub-controllable if it can be equivalently converted into a sub-FAS in the form of (27) or (32)."*
- **全量测系统与高阶完全能观性**（`aas_2020_part3` 定义 1, p.4 & 定义 2, p.7）`[Formal Def.]`：若对任意 $u$ 输出映射 $y=C(z,u)$ 构成 $z\mapsto y$ 的微分同胚，称为 **$m$ 阶全量测系统**；若系统可经适当等价变换化为高阶全量测系统，则称为**完全能观的**。
- **平坦输出（Flat Output）与全套相对阶**（`tcyb_2024_overview` Defs. 3–6, pp.6–7）`[Formal Def.]`：依次定义 `fully flat output`、`solid flat output`、`control-oriented flat output`（伴随可行集 $\mathbb{G}$）及 `full / solid / control-oriented set of relative degrees`。
- **Type I 与 Type II 系统及可镇定性（切勿混淆两者输入结构！）**（`ijss_2021_part7` Defs. 4.2, 4.6, 4.7, pp.14–16）`[Formal Def.]`：
  - **Type I 系统**（`Def. 4.2`）：等价于“受控全驱子系统 (48) + **不含控制输入 $u$ 的不可控自治子系统** (49)”；当 (49) 在某意义下稳定时称为 `stabilisable in a certain sense`；
  - **Type II 系统**（`Def. 4.6–4.7`）：等价于“主全驱子系统 (48) + **共享控制输入 $u$ 的附加子系统** (57)”；若可由形如 (60) 的控制器镇定，称为 `strongly stabilisable`（原文无 `weakly stabilisable`）。
- **频域互质 MFD 与稳定性预备工具**`[Formal Def.]`：`jssc_2022_freq` Def. 3.1 (p.5，左右不可约 MFD 与互质)；`book_2026_volume1` Defs. 2.2–2.5（LTV 等价、能控指标、反馈线性化）、Def. 3.1 & `tcyb_2024_overview` Def. 7（有限时间稳定允许函数）；`tcyb_2023_robustdelay` Defs. 1–4 & `book_2026_volume1` Defs. 12.1–12.4（类 $\mathcal{K}/\mathcal{KL}$、$\mathcal{K}_\infty$-有界函数与 ISS）；`odfas_2026_part4` Defs. 2.2–2.4, 3.1–3.2（一致有界、次线性增长与 LTV 矩阵一致渐近稳定）。

---

## 6. 亚严反馈（sub-SFS）、广义链式与单向连接全驱系统（UC-FAS，17 条）`[E]`

- **亚严反馈系统（sub-SFS）**（`aaas_2024_subsfs` 定义 1–2, p.3；`tcyb_2024_overview` Defs. 8–9, p.13）`[Formal Def.]`：由各层 $\det G_i(x_{1\sim i},t)=0\text{ or }\infty$ 定义奇异集 $\hat{\mathbb{S}}$ 与可行集 $\hat{\mathbb{F}}=\mathbb{R}^{nr}\setminus\hat{\mathbb{S}}$；$\hat{\mathbb{F}}\neq\emptyset$ 时称为 `sub-SFS`（亚严反馈系统）。
- **广义链式系统分类**（`scis_2024_chained1` Defs. 1–7, pp.6–7, 21–22）`[Formal Def.]`：`globally normal`、`locally normal / abnormal`、奇异集 $\hat{\mathbb{S}}_x$ 与可行集 $\hat{\mathbb{F}}_x$、`sub-normal`、`rational sub-normal`（含时变参数化奇异集 $\mathbb{S}_x(x_0)$ 的 `Def. 5–7`）。
- **强/弱单向连接全驱系统（UC-FAS）与内外可行集 / 内外 RoEA**（`ucfas_2025_part1` Defs. 4.1, 5.1；`ucfas_2025_part2` §2.1 & Defs. 2.1–2.2, pp.4–5）`[Formal Def. & Prose]`：
  - 总可行集 $\mathbb{F}=\mathbb{F}^{\mathrm{in}}\cap\mathbb{F}^{\mathrm{ex}}$，总吸引域 $\mathcal{R}=\mathcal{R}^{\mathrm{in}}\cap\mathcal{R}^{\mathrm{ex}}$。

---

## 7. 输出依赖全驱系统（OD-FAS / sub-OD-FAS，4 条）`[E]`

- **输出空间可行集与全局/亚 OD-FAS**（`odfas_2026_part1` Def. 2.1 & `Convention C1`, p.4；`odfas_2026_part4` Def. 2.1, p.9）`[Formal Def. & Prose]`：
  - $\mathbb{F}=\{Y\mid\det B(Y,t)\neq 0\text{ [or }\infty\text{]},\ Y\in\mathbb{R}^{mq},\ t\ge 0\}$；
- **动态输出反馈增广初值 RoEA**（`odfas_2026_part1` §4.2 Thm. 4.2 前正文及式 (91), p.14 `[Prose + Thm.]`）：因动态补偿器状态 $z(t)\in\mathbb{R}^\nu$ 共同决定输出轨迹，RoEA $\mathcal{R}$ 定义在增广初值 $[X_0^\top\ z_0^\top]^\top\in\mathbb{R}^{nr+\nu}$ 上。

---

## 8. 离散时间与时滞全驱/亚全驱系统（20 条）`[E]`

- **离散前进步/后退步栈记号（严禁颠倒上下取整括号！）与可行轨迹集**（`ijss_2022_part10` §2.2–2.3 & Defs. 3.2–3.3, 4.1–4.3, 6.1, 7.1, 7.3；`tcyb_2024_overview` p.4 式 (7)–(9)）`[Formal Def. & Prose]`：
  - **前进步算子（下取整括号 `floor`）**：$x^{\lfloor i\rfloor}(k)=x(k+i)$，$x^{\lfloor 0\sim n\rfloor}(k)=[x^\top(k+n),\dots,x^\top(k)]^\top$；
  - **后退步算子（上取整括号 `ceiling`）**：$x^{\lceil i\rceil}(k)=x(k-i)$，$x^{\lceil 0\sim n\rceil}(k)=[x^\top(k),\dots,x^\top(k-n)]^\top$；
  - 在有界序列空间 $\mathbb{B}_{\mathbb{N}}^\kappa$（及输入扩展空间 $\mathbb{B}_{\mathbb{N}}^{\kappa+mr}$）上定义**可行轨迹（feasible trajectory）**与**奇异轨迹集**（注：`Part X` 第 7 节因定理共用序号，只有 `Defs. 7.1, 7.3`，`7.2` 为 `Theorem 7.2`）。
- **离散时滞与连续状态时滞亚全驱定义**（`scis_2022_discdelay2` Defs. 1–4；`scis_2023_delay1` Defs. 1–8）`[Formal Def.]`。

---

## 附：原刊自身印刷笔误备忘（核查时保留原文并标 `[sic]`，起草新稿时规避）`[E]`

1. `aaas_2024_subsfs` 定义 5 (p.6)：可行集印为 $F=\mathbb{R}^m\setminus\mathbb{S}$（该文无分布矩阵 $T$，上下文维数为 $\mathbb{R}^{nr}$）；
2. `tcyb_2024_overview` Def. 8 (p.13)：印为 $\hat{\mathbb{F}}\subset\mathbb{R}^{nr}\setminus\hat{\mathbb{S}}$（应为 $=$）；
3. `tcyb_2023_subfas` Thm. 3 (p.8)：印为 $A_E\in\mathbb{R}^M$（实为方阵 $\mathbb{R}^{\kappa\times\kappa}$ 或相应块维数）；
4. `ijss_2021_part7` Def. 4.6 (p.16)：第二句把附加子系统 `(57)` 误印成了 `(49)`；
5. `ijss_2022_part10` Def. 4.1 (p.10)：奇异轨迹集说明误印为 `the set of feasible singular trajectories`。

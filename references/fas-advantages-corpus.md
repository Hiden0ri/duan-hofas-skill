# Duan 关于高阶全驱系统（FAS）方法优势、方法对比与客观边界的精选语料库

本文件从段广仁（Guang-Ren Duan）32 篇一作中英文论文与 2026 年专著 *Fully Actuated System Approach, Volume I* 中提炼关于 **FAS 方法核心优势、与传统方法对比及客观适用边界** 的**单篇逐字原话（`[E]`）**，并与本地全量分拣原文库 `corpus/sorted/fas_advantages_by_theme.md`（共 **53 段**，由 `scripts/build_fas_advantages_bank.py` 生成）一一对应。撰写论文 `Introduction`、方法对比 `Remark`（`R3` 类）、中文博士论文绪论或审稿回复时，可直接按维度选用。

---

## 1. 建模哲学：面向响应的一阶状态空间法 vs 面向控制的高阶全驱法 `[E]`

### 1.1 两大极端模型的对称对比（`tcyb_2024_overview` §II-D, Table I, PDF p.4）`[E]`

| 比较维度 | 状态空间模型（State-space model） | 全驱系统模型（FAS model） |
|---|---|---|
| 表达式复杂度 | 简洁（simple） | 较复杂（complex） |
| 微分阶次 | 最低（lowest） | 最高（highest） |
| 标量方程个数 | 最多（maximum） | 最少（minimum） |
| 由原始物理模型的导出途径 | 增元降阶（variable extension） | 消元升阶（variable elimination） |
| 核心主导变量 | 状态向量（state vector） | 控制向量（control vector） |
| 擅长求解的问题类型 | 面向状态的问题（state-oriented problems） | 面向控制的问题（control-oriented problems） |

### 1.2 中英文逐字高频原句 `[E]`
- **状态空间法的历史定位与控制瓶颈**：
  - *"A state-space model of a dynamical system emphasizes the state vector by integrating the state variables together, and is probably the best choice for solving the problem of response analysis. However, unlike the problem of seeking the state solution, controller design emphasizes the control vector. Toward this goal, a state-space representation does not provide very much convenience."* `[E: book_2026_volume1, §1.1.2, PDF p.24]`
  - *"State-space models are extreme ones: they feature the lowest order of differentials but encompass the maximum number of scalar equations."* `[E: tcyb_2024_overview, §I-A, PDF p.1]`
  - 「状态空间法中的一阶系统模型注重的是状态的整体性, 对于控制系统的状态响应分析、观测器设计、状态滤波与预报等问题而言, 采用增广的一阶系统方法无疑是非常合适的. 但这种方法显然没有把系统的控制变量作为重点, 对于求解动态系统的控制问题实际上没有提供任何方便.」`[E: aas_2020_part1, §1.2, PDF p.2]`
- **物理定律的天然全驱性与反对“增元降阶再还原”**：
  - *"There is no doubt that a model which permits the control vector to be explicitly solved will provide great convenience for its controller design, and will simultaneously optimize control performance."* `[E: tcyb_2024_overview, §I-B, PDF p.1]`
  - 「把系统模型化为一阶系统描述的一个更重要的问题是破坏了系统的全驱特性. …… 一旦把它们化成一阶系统, 全驱特性就不复存在了.」`[E: aas_2020_part1, §1.2, PDF p.2]`
  - 「我们只是通过这两个事实进一步说明高阶全驱系统的广泛存在性, 并不建议在应用中先获得系统的一阶状态空间模型, 然后再将其化为高阶全驱系统. 因为这是不经济的, 对于控制系统设计而言是个 “画蛇添足”、“费力不讨好” 的过程. 可能的话, 我们提倡在系统建模的过程中直接获得系统的高阶全驱模型.」`[E: aas_2020_part1, §3, PDF p.7]`

---

## 2. 定常线性闭环与完整特征结构参数化自由度（DOFs）`[E]`

- **任意复杂可测非线性项直接对消与归约为单一特征结构配置对**：
  - *"With such models, we can easily eliminate the nonlinear terms using the full-actuation structure, no matter how complicated the nonlinear terms are, but as long as they are measurable. Eventually, an LTI closed-loop system is obtained."* `[E: book_2026_volume1, §1.2.1, PDF pp.27–28]`
  - *"It is often seen that one class of problems is converted into another one in science research, but the above particular conversion is special in two aspects: 1) the scope of the problems can be converted is astonishingly wide, as we have seen; 2) the finally converted problem turns out to be not a class, but a single one, namely, the eigenstructure assignment of a specific pair of matrices $(\Phi(0_{0\sim n-1}), B_c)$, which is determined by only two parameters $n$ and $r$."* `[E: tcyb_2024_overview, Remark 4, PDF p.9]`
- **解耦简易性与耦合设计自由度兼得**：
  - *"The decoupled control design is obviously very simple, while the advantage of the coupled design is that it provides much more degrees of freedom. ... When properly utilised, these extra degrees of freedom can make the system perform much better."* `[E: ijss_2021_part7, Remark 5.1, PDF p.19]`

---

## 3. 对比经典反步法（Backstepping）：克服“微分爆炸”并获得 LTI 闭环 `[E]`

- **段广仁最经典的两点式标准对比模板**（回复审稿人或写 `Remark` 首选）：
  - *"The proposed HOFA system approach is generally more effective than the method of backstepping because of the following two facts: • The HOFA system approach can always produce a constant linear closed-loop system, but the method of backstepping can not; • Due to the well-known problem of ‘differential explosion’, the method of backstepping is generally not applicable to a SFS with more than 3 or 4 subsystems, while the HOFA system approach is, noting that the proposed recursive solutions are easy to realise."* `[E: ijss_2021_part2, Remark 2.3, PDF p.7]`（同见 `book_2026_volume1` Remark 6.4 & Remark 7.2）
- **高阶/混合阶严反馈直接设计与高阶反步法**：
  - *"As a matter of fact, many practical systems are in fact in the form of a high-order, or mixed-order SFS. Converting them into the first-order SFS not only adds an extra computational burden, but also makes the backstepping design much more complicated since in this case the layers in the converted first-order SFS are doubled."* `[E: ucfas_2025_part1, Remark 6.2, PDF pp.10–11]`
  - *"The proposed high-order backstepping method is a great contribution of the FAS approach which greatly reduces the possibility of “differential explosion” of the normal first-order method of backstepping."* `[E: book_2026_volume1, §1.4, PDF p.57]`
  - 「1）反步法存在“微分复杂性爆炸”问题，本文方法所涉及到的亚全驱系统求解过程不存在“微分复杂性爆炸”问题，控制律设计简单易行。2）对于亚严反馈系统的情形，反步法只能处理一些非常特殊的个类系统，而本文给出的则是一般性的处理方法。」`[E: aaas_2024_subsfs, §3 说明, PDF p.8]`

---

## 4. 对比几何反馈线性化并延伸至亚全驱（sub-FAS）与非完整系统 `[E]`

- **回应“FAS 是否只是反馈线性化”的标准辩护原句**：
  - *"Some readers who are not yet familiar with the FAS approach might be mistaken that the FAS approach is nothing but feedback linearization. The above result can only tell that feedback linearization is a special case of the FAS approach, but not vice versa since the FAS approach also treats systems not in the state-space form, and can solve the stabilization of systems which have already been proven to be not feedback linearizable. Indeed, the FAS approach really does much more than the feedback linearization technique."* `[E: tcyb_2024_overview, Remark 2, PDF p.5]`
- **非反馈线性化系统、过原点奇异集与非完整约束的亚镇定突破**：
  - *"More specifically, for nonlinear systems which are not completely controllable (or not globally feedback linearizable in the state-space representation), a sub-FAS model of such a system is often obtained, which defines, when designing the controller of the system using the FAS approach, a singular set on which the controller is not well defined. This naturally leads to a problem of substabilization of the system."* `[E: tcyb_2023_subfas, §I, PDF p.2]`
  - *"As a matter of fact, sub-FAS describes a larger category covering nonholonomic systems. Eventually, the nonholonomic constraints generally produce a singular set containing the origin, often as a boundary point. The FAS approach provides a general approach for dealing with systems possessing constraints on the state variables and their derivatives."* `[E: scis_2024_chained1, §6.2, PDF p.23]`

---

## 5. 能控性、能观性与控制器显式求解的统一 `[E]`

- *"With this definition, it is obvious that • all dynamical control systems, not only those in state-space representations, possess the concepts of controllability; • the problem of controllability analysis and the problem of control are now highly consistent in the sense that, once the controllability of a system is verified by obtaining the HOFA model of the system, the design problem is then easily solved"* `[E: ijss_2021_part7, §3.2, PDF p.11]`
- 「由定义 2 可知, 全驱系统是一类以控制变量为核心的系统, 本质上可以几乎显示解出控制变量 u. 进一步由定义 3 可知, 完全能控的系统就是可以求解出控制变量的系统.」`[E: aas_2020_part2, §4 说明 2, PDF p.9]`（注：原刊印作“显示”`[sic]`）

---

## 6. 天然抗扰、时滞超前对消、单向连接（UC-FAS）与输出反馈（OD-FAS）`[E]`

- **天然抗扰特性**：
  - *"It is clearly seen from (11) that some constant disturbances, slope disturbances, etc., may automatically disappear when the HOFA system method is used for design. Therefore, the HOFA system approach itself has certain ‘natural’ anti-disturbance characteristics."* `[E: ijss_2021_part6, Remark 2.1, PDF p.6]`
- **时变与时滞系统的独特优势**：
  - *"It is pointed out that the FAS approach is superior to dealing with time-varying and time-delay systems."* `[E: book_2026_volume1, Preface, PDF p.7]`
- **超越单个 FAS/sub-FAS 的扩展（UC-FAS 与 OD-FAS）**：
  - *"In spite of the fact that numerous dynamical systems can be converted into FASs and their control can be more effectively solved by the FAS approach, there are still systems which cannot be converted into a single FAS or sub-FAS."* `[E: ucfas_2025_part3, §1, PDF p.2]`
  - *"We here treat the static output feedback control of this example system from the angle of substabilization. The result turns out to be finer and more intuitive."* `[E: odfas_2026_part1, Remark 4.1, PDF pp.14–15]`

---

## 7. 客观适用边界与防夸大红线表述（撰写引言必读 `[E]`）

段广仁本人在专著与综述中对状态空间法与 FAS 方法的边界做了非常客观克制的界定，撰写稿件时**严禁全盘否定状态空间法或夸大全局 FAS 的能力范围**：

1. **区分“全局 FAS 更好求解”与“亚全驱求解状态空间不能解的问题”** `[E: book_2026_volume1, Preface, PDF p.7]`：
   > *"Senior researchers on nonlinear control may find that this volume does not solve problems that the state-space approach does not solve, but it does solve many problems in a better way. It will be found in Volumes II and III that the FAS approach indeed can solve many problems that the state-space approach can not."*
2. **肯定一阶状态空间法在响应分析、观测与滤波中的优势** `[E: aas_2020_part1 §1.2; aaas_2024_subsfs §1]`：
   - 切勿笼统贬低状态空间模型本身；应准确表述为：状态空间模型适合**面向状态（state-oriented）**的响应分析、状态滤波与观测问题，而高阶全驱模型适合**面向控制（control-oriented）**的控制律显式求解与闭环特征结构配置问题。
3. **如实交代不确定性/未知参数需要改进基本流程** `[E: tcyb_2024_overview, §IV-E, PDF p.10]`：
   > *"However, this basic procedure is not directly applicable to those original systems with dynamical uncertainties or unknown parameters. To cope with systems with dynamical uncertainties, unknown parameters, disturbances and reference signals, the procedure needs to be modified in certain ways."*

---

## 快速调取全量 53 段原文与检索

1. 按 7 大维度通读全部 53 段逐字原文：直接读取 `corpus/sorted/fas_advantages_by_theme.md`；
2. 重建该主题库：`python3 scripts/build_fas_advantages_bank.py`。

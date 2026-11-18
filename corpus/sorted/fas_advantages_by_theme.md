# Duan 全集关于 FAS 方法优势、方法对比与客观边界的原文分拣库（共 53 段）

- **覆盖范围**：从 32 篇段广仁一作中英文论文（引言、`R3` 类方法对比 `Remark`、结论）及 2026 专著 *Volume I*（前言、第 1 章 `§1.1–1.2`、第 6–7 章 `Remark 6.4 / 7.2` 等）中逐字提取。
- **核心用途**：撰写英文小论文 `Introduction`、中文博士论文绪论/开题报告、基金申请书以及回复审稿人关于状态空间法 / 反馈线性化 / 反步法的对比质询。

## 七大维度统计总览

| 维度 | 原文段落数 |
|---|---:|
| 1. 建模哲学：面向响应的一阶状态空间法 vs 面向控制的高阶全驱法（增元降阶 vs 消元升阶） | 13 |
| 2. 定常线性闭环与完整特征结构参数化设计自由度（LTI Closed-Loop & Parametric DOFs） | 8 |
| 3. 对比经典反步法：克服“微分爆炸 / 复杂性爆炸”与多阶严反馈归约 | 12 |
| 4. 对比反馈线性化并延伸至亚全驱（sub-FAS）、奇异陷阱与非完整临界有理系统 | 5 |
| 5. 高阶能控性、能观性与控制器显式求解的统一（突破 Kalman 线性状态空间局限） | 4 |
| 6. 天然抗扰、时变/输入时滞超前对消、单向连接（UC-FAS）与输出依赖输出反馈（OD-FAS） | 8 |
| 7. 客观适用边界与防夸大红线表述（肯定状态空间滤波/观测优势，区分更好求解 vs 求解新问题） | 3 |
| **合计** | **53** |

---

## 1. 建模哲学：面向响应的一阶状态空间法 vs 面向控制的高阶全驱法（增元降阶 vs 消元升阶）

### [1] `aas_2020_part1` — §1.2 一阶系统方法的利与弊及高阶全驱出发点 (PDF p.2, L166)

### 1.2 利与弊

一阶系统方法在控制系统科学发展中所起的作
用是巨大的. 然而, 动态系统的控制问题和微分方程
的求解问题不同. 微分方程的求解关注的是系统状
态的解. 系统控制的核心问题是控制量的求取.
状态空间法中的一阶系统模型注重的是状态的
整体性, 对于控制系统的状态响应分析、观测器设
计、状态滤波与预报等问题而言, 采用增广的一阶系
统方法无疑是非常合适的. 但这种方法显然没有把
系统的控制变量作为重点, 对于求解动态系统的控
制问题实际上没有提供任何方便. 这种现象自然使
得基于一阶系统的控制分析与设计存在一系列问题.
一个简单的例子便是系统的解耦问题. 求解一
个高阶全驱系统的模型解耦问题是很简单的 (见第 5
节), 可是当把系统转化成一阶系统再来考虑其输入
输出解耦就很难了[27], 而且还失去了物理上通道解
耦的含义. 关于能控性方面的问题请见文献 [28].
把系统模型化为一阶系统描述的一个更重要的
问题是破坏了系统的全驱特性. 物理世界中存在许
多全驱系统. 例如, 在机械臂制作中人们往往为每个
关节都安装一个驱动电机; 在飞行器设计中要确保
俯仰、偏航和滚动三个方向上都有控制力矩;· · · · · ·
全驱系统的控制是很简单的. 全驱特性允许我们对
消掉开环系统的所有动态特性 (无论是线性还是非
线性的), 同时建立全新的希望的闭环动态特性. 即
使在非线性系统的情况, 也能给出一个希望的定常
线性闭环系统. 但由于牛顿定律等一批物理规律的
主宰, 这些全驱系统更多是以二阶或高阶系统的形
式存在的. 一旦把它们化成一阶系统, 全驱特性就不
复存在了. 可人们为了机械地利用一阶系统的控制
理论方法处理问题, 仍然几乎千篇一律地把这些高
阶系统转化成一阶系统, 其结果是把一些简单的问
题复杂化了. 更严重的是, 当系统为非线性时, 还无
法保证一定能够求得系统的镇定控制器, 即使能够
求得, 也不一定能够保证闭环系统的全局稳定性, 更
谈不上给出一个希望的定常线性闭环系统了.
时值 1995 年, 非线性系统理论还被称为 “al-
most everything is open”、“缺乏更好的理解和设

计方法”[29]. 对非线性控制来说, 下述两方面事实说
明一阶系统方法远不完备:
1) 大多数方法, 如反步法、反馈线性化方法等,
都是针对特殊形式或者满足特殊条件的系统提出的,
比较一般性的理论方法较少;
2) 虽然有些方法在理论上具有一般性, 但在实
际设计中未必能够实现, 如应用 Lyapunov 方法时
在很多情形下不一定能够找到所需要的李亚普诺夫
函数; 应用 Pongtriagin 极大值原理时, 未必能够求
出 HJB 方程的解.
一阶系统方法把系统的二阶或高阶模型通过状
态增广化成一阶系统模型来处理, 本质上就是数学
上所谓的降阶法或变量增广法. 这种方法可以把一
个全驱的二阶或者高阶系统化为一阶系统, 那么我
们可不可以反过来把一个一阶系统还原为一个全驱
的二阶或高阶系统呢？这就是高阶系统方法的根本
出发点.
本文揭示了高阶全驱系统在控制器设计方面的
突出优势, 同时又充分说明了高阶全驱系统的普遍
存在性. 进而指出, 高阶全驱系统远非一部分物理系
统而已, 它和系统的状态空间模型一样, 是控制系统
的一种描述形式, 是面向控制设计的系统模型. 在基
于物理定律的控制系统建模过程中, 采用增元降阶
处理便可得到系统的一阶状态空间模型, 采用消元
升阶处理便可得到系统的高阶全驱模型. 针对高阶
全驱模型, 本文也提出了一种参数化设计方法, 提供
了系统设计过程中的所有自由度.

### [2] `aas_2020_part1` — §3 反对先化一阶再转高阶（“画蛇添足”论断） (PDF p.7, L758)

定理 2 和 3 说明, 严格反馈非线性系统和所有
可以反馈线性化的系统都可以通过适当的状态变换
化成高阶全驱系统. 我们只是通过这两个事实进一
步说明高阶全驱系统的广泛存在性, 并不建议在应
用中先获得系统的一阶状态空间模型, 然后再将其
化为高阶全驱系统. 因为这是不经济的, 对于控制系
统设计而言是个 “画蛇添足”、“费力不讨好” 的过
程. 可能的话, 我们提倡在系统建模的过程中直接获
得系统的高阶全驱模型.
本节只是展示了几方面的例子. 事实上, 能化为
高阶全驱模型的系统还有很多. 如果再考虑到亚全
驱的情形, 能化为高阶全驱模型的系统就更多了.

### [3] `aas_2020_part1` — §4 物理定律天然二阶全驱性与一阶降阶局限 (PDF p.10, L1119)

从而丧失了本有的全驱性; 另一方面是物理世界中
确实存在着许多欠驱动系统[52]. 但受制于一阶系统
方法的局限就不会考虑和认识到许多欠驱动系统都
可以通过增阶化为全驱系统. 高阶全驱系统是普遍
存在的, 它们是动态系统的一类面向控制的模型. 大
多数状态空间模型并不是 “天然” 存在的, 而是从二
阶模型化过去的. 相反, 由于动量矩定理和拉格朗
日方程等一批物理规律的存在, 我们倒是有很多 “天
然” 的二阶全驱系统.

### [4] `aaas_2024_subsfs` — §1 一阶状态空间方法在控制律求解上的束缚 (PDF p.2, L167)

值得注意的是，在严反馈系统的研究中，基
于状态空间方程的一阶系统方法占据着绝对的
统治地位。一阶状态空间方法注重的是状态的
整体性，在状态的响应分析、观测和滤波等方面
无疑是非常适合的。但该方法没有把系统的控
制变量作为重点，因而对于控制律的求解没有提
供任何方便，还无法保证一定能够求得非线性系
统的镇定控制器［24］。为了打破一阶状态空间方

法的束缚，高阶全驱系统方法作为一种新的控制
框架和思想被提出［24-30］。文献［24-26］分别给出

了关于高阶全驱系统方法的参数化设计、能控性
和全驱性、能观测性和全量测性等方面研究的详
细论述。文献［27］指出，一般的严反馈系统，包

括一阶、二阶和高阶的严反馈系统，可以通过“消
元升阶”法转换成高阶全驱系统；此外，文献［28］
还给出了亚全驱系统的定义，提出了亚全驱系统
的亚稳定性和亚镇定的控制方法，文献［29-30］
分别研究了带时变时滞的连续时间系统和离散
时间系统的亚全驱系统方法。文献［31-34］还研
究了不确定性系统鲁棒控制问题的全驱系统方
法。与一阶系统方法相比，高阶全驱系统方法更
加简单、直观和高效，并且总能获得一个期望的
线性定常的闭环控制系统。

### [5] `tcyb_2024_overview` — §I-A State-Space Approach Origin & Control Bottlenecks (PDF p.1, L88)

A. The State-Space Approach
State-space models are not the original forms used to
describe dynamical control systems. The original models for
physical dynamical systems come in the form of a set of basic
equations, which can be differential, difference, or mixed.
They are established based on the system’s mechanism or
certain physical laws, which frequently manifest as high-
order differential equations. Renowned first-order state-space
models are derived from these basic equations, primarily
through a method of variable extension. State-space models
are extreme ones: they feature the lowest order of differentials
but encompass the maximum number of scalar equations.
State-space models prove efficient for linear systems, yet
struggle considerably when dealing with nonlinearities, time-
varying properties, time delays, system constraints, and issues
of controllability of nonlinear systems. As early as 1982,
it was described in a survey paper [1] by John Casti that
“seeking a completely general theory of nonlinear systems is

Natural Science Foundation of China under grant No. 62188101, and has
been also partially supported by Shenzhen Key Laboratory of Control The-
ory and Intelligent Systems under Grant No. ZDSYS20220330161800001,
and the Shenzhen Science and Technology Program under Grant No.
Harbin Institute of Technology, Harbin, China, and also the Center for Control
Science and Technology, Southern University of Science and Technology,
Shenzhen, China (e-mail: g.r.duan@hit.edu.cn / duangr@sustech.edu.cn).

somewhat akin to the search for the Holy Grail: a relatively
harmless activity full of many pleasant surprises and mild
disappointments, but ultimately unrewarding”. It was also
claimed by Alberto Isidori at an open talk in Korea that “from
the mid 1990s, the study of problems of feedback design for
MIMO nonlinear systems came to a (almost complete) stall”.
He then asked: “Why was this the case? Was the study of these
problems irrelevant? Or was it too difficult?” Eventually, these
observations have become widely acknowledged in the last
decades, and many control theorists have turned to application
topics.
Why is this the case? Isidori’s question is certainly worth
serious consideration.
As a matter of fact, the reason lies in that state-space
models, despite their dominance in modern control theory for
centuries, are not necessarily the best suited for control tasks.
This reason can be difficult to accept, especially for those who
frequently utilize state-space models. Indeed, the state-space
models serve well in tackling problems directly tied to the
states. This is evident from the application of linear state-space
models, first proposed by Euler in early 1750 to solve high-
order linear differential equations (giving the state responses),
and of nonlinear models, used by Lyapunov in 1892 to analyze
the limit behavior of states. They were not originally proposed
to solve control problems. State-space models do have found
success in controlling linear systems, but largely because linear
systems are straightforward to handle.
If state-space models are not the ideal choice, could there
be a better model for managing control tasks?

### [6] `tcyb_2024_overview` — §I-B Explicit Control Solvability & Birth of the FAS Approach (PDF p.1, L148)

B. The Fully Actuated System Approach
There is no doubt that a model which permits the control
vector to be explicitly solved will provide great convenience
for its controller design, and will simultaneously optimize
control performance. Do such models exist? Indeed, they are
prevalent but often overlooked, overshadowed by the existence
of state-space models and our substantial reliance on the state-
space approach.
In certain practical applications, there are physical systems
referred to as fully actuated systems (FASs). Frequently mod-
eled as Lagrangian systems (a type of second-order differential
equations), these systems are prevalent in mechanical, electri-
cal, and aerospace domains, which allow the control vectors to
be explicitly solved, and are therefore inherently more straight-
forward to be controlled. Often, time-invariant linear closed-
loop systems can be derived in control system designs based
on such models. In fact, many systems originally modeled by

physical laws, such as Newton’s Law or Lagrangian Equations,
fall under this category of FASs.
However, the range of physical FASs is very limited.
What about control of the numerous under-actuated
systems (UASs) and those which are neither FASs nor
UASs? An alternative approach, rather than converting
the model of a dynamical system into a state-space one,
is to transform it into a mathematically generalized FAS.
Similar to a physical FAS, this converted mathematical
version can also be easily controlled, and a linear closed-
loop system can also be achieved with an arbitrarily
assignable eigenstructure. This results in the birth of the
FAS approach as marked by the two sets of papers [2]–[4]
and [5]–[14] (see also the Int. J. Systems Science webpage
“https://www.tandfonline.com/journals/tsys20/collections/HOFA ”
for an introduction).
The FAS approach, owing to its distinct advantages, has
attracted widespread and rapid-increasing attention ever since
its emergence. By now, numerous publications in the field have
been produced (see Fig. 1).
Indeed, the FAS approach has been instrumental in resolving
many nonlinear control problems, encompassing areas such as
robust control, adaptive control, disturbance rejection, optimal
control, and tracking control. Several issues, insurmountable
or inadequately addressed with the state-space approach, have
been effectively and satisfactorily resolved using the FAS ap-
proach. Frequently, the closed-loop systems designed through
the FAS approach have been rendered linear and stable, or
globally exponentially stable or sub-stable. Furthermore, this
methodology has been extended to diverse domains including
discrete-time systems, time-delay systems, stochastic systems
and impulsive systems.

### [7] `tcyb_2024_overview` — §II-D & Table I Comparison of Two Extreme Dynamical Models (PDF p.4, L446)

D. FAS Models vs State-Space Models
In general, state-space models are derived from the system’s
fundamental equations through variable extension, and are
eventually a type of extreme models with the lowest order
and the maximum number of scalar equations. What happens
if the method of variable elimination is employed instead? The
system order will increase, and the number of equations will
diminish. Generally, this number of equations will not exceed
the number of control variables (except in some over-actuated
systems). When equal, a mathematical FAS or sub-FAS is
available for utilization. Hence, FAS models constitute another
class of extreme system models characterized by the highest
system orders but the fewest scalar equations. Technically and
mathematically, this model conversion is in fact a process of
identifying an appropriate homeomorphism, under which the
original system is equivalent to a FAS or sub-FAS. Specifically,

TABLE I
COMPARISON OF TWO EXTREME DYNAMICAL MODELS

State-space model FAS model
Expression simple complex
Differential order lowest highest
Number of scalar equations maximum minimum
Derivation from original variable extension variable elimination
physical model
Dominant variables state vector control vector
Advantageous in solving state-oriented control-oriented
problems problems

it is shown in the next section that all controllable linear time-
invariant systems can be equivalently converted into linear
FASs [2], [24], and several very typical nonlinear systems can
also be equivalently converted via certain homeomorphisms
into nonlinear FASs.
In Table I, a comparison of the FAS models and the state-
space models is given. Indeed, as we have seen that the FAS
models, especially the multi-order ones, are more complicated
than the state-space models. However, the FAS models, as
we will soon find out in subsequent sections, do have many
advantages over the state-space ones, especially in the process
of realizing controller designs.

### [8] `tcyb_2024_overview` — Remark 1 From Mechanical FASs to General Dynamical Models (PDF p.4, L433)

Remark 1: The original physical FASs in the field of
mechanical engineering are only a very small category. With
our generalization, FASs have really become a general model
for dynamical systems, which can characterize most dynamical
systems not restricted to only continuous- and discrete-time
systems (see also the next section). Continuous-time FASs
with time delays can be found in [16]–[19], and time-varying
discrete-time FASs with time delays can be found in [20],
[21]. For a generalization of FASs to stochastic systems, please
refer to [22], [23]. Furthermore, we declare that all the above
mentioned affine FASs can be generalized into nonaffine FASs
(see, e.g., [16]–[19]).

### [9] `ijss_2021_part5` — Remark 2.1 Generality of HOFA Models Beyond Mechanical Systems (PDF p.4, L388)

Remark 2.1: The above HOFA model (3) might be
easily mistaken to represent a very small portion of
systems due to full-actuated Assumption A1. While,
as a matter of fact, many systems which are in state-
space forms can be converted into HOFA systems
(see Duan, 2020a, 2020b, 2020c, 2021a). Furthermore,
many practical systems can also be modelled as HOFA
systems. In fact, most physical systems are governed
by certain physical laws, such as Newton’s law, the
Lagrangian Equation, the Theorem of Linear and
Angular Momentum, and Kirchhoff’s Laws of Cur-
rent and Voltage. When such physical laws are used
in modelling, a series of second-order subsystems are
originally obtained. From this stage, we can further get
a state-space model by variable extension, and on the
other side, we can get a HOFA model by variable elim-
ination. It should be also noted that many physically
fully actuated systems exist, which are already in the

form of second-order HOFA systems at the modelling
stage.

### [10] `ijss_2024_underactuated4` — Remark 3.1 Physical vs Mathematical FAS Conversion of UASs (PDF p.6, L614)

Remark 3.1: The concept of FASs is really origi-
nally proposed for second-order mechanical systems,
describing a class of second-order systems with the
number of control variables equal to the degrees of
the system. Such systems, when converted into state-
space models, have twice as many state variables as the
number of controls. Therefore, the original concept of
FASs fails to describe a system in state-space form with
arbitrary numbers of state and control variables. To
prevent this confusion, in this paper we simply adopt
the extended concept of FAS defined in Section 2. In
this sense, both systems (9) and (10) are UASs.

### [11] `tcyb_2023_subfas` — §III-C Generality of Single- and Multi-Order FASs (PDF p.6, L755)

C. Generality of FASs
Both the above single-order FAS model (18) and the
multiple-order FAS model (25) might be easily mistaken to
be special due to the feasibility requirement

det B(X, t) ≠ 0 or ∞, for some X ∈ 𝔽 ⊂ ℝm and t ≥ 0

where 𝔽 = ℝm\𝕊 ≠ ∅ is the feasible set of the system.
As discussed in [40], [44], and [50], the FASs (18) and (25)
really serve as general models for controllable dynamical
systems. On the one side, many practical systems can be orig-
inally modeled as FASs by directly applying certain physical
laws, such as Newton’s law, the linear and angular theorems of
momentum, and the Lagrangian equation. On the other side,
those systems which can not be modeled originally as FASs
can usually be converted into FASs.
As pointed out in [56], it has been shown that all completely
controllable systems can be even converted into (global)
FASs [50], [56]. Examples include, but are not limited to, the
following typical systems in state-space forms.
1) Linear controllable systems, including both the
continuous-time ones [41], [43] and the discrete-time
ones [53].
2) Linear controllable time-delay systems, including
discrete-time ones with both state and input constant
delays [54], [55], and continuous-time ones with a
constant input delay.
3) Feedback linearizable systems, including both the
continuous-time ones [40] and discrete-time ones [53].
4) Strict-feedback systems, including the continuous-time
ones [40], [45] and discrete-time ones [53], and both
with time-varying delays [56], [57].
5) Some more general types of nonlinear systems [41],
[44], [53].
Furthermore, many systems which are not completely con-
trollable can be converted into sub-FASs. It has been shown

that the well-known two examples proposed in [35] can be
converted into sub-FASs [39], [59]. As a matter of fact, it is
anticipated that the whole set of nonholonomic systems can
be converted into sub-FASs (under consideration).
Finally, as pointed out in [50], an uncontrollable system
can be divided into a controllable subsystem and an uncon-
trollable subsystem. The controllable system is represented by
a sub-FAS, while the uncontrollable subsystem is an unforced
subsystem which is decoupled from the controllable one.
All in all, an FAS is another general model for a dynamical
system besides a state-space model. A state-space model con-
centrates on the state vector of the system and is more suitable
to deal with the problem of state estimation, while an FAS
model concentrates on the control vector of the system and is
more suitable to deal with problems of control. There should
be no doubt that a system model from which one can solve
explicitly the control vector provides great convenience in
realizing the control of the system.

### [12] `book_2026_volume1` — §1.1.2 Deficiencies of the State-Space Approach (Response Analysis vs Control Vector) (PDF p.24, L3)

1.1.2 Deficiencies of the State-Space Approach
A state-space model of a dynamical system emphasizes the state vector by inte-
grating the state variables together, and is probably the best choice for solving the
problem of response analysis. However, unlike the problem of seeking the state solu-
tion, controller design emphasizes the control vector. Toward this goal, a state-space
representation does not provide very much convenience. For over a half century of
research, results with the first-order state-space approaches have been numerous, but
today we are still facing too many unsolved nonlinear control problems (Blondel et
al., 1995).
Control design
The basic step involved in Lyapunov stability analysis and design is to find a proper
Lyapunov function. Since the condition is only sufficient for general nonlinear sys-
tems, in certain cases it might not be able to give a definite conclusion. Furthermore,
even if a Lyapunov function can be found, often a local stability result is obtained. It
is generally difficult to realize global stabilization of a general nonlinear system. The
cases with Bellman dynamic programming and Pontryagin’s maximum principle are
similar, noting that the HJB equations which determine the solutions may not be
solvable for complicated nonlinear systems.
Physical background
All practical systems have physical backgrounds. When modeling a system using
some physical laws, such as Lagrangian Equation or Theorem of Momentum, a
second- or high-order model is obtained, and this original model also reflects in some
ways the physical backgrounds of the system. In certain situations, the background
information may help in the analysis and design. However, with the first-order system
approaches, the system model is reduced to a first-order state-space model, and all
the background information is then removed from the original model.
Full-actuation
Physically, there are many FASs in the world, and their original system models estab-
lished by certain physical laws are of second- or high-order. For such systems, the
control can be realized in an extremely simple way, since the full-actuation property
allows us to eliminate all the nonlinear dynamics. As a consequence, a desired LTI
closed-loop system can be obtained, and the theories and techniques for analysis
and design of linear systems can then be applicable. Furthermore, with the help of
the full-actuation feature, we can also solve many design problems, such as feed-
back stabilization and system decoupling, very easily. Nevertheless, when converted
into first-order state-space models, such systems no longer possess the full-actuation
property, and the nonlinear dynamics needs then to be tackled with Lyapunov sta-
bility design approaches. In certain complicated cases even local stabilization of
the system cannot be realized, not to mention giving a global stabilization result or
obtaining an LTI closed-loop system.
Some of the deficiencies have really limited the developments of the state-space
approach. As a phenomenon, almost all of the main topics today’s researchers are
investigating, e.g., Lyapunov’s second method, differential geometric method, sliding
mode control, linear matrix inequality techniques, H.∞ control, feedback lineariza-
tion, differential flatness, etc., were all originally proposed before 1992. In spite of
the prosperity of the state-space approach for more than half a century, today it has
lost its past glory to an extent.

### [13] `book_2026_volume1` — §1.1.3 Historical Bottlenecks of First-Order Nonlinear MIMO Control (Casti & Isidori Quotes) (PDF p.25, L4)

1.1.3 Decline of the State-Space Approach
State-space models rarely represent original models of dynamical control systems.
The original models of physical dynamical systems are the set of basic equations,
either differential or difference, or mixed, established by the system mechanism, or by
certain physical laws. They often appear in the form of a set of high-order differential
equations. While the well-known first-order state-space models are converted from
this set of basic equations based on, essentially, the method of variable extension.
State-space models are a type of extreme models which possess the lowest order of
differentials but the maximum number of (scalar) equations.
In terms of system control, how well do state-space models work? They worked
well for typical linear systems from the 1960 to the 1980s, but after that, they encoun-
tered insurmountable difficulties in handling nonlinearities, time-varying properties,
time delays, system constraints and issues of controllability, and consequently entered
into a truly difficult situation, as asserted by many facts including the following:
• As early as 1982, in a survey paper by Casti (1982), it was described that “seeking
a completely general theory of nonlinear systems is somewhat akin to the search
for the Holy Grail: a relatively harmless activity full of many pleasant surprises
and mild disappointments, but ultimately unrewarding.” Because of this, he then
made the suggestion: “A far more profitable path to follow is to concentrate upon
special classes of nonlinear problems, usually motivated by applications, and to
use the structure inherent in these classes as a guide to useful (i.e., applicable)
results.”
• A book entitled Rise of The Machines: A Cybernetic History, written by Rid
(2016), and published by Felicity Bryan Associates Ltd., even made the follow-
ing appalling and exaggerating claims: “The history of cybernetics holds several
warnings. The new field’s scientific popularity peaked around 1969. By the 1980s,
cybernetics had lost a great deal of academic respectability; it had ‘died of dry
rot.’ ” “Today, the most serious scholars working on cybernetics are historians of
science and cultural scholars, engineers and computer scientists abandoned it in
droves, renaming their projects and their degrees. “Cybernetics”, nearly seventy
years after the word was coined, sounds oddly old-fashioned and out-of-touch.”
• In 2001, a selected reprint volume entitled: “Control Theory: Twenty-Five Seminal
Papers (1932–1981)” was published by the IEEE Press (Basar, 2001). The editorial
board for this special volume is led by Tamer Basar and includes Brian D. O.
Anderson, Karl J. Åström, John Baillieul, Bruce A. Francis, Alberto Isidori, Petar
V. Kokotović, Huibert Kwakernaak, William J. Levine, Lennart Ljung, David Q.
Mayne, and Jan C. Willems. The 12 most authoritative control scientists could
have chosen to include some papers published within the 20 years from 1981 to
2001, but they did not.
• It was also claimed by Alberto Isidori in an open talk given at Seoul National
University, South Korea, on September 1, 2017, that “Inexplicably, in the case
of nonlinear systems, while most of the methods for the analysis of the internal
structure have been conveniently extended (in the 1980s and early 1990s), from the
mid 1990s, the study of problems of feedback design for MIMO nonlinear systems
came to a (almost complete) stall.” He then asked “Where are MIMO systems
gone?” “Why was this the case? Was the study of these problems irrelevant? Or
was it too difficult?” (see Fig. 1.1).
• As these observations became widely acknowledged, in 2010, the assertion “con-
trol is dead” sparked debate within the global control community. Distinguished
figures, including Graham Goodwin (University of Newcastle, Australia) and Yu-
Chi Ho (Harvard University, USA), were among those who mentioned or explained
the assertion. Yu-Chi Ho made the following points: “Currently everyone agrees
that the field of control is in this mature third stage. The framework and foundation
of the main stream control system thinking is very clear. Most application works
have been standardized and more or less routine. Academic research efforts are
basically third generation problems removed from real world dealing with theoret-
ical extensions within the established framework whether the subject is H-infinity,
robust control or LMI.” He also commented that “Control is dead until it is reborn
like Lazarus by a Jesus miracle. In this sense, one can argue CONTROL is certainly
not dead and now may be waiting for the ‘second coming’ of another golden age
of control. But chances are it won’t be from extending the current mature theory.”
“Why was this the case?” Alberto Isidori’s question is certainly worth our serious
consideration.
The reason actually lies in the fact that state-space models, which have dominated
the modern control theory for centuries, are not the best ones to handle control
problems. Such a reason is generally hard to be recognized and also difficult to be
accepted because most of us are working with state-space models. As a matter of
fact, state-space models were originally proposed to deal with problems directly
tied to the states: linear state-space models were firstly used by Euler in early 1750
for solving high-order linear differential equations (giving the state responses), and
nonlinear ones were used by Lyapunov in 1892 to analyze the limit behavior of the
states. Exceptionally, state-space models have been successfully used in the control
of typical linear systems because LTI systems without delays are easy to handle.
While state-space models are not the best, would there be a better one to perform
control tasks?

---

## 2. 定常线性闭环与完整特征结构参数化设计自由度（LTI Closed-Loop & Parametric DOFs）

### [14] `tcyb_2024_overview` — Remark 4 Wide Scope Reduced to a Single Eigenstructure Assignment Pair (PDF p.9, L1118)

Remark 4: It is often seen that one class of problems is
converted into another one in science research, but the above
particular conversion is special in two aspects: 1) the scope
of the problems can be converted is astonishingly wide, as
we have seen; 2) the finally converted problem turns out to
be not a class, but a single one, namely, the eigenstructure
assignment of a specific pair of matrices (Φ (00∼n−1) , Bc),
which is determined by only two parameters n and r.

### [15] `ijss_2021_part1` — Remark 3.2 Complete Parametric Freedom in Closed-Loop Matrix F (PDF p.10, L1063)

Remark 3.2: It is seen from the above result that as
long as the matrix F is chosen stable, the closed-loop
system is stable. Clearly, there are quite some free-
dom in the selection of F, while on the other hand
we also have the parameter matrix Z, which provides
m2n degrees of freedom. All these degrees of freedom
can be further utilised to achieve additional perfor-
mance of the system (see, e.g. Duan, 1992, 1993; Duan
et al., 2002, 2000; Duan & Zhao, 2020.

### [16] `ijss_2021_part7` — Remark 5.1 Decoupled Simplicity vs Coupled Parametric DOFs (PDF p.19, L1951)

Remark 5.1: The decoupled control design is obvi-
ously very simple, while the advantage of the cou-
pled design is that it provides much more degrees of
freedom. This can be clearly seen from

η η
dfreedomc − dfreedomd = ∑(∑rkriμi − rk2μk)
k=1 i=1
η η
= ∑∑rkriμi.
k=1 i=1
i≠k

When properly utilised, these extra degrees of freedom
can make the system perform much better.

### [17] `ijss_2022_part8` — Remark 4.3 Global Stabilization & Infinite-Horizon Optimal Control via FAS (PDF p.9, L927)

Remark 4.3: Generally speaking, it is hard to achieve
global stabilisation (including infinite-time optimal
control) of nonlinear systems. However, as demon-
strated by the above Theorem 4.3, once a nonlinear
system is represented in a HOFA system form, global
stabilisation can be easily realised. What is more,
the closed-loop system is even linear (which obvi-
ously implies global exponential stabilisation). This
fact again demonstrates the great advantage of the
HOFA design approaches.

### [18] `ijss_2022_part9` — Remark 3.1 Generalized PID Advantages & Parametric Tracking (PDF p.8, L853)

Remark 3.1: The generalised PID controller (7) pos-
sesses two advantages:

(1) it guarantees asymptotical tracking to a constant
vector under an arbitrary constant disturbance,
and often works practically well enough with slow
time-varying tracked vectors and disturbances;
and
(2) it provides very smooth and steady transient
response due to the relations in (27).
As a matter of fact, the relation (27) is really
an extra and seldom by-product. For instance,
when such a generalised PID controller is applied
to a second-order system, besides the velocity
signals, the acceleration signals also converge to
zero.

### [19] `ijss_2022_part10` — Remark 5.2 Decoupled and Decentralized Structure of Discrete FAS Control (PDF p.13, L1418)

Remark 5.2: The design given in Theorem 5.2 is
a decoupled one, and the u∗(t) given in the con-
troller (48) is in fact a decentralised one. This is ade-
quate to show the advantage of the HOFA approach.
However, a coupled design can also be carried out, with
the expression of u∗(t) in (48) replaced by

∗ ⌈0∼ϖp−1⌉
u (k) = Kxp (k) |p=1∼η − v (k) ,

where K ∈ ℝr×κ is a feedback gain. For details, one
can refer to the coupled design for continuous-time
HOFA systems given in Duan (2021c).

### [20] `scis_2022_discdelay1` — Remarks 2–3 Decentralized Design & Complete Parameterization for Delay FAS (PDF p.13, L815)

Remark 2. The design given in Theorem 1 is a decoupled one, and u∗(k) given in the controller (46)
is in fact a decentralized one. This is adequate to show the advantage of the FAS approach. However, a
coupled design can also be carried out, with the expression of u∗(k) in (46) replaced by

u∗(k) = Kx⌈p0∼̟p−1⌉(k) |p=1∼η + v (k) ,

where K ∈ ℝr×κ with
κ = r1̟1 + r2̟2 + · · · + rη̟η
is a feedback gain. For details, one can refer to the coupled design given in [26] for the continuous-time
case.
Remark 3. Another aspect associated with the control design of a discrete-time delay FAS is the
complete parameterization of the designs. Since constant linear closed-loop systems are obtained, as done
in the continuous-time case, complete parametric expressions for the feedback gains in the controllers as
well as the closed-loop systems can be established, which provide all the design degrees of freedom to be
used for further improving the system performance.

### [21] `book_2026_volume1` — §1.2.1–1.2.2 Eliminating Complicated Nonlinearities & Physical-to-Mathematical HOFAS (PDF p.27, L6)

Fortunately, besides the state-space models, there exists another type of system
models, namely the FAS models, proposed by Duan (2020a, 2020b, 2021a). With
such models, we can easily eliminate the nonlinear terms using the full-actuation
structure, no matter how complicated the nonlinear terms are, but as long as they are
measurable. Eventually, an LTI closed-loop system is obtained.
FASs physically exist, but only as a minor part of the set of control systems. How-
ever, when this concept is mathematically generalized, a high-order FAS (HOFAS)
becomes a general model for control systems. As a matter of fact, most nonlinear
systems can be either physically modeled as, or converted into HOFASs. This fact
has been demonstrated in Duan (2020a, 2020b).
1.2.2 FASs: From Physical to Mathematical
In certain practical applications, there exists a type of physical systems which are
referred to as FASs. They are often modeled as Lagrangian systems (a type of dif-
ferential equations of second order), and are widely encountered in the mechanical,
electrical and aerospace fields. They are of the type from which the control vectors
can be explicitly solved out, and are therefore inherently more straightforward to
be controlled. What is more, LTI closed-loop systems with some initial value con-
straints can often be obtained. As a matter of fact, many systems originally modeled
by physical laws, such as Newton’s Law and the Lagrangian Equations, fall naturally
into this category of FASs.
After all, the set of physical FASs is small. How about the control of the so many
UASs and the so many systems which are neither FASs nor UASs? Very recently,
the physical concept of FAS is generalized mathematically, and a new methodology
termed as FAS approach has been proposed. Instead of converting the model of a
general dynamical system into a state-space one, the FAS approach converts it into a
so-called mathematical FAS model. Then, similar to a physical FAS, the converted
mathematical FAS can be easily controlled and a linear closed-loop system can often
be obtained with an arbitrarily assignable eigenstructure.
In general, a state-space model is obtained from the original system’s fundamental
equations by the method of variable extension. As a result, a state-space model has
the lowest differential order but the maximum number of (scalar) equations which is
in general greater than the number of control variables. What happens if we apply the
method of variable elimination to the original set of fundamental equations? —The
system order will increase, and the number of (scalar) equations will decrease. Then,
how small could the number of equations be? Generally speaking, it is limited by the
number of control variables. When the number of equations is less than the number
of control variables, an over-actuated system is derived, and when they are equal, a
mathematical FAS, or a sub-FAS, is there ready for utilization. Hence, FAS models
are another type of extreme system models which possess the highest system orders
but the fewest scalar equations.

---

## 3. 对比经典反步法：克服“微分爆炸 / 复杂性爆炸”与多阶严反馈归约

### [22] `aas_2020_part1` — 说明 1 对比反步法与滑模控制（非线性闭环 vs 定常线性闭环） (PDF p.7, L687)

说明 1. 严格反馈系统的控制方法很多. 反步
法和滑模控制的优点是鲁棒性好, 但所获得的闭环
系统也多为非线性的. 由定理 2 知严格反馈系统可
以化为高阶全驱系统, 因此可以得到线性定常的闭
环系统.

### [23] `aaas_2024_subsfs` — 说明 对比传统反步法的三大优势（无微分爆炸、普适亚严反馈、线性闭环） (PDF p.8, L800)

说明 由本节结果可见，本文方法较传统反
步法具有下述优点：
1）反步法存在“微分复杂性爆炸”问题，本文
方法所涉及到的亚全驱系统求解过程不存在“微
分复杂性爆炸”问题，控制律设计简单易行。
2）对于亚严反馈系统的情形，反步法只能处
理一些非常特殊的个类系统，而本文给出的则是
一般性的处理方法。
3）基于反步法的设计不一定总能保证闭环
系统的指数收敛性，但利用本文方法则可以在可
行域范围内实现系统响应按照线性规律指数收
敛的结果。

### [24] `ijss_2021_part1` — Remark 4.2 Applicability Beyond Triangular Strict-Feedback Structure (PDF p.13, L1340)

Remark 4.2: This example system does not obey the
triangular structure of a strict-feedback system, hence
the well-know method of backstepping is generally
not applicable. Furthermore, with only the assump-
tion (56), the conditions for the well-known method
of feedback linearisation are also not met. Yet with the
proposed HOFA system approach the problem is well
solved in the sense that a constant linear closed-loop
system is obtained with a desired eigenstructure.

### [25] `ijss_2021_part2` — Remark 2.3 Two Core Advantages of HOFA Over Backstepping (PDF p.7, L701)

Remark 2.3: The proposed HOFA system approach is
generally more effective than the method of backstep-
ping because of the following two facts:

• The HOFA system approach can always produce a
constant linear closed-loop system, but the method
of backstepping can not;
• Due to the well-known problem of ‘differential
explosion’, the method of backstepping is generally
not applicable to a SFS with more than 3 or 4 subsys-
tems, while the HOFA system approach is, noting
that the proposed recursive solutions are easy to
realise.

### [26] `ijss_2021_part3` — Remarks 5.3–5.4 Why High-Order Backstepping Needs Fewer Steps Than First-Order (PDF p.16, L1731)

Remark 5.3: The above high-order backstepping
method for high-order systems appears to be more
complicated in description. It should be noted that,
in many specific engineering applications, mi, i =
1, 2, . . . , n often take the values of 1 and 2. So the fact
is, in such applications, the mixed-order backstepping
method is even simpler than that of the second-order
systems.

Remark 5.4: For a specific practical system of high-
order, direct application of the high-order backstep-
ping generally requires fewer steps than application
of the normal first-order backstepping method, since
there are more subsystems in the converted first-order
SFS. What is more, application of high-order back-
stepping also saves the process of converting the high-
order subsystems originally obtained from physical
modelling into first-order ones. Therefore, to solve a
specific practical problem, the method of high-order
(or mixed-order) backstepping is generally simpler
than the normal first-order method of backstepping.

### [27] `ijss_2021_part3` — Remark 6.1 4-Step First-Order Backstepping vs Direct High-Order Design (PDF p.18, L1904)

Remark 6.1: If the system (109) is converted into
the first-order state-space model, then the converted
model is composed of 4 subsystems, and eventually
four steps of backstepping are needed to solve the
problem. Experience with normal first-order back-
stepping designs tells us that the design process for the
converted first-order systems with four steps of back-
stepping is definitely much more complicated than the
above process.

### [28] `ijss_2021_part4` — Remark 5.2 Avoiding Differential Explosion in Adaptive High-Order Backstepping (PDF p.15, L1604)

Remark 5.2: It is commonly known that the method
of backstepping can hardly be applicable to a SFS with
many subsystems due to the well-known ‘differential
explosion’ problem. Such a problem of course applies
to the newly proposed second- and high-order meth-
ods of backstepping. Nevertheless, for a specific sys-
tem physically modelled by, e.g. Lagrangian Equation,
a second-order method of backstepping needs only
half of the steps of the first-order method of back-
stepping, and also saves the process of converting the
second-order system into a first-order one. Therefore,
the method of high-order (or mixed-order) backstep-
ping is generally simpler than the normal first-order
method of backstepping.

### [29] `ucfas_2025_part1` — Remarks 6.2–6.3 Avoiding Doubled Layers & Differential Explosion in SFSs (PDF p.10, L1104)

Remark 6.2: In Duan (2021a), the SFSs have been
generalised into second-order SFSs and mixed-order
SFSs. On the one hand, it has been proven that such
second-order SFSs and mixed-order SFSs can also be
equivalently converted into FASs. On the other hand,
corresponding high-order backstepping designs are
also established. As a matter of fact, many practical
systems are in fact in the form of a high-order, or
mixed-order SFS. Converting them into the first-order
SFS not only adds an extra computational burden, but

also makes the backstepping design much more com-
plicated since in this case the layers in the converted
first-order SFS are doubled. Now, corresponding to
the UC-SFSs in first-order form, we can also propose
second-order and mixed-order UC-SFSs.

Remark 6.3: In the state-space approach, SFSs are
coped with the well-known backstepping designs. As
is commonly known, the backstepping design is sub-
ject to a big problem of ‘differential explosion’ or
‘computation explosion’ when an SFS has more lay-
ers. Yet, in the FAS approach, it has been shown in
Duan (2021a) that an SFS can be easily converted into
a FAS by applying an iterative procedure, and there-
fore can be always easily stabilised in the sense of
producing a time-invariant linear system with desired
eigen-polynomials. But with a backstepping design, a
time-invariant closed-loop system cannot be always
achieved. In other words, within the FAS approach,
SFSs are actually shown to belong to the category of
feedback linearisable systems.

### [30] `scis_2024_chained2` — Remark 3 FAS vs Backstepping on Generalized Chained Systems (PDF p.11, L693)

Remark 3. As pointed out in [1], the above Problem 2 can be indeed solved by applying the well-
known backstepping technique. However, as it is well-known, the method of backstepping suffers from the
serious problem of “complexity explosion”, which renders the application of the method of backstepping
extremely difficult or even impossible when the dimension of the system is large. Furthermore, compared
with the FAS approach given in Section 5, the method of backstepping may have two drawbacks:
(1) It is not guaranteed that a UGE stable closed-loop system can be always obtained as the UGE
stabilizability of system (27) requires UGE stabilization of SFS (54);
(2) It does not always provide a linear closed-loop system like the FAS approach does.
Remark 4. Please note that, although η0 is an initial value of system (10), relative to the original
Problem 1, it is only an external design parameter. Hence it can be allowed to be set to any desired
value. From this point of view, choosing η0 = −βζ0 may just sufficiently and perfectly solve the problem
in the above sense of converting the problem into Problem 2. However, as an initial value of system (10),
after all, η0 may affect the response of system (10), that is, x0 (t) and u0 (t) , and hence that of the whole
system.
Owing to the above Remark 4, let us now also give a treatment for the case of η0 ≠ −βζ0, which will
produce a continuous controller.

### [31] `book_2026_volume1` — §1.4 Preview: High-Order Backstepping Greatly Reduces Differential Explosion (PDF p.57, L36)

Both Chaps. 9 and 10 propose high-order backstepping for high-order SFSs. More
specifically, Chap. 9 concentrates on the high-order backstepping for robust control
of uncertain SFSs, while Chap. 10 concentrates on high-order backstepping for
adaptive control of high-order SFSs with parametric uncertainties. In both chapters,
two types of high-order SFSs are considered, namely the second-order SFSs subject
to uncertain dynamics or unknown parameter vectors, and the mixed-order SFSs
subject to uncertain dynamics or unknown parameter vectors. Correspondingly, the
direct second-order backstepping strategy and the direct mixed-order backstepping
strategy are proposed. The proposed high-order backstepping method is a great con-
tribution of the FAS approach which greatly reduces the possibility of “differential
explosion” of the normal first-order method of backstepping. Effect of the proposed
high-order backstepping is demonstrated via a numerical example.

### [32] `book_2026_volume1` — Remark 6.4 Two Core Advantages of FAS Approach Over Backstepping (PDF p.227, L209)

Remark 6.4 The proposed FAS approach is generally more effective than the method
of backstepping because of the following two facts:
• the FAS approach can always produce an LTI closed-loop system, but the method
of backstepping cannot;
• due to the well-known problem of “differential explosion”, the method of back-
stepping is generally not applicable to an SFS with more than 3 or 4 subsystems,
while the FAS approach is, noting that the proposed recursive solutions are easy
to realize.

### [33] `book_2026_volume1` — Remark 7.2 Canonical Two-Point Summary of FAS Advantages Over Backstepping (PDF p.251, L233)

Remark 7.2 As pointed out in Duan (2021b), the FAS approach has two distinctive
advantages compared with the backstepping method. First, the FAS approach can
always produce an LTI closed-loop system. Second, the FAS approach can avoid the
“differential explosion” problem, which makes the method of backstepping generally
not applicable to an SFS with more than 3 or 4 subsystems.

---

## 4. 对比反馈线性化并延伸至亚全驱（sub-FAS）、奇异陷阱与非完整临界有理系统

### [34] `tcyb_2024_overview` — Remark 2 Why FAS Approach Is Much More Than Feedback Linearization (PDF p.5, L571)

Remark 2: Some readers who are not yet familiar with the
FAS approach might be mistaken that the FAS approach is
nothing but feedback linearization. The above result can only
tell that feedback linearization is a special case of the FAS
approach, but not vice versa since the FAS approach also
treats systems not in the state-space form, and can solve the
stabilization of systems which have already been proven to
be not feedback linearizable. Indeed, the FAS approach really
does much more than the feedback linearization technique.

### [35] `tcyb_2023_subfas` — §I Motivation of Sub-FAS & Substabilization for Non-Linearizable Systems (PDF p.2, L230)

More specifically, for nonlinear systems
which are not completely controllable (or not globally feed-
back linearizable in the state-space representation), a sub-FAS
model of such a system is often obtained, which defines, when
designing the controller of the system using the FAS approach,
a singular set on which the controller is not well defined. This
naturally leads to a problem of substabilization of the system.

### [36] `jssc_2022_casestudy` — Remark 2.3 Sub-FAS Handling Singular Sets Passing Through the Origin (PDF p.5, L248)

Remark 2.3 This system falls into such a scope whose equivalent FAS model is a sub-FAS
with its singularity set containing the origin. In general, such systems are difficult to handle,
and many typical benchmark systems for feedback stabilization in the literature in fact fall into
such a scope. This particular feature makes the system not feedback linearizable, and makes
the linearized model of the system at the origin an uncontrollable one.

### [37] `jssc_2022_casestudy` — Remark 3.3 Overcoming Smooth Feedback-Linearization Obstruction on Irregular Feasible Set (PDF p.7, L369)

Remark 3.3 For this example system (1), it is well-known that it is not feedback lineariz-
able by a smooth state feedback controller, and equivalently, it is not globally exponentially
stabilizable by a smooth state feedback controller. While in this section, it is clearly shown
that from which subset in the initial value space the trajectories of the closed-loop system can
be made decaying to the origin exponentially by a smooth state feedback controller.

### [38] `scis_2024_chained1` — §6.2 Pre-Controller Ease, Nonholonomic Systems as Sub-FASs & State/Derivative Constraints (PDF p.23, L1425)

When the initial values are inevitably chosen out of the ROEA ℚ, a pre-controller can be easily designed
(see also [2, 3, 49]), to drive the trajectory of the closed-loop system onto the ROEA ℚ first, and then
let the above controller (99) take over. Clearly, the design of such a pre-controller is much easier than
solving a stabilizing controller because the ROEA is generally a very large region, while stabilization in
the Lyapunov sense requires convergence of the states to a single point, which is usually the origin.
Finally, let us point out that the general theory of sub-FAS provides a general framework for dealing
with nonholonomic systems. As a matter of fact, sub-FAS describes a larger category covering nonholo-
nomic systems. Eventually, the nonholonomic constraints generally produce a singular set containing
the origin, often as a boundary point. The FAS approach provides a general approach for dealing with
systems possessing constraints on the state variables and their derivatives.

---

## 5. 高阶能控性、能观性与控制器显式求解的统一（突破 Kalman 线性状态空间局限）

### [39] `aas_2020_part2` — Abstract Critique of Kalman State-Space Controllability & FAS Necessary/Sufficient Criterion (PDF p.1, L59)

Abstract In this paper, development in controllability of dynamical systems described by first-order state-space models
is firstly overviewed briefly, and problems with the controllability theory originally introduced by Kalman are pointed out.
It is then proven that a necessary and sufficient condition for a constant linear system to be controllable is that it can
be equivalently expressed as a high-order fully-actuated system, and this result is also generalized, in a sense, to the case
of nonlinear systems. Based on this discovery, complete-controllability of general dynamical systems is defined. Together
with some other important properties, significance of super-controllability is clearly revealed as such that the system can
be turned, by a feedback controller, into a high-order constant linear system with the coefficient matrices of the closed-loop
eigen-polynomial being arbitrarily assignable.

### [40] `aas_2020_part2` — 说明 2–3 以控制变量为核心的全驱能控性及高阶导数可测性等价 (PDF p.9, L953)

说明 2. 由定义 2 可知, 全驱系统是一类以控制
变量为核心的系统, 本质上可以几乎显示解出控制
变量 u. 进一步由定义 3 可知, 完全能控的系统就是
可以求解出控制变量的系统. 控制系统的状态空间

模型以系统的状态为核心, 对于求解系统的状态响
应、状态观测与估计等问题自然提供了方便, 但对于
求解系统的控制问题并没有提供多少益处. 由命题
2 可见, 控制系统的高阶全驱模型则为求解控制问
题提供了 “天然” 条件.
说明 3. 上述控制律 (62) 要求基础状态 x 及其
相关的各阶导数的信息. 这些信息是系统 (57) 的最
基本的信息, 很多情况下都是可测的. 如果系统 (57)
是由某个一阶状态空间模型转化所得, 由于这种转
化的可逆性, 容易证得, 当原系统的状态可测时, 必
有系统 (57) 中的 x 及其相关的各阶导数可测, 而且
这些信息还可以从模型转化过程中的变换关系获得.
当然, 这些信息必要时也可以通过设计系统 (57) 的
状态观测器获得.
上述事实的意义是重大的. 它允许我们将很多
非线控制问题直接转化成线性系统领域中的相应控
制问题. 下面仅以几例概括一下这种思想.

### [41] `ijss_2021_part7` — §3.2 Consistency Between Controllability Verification and Control Design (PDF p.11, L1132)

With
this definition, it is obvious that

• all dynamical control systems, not only those in
state-space representations, possess the concepts of
controllability;
• the problem of controllability analysis and the prob-
lem of control are now highly consistent in the sense
that, once the controllability of a system is veri-
fied by obtaining the HOFA model of the system,
the design problem is then easily solved in view of
Proposition 3.1.

### [42] `scis_2023_delay1` — Remark 4 Extending Controllability Beyond State-Space Representations (PDF p.20, L1294)

Remark 4. With this definition, the following is obvious:
(1) all dynamical control systems, not only those in state-space representations, possess the concepts
of controllability;
(2) the problem of controllability analysis and the problem of control are now highly consistent in the
sense that, once the controllability of a system is verified by obtaining the FAS model of the system, the
design problem is then easily solved in view of Theorems 1 and 2.

---

## 6. 天然抗扰、时变/输入时滞超前对消、单向连接（UC-FAS）与输出依赖输出反馈（OD-FAS）

### [43] `ijss_2021_part6` — Remark 2.1 Natural Anti-Disturbance Property of HOFA Controllers (PDF p.6, L560)

Remark 2.1: It is clearly seen from (11) that some con-
stant disturbances, slope disturbances, etc., may auto-
matically disappear when the HOFA system method is
used for design. Therefore, the HOFA system approach
itself has certain ‘natural’ anti-disturbance character-
istics. In certain situations, the control of a system
subject to disturbances can be turned in a control
problem free of disturbances (see the examples in
Duan (2021a, 2021b, 2020a, 2020b)).

### [44] `ijss_2021_part6` — Remark 4.1 Complete Parametric Freedom in Disturbance Decoupling (PDF p.12, L1290)

Remark 4.1: The above theorem has provided a para-
metric approach for the problem of disturbance decou-
pling in the HOFA system (17). The design degrees
of freedom are explicitly given by the parameters
F1 ∈ ℂnr×nr, Z1 ∈ ℝr×nr and Z2 ∈ ℝr×kp, which can
be further properly selected to meet additional per-
formance requirements of the closed-loop system. It
should be also noted that explicit parametric solutions
of Lx and Ld satisfying the first condition in the above
Theorem 4.5 can be also readily established using state
feedback eigenstructure assignment results for linear
systems (see, Duan, 1992b, 1993a, 1998, 2004, 2005).
We point out that there exist usually also certain
degrees of freedom in the solution of Lx and Ld sat-
isfying the first condition in the theorem, and the case
of dynamic state feedback will be further addressed in
the next subsection.

### [45] `tcyb_2023_robustdelay` — Remark 1 Generality of Time-Delay FAS Models (PDF p.3, L404)

Remark 1: The above FAS model (6) or (7) might be
easily mistaken to be very special due to the full-actuation
Assumption A0 or B0. However, as discussed in [26], [28],
and [34], it really serves as a general model for controllable
dynamical systems. Many practical systems that obey certain
laws of physics, such as Newton’s second law, conservation
of linear and angular momentum, and Lagrangian equations
of motion, can initially be modeled as FASs, while those can-
not be directly modeled, can usually be converted into FASs.
Specifically, it has been shown that all completely control-
lable systems can be converted into FASs [34], [40], and these
include, but are not limited to the following typical systems
in state-space forms:
1) linear controllable systems, including both the
continuous-time ones [27], [44] and discrete-time
ones [37];
2) linear controllable time-delay systems, including
discrete-time ones with both state and input constant
delays [38], [39], and continuous-time ones with a
constant input delay;
3) feedback linearizable systems, including both the
continuous-time ones [26] and discrete-time ones [37];
4) strict-feedback systems, including the continuous-time
ones [26], [29] and discrete-time ones [37], and both
with time-varying delays [40], [41];

5) some more general types of nonlinear
systems [27], [28], [37].

### [46] `tcyb_2023_robustdelay` — Remark 3 Dynamic Input-Delay Compensation Within FAS Framework (PDF p.7, L878)

Remark 3: It is very important to point out that, in the case
that the delay term of the control, namely, ζu, is present, the
controller (40)-(41) also forms a dynamic system with respect
to the variable u. Therefore, the unexpected phenomenon may
arise that, although the states x(0∼m−1) and z(0∼n−1) are con-
verging to the origin, the control input u may still diverge or
possess a periodic oscillating property. This phenomenon is
in fact caused by the instability of the dynamical system in
which the variable u is no longer an external vector but an
internal one. Therefore, careful attention is really needed in
applications when the open-loop system possesses an input
delay.

### [47] `ucfas_2025_part3` — §1 Extending Beyond Single FAS/sub-FAS via Unidirectionally Connected FASs (PDF p.2, L136)

In spite of the fact
that numerous dynamical systems can be converted
into FASs and their control can be more effectively
solved by the FAS approach, there are still systems
which cannot be converted into a single FAS or sub-
FAS. Part I of this series of papers, Duan (2025b),
shows that an extra tremendously big class of sys-
tems, which cannot be converted into a single FAS,
or sub-FAS, can be converted into the form of a
group of FASs or sub-FASs, with unidirectional con-
nections. Such a type of systems is termed as uni-
directionally connected FASs (UC-FASs). In Part II,
Duan (2025a), the sub-stabilisation of weakly UC-
FASs is proposed, and several examples, including

some generalised well-known nonholonomic example
systems, are presented. This paper further investi-
gates the applications of the proposed sub-stabilisation
approach for UC-FASs. To do this, let us outline
the models of certain maneuvered moving objects
(MMOs).

### [48] `odfas_2026_part1` — Remark 4.1 Finer Substabilization Perspective on Khalil/Isidori Benchmark System (PDF p.14, L1631)

Remark 4.1. We mention that this is a typical
example system extensively examined in the lit-
erature, e.g., in Bin and Hou (2024); Byrnes and
Isidori (1991); Khalil (2002); A. R. Teel (1992),
this example system has been used to demon-
strate semi-global output stabilization. Specifi-
cally, this system has been treated in the Ex-
ample 13.16 of Khalil (2002), the Example 3.3.1
of Bin and Hou (2024), the Example 1.1 of
A. R. Teel (1992), and the Example 8.2 of Byrnes
and Isidori (1991). We here treat the static out-
put feedback control of this example system from

the angle of substabilization. The result turns
out to be finer and more intuitive.

### [49] `odfas_2026_part4` — Remark 7.1 Position vs Velocity Output-Feedback Observability & Error Dynamics (PDF p.50, L2861)

Remark 7.1. Section 4 and this section treat systems with the same state equation, but with

different output equations. In Section 4, only x is measured, and in this section, only x ˙ is measured.

By comparing the results in this section and Section 4, we can find the following differences between

the two cases:

1. the position information automatically can ensure the observability of the velocity and the dis-

turbance, but the velocity information cannot unless extra assumptions, namely, Assumptions

Av1 and Av2, are added;

2. once Assumptions Av1 and Av2 are met, the case of velocity feedback admits an LTI observation

error equation, but the case of position feedback needs the observation error to obey an LTV

system whose stability requires an extra assumption, namely, Assumption Ap2.

Remark 7.2. Similar to the treatment in Subsection 5.4, the output feedback tracking control of

system (7.1) with disturbance rejection can be also solved under certain conditions.

### [50] `book_2026_volume1` — §1.2.3 Summary of Resolved Nonlinear Control Areas & Extensions (PDF p.30, L9)

The FAS approach, owing to its distinct and well-recognized advantages, has
attracted widespread attention since the emergence of the seminal works in two sets
of papers Duan (2020a, 2020b, 2020c, 2021a, 2021b, 2021c, 2021d, 2021e, 2021f,
2021g, 2022e, 2022d, 2022f). By now, over a hundred research groups from at least
70 institutions across the globe have begun to delve into the field. Hundreds of papers
on the FAS approach have been published, and a large portion of these has appeared in
Automatica and various IEEE Transactions [see the overview paper Duan (2024e)].
The FAS approach has been instrumental in resolving many nonlinear control
problems, encompassing areas such as robust control, adaptive control, disturbance
rejection, optimal control, and tracking control. Several issues, insurmountable or
inadequately addressed with the state-space method, have been effectively and sat-
isfactorily resolved using the FAS approach. Frequently, the closed-loop systems
derived through the FAS approach have been rendered linear and stable, or glob-
ally exponentially stable or sub-stable. By now, we have extended the methodology
to diverse domains including discrete-time systems, time-delay systems, and also
stochastic systems.

---

## 7. 客观适用边界与防夸大红线表述（肯定状态空间滤波/观测优势，区分更好求解 vs 求解新问题）

### [51] `ijss_2022_part10` — Remark 5.4 Distinct Roles of State-Space Response Analysis vs FAS Control (PDF p.13, L1447)

Remark 5.4: Response analysis and stability analy-
sis are two very fundamental and important aspects
of system analysis. Generally speaking, these two
problems are very hard to treat with the state-space
approaches for general nonlinear dynamical control
systems. However, as it is clearly seen in the above
Theorems 5.1 and 5.2, with the proposed HOFA
approaches these two problems really vanish since
they are both converted into corresponding problems
for linear systems. As is well-known that many con-
trol systems design approaches are based on, and also
limited by, certain stability analysis results. While it
is now clearly seen that the provided HOFA system
approaches are such a type of approaches which are
not dependent on stability analysis results and there-
fore are not subject to the conservatism brought about
by the stability analysis results..

### [52] `tcyb_2024_overview` — §IV-E Scope Conditions & Necessary Modifications for Uncertainties/Parameters (PDF p.10, L1153)

Regarding the above procedure, we have the following
statements.
• The original physical system is not necessarily in the
state-space form, but may be in any form as originally
modeled by physical laws. It may be as complicated
as to possessing time-varying features and time delays.
However, this basic procedure is not directly applicable
to those original systems with dynamical uncertainties or
unknown parameters. To cope with systems with dynam-
ical uncertainties, unknown parameters, disturbances and
reference signals, the procedure needs to be modified in
certain ways.
• In certain complicated applications, the above procedure
may be applied repeatedly to some subsystems, but not
the whole original physical system.
• The homeomorphism φ may not be necessarily a global
one. It may be a homeomorphism defined on a subset
of the whole system state space. In most cases, it is a
diffeomorphism.
• Assured by theory, the closed-loop response obtained in
Step 4 always converges to zero exponentially. However,
this may not be the case for the closed-loop response
corresponding to the original system. It also depends on
the homeomorphism φ−1. Usually, convergence to zero
is guaranteed, but may not be exponential.

### [53] `book_2026_volume1` — Preface: Objective Distinction Between Global FAS ('Better Way') and Volumes II–III ('Problems State-Space Cannot Solve') & Delay Superiority (PDF p.7, L7)

The present Volume I focuses on global FASs, which provides the basic idea and
a more fundamental scheme for the FAS approach. Senior researchers on nonlinear
control may find that this volume does not solve problems that the state-space
approach does not solve, but it does solve many problems in a better way. It will
be found in Volumes II and III that the FAS approach indeed can solve many prob-
lems that the state-space approach can not. This Volume I is a book to begin with,
while Volumes II and III are for researchers to further go in-depth.
It is pointed out that the FAS approach is superior to dealing with time-varying
and time-delay systems. However, as an elementary introduction to FAS approach,
these presently planned book volumes do not include contents related to time-delay
systems.

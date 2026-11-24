# Sorted Proposition Corpus Across 32 Duan First-Author Papers + Volume I (90 items)

## [1] `aaas_2024_subsfs` (PDF p.4, L457)

命题 1 假设 1 满足 ，变量 B k( x1~k，t) 和
hk( x1~k，t) ( k = 1，2，…，n )由式（3）~式（5）给出，

则当 x1~n ∈ 𝔽̂时，变换式（6）在 𝔽̂上是一个一一映
射（是 𝔽 上的一个同胚），且保持原点不动。

## [2] `aaas_2024_subsfs` (PDF p.6, L670)

命题 2 𝕊 = 𝕊̂，𝔽 = 𝔽

## [3] `aas_2020_part1` (PDF p.4, L334)

命题 1. 对于任何给定的定常矩阵 Ai, i =
0, 1, · · · , m − 1, 都可以选取全驱系统 (8) 的下述控
制律
m−1
u = −B−1(·) Aix(i) + f(x,x, ˙ · · · , x(m−1), t) − v
i=0
(9)
获得如下的线性定常闭环系统

Ex(m) + Am−1x(m−1) + · · · + A1x + A0x = v
˙
(10)

鉴于矩阵 Ai, i = 0, 1, · · · , m−1, 的任意性, 我
们可以通过合理地选择这些矩阵获得希望的闭环系
统特性. 第 4 节将从闭环系统的特征结构配置角度
出发对此给出具体的参数化方法.

## [4] `aas_2020_part1` (PDF p.10, L1093)

命题 2. 设 T∞c, V∞ c ∈ Rmn×n0 由式 (50)-(52)
给出, 则闭环系统是正则的当且仅当下述二式之一
成立:

det (T∞c)T AcV∞c ≠ 0 (66)

det T∞TAm−1V∞ − T∞ TBW∞ ≠ 0 (67)

在具体设计应用中, 为了保证闭环系统的正则
性, 可以在求取设计参数矩阵 W∞ 时, 考虑加上约
束 (66) 或 (67).
本节针对高阶全驱系统提出了一种直接参数
化设计方法. 对于系统为二阶情形和当假设 A3
中的 n0 = n 时, 可参见相关的文献 [41−42]. 相
关结果也推广到含有输入导数项的高阶全驱系统
中[43], 所提出的全驱系统设计方法也应用到实际系
统中[44−49]. 更多有关全驱系统的设计和应用可参见
文献 [50−51].

## [5] `aas_2020_part2` (PDF p.8, L895)

命题 1. 一阶状态空间模型描述的线性定常系
统 (4) 的完全能控性与其通常意义下的能控性等价.
尽管在线性定常系统的情况下, 完全能控性与
其通常意义下的能控性是等价的, 但由定理 3 和 4

8 期

以及文献 [54] 中的定理 2 和 3 可以推知, 在非线性
系统的情况下, 能控性的定义有多种, 某些意义下能
控的系统不一定都是完全能控, 即完全能控系统仅
是某些意义下能控系统的一个真子集. 因此, 在非线
性的情况下, 完全能控性和卡尔曼意义下的一些能
控性之间还是有缝隙的. 事实上, 文献 [55] 中所给
出的非线性系统的能控规范型只代表一类一阶非线
性完全能控系统.
根据上述定义 3, 机器人领域中的下述系统

M(x,x, t ˙)¨x + D(x,x, t ˙) ˙x + K(x,x, t ˙)x = u (61)

其中 M(·)、D(·) 和 K(·) ∈ Rn×n 分别为系统的广
义质量矩阵、广义阻尼矩阵和广义刚度矩阵, 是完全
能控的. 航天器控制中所涉及的许多系统也是完全
能控的[55−56]. 文献 [1] 中所涉及的积分型系统、串
联系统、严格反馈型系统和可反馈线性化的系统都
是完全能控的. 更重要的是, 现在不只是对于一阶的
状态空间模型描述的系统才有能控性定义, 而是对
任何连续系统都有能控性的定义了.

## [6] `aas_2020_part2` (PDF p.9, L931)

命题 2. 对于任意给定的定常矩阵 Ai ∈
Rn×n, i = 0, 1, · · · , m − 1, 都可以选取高阶全驱
系统 (57) 的下述控制律
m−1
w = − Aix(i) + f(x,x, ˙ · · · , x(m−1), t) − ν
{ i∑=0
u = g−1(w)
(62)

获得如下的线性定常闭环系统

Ex(m) + Am−1x(m−1) + · · · + A1x + A0x = ν
˙
(63)

上述命题为文献 [1] 中高阶仿射系统情形的自然推
广.
鉴于矩阵 Ai, i = 0, 1, · · · , m − 1 的任意性, 总
可以通过合理地选择这些矩阵获得希望的闭环系统
特性. 文献 [1] 从闭环系统的特征结构配置角度出发
对此给出了具体的参数化方法, 并提供了系统设计
中的所有自由度.

## [7] `aas_2020_part3` (PDF p.3, L237)

命题 1. 单输入线性定常系统

x˙ = Ax + bu, A ∈ Rn×n, b ∈ Rn
y = cx, c ∈ R1×n (5)

能观的充要条件是其等价于 Luenberger 第二能观
测规范型 (4), 其中 αi, i = 0, 1, · · · , n − 1 为矩阵 A
的特征多项式系数, 由下式决定:

det(sI − A) = sn + αn−1sn−1 + · · · + α1s + α0
(6)

βi, i = 0, 1, · · · , n − 1 为如下定义的一组常数:

βn−1 = cb
βn−2 = cAb + αn−1cb

... (7)
β1 = cAn−2b + αn−1cAn−3b + · · · + α2cb
β0 = cAn−1b + αn−1cAn−2b + · · · + α1cb

线性系统能观的充要条件是其可以化成 Luen-
berger 第二能观规范型 (4), 但是显然不是所有能观
的非线性系统 (1) 都能化成上述规范型 (2).
值得说明的是, 上面定义的非线性系统的能观
规范型 (2) 具有下述特点:

段广仁: 高阶系统方法 — III. 能观性与观测器设计

1) 与线性系统的能观规范型 (4) 一样, 其输出
方程只与 x ¯n 有关;
2) 状态方程中的非线性部分也只与 x ¯n 有关.

## [8] `aas_2020_part3` (PDF p.4, L339)

命题 2. 线性系统 (16) 能观的充要条件是其
代数等价于下述 Luenberger 第二能观规范型:

x ˙˜ = ˜Ax˜ + ˜Bu
(17)
y = C˜x˜

其中 x ˜, A˜ 由式 (10) ∼ (13) 给出, 矩阵 B˜, C˜ 具有下
述特殊结构:

B˜1 bi0

B˜2 bi1 µi×r
B˜ = , B˜i = ∈ R (18)
... ...
B˜m bi,µi−1

C˜ = C1 C2 · · · Cm
0 · · · 0 0

... ... ... ...
0 · · · 0 0
(19)
Ci = 0 · · · 0 1 ∈ Rm×µi

0 · · · 0 ci+1,i

... ... ... ...
0 · · · 0 cm,i

由式 (19) 中矩阵 C 的结构可见, 线性系统
能观标准型 (17) 中的输出方程只与一批主向量
x˜1µ1,x ˜2µ2, · · · ,x ˜mµm 相关. 同样, 非线性系统的能
观规范型 (9) ∼ (15) 中的输出方程也只与这些主向
量相关, 而且其状态方程中的非线性部分也只是这
些向量的函数. 事实上, 规范型的这一点要求并不苛
刻, 文献 [19] 已经从理论上证明了许多非线性系统
都可以通过状态变换化成类似的形式. 但是, 这一特

46 卷

点却为我们后面设计完全能观非线性系统的状态观
测器提供了极大的方便.

## [9] `aas_2020_part3` (PDF p.8, L838)

命题 3. 给定高阶全量测系统 (44), 或其状
态空间实现 (47) ∼ (50), 对于任意给定的定常矩阵
Pi ∈ Rn×n, i = 0, 1, · · · , m−1, 都可以选取该系统
的状态观测器 (52) 中的参数矩阵

Li = Ai − Pi, i = 0, 1, · · · , m − 1 (55)

46 卷

使得系统 (47) ∼ (50) 在观测器 (52) 下的观测误差
方程为

E∆e ˙ = Ψ(P0, P1, · · · , Pm−1)e (56)

注意到

det(sE∆ − Ψ(P0, P1, · · · , Pm−1)) =
det(Esm + Pm−1sm−1 + · · · + P1s + P0)
(57)

上述命题说明, 对于非线性完全能观系统, 可以设
计其观测器使得观测误差系统为一个线性定常系统,
且其特征多项式的系数矩阵还可以任意配置.
下面进一步说明一下这些系数矩阵 Pi ∈
Rn×n, i = 0, 1, · · · , m − 1 的配置方法.
注意到

ΨT(P0, P1, · · · , Pm−1) = ΨT(0) − B∆K (58)

其中

0

...
Ψ(0) = , B∆ = (59)
0
In

K = P0 P1 · · · Pm−1 (60)

系数矩阵 Pi ∈ Rn×n, i = 0, 1, · · · , m − 1 的求取问
题可以通过求解下述系统

E∆Tx˙ = ΨT(0)x + B∆u (61)

的状态反馈特征结构配置来解决.
关于广义线性系统状态反馈特征结构配置问题
的求解, 可以参阅相关文献 [32 − 36]. 特别地, 对于
上述这一特殊系统 (61) 的特征结构配置问题, 文献
[37] 给出了一种具体的参数化设计方法, 并提供了
系统设计中的所有自由度.
文献 [1] 和 [37] 针对完全能控非线性系统给出
了一种状态控制律设计方法, 使得闭环系统为线性
定常的, 且具有希望的闭环特征结构. 本文的方法则
提供了完全能观非线性系统状态观测器的设计方法.
通过两方面的有机结合可以给出完全能控、完全能
观非线性系统的基于状态观测器的控制系统设计方
法.

## [10] `fasta_2026_roea` (PDF p.3, L347)

Proposition 1. Suppose Φ (A0∼n−1) possesses different sta-
ble real eigenvalues. Then
1) ϕi (t), i = 1, 2, ..., m, are smooth if c (t) is smooth;
2) ϕi (t), i = 1, 2, ..., m, are bounded and tend to zero if
c (t) is bounded; and
3) ϕi(t), i = 1, 2, . . . , m, have a finite number of station-
ary points on [0, +∞) if c(t) ≡ c.

Main Results

## [11] `ijss_2021_part1` (PDF p.5, L489)

Proposition 2.2: Let Ai ∈ ℝr×r, i = 0, 1, . . . , m − 1,
be a set of given matrices, then the following controller

u = −B−1 x(0∼m−1), ζ A0∼m−1x(0∼m−1) + u∗
{ ( ) ( )
u∗ = f x(0∼m−1), ζ − v,
( )
(6)

for the fully actuated system (3) produces the following
constant linear closed-loop system

Ex(m) + A0∼m−1x(0∼m−1) = v. (7)

When expanded, the above linear system (7) can be
also written as

Ex(m) + Am−1x(m−1) + · · · + A1x˙ + A0x = v.

Due to the arbitrariness of the series of matri-
ces Ai, i = 0, 1, . . . , m − 1, closed-loop systems with
desired performance can be obtained by properly
selecting these matrices. A parametric approach for
solving these Ai, i = 0, 1, . . . , m − 1 has been given
in Duan (2020a), which also provides all the design
degrees of freedom (see also Section 3.5).
A generalised form of system (3) appears as follows
(Duan, 2020b):

Ex(m) = f (x(0∼m−1), ζ) + g (x(0∼m−1), ζ, u), (8)

where g(·) ∈ ℝn is also a sufficiently differentiable vec-
tor function. In the case of m = 1, E = Ir and p = 0,
the system turns into the following well-known form:

x˙ = f (x) + g (x, u) . (9)

The above more general system (8) is called fully
actuated on Ω, if n = r and for t ≥ 0, the mapping
w = g(x(0∼m−1), ζ, u) forms a differential homeomor-
phism from u to w for all ζ ∈ ℝp and x(i) ∈ Ωi, i =
0, 1, . . . , m − 1; it is called (globally) fully actuated if
w = g(x(0∼m−1), ζ, u) ∈ ℝr forms a differential home-
omorphism from u to w for all ζ ∈ ℝp and x(i) ∈
ℝn, i = 0, 1, . . . , m − 1. Sub-full-actuation on Ω can
also be similarly defined.
For the more general fully actuated system (8), a
result similar to Proposition 2.2 still holds. In this case,
the controller corresponding to (6) becomes

w = − mi=−01Aix(i) − f x(0∼m−1), ζ + v
{ ∑ ( ) (10)
u = g−1 w, x(0∼m−1), ζ ,
( )
and the same closed-loop system as in (7) is achieved.

## [12] `ijss_2021_part1` (PDF p.10, L1041)

Proposition 3.5: For an arbitrarily chosen F ∈
ℝmn×mn, all the matrix A0∼m−1 and the nonsingular
matrix V ∈ ℝmn×mn satisfying

Φ(A0∼m−1) = VFV−1

are given by

A0∼m−1 = −ZFnV−1(Z, F) ,

Z
⎡ ⎤
ZF
V = V (Z, F) =
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
ZFn−1

where Z ∈ ℝm×mn is an arbitrary parameter matrix
satisfying

det V (Z, F) ≠ 0.

## [13] `ijss_2021_part3` (PDF p.9, L860)

Proposition 3.6: For an arbitrarily chosen F ∈ ℝnr×nr,
all the matrix A0∼n−1 and the nonsingular matrix V ∈
ℝnr×nr satisfying

Φ(A0∼n−1) = VFV−1

are given by

A0∼n−1 = −ZFnV−1(Z, F) ,

Z
⎡ ⎤
ZF
V = V (Z, F) =
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
ZFn−1

where Z ∈ ℝr×nr is an arbitrary parameter matrix sat-
isfying

det V (Z, F) ≠ 0.

## [14] `ijss_2021_part3` (PDF p.18, L1946)

Proposition 6.1: The uncertain term in system (128)
satisfies

Δf (z(0∼3) ≤ ρ (z(0∼3)),
||| )||
|

with

ρ (z(0∼3)) = γ1 |˙z| + γ2z˙2 |¨z|
( )
+ σ2 |z| |...z − 2zz˙| + γ1 |˙z|2 .
( )

## [15] `ijss_2021_part4` (PDF p.7, L702)

Proposition 3.3: For an arbitrarily chosen F ∈ ℝnr×nr,
all the matrix A0∼n−1 and the nonsingular matrix V ∈
ℝnr×nr satisfying

Φ(A0∼n−1) = VFV−1

are given by

A0∼n−1 = −ZFnV−1(Z, F) ,

Z
⎡ ⎤
ZF
V (Z, F) =
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
ZFn−1

where Z ∈ ℝr×nr is an arbitrary parameter matrix
satisfying

det V (Z, F) ≠ 0.

To meet the requirement, it suffices to choose a diag-
onal matrix F with negative diagonal elements. In the
case that complex eigenvalues are expected, we may
have such a block

−a −b
[ ], (16)
b −a

with a and b being two positive scalars, included as a
diagonal block in F.
Further, to solve the matrix P(A0∼n−1) satisfying
the Lyapunov matrix equation (6), we introduce the
following notations related to a square matrix Φ ∈
ℝn×n:
n
det (sI + Φ) ≜ ∑ciΦsi,
i=0
n−1
adj sI + ΦT ≜ ∑CiΦsi.
( )
i=0

Then we have the following result which is simplified
from Duan (2015, p. 356).

## [16] `ijss_2021_part4` (PDF p.7, L750)

Proposition 3.4: If Φ ∈ ℝn×n is Hurwitz, then, for an
arbitrary positive definite matrix Q ∈ ℝn×n, the follow-
ing Lyapunov equation

ΦTP + PΦ = −Q

has a unique solution given by

n−1
P = −∑CiΦQP0−1Φi, (17)
i=0

with
n
P0 = ∑ciΦΦi. (18)
i=0

Clearly, there are quite some degrees of freedom in
the selection of F, while on the other hand we also have
the parameter matrix Z, which provides r2n degrees of
freedom. All these degrees of freedom can be further
utilised to achieve additional performance of the sys-
tem (see, e.g. Duan, 1992, 1993; Duan et al., 2002, 2000;
Duan & Zhao, 2020).

## [17] `ijss_2021_part5` (PDF p.11, L1108)

Proposition 6.1: For an arbitrarily chosen F ∈ ℝnr×nr,
all matrices A0∼n−1 and V ∈ ℝnr×nr satisfying det V ≠
0 and

Φ(A0∼n−1) = VFV−1

are given by

A0∼n−1 = −ZFnV−1(Z, F) ,

Z
⎡ ⎤
ZF
V (Z, F) =
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
ZFn−1

where Z ∈ ℝr×nr is an arbitrary parameter matrix
satisfying

det V (Z, F) ≠ 0.

Clearly, there are quite some degrees of freedom in
the selection of F, while on the other hand we also have
the parameter matrix Z, which provides r2n degrees of
freedom. All these degrees of freedom can be further
utilised to achieve the additional performance of the
system (see, e.g. Duan, 1992, 1993; Duan & Zhao, 2020;
Duan et al., 2000, 2002).
In addition, it should be pointed out that when the
uncertain nonlinear terms and unknown parameters
⌢
do not exist, only the basic part u0 or u0 is left in the
designed control law. In such a case, the closed-loop
system is a constant linear one with assignable closed-
loop eigenstructure, and the problem reduces to the
standard problem in Duan (2020a).

## [18] `ijss_2021_part6` (PDF p.5, L447)

Proposition 2.1: The above strict-feedback system (2),
with Gi, i = 1, 2, . . . , n being nonsingular, can be trans-
formed into the form of

z(n) = f (z(0∼n−1), ζ, t) + Δf (z(0∼n−1), ζ, t) + Lnu,
(3)
with z = x1, and

Lk = G1G2 · · · Gk, k = 1, 2, . . . , n, (4)

f1(n−1)(z, ζ, t)
⎡ ⎤
f2(n−2)(z, x2, ζ, t)
f (z(0∼n−1), ζ, t) = L0∼n−1 ... ,
⎢⎢⎢⎢⎢⎢⎢⎣ ⎥⎥⎥⎥⎥⎥⎥⎦
f˙n−1(x1∼n−1, ζ, t)

fn(x1∼n, ζ, t)
(5)

Δf(n−1)(z, ζ, t)
⎡ ⎤
Δf2(n−2)(z, x2, ζ, t)
Δf (z(0∼n−1), ζ, t) = L0∼n−1 ... ,
⎢⎢⎢⎢⎢⎢⎢⎣ ⎥⎥⎥⎥⎥⎥⎥⎦
Δf˙n−1(x1∼n−1, ζ, t)

Δfn(x1∼n, ζ, t)
(6)

where L0 = I, and in (5) and (6) the xk, k = 2, 3, . . . , n
and their derivatives are all given or determined
by certain transformation (see the Theorem 3.1 in
Duan, 2020b).

Similarly, it can be shown via the Theorems
3.2, 3.3 and 3.6 in Duan (2020b) that the second-
and high-order strict-feedback systems proposed in
Duan (2020b), with uncertainties properly added, can
be also converted into the form of the HOFA system
(1).

## [19] `ijss_2021_part7` (PDF p.10, L1011)

Proposition 3.1: Let Ω ⊂ ℝκ be a desired open set,
and 𝔽 ⊂ ℝκ be the set of feasible points of the sys-
tem (8), whose dimension is greater than 1. Further,
let [Ai]0∼μi−1 ∈ ℝri×μiri, i = 1, 2, . . . , η, be a set of
arbitrarily given matrices. Then the following controller

[A1] (0∼μ1−1)
⎧ ⎛⎡ 0∼μ1−1 x1 ⎤ ⎞
[A2] (0∼μ2−1)
0∼μ2−1 x2
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨u = −B−1(·) + u∗
⎜⎜⎜⎜⎜⎜⎝⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ ⎟⎟⎟⎟⎟⎟⎠
(0∼μη−1)
[Aη]0∼μη−1xη

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩u∗ = f (xk(0∼μk−1)|k=1∼η, ζ, t) − v,
(30)
for system (8) produces the following constant linear
closed-loop system

xk(μk) + [Ak]0∼μk−1xk(0∼μk−1) = vk, k = 1, 2, . . . , η,
(31)
with vk, k = 1, 2, . . . , η, being defined by

v1
⎡ ⎤
v2 rk
v = vk ∈ ℝ , (32)
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
vη

provided that the states of the above closed-loop system
(31) satisfy

x(0∼μk−1)|k=1∼η ∈ 𝔽. (33)
k

## [20] `ijss_2021_part7` (PDF p.11, L1143)

Proposition 3.1.

Now let us consider again modelling a physical sys-
tem Σphysical by mechanism. To be more strict, let us
impose the following assumption:

## [21] `ijss_2021_part7` (PDF p.12, L1185)

Proposition 3.3: Let (26) be the set of basic equa-
tions of the original physical system Σphysical satisfying

## [22] `ijss_2021_part7` (PDF p.14, L1386)

Proposition 4.1: Consider the system represented by
(26), or the original physical system Σphysical, satisfying

## [23] `ijss_2021_part7` (PDF p.15, L1567)

Proposition 4.5: Let the system represented by (26), or
the original physical system Σphysical, satisfy Assump-
tion A1. Then it may possess a high-order system model
consisting of a HOFA model in the form of (48) and an
extra subsystem of the form

yk(γk)|k=1∼ξ = g (yk(0∼γk−1)|k=1∼ξ, ζ, t, u), (57)

where the variables are as stated before.

Different from the extra subsystem (49), the sub-
system (57) shares the common control vector u with
the HOFA system (48). An affine form of the above
system (57) is obviously given by

yk(γk)|k=1∼ξ = g (yk(0∼γk−1)|k=1∼ξ, ζ, t)

+ H(yk(0∼γk−1)|k=1∼ξ, ζ, t)Lu, (58)

where L is some constant matrix of full-row rank, and
H(·) is a matrix of appropriate dimensions and is not
necessarily nonsingular or even square.
Corresponding to systems of type I, we further give
the following definition.

## [24] `ijss_2021_part7` (PDF p.21, L2182)

Proposition 6.3: Let a0, a1 and β be positive scalars,
u0(t) and v0(t) be continuous and bounded, and v0(t)
satisfy the following condition

|v0 (t)| ≥ γ , ∀t ≥ 0, (100)

for some γ > 0. Then the controller (97) is bounded
(feasible) if the initial condition y0 = y(0) is chosen
different from zero and has the same sign as v0(0), that is

y0v0 (0) > 0. (101)

It is understandable that signal tracking can be fur-
ther easily considered by properly selecting the exter-
nal signals u0(t) and v0(t). The above proposition tells
us that signal tracking in such a system can be realised
‘almost’ globally. What is more, the system variables y
and z are governed by a linear system, while the sys-
tem variable x given by (94) can be easily reasoned to
be bounded.

## [25] `ijss_2021_part7` (PDF p.22, L2237)

Proposition 6.4: Let a0, a1 and β be positive scalars
satisfying Assumption A2. Further assume

(1) y(0) ≠ 0, and
(2) αi > β > 0, i = 1, 2,

then the system variables x, y, z and the controller
given in (102) all converge exponentially to zero.

## [26] `ijss_2022_part10` (PDF p.6, L564)

Proposition 3.1: The linear system (1) is controllable if
and only if it can be converted equivalently into a high-
order system in the form of

(0∼μp−1)
(μ1) ⎡L1(xp |p=1∼η)⎤
⎡x1(μ2)⎤ (0∼μp−1)
x2 L2(xp |p=1∼η)
= + Buˆ, (3)
⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎦ ⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦
(μη)
xη (0∼μp−1)
Lη (xp |p=1∼η)

where μp, p = 1, 2, . . . , η, are a set of integers, xp, p =
1, 2, . . . , η, are a set of state vectors of proper dimen-
sions, Lp(·), p = 1, 2, . . . , η, are a set of linear functions,
andB is a square upper triangular matrix with diagonalˆ
elements all being 1.

The above result is in fact a modified form of the
Theorem 2 in Duan (2020b). It can be proven simply
following the proof therein.
A system in the form of (3) is called a linear HOFA
system with multiple orders if

rankBˆ = r = n. (4)

A typical special continuous-time linear HOFA system
is the following single-order one:
n−1
x(n) = Aix(i) + Bu, (5)
∑
i=0
where Ai ∈ ℝr×r, i = 1, 2, . . . , n, are a set of matrices,
and the matrix B ∈ ℝr×r is nonsingular.

## [27] `ijss_2022_part10` (PDF p.14, L1550)

Proposition 6.2: Let system (57) be locally feedback
linearisable at (x0, u0) via the feedback (58). Then the
system (57) is equivalent to both a step forward HOFA
system in the form of (40) within a neighbourhood of
(x0, u0), and a step backward HOFA system in the form
of (41) within a neighbourhood of (x0, u0).

For a proof of the above proposition, one can refer
to the appendix.
Particularly, when the system (57) is locally feed-
back linearisable via the following feedback

u (k) = ξ (x (k) , v (k)) = α (x (k)) + β (x (k)) v (k) ,
(61)

where α(x) and β(x) satisfy

α (x0) = u0, rankβ (x) = r, (62)

the above result becomes the following.

## [28] `ijss_2022_part10` (PDF p.15, L1609)

Proposition 6.4: Let fi(·) ∈ ℝr, and gi(·) ∈ ℝr×r, i =
1, 2, . . . , n, are sufficiently differentiable nonlinear func-
tions. Then the above system (63), with Assumption A2
satisfied, can be equivalently converted into both a step
forward HOFA system in the form of (28), and a step
backward HOFA system in the form of (29).

For a proof of the above proposition, refer to the
appendix.
The importance of the above result lies in that, once
a strict-feedback system is converted into a HOFA
model, the system can be easily controlled in view
of Theorems 5.1 and 5.2, with the closed-loop sys-
tem being a constant linear one with an arbitrarily
assignable eigenstructure. It should be noted that such
an advantage is not generally achievable with the well-
known method of backstepping. We point out that the
converted HOFA model is a global fully actuated one
due to Assumption A2. Therefore, the thorny problem
of singularity vanishes.
To finish this section, let us make some further
remarks.

## [29] `ijss_2022_part10` (PDF p.18, L1926)

Proposition 7.4: The above system (77) satisfying
Assumption A3 can be equivalently converted into the
step backward HOFA system (65).

For a proof of the above proposition, one can refer
to the appendix.

## [30] `jssc_2022_brockett1` (PDF p.6, L288)

Proposition 3.1 Let y (0) ≠ 0, then a controller for the system (1) can be designed as
in (8), which results in the following closed-loop system

1
⎧ x˙ = − (a0z + (a1 − γ) xy) ,
⎪⎪ y
⎪⎪⎨ (9)
y˙ = −γy,

⎪⎪⎪⎪ z˙ = xy.
⎩
Furthermore, if, in addition,
a0 = αβ, a1 = α + β, (10)

with α and β being two real scalars satisfying

α > β > γ > 0, (11)

then all x (t) , y (t) , z (t) and u1 (t) , u2 (t) converge to zero exponentially as t → ∞.
A proof of the above result is provided in the appendix.
The above result indicates that, for this well-known example (1), there exists a smooth
controller (8) which “almost” globally exponentially stabilizes the system since all trajectories
starting from the initial value space

ℝ30 = {(x0, y0, z0) | x0, y0, z0 ∈ ℝ} (12)

go to the origin except those starting from the x0-z0 plane.

## [31] `jssc_2022_brockett1` (PDF p.7, L359)

Proposition 3.2 Let x (0) ≠ 0, then a controller for the system (1) can be designed as
in (17), which results in the following closed-loop system

⎧ x˙ = −γx,

⎪⎪⎪⎨ y˙ = −1 (a0z + (a1 − γ) xy) , (18)
x
⎪⎪⎪ z˙ = xy.
⎩
Furthermore, if, in addition, a0, a1 and γ are taken as in (10)–(11), then all x (t) , y (t) , z (t)
and u1 (t) , u2 (t) tend to zero exponentially.
Similar to Case A, the above result indicates that, for this well-known example (1), there
exists another smooth controller (17) which “almost” globally exponentially stabilizes the sys-
tem, since all trajectories starting from the initial value space ℝ30, defined in (12), go to the
origin except those starting from the y0-z0 plane.

## [32] `jssc_2022_brockett1` (PDF p.9, L457)

Proposition 4.1 Let x (0) ≠ 0 or y (0) ≠ 0, and a0, a1 and γ be taken to satisfy (10)–(11).
Then the above controller (22) gives the closed-loop system (9) when y (0) ≠ 0, and the closed-
loop system (18) when x (0) ≠ 0, and also guarantees that all x (t) , y (t) , z (t) and u1 (t) , u2 (t)
tend to zero exponentially as t → ∞.
The above result indicates that, for this well-known example system (1), there exists a
controller (22) which is smooth for all t > 0, and “almost” globally exponentially stabilizes the
system. Since the system initial values are required to satisfy

x (0) ≠ 0 or y (0) ≠ 0,

the region of attraction for the system is

ℚ = (x0, y0, z0) x20 + y02 ≠ 0 , (23)
{ || }
which is the whole three-dimensional space taking out only the z0-axis.

## [33] `jssc_2022_brockett1` (PDF p.12, L593)

Proposition 5.2 The following switching controller
−1
⎧ ⎡y x⎤ ⎡a0z + a1xy⎤
⎪⎪− , if x0 ≠ 0,
⎪⎪⎪ ⎣1 0⎦ ⎣ γx ⎦
⎪⎪⎪⎪ −1
⎪⎪⎪⎪ ⎡y x⎤ ⎡a0z + a1xy⎤
⎪⎪− , if y0 ≠ 0,
⎡u1⎤ ⎪⎪⎪ ⎣0 1⎦ ⎣ γy ⎦
= ⎪⎨ (26)
⎣u2⎦ ⎡σx − z0⎤ if x0 = y0 = 0,
⎪⎪⎪− ,
⎪⎪⎪ ⎣ γy ⎦ 0 ≤ t < t0,
⎪⎪⎪ −1
⎪⎪⎪⎪ ⎡y x⎤ ⎡a0z + a1xy⎤ if x0 = y0 = 0,
⎪⎪− ,
⎪⎪⎪ ⎣1 0⎦ ⎣ γx ⎦ t ≥ t0,
⎪⎩
globally stabilizes the system (1), where t0 is a positive number, and all the other variables are
stated as before.
Obviously, in the above controller (26), instead of (24), the finite-time pre-controller (25)
can also be used.

## [34] `jssc_2022_casestudy` (PDF p.4, L215)

Proposition 2.1 The state-space system (1) has an equivalent sub-FAS model (5). Fur-
thermore,
1) on the feasibility set 𝔽, a controller for the sub-FAS (5) can be given as (7), which results
in the following constrained linear closed-loop system

⎧ x¨ + a1x ˙ + a0x = 0,
⎨ (10)
x ∈ 𝔽;
⎩
2) once x and ˙x are obtained via the closed-loop system (9) or (10), the original variables
x1 and x2 of the state-space system (1) can be obtained from the following transformation

⎧ x1 = x,
⎨ 13 (11)
x2 = ( ˙x − x) ;
⎩

STABILIZATION VIA FAS APPROACH: A CASE STUDY 735

3) in the original coordinates (x1, x2), the feasibility condition becomes x2 ≠ 0, and the
controller (7) is equivalently given as

u = − 12 a0x1 + (1 + a1) x1 + x32 − v . (12)
3x2 [ ( ) ]

## [35] `jssc_2022_casestudy` (PDF p.6, L309)

Proposition 3.1 Let a0 and a1 be determined by (17)–(18), with α and β, α > β, being a
pair of distinct positive scalars, and the controller for the system (5) be designed as (7). Then,
1) the singularity condition ˙x = x is equivalent to

c (t) x0 + d (t) y0 = 0, (19)

where

c (t) = (1 + α) βe−(α−β)t − α (1 + β) ,
d (t) = (1 + α) e−(α−β)t − (1 + β) ;

2) the region of evaporation is given by

𝕎 = 𝕎1 ∪ 𝕎2, (20)

with
⎧ y0 − x0 ≤ 0 ⎫
𝕎1 = ⎨(x0, y0) ⎬, (21)
|||||| y0 + αx0 ≥ 0
⎩ ⎭
⎧ y0 − x0 ≥ 0 ⎫
𝕎2 = ⎨(x0, y0) ⎬, (22)
|||||| y0 + αx0 ≤ 0
⎩ ⎭
which is a sector field in the initial value plane (x0, y0) as shown in Figure 1.

STABILIZATION VIA FAS APPROACH: A CASE STUDY 737

The above result reveals the fact that the designed smooth controller (7) does make the
closed-loop system “almost” globally stable because it has a truly large region of attraction,
larger than any ball with a limited radius.

Figure 1 Region of evaporation for the sub-FAS

## [36] `jssc_2022_casestudy` (PDF p.7, L352)

Proposition 3.2 Let a0 and a1 be determined by (17)–(18), with α and β, α > β, being
a pair of distinct positive scalars, and the controller be designed as in (7) for the sub-FAS (5).
Then x (t) ,x ˙ (t) and u (t) all converge to zero exponentially as long as the system initial values
are taken from the region of attraction

ℚ = ℚ1 ∪ ℚ2,

with
⎧ y0 − x0 > 0 ⎫
ℚ1 = ⎨(x0, y0) ⎬, (23)
|||||| y0 + αx0 < 0
⎩ ⎭
⎧ y0 − x0 < 0 ⎫
ℚ2 = ⎨(x0, y0) ⎬. (24)
|||||| y0 + αx0 > 0
⎩ ⎭
For a proof of the above result, please refer to the appendix.

## [37] `jssc_2022_casestudy` (PDF p.10, L471)

Proposition 4.3 Let a0 and a1 be determined by (17)–(18), b > 1 + α, with α and β,
α > β, being a pair of distinct positive scalars. Then a globally stabilizing controller for the
system (1) is given,
1) when (x10, x20) ∈ ℚ, by

u = − 12 (1 + a0 + a1) x1 + (1 + a1) x32 ,
3x2 [ ]

2) when (x10, x20) ∈ 𝕎, by

⎧ −b x1x−22 + x2 , t ∈ [0, t0),
⎪ 3 ( )
u = ⎪⎨ 1
− 2 [(1 + a0 + a1) x1 + (1 + a1) x32], t ≥ t0,
⎪⎪⎩ 3x2

where t0 = 0 if x10 = 0, otherwise it is a time switching point determined by

x32(t) > sign (x10) ε, ∀t ≥ t0, (31)

where ε is some positive number satisfying

2b − 1 3
ε < b − 1 (bx10 + x20). (32)

As a matter of fact, it can be seen in the proof of the result given in the appendix that, for
some ε satisfying (32) there must exist a finite time instant t0 satisfying the condition (31).
An illustration of the above result is given in Figure 3.

Figure 3 Global stabilization using a pre-controller

## [38] `jssc_2022_freq` (PDF p.3, L166)

Proposition 2.1 The linear system (1) is controllable if and only if it can be converted
equivalently into a high-order system in the form of

z(µ1)
⎡ 1 ⎤ (0∼µp−1)
⎡ L1xp |p=1∼r ⎤
z(µ2) (0∼µp−1)

## [39] `jssc_2022_freq` (PDF p.6, L288)

Proposition 3.3 Let (N(s), D(s)) be right coprime and satisfy (11). If the generated
state vector Z (s) satisfies the fully actuated PMD model

D(s)Z(s) = U(s), (12)

then the state of the state-space model (1) can be given by

X(s) = N(s)Z(s). (13)

It follows that, a fully actuated PMD can be obtained for a linear state-space system once
an irreducible right MFD (N(s), D(s)) of its transfer function H(s) is obtained. However, there
may exist two problems:
1) Even (N(s), D(s)) is given, the generated state vector z (t), which satisfies (13), might
not be determined uniquely by x(t).
2) The time-domain expression for (12) might be a descriptor high-order linear state-space
system, rather than a conventional high-order linear state-space system.
To illustrate the above two problems, we give an example.

## [40] `odfas_2026_part1` (PDF p.4, L469)

Proposition 2.1. Let system (6) be a global
OD-FAS, and the system

{ x(n)(t) = fx(x(0∼n−1)(t − τi (t)) i=1∼p, t) + u0
y (t) = h x(0∼n−1), t
( )
(7)

possesses an output feedback stabilizing controller

u0 = α(y (t − τi (t))|i=1∼p , t)

in certain sense. Then the following output feed-
back controller

u (t) = −B−1(·, t) (fy (·, t) − u0)
{ (8)
u0 = α(y (t − τi (t))|i=1∼p , t)

stabilizes the global OD-FAS (6) (in the same
sense).

We point out that the stabilization mentioned
in the above Proposition 2.1 may be local or
global asymptotical stability or finite-time sta-
bility.

## [41] `odfas_2026_part1` (PDF p.7, L797)

Proposition 3.1. Suppose that system (25) is a
global OD-FAS, and there exists a controller

u0 (t) = β (y (t − τi (t))|i=1∼p , t), (28)

which stabilizes in certain sense the linear system
(27). Then

u (t) = −B−1(·, t) [fy (·, t) − u0 (t)]
{ (29)
u0 (t) = β (y (t − τi (t))|i=1∼p , t),

is a stabilizing output feedback controller in the
same sense for OD-FAS (25).

The above result converts the stabilization of a
nonlinear OD-FAS into that of a quasi-linear one.
It holds because the closed-loop system resulted
in by the output feedback controller (29) is easily
checked to be

x(n)(t)
p
= Fi,0∼n−1 (y (t) , t) x(0∼n−1)(t − τi (t))
{ i∑=1
+ β (C (t) x(0∼n−1)(t − τi (t)) i=1∼p, t)
y (t) = C (t) x(0∼n−1),
(30)
which is stable by assumption.
Please note that controller (28) can be linear
when system (27) is linear. In most cases, it may
be a dynamical compensator.

## [42] `odfas_2026_part1` (PDF p.11, L1326)

Proposition 3.2. Under diffeomorphism (68),
system (65) is equivalent to the following OD-

FAS: k Mgl 1 1
+ [ cos x − k( + )]
J1 J1 J1 J2
{ x(4) = A2 (y1) ¨x + fy (y1∼2) + J1kJ2u J1 k
y1∼2 = x(0∼1), (70) ×( x¨ − Mgl sin x + x) + u
k k J1J2
Mgl k Mgl k
where = ( cos x − ) ( sin x − x)
J1 J1 J1 J1
Mgl 1 1 Mgl 2 k2
A2 (y1) = cos y1 − k( + ), (71) − x sin x + x
J1 J1 J2 J1 ˙ J1J2
Mgl k Mgl 1 1
fy (y1∼2) = ( cos y1 − ) +[ cos x − k( + )]x¨
J1 J1 J1 J1 J2
Mgl k k Mgl 1 1
×( sin y1 − y1) + [ cos x − k( + )]
J1 J1 J1 J1 J1 J2
Mgl 2 k2 Mgl k
− y2 sin y1 + y1 ×(− sin x + x) + u.
J1 J1J2 k J1J2
k Mgl 1 1
+ [ cos y1 − k( + )] This gives the OD-FAS (70).
J1 J1 J1 J2
Mgl
×(y1 − sin y1) (72) 3.3.2. Stabilizing controller
k
Under the following control transformation:

## [43] `odfas_2026_part1` (PDF p.17, L1886)

Proposition 5.1. Let

π
|θ| < , c = M (b2 − b1) > 0,
2

and introduce the following diffeomorphism

ξ = b2θ + b1x
ξ˙ = b2θ ˙ + b1x ˙
{ (111)
ξ¨... = c sin θ
ξ = cθ˙ cos θ.

Then,

(1) the inverse of diffeomorphism (111) is
given by

θ = arcsin(1cξ¨)
θ˙ = √ 1 ...ξ
c2−ξ¨2
{ x = b11 (ξ − b2 arcsin(1cξ¨)) (112)

x˙ = b11 (ξ˙ − b2√ 21 2 ...ξ);
c −ξ¨

(2) under and the following controller transfor-
mation

u = M sin η1 − b1σ,

and the following output transformation

y1 = b2η1 + b1η3
{ y2 = c sin η1 (113)
y3 = cη2 cos η1,

system (109) is equivalently converted into
the following output-dependent sub-FAS:

ξ(4) = f (y2∼3) + B (y2) u
{ y1∼3 = Cξ(2∼3), (114)

where

y2 y32
f (y2∼3) = − 2 2, (115)
c − y2

B (y2) = c2 − y22, (116)

and

C = [ 1 0 01×2 ]. (117)
02×1 02×1 I2

(3) ξ(0∼3)(t) converges to zero exponentially
implies

lim θ(0∼1) (t) = 0, lim x(0∼1) (t) = 0,
t→+∞ t→+∞
(118)
exponentially.

## [44] `odfas_2026_part1` (PDF p.25, L2815)

Proposition 9.1. Let L = [ L1 L2 ]T make
AL Hurwitz. Then an observer producing the es-
timate of q3∼4 is given by

0 2 0
z˙ = ALqˆ3∼4 + [ Mgl ]y2 sin y1 + [ 1 ]u0
{ J1
qˆ3∼4 = z − [ L1 ]y2.
L2 − A2 (y1)
(156)
Furthermore, the observation error e = q3∼4 −
qˆ3∼4 obeys the following equation

e˙ = ALe. (157)

## [45] `odfas_2026_part2` (PDF p.6, L579)

Proposition 2.1: Let system (12) be a global OD-FAS,
anditscompanionsystem(14)possessesanoutputfeed-
back stabilising controller

u0 = α(y(t − τi(t))|i=1∼p, t)

in a certain sense. Then the following output feedback
controller

{︃ u(t) = −B−1(·, t)(fy(·, t) − u0)
(15)
u0 = α(y(t − τi(t))|i=1∼p, t)

stabilises the global OD-FAS (12) (in the same sense).

Wepointoutthatthestabilisationmentionedinthe
above Proposition 2.1 may be local or global asymp-
totic stability or even finite-time stability.
Theaboveresultindicatesthatoutputfeedbacksta-
bilisation of OD-FAS (12) totally depends on that of
itscompanionsystem.Becauseofthis,letusintroduce
the following concept.

## [46] `odfas_2026_part2` (PDF p.9, L1012)

Proposition 3.1: Suppose that condition (37) is met.
Then, under the above diffeomorphism (39), and the
output transformation (44), system (36) can be equiv-
alently converted into the following global OD-FAS:
⎧ [︃ ]︃
ξ¨1
(4) = f (y) + B(y)u
⎪⎪⎪⎪⎨ x ⎡ ⎤
ξ1 (46)
y = To⎣ x ⎦ .
⎪⎪⎪⎪⎩
x¨

## [47] `odfas_2026_part2` (PDF p.14, L1483)

Proposition 4.1: Suppose that system (82) is a global
OD-FAS, and there exists a controller

u0(t) = β(y(t − τi(t))|i=1∼p, t) (85)

whichstabilisesinacertainsensethelinearsystem(84).
Then
{︄ −1
u(t) = −B (·, t)[fy(·, t) − u0(t)]
(86)
u0(t) = β(y(t − τi(t))|i=1∼p, t),

is a stabilising output feedback controller in the same
sense for OD-FAS (82).

Theaboveresultconvertsthestabilisationofanon-
linear OD-FAS into that of a linear one. It holds
because the closed-loop system resulted in by the out-
put feedback controller (86) is easily checked to be
⎧ (µk)
xk |k=1∼η(t)
∑︂p
⎪⎪⎪⎪⎪⎪⎨ = Gi(t)xk(0∼µk−1)(t − τi(t))|k=1∼η
(87)
i=1
+β(ξ(t), t)
⎪⎪⎪⎪⎪⎪⎩ y(t) = C(t)xk(0∼µk−1)|k=1∼η,

with

ξ(t) = [C(t − τi(t))xk(0∼µk−1)|k=1∼η(t − τi(t))]i=1∼p,

which is stable by assumption.

Please note that controller (85) can be often linear
since system (84) is linear. In most cases, it may be a
linear dynamical compensator.

## [48] `odfas_2026_part2` (PDF p.15, L1655)

Proposition 4.2: Let fya(·) and fy b(·) be given by (93)
and (94), respectively, and matrix C be given by (99).
Then,underdiffeomorphism(91)andtheoutputtrans-
formation(97),system(88)isequivalenttothefollowing
OD-FAS:
⎧ ⎡ ⎤
[︃ ]︃
ξ ¨3 ⎣ − 1 d3ξ̇3 ⎦
x(4) = bm3 (1∼3)
−G1∼3x
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ [︃ ]︃
+ fy(y) + B u1 (100)
u2

ya = ξ3
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ yb = Cx(0∼3),

where
[︄ ]︄ ⎡ 1 ⎤
fya(y) 0 m3
fy(y) = b , B = ⎢⎣ k2 ⎥⎦ ,
fy (y) 0
m1m2

and Gb0 = 0,
[︃ 3 (︃ )︃ ]︃
b d1 d1 d2
G1 = 1 2 − − (k1 + k2) , (101)
m1 m1 m1 m2
(︃ )︃
b 1 d1 d2
G2 = d + , (102)
m1 m1 m2
b 1 d2
G3 = d + . (103)
m1 m2

## [49] `odfas_2026_part2` (PDF p.21, L2353)

Proposition 6.1: Let φ(x,x ¨) and ω(x,x ̇) be defined
by (144) and (145), respectively. Then

(1) transformation (146) implies

1
sin 2θ2 = φ(x,x ¨), (148)
c11
√︂
cos 2θ2 = 1 c112 − φ2(x,x ¨); (149)
c11

(2) transformation (146) is invertible if and only if

cos(2θ2) ≠ 0, (150)

or, equivalently,

|φ(x,x ¨)| < c11; (151)

(3) undercondition(150)or(151),theinverseof(146)
is given by
⎧
θ1 = x

θ̇1 =ẋ
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ (︃ )︃
1 1
θ2 = arcsin φ(x,x ¨) (152)
2 c11
1 ...
θ̇2 = √︂ [x − ω(x,x ̇)] ;
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ 2 c112 − φ2(x,x ¨)

(4) the above diffeomorphism (152) admits

lim θ(0∼1) = lim θ(0∼1) = 0. (153)
x(0∼3)→0 1 x(0∼3)→0 2

## [50] `odfas_2026_part2` (PDF p.22, L2470)

Proposition 6.2: Under diffeomorphism (146) and
condition(150)or(151),system(143)canbeconverted
into the following corresponding output-dependent sub-
FAS:
⎧[︃ (4)]︃ [︃ (0∼3) ]︃
x fy(x , θ2∼3)
=
θ¨3 hb(θ2∼3)
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ [︃ ]︃ [︃ ]︃
b(x,x ¨) 0 τ2
+ (159)
0 1 τ3

ya = x(0∼3)
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩
yb = θ3,

where
√︂
b(x,x ¨) = 2 c112 − φ2(x,x ¨), (160)

fy(x(0∼3), θ2∼3) = ¨x(c0 cos x − 2c11 cos 2x)

−ẋ2(c0 sin x − 4c11 sin 2x)

2φ(x,x ¨) 2
− [...x − ω(x,x ̇)]
c11b(x,x ¨)

+ b(x,x ¨)ha(θ1∼3). (161)

Furthermore, the feasibility set of the sub-FAS is given
by

{︂ }︂
𝔽 = x(0∼3)⃓⃓⃓ |φ(x,x ¨)| < c11 . (162)

## [51] `odfas_2026_part4` (PDF p.6, L450)

Proposition 2.1. Let M ∈ ℝn×n be nonsingular. Then, system (2.1) is controllable. Furthermore,

1. in the case of C0 = In and C1 = 0, system (2.1) is also observable; and

2. in the case of C0 = 0 and C1 = In, system (2.1) is observable if K is nonsingular.

The above result states that, for linear second-order systems, there always exists a stabilizing

controller using only position feedback, but a stabilizing controller using only velocity feedback may

not exist if K is singular.

For nonlinear second-order systems in the form of

{M (q) ¨q + D (q,q ˙) ˙q + K (q) q = u
(2.2)
y = C0q + C1q, ˙

the situation is much more complicated.

2.1.1. Pure position feedback It follows from Proposition 2.1 that, for a constant linear second-

order system with only position measurement, an output feedback stabilizing controller always exists.

Here let us show that, unlike the linear case, a nonlinear second-order system which is weakly control-

lable and observable may not be stabilized by a smooth static or dynamic output feedback controllers,

as demonstrated by the following simple counter example.

## [52] `odfas_2026_part4` (PDF p.17, L1014)

Proposition 4.1. Let Assumptions A1 and Aϕ1 be met, and Ao1 ∈ ℝr×r be an arbitrary Hurwitz

matrix. Then an observer giving the estimate of q2 can be given as follows:

z˙ = Ao1z + ΘIa(ϕ(0∼2))y + u0
{ (0∼1) (4.7)
qˆ2 = z − L(ϕ )y,

where

ΘIa(ϕ(0∼2)) = L˙(ϕ(0∼1)) − Ao1L(ϕ(0∼1)), (4.8)

L(ϕ(0∼1)) = Ao1 − R (ϕ) A1(ϕ(0∼1)). (4.9)

Furthermore, the observation error e = q2 −q ˆ2 is governed by the following equation

e˙ = Ao1e. (4.10)

## [53] `odfas_2026_part4` (PDF p.27, L1583)

Proposition 5.1. Let Assumptions A1-A2, Aϕ1, and AD be met, AoI(ϕ(0∼1)) be given by (5.11),

and L(ϕ(0∼1)) make AoI(ϕ(0∼1)) uniformly asymptotically stable. Then an observer producing simul-

taneously the estimates of q2 and d is given by

z˙ = AoI(ϕ) z − ΘIb(ϕ(0∼2))y +[Ir]u0
0
{ (5.13)
[qˆ2] = z − L ϕ(0∼1) y,
dˆ ( )

where

ΘIb(ϕ(0∼2)) = L˙(ϕ(0∼1))− AoI (ϕ) L(ϕ(0∼1)). (5.14)

Furthermore, the observation error

e = [q2]−[qˆ2] (5.15)
d dˆ

is governed by the following uniformly asymptotically stable system

e˙ = AoI(ϕ(0∼1))e. (5.16)

## [54] `odfas_2026_part4` (PDF p.30, L1759)

Proposition 5.2. Let Assumptions A1-A2 and Aϕ1, AD and Ap2 be met, and AL be given by

(5.18) with Li ∈ ℝr×r, i = 1, 2, making AL Hurwitz. Then an observer producing simultaneously the

estimates of q2 and d is given by (5.13)-(5.14), with AoI(ϕ) and L(ϕ(0∼1)) being given by (5.24) and

(5.23), respectively, Furthermore, the observation error (5.15) is governed by the uniformly asymptot-

ically stable system (5.25).

5.1.3. Case of A1(ϕ(0∼1)) = A1 (ϕ) In the case of A1(ϕ(0∼1)) = A1 (ϕ) , equation (5.9) becomes

(0∼1) [R (ϕ) A1 (ϕ) R (ϕ)]
AI (ϕ ) = AI (ϕ) = . (5.26)

## [55] `odfas_2026_part4` (PDF p.39, L2208)

Proposition 6.1. Let Assumptions A1 and Av1 be met, Ao2 ∈ ℝr×r be an arbitrary Hurwitz matrix,

and define

L(ϕ(0∼1)) = Ao2A−01(ϕ(0∼1))M (ϕ) , (6.8)

ΘIIa(ϕ(0∼2)) = L˙(ϕ(0∼1))− Ao2L(ϕ(0∼1))+ Ir. (6.9)

Then an observer giving the estimate of q1 can be given as follows:

z˙ = Ao2z + ΘIIa(ϕ(0∼2))y + L(ϕ(0∼1))u0
{ (0∼1) (6.10)
qˆ1 = z − L(ϕ )y.

Furthermore, the observation error e = q1 −q ˆ1 is governed by the following equation

e˙ = Ao2e. (6.11)

## [56] `odfas_2026_part4` (PDF p.41, L2312)

Proposition 6.2. Let Assumptions A1-A2 and Av1-Av2 be satisfied, and F0∼1 ∈ ℝr×2r be a matrix

making Φ (F0∼1) Hurwitz. Then a GUA stabilizing output feedback controller for system (6.5) is given

in the form of (4.20) with

K11(ϕ(0∼1)) = −K12(ϕ(0∼1))L(ϕ(0∼1)) − F1

K12(ϕ(0∼1)) = −(F0 + R (ϕ) A0(ϕ(0∼1)))

{K21(ϕ(0∼2)) = ΘIIa(ϕ(0∼2))+ L(ϕ(0∼1))K11(ϕ(0∼1)) (6.22)

K22(ϕ(0∼1)) = −L(ϕ(0∼1))F0,

where Ao2 is an arbitrary Hurwitz matrix, L(ϕ(0∼1)) is given by (6.8), and ΘIIa(ϕ(0∼2)) is given by

(6.9).

## [57] `odfas_2026_part4` (PDF p.45, L2581)

Proposition 7.1. Let Assumptions A1, AD, Av1 and Av2 be met, and

L(ϕ(0∼1)) = L] ϕ(0∼1))M (ϕ) ,
(
with L] ϕ(0∼1)) ∈ ℝ2r×r making system (7.9) uniformly asymptotical stable. Then an observer pro-
(
ducing the estimates of q1 and d simultaneously is given by

z˙ = AoII (ϕ(0∼1))z + ΘIIb(ϕ(0∼2))y + L(ϕ(0∼1))u0

{[qˆ1] = z − L ϕ(0∼1) y, (7.12)
dˆ ( )

where AoII (ϕ(0∼1)) is defined by (7.10), and

ΘIIb(ϕ(0∼2)) = L˙(ϕ(0∼1))− AoII (ϕ(0∼1))L(ϕ(0∼1))

+[Ir]. (7.13)
0

Further, the observation error

e = [q1]−[qˆ1] (7.14)
d dˆ

obeys the uniformly asymptotically stable system (7.9).

## [58] `odfas_2026_part4` (PDF p.47, L2711)

Proposition 7.2. Let Assumptions A1-A2, AD, Av1 and Av2 be met, AoII (ϕ(0∼1)) ∈ ℝ2r×2r be

given by (7.10) with L] ϕ(0∼1)) ∈ ℝ2r×r making system (7.9) uniformly asymptotical stable, and
(
L(ϕ(0∼1)) ∈ ℝ2r×r is given by (6.26). Furthermore, let F0∼1 ∈ ℝr×2r be a matrix making Φ(F0∼1)

Hurwitz. Then a GUA stabilizing output feedback controller for system (7.3) is given in the form of

u0 = K11(ϕ(0∼1))y + K12(ϕ(0∼1))z

{z˙ = K21(ϕ(0∼2))y + K22(ϕ(0∼1))z, (7.22)

with
K11(ϕ(0∼1)) = −K12(ϕ(0∼1))L(ϕ(0∼1))− F1

K12(ϕ(0∼1)) = −⌊F0 + R (ϕ) A0(ϕ(0∼1)) R (ϕ)⌋

{K21(ϕ(0∼2)) = L(ϕ(0∼1))K11(ϕ(0∼1)) + ΘIIb(ϕ(0∼1)) (7.23)

K22(ϕ(0∼1)) = AoII (ϕ(0∼1))+ L(ϕ(0∼1))K12(ϕ(0∼1)),

where ΘIIb(ϕ(0∼1)) is given by (7.13).

## [59] `odfas_2026_part4` (PDF p.54, L3053)

Proposition 8.1. Let

A0 = −G[, (8.16)

fy (y†, φ, t) = ˙φEy† − RT(φ) ¨η∗(t) . (8.17)

Then, under diffeomorphism (8.14) and the following output transformation

y = R (φ) y† −η ˙∗. (8.18)

system (8.12) can be equivalently converted into the following OD-FAS:

{RT(φ) ¨x = A0x + fy y†, φ, t + u + d
( ) (8.19)
y = ˙x.

## [60] `odfas_2026_part4` (PDF p.58, L3322)

Proposition 8.2. Let Assumption Aφ be satisfied, Ao2 be an arbitrary Hurwitz matrix, and F0∼1 ∈

ℝ2×4 be a matrix making Φ (F0∼1) Hurwitz. Then a GUA stabilizing output feedback controller for

system (8.34) is given by
{uζ = K11 (φ) y1 + K12 (φ) z
z˙ = K21 φ(0∼1) y1 + K22 (φ) z, (8.43)
( )
with
K11 (φ) = −K12 (φ) Ao2A−111RT0(φ) − F1
K12 (φ) = −F0 − R0 (φ) A11
{K21 φ(0∼1) = ΘIIa φ(0∼1) + Ao2A−111R0T(φ) K11 (φ) (8.44)
( )o (−1 T )
K22 (φ) = A (Ir + A11 R0 (φ) K12 (φ)),

where ΘIIa φ(0∼1) is given by
( )

ΘIIa(φ(0∼1)) = −φA ˙o2A−111E0R0T(φ) − (Ao2)2 A−111RT0(φ) + I2. (8.45)

For output control of subsystem (8.35), we can simply take the following controller

uφ = −a0∼1φ(0∼1), (8.46)

where ai, i = 0, 1, are two positive scalars. The closed-loop system is given by

φ¨ = −a0∼1φ(0∼1) + A21ζ. (8.47)

Combining the above two aspects, yields the following result.

## [61] `odfas_2026_part4` (PDF p.59, L3354)

Proposition 8.3. Let Assumption Aφ be satisfied, F0∼1 ∈ ℝ2×4 be a matrix making Φ(F0∼1)

Hurwitz, and ai, i = 0, 1, be two positive scalars. Then a GUA stabilizing output feedback controller

for system (8.32) is given by
{u1 = uζ − A12φ − fy1 y†, φ, t
( † ) (8.48)
u2 = uφ − A22φ − fy2(y , φ, t),

where uζ is given by (8.43)-(8.45), and uφ is given by (8.46).

## [62] `scis_2022_discdelay1` (PDF p.5, L295)

Proposition 1. The linear time-delay system (1) is controllable if and only if it can be converted
equivalently into a system in the form of

x1 (k + 1) L1 xp⌈0∼μp−1⌉(k) |p=1∼η
( )
x2 (k + 1) L2 xp⌈0∼μp−1⌉(k) |p=1∼η
= ( ) + Bu (k − h) , (4)
... ...
xη (k + 1) Lη xp⌈0∼μp−1⌉(k) |p=1∼η
( )

where η ⩾ 1 is an integer, μp, p = 1, 2, . . . , η are a set of integers, xp ∈ ℝrp, p = 1, 2, . . ., η are a set of
state vectors, with rp, p = 1, 2, . . ., η, being a set of distinct integers satisfying

r1 + r2 + · · · + rη = r. (5)

Further, Lp (·) , p = 1, 2, . . . , η, are a set of linear functions, and B ∈ ℝr×r is a square upper-triangular
matrix with diagonal elements all being 1.
Generally, a system in the form of (4) is called a linear time-delay FAS if B ∈ ℝr×r is nonsingular,
that is,
rankB = r. (6)

As we will see in Section 5, such a full-actuation condition provides great convenience in the control of
the system.
Since the system (4) has a set of interconnected sub-states, it is often called a time-delay FAS with
interconnections for short.
With our notations, the above FAS (4) can be also compactly written in the form of

x1∼η (k + 1) = L xp⌈0∼μp−1⌉(k) |p=1∼η + Bu (k − h) , (7)
( )

where
L1 (·)
L2 (·)
L (·) = .
...
Lη (·)

A typical special form of the above linear discrete-time interconnected FAS (4) with delays is the following
linear time-delay FAS:
x (k + 1) = L x⌈0∼n−1⌉(k) + Bu (k − h) , (8)
( )
where L (·) is a linear function, and the matrix B ∈ ℝr×r is nonsingular.
As we will show later, or as demonstrated with the non-delay FAS approaches ([17,18,20,29]), a great
advantage of a FAS lies in the control of the system.
Based on the above description, we can now further propose more general linear FASs with time delays.

## [63] `scis_2022_discdelay1` (PDF p.8, L504)

Proposition 2. The above system (25), with Assumption 1 satisfied, can be equivalently converted
into the following form:

x (k + 1) = f x⌈0∼n−1⌉(k) + B x⌈0∼n−1⌉(k) u (k − h) , (26)
( ) ( )

where f (·) ∈ ℝr and B (·) ∈ ℝr×r are nonlinear functions, and particularly, B (·) satisfies the following
condition:
det B x⌈0∼n−1⌉(k) ≠ 0, ∀x⌈0∼n−1⌉(k) ∈ ℝnr and k ⩾ h. (27)
( )
The above condition (27) is called a full-actuation condition, while the system (26) is called a discrete-
time FAS with delays.
The full-actuation condition (27) makes the above time-delay FAS (26) totally different from a state-
space time-delay system. Without loss of generality, let us choose to consider the following nonlinear
(affine) discrete-time delay system in a state-space representation:

x (k + 1) = f (x (k) , x (k − τ) , k) + B (x (k) , x (k − τ) , k) u (k − h) , (28)

where f(·) ∈ ℝn and B(·) ∈ ℝn×r are nonlinear functions. Although in appearance the state-space
system (28) looks like a specific form of the FAS (26), it differs from the FAS (26) in the system dimensions.
For the FAS (26), we have r = n, and the full-actuation condition (27) holds, while for the state-space
system (28), we have r < n, not to mention the nonsingularity of the matrix B (x (k) , x (k − τ) , k) . It
is this difference that really makes the control of a nonlinear discrete-time delay system in a state-space
approach still a very difficult problem today. Nevertheless, the above Proposition 2 has shown a very
important fact that a discrete-time delay system in a state-space representation may be converted into a
discrete-time FAS with time delays. As we will see in Section 5, this brings about great convenience in
the control of time-delay dynamical systems.

## [64] `scis_2023_delay1` (PDF p.4, L282)

Proposition 1. Let Assumptions A and B hold, then the state-space system (1) is equivalent to the
following second-order system:

x¨1 (t) = f (t) + B(xk (t − σj (t))|j=1∼γ,k=1,2 , t)u (t) , (4)

where

B(xk (t − σj (t))|j=1∼γ,k=1,2 , t)

= B1(x1 (t − σj (t))|j=1∼γ, t)B2(xk (t − σj (t))|j=1∼γ,k=1,2 , t), (5)

and

f (t) ≜ ˙α(x1 (t − τj (t))|j=1∼ζ , t)+ B˙1(x1 (t − σj (t))|j=1∼γ, t)x2 (t)

+B1(x1 (t − σj (t))|j=1∼γ, t)β(xk (t − τj (t))|j=1∼ζ,k=1,2 , t), (6)

with the x2 related terms determined by the following relation:

x2 (t) = B−1(x1 (t − σj (t))|j=1∼γ, t) [x˙1 (t) − α(x1 (t − τj (t))|j=1∼ζ , t)]. (7)

Duan G R Sci China Inf Sci January 2023 Vol. 66 112201:5

## [65] `scis_2023_delay2` (PDF p.3, L196)

Proposition 1. The linear time-delay system (1) is controllable if and only if it can be converted
equivalently into a system in the form of

x(1µ1)(t) L1 x(0p∼µp−1)(t) |p=1∼η
( )
x(2µ2)(t) L2 x(0p∼µp−1)(t) |p=1∼η
= ( ) + Bu (t − h) , (2)
... ...
x(ηµη)(t) Lη xp(0∼µp−1)(t) |p=1∼η
( )
where η ⩾ 1 is an integer, µp, p = 1, 2, . . . , η are a set of integers, xp ∈ ℝrp, p = 1, 2, . . ., η are a set of
state vectors with rp, p = 1, 2, . . ., η being a set of distinct integers satisfying

r1 + r2 + · · · + rη = r. (3)

Further, Lp (·) , p = 1, 2, . . ., η are a set of linear functions, and B ∈ ℝr×r is a square upper-triangular
matrix with diagonal elements all being 1.
Generally, a system in the form of (2) is called a linear time-delay FAS if B ∈ ℝr×r is nonsingular,
that is, det B ≠ 0. Since the system (2) has a set of sub-states with different differential orders, it is often
called a time-delay FAS with multi-orders.
With our notations, the above FAS (2) can also be compactly written in the form of

x(µp)(t) |p=1∼η = L xp(0∼µp−1)(t) |p=1∼η + Bu (t − h) , (4)
( )
where
L1 (·)
L2 (·)
L (·) = .
...
Lη (·)

Duan G R Sci China Inf Sci February 2023 Vol. 66 122201:4

A typical special form of the above linear continuous-time multi-order FAS (2) with delays is the following
linear time-delay single-order FAS:

x(n)(t) = L x(0∼n−1)(t) + Bu (t − h) , (5)
( )
where L (·) is a linear function, and the matrix B ∈ ℝr×r is nonsingular.

## [66] `scis_2023_delay2` (PDF p.4, L275)

Proposition 2. Let Conditions C1 and C2 be met, then the state-space system (6) is equivalent to the
following second-order system:

x¨1 (t) = f (t) + B(xk (t − σj (t))|j=1∼γ,k=1,2 , t)u (t − δ (t) − h) , (9)

where

B(xk (t − σj (t))|j=1∼γ,k=1,2 , t) = B1(x1 (t − σj (t))|j=1∼γ, t)

×B2 xk (t − δ (t) − σj (t − δ (t)))|j=1∼γ,k=1,2 , t − δ (t) , (10)
( )
and

f (t) ≜ ˙α(x1 (t − τj (t))|j=1∼ζ , t)+ B˙1(x1 (t − σj (t))|j=1∼γ, t)x2 (t − δ (t))

+B1(x1 (t − σj (t))|j=1∼γ, t)β(xk (t − δ (t) − τj (t − δ (t)))|j=1∼ζ,k=1,2 , t − δ (t)), (11)

with the x2 related terms determined by the following relation:

x2 (t − δ (t)) = B−1 x1 (t − σj (t))|j=1∼γ, t x˙1 (t) − α x1 (t − τj (t))|j=1∼ζ , t . (12)
( ) [ ( )]

Duan G R Sci China Inf Sci February 2023 Vol. 66 122201:5

## [67] `scis_2024_chained1` (PDF p.4, L297)

Proposition 1. The nonlinear system (6)–(8) does not have a smooth exponentially stabilizing con-
troller. Furthermore, for the special case that both ˆϕi (·) and ψˆi (·) are time-invariant, system (6)–(8)
does not have a time-invariant continuous stabilizing controller if, for i = 1, 2, . . . , n − 1, one of the
following conditions holds:
(1) In the case of ρi = x0,
ϕˆi (·) |u0=0 = ψˆi (·) |u0=0 = 0;

(2) In the case of ρi = u0,
ϕˆi (·) |u0=0 = 0.

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:5

## [68] `scis_2024_chained2` (PDF p.4, L260)

Proposition 1. The nonlinear system (1)–(3) does not have a smooth time-invariant exponentially
stabilizing controller. Furthermore, for the special case that both ˆϕi (·) and ψˆi (·) are time-invariant,
system (1)–(3) does not have a continuous time-invariant stabilizing controller if, for some 1 ⩽ i ⩽ n − 1,
one of the following conditions holds:
(1) In the case of ρi = x0,
ϕˆi (·) |u0=0 = ψˆi (·) |u0=0 = 0;

(2) In the case of ρi = u0,
ϕˆi (·) |u0=0 = 0.

The above fact states that, under certain circumstances, to realize stabilization of system (1)–(3) with
a continuous controller, the controller must be a time-varying one. In [1], a discontinuous time-invariant
stabilizing controller for system (1)–(3) is designed. While in this paper, a continuous time-varying
stabilizing controller is sought.

## [69] `scis_2024_chained2` (PDF p.5, L336)

Proposition 2. Let a0 and a1 be determined by

α + β = a1, αβ = a0, (15)

where α > β > 0. Further, let ζ0 = x0 (0) and η0 = ˙x0 (0) denote the initial values. Then the response of
system (13) is given by

x0 (t) = −c1e−αt + c2e−βt, (16)
x˙0 (t) = αc1e−αt − βc2e−βt, (17)

where
1 1
c1 = (η0 + βζ0) , c2 = (η0 + αζ0) . (18)
α − β α − β
Impose the following assumption on the initial values of the first closed-loop subsystem (13).

## [70] `scis_2024_chained2` (PDF p.6, L363)

Proposition 3. Let Assumption B be met, and α > β > 0 be scalars satisfying (15). Further, let

σ0 (t) = c2e−βt ≠ 0, ∀t ⩾ 0,
{ω (t) = c1e−(α−β)t. (19)
c2

Then there hold

x0 (t) = σ0 (t) [1 − ω (t)] , (20)
u0 (t) = ˙x0 (t) = σ0 (t) [−β + αω (t)] , (21)

and
ρi (γi, ϑi, t) ≜ ρi (x0,x ˙0) = σ0 (t) [γi − ϑiω (t)] , (22)
where
(1, 1) , if ρi = x0,
(γi, ϑi) = { (23)
(−β, −α) , if ρi = u0.

Owing to (16) and (17), we can now write

ϕ′i(·) ≜ ϕ′i(ζ0, η0, xi+1∼n, t) = ˆϕi (x0, xi+1∼n, u0, t) , (24)
ψi′(·) ≜ ψi′(ζ0, η0, xi+1∼n, t) = ˆψi (x0, xi+1∼n, u0, t) , i = 1, 2, . . ., n − 1,

and Assumption A correspondingly becomes the following.

## [71] `scis_2025_chained3` (PDF p.4, L291)

Proposition 1. Let Assumptions A1 and A2 be met. Then the following conclusions hold:
(1) the linearized model of the nonlinear system (9)–(11) at the origin is uncontrollable, and is (uni-
formly) asymptotically unstabilizable if there exists an i, satisfying 1 ⩽ i < n, such that the time-varying
linear system
x˙ = ΦTi(0, 0, 0, t) x

is not (uniformly) asymptotically stable;
(2) the nonlinear system (9)–(11) does not have a smooth exponentially stabilizing controller; and

Duan G-R Sci China Inf Sci June 2025, Vol. 68, Iss. 6, 162201:5

(3) for the special case that both Φi (·) and Ψi (·) are time-invariant, system (9)–(11) does not have a
time-invariant continuous stabilizing controller if, for some integer i, 1 ⩽ i ⩽ n − 1, there holds

Φi (·) |u0=0 = Ψi (·) |u0=0 = 0, (12)

or
Φi (·) |u0=0 = 0, and ci = 0. (13)

## [72] `scis_2025_chained3` (PDF p.9, L563)

Proposition 2. Let a0, a1, α, and β be scalars satisfying Assumption A3. Further, let ζ0 = x0 (0) and
η0 = ˙x0 (0) denote the initial values. Then the response of system (35) is given by

x0 (t) = −φ˜0e−tα + φ0e−tβ, (36)
x˙0 (t) = αφ˜0e−tα − βφ0e−tβ, (37)

where
1 1
φ0 = (η0 + αζ0) , ˜φ0 = (η0 + βζ0) . (38)
α − β α − β
Define

Pi = {η | η ∈ ℝr, ΓTi(η + αζ0) = 0}, i = 1, 2, . . ., n − 1,
n−1
P = Pi = {η | η ∈ ℝr, ΓTi(η + αζ0) = 0, for some 1 ⩽ i ⩽ n − 1}.
i=1
Then each Pi is a hyperplane in ℝr, and P is a set of hyperplanes in ℝr. Introduce the following
assumptions.

## [73] `scis_2025_chained3` (PDF p.9, L600)

Proposition 3. Let Assumptions A2–A5 be met. Then

ρi (x0,x ˙0) = ˜ωie−tα + ωie−tβ, i = 1, 2, . . . , n − 1, (39)

where
ω˜i = (−ci + αdi) ΓTiφ˜0, ωi = (ci − βdi) ΓTiφ0 ≠ 0. (40)
Substituting the expressions in (36) and (37), and (39) and (40), turns subsystem (31) into the following
form:
x˙1 = u,
x˙2 = Φ˜1 (·) x2 + ω˜1e−tα + ω1e−tβ Ψ ˜1 (·) x1,
x˙3 = Φ˜2 (·) x3 +(ω˜2e−tα + ω2e−tβ)Ψ ˜2 (·) x2, (41)
{ ( )
...
x˙n = Φ˜n−1 (·) xn + ω˜n−1e−tα + ωn−1e−tβ Ψ ˜n−1 (·) xn−1,
( )

Duan G-R Sci China Inf Sci June 2025, Vol. 68, Iss. 6, 162201:10

where

˜Φi (·) ≜ ˜Φi (α, β, ζ0, η0, xi+1∼n, t) = Φi (x0, xi+1∼n, u0, t) , (42)
˜Ψi (·) ≜ ˜Ψi (α, β, ζ0, η0, xi+1∼n, t) = Ψi (x0, xi+1∼n, u0, t) , i = 1, 2, . . ., n − 1. (43)

Due to Proposition 3, Assumptions A2–A5 can be substituted by the following assumption on system
(41)–(43).

## [74] `scis_2025_chained3` (PDF p.17, L1045)

Proposition 4. Let Assumptions C1 and C2 be satisfied. Then, with the restriction of z1∼n ∈ 𝔽z(α, β,
ζ0, η0), the transformation (81) is one-to-one, and keeps the origin unchanged. Furthermore, the inverse
transformation of (81) is given by

z1∼n = Bˇe−1(α, β, ζ0, η0, z(0∼n−1), t) z(0∼n−1) −fˇe(α, β, ζ0, η0, z(0∼n−1), t) ,
( )
where

Bˇe(α, β, ζ0, η0, z(0∼n−1), t)

= diag Ir,Bˇ1 (α, β, ζ0, η0, z, t) ,Bˇ2(α, β, ζ0, η0, z(0∼1), t), . . . ,Bˇn−1(α, β, ζ0, η0, z(0∼n−2), t) ,
( )
and
0
fˇ1 (α, β, ζ0, η0, z, t)
fˇe(α, β, ζ0, η0, z(0∼n−1), t) = fˇ2(α, β, ζ0, η0, z(0∼1), t) .

...
fˇn−1(α, β, ζ0, η0, z(0∼n−2), t)

Finally, regarding the FAS model of SFS (60), we have the following result.

## [75] `tcyb_2023_robustdelay` (PDF p.6, L738)

Proposition 1: Let Assumptions A1–A4 be met. Then,
there exists a controller in the form of (21) that GUA stabilizes
the uncertain type I system (17) if there exists a controller in
the form of (21) that robustly input-to-state stabilizes, with
respect to the external input zk(0∼γk−1)|k=1∼ξ, the uncertain
multiorder FAS in (17).

The above proposition clearly implies the following corol-
lary corresponding to the uncertain single-order FAS (22).

## [76] `tcyb_2023_robustdelay` (PDF p.10, L1206)

Proposition 2: For an arbitrarily chosen F ∈ ℝnr×nr, all
the matrix A0∼n−1 and the nonsingular matrix V ∈ ℝnr×nr
satisfying

Φ(A0∼n−1) = VFV−1

are given by

A0∼n−1 = −ZFnV−1(Z, F)
Z
⎡ ZF ⎤
V = V(Z, F) =
⎢⎢⎢⎣ ... ⎥⎥⎥⎦
ZFn−1

where Z ∈ ℝr×nr is an arbitrary parameter matrix satisfying

det V(Z, F) ≠ 0.

It is seen from the above result that in order to meet the
condition (36), it suffices only to select a matrix F satisfying
μ
Reλi(F) ≤ − , i = 1, 2, . . . , nr. (67)
2
Clearly, there are quite some degrees of freedom in the selec-
tion of F, while on the other hand, we also have the parameter
matrix Z, which provides r2n degrees of freedom. All these
degrees of freedom can be further utilized to achieve the
additional performance of the system (see [47], [48]).

## [77] `tcyb_2023_subfas` (PDF p.3, L332)

Proposition 1: Let (x0(0), x1(0)) ≠ (0, 0), and a0 and a1
be two positive scalars. Then, the above controller (7) for
system (1) guarantees the following:
1) both x0(t) and x1(t) converge to zero exponentially;
2) the control signal u(t) also converges to zero
exponentially.

## [78] `tcyb_2023_subfas` (PDF p.5, L643)

Proposition 2: A nonlinear time-varying system is locally
feedback linearizable if and only if it can be equivalently
converted into a 0-type rational sub-FAS.

## [79] `tcyb_2023_subfas` (PDF p.11, L1367)

Proposition 3: Let b and ci, i = 0, 1, be positive scalars,
while ai, i = 0, 1, 2, are chosen as

a0∼2 = s31 s32 s33 V−1 (69)
[ ]
with
1 1 1
⎡ ⎤
V = −s1 − s2 − s3 (70)
⎣ s21 s22 s23⎦

where si, i = 1, 2, 3, are three distinct positive scalars. Then,
the controller (63) substabilizes system (60), and
1) the ROEA of the linear closed-loop subsystem (65) with
respect to the singularity condition (68) is determined by

1 ⎡ s2s3(s2 − s3) s22 − s23 s2 − s3⎤
x1(0∼2)(0) = −s1s3(s1 − s3) s23 − s21 s3 − s1 X0
Δ⎣ s1s2(s1 − s2) s21 − s22 s1 − s2⎦
(71)

where

Δ = (s1 − s2)(s1 − s3)(s2 − s3)

and X0 = [ x0 y0 z0 ]T satisfies

e−s1(t−σ)x0 + e−s2(t−σ)y0 + e−s3(t−σ)z0
≠ e−γ (t−σ) + 1, t ≥ 0; (72)

2) the control vector also converges to zero when initial val-
ues of the system are chosen within the ROEA described
above.

## [80] `tcyb_2024_overview` (PDF p.13, L1594)

Proposition 1: Let the variables Bk (x1∼k, t) and
hk (x1∼k, t), k = 1, 2, . . . , n, be given by (79)-(81).
Then, when x1∼n ∈ 𝔽ˆ, the transformation (82) is a one-to-
one mapping (a homeomorphism in 𝔽ˆ) and keeps the origin
unchanged.
Because of the above result, all x1∼k, k = 1, 2, . . . , n, can
be represented by x(0∼k−1), k = 1, 2, . . . , n. Therefore, we
have (a procedure is given in [42])

h˘k x(0∼k−1), t ≜ hk (x1∼k, t) ,
B˘k(x(0∼k−1), t) ≜ Bk (x1∼k, t) , k = 1, 2, . . . , n. (83)
( )
Based on the above, the following result is obtained in [42].

## [81] `book_2026_volume1` (PDF p.66, L45)

Proposition 1.1 For an arbitrarily chosen F ∈ Rmn×mn , all the matrix A0∼m−1 and
the nonsingular matrix V ∈ Rmn×mn satisfying
A0∼m−1 ) = V F V −1
are given by
A0∼m−1 = −Z F n V −1 (Z , F) ,
⎡                 ⎤
Z
⎢ ZF              ⎥
V = V (Z , F) = ⎢                   ⎥,
⎣ ...             ⎦
Z F n−1
46                                                                                1 Introduction
where Z ∈ Rm×mn is an arbitrary parameter matrix satisfying
detV (Z , F) = 0.

## [82] `book_2026_volume1` (PDF p.67, L46)

Proposition 1.1 are provided. These results present, in a sense, a database for users of
the FAS approach to derive a specific parameter A0∼m−1 for the designed controller
and the closed-loop systems.
Open Access This chapter is licensed under the terms of the Creative Commons Attribution 4.0
International License (http://creativecommons org/licenses/by/4.0/), which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons license and
indicate if changes were made.
The images or other third party material in this chapter are included in the chapter’s Creative
Commons license, unless indicated otherwise in a credit line to the material. If material is not
included in the chapter’s Creative Commons license and your intended use is not permitted by
statutory regulation or exceeds the permitted use, you will need to obtain permission directly from
the copyright holder.
Part I
Basic Theories
In addition to the well-known state-space models, another general type, termed FAS
models, is newly discovered, which has been proven to be more advantageous for
controller design in dynamical systems.

## [83] `book_2026_volume1` (PDF p.83, L63)

Proposition 2.1 System (2.66) is controllable if and only if the following controlla-
bility matrix
Q c = b Ab · · · A
n−1
b
is invertible. Further, define
⎡            ⎤
α1 · · · αn−1 1
⎢ ..      .  . ⎥
⎢     .. ..      ⎥
P = Qc ⎢ .       .      ⎥,                       (2.68)
⎣αn−1 . .        ⎦
then under the coordinate transformation x̄ = P −1 x, system (2.66) can be converted
into the Luenberger controllability canonical form
x̄˙ = Ac x̄ + bc u,                         (2.69)
where                           ⎡                 ⎤        ⎡ ⎤
0   1                         0
⎢ ..      . ..        ⎥        ⎢ .⎥
⎢                     ⎥        ⎢.⎥
Ac = ⎢ .                   ⎥ , bc = ⎢ . ⎥ (2.70)
⎣ 0               1 ⎦          ⎣0⎦
−α0 −α1 · · · −αn−1            1
Based on the above proposition, we can further obtain the following result which
reveals the relation between controllability of system (2.66) and its FAS presentation.

## [84] `book_2026_volume1` (PDF p.85, L65)

Proposition 2.2 System (2.74) is controllable if and only if there exists an invert-
ible state transformation x̂ = P x, which converts system (2.74) into the following
Luenberger controllability canonical form:
x̂˙ = Âc x̂ + B̂c u,                  (2.75)
where                                                   ⎡ ⎤
⎡               ⎤        B̂1
Â11 · · · Â1r        ⎢ B̂2 ⎥
⎢ . . . .. ⎥            ⎢ ⎥
Â c = ⎣ .       . . ⎦ , B̂c = ⎢  . ⎥,                 (2.76)
⎣ .. ⎦
Âr1 · · · Ârr
B̂r
with
⎡                               ⎤
0     1
⎢ ..           ..              ⎥
⎢ .                .           ⎥
Âii = ⎢                              ⎥ ∈ Rμi ×μi ,
⎣ 0                    1 ⎦
−αii0 −αii1 · · · −αiiμi −1
⎡                     ⎤
0 ···       0
⎢ ..              ..  ⎥
⎢                     ⎥
Âi j = ⎢ .                .  ⎥ ∈ Rμi ×μ j , i       j,
⎣ 0 ···          0 ⎦
μ −1
−αi0j · · · −αi j j
⎡                              ⎤
0 ··· 0 0 0 ··· 0
⎢ ..    .. .. ..            .. ⎥
⎢                            . ⎥
B̂i = ⎢ .      . . .                 ⎥ ∈ Rμi ×r .
⎣0 ··· 0 0 0 ··· 0 ⎦
0     0 1 bi,i+1 · · · bi,r
In fact, a procedure for finding such a transformation matrix P can be given as
follows.
Algorithm 2.1 Let μi , i = 1, 2, . . . , r , be the controllability indices of system

## [85] `book_2026_volume1` (PDF p.147, L128)

Proposition 4.1 The above SFS (4.2), with G i , i = 1, 2, . . . , n, being nonsingular,
can be transformed into the form of
z (n) = f z (0∼n−1) , ζ, t +         f z (0∼n−1) , ζ, t + L n u,         (4.3)
with z = x1 , and
L k = G 1 G 2 · · · G k , k = 1, 2, . . . , n,               (4.4)
4.1 FAS Models with Disturbances                                                         129
⎡                          ⎤
f 1(n−1) (z, ζ, t)
⎢ f (n−2) (z, x2 , ζ, t) ⎥
⎢ 2                         ⎥
(0∼n−1)                   ⎢              ..           ⎥
f (z         , ζ, t) = L 0∼n−1 ⎢                           ⎥,      (4.5)
⎢               .           ⎥
⎣ f˙ (x                     ⎦
n−1 1∼n−1 , ζ, t)
f n (x1∼n , ζ, t)
⎡                              ⎤
f 1(n−1) (z, ζ, t)
⎢ f (n−2) (z, x2 , ζ, t) ⎥
⎢      2                       ⎥
(0∼n−1)                   ⎢                 ..           ⎥
f (z         , ζ, t) = L 0∼n−1 ⎢                  .           ⎥,   (4.6)
⎢                              ⎥
⎣ f˙ (x                , ζ, t) ⎦
n−1    1∼n−1
f n (x1∼n , ζ, t)
where L 0 = I, and in (4.5)–(4.6) the xk , k = 2, 3, . . . , n, and their derivatives
are all given or determined by certain transformation [see Theorem 3.1 in Duan
(2021b)].
Similarly, it can be shown via Theorems 3.2, 3.4 and 3.6 in Duan (2021b) that the
second- and high-order SFSs proposed in Duan (2021b), with uncertainties properly
added, can be also converted into the form of FAS (4.1).
4.1.2 FAS Models with Deterministic Disturbances
Now let us consider the case where f x (0∼n−1) , ζ, t is a deterministic external
disturbance. In such a case we may assume

## [86] `book_2026_volume1` (PDF p.154, L135)

Proposition 1.1 can be readily used, which can be briefly restated as below.

## [87] `book_2026_volume1` (PDF p.187, L168)

Proposition 5.1 The uncertain term in system (5.22) satisfies
f z (0∼3)    ≤ ρ z (0∼3) ,
with
..
ρ z (0∼3) = γ1 |ż| + γ2 ż 2 |z̈| + σ2 |z| | z − 2z ż| + γ1 |ż|2 .

## [88] `book_2026_volume1` (PDF p.241, L223)

Proposition 6.1 Let Condition 6.1 be satisfied, then the generalized SFS (6.94) can
be transformed into the following FAS model
z (n) = h(z (0∼n−1) , ζ, t) +           h(z (0∼n−1) , ζ, t) + L n (z (0∼n−1) , ζ, t)u,   (6.95)
with
L n (z (0∼n−1) , ζ, t) = G 1 G 2 · · · G n−1 G n (x1∼n , ζ, t),        (6.96)
and
⎡                   ⎤
f 1(n−1) (z, ζ, t)
⎢ f (n−2) (z, x2 , ζ, t) ⎥
⎢ 2                        ⎥
(0∼n−1)                   ⎢             ..           ⎥
h(z         , ζ, t) = L 0∼n−1 ⎢              .           ⎥,               (6.97)
⎢                          ⎥
⎣ f˙ (x            , ζ, t) ⎦
n−1   1∼n−1
f n (x1∼n , ζ, t)
⎡                            ⎤
f 1(n−1) (z, ζ, t)
⎢    f 2(n−2) (z, x2 , ζ, t) ⎥
⎢                            ⎥
(0∼n−1)                     ⎢               ..           ⎥
h(z             , ζ, t) = L 0∼n−1 ⎢                .           ⎥,      (6.98)
⎢                            ⎥
⎣    f˙n−1 (x1∼n−1 , ζ, t) ⎦
f n (x1∼n , ζ, t)
where L 0 = I, and L k , k = 1, 2, . . . , n − 1, are given by (6.88 ).
The above proposition provides a basic result for further investigating robust
control of uncertain SFS based on the FAS approach.
6.6.3 An Anti-Disturbance Feature
For convenience, let us consider the following first-order SFS with polynomial
disturbances:
⎧
⎪
⎪ ẋ1 = f 1 (x1 , ζ, t) + G 1 x2 + p {n−2} (t)
⎪
⎪                                       {n−3}
⎨ ẋ2 = f 2 (x1∼2 , ζ, t) + G 2 x 3 + p

## [89] `book_2026_volume1` (PDF p.242, L224)

Proposition 6.2 Let Condition 6.1 be satisfied, then the generalized SFS (6.99) can
be transformed into the following FAS model
z (n) = h n (z (0∼n−1) , ζ, t) + L n (z (0∼n−1) , ζ, t)u,      (6.103)
with
L n (z (0∼n−1) , ζ, t) = G 1 G 2 · · · G n−1 G n (x1∼n , ζ, t),      (6.104)
6.7 Notes and References                                                              225
and                                                ⎡                          ⎤
f 1(n−1) (z, ζ, t)
⎢ f (n−2) (z, x2 , ζ, t) ⎥
⎢ 2                        ⎥
(0∼n−1)                   ⎢             ..           ⎥
h n (z         , ζ, t) = L 0∼n−1 ⎢                          ⎥,   (6.105)
⎢              .           ⎥
⎣ f˙ (x            , ζ, t) ⎦
n−1    1∼n−1
f n (x1∼n , ζ, t)
where L 0 = I, and L k , k = 1, 2, . . . , n − 1, are given by (6.88).
The above result implies a very important fact, i e., although the state-space model
(6.99) is subject to polynomial disturbances, the derived FAS is free of disturbances.
This becomes vitally important when we are only interested in z = x1 In engineering,
a constant disturbance is often encountered, which corresponds to the “drift” of
certain values and is sometimes referred to as a step disturbance. The first-order
disturbance d (t) = d1 t + d0 is also commonly encountered and is referred to as
a slope disturbance or a ramp disturbance. By Taylor series expansion theory, any
function can be approximated by a polynomial, thus a general disturbance can also be
approximated by a polynomial p {k} (t). Due to these facts, the above anti-disturbance
feature of the FAS approach is truly crucial.
6.7 Notes and References
The FAS approach is very powerful in dealing with the control of nonlinear systems,
since the full-actuation feature allows one to eliminate the nonlinearities and hence
an LTI closed-loop system can be obtained. To apply the FAS approach, the key step
is to obtain a FAS model for a nonlinear system. Toward this goal, this chapter has
shown the following:
1. the conventional SFS can be further generalized to contain parameter vectors
and the derivatives of the state vectors, and a recursive solution exists to convert
the generalized version of SFS equivalently into a FAS model;

## [90] `book_2026_volume1` (PDF p.400, L386)

Proposition 12.1 Let Assumptions 12.3–12.8 be met. Then, there exists a controller
in the form of (12.20) that GUA stabilizes the uncertain Type I system (12.16) if
there exists a controller in the form of (12.20) that robustly input-to-state stabilizes,
(0∼γ −1)
with respect to the external input z k k |k=1∼ξ , the uncertain multi-order FAS in
(12.16).
The above proposition clearly implies the following corollary corresponding to
the uncertain single-order FAS (12.21).

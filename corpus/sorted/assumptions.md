# Sorted Assumption Corpus Across 32 Duan First-Author Papers + Volume I (165 items)

## [1] `aaas_2024_subsfs` (PDF p.3, L267)

假设 1 fi( x1~i，t)| x1~n = 0 = 0 ( i = 1，2，…，n )

许多关于系统式（1）的研究 ，均假设了
G i( x1~i，t) ∈ ℝr × r ( i = 1，2，…，n ) 可逆的条件 ，在

本文中去掉了该条件，为此引入如下定义。

## [2] `aas_2020_part1` (PDF p.5, L468)

假设 A1. 参数向量 θ = θ (t) ∈ Rl 含于某紧集
Ω 中, 即 θ (t) ∈ Ω ⊂ Rl.
M (θ, x, x ˙), D (θ, x, x ˙), K (θ, x, x ˙) ∈ Rn×n
和 B (θ, x, x ˙) ∈ Rn×n 是系统的系数矩阵, 它们关
于 x, x ˙ 和 θ 是分段连续的, 且 M(·) 恒不为零, B(·)
满足如下全驱性假设:

## [3] `aas_2020_part1` (PDF p.5, L474)

假设 A2. det B (θ, x, x ˙) ≠ 0, ∀x, x ˙ 和 θ (t)
∈ Ω.
在机电系统中, 控制向量 τ (t) 一般是广义力向
量或者广义力矩向量, 由如下一阶模型

τ˙ = f (τ, t) + u (20)

或者如下二阶模型

τ¨ = f (τ, ˙τ, t) + u (21)

决定, 其中 f (·) 是 n 维的向量函数, u (t) 是驱动控
制向量, 一般是电信号向量.
由二阶系统 (19) 和系统 (20) 或 (21) 组成的串
联系统的常规控制方法是将其化为一阶状态空间形
式, 然后采用一阶系统的有关方法实现控制设计. 此
时需要处理一个 3n 维的一阶系统, 而且也不一定
能够保证求得系统的镇定控制律. 不同于一阶系统
方法, 文献 [33] 应用高阶系统方法, 将系统 (19) 和
(20) 组成的串联系统等价转化为全驱的三阶微分系
统.

段广仁: 高阶系统方法 — I. 全驱系统与参数化设计

## [4] `aas_2020_part1` (PDF p.8, L816)

假设 A3. rankE = n0 ≤ n
则由广义系统理论[36] 可知, 闭环系统 (10) 或者 (44)
具有

nc = rankEc = (m − 1)n + n0 (48)

个有限相对特征值和 n − n0 个无穷相对特征值. 因
此, 闭环系统的若当标准型 F ∈ Rnc×nc 所对应的有
限特征向量矩阵 V ∈ Rmn×nc 由下式决定:

AcV = EcV F (49)

另外, 定义如下两个矩阵 T∞ 和 V∞ ∈
Rn×(n−n0):

T∞TE = 0, rankT∞ = n − n0 (50)

EV∞ = 0, rankV∞ = n − n0 (51)

则通过文献 [37] 中的定义, 可以很容易地证明, 对应
于 n − n0 个无穷相对特征值的左右无穷特征向量矩
阵分别由下面的公式给出

0 0

T∞c = ... , V∞c = ... (52)
0 0
T∞ V∞

而 V V∞c 作为闭环系统的整体特征向量矩阵
应满足下述条件:

det V V∞c ≠ 0 (53)

46 卷

## [5] `ijss_2021_part1` (PDF p.7, L644)

Assumption 3.1: For arbitrary ζ ∈ ℝp, x(0∼m−1) ∈
ℝmn, there holds

rankB(x(0∼m−1), ζ) = r < n. (12)

In the case of r = n, the system (11) is already an
HOFA system, and the controller can be immediately
written out.
In the case of m = 1, and ζ does not exist, the above
system (11) reduces to the following well-known affine
nonlinear system

x˙ = f (x) + B(x)u, (13)

In this section, we aim to provide a basic procedure of
the so-called HOFA systems approach for the control
of the above system (11). The procedure contains the
following steps.

## [6] `ijss_2021_part1` (PDF p.7, L683)

Assumption 3.2: There exists a constant nonsingular
matrix Q(x(0∼m−1), ζ) = Q satisfying (14).

The general case will be addressed elsewhere, while
the idea is illustrated in Example 2.
Under Assumption 3.2, we can define the following
transformation

z = [z1] = Qx, z1 ∈ ℝn−r. (16)
z2

Partitioning the matrix Q as

Q = [Q1], Q2 ∈ ℝr×n,
Q2

and using (11) and (14), we have

z(m) Q1f (x(0∼m−1), ζ)
[ 1(m)] = [ (0∼m−1) ]
z2 Q2f (x , ζ)

0
+ [G(x(0∼m−1), ζ)]u, (17)

which can be equivalently decomposed, in view of
the invertibility of the transformation (16), into two
subsystems of the following forms:

z(m) = g(z(0∼m−1), ζ), (18)
1
z2(m) = f2(z(0∼m−1), ζ) + G(z(0∼m−1), ζ)u. (19)

Further, assume that the above system (18) is in the
following form

z(m) = f1(z(0∼m−1), ζ) + B1(z(0∼m−1), ζ)z2, (20)
1 1 1

then the above system (20) is again in the form of (11)
when z2 ∈ ℝr is looked upon as the control input. If

n − r > r, by repeating the above process (if repeat-
able), the system (20) can also be divided into the
following two subsystems:

z(m) = g1(z(0∼m−1), ζ), (21)
11 1

z(m) = g2(z(0∼m−1), ζ) + G2(z(0∼m−1), ζ)z2. (22)
12 1 1

Continue the above process, under certain conditions,
we obtain a pseudo strict-feedback system in the fol-
lowing form:

z(m) = g(z(0∼m−1), ζ)
⎧ 0 0∼1
z(m) = f1(z(0∼m−1), ζ) + B1(z(0∼m−1), ζ)z2
1 0∼1 0∼1
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨z(m) = f2(z(0∼m−1), ζ) + B2(z(0∼m−1), ζ)z3
2 0∼2 0∼2
...
zq(m−)1 = fq−1(z0(0∼∼qm−−11), ζ) + Bq−1(z0(0∼∼qm−−11), ζ)zq
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩zq(m) = fq(z(0∼m−1), ζ) + Bq(z(0∼m−1), ζ)u,
0∼q 0∼q

## [7] `ijss_2021_part1` (PDF p.8, L761)

Assumption 3.3: For all ζ ∈ ℝp, and z(0∼m−1) ∈ ℝmr,
k
there hold

detBi(z0(0∼∼im−1), ζ) ≠ 0, k = 0, 1, . . . , q.

## [8] `ijss_2021_part1` (PDF p.8, L832)

Assumption 3.4: The first subsystem in (26) is in the
following form:

z0(m) = g(z0(0∼m−1), ζ) + B0z1, (29)

where B0 ∈ ℝn0×r is a full-row rank matrix.

This assumption restricts the subsystem to be lin-
ear with respect to z1, but is independent on the
derivatives of z1. The general nonlinear case will be
addressed elsewhere.

Taking the derivative of order mc on both sides
of (29), and using (24), yield

z(m+mc) = g(mc)(z(0∼m−1), ζ) + B0z(mc)
0 0 1
= g(mc)(z0(0∼m−1), ζ) + B0 [h(·) + L(·)u]
(30)

which gives the following higher-order system

z(m+mc) = ψ(z(0∼m+mc−1), z(0∼mc−1), ζ(0∼mc))
0 0 1
+ B0L(·)u, (31)

where

ψ(z(0∼m+mc−1), z(0∼mc−1), ζ(0∼mc))
0 1
= g(mc)(z(0∼m−1), ζ)
0
+ B0h(z(0∼m−1), z(0∼mc−1), ζ).
0 1

If we divide the control vector as

u = [u1], u1 ∈ ℝn0, (32)
u2

and partition L(z(0∼mc−1), z(0∼mc−1), ζ) as
0 1

L(z(0∼mc−1), z(0∼mc−1), ζ) = [L1 L2] , L1 ∈ ℝr×n0,
0 1
(33)
then the system (31) can be written as

z(m+mc) = ψ(z(0∼m+mc−1), z(0∼mc−1), ζ(0∼mc))
0 0 1
+ B0L1u1 + B0L2u2, (34)

Without loss of generality, let us assume

det B0L1(z(0∼mc−1), z(0∼mc−1), ζ) ≠ 0, (35)
( 0 1 )

for all z(0∼mc−1), z(0∼mc−1) and ζ, since otherwise we
0 1
can apply a transformation to the control u, which
equals to applying a series of elementary column trans-
formations to the matrix L. Under the condition (35),
system (34) is clearly a fully actuated system with
respect to u1, while u2 and z1 can be treated as external
vectors which will be given later. Thus we can design

## [9] `ijss_2021_part2` (PDF p.4, L382)

Assumption A1: For arbitrary xi ∈ ℝr, i = 1, 2, . . . ,
n, and ζ ∈ ℝm, there holds

det Gi(x1(0∼∼i−1)1, xi, ζ, t) ≠ 0, ∀ t ≥ 0. (4)

In certain high-dimensional cases, the above Assump-
tion A1 may be difficult to verify. It is recommanded
that symbolic computation techniques may be consid-
ered to help in such cases.
For this generalised form (3), some existing con-
trol methods, such as the backstepping methods, may
become extremely difficult or even impossible to apply
when r and n are large due to the ‘differential explosion’
problem. However, if we can transform it into a HOFA
system model, its control problems can then be solved
easily and conveniently (Duan, 2020a).

## [10] `ijss_2021_part2` (PDF p.5, L500)

Assumption A2: For arbitrary xi ∈ ℝr, i = 1, 2, . . . ,
n, and ζ ∈ ℝm, there holds

det Gi(x1(0∼∼i−2)1, xi(0∼1), ζ, t) ≠ 0, ∀ t ≥ 0.

Parallel to the first-order case, we have the following
conclusion.

## [11] `ijss_2021_part2` (PDF p.6, L612)

Assumption A3: For all xk ∈ ℝr, k = 1, 2, . . . , n, and
ζ ∈ ℝm, there holds

det Gk(xi(0∼mi)|i=1∼k−1, xk(0∼mk−1), ζ, t) ≠ 0,

∀ t ≥ 0.

For convenience, we further introduce the following
notations:

pi = m1 + m2 + · · · + mi, i = 1, 2, . . . , n
{ (19)
p = pn.

Then, parallel to the first-order and second-order
cases, we have the following conclusion.

## [12] `ijss_2021_part3` (PDF p.4, L331)

Assumption A1: det L(x(0∼n−1)) ≠ 0, ∀ x(i) ∈ ℝr, i =
0, 1, . . . , n − 1.
Correspondingly, for some nonlinear systems sub-
ject to uncertainties, often their HOFA models can be
also derived, but in the following form:

x(n) = f (x(0∼n−1)) + Δf (x(0∼n−1)) + L(x(0∼n−1))u,
(2)
where Δf (x(0∼n−1)) ∈ ℝr is the nonlinear uncer-
tainty of the system. The derivation of the above
uncertain HOFA model may be of two folds: one is
through physical modelling, see, e.g. the Example 2 in
Duan (2020d), when the disturbances di, i = 1, 2, 3,
are taken as uncertainties; the other is through model
conversion (see the example section in this paper).

## [13] `ijss_2021_part3` (PDF p.4, L376)

Assumption A2: Gi(x1(0∼∼i1)) ≠ 0, ∀ xi,x ˙i ∈ ℝr, i = 1,
2, . . . , n.
In the case that the nonlinear uncertainties in the
above second-order SFS do not appear, it has been
shown in Duan (2020d) that the model can be equiv-
alently converted into the form of (1). However, when
nonlinear uncertainties do exist, in some cases, an
equivalent single HOFA model in the form of (2) may
not be able to be derived, or in other words, the derived
HOFA model may be too conservative in the sense that
too much of certain information has to be included
into the uncertain terms Δfi(x1(0∼∼i1)), i = 1, 2, . . . , n,
since it is sometimes hard to separate the certain part
from the uncertain terms. Therefore, in certain appli-
cations, it may be more favourable to treat directly the
set of models in (3), or, only convert a few of the sub-
systems in (3) into several HOFA models in the form
of (2). After all, all the subsystems in (3), as they stand,
are a set of cascade fully actuated subsystems, when the
xi+1 in the i-th subsystem is looked upon as the control
variable.
It is worth pointing out that the above second-order
SFS (3) also has the following companion form:

⎧x¨1 = f1(x1,x ˙1) + Δf1(x1,x ˙1) + G1(x1,x ˙1)x˙2
x¨2 = f2(x1(0∼∼21)) + Δf2(x1(0∼∼21)) + G2(x1(0∼∼21))x˙3
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
...
x¨n−1 = fn−1(x1(0∼∼n1−)1) + Δfn−1(x1(0∼∼n1−)1)
+Gn−1(x1(0∼∼n1−)1)x˙n
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ (0∼1) (0∼1) (0∼1)
x¨n = fn(x1∼n ) + Δfn(x1∼n ) + Gn(x1∼n )u.
(4)

As a matter of fact, the last term Gi(x1(0∼∼i1))x˙i+1 in each
subsystem can be further generalised into

G0i(x1(0∼∼i1))xi+1 + G1i(x1(0∼∼i1))x˙i+1,

with [G0i(x1(0∼∼i1)) G1i(x1(0∼∼i1))] being of full rank.

## [14] `ijss_2021_part3` (PDF p.5, L451)

Assumption A3: det Gk(xi(0∼mi−1)|i=1∼k) ≠ 0, ∀ xi(j) ∈
ℝr, j = 0, 1, . . . , mi − 1, i = 1, 2, . . . , k, k = 1, 2, . . . , n.
Regarding the derivation of the above uncertain
mixed-order SFS (5), we make the following state-
ments:

• In the modelling of physical systems, we often use
physical laws such as Lagrangian Equations and

Theorem of Linear and Angular Momentum. In
such cases the original models of the obtained sub-
systems are of second-order. On the other side,
there are also subsystems modelled by other phys-
ical laws, such as the well-known Hamiltonian
Theorem, and the obtained original models are
of first-order. Such operations give a mixed-order
SFS (5), with mi, i = 1, 2, . . . , n, taking the values
of 1 or 2.
• It has been pointed out above that the mixed-
order SFS may be obtained from the second-order
SFS by converting equivalently some of the subsys-
tems in (3) into several HOFA models in the form
of (2). Meanwhile, some of the subsystems in (3) can
also be converted into several first-order equations.
Both operations gives mixed-order SFSs.

Parallely, the above mixed-order SFS (5) also has a
companion form which appears as follows:

x(m1) = f1(x(0∼m1−1)) + Δf1(x(0∼m1−1))
⎧ 1 1 1
+G1(x(0∼m1−1))x2
1 ˙
x2(m2)=f2(xi(0∼mi−1)|i=1∼2)+Δf2(xi(0∼mi−1)|i=1∼2)
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ +G2(xi(0∼mi−1)|i=1∼2)x˙3

...
xn(m−n1−1) = fn−1(xi(0∼mi−1)|i=1∼n−1)
+Δfn−1(xi(0∼mi−1)|i=1∼n−1)
+Gn−1(xi(0∼mi−1)|i=1∼n−1)x˙n
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩xn(mn)=fn(xi(0∼mi−1)|i=1∼n)+Δfn(xi(0∼mi−1)|i=1∼n)
+Gn(xi(0∼mi−1)|i=1∼n)u.
(6)

It is reminded that this form can be often converted
into the form of (5) by lowering the orders of the sub-
systems. A by-product of doing this is that the number
of equations in the system will be increased.

## [15] `ijss_2021_part4` (PDF p.4, L376)

Assumption A1: det L(x(0∼n−1)) ≠ 0, ∀ x(i) ∈ ℝr,
i = 0, 1, . . . , n − 1.
The above HOFA system (1) can be easily mis-
taken as a very special type of systems, while as
a matter of fact, it does represent a quite gen-
eral model for ‘completely controllable’ systems, and
can either be obtained through physical modelling,
or through conversion from other types of models
(Duan, 2020a, 2020b, 2020d, 2020e).

## [16] `ijss_2021_part4` (PDF p.5, L413)

Assumption A2: gi(x1(0∼∼i1)) ≠ 0, ∀ xi,x ˙i ∈ ℝ, i =
1, 2, . . . , n.

Besides physical modelling, many conventional
first-order SFSs can also be converted into the above
second-order form (2).
Clearly, a companion form of the above SFS (2) is
the following:

x¨1 = f1(x1,x ˙1)ϑ1 + g1(x1,x ˙1)x˙2
⎧
x¨2 = f2(x1(0∼∼21))ϑ2 + g2(x1(0∼∼21))x˙3
⎪⎪⎪⎪⎪⎪⎪⎪⎨
... (3)

x¨n−1 = fn−1(x1(0∼∼n1−)1)ϑn−1 + gn−1(x1(0∼∼n1−)1)x˙n

⎪⎪⎪⎪⎪⎪⎪⎪⎩x¨n = fn(x1(0∼∼n1))ϑn + gn(x1(0∼∼n1))u.

## [17] `ijss_2021_part4` (PDF p.5, L462)

Assumption A3: gk(xi(0∼mi−1)|i=1∼k) ≠ 0, ∀
x(0∼mi−1) ∈ ℝmi, k = 1, 2, . . . , n.
i

Parallel to (3), a companion form of the above
SFS (4) is the following:

x(m1) = f (x(0∼m1−1))ϑ1 + g1(x(0∼m1−1))x2
⎧ 1 1 1 1 ˙
x2(m2) = f2(xi(0∼mi−1)|i=1∼2)ϑ2

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ + g2(xi(0∼mi−1)|i=1∼2)x˙3

...

xn(m−n1−1) = fn−1(xi(0∼mi−1)|i=1∼n−1)ϑn−1

+ gn−1(xi(0∼mi−1)| i=1∼n−1)x˙n

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ xn(mn) = fn(xi(0∼mi−1)|i=1∼n)ϑn

+ gn(xi(0∼mi−1)|i=1∼n)u.
(5)
In Duan (2020f), the relations among three types of
high-order models with uncertainties are discussed,
while the above three types high-order models with
unknown parameters have similar relations.

## [18] `ijss_2021_part4` (PDF p.7, L664)

Assumption A1. Let Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1 be
a set of matrices such that Φ(A0∼n−1) is stable, and
PL(A0∼n−1) be given by (6)–(8). Then, the following
control law

θ˙ˆ = H(x(0∼n−1))PLT(A0∼n−1)

× x(0∼n−1) − (x∗)(0∼n−1)
( )

u = −L−1 x(0∼n−1) A0∼n−1x(0∼n−1) + u∗
( ) ( )
u∗ = HT(x(0∼n−1))θˆ + q(x(0∼n−1)) + u0(x∗)

u0(x∗) = (x∗)(n) − A0∼n−1(x∗)(0∼n−1),

when applied to system (1), guarantees the following:

(1) x(0∼n−1)−(x∗)(0∼n−1) → 0, t → ∞;
(2) ‖θ − θˆ‖ is bounded.

## [19] `ijss_2021_part5` (PDF p.4, L370)

Assumption A1: det L(x(0∼n−1)) ≠ 0, ∀x(i) ∈ ℝr, i =
0, 1, . . . , n − 1.
Furthermore, Δf (x(0∼n−1)) ∈ ℝr is an uncertain
nonlinearity of the system satisfying the following
assumption:

## [20] `ijss_2021_part5` (PDF p.4, L376)

Assumption A2: There exists a non-negative contin-
uous scalar function ρ(x(0∼n−1)), such that

Δf (x(0∼n−1)) ≤ ρ(x(0∼n−1)).
‖‖‖ ‖‖‖
While θ = θ(t) ∈ ℝm is an unknown time-varying
parameter vector with a pre-estimate θ0 = θ0(t) ∈ ℝm,
and satisfies

## [21] `ijss_2021_part5` (PDF p.4, L385)

Assumption A3: ‖θ − θ0‖ ≤ δ0, ‖ θ˙ − θ˙0‖ ≤ δ1, ∀t ≥
0, with δ0 and δ1 being two non-negative real numbers.

## [22] `ijss_2021_part5` (PDF p.9, L928)

Assumption A2’: There exists a non-negative contin-
uous scalar function ρ(x(0∼n−1)), such that

Δf (x(0∼n−1)) ≤ ρ(x(0∼n−1)) PTx(0∼n−1) .
L
‖‖‖ ‖‖‖ ‖‖‖ ‖‖‖

Under Assumptions A1 and the above thmA2’, we will
present a modified adaptation scheme for the case of
constant θ, which has the following two advantages:

(1) the adaptation scheme does not depend on a pre-
estimate of the parameter θ;
(2) the robust adaptive controller guarantees that the
state x(0∼n−1) converges to zero.

In the case that the parameter vector θ is constant, the
modification of our robust adaptive controller consists
of the following two aspects:

• replacing the robustness part in robust adaptive
controller (12)–(14) by

ur = 1ρ(x(0∼n−1))PT(A0∼n−1)x(0∼n−1), (48)
ε L

where ε is an arbitrarily selected positive real num-
ber not greater than 1, and
• replacing the adaptation part in robust adaptive
controller (12)–(14) by the following

θ ˙ˆ = H(x(0∼n−1))PT(A0∼n−1)x(0∼n−1),
{ L (49)
ua = HT(x(0∼n−1))θˆ.

As a result, we have the following theorem.

## [23] `ijss_2021_part6` (PDF p.5, L416)

Assumption A1 det B(x(0∼n−1), ζ, t) ≠ 0, ∀ζ ∈ ℝp,
x(i) ∈ ℝr, i = 0, 1, . . . , n − 1.
From appearance, the above Assumption A1 seems
to be strict. While as a matter of fact, the above
HOFA system (1) represents a quite general model
for ‘completely controllable’ systems, and can either
be obtained through physical modelling, or through
conversion from other types of models (Duan, 2021a,
2021b, 2020a, 2020b, 2020c, 2020d, 2021d).
As a demonstration, let us restate that the following
uncertain strict-feedback system can be converted into
the form of (1):

⎧x˙1 = f1(x1, ζ, t) + Δf1(x1, ζ, t) + G1x2
x˙2 = f2(x1, x2, ζ, t) + Δf2(x1, x2, ζ, t) + G2x3
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
...

x˙n−1 = fn−1(x1∼n−1, ζ, t) + Δfn−1(x1∼n−1, ζ, t)
+Gn−1xn
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩
x˙n = fn(x1∼n, ζ, t) + Δfn(x1∼n, ζ, t) + Gnu,
(2)
where xi ∈ ℝr, i = 1, 2, . . . , n are the state vec-
tors, u ∈ ℝr is the control input, fi(x1∼i, ζ, t) and
Δfi(x1∼i, ζ, t) ∈ ℝr, i = 1, 2, . . . , n are sufficiently
smooth vector functions, and Gi ∈ℝr×r, i = 1, 2, . . . , n
are a set of nonsingular matrices. According to the
Theorem 3.1 or 3.6 in Duan (2020b), we have the
following simplified result.

## [24] `ijss_2021_part6` (PDF p.11, L1120)

Assumption A2 The matrix pair (ΦE, CE) defined
by (58) is detectable.
Let us introduce the following control law for the
HOFA system (44):

[x˙ˆ(0∼n−1)] Φ(00∼n−1) BcE [xˆ(0∼n−1)]
⎧ d˙ˆ(0∼k−1) = [ 0 Φ(S0∼k−1)] dˆ(0∼k−1)

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ +[Bc]v +[Lx](Cmx(0∼n−1) − ym)

## [25] `ijss_2021_part7` (PDF p.12, L1151)

Assumption A1: The considered physical system
Σphysical, with basic equations in (26), has r number of
independent and functioning control variables.

As mentioned above, once we obtain the basic equa-
tions in (26) by mechanism for a physical system
Σphysical, on one hand one can obtain a state-space
model by the method of variable extension, while on
the other hand one can get a high-order model for
the system by the method of variable elimination. As
a result, the state-space model obtained by the method
of variable extension contains the maximum number
of independent scalar equations, while the number of
scalar equations in a high-order model obtained by the
method of variable elimination gets fewer as the order
of the model goes higher.
Now the questions is, how few can the scalar equa-
tions in a finally obtained high-order model be? There
must be a smallest number of scalar equations in such
a finally obtained high-order model. On one side, the
number of scalar equations is generally not less than
r since otherwise the system would have fewer than
r control variables, and this would contradict with

## [26] `ijss_2021_part7` (PDF p.12, L1174)

Assumption A1. On the other side, the number of
scalar equations is getting close to r as the process of
variable elimination goes. For a system which is ‘com-
pletely controllable’, in the sense that the whole set of
control variables fully determine the dynamics of the
system, the smallest number of scalar equations in the
finally obtained high-order model becomes r, in this
case a HOFA model for the system Σphysical is derived.
To summarise, we immediately have the following
fact.

## [27] `ijss_2021_part7` (PDF p.12, L1187)

Assumption A1. Further, assume that the set of control
variables of system Σphysical fully determine the dynam-
ics of the system. Then the set of basic equations in (26)
can be further converted into a HOFA model in the
form of (8) or (19) by applying the method of variable
elimination.

The fact mentioned in the above Proposition 3.3
has been demonstrated by many examples (see those
in Duan, 2020d, 2020e, 2021a, 2021b, 2021c, 2021d).
While in the case where the considered system
Σphysical or (26) is not controllable, its model appears
to be more complicated.

According to the above definition, the system pre-
sented in Example 2.4 is clearly an almost completely
controllable one. Following the above Proposition 3.1,
a controller can be properly designed to produce a con-
stant linear system. Therefore, with a choice of proper
set of initial values, the amplitude of the pitch angle
ϑ can be kept well within (−π/2, π/2). Hence the
designed control system works (see Duan, 2014 for
detail). To further demonstrate the approach, let us
present another simple example.

## [28] `ijss_2021_part7` (PDF p.14, L1388)

Assumption A1. If the system is not controllable, then it
may possess a high-order system model consisting of

xk(μk)|k=1∼η = f (xk(0∼μk−1)|k=1∼η,

yk(0∼γk−1)|k=1∼ξ, ζ, t)

+ B(xk(0∼μk−1)|k=1∼η,

yk(0∼γk−1)|k=1∼ξ, ζ, t)u, (48)

and

yk(γk)|k=1∼ξ = g (yk(0∼γk−1)|k=1∼ξ, ζ, t), (49)

where ζ ∈ ℝp is an external vector, γk, =˛1, 2, . . . , ξ, are
a set of integers, yk, k = 1, 2, . . . , ξ, are a set of vectors
of proper dimensions, f (·) and g(·) are two nonlin-
ear vector functions, while the variables in (48) are as
stated before. It is required that y(0∼γk−1)|
k k=1∼ξ and
x(0∼μk−1)|
k k=1∼η are independent from each other, and
the following full-actuation condition

det B(xk(0∼μk−1)|k=1∼η, yk(0∼γk−1)|k=1∼ξ, ζ, t) ≠ 0,
(50)
is met for xk(0∼μk−1)|k=1∼η ∈ 𝔽, arbitrary ζ ∈ ℝp, t ≥
0 and arbitrary solution y(0∼γk−1)|
k k=1∼ξ to the sys-
tem (49).

Clearly, there is another version of the above
proposition corresponding to the HOFA model (19).

Moreover, an extreme special case of the above sys-
tem (48)–(49) is the following:

x(μ) = f x(0∼μ−1), y(0∼γ −1), ζ, t
⎧⎨ +B x((0∼μ−1), y(0∼γ −1), ζ, t u) (51)
y(γ ) =( g y(0∼γ −1), ζ, t . )
⎩ ( )
The extra subsystem (49) is obviously an isolated
autonomous one since y(0∼γk−1)|k=1∼ξ and
k
x(0∼μk−1)|
k k=1∼η are independent from each other.
Based on the above Proposition 4.1, we can now intro-
duce the following definition.

## [29] `ijss_2021_part7` (PDF p.21, L2223)

Assumption A2: The parameters a0 and a1 are so
designed that the first equation in system (103) has the
solution

z = c1 e−tα1 + c2 e−tα2, (104)

where c1 and c2 are two scalars, and α1 and α2 are two
distinct positive real scalars.

Under the above assumption, we have the following
conclusion.

## [30] `ijss_2022_part10` (PDF p.15, L1606)

Assumption 1: det gi(x1∼i) ≠ 0, ∀ x1∼i ∈ ℝir, i =
1, 2, . . . , n.

## [31] `ijss_2022_part10` (PDF p.18, L1924)

Assumption 2: det B(x1∼n(k)) ≠ 0, ∀ x1∼n(k) ∈ ℝnr.

## [32] `ijss_2022_part8` (PDF p.5, L427)

Assumption A1: det B(xk(0∼μk−1)|k=1∼η, ζ, t) ≠ 0, or
∞, for all xk(0∼μk−1)|k=1∼η, ζ, and t >0.

The system (1) satisfying the above Assump-
tion A1 is called a (globally) fully actuated system
(Duan, 2020j).

## [33] `ijss_2022_part8` (PDF p.8, L852)

Assumption A1: The matrix pair [AE, DC] is observ-
1
able, where D = Q2 .
Since [Φk(00∼μk−1), Bkc], k = 1, 2, . . . , η, are all
controllable, it is easy to know that [AE, BE] is also con-
trollable. Thus it follows from the above Lemma 4.2
and Assumption A1 that the particular solution P(t)
to the Riccati differential Equation (20) satisfying the
final condition P(tf ) = P converges, as tf → ∞, to
the unique solution of the following Riccati algebraic
equation:

ATEP + PAE − PBER−1BTEP + CTQC = 0. (32)

According to optimal control theory, for the linear sys-
tem (14) the optimal controller which minimise the
index
∞
J3′ = 1 ∫ y 2Q + ‖v‖2R)dt (33)
2 0 (‖‖ ‖‖

is given by

v = −R−1BTEPx(0∼μk−1)|k=1∼η,
k

and the corresponding closed-loop system is

x˙k(0∼μk−1)|k=1∼η = (AE − BER−1BTEP)

× x(0∼μk−1)|k=1∼η, (34)
k

which is asymptotically stable according to the above

## [34] `ijss_2022_part8` (PDF p.10, L1010)

Assumption A1: The set of singular points, 𝕊, meets
the following two conditions:

(a) it does not depend on time t, that is,

𝕊 = 𝕊t = 𝕊0, t ≥ 0;

(b) it does not contain the origin, that is,

d0 = inf{‖z‖| z ∈ 𝕊} > 0.

Obviously, the above d0 is clearly the distance of the
set 𝕊 from the origin. As a consequence of the above
Assumption A3, we also have

𝔽 = 𝔽0 = 𝔽t = ℝκ\𝕊, t ≥ 0.

With the above preparation, the optimal control prob-
lem to be solved can be now stated as follows.

## [35] `ijss_2022_part9` (PDF p.5, L445)

Assumption A1: det B(xk(0∼μk−1)|k=1∼η, ζ, t) ≠ 0, or
∞, for all xk(0∼μk−1)|k=1∼η, ζ, and t ≥ 0.

The system (1) satisfying the above Assumption A1
is called a (global) fully actuated system (Duan, 2021c).
Since xk ∈ ℝrk, k = 1, 2, . . . , η, we have

x(0∼μk−1) ∈ ℝμkrk, k = 1, 2, . . . , η.
k

Denote
η
κ = ∑rkμk, (4)
k=1
then it is easy to see

x(0∼μk−1)|k=1∼η ∈ ℝκ.
k

For the above system (2), the following output
equation is imposed:

y = Cx(0∼μk−1)|k=1∼η, (5)
k

where C ∈ ℝm×κ is a known constant full-row rank
matrix.
About the considered HOFA model (1), or equiv-
alently, (2), the following remarks are made (see also,
Duan, 2021d).

## [36] `ijss_2022_part9` (PDF p.9, L938)

Assumption A2: There exist matrices G ∈ ℝκ×p and
H ∈ ℝr×p satisfying the following two equations

AEG + BEH = GAm
{ (35)
CG = Cm.

In (35), there are clearly κ + m equations, and (κ +
r)p unknowns. Recall that m ≤ r, and note p ≥ 1, we
generally have more unknowns than the number of
the equations. Therefore, this set of equations generally
have more than one solution.
Define the generalised error variables

δx = xk(0∼μk−1)|k=1∼η − Gxm
⎧
⎨ δv = v − Hxm (36)
δy = y − ym,
⎩
then, by taking derivatives of the above variables, and
using (5) and (16), we can easily obtain the following
lemma.

## [37] `ijss_2022_part9` (PDF p.12, L1345)

Assumption A2′: There exists a parameter matrix
Z ∈ ℝr×p satisfying constraint (76). ■

## [38] `ijss_2022_part9` (PDF p.13, L1449)

Assumption A3: The matrix B(·) in system (1)
depends on only the state, that is,

B (·) = B(xk(0∼μk−1)|k=1∼η).

For the general case, please refer to Duan (2021c,
2021d).

## [39] `ijss_2022_part9` (PDF p.16, L1720)

Assumption A4: There exists a xc ∈ Ω¯ and a constant
dc > 0, such that

Ω¯ ⊂ 𝔹 = {x | ‖x − xc‖ ≤ dc} , (102)

and

d0 = d (𝔹, 𝕊) > 0. (103)

Clearly, (102) assumes the boundedness of set Ω,
while (103) assumes that Ω is far away enough from
𝕊.
With the above preparation, the following result
about the MRT control of the sub-fully actuated sys-
tem (2) can be proven.

## [40] `ijss_2024_underactuated4` (PDF p.6, L630)

Assumption A2: There exists a simply connected set
Ω1 ⊂ ℝ2m, which contains the origin at least as a
boundary point, such that the second equation in (9) has
a solution with respect to x on Ω1, that is,

x = h y,y ˙, t . (11)
( )

## [41] `ijss_2024_underactuated4` (PDF p.9, L983)

Assumption A2: There exists a simply connected set
U1 ⊂ ℝ2m+n, which contains the origin at least as a
boundary point, such that the last equation in (37) has
a solution with respect to x2 on U1, that is,

x2 = h (x1, x3,x ˙3, t) . (38)

Clearly, in the case that Bˆi(x1, x2, x3, t), i = 1, 2,
are nonsingular for all their variables, system (37) is
reduced to the following simple form:

⎧x˙1 = u1
⎨x˙2 = u2 (39)
x˙3 = g (x1, x2, x3, t) .
⎩
For convenience, we also define
∂g (x1, x2, x3, t)
Gi = , i = 1, 2, 3,
∂xi
∂g (x1, x2, x3, t)
Gt = .
∂t

## [42] `ijss_2024_underactuated4` (PDF p.12, L1306)

Assumption A2′: There exists a simply connected set
U1′ ⊂ ℝnp+2m, which contains the origin at least as a
boundary point, such that the last equation in (65) has
a solution with respect to x2 on U1′, that is,

(0∼p−1)
x2 = h(x1 , x3,x ˙3, t). (66)

When Assumption A2′ is met, it can be similarly
proven that, under the following homeomorphism
(x1, x2, x3) → (x, y,y ˙) :

⎧x1 = x
⎪⎨x2 = h(x(0∼p−1), y,y ˙, t) (67)

x3 = y,
⎪⎩

system (65) is equivalent to the following sub-FAS:

x(p) f0(x(0∼p−1), y,y ˙, t) u1
[ ] = [ (0∼p−1) ] + B (·)[ ], (68)
y¨ f (x , y,y ˙, t) u2

where
B0(x(0∼p−1), y,y ˙, t) 0
B (·) = [B1 x(0∼p−1), y,y, t B2 x(0∼p−1), y,y, t ],
( ˙ ) ( ˙ )

and f0(·), B0(·), f (·), B1(·), and B2(·) are given as
in Theorem 4.1, with x being replaced by x(0∼p−1).
Furthermore, the set of feasibility of the above sub-
FAS (68) is given by U′ = U1′ ∩ U2′, with

U2′ = X, y, z | det B0(X, y, z, t)B2 X, y, z, t ≠ 0
{( ) ( ( ))
or ∞, X ∈ ℝnp , y, z ∈ ℝm , and t ≥ 0 .
}
Obviously, the corresponding extension of system (39)
takes the following form:

(p)
⎧x1 = u1
⎪⎪⎨x˙2 = u2 (69)
(0∼p−1)
x˙3 = g (x1 , x2, x3, t).
⎪⎪⎩
Again, when Assumption A2′ is satisfied, under the
homeomorphism (67), it can be easily shown that sys-
tem (69) is equivalent to the following sub-FAS:

x(p) [ 0 ] u1
[ ] = (0∼p−1) + B (·)[ ], (70)
y¨ f (x , y,y ˙, t) u2

where

In 0
B (·) = [B1 x(0∼p−1), y,y, t B2 x(0∼p−1), y,y, t ],
( ˙ ) ( ˙ )

and f (x(0∼p−1), y,y ˙, t), B1(x(0∼p−1), y,y ˙, t), and
B2(x(0∼p−1), y,y ˙, t) are given as in Corollary 4.1, with
x being replaced by x(0∼p−1). Furthermore, the set of
feasibility of the above sub-FAS (70) is given by U′′ =
U1′ ∩ U2′′, with

## [43] `ijss_2024_underactuated4` (PDF p.13, L1454)

Assumption A3: There exists a set W1 ⊂ ℝ4n on
which (76) has a solution

⎧q1 = h1(q(20∼3), t)
⎨ (0∼3) (77)
q˙1 = h2(q2 , t).
⎩
Based on the above assumption, we can introduce
the following map:

q1 = h1 q(0∼3), t
⎧⎨q1 = h2(q(0∼3), t) (78)
˙ ( )
q2 = q.
⎩

## [44] `ijss_2024_underactuated4` (PDF p.16, L1867)

Assumption A4: There exists a set H1 ⊂ ℝ2n+4m on
which equation (117) has a solution

⎧q1 = h1(q(00∼1), q(20∼3), t)
⎨ (0∼1) (0∼3) (118)
q˙1 = h2(q0 , q2 , t).
⎩
Based on the above assumption, we can introduce the
following map:

q0 = x
⎧
⎪⎪⎨q2 = y (119)
q1 = h1 x(0∼1), y(0∼3), t
q1 = h2(x(0∼1), y(0∼3), t).
⎪⎪⎩˙ ( )

## [45] `ijss_2024_underactuated4` (PDF p.19, L2160)

Assumption A4′: There exists a set H1′ ⊂ ℝnp+4m on
which equation (137) has a solution

(0∼p−1) (0∼3)
⎧q1 = h1(q0 , q2 , t)
⎨ (0∼p−1) (0∼3) (138)
q˙1 = h2(q0 , q2 , t).
⎩
Based on the above assumption, we can introduce
the following homeomorphism

⎧q0 = x
q2 = y
⎪⎪⎪⎪⎨q1 = h1(x(0∼p−1), y(0∼3), t) (139)

q˙1 = h2(x(0∼p−1), y(0∼3), t).
⎪⎪⎪⎪⎩

Let Assumption A4′ be met. Then, under the home-
omorphism (139), it can be similarly proven that sys-
tem (135) is equivalently converted into the following
sub-FAS:

x(p) [f˘1(x(0∼p−1), y(0∼3), t)] v
[y(4)] = (0∼p−1) (0∼3) + B (·)[u],
f (x , y , t)
(140)

where

B (·)

[B˘1(x(0∼p−1), y(0∼3), t) 0 ]
= ,
B1(x(0∼p−1), y(0∼3), t) B2(x(0∼p−1), y(0∼3), t)

and the functions f (·), B1(·) and B2(·) are given
as in Theorem 6.1, with x(0∼1) being replaced by
x(0∼p−1), and (120)–(122), with q(0∼1) being replaced
0
(0∼p−1)
by q0 . Furthermore, the set of feasibility of sub-
FAS (140) is given by H′ = H1′ ∩ H2′, with

H2′ = (X, Y) |det B˘1 (X, Y, t) B2(X, Y, t) ≠0 or ∞,
{ [ ]
X ∈ ℝnp, Y ∈ ℝ4m and t ≥ 0 . (141)
}

For UAS (115), the corresponding extended form is

(p)
⎧q0 = v
⎪⎪⎨q¨1 = u (142)
(0∼p−2) (0∼1)
q¨2 = g (q0 , q1, q2 , t).
⎪⎪⎩
Again, when Assumption A4′ is met, under the home-
omorphism (139), it can be shown that system (142) is
equivalently converted into the following sub-FAS:

x(p) 0 v
[y(4)] = [f (x(0∼p−1), y(0∼3), t)] + B (·)[u],

(143)

## [46] `odfas_2026_part4` (PDF p.10, L680)

Assumption A0 det B (Y, t) ≠ 0 or ∞, ∀Y ∈ ℝmq, t ≥ 0;

M (ϕ) ∈ ℝr×r is differentiable and satisfies

## [47] `odfas_2026_part4` (PDF p.10, L684)

Assumption A1 R (ϕ) = M−1(ϕ) exists for all ϕ ∈ ℝnϕ.

To express the other assumption on M (ϕ), let us introduce the following concepts.

## [48] `odfas_2026_part4` (PDF p.11, L714)

Assumption A2 M (ϕ) meets one of the following conditions:

1. it is uniformly bounded;

2. it sublinearly grows with respect to ϕ ∈ ℝnϕ;

3. it is locally Lipschitz.

## [49] `odfas_2026_part4` (PDF p.18, L1103)

Assumption Ap1 A1(ϕ(0∼1)) is smooth and uniformly bounded.

If both x and x ˙ are measured, we can design a full-state feedback controller for system (4.4) as

u0 = −F0x −(F1 + R (ϕ) A1(ϕ(0∼1)))x,˙ (4.18)

where F0∼1 ∈ ℝr×2r makes Φ(F0∼1) Hurwitz. The closed-loop system is given by

x¨ + F1x ˙ + F0x = 0. (4.19)

Now, since q2 = ˙x in (4.18) is unknown, let us substitute x ˙ with q ˆ2, and get the following observer-

based controller

u0 = −F0y −(F1 + R (ϕ) A1(ϕ(0∼1)))qˆ2.

Based on this idea, we further obtain the following result.

## [50] `odfas_2026_part4` (PDF p.25, L1493)

Assumption AD AD ∈ ℝr×r is a Hurwitz matrix.

Under Assumption A1, system (5.1) can be equivalently converted into

x¨ (t) = R (ϕ (t)) A0∼1(ϕ(0∼1)(t))x(0∼1)(t)

+ R (ϕ (t)) fy (y (t − σi (t))|i=1∼p , t)

{ + R (ϕ (t)) B(y (t − τj (t))|j=1∼q , t)u (t) (5.3)
+ R (ϕ (t)) d (t)
y (t) = x (t) .

Further, under control transformation (4.3), the above system is transformed into

x¨ = R (ϕ) A1(ϕ(0∼1))x˙ + u0 + R (ϕ) d
{ (5.4)
y = ⌊Ir 0⌋x(0∼1).

Therefore, the output feedback control problem of system (5.1) reduces to the output feedback control

problem of the above system (5.4).

## [51] `odfas_2026_part4` (PDF p.29, L1675)

Assumption Ap2 R (ϕ) is uniformly bounded and uniformly positive definite.

Due to this assumption, we know that R−1(ϕ) is also uniformly bounded and uniformly positive

definite.

Firstly, let us state a simple result.

## [52] `odfas_2026_part4` (PDF p.38, L2172)

Assumption Av1 det A0(ϕ(0∼1)) ≠ 0, ∀ϕ(0∼1) ∈ ℝ2nϕ.

## [53] `odfas_2026_part4` (PDF p.38, L2174)

Assumption Av2 A−01(ϕ(0∼1)) meets one of the following conditions:

1. it is uniformly bounded;

2. it sublinearly grows with respect to ϕ(0∼1) ∈ ℝ2nϕ;

3. it is local Lipschitz.

Under Assumption A0, the following control transformation can be proposed:

u (t) = −B−1 y (t − τj (t))|j=1∼q , t)(u′(t) − M (ϕ) u0 (t))
{ ( (0∼1) (6.4)
u′(t) = fy (y (t − σi (t))|i=1∼p , t) + A1(ϕ (t))y (t) ,

under which system (6.3) is reduced to

x¨ = R (ϕ) A0(ϕ(0∼1))x + u0
{ (6.5)
y = ⌊0 Ir⌋x(0∼1).

## [54] `odfas_2026_part4` (PDF p.52, L2968)

Assumption AG There exists a constant vector h ∈ ℝ3 such that

G†[ = G† +⌊03×2 h⌋ (8.9)

is nonsingular.

Please note that, in the case that matrix G† is already nonsingular, we may simply choose h = 0.

Under the above assumption and relation (8.7), system (8.8) can be converted into

Mv ˙ + D†(v) + G†[η = τ† − G†η∗ + hφ + Δτ†
{η˙ = R (φ) v −η ˙∗ (8.10)
y† = v.

Further, denote

D (v) = M−1D†(v) ,

G = M−1G†,

G[ = M−1G†[,

d = M−1Δτ†,

and

u = M−1τ† − D(y†) − Gη∗ + M−1hφ. (8.11)

Then system (8.10) can be further converted into

v˙ + G[η = u + d
{η˙ = R (φ) v −η ˙∗ (8.12)
y† = v.

Through the above treatments, the problem to be solved in this section becomes one of solving the

output feedback stabilization of system (8.12). Before proceeding further with the solution, let us first

give a preliminary result.

Denote
0 −1 0
E = 1 0 0 . (8.13)
0 0 0

Then, as a preliminary result, we can summarize some of the known results regarding R (φ).

## [55] `scis_2022_discdelay1` (PDF p.8, L499)

Assumption 1. det gi (x1∼i (k)) ≠ 0, ∀x1∼i (k) ∈ ℝir, i = 1, 2, . . . , n, and k ⩾ h.
In [29], it is shown that the above strict-feedback system (25), with h = 0, can be equivalently converted
into a FAS with state delays only. Applying this result to the above strict-feedback system (25), with
h ≠ 0, gives the following result which tells us that a strict-feedback system (25) with input delay can be
converted equivalently into a FAS with both state and control delays.

## [56] `scis_2022_discdelay1` (PDF p.9, L548)

Assumption 2. det B x⌈τ1∼ζ(k)⌉(k) , k ≠ 0, ∀x⌈τ1∼ζ(k)⌉(k) and k ⩾ h.
Corresponding to the general linear discrete-time delay FAS (13) with interconnections, we can also()
propose the following nonlinear discrete-time delay FAS with interconnections:

x1 (k + 1) ⌈τp,1∼ζp(k)⌉
f1(xp (k) |p=1∼η, k)

x2 (k + 1) ⌈τp,1∼ζp(k)⌉
f2(xp (k) |p=1∼η, k) ⌈τp,1∼ζp(k)⌉
= + B(xp (k) |p=1∼η, k)u (k − h) , (30)
... ...
⌈τp,1∼ζp(k)⌉
fη(xp (k) |p=1∼η, k)
xη (k + 1)

where, again, ζp, p = 1, 2, . . ., η, are a set of distinct integers, xp ∈ ℝrp, p = 1, 2, . . . , η, are a set of
state vectors, with rp, p = 1, 2, . . ., η, being a set of distinct integers satisfying (5). τp,1∼ζp (k) , p =
1, 2, . . . , η, are the delay vectors defined in (14). Further, fp (·) ∈ ℝrp, p = 1, 2, . . . , η, are a set of nonlinear
vector functions, and B (·) ∈ ℝr×r is a nonlinear matrix function satisfying the following full-actuation
assumption.
⌈τp,1∼ζp(k)⌉ ⌈τp,1∼ζp (k)⌉

## [57] `scis_2022_discdelay1` (PDF p.9, L569)

Assumption 3. det B(xp (k) |p=1∼η, k) ≠ 0, ∀xp (k) |p=1∼η, and k ⩾ h.
Let
f1 (·, k)
f2 (·, k)
f (·, k) = , (31)
...
fη (·, k)
and then the FAS (30) can be compactly written as

⌈τp,1∼ζp(k)⌉ ⌈τp,1∼ζp(k)⌉
x1∼η (k + 1) = f (xp (k) |p=1∼η, k)+ B(xp (k) |p=1∼η, k)u (k − h) . (32)

In fact, under Assumption 3, we can introduce a new control vector in the following way:

⌈τp,1∼ζp(k)⌉
u˜ (k − h) = B(xp (k) |p=1∼η, k)u (k − h) ,

and then the system (32) can be written into the following standard form:

⌈τp,1∼ζp(k)⌉
x1∼η (k + 1) = f (xp (k) |p=1∼η, k)+ ˜u (k − h) . (33)

Furthermore, this system can also be written in the following decoupled form:

⌈τp,1∼ζp(k)⌉
xi (k + 1) = fi(xp (k) |p=1∼η, k)+ ˜ui (k − h) , i = 1, 2, . . ., η, (34)

where ˜ui, i = 1, 2, . . . , η are defined as

u˜1
u˜2 ri
u˜ = , u˜i ∈ ℝ . (35)
...
u˜η

## [58] `scis_2022_discdelay1` (PDF p.10, L616)

Assumption 4. g x⌈τ1∼ζ(k)⌉(k) , k, u = ˜u forms a differential homeomorphism from u to ˜u for all
x⌈τ1∼ζ(k)⌉(k) and k ⩾( h. )
Corresponding to the general nonlinear affine discrete-time delay FAS (32) with interconnections, we
can also propose the following non-affine discrete-time delay FAS with interconnections:

⌈τp,1∼ζp(k)⌉ ⌈τp,1∼ζp(k)⌉
x1∼η (k + 1) = f (xp (k) |p=1∼η, k)+ g(xp (k) |p=1∼η, k, u (k − h)), (37)

where g (·) ∈ ℝr is a nonlinear function satisfying the following full-actuation assumption.
⌈τp,1∼ζp(k)⌉

## [59] `scis_2022_discdelay1` (PDF p.10, L626)

Assumption 5. g(xp (k) |p=1∼η, k, u) = ˜u forms a differential homeomorphism from u to ˜u for
⌈τp,1∼ζp(k)⌉
all xp (k) |p=1∼η and k ⩾ h.
Under Assumption 5, the following new control can be also introduced:

⌈τp,1∼ζp(k)⌉
u˜ (k − h) = g(xp (k) |p=1∼η, k, u (k − h)),

and with this control variable transformation, the FAS (37) can be also turned into the standard form of
(33), as well as the decoupled form of (34).

## [60] `scis_2022_discdelay1` (PDF p.10, L654)

Assumption 6. B(x⌈pτp,1∼ζp(k)⌉(k) |p=1∼η, u⌈σ1∼ξ(k)⌉(k − h) , k) is nonsingular for all its variables when
k ⩾ h.
Let
f1 (·, ·, k)
f2 (·, ·, k)
f (·, ·, k) = , (39)
...
fη (·, ·, k)

and then the time-delay FAS (38) can be compactly written as

x1∼η (k + 1) = f (xp⌈τp,1∼ζp(k)⌉(k) |p=1∼η, u⌈σ1∼ξ(k)⌉(k − h) , k)

+B(xp⌈τp,1∼ζp(k)⌉(k) |p=1∼η, u⌈σ1∼ξ(k)⌉(k − h) , k)u (k − h) . (40)

The above FAS can be further simply written in the form of

x1∼η (k + 1) = fx,u (k) + Bx,u (k) u (k − h) (41)

Duan G R Sci China Inf Sci August 2022 Vol. 65 182201:11

with the following notations:

fx,u (k) ≜ f (xp⌈τp,1∼ζp(k)⌉(k) |p=1∼η, u⌈σ1∼ξ(k)⌉(k − h) , k),

Bx,u (k) ≜ B(xp⌈τp,1∼ζp(k)⌉(k) |p=1∼η, u⌈σ1∼ξ(k)⌉(k − h) , k). (42)

Parallel to the extended affine FAS (38), the following extended non-affine one can also be defined:

x1∼η (k + 1) = fx,u (k) + g(xp⌈τp,1∼ζp(k)⌉(k) |p=1∼η, u⌈σ1∼ξ(k)⌉(k − h) , k, u (k − h)), (43)

where ˜u = g (·, ·, k, u) forms a differential homeomorphism from u to ˜u.

## [61] `scis_2022_discdelay2` (PDF p.8, L500)

Assumption 1. detB (X, k) ≠ 0 or ∞, ∀X ∈ ℝκ(k) and k ⩾ h.
Parallelly, the non-affine discrete-time delay FAS (20) has the following equivalent form:

x (k + 1) = f (ψ (k) , k) + g(x⌈p0∼γp(k)⌉(k) , k, u (k − h)), (32)
|||p=1∼r

where ψ (k) takes one of the forms in (28)–(30), and represents the delay terms in the f (·) function, while
the function g (·) satisfies the following assumption.

## [62] `scis_2022_discdelay2` (PDF p.8, L508)

Assumption 2. g (X, k, u) = ˜u forms a differential homeomorphism from u to ˜u for all X ∈ ℝκ(k) and
k ⩾ h.
We point out that the above two assumptions are not at all too conservative, but are relatively general.
To understand this point, it is suggested to refer to [1]. Furthermore, it is noted that a sufficient condition
for the above Assumption 2 is that ∂u∂g (X, k, u) is nonsingular for all X ∈ ℝκ(k) and k ⩾ h.
As a further generalization of the discrete-time time-delay system (27), the following discrete-time
system with time-varying multiple input delays is proposed:

x (k + 1) = fe x⌈0∼ρ(k)⌉(k) , u⌈1∼ξ(k)⌉(k − h) , k + Be x⌈0∼ρ(k)⌉(k) , u⌈1∼ξ(k)⌉(k − h) , k u (k − h) ,
( ) ( )
(33)
where ξ (k) ⩾ 1 is a positive integer-valued function, representing the number of delays in the control
vector, fe (·) ∈ ℝr and Be (·) ∈ ℝr×r are proper nonlinear vector and matrix functions, respectively, while
the other variables are as stated before.
Parallel to the extended affine system (33), the following extended non-affine one can also be defined:

x (k + 1) = fe x⌈1∼ρ(k)⌉(k) , u⌈1∼ξ(k)⌉(k − h) , k + ge x⌈1∼ρ(k)⌉(k) , u⌈1∼ξ(k)⌉(k − h) , k, u (k − h) ,
( ) ( )
(34)
where ˜u = ge (X, U, k, u) forms a differential homeomorphism from u to ˜u for all X ∈ ℝrρ(k), U ∈ ℝrξ(k)
and k ⩾ h.

## [63] `scis_2023_delay1` (PDF p.4, L278)

Assumption A. There exists a non-empty set Ω1 ⊂ ℝγr such that det B1 (X, t) ≠ 0 or ∞, for all X ∈ Ω1
and t ⩾ 0.

## [64] `scis_2023_delay1` (PDF p.4, L280)

Assumption B. There exists a non-empty set Ω2 ⊂ ℝ2γr such that det B2 (Y, t) ≠ 0 or ∞, for all Y ∈ Ω2
and t ⩾ 0.

## [65] `scis_2023_delay1` (PDF p.7, L471)

Assumption A1. det B (X, t) ≠ 0 or ∞, ∀X∈ℝγnr and t ⩾ 0.
Recall that the system (23)-(24) obtained in Example 1 serves as an example for a single-order FAS
when the condition (16) is met.
Under the above assumption, we can define a new control

u˜ (t) = B x(0∼n−1)(t − σj (t)) |j=1∼γ, t u (t) , (29)
( )

and write the FAS (26) into the following standard form:

x(n)(t) = f x(0∼n−1)(t − τj (t)) |j=1∼ζ, t + ˜u (t) . (30)
( )

Particularly, a constant linear single-order FAS with state time delays is of the following form:
m
x(n)(t) = Cix(0∼n−1)(t − τi (t)) + Bu (t) , (31)
∑i=0

where B is a constant square nonsingular matrix, and Ci ∈ ℝr×nr, i = 0, 1, . . ., m are the coefficient
matrices.

## [66] `scis_2023_delay1` (PDF p.8, L510)

Assumption A2. The following mapping

u˜ (t) = g (X, t, u (t)) (33)
forms a differential homeomorphism from u to ˜u for all X ∈ ℝγnr and t ⩾ 0.
Due to Assumption A2, we can introduce the control vector transformation

u˜ (t) = g x(0∼n−1)(t − σj (t)) |j=1∼γ, t, u (t) , (34)
( )
under which the single-order non-affine (global) FAS (32) can be equivalently represented into the stan-
dard form of (30).

## [67] `scis_2023_delay1` (PDF p.9, L572)

Assumption A3. det B (X, t) ≠ 0 or ∞, ∀X ∈ ℝγκ0 and t ⩾ 0.
Let

f1 xk(0∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, t
( )
(0∼µk−1) f2 xk(0∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, t
f xk (t − τj (t)) |k=1∼η, j=1∼ζ, t = ( ) . (41)
( )
...
fη xk(0∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, t
( )
Then the FAS (35) can be compactly written as

x(kµk)|k=1∼η (t) = f xk(0∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, t
( )
+ B xk(0∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, t u (t) . (42)
( )
Obviously, in the case of η = 1, the above FAS model (35), or (42), reduces to the form of the
single-order FAS (26).
Under Assumption A3, we can in fact introduce a new control vector

u˜ (t) = B x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, t u (t) , (43)
( )
and now the (global) FAS (42) can be written in the following standard form:

x(kµk)|k=1∼η (t) = f xk(0∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, t + ˜u (t) , (44)
( )
or
x(iµi)(t) = fi x(0k∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, t + ˜ui (t) , i = 1, 2, . . . , η, (45)
( )
where ˜ui, i = 1, 2, . . . , η are defined by

u˜1
u˜2 ri
u˜ = , u˜i ∈ ℝ . (46)
...
u˜η

As a special case of the multi-order nonlinear time-delay FAS (42), a constant linear multi-order FAS
with state delays is in the form of
m
x(kµk)|k=1∼η (t) = Dixk(0∼µk−1)(t − τi (t)) |k=1∼η + Bu (t) , (47)
∑i=0
where B is a constant square nonsingular matrix, and Di ∈ ℝr×γκ0, i = 0, 1, . . ., m are the coefficient
matrices.
For convenience, in the following of this paper we also use the following notation introduced in [51]:

x (t − τ1 (t))

⌈τ1∼ζ(t)⌉ x (t − τ2 (t))
x ≜ x (t − τj (t))|j=1∼ζ = . (48)
...
x (t − τζ (t))

Duan G R Sci China Inf Sci January 2023 Vol. 66 112201:10

## [68] `scis_2023_delay1` (PDF p.10, L640)

Assumption A4. The following mapping

u˜ (t) = g (X, t, u (t)) (50)

forms a differential homeomorphism from u to ˜u for all X ∈ ℝγκ0 and t ⩾ 0.
Due to the above Assumption A4, we can similarly introduce the following control vector transforma-
tion:
u˜ (t) = g x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, t, u (t) , (51)
( )
and the multi-order non-affine (global) FAS (49) can also be represented into the standard form of (44).

## [69] `scis_2023_delay1` (PDF p.26, L1686)

Assumption A5. det B (X, Y, t) ≠ 0 or ∞, ∀X ∈ ℝγκ0, Y ∈ ℝrξ and t ⩾ 0.
Under Assumption A5, we can introduce a new control vector

u˜ (t) = B x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, u (t − ωj (t)) |j=1∼ξ, t u (t) , (139)
( )
and now the (global) FAS (138) can be written in the following standard form:

x(kµk)|k=1∼η (t) = f x(0k∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, u (t − ωj (t)) |j=1∼ξ, t + ˜u (t) . (140)
( )
Parallel to the above multi-order affine FAS (138), we can also introduce the following multi-order
non-affine generalized one:

x(kµk)|k=1∼η (t) = f x(0k∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, u (t − ωj (t)) |j=1∼ξ, t
( )
+g x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, u (t − ωj (t)) |j=1∼ξ, t, u (t) . (141)
( )
The above system (141) is called a non-affine (global) FAS if the function g (·) satisfies the following
assumption.

## [70] `scis_2023_delay1` (PDF p.26, L1704)

Assumption A6. The following mapping

u˜ (t) = g (X, Y, t, u (t)) (142)

forms a differential homeomorphism from u to ˜u for all X ∈ ℝγκ0, Y ∈ ℝrξ and t ⩾ 0.
Due to Assumption A6, we can similarly introduce the following control vector transformation:

u˜ (t) = g x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, u (t − ωj (t)) |j=1∼ξ, t, u (t) , (143)
( )
under which the multi-order non-affine (global) FAS (141) is also turned into the standard form of (140).

Duan G R Sci China Inf Sci January 2023 Vol. 66 112201:27

## [71] `scis_2023_delay2` (PDF p.6, L407)

Assumption A1. det B (X, t) ≠ 0 or ∞, ∀X ∈ ℝγnr and t ⩾ 0.
Clearly, a constant linear single-order FAS with state time-varying delays and a constant input delay
is of the following form:
m
x(n)(t) = Cix(0∼n−1)(t − τi (t)) + Bu (t − h) , (22)
∑i=0
where B is a constant square nonsingular matrix, and Ci ∈ ℝr×nr, i = 0, 1, . . ., m are the coefficient
matrices.
Parallel to the above single-order affine FAS (21), we can also define the following non-affine one:

x(n)(t) = f x(0∼n−1)(t − τj (t)) |j=1∼ζ, t + g x(0∼n−1)(t − σj (t)) |j=1∼γ, t, u (t − h) , (23)
( ) ( )
where g (·) ∈ ℝr is a nonlinear function, and the other variables are as stated before. Particularly, we
call the system (23) a single-order non-affine (global) FAS if the function g (·) satisfies the following
assumption.

## [72] `scis_2023_delay2` (PDF p.6, L422)

Assumption A1′. The following mapping:

u˜ (t) = g (X, t, u (t)) (24)

forms a differential homeomorphism from u to ˜u for all X ∈ ℝγnr and t ⩾ 0.

Duan G R Sci China Inf Sci February 2023 Vol. 66 122201:7

## [73] `scis_2023_delay2` (PDF p.7, L472)

Assumption A2. det B (X, t) ≠ 0 or ∞, ∀X ∈ ℝγκ0 and t ⩾ 0.
Obviously, in the case of η = 1, the above FAS model (28) reduces to the form of the single-order FAS
(21).
As a special case of the multi-order nonlinear time-delay FAS (28), a constant linear multi-order FAS
with time-varying state delays and a constant input delay is in the form of
m
x(kµk)|k=1∼η (t) = Dixk(0∼µk−1)(t − τi (t)) |k=1∼η + Bu (t − h) , (31)
∑i=0

where B is a constant square nonsingular matrix, and Di ∈ ℝr×κ0, i = 0, 1, . . ., m are the coefficient
matrices.
Parallel to the above multi-order affine FAS (28), we can also define the following multi-order non-affine
one:

x(kµk)|k=1∼η (t) = f x(0k∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, t
( )
+g xk(0∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, t, u (t − h) , (32)
( )

where g (·) ∈ ℝr is a nonlinear function, and the other variables are as stated before. We call the
system (32) a non-affine (global) multi-order FAS if the function g (·) satisfies the following assumption:

Duan G R Sci China Inf Sci February 2023 Vol. 66 122201:8

## [74] `scis_2023_delay2` (PDF p.8, L498)

Assumption A2′. The following mapping:

u˜ (t) = g (X, t, u (t)) (33)

forms a differential homeomorphism from u to ˜u for all X ∈ ℝγκ0 and t ⩾ 0.

## [75] `scis_2023_delay2` (PDF p.8, L504)

Assumption A2:
u˜ (t − h) = B xk(0∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, t u (t − h) , (34)
( )
or the following new one for the non-affine FAS (32) under Assumption A2′:

u˜ (t − h) = g x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, t, u (t − h) . (35)
( )

Consequently, the (global) affine FAS (28) or the non-affine FAS (32) can be converted into the following
standard form:

x(kµk)|k=1∼η (t) = f x(0k∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, t + ˜u (t − h) , (36)
( )

which can be written separately as

x(iµi)(t) = fi x(0k∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, t + ˜ui (t − h) , i = 1, 2, . . ., η, (37)
( )

where ˜ui, i = 1, 2, . . . , η are defined by

u˜1
u˜2 ri
u˜ = , u˜k ∈ ℝ . (38)
...
u˜η

However, the transformations (34) and (35) may become unrealizable if h > 0 since future states may be
involved in these transformations.

## [76] `scis_2023_delay2` (PDF p.9, L606)

Assumption A3. The system (46) has a unique solution with respect to arbitrarily given initial values
and external input u (t).
Then, note that
Z (s) = Y (t + s) = x(0∼n−1)(t + s).

We immediately have the following result.

## [77] `scis_2023_delay2` (PDF p.12, L812)

Assumption A4. The system (67) has a unique solution with respect to arbitrarily given initial values
and external input u (t) .
Then following the same procedure as in the case of single-order FAS, we can obtain the following
result.

Duan G R Sci China Inf Sci February 2023 Vol. 66 122201:13

## [78] `scis_2024_chained1` (PDF p.4, L280)

Assumption A1. For all x0, u0 ∈ ℝ, xi+1∼n ∈ ℝn−i, and t ⩾ 0, there holds

ψˆi (x0, xi+1∼n, u0, t) ≠ 0, i = 1, 2, . . ., n − 1.

Clearly, system (6) is a time-invariant one if and only if ˆϕi (·) ≜ ϕ ˆi (x0, xi+1∼n, u0, t) and ψˆi (·) ≜
ψˆi (x0, xi+1∼n, u0, t), i = 1, 2, . . ., n − 1, are all time-invariant (dependent on xi, i = 0, 1, . . ., n, and
u0 only). Furthermore, because of (7), the above system (6) is in fact a unified representation of 2n−1
number of systems.
In the special case of

ϕˆi (x0, xi+1∼n, u0, t) = 0, ψˆi (x0, xi+1∼n, u0, t) = 1, i = 1, 2, . . ., n − 1,

the above system (6), with ρi = x0, i = 1, 2, . . ., n − 1, becomes the Brockett’s first chained form (4)
which clearly contains the Brockett’s first example system (1) as a special case [1,2]; while the above (6),
with ρi = u0, i = 1, 2, . . . , n−1, becomes the Brockett’s second chained form (5) which obviously contains
the famous Brockett integrator (3) as a special case [1,2].
The following result reveals some special features of the proposed system (6).

## [79] `scis_2024_chained1` (PDF p.6, L435)

Assumption B1. There exists a ball (neighborhood) 𝔹ˆ0 centered at (x0∼n, u0) = (0, 0), such that

ψˆi (x0, xi+1∼n, u0, t) ≠ 0, ∀ (x0∼n, u0) ∈ 𝔹 ˆ0, t ⩾ 0, i = 1, 2, . . ., n − 1.

Corresponding to the above Definition 1, we also have the following one.

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:7

## [80] `scis_2024_chained1` (PDF p.7, L483)

Assumption C1. For all Xi ∈ ℝn−i+1, i = 1, 2, . . ., n − 1, y ∈ ℝ, and t ⩾ −h, there holds

ψˆid(Xi, y, t) ≠ 0, i = 1, 2, . . ., n − 1.

The above description for time-delay systems gives only the globally normal case as guaranteed by the
above Assumption C1. We point out that the proposed FAS approach can also be extended to treat the
time-delay locally normal case and the sub-normal case.
For simplicity, in this paper, we will only treat the above case where the functions ˆϕdi(·) and ˆψid(·) ,
i = 1, 2, . . . , n − 1 possess the forms in (16) and (17), or, in other words, u0 and each xj have only simple
delays. As a matter of fact, the proposed approach is also applicable to the cases where these two sets of
functions are in much more complicated forms as shown in the following two cases.
(1) Multiple delays. When u0 and each xj in ˆϕdi(·) have the multiple delays τi,j,k, k = 1, 2, . . ., pij,
and u0 and each xj in ψˆid(·) have known multiple delays σi,j,k, k = 1, 2, . . . , qij, the functions ˆϕdi(·) and
ψˆid(·) , i = 1, 2, . . . , n − 1 may appear as follows:

ϕˆdi(·) ≜ ϕ ˆdi(ξi, u0 (t − τi,0,1∼pi0) , t − τi) , ψ ˆid(·) ≜ ψ ˆid(ζi, u0 (t − σi,0,1∼qi0) , t − σi) , (18)

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:8

where

ξi = xj t − τi,j,1∼pij |j=0,i+1∼n, ζi = xj t − σi,j,1∼qij |j=0,i+1∼n, i = 1, 2, . . . , n − 1.
( ) ( )
(2) Distributed delays. When u0 and each xj in ˆϕdi(·) and ˆψid(·) have distributed delays, the functions
ϕˆdi(·) and ˆψid(·) , i = 1, 2, . . ., n − 1 may appear as follows:

τi0 σi0
ϕˆdi(·) ≜ ϕ ˆdi(ξi,∫ pi0(θ)u0(t − θ)dθ, t − τi), ψˆid(·) ≜ ψ ˆid(ζi,∫ qi0(θ)u0(t − θ)dθ, t − σi), (19)
0 0

where
τij σij
ξi = ∫ kijϕ(θ)xj(t − θ)dθ , ζi = ∫ kijψ(θ)xj(t − θ)dθ , i = 1, 2, . . ., n − 1, (20)
0 ||||j=0,i+1∼n 0 ||||j=0,i+1∼n

with kijϕ : [0, τij] → ℝ and kijψ : [0, σij] → ℝ denoting the delay kernels.

## [81] `scis_2024_chained1` (PDF p.9, L568)

Assumption A2. For all x0 ∈ ℝ, xi+1∼n ∈ ℝn−i, and t ⩾ 0, there holds

ψi (x0, xi+1∼n, t) ≠ 0, i = 1, 2, . . . , n − 1.

Furthermore, with (23), the subsystem (22) can be rewritten as

x˙1 = u,
x˙2 = x2ϕ1 (·) + γ1x0x1ψ1 (·) ,
x˙3 = x3ϕ2 (·) + γ2x0x2ψ2 (·) , (28)
{
...
x˙n = xnϕn−1 (·) + γn−1x0xn−1ψn−1 (·) ,

where
1, if ρi = x0,
γi = { (29)
−β, if ρi = u0.

In the case that system (28) is looked upon as an individual problem, we can replace (29) with

γi ∈ {1, −β}, i = 1, . . . , n − 1. (30)

In this case, system (28) is a unified representation of 2n−1 number of systems.
Parallel to Definition 1, a nonlinear system in the form of (28) is also called globally normal if As-
sumption A2 is satisfied. For system (28), we can also introduce the local assumption.

## [82] `scis_2024_chained1` (PDF p.9, L593)

Assumption B2. There exists a ball (neighborhood) 𝔹0 centered at x0∼n = 0, such that

ψi (x0, xi+1∼n, t) ≠ 0, ∀x0∼n ∈ 𝔹0, t ⩾ 0, i = 1, 2, . . ., n − 1.

Corresponding to Definition 1, the nonlinear system (28) is also called locally normal if Assumption B2
is satisfied. Otherwise, it is called abnormal.
When u0 is designed as in (23), x0 (t) is given by (25). Hence, in the above subsystem (28), x0 (t) =
x0 (0) e−βt is a time-varying parameter rather than a state variable. Since x0 (t) = 0, t ⩾ 0 makes the
subsystem (28) uncontrollable, let us impose the following assumption.

## [83] `scis_2024_chained1` (PDF p.9, L602)

Assumption X. x0 (t) = x0 (0) e−βt, x0 (0) ≠ 0.
Based on the above deduction, it can be clearly seen that, to stabilize system (6), it suffices to solve
the following basic problem.

## [84] `scis_2024_chained1` (PDF p.11, L704)

Assumption A3. For all x0 ≠ 0, z1∼i ∈ ℝi and t ⩾ 0, there holds

hi (x0, z1∼i, t) ≠ 0, i = 1, 2, . . . , n − 1.

Clearly, system (33) is an SFS when the above Assumption A3 is met.
According to the above Theorem 1, Problem 1 is clearly equivalently converted into the following one.

## [85] `scis_2024_chained1` (PDF p.23, L1462)

Assumption C2. For all Xi ∈ ℝn−i+1, i = 1, 2, . . ., n − 1, and t ⩾ −h, there holds

ψid(Xi, t) ≠ 0, i = 1, 2, . . . , n − 1.

Therefore, in this case the problem becomes the one of finding, under Assumption C2, a control u to
stabilize system (103)–(105).
Once again, let us start with giving an extension of Theorem 1.

## [86] `scis_2024_chained1` (PDF p.24, L1493)

Assumption C3. For all x ∈ ℝ, Zi ∈ ℝi2, i = 1, 2, . . ., n − 1, and t ⩾ −h, there holds

hdi(x, Zi, t) ≠ 0, i = 1, 2, . . ., n − 1.

Under the above Assumption C3, it is clear that the above system (106) is an SFS with time delays.

## [87] `scis_2024_chained2` (PDF p.3, L213)

Assumption A. For all x0, u0 ∈ ℝ, xi+1∼n ∈ ℝn−i, and t ⩾ 0, there holds

ψˆi (x0, xi+1∼n, u0, t) ≠ 0, i = 1, 2, . . ., n − 1.

Clearly, system (1) is a time-invariant one if and only if ˆϕi (·) and ψˆi (·) , i = 1, 2, . . ., n − 1, are all
time-invariant.
In the special case of

ϕˆi (x0, xi+1∼n, u0, t) = 0, ψˆi (x0, xi+1∼n, u0, t) = 1, i = 1, 2, . . ., n − 1,

the above system (1) becomes

x˙0 = u0,
x˙1 = u,
x˙2 = ρ1x1,
(4)
{x˙3 = ρ2x2,

...
x˙n = ρn−1xn−1.

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:4

Further, choosing in (4) ρi = x0, i = 1, 2, . . ., n − 1 and ρi = u0, i = 1, 2, . . . , n − 1, gives, respectively,
the following Brockett’s first chained form:

x˙0 = u0,
x˙1 = u,
x˙2 = x0x1, (5)
{
...
x˙n = x0xn−1,

and the Brockett’s second chained form:

x˙0 = u0,
x˙1 = u,
x˙2 = x1u0, (6)
{
...
x˙n = xn−1u0.

These obviously contain the Brockett’s first and second example systems proposed in [2] as special cases [2–
4].
The following result is given in [1], which reveals the nonholonomic feature of the proposed system (1).

## [88] `scis_2024_chained2` (PDF p.5, L351)

Assumption B. η0 = ˙x0 (0) ≠ −αx0 (0) = −αζ0.
Then, under the above assumption, we clearly have

c2 = (η0 + αζ0) ≠ 0.
α − β

With the help of the above Proposition 2, the following result can be immediately obtained.

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:6

## [89] `scis_2024_chained2` (PDF p.6, L387)

Assumption A′. For all ζ0, η0 ∈ ℝ, xi+1∼n ∈ ℝn−i, and t ⩾ 0, there holds

ψi′(ζ0, η0, xi+1∼n, t) ≠ 0, i = 1, 2, . . . , n − 1.

Furthermore, due to (22), the subsystem (9) can be written as

x˙1 = u,
x˙2 = x2ϕ′1(·) + ρ1 (γ1, ϑ1, t) x1ψ1′(·) ,
x˙3 = x3ϕ′2(·) + ρ2 (γ2, ϑ2, t) x2ψ2′(·) , (25)
{
...
x˙n = xnϕ′n−1(·) + ρn−1 (γn−1, ϑn−1, t) xn−1ψn′−1(·) .

It is seen from the above that, when u0 is designed as in (11), x0 (t) and ˙x0 (t) are given by (20) and
(21), respectively. Hence, in the above subsystem (25), ρi (γi, ϑi, t) is really a time-varying parameter.
Based on the above deduction, it can be clearly seen that, to realize the stabilization of system (1)
with the help of the partial controller (11) or (12), it suffices to solve the problem of stabilizing system
(25) under Assumption B.

3.2 σ-process

To stabilize system (25), let us transform the system into an almost SFS using an extended σ-process.

## [90] `scis_2024_chained2` (PDF p.8, L492)

Assumption A′′. For all ζ0, η0 ∈ ℝ, z1∼i ∈ ℝi, and t ⩾ 0, there holds

h′i(ζ0, η0, z1∼i, t) ≠ 0, i = 1, 2, . . ., n − 1.

Clearly, when ϕ′i(·) and ψi′(·) , i = 1, 2, . . ., n − 1, are state-dependent, unlike the simple case treated
in [15], the transformed system (27) is no longer a linear one.
With the above understanding, to realize the stabilization of system (25), it suffices to solve the
following problem.

## [91] `scis_2024_chained2` (PDF p.11, L713)

Assumption C. There exists a series of positive functions ρψi (t) , i = 1, 2, . . ., n − 1, satisfying

ψn′−i(ζ0, η0, z1∼i, t) zi+1 ⩽ 1 ρψi (t) ‖z1∼n‖ , t ⩾ 0, i = 1, 2, . . ., n − 1.
|| || |ϑn−i|

When a feedback stabilizing controller u = u (z1∼n, t) for SFS (54) is found, the closed-loop system
can be represented in the form of ˙x = f (x, t) with

g1′(·) + h′1(·) z2
g2′(·) + h′2(·) z3
f (x, t) = ... , x = z1∼n. (58)

gn′−1(·) + h′n−1(·) zn
u (z1∼n, t)

When the same feedback stabilizing controller u = u (z1∼n, t) is applied to system (27), the closed-loop
system can be represented in the form of (38) with f (x, t) being given by (58) and

T
∆f (x, t) = ∆f1T(·) ∆f2 T(·) · · · ∆fn T−1(·) 0 . (59)
[ ]

Under Assumption C, we have, using the expression of ω (t) in (19), the following relations:

|∆fi (·)| ⩽ |ϑn−iω| ψn′−i(·) zi+1

⩽ c1 ρψi|| (t) e−(α−β)t ‖||z1∼n‖ , i = 1, 2, . . ., n − 1.
||||c2||||

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:12

Therefore,

‖∆f (·)‖ ⩽ c1 ‖ρψ (t)‖ e−(α−β)t ‖z1∼n‖ , (60)
||||c2||||
where
T
ρψ (t) = [ρψ1 (t) ρψ2 (t) · · · ρψ,n−1 (t)] . (61)

This implies that, in view of c1 ≠ 0, inequality (42) is satisfied with

ρ∆ (t) = ‖ρψ (t)‖ e−(α−β)t. (62)

With the above analysis, the following result can be immediately obtained by using Corollary 1.

## [92] `tcyb_2023_robustdelay` (PDF p.3, L355)

Assumption A0: detB˜(X, Y, Z, t) ≠ 0, or ∞, for all X ∈
ℝκ, Y ∈ ℝςκ, Z ∈ ℝrν, and t ≥ 0, where

η
κ = ∑μiri.
i=1

By our notations, the above FAS (2) can be also written
more compactly as

xk(μk)|k=1∼η = f˜(xk(0∼μk−1)|k=1∼η, ζX, ζu, t)

+ B˜(xk(0∼μk−1)|k=1∼η, ζX, ζu, t)u (6)

where

⎡f˜1(xk(0∼μk−1)|k=1∼η, ζX, ζu, t)⎤

f˜2(xk(0∼μk−1)|k=1∼η, ζX, ζu, t)
f˜(·) = , f˜i ∈ ℝri.
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
f˜η(xk(0∼μk−1)|k=1∼η, ζX, ζu, t)

Clearly, a special case of the above general FAS (2) or (6)
is the following single-order one:

x(n) = f(x(0∼n−1), ζx, ζu, t)

+ B(x(0∼n−1), ζx, ζu, t)u (7)

where ζu is defined in (5), and the delay term ζx is defined as
x(0∼n−1)(t − τx1(t))
⎡x(0∼n−1)(t − τx2(t))⎤
ζx = (8)
⎢⎢⎢⎣ ... ⎥⎥⎥⎦
x(0∼n−1) t − τxς(t)
( )
and Assumption A0 becomes the following assumption.

## [93] `tcyb_2023_robustdelay` (PDF p.3, L393)

Assumption B0: det B(X, Y, Z, t) ≠ 0, or ∞, for all X ∈
ℝnr, Y ∈ ℝςnr, Z ∈ ℝrν, and t ≥ 0.
When the time-delay terms are not present, the above single-
order FAS (7) forms the basic part of the system models
involved in the problems of robust control, adaptive control,
and disturbance rejection treated in [30]–[33], while the mul-
tiorder FAS (6) forms the basic part of the system models
involved in the problems of optimal control, PID control,
and model reference tracking control treated in [35] and [36].
When the time-delay terms are present, the control of these
FAS models is treated in [40] and [41].

## [94] `tcyb_2023_robustdelay` (PDF p.4, L480)

Assumption A1: The subsystem (10) is GUA stable at the
origin.
Furthermore, the following full-actuation assumption is also
imposed.

## [95] `tcyb_2023_robustdelay` (PDF p.4, L484)

Assumption A2: detB˜(X, Y, Z, zk(0∼γk−1)|k=1∼ξ, ζZ, t) ≠ 0
or ∞, for all X ∈ ℝκ, Y ∈ ℝςκ, Z ∈ ℝrν, t ≥ 0, and
arbitrary ζZ and zk(0∼γk−1)|k=1∼ξ, with zk(0∼γk−1)|k=1∼ξ being
the solution to the system (10).
According to [34] and [40], under Assumption A2, if in
addition, the whole type I system (9)-(10) cannot be further

converted into another type I system in which the fully actu-
ated subsystem is of a higher order than that of the FAS (9),
then the FAS in (9) represents the controllable subsystem,
while (10) represents the uncontrollable subsystem, and the
variables zk(t), k = 1, 2, . . . , ξ, are called the uncontrollable
variables. Furthermore, the whole system (9)-(10) is called sta-
bilizable in a certain sense if the uncontrollable subsystem (10)
is stable in the same sense. Please note that, in certain cases,
a type I system may be still completely controllable, that is,
it can be still further converted into an FAS.
When η = 1, the above system (9)–(10) obviously reduces
to the following:

x(n) = f(x(0∼n−1), ζx, ζu, z(0∼m−1), ζz, t)

+ B(x(0∼n−1), ζx, ζu, z(0∼m−1), ζz, t)u (12)

z(m) = g(z(0∼m−1), ζz, t) (13)

where n and m are two positive integers, ζx and ζu are given
by (8) and (5), respectively, and
z(0∼m−1)(t − τz1(t))
⎡ z(0∼m−1)(t − τz2(t)) ⎤
ζz = . (14)
⎢⎢⎢⎣ ... ⎥⎥⎥⎦
z(0∼m−1) t − τzγ (t)
( )
In this circumstance, Assumptions A1 and A2, respectively,
become the following assumptions.

## [96] `tcyb_2023_robustdelay` (PDF p.4, L520)

Assumption B1: The system (13) is GUA stable at the
origin.

## [97] `tcyb_2023_robustdelay` (PDF p.4, L522)

Assumption B2: det B(X, Y, Z, z(0∼m−1), ζz, t) ≠ 0 for all
X ∈ ℝnr, Y ∈ ℝςnr, Z ∈ ℝrν, t ≥ 0, and arbitrary ζz and
z(0∼m−1), with z(0∼m−1) being the solution to the system (13).
When Assumption A2 is met, we can design the following
controller for the type I system (9)-(10) based on only the
FAS (9) as follows (see [34], [40]):

u =
⎧−B˜−1(xk(0∼μk−1)|k=1∼η, ζX, ζu, zk(0∼γk−1)|k=1∼ξ, ζZ, t)u′
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨u′ =
f˜(xk(0∼μk−1)|k=1∼η, ζX, ζu, zk(0∼γk−1)|k=1∼ξ, ζZ, t)+ u∗
(15)
u∗1
⎡u∗⎤
u∗ = 2 , u∗k = [Ak]0∼μk−1xk(0∼μk−1)
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ ⎢⎢⎢⎣ ... ⎥⎥⎥⎦
u∗η

and the following closed-loop system is obtained:

xk(μk) + [Ak]0∼μk−1xk(0∼μk−1) = 0, k = 1, 2, . . . , η
{z(γkk)|k=1∼ξ = g(zk(0∼γk−1)|k=1∼ξ, ζZ, t) (16)

which is clearly GUA stable if the coefficient matrices
[Ak]0∼μk−1, k = 1, 2, . . . , η, are so chosen that the linear
systems in (16) are asymptotically stable. However, this con-
troller (15) may not work when the FAS (9) is subject to
uncertainties, since in this case the obtained first subsystem in
the closed-loop system (16) is no longer an independent lin-
ear one, but may be affected by z(0∼γk−1). This gives rise to
k

the robust stabilization problem to be formulated in the next
section.

## [98] `tcyb_2023_robustdelay` (PDF p.5, L606)

Assumption A3: There exist two sets of non-negative func-
tions ˜ρi(·) and ˜σi(·), i = 1, 2, . . . , η, such that each of the
nonlinear uncertainty Δf˜i(·) ∈ ℝri satisfies

Δf˜i(·) ≤ ˜ρi(·) xi(0∼μi−1)
‖‖‖ ‖‖‖ ‖‖‖ ‖‖‖
+ ˜σi(·)κi zk(0∼γk−1)|k=1∼ξ ) (19)
(‖‖‖ ‖‖‖
i = 1, 2, . . . , η

where κi(·), i = 1, 2, . . . , η, are a set of properly chosen K∞
functions.

The nonlinear function
h˜1(·)
⎡ ⎤
h˜2(·) ri
h˜(·) = , ˜hi ∈ ℝ (20)
⎢⎢⎢⎣ ... ⎥⎥⎥⎦
h˜η(·)
in (17) is required to satisfy the following assumption.

## [99] `tcyb_2023_robustdelay` (PDF p.5, L627)

Assumption A4: h˜i(zk(0∼γk−1)|k=1∼ξ), i = 1, 2, . . . , η, are a
series of K∞-bounded functions.
Based on the above description, the main problem to be
solved in this article can be described as follows.

## [100] `tcyb_2023_robustdelay` (PDF p.5, L648)

Assumption B3: There exist two non-negative functions
ρ(·) and σ(·), such that

‖Δf(·)‖ ≤ ρ(·) x(0∼n−1) + σ(·)κ z(0∼m−1) )
‖‖‖ ‖‖‖ (‖‖‖ ‖‖‖
where κ(·) is a K∞ function.

## [101] `tcyb_2023_robustdelay` (PDF p.5, L654)

Assumption B4: h(z(0∼m−1)) is a K∞-bounded function.
Furthermore, Problem 1 reduces to the following one.

## [102] `tcyb_2023_robustdelay` (PDF p.8, L1017)

Assumption B3′: There exist two non-negative functions
ρ(x(0∼n−1), ζx, ζu, t) and σ(x(0∼n−1), ζx, ζu, t) such that the
nonlinear uncertainty Δf(·) ∈ ℝr satisfies

‖Δf(·)‖ ≤ ρ(x(0∼n−1), ζx, ζu, t x(0∼n−1)
)‖‖‖ ‖‖‖
+ σ(x(0∼n−1), ζx, ζu, t)κ z(0∼m−1) ) (51)
(‖‖‖ ‖‖‖
where κ(·) is a K∞ function.

## [103] `tcyb_2023_robustdelay` (PDF p.9, L1074)

Assumption B5: The following condition:

ΔB(·)B−1(·) ≤ c < 1 (55)
‖‖‖ ‖‖‖
holds for all the variables x(0∼n−1), ζx, ζu, z(0∼m−1), ζz
and t ≥ 0.

## [104] `tcyb_2023_robustdelay` (PDF p.9, L1080)

Assumption B6: There exist two non-negative functions
ρb(·) and σb(·), such that

‖ΔB(·)‖ ≤ ρb(·) x(0∼n−1) + σb(·)κb z(0∼m−1) )
‖‖‖ ‖‖‖ (‖‖‖ ‖‖‖
where κb(·) is a K∞ function.
Still, as in Section V-A, let the controller be in the form of
u = −B−1(·)(f(·) + u∗)
⎧
⎨u∗ = (A0∼n−1 + 1ε 2 1 ϑPTL)x(0∼n−1). (56)
σmin(PL)
⎩
Then the closed-loop system is

x(n) = −(A0∼n−1 + 1 1 ϑPLT)x(0∼n−1)
ε σmin2(PL)

+ h(z0∼m−1)+ Δf(·) + Δfb(·) (57)

where

Δfb(·) = −ΔB(·)B−1(·)(f(·) + A0∼n−1x(0∼n−1))

− 1 1 ϑΔB(·)B−1(·)PTLx(0∼n−1). (58)
ε σmin2(PL)
Thus, it can be shown that

‖Δfb(·)‖ ≤ B−1(·)(f(·) + A0∼n−1x(0∼n−1)
‖‖‖ )‖‖
× (ρb(·) z(0∼m−1) + σb(·)κb ‖z(0∼m−1) ))
‖‖‖ ‖‖‖ (‖‖‖ ‖‖‖
+ c 1 ϑ PTx(0∼n−1) . (59)
ε σmin2(PL) ‖‖‖ L ‖‖‖

Now, let σ(ˆ·) be a positive scalar function, and
κ(‖z(0∼m−1)‖) be a K∞-function satisfying
ˆ
B−1(·)(f(·) + A0∼n−1x(0∼n−1)
‖‖‖ )‖‖
× σb(·)κb z(0∼m−1) )+ σ(·)κ‖ z(0∼m−1) )
(‖‖‖ ‖‖‖ (‖‖‖ ‖‖‖
≤ ˆσ(·)κ z(0∼m−1) ) (60)
ˆ(‖‖‖ ‖‖‖

and define

ρ(ˆ·) = ρ(·) + B−1(·)(f(·) + A0∼n−1x(0∼n−1) ρb(·). (61)
‖‖‖ )‖‖
Then, as a generalization to Lemma 5, we have the following‖
lemma.

## [105] `tcyb_2023_robustdelay` (PDF p.9, L1164)

Assumption B3′′: There exists a non-negative function
ρ(x(0∼n−1), ζx, ζu, t) such that

‖Δf(·)‖ ≤ ρ(x(0∼n−1), ζx, ζu, t x(0∼n−1) . (64)
)‖‖‖ ‖‖‖
As a direct corollary of Theorem 3, the following result
holds.

## [106] `tcyb_2023_subfas` (PDF p.7, L902)

Assumption 1: The matrix B(·) in the single-order affine
sub-FAS (18) has relations only with x1(0∼n−1)(t−σj(t) )|j=1∼γ ,
that is

B(Tx(0∼n−1) t − σj(t) |j=1∼γ , t)
( )
= B(T1x1(0∼n−1) t − σj(t) |j=1∼γ , t)
( )
where T1 ∈ ℝm1×γ nr1 is a structural distribution matrix.
The above assumption is not strict because it can be always
satisfied by adjusting the order of the scalar equations in
system (18). In this case, under the feasibility condition

X1(t) ≜ T1x(0∼n−1) t − σj(t) |j=1∼γ ∈ 𝔽, t ≥ 0 (37)
( )

we can construct the following decoupling controller for the
single-order affine sub-FAS (18):

u(t) = −B−1 Tx(0∼n−1) t − σj(t) |j=1∼γ , t u′(t)
⎧u′(t) = f x(0∼(n−1) t − τ(j(t) |j=1∼)ζ, t + u∗)(t)
⎪⎪⎪⎪⎨ (u∗(t) ( ) ) (38)
u∗(t) = [ 1∗ ]
u2(t)
⎪⎪⎪⎪⎩u∗i(t) = Ai,0∼n−1xi(0∼n−1)(t), i = 1, 2.

The effect of this controller is clearly given as follows.

## [107] `tcyb_2023_subfas` (PDF p.9, L1062)

Assumption 2: The matrix B(·) in the sub-FAS (25) takes
the following form:

B(·) = B(Txk(0∼μk−1) t − σj(t) |k=1∼q1, j=1∼γ , t).
( )
Eventually, the feasible set becomes

𝔽 = X | ϕ0(X, t)ϕ∞(X, t) ≠ 0, X ∈ ℝM, t ≥ 0
{ }
with M ≤ γ κ1, and the feasibility condition can be
expressed as

Txk(0∼μk−1) t − σj(t) |k=1∼q1, j=1∼γ ∈ 𝔽. (46)
( )
With the above preparation, we can now design a controller
for the multiorder sub-FAS (25) in the following form:
u =
⎧−B−1(Txk(0∼μk−1) t − σj(t) |k=1∼q1, j=1∼γ , t)u′(t)
( )
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨u′ = f(xk(0∼μk−1) t − τj(t) |k=1∼η, j=1∼ζ, t)+ u∗(t)
( )
u∗1 (47)
⎡u∗⎤
u∗ = 2 , u∗i = Ψixk(0∼μk−1)(t)|k=qi−1+1∼qi.
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ ⎢⎢⎢⎣ ... ⎥⎥⎥⎦
u∗l
The conditions and variables as well as the effect of the
controller (47) are given in the following theorem.

## [108] `tcyb_2024_overview` (PDF p.7, L826)

Assumption A1 There exists a simply connected set Ω1 ⊂
ℝ2m, which contains the origin at least as a boundary point,
such that the second equation in (39) has a solution with
respect to x on Ω1, i.e.,

x = h (y,y, t ˙) . (40)

An extremely special form of the above system is clearly the
following:
{ ˙x = u (41)
y˙ = g (x, y, t) .

## [109] `tcyb_2024_overview` (PDF p.7, L847)

Assumption A2 There exists a simply connected set U1 ⊂
ℝ2m+n, which contains the origin at least as a boundary point,
such that the last equation in (42) has a solution with respect
to x2 on U1, that is,

x2 = h (x1, x3,x ˙3, t) . (43)

Clearly, a special form of system (42) is the following:

x˙1 = u1
{ x˙2 = u2 (44)
x˙3 = g (x1∼3, t) ,
which contains the Brockett’s second example ([33], [34]) as
a special case.
General effective ways have been proposed in [32] to
convert the above two types of UASs, together with another
two second-order types, Type III and IV, into global FASs or
sub-FASs. Furthermore, some guideline is also provided in [2]
to convert a general dynamical system into a FAS.

## [110] `book_2026_volume1` (PDF p.62, L41)

Assumption 1.1 (A, B) is controllable.

## [111] `book_2026_volume1` (PDF p.62, L41)

Assumption 1.2 rank B = r.
When a controller for system (1.10) is chosen as
u = K x,
(1.11)
42                                                                            1 Introduction
the closed-loop system is obtained as
ẋ = (A + B K ) x.                     (1.12)
The purpose of this subsection is to present solutions to the following generalized
ESA problem.

## [112] `book_2026_volume1` (PDF p.76, L56)

Assumption 2.1 det B (X, t) = 0 or .∞, .∀X ∈ Rnr , t ≥ 0.
When the above assumption is met, we can get from (2.39) the following:
u = B −1 (x (0∼n−1) , t) x (n) − f (x (0∼n−1) , t) (2.40)
This states that, from a FAS model, the control vector can be explicitly solved. So it
is no wonder the FAS models are convenient to deal with the control problems.
When the above assumption is not met, we can get a sub-FAS which is treated in
the second volume of the book Duan (2026b).
Nonaffine FASs
The so-called single-order nonaffine FASs, first introduced in Duan (2023b, 2023c),
appear in the following form:
x (n) = f (x (0∼n−1) , t) + g(x (0∼n−1) , u, t),                            (2.41)
where x, u and f (x (0∼n−1) , t) are as stated above, while g(x (0∼n−1) , u, t) ∈ Rr is a
piece-wise continuous vector function.
2.2 Single-Order FASs                                                                57
The above nonaffine system (2.41) is called a global FAS due to the following
assumption.

## [113] `book_2026_volume1` (PDF p.77, L57)

Assumption 2.2 The following mapping
ũ = g (X, u, t)
(2.42)
forms a homeomorphism from u to ũ for all X ∈ Rnr and t ≥ 0.
Again, when the above assumption is not met, we can obtain a nonaffine sub-FAS
which is treated in the second volume of the book Duan (2026b).
Traditional treatments
In traditional context of related research, for the affine FAS (2.39), due to Assumption
2.1, the following control transformation is often applied:
û = f (x (0∼n−1) , t) + B(x (0∼n−1) , t)u.
(2.43)
Parallelly, for the nonaffine FAS (2.41), due to Assumption 2.2, the following control
transformation is often applied:
û = f (x (0∼n−1) , t) + g(x (0∼n−1) , u, t).
(2.44)
Based on the above two control transformations, both the affine FAS (2.39) and the
nonaffine FAS (2.41) are reduced to the following linear system:
x (n) = û.

## [114] `book_2026_volume1` (PDF p.81, L61)

Assumption 2.3 det B (X, t) = 0 or .∞ for X ∈ Rκ0 , and t ≥ 0.
If we denote
⎡                             ⎤
−1)
f 1 xk(0∼μk |k=1∼η , t
⎢                                     ⎥
⎢      (0∼μ −1)                       ⎥
⎢ f 2 xk k |k=1∼η , t                 ⎥
f xk(0∼μk −1) |k=1∼η , t = ⎢
⎢             ..
⎥,
⎥
⎢              .                      ⎥
⎣                                     ⎦
(0∼μk −1)
f η xk         |k=1∼η , t
then system (2.57) can be compactly written as
x (μk ) |k=1∼η = f xk(0∼μk −1) |k=1∼η , t + B (·) u.
k                                                                   (2.59)
Clearly, in the case of η = 1, the above FAS model (2.57), or ( 2.59) reduces to the
form of (2.39).
When the above Assumption 2.3 is met, we can obtain from (2.59) the following:
u = B −1 xk(0∼μk −1) |k=1∼η , t
xk(μk ) |k=1∼η − f xk(0∼μk −1) |k=1∼η , t      (2.60)
Again, this states that, from a FAS model, the control vector can be explicitly solved.
Such models from which the control vector can be explicitly solved are no doubt
convenient to deal with control problems. This will be sufficiently testified in the
next chapter.
When nonlinear uncertainties, unknown parameters and disturbances are added
to these basic FASs, problems of robust and adaptive control as well as disturbance
rejection control rise, and have been investigated in Duan (2021c, 2021d, 2021e,
2021f) (see also Chaps. 4 and 5).
Nonaffine multi-order FASs
A nonaffine multi-order FAS, first introduced in Duan (2023b, 2023c), is in the
following form:
⎡                                    ⎤
⎡         ⎤                    −1)

## [115] `book_2026_volume1` (PDF p.82, L62)

Assumption 2.4 The following mapping
ũ = g (X, u, t) ,
(2.62)
forms a homeomorphism from u to ũ for all X ∈ Rκ0 and t ≥ 0.
Similarly, the nonaffine FAS (2.61) can also be compactly written as
−1)                              −1)
kx (μk ) |k=1∼η = f xk(0∼μk          |k=1∼η , t + g xk(0∼μk           |k=1∼η , u, t (2.63)
Clearly, in the case of η = 1, the above FAS model (2.61) or (2.63) reduces to the
form of (2.41).
Let us also point out, when the above Assumption 2.4 is met, we can also obtain
from the nonaffine FAS (2.63) the explicit expression of the control vector. In general,
we can conclude that a global FAS can be expressed as
h xk(0∼μk ) |k=1∼η , t = u,                                   (2.64)
2.4 Linear Time-Invariant FASs                                                       63
where h (·) is some proper vector function of the same size as u.

## [116] `book_2026_volume1` (PDF p.97, L77)

Assumption 2.5 The LTV system (2.109) is lexicography-fixedly controllable on
t ∈ [t0 , ∞).

## [117] `book_2026_volume1` (PDF p.97, L77)

Assumption 2.6 For .∀t ≥ t0 , all elements of A (t) and B (t) are at least n-times
continuously differentiable.

## [118] `book_2026_volume1` (PDF p.99, L79)

Assumption 2.7 The LTV system (2.109) is uniformly controllable but not
lexicography-fixedly controllable on t ∈ [t0 , ∞) and the maximum values μi max ,
i = 1, 2, . . . , r, of all controllability indices are known.
The following augmented system instead of (2.109) is considered
x̃˙ = Ã (t) x̃ + B̃ (t) u,               (2.122)
where
A (t) 0n×n e                      B (t)
Ã (t) =                        , B̃ (t) =                .
Ae1 (t) Ae2 (t)                    Be (t)
T
with x̃ = x T xeT ∈ Rn+n e being the extended state vector, Ae1 (t) ∈ Rn e ×n ,
n ×n e
A e2 (t) ∈ R e     and Be (t) ∈ Rn e ×r being the auxiliary system matrices to be deter-
mined. Regarding the augmented system, Valasek and Olgac provide the following
result (Valášek & Olgac, 1999).

## [119] `book_2026_volume1` (PDF p.147, L128)

Assumption 4.1 det B (X, ζ, t) = 0 or .∞, ∀X ∈ Rnr , ζ ∈ R p , and t ≥ 0.
From its appearance, the above Assumption 4.1 seems to be strict. While as a
matter of fact, the above FAS (4.1) represents a quite general model for “completely
controllable” systems, and can either be obtained through physical modeling, or
through conversion from other types of models (Duan, 2020a, 2020b, 2021a, 2021b,
2021c, 2021d, 2021e).
As a demonstration, let us restate that the following uncertain strict feedback
system (SFS) can be converted into the form of (4.1):
⎧
⎪ ẋ1 = f 1 (x1 , ζ, t) + f 1 (x1 , ζ, t) + G 1 x2
⎪
⎪
⎪
⎨ ẋ2 = f 2 (x1 , x2 , ζ, t) + f 2 (x1 , x2 , ζ, t) + G 2 x3
⎪
.                                                                           (4.2)
⎪      .
⎪
⎪
⎪
⎪ ẋ n−1 = f n−1 (x1∼n−1 , ζ, t) + f n−1 (x1∼n−1 , ζ, t) + G n−1 xn
⎩
ẋn = f n (x1∼n , ζ, t) + f n (x1∼n , ζ, t) + G n u,
where xi ∈ Rr , i = 1, 2, . . . , n, are the state vectors, u ∈ Rr is the control input,
f i (x 1∼i , ζ, t) and. f i (x1∼i , ζ, t) ∈ Rr ,.i = 1, 2, . . . , n, are sufficiently smooth vec-
tor functions, and G i ∈ Rr×r , i = 1, 2, . . . , n, are a set of nonsingular matrices.
According to Theorem 3.1 or 3.6 in Duan (2021b), we have the following simplified
result.

## [120] `book_2026_volume1` (PDF p.157, L138)

Assumption 4.2 The matrix pair (A, B) is stabilizable.

## [121] `book_2026_volume1` (PDF p.157, L138)

Assumption 4.3 The matrix pair ( Ã, C̃) is detectable, where
A   Ew
Ã =              , C̃ = C y     0 .
0   S
The following lemma is a simplified version of Theorem 2.4.1 in Saberi et al.
(2012, p. 25) [see also Theorem 2.6 in Duan (2015, p. 51)], which gives a basic
output regulation result for the linear system (4.47).

## [122] `book_2026_volume1` (PDF p.159, L140)

Assumption 4.4 The matrix pair (                  E , C E ) defined by (4.59) is detectable.
Let us introduce the following control law for FAS (4.45):
⎧
⎪
⎪ x̂˙ (0∼n−1)                (00∼n−1 )     Bc E          x̂ (0∼n−1)   Bc
⎪
⎪                =                                                  +    v
⎪
⎪
⎪
⎪ d̂˙ (0∼k−1)                  0          (S0∼k−1 )      d̂ (0∼k−1)   0
⎪
⎨                              Lx
+     Cm x̂ (0∼n−1) − ym                                      (4.60)
⎪                              Ld
⎪
⎪                                     x̂ (0∼n−1)
⎪
⎪
⎪
⎪ v = −K 0∼n−1 + K 0∼n−1
⎪
⎪                                     d̂ (0∼k−1)
⎩       −1
u = −B (ym , ζ, t) ( f (ym , ζ, t) − v) ,
where                             ⎧                     n −1
⎪
⎪ K 0∼n−1 = −Z⎡   1 F1 V       (F⎤1 , Z 1 )
⎪
⎪
⎪
⎨                        Z   1
⎢ Z 1 F1 ⎥
⎢              ⎥                            (4.61)
⎪
⎪ V (F1 , Z 1 ) = ⎢       ..     ⎥,
⎪
⎪                 ⎣        .     ⎦
⎪
⎩                            n−1
Z 1 F1

## [123] `book_2026_volume1` (PDF p.181, L162)

Assumption 5.1 det L (X ) = 0 or .∞, ∀X ∈ Rnr .
Correspondingly, for some nonlinear systems subject to uncertainties, often their
FAS models can be also derived, but in the following form:
x (n) = f (x (0∼n−1) ) +       f (x (0∼n−1) ) + L(x (0∼n−1) )u,          (5.2)
where f (x (0∼n−1) ) ∈ Rr is the nonlinear uncertainty of the system. The derivation
of the above uncertain FAS model may be of two folds: one is through physical
modeling, see, e g., Example 2 in Duan (2021b), when the disturbances di , i =
1, 2, 3, are taken as uncertainties; the other is through model conversion.
In this section, let us consider the control of systems represented by the single-
order FAS model (5.2) under the following condition:

## [124] `book_2026_volume1` (PDF p.181, L162)

Assumption 5.2 There exists a non-negative continuous scalar function
ρ(x (0∼n−1) ) such that the nonlinear uncertainty f (x (0∼n−1) ) ∈ Rr satisfies
f (x (0∼n−1) )     ρ(x (0∼n−1) ).
We point out that, in this section, the following particular notation is also used:
⎡              ⎤
0 0       1
In = ⎣ 0 .
◦
.    0 ⎦ ∈ Rn×n .
1 0       0
5.1 Robust Control                                                                             163
Preliminaries
In order to give a control law for the above high-order system (5.2) with dynamic
uncertainties, let us give two preliminary results.

## [125] `book_2026_volume1` (PDF p.196, L177)

Assumption 5.3 For two non-negative real numbers δ0 and δ1 , there hold
θ (t) −θ0 (t) ≤ δ0 , θ̇ (t) −θ̇0 (t) ≤ δ1 , ∀t ≥ 0.

## [126] `book_2026_volume1` (PDF p.202, L183)

Assumption 5.4 There exists a non-negative continuous scalar function
ρ(x (0∼n−1) ), such that
f (x (0∼n−1) ) ≤ ρ(x (0∼n−1) ) PLT x (0∼n−1) .
Under Assumption 5.1 and the above Assumption 5.4, we will present a modified
adaptation scheme for the case of constant.θ , which has the following two advantages:
1. the adaptation scheme does not depend on a pre-estimate of the parameter θ ;
2. the robust adaptive controller guarantees that the state x (0∼n−1) converges to
zero.
In the case that the parameter vector θ is constant, the modification of our robust
adaptive controller consists of the following two aspects:
• replacing the robustness part in the robust adaptive controller (5.53)–(5.56) by
u =
r      ρ(x (0∼n−1) )PLT ( A0∼n−1 )x (0∼n−1) ,          (5.74)
ε
where ε is an arbitrarily selected positive real number not greater than 1, and
• replacing the adaptation part in the robust adaptive controller (5.53)–(5.56) by the
following:
θ̂˙ = H (x (0∼n−1) )PLT ( A0∼n−1 )x (0∼n−1)
(5.75)
u a = H T (x (0∼n−1) )θ̂ .
As a result, we have the following theorem.
184                                                           5 Robust and Adaptive Control

## [127] `book_2026_volume1` (PDF p.218, L200)

Assumption 6.1 For arbitrary xi ∈ Rr , i = 1, 2, . . . , n, and ζ ∈ Rm , there holds
det G i (x1∼i , ζ, t)   0, ∀t ≥ 0.                         (6.2)
In certain high-dimensional cases, the above Assumption 6.1 may be difficult to
verify. It is recommended that symbolic computation techniques may be considered
to help in such cases.
More concretely, the. f and. B terms in FASs (2.39) or (2.57) are finally obtained by
iterative formulas using. f i (x1∼i ) and G i (x1∼i ),.i = 1, 2, . . . , n. Moreover, a discrete-
time version of similar results can be found in Duan (2022f), and generalization of
the results to SFSs with time-varying delays can be found in Duan (2023b, 2023c).

## [128] `book_2026_volume1` (PDF p.223, L205)

Assumption 6.2 For arbitrary xi ∈ Rr , i = 1, 2, . . . , n, and ζ ∈ Rm , there holds
(0∼1)
det G i (x1∼i   , ζ, t)      0, ∀t ≥ 0.
6.3.1 Recursive Solution
In parallel to the first-order case, we have the following conclusion.

## [129] `book_2026_volume1` (PDF p.226, L208)

Assumption 6.3 For all xk ∈ Rr , k = 1, 2, . . . , n, and ζ ∈ Rm , there holds
det G k (xi(0∼m i −1) |i=1∼k , ζ, t)   0, ∀t ≥ 0.
For the sake of convenience, we further introduce the following notations:
pi = m 1 + m 2 + · · · + m i , i = 1, 2, . . . , n
(6.34)
p = pn .
Then, parallel to the first-order and second-order cases, we have the following
conclusion.

## [130] `book_2026_volume1` (PDF p.246, L228)

Assumption 7.1 The gain matrices G i , i = 1, 2, . . . , n, are all of full-row rank,
i e., rank(G i ) = ri , i = 1, 2, . . . , n.

## [131] `book_2026_volume1` (PDF p.246, L228)

Assumption 7.1 The gain matrices G i , i = 1, 2, . . . , n, are all of full-row rank,
i e., rank(G i ) = ri , i = 1, 2, . . . , n.

## [132] `book_2026_volume1` (PDF p.251, L233)

Assumption 7.2 For any x1∼i ∈ Rπi , the matrix function G i (x1∼i ) is of full-row
rank, i e., rankG i (x1∼i ) = ri , i = 1, 2, . . . , n.
It follows from Assumption 7.2 that there exist sufficiently smooth functions
Q i (·) : Rπi → Rri+1 ×ri+1 and Ḡ i (·) : Rπi → Rri ×ri such that
G i (·)Q i (·) = Ḡ i (·) 0 ,
where Q i (·) and Ḡ i (·) are nonsingular for any x1∼i ∈ Rπi Define a homeomorphism
⎡ ⎤         ⎡ ⎤
x1             x̄1
⎢ x2 ⎥         ⎢ x̄2 ⎥
⎢ ⎥            ⎢ ⎥
x = ⎢ . ⎥ : → x̄ = ⎢ . ⎥
⎣ .. ⎦         ⎣ .. ⎦
xn                  x̄n
as follows:
234                                             7 Strict Feedback Systems with Increasing Dimensions
⎧
⎪
⎪ x̄1 = x1
⎪ x̄ = Q −1 (x )x
⎪
⎪
⎨ 2         1     1 2
−1
x̄ 3 =  Q 2  (x 1 , x2 )x3                                         (7.29)
⎪
⎪      ..
⎪
⎪       .
⎪
⎩
x̄n = Q −1n−1 (x 1 , x 2 , · · · , x n−1 )x n .
Then the inverse mapping from x̄ to x can be written as
⎧
⎪ x1 = x̄1
⎪
⎪
⎪
⎪ x2 = Q 1 (x̄1 )x̄2 Q̄ 1 (x̄1 )x̄2

## [133] `book_2026_volume1` (PDF p.256, L238)

Assumption 7.3 For any X i ∈ R3r1 +···+3ri−1 and Yi ∈ R2ri , the matrix function
G i (X i , Yi ) is of full-row rank, i e., rankG i (X i , Yi ) = ri , i = 1, 2, . . . , n.
It follows from Assumption 7.3 that there exist differentiable functions Q i (·) :
R3r1 +···+3ri−1 +2ri → Rri+1 ×ri+1 and Ḡ i (·) : R3r1 +···+3ri−1 +2ri → Rri ×ri such that
G i (·)Q i (·) = Ḡ i (·) 0 ,
where Q i (·) and Ḡ i (·) are both of full rank. Define the mapping from
⎡ ⎤         ⎡ ⎤
x1             x̄1
⎢ x2 ⎥         ⎢ x̄2 ⎥
⎢ ⎥            ⎢ ⎥
x = ⎢ . ⎥ : → x̄ = ⎢ . ⎥
⎣ .. ⎦         ⎣ .. ⎦
xn                 x̄n
7.2 Second-Order SFSs with Increasing Dimensions                                            239
as follows:                         ⎧
⎪
⎪ x̄1 = x1
⎪
⎪               (0∼1)
⎪          −1
⎪ 2 = Q 1 x1
x̄                    x2
⎪
⎪
⎨
x̄3 = Q −1
2   x1(0∼1) , x2(0∼1) x3                    (7.44)
⎪
⎪     ..
⎪
⎪
⎪
⎪      .
⎪
⎪
⎩ x̄n = Q −1     (0∼1)
xn .

## [134] `book_2026_volume1` (PDF p.263, L245)

Assumption 7.4 For any X i ∈ R i with i =         (m p + 1)r p and Yi ∈ Rm i ri , the
p=1
gain matrix function G i (X i , Yi ) is of full-row rank, i e., rankG i (X i , Yi ) = ri , i =
1, 2, . . . , n.
It follows from Assumption 7.4 that there exist sufficiently smooth functions. Q i (·)
and Ḡ i (·) for i = 1, 2, . . . , n, such that
G i (·)Q i (·) = Ḡ i (·) 0 ,
where Q i (·) and Ḡ i (·) are nonsingular. Then we define
T
x̄ = x̄1T x̄2T   · · · x̄nT
as follows:
246                                         7 Strict Feedback Systems with Increasing Dimensions
⎧
⎪
⎪ x̄1 = x1
⎪
⎪              (0∼m 1 −1)
⎪          −1
⎪ x̄2 = Q 1 x1
⎪
⎪
x2
⎨              (0∼m 1 −1)
−1
x̄3 = Q 2 x1            , x2(0∼m 2 −1) x3                      (7.62)
⎪
⎪     ..
⎪
⎪
⎪
⎪      .
⎪
⎪
⎩ x̄n = Q −1 x (0∼m i −1)               xn .
n−1  i
i=1∼n−1
Similar to the reasoning given in Sect. 7.2 of this chapter, the inverse mapping from
x̄ to x can be written as

## [135] `book_2026_volume1` (PDF p.279, L261)

Assumption 8.1 For arbitrary xi ∈ Rr , i = 1, 2, . . . , n, ζ ∈ Rm , and t ≥ 0, there
hold
det ∂ x∂i+1 gi (x1∼i+1 , ζ, t) 0, i = 1, 2, . . . , n − 1
∂                                                               (8.2)
det ∂u   gn (x1∼n , u, ζ, t) 0.
The meaning of the above assumption lies in the following facts:
• for each i = 1, 2, . . . , n − 1, the inverse function of g i (x1∼i+1 , ζ, t) with respect
to xi+1 exists for all x1∼i ∈ Rir , ζ ∈ Rm , and t ≥ 0;
• the inverse function of g n (x1∼n , u, ζ, t) with respect to u exists for all x1∼n ∈ Rnr ,
ζ ∈ R , and t ≥ 0;
m
• for arbitrary yi ∈ Rr , i = 1, 2, . . . , n − 1, the following equations
g (x1∼i+1 , ζ, t) = yi , i = 1, 2, . . . , n − 1, t ≥ 0,
i                                                                        (8.3)
have solutions with respect to xi+1 ∈ Rr , i = 0, 1, . . . , n − 1, which can also be
represented by
x
i+1   = gi−1 (x1∼i , yi , ζ, t), i = 1, 2, . . . , n − 1;               (8.4)
• for an arbitrary yn ∈ Rr , the following equation
g (x1∼n , u, ζ, t) = yn , ∀t ≥ 0,
n                                                             (8.5)
has a solution with respect to u ∈ Rr , which can also be represented by
u = gn−1 (x1∼n , yn , ζ, t).
(8.6)
In this section, we assume that the inverse function can be explicitly obtained. In
certain high-dimensional cases, the above Assumption 8.1 may be difficult to verify.
It is recommended that symbolic computation techniques may be considered to help
in such cases.
262                                                                              8 Nonaffine Strict Feedback Systems
The purpose of this section is to find a homeomorphism under which the above
nonaffine SFS (8.1) is equivalently converted into a nonaffine FAS.

## [136] `book_2026_volume1` (PDF p.282, L264)

Assumption 8.1 becomes

## [137] `book_2026_volume1` (PDF p.282, L264)

Assumption 8.2 For arbitrary xi ∈ Rr , i = 1, 2, . . . , n, ζ ∈ Rm , and t ≥ 0, there
hold
det ∂ x∂i+1 gi (xi+1 , t) 0, i = 1, 2, . . . , n − 1
∂                                                            (8.16)
det ∂u   gn (u, t) 0.
Due to (8.14), we have
∂gi (xi+1 , t)         ∂gi (xi+1 , t)
ġ (x1∼i+1 , ζ, t) =
i                                   ẋi+1 +                , i = 1, 2, . . . , n − 1.
∂ xi+1                   ∂t
Setting, for i = 1, 2, . . . , n,
∂
gi (x1∼i+1 , ζ, t) = 0,
∂ x1∼i
∂
gi (x1∼i+1 , ζ, t) = 0,
∂ζ
and
∂gi (x1∼i+1 , ζ, t)   ∂gi (xi+1 , t)
=                ,
∂ xi+1             ∂ xi+1
∂gi (x1∼i+1 , ζ, t)   ∂gi (xi+1 , t)
=                ,
∂t                 ∂t
where xn+1 = u, immediately gives the following corollary.
8.1 First-Order Nonaffine SFSs                                                                                265

## [138] `book_2026_volume1` (PDF p.287, L269)

Assumption 8.3 For arbitrary xi ∈ Rr , i = 1, 2, . . . , n, ζ ∈ Rm , and .∀t ≥ 0, there
hold
(0∼1)
det ∂ x∂i+1 gi (x1∼i    , xi+1 , ζ, t) 0, i = 1, 2, . . . , n − 1
∂          (0∼1)                                                    (8.30)
det ∂u gn (x1∼n , u, ζ, t) 0.
The meaning of the above assumption lies in the following facts:
(0∼1)
• for each i = 1, 2, . . . , n − 1, the inverse function of g i (x1∼i       , xi+1 , ζ, t) with
(0∼1)
respect to xi+1 exists for all x1∼i ∈ R , ζ ∈ R , and t ≥ 0;
2ir       m
(0∼1)                                                   (0∼1)
• the inverse function of g n (x1∼n      , u, ζ, t) with respect to u exists for all x1∼n     ∈
R2nr , ζ ∈ Rm , and t ≥ 0;
• for arbitrary yi ∈ Rr , i = 1, 2, . . . , n − 1, the following equations
270                                                             8 Nonaffine Strict Feedback Systems
(0∼1)
g (x1∼i
i        , xi+1 , ζ, t) = yi , t ≥ 0,                       (8.31)
have solutions with respect to xi+1 ∈ Rr , which can also be represented by
(0∼1)
x
i+1   = gi−1 (x1∼i   , yi , ζ, t);                    (8.32)
• for an arbitrary yn ∈ Rr , the following equation
(0∼1)
g (x1∼n
n        , u, ζ, t) = yn , ∀t ≥ 0,                          (8.33)
has a solution with respect to u ∈ Rr , which can also be represented by
(0∼1)
u = gn−1 (x1∼n
, yn , ζ, t).                      (8.34)
In certain high-dimensional cases, the above Assumption 8.3 may be difficult to
verify. It is recommended that symbolic computation techniques may be considered
to help in such cases.
The purpose of this section is to find a homeomorphism under which the above
nonaffine SFS (8.29) is equivalently converted into a nonaffine FAS.

## [139] `book_2026_volume1` (PDF p.291, L273)

Assumption 8.4 For arbitrary xi ∈ Rr , i = 1, 2, . . . , n, and .∀t ≥ 0, there hold
det ∂ x∂i+1 gi (xi+1 , t)   0, i = 1, 2, . . . , n − 1
∂                                                            (8.50)
det ∂u   gn (u, t) 0.
Due to (8.48), we have
(0∼1)
ġ i (x
1∼i , xi+1 , ζ, t) = ġ i (xi+1 , t)
∂                      ∂
=          gi xi+1 , t ẋi+1 + gi xi+1 ,t , i = 1, 2, . . . , n − 1.
∂ xi+1                    ∂t
Hence, setting for i = 1, 2, . . . , n − 1,
∂         (0∼1)                      ∂
gi (x1∼i    , xi+1 , ζ, t) =        gi (xi+1 , t) = 0,
∂ x1∼i                               ∂ x1∼i
∂        (0∼1)                    ∂
gi (x1∼i    , xi+1 , ζ, t) =     gi (xi+1 ,t) = 0,
∂ζ                                ∂ζ
274                                                                             8 Nonaffine Strict Feedback Systems
and
∂        (0∼1)                     ∂
gi (x1∼i   , xi+1 , ζ, t) =        gi (xi+1 , t) ,
∂ xi+1                             ∂ xi+1
∂       (0∼1)                    ∂
gi (x1∼i   , xi+1 , ζ, t) = gi (xi+1 , t) ,
∂t                              ∂t
in Theorem 8.2 immediately gives the following corollary.

## [140] `book_2026_volume1` (PDF p.298, L280)

Assumption 8.5 For arbitrary xk ∈ Rr , k = 1, 2, . . . , n − 1, ζ ∈ Rm , and .∀t ≥ 0,
there hold
det ∂ x∂k+1 gk (xi(0∼m i −1) |i=1∼k , xk+1 , ζ, t)   0, k = 1, 2, . . . , n − 1
(8.71)
∂
det ∂u   gn (xi(0∼m i −1) |i=1∼n , u, ζ, t) 0.
and the inverse functions of g k (xi(0∼m i −1) |i=1∼k , xk+1 ,ζ, t) with respect to xk+1 and
(0∼m i −1)
g n (x i          |i=1∼n , u, ζ, t) with respect to u can be explicitly solved.
The meaning of the above assumption lies in the following facts:
• for each k = 1, 2, . . . , n − 1, the inverse function of g k (xi(0∼m i −1) |i=1∼k , xk+1 ,ζ, t)
with respect to xk+1 exists for all xi(0∼m i −1) |i=1∼k ∈ Rr pk , ζ ∈ Rm , and t ≥ 0;
• the inverse function of g n (xi(0∼m i −1) |i=1∼n , u, ζ, t) with respect to u exists for all
(0∼m i −1)
xi          |i=1∼n ∈ Rr p , ζ ∈ Rm , and t ≥ 0;
• for arbitrary yk ∈ Rr , k = 1, 2, . . . , n − 1, the following equations
g (xi(0∼m k −1) |i=1∼k , xk+1 ,ζ, t) = yk , k = 1, 2, . . . , n − 1, ∀t ≥ 0,
k                                                                                        (8.72)
8.3 Mixed-Order Nonaffine SFSs                                                                      281
have solutions with respect to xk+1 ∈ Rr , k = 1, 2, . . . , n − 1, which can also be
represented by
x
k+1   = gk−1 (xi(0∼m k −1) |i=1∼k , yk , ζ, t), k = 1, 2, . . . , n − 1;            (8.73)
• for an arbitrary yn ∈ Rr , the following equation
g (xi(0∼m i −1) |i=1∼n , u, ζ, t) = yn , ∀t ≥ 0,
n                                                                 (8.74)
has a solution with respect to u ∈ Rr , which can also be represented by
u = gn−1 (xi(0∼m i −1) |i=1∼n , yn , ζ, t).
(8.75)
In certain high-dimensional cases, the above Assumption 8.5 may be difficult to
verify. It is recommended that symbolic computation techniques may be considered
to help in such cases.

## [141] `book_2026_volume1` (PDF p.302, L284)

Assumption 8.5 becomes

## [142] `book_2026_volume1` (PDF p.302, L284)

Assumption 8.6 For arbitrary xk ∈ Rr , k = 1, 2, . . . , n, ζ ∈ Rm , and t ≥ 0, there
hold
det ∂ x∂k+1 gk (xk+1 , ζ, t) 0, k = 1, 2, . . . , n − 1
∂                                                            (8.88)
det ∂u   gn (u, ζ, t) 0.
Due to (8.86), we have
ġ (xi(0∼m i −1) |i=1∼k , xk+1 , ζ, t) = ġ k (xk+1 , ζ, t)
k
∂gk (xk+1 ,ζ, t) ẋk+1   ∂gk (xk+1 ,ζ, t)
=                        +                  ,
∂ xk+1               ∂t
k = 1, 2, . . . , n − 1.
Hence, setting, for k = 1, 2, . . . , n − 1,
8.3 Mixed-Order Nonaffine SFSs                                                                                        285
∂g k (xi(0∼m i −1) |i=1∼k , xk+1 , ζ, t)
= 0,
∂ x1∼k
and                                    ⎧
⎨ ∂gk (xi(0∼mi −1) |i=1∼k ,xk+1 ,ζ,t) = ∂gk (xk+1 ,ζ,t)
∂ xk+1                      ∂ xk+1
⎩ ∂gk (xi(0∼mi −1) |i=1∼k ,xk+1 ,ζ,t) = ∂gk (xk+1 ,ζ,t) ,
∂t                           ∂t
in Theorem 8.3 immediately gives the following corollary.

## [143] `book_2026_volume1` (PDF p.321, L304)

Assumption 9.1 det G i (x1∼i   )           0, ∀xi ∈ Rr , i = 1, 2, . . . , n.
In the event that the nonlinear uncertainties in the above second-order SFS do
not appear, it has been shown in Duan (2021b) that the model can be equivalently
converted into the form of (5.1). However, when nonlinear uncertainties do exist, in
some cases, an equivalent single FAS model in the form of (5.2) may not be able to
be derived, or in other words, the derived FAS model may be too conservative in the
sense that too much certain information has to be included into the uncertain terms
(0∼1)
f i (x1∼i   ), i = 1, 2, . . . , n, since it is sometimes hard to separate the certain part
from the uncertain terms. Therefore, in certain applications, it may be more favorable
to treat directly the set of models in (9.1), or, only convert a few of the subsystems
in (9.1) into several FAS models in the form of (5.2). After all, all the subsystems in
(9.1), as they stand, are a set of cascade fully actuated subsystems, when the xi+1 in
the i-th subsystem is looked upon as the control variable.
It is worth pointing out that the above second-order SFS (9.1) also has the following
companion form:
9.1 Uncertain High-Order SFSs                                                                         305
⎧
⎪ ẍ1 = f 1 (x1 , ẋ1 ) + f 1 (x1 , ẋ1 ) + G 1 (x1 , ẋ1 )ẋ2
⎪
⎪
⎪                (0∼1)           (0∼1)             (0∼1)
⎨ ẍ2 = f 2 (x1∼2 ) + f 2 (x1∼2 ) + G 2 (x1∼2 )ẋ3
⎪
.
.                                                                       (9.2)
⎪
⎪
⎪
⎪ ẍ     =             (0∼1)
f n−1 (x1∼n−1                (0∼1)
) + f n−1 (x1∼n−1                 (0∼1)
) + G n−1 (x1∼n−1  )ẋn
⎪
⎩    n−1
(0∼1)           (0∼1)             (0∼1)
ẍn = f n (x1∼n ) + f n (x1∼n ) + G n (x1∼n )u.
(0∼1)
As a matter of fact, the last term G i (x1∼i     )ẋi+1 in each subsystem can be further
generalized into
(0∼1)                 (0∼1)
G 0i (x 1∼i )x i+1 + G 1i (x 1∼i ) ẋ i+1 ,

## [144] `book_2026_volume1` (PDF p.322, L305)

Assumption 9.2 det G k (xi(0∼m i −1) |i=1∼k )            0, ∀xi ∈ Rr , k = 1, 2, . . . , n.
Regarding the derivation of the above uncertain mixed-order SFS (9.3), we make
the following statements:
• In the modeling of physical systems, we often use physical laws such as Lagrangian
Equations and Theorem of Linear and Angular Momentum. In such cases the
original models of the obtained subsystems are of second-order. On the other side,
there are also subsystems modeled by other physical laws, such as the well-known
Hamiltonian Theorem, and the obtained original models are of first-order. Such
operations give a mixed-order SFS (9.3), with m i , i = 1, 2, . . . , n, taking the
values of 1 or 2.
306                                                     9 High-Order Backstepping for Robust Control
• It has been pointed out above that the mixed-order SFS may be obtained from the
second-order SFS by converting equivalently some of the subsystems in (9.1) into
several FAS models in the form of (5.2). Meanwhile, some of the subsystems in
(9.1) can also be converted into several first-order equations. Both operations give
mixed-order SFSs.
Parallelly, the above mixed-order SFS (9.3) also has a companion form which
appears as follows:
⎧ (m )
⎪
⎪  x1 1 = f 1 (x1(0∼m 1 −1) ) + f 1 (x1(0∼m 1 −1) ) + G 1 (x1(0∼m 1 −1) )ẋ2
⎪
⎪
⎪
⎪
⎪  x2(m 2 ) = f 2 (xi(0∼m i −1) |i=1∼2 ) + f 2 (xi(0∼m i −1) |i=1∼2 ) + G 2 (xi(0∼m i −1) |i=1∼2 )ẋ3
⎪
⎨             ..
⎪    (m n−1 )
⎪ xn−1 = f n−1 (xi(0∼m i −1) |i=1∼n−1 )
⎪
⎪
⎪
⎪                + f n−1 (xi(0∼m i −1) |i=1∼n−1 ) + G n−1 (xi(0∼m i −1) |i=1∼n−1 )ẋn
⎪
⎪
⎩ (m n )
xn = f n (xi(0∼m i −1) |i=1∼n ) + f n (xi(0∼m i −1) |i=1∼n ) + G n (xi(0∼m i −1) |i=1∼n )u.
(9.4)

## [145] `book_2026_volume1` (PDF p.344, L328)

Assumption 10.1 gi (x1∼i   )          0, ∀xi , ẋi ∈ R, i = 1, 2, . . . , n.
Besides physical modeling, many conventional first-order SFSs can also be
converted into the above second-order form (10.1).
Clearly, a companion form of the above SFS (10.1) is the following:
⎧
⎪ ẍ1 = f 1 (x1 , ẋ1 )ϑ1 + g1 (x1 , ẋ1 )ẋ2
⎪
⎪                (0∼1)            (0∼1)
⎪ ẍ2 = f 2 (x1∼2
⎪                      )ϑ2 + g2 (x1∼2    )ẋ3
⎨
.
.                                                         (10.2)
⎪
⎪
⎪
⎪ ẍ     =             (0∼1)
f n−1 (x1∼n−1                   (0∼1)
)ϑn−1 + gn−1 (x1∼n−1   )ẋn
⎪
⎩    n−1
(0∼1)            (0∼1)
ẍn = f n (x1∼n )ϑn + gn (x1∼n )u.
10.1.2 High-Order SFSs
A straight forward generalization of the above second-order SFS (10.1) is the fol-
lowing high-order (mixed-order) strict-feedback nonlinear system with unknown
parameters:
⎧ (m )
⎪
⎪ x1 1 = f 1 (x1(0∼m 1 −1) )ϑ1 + g1 (x1(0∼m 1 −1) )x2
⎪
⎪   (m )            (0∼m i −1)
⎪
⎪ x2 2 = f 2 (xi
⎨                              | i=1∼2 )ϑ2 + g2 (xi(0∼m i −1) | i=1∼2 )x3
.                                                                          (10.3)
⎪             .
⎪
⎪   (m n−1 )

## [146] `book_2026_volume1` (PDF p.344, L328)

Assumption 10.2 gk (xi(0∼m i −1) | i=1∼k )         0, ∀xi(0∼m i −1) ∈ Rm i , k = 1, 2, . . . , n.
10.2 Backstepping for Second-Order SFSs                                                           329
In parallel to (10.2), a companion form of the above SFS (10.3) is the following:
⎧ (m )
⎪
⎪ x1 1 = f 1 (x1(0∼m 1 −1) )ϑ1 + g1 (x1(0∼m 1 −1) )ẋ2
⎪
⎪   (m 2 )        (0∼m i −1)
⎪
⎨ x2 = f 2 (xi
⎪                            | i=1∼2 )ϑ2 + g2 (xi(0∼m i −1) | i=1∼2 )ẋ3
.                                                                             (10.4)
⎪             .
⎪
⎪ x (m n−1 ) = f (x (0∼m i −1) |                                (0∼m i −1)
⎪
⎪                                  i=1∼n−1 )ϑn−1 + gn−1 (x i               | i=1∼n−1 )ẋn
⎪  n−1
⎩ (m n )
n−1 i
xn = f n (xi(0∼m i −1) | i=1∼n )ϑn + gn (xi(0∼m i −1) | i=1∼n )u.
In Duan (2021c), the relations among four types of high-order models with uncer-
tainties are discussed, while the above four types of high-order models with unknown
parameters have similar relations.
10.2 Backstepping for Second-Order SFSs
Before proceeding, let us introduce the following new notation for convenience:
Ai0∼m = [ Ai ]0∼m , i = 1, 2, . . . , n,
where Ai , i = 1, 2, . . . , n, are a series of matrices of appropriate dimensions.
Based on Theorem 5.3, we can give a direct backstepping design method for the
second-order SFS (10.1) without turning the system into a conventional first-order
SFS. To do this, we need some preparations.
Suppose Ai0∼1 ∈ R1×2 , i = 1, 2, . . . , n, are a set of matrices which make
Ai0∼1 ∈ R2×2 , i = 1, 2, . . . , n, stable, and
Pi Ai0∼1 = Pi F Ai0∼1                    Pi L Ai0∼1    ∈ R2×2 ,

## [147] `book_2026_volume1` (PDF p.365, L350)

Assumption 11.1 det B (y, t) = 0 or ∞, for all y ∈ Rm , and t ≥ 0.

## [148] `book_2026_volume1` (PDF p.365, L350)

Assumption 11.2 There exist a scalar ρ > 0 and a convex subset .                  ⊆ Rnr
containing the origin such that:
f x1(0∼n−1) , t − f x2(0∼n−1) , t       ρ x1(0∼n−1) − x2(0∼n−1) ,        (11.2)
holds for all x1(0∼n−1) , x2(0∼n−1) ∈
11.2 Full-Order Observer-Based Control                                                          351
The observer-based dynamical output controller for system (11.1) can be designed
as
u = −B −1 (·) f x̂ (0∼n−1) , t + A0∼n−1 x̂ (0∼n−1)
(11.3)
x̂˙ (0∼n−1) = ( A0∼n−1 )x̂ (0∼n−1) − L y − C0∼n−1 x̂ (0∼n−1) ,
where x̂ (0∼n−1) is the estimation of x (0∼n−1) , and A0∼n−1 ∈ Rr ×nr and L ∈ Rnr ×m
are matrices to be designed.
With the above controller, system (11.1) becomes
x (n) = −A0∼n−1 x̂ (0∼n−1) +      f (·) ,              (11.4)
where
f (·)        f x (0∼n−1) , x̂ (0∼n−1) , t
= f x (0∼n−1) , t − f x̂ (0∼n−1) , t (11.5)
Note that the state-space form of (11.4) is
ẋ (0∼n−1) =   (00∼n−1 ) x (0∼n−1) + B c          f (·) − A0∼n−1 x̂ (0∼n−1) (11.6)
The closed-loop system is obviously composed of
x̂˙ (0∼n−1) =      (A0∼n−1 ) x̂ (0∼n−1) − LC0∼n−1 x (0∼n−1) − x̂ (0∼n−1) ,          (11.7)
and
ẋ (0∼n−1) =   (00∼n−1 ) x (0∼n−1) + B c          f (·) − A0∼n−1 x̂ (0∼n−1) (11.8)
Then, we impose the following assumption, which plays a role in the subsequent
stability analysis.

## [149] `book_2026_volume1` (PDF p.366, L351)

Assumption 11.3 The matrix pair ( (00∼n−1 ) ,C0∼n−1 ) is observable.
Based on the above preparation, we can now state the problem to be solved in this
section as follows.

## [150] `book_2026_volume1` (PDF p.369, L354)

Assumption 11.4 det B(z, t)               0 or .∞, .∀z ∈ Rn 1 r1 and t ≥ 0.
Without loss of generality, the function f (·, ·) can be always decomposed as
follows:
z1
f (z 1 , z 2 ) = FD    + f 0 (z 1 , z 2 ),         (11.26)
z2
where f 0 (·, ·) : Rn 1 r1 × Rn 2 r2 → Rr1 +r2 is a known nonlinear function, and
F11 F12
FD =            ,                                 (11.27)
F21 F22
with F11 ∈ Rr1 ×n 1 r1 , F12 ∈ Rr1 ×n 2 r2 , F21 ∈ Rr2 ×n 1 r1 , F22 ∈ Rr2 ×n 2 r2 being known
matrices. In the special case of f 0 (z 1 , z 2 ) = 0, system (11.25) reduces to
11.3 Reduced-Order Observer-Based Control                                                                        355
⎧ (n 1 )
⎨ x1                 x1(0∼n 1 −1)
(n 2 ) = FD                  + B(x1(0∼n 1 −1) , t)u
x2               x2(0∼n 2 −1)                                                       (11.28)
⎩
y = x1(0∼n 1 −1) .
When both x1(0∼n 1 −1) and x2(0∼n 2 −1) are measurable, we can design for system
(11.25) the following state feedback controller:
x1(0∼n 1 −1)
u = −B −1 (x1(0∼n 1 −1) , t)             f 0 (x1(0∼n 1 −1) , x2(0∼n 2 −1) ) + A F                        , (11.29)
x2(0∼n 2 −1)
where
A11 A12
AF =
A21 A22
is a feedback gain with A11 ∈ Rr1 ×n 1 r1 , A12 ∈ Rr1 ×n 2 r2 , A21 ∈ Rr2 ×n 1 r1 , and A22 ∈
Rr2 ×n 2 r2 Under this controller, the closed-loop system is given by
x1(n 1 )             F11 − A11 F12 − A12                     x1(0∼n 1 −1)

## [151] `book_2026_volume1` (PDF p.376, L361)

Assumption 11.5 The function f 0 (·, ·) : Rn 1 r1 × Rn 2 r2 → Rr1 +r2 is α-Lipschitz with
respect to its second argument, that is, there exists a scalar α > 0 such that
f 0 (X, Y1 ) − f 0 (X, Y2 ) ≤ α Y1 − Y2 .
Closed-Loop System
In this case, partition
f 0 = f 0 x1(0∼n 1 −1) , x2(0∼n 2 −1) − f 0 x1(0∼n 1 −1) , x̂2(0∼n 2 −1)
⎡                                                   ⎤
f 1 x1(0∼n 1 −1) , x2(0∼n 2 −1) , x̂2(0∼n 2 −1)
=⎣                                                    ⎦,                          (11.49)
f 2 x1(0∼n 1 −1) , x2(0∼n 2 −1) , x̂2(0∼n 2 −1)
362                                                                               11 Observer-Based Control
where f 1 : Rn 1 r1 × Rn 2 r2 → Rr1 , f 2 : Rn 1 r1 × Rn 2 r2 → Rr2 Then all f 0 , f 1
and f 2 are present, and now Theorem 11.2 becomes the following.

## [152] `book_2026_volume1` (PDF p.393, L379)

Assumption 12.1 det B̃ (X, t) = 0 or ∞, for all X ∈ Rκ0 , and t ≥ 0, where
η
κ0 =
μi ri .
i=1
Clearly, a special case of the above general FAS (12.6) is the following single-order
one:
(n)
x     = f x (0∼n−1) , t + B x (0∼n−1) , t u,               (12.8)
and the above Assumption 12.1 becomes

## [153] `book_2026_volume1` (PDF p.393, L379)

Assumption 12.2 det B (X, t) = 0 or ∞, for all X ∈ Rnr , and t ≥ 0.
It is known from linear systems theory that a stabilizable linear system can be
decomposed into a controllable subsystem and a stable uncontrollable subsystem. A
similar fact holds also for nonlinear systems.
According to Duan (2021g), nonlinear (affine) systems which are not completely
controllable generally fall into two main categories: one is the type of sub-controllable
systems or sub-FASs in which the full-actuation assumption is not met completely
but partially, and the other is the Type I system in the following form:
−1)         (0∼γ −1)
x (μk ) |k=1∼η = f˜ xk(0∼μk |k=1∼η , z k k |k=1∼ξ , t
k
−1)              (0∼γk −1)
+ B̃ xk(0∼μk             |k=1∼η , z k           |k=1∼ξ , t u,    (12.9)
(γ )                  (0∼γk −1)
z k |k=1∼ξ = g̃ z k
k                                 |k=1∼ξ , t ,                                 (12.10)
where γk , k = 1, 2, . . . , ξ, are a set of positive integers, z k ∈ Rlk , k = 1, 2, . . . , ξ,
are a set of vectors of proper dimensions,. f˜ (·) and g̃ (·) are two nonlinear vector func-
(0∼γ −1)
tions, while the other variables are as stated before. It is required that z k k |k=1∼ξ
−1)
and xk(0∼μk |k=1∼η are independent of each other. Under this requirement, the extra
subsystem (12.10) is obviously an isolated unforced one.
The stability of the subsystem (12.10), when it is nonlinear, is complicated. Note
that a system in the form of (12.10) can be always converted into a state-space form.
Regarding the stability of a high-order system in the form of (12.10), we make the
following convention.
Convention I: A high-order nonlinear system in the form of (12.10) is said to be
GUA stable if its state-space form is GUA stable.
Without loss of generality, in this chapter, the following stability assumption is
proposed:

## [154] `book_2026_volume1` (PDF p.394, L380)

Assumption 12.3 Subsystem (12.10) is GUA stable at the origin.
Furthermore, the following full-actuation assumption is also imposed.
(0∼γk −1)

## [155] `book_2026_volume1` (PDF p.394, L380)

Assumption 12.4 det B̃ X, z k                           |k=1∼ξ , t = 0 or .∞, for all X ∈ Rκ0 , t ≥ 0,
(0∼γ −1)             (0∼γ −1)
and z k k |k=1∼ξ , with z k k |k=1∼ξ being the solution to subsystem (12.10).
According to Duan (2021g, 2023b), under Assumption 12.4, in addition, if the
whole Type I system (12.9)–(12.10) cannot be further converted into another Type I
system in which the fully actuated subsystem is of a higher order than that of FAS
(12.9), then the FAS in (12.9) represents the controllable subsystem, while (12.10)
represents the uncontrollable subsystem, and the variables z k (t) , k = 1, 2, . . . , ξ,
are called the uncontrollable variables. Furthermore, the whole system (12.9)–(12.10)
is called stabilizable in a certain sense if the uncontrollable subsystem (12.10) is stable
in the same sense. Please note that, in certain cases, a Type I system may be still
completely controllable, that is, it can be still further converted into a FAS.
When.η = 1, the above system (12.9)–(12.10) obviously reduces to the following:
x (n) = f x (0∼n−1) , z (0∼m−1) , t + B x (0∼n−1) , z (0∼m−1) , t u,                  (12.11)
(m)           (0∼m−1)
z          =g z             ,t (12.12)
where n and m are two positive integers.
In this circumstance, the above Assumptions 12.3 and 12.4 respectively become
12.2 Robust Control Problem Formulation                                                  381

## [156] `book_2026_volume1` (PDF p.395, L381)

Assumption 12.5 Subsystem (12.12) is GUA stable at the origin.

## [157] `book_2026_volume1` (PDF p.395, L381)

Assumption 12.6 det B X, z (0∼m−1) , t = 0 or .∞ for all X ∈ Rnr , t ≥ 0, and
(0∼m−1)
z         , with z (0∼m−1) being the solution to subsystem (12.12).
When Assumption 12.4 is met, we can design the following controller for the
Type I system (12.9)–(12.10) based on only FAS (12.9) as follows [see Duan (2021g,
2023b)]:
⎧
−1)           (0∼γ −1)
⎪
⎪
⎪ u = − B̃ −1 xk(0∼μk |k=1∼η , z k k |k=1∼ξ , t u
⎪
⎪
⎪
⎪ u = f˜ x (0∼μk −1) |           (0∼γk −1)
⎪
⎪                      k=1∼η , z k         |k=1∼ξ , t + u ∗
⎪
⎨            k
⎡ ∗    ⎤
u1                                                        (12.13)
⎪
⎪ ∗ ⎢ u ∗2 ⎥
⎪
⎪
⎢
⎥
⎪
⎪ u = ⎢ .. ⎥ , u ∗k = [ Ak ]0∼μk −1 xk(0∼μk ,
−1)
⎪
⎪      ⎣      ⎦
⎪
⎪          .
⎩
u ∗η
and the following closed-loop system is obtained:
⎧
⎨ xk(μk ) + [ Ak ]0∼μk −1 xk(0∼μk −1) = 0, k = 1, 2, . . . , η
(12.14)
⎩ z k(γk ) |k=1∼ξ = g̃ z k(0∼γk −1) |k=1∼ξ , t ,
which is clearly GUA stable if the coefficient matrices [ Ak ]0∼μk −1 , k = 1, 2, . . . , η,

## [158] `book_2026_volume1` (PDF p.397, L383)

Assumption 12.7 There exist two sets of nonnegative functions ρ̃i (·) and σ̃i (·) ,
i = 1, 2, . . . , η, such that the nonlinear uncertainty f˜i (·) ∈ Rri satisfies
−1)                      (0∼γk −1)
f˜i (·)       ρ̃i (·) xi(0∼μi               + σ̃i (·) κi      zk           |k=1∼ξ   ,   (12.18)
i = 1, 2, . . . , η,
where κi (·) , i = 1, 2, . . . , η, are a set of properly chosen K∞ functions.
The nonlinear function
⎡           ⎤
h̃ 1 (·)
⎢ h̃ 2 (·) ⎥
⎢          ⎥
h̃ (·) = ⎢      . ⎥ , h̃ i ∈ R i ,
r
(12.19)
⎣ .. ⎦
h̃ η (·)
in (12.16) is required to satisfy the following assumption.
(0∼γk −1)

## [159] `book_2026_volume1` (PDF p.398, L384)

Assumption 12.8 h̃ i z k                  |k=1∼ξ , i = 1, 2, . . . , η, are a series of K∞ -
bounded functions.
Based on the above description, the main problem to be solved in this chapter can
be described as follows.

## [160] `book_2026_volume1` (PDF p.398, L384)

Assumption 12.9 There exist two nonnegative functions ρ (·), σ (·) , such that
f (·)          ρ (·) x (0∼n−1) + σ (·) κ             z (0∼m−1)   ,
where κ (·) is a K∞ function.

## [161] `book_2026_volume1` (PDF p.398, L384)

Assumption 12.10 h z (0∼m−1) is a K∞ -bounded function.
Moreover, Problem 12.1 reduces to the following one.

## [162] `book_2026_volume1` (PDF p.406, L392)

Assumption 12.11 There exist two nonnegative scalar functions ρ x (0∼n−1) , t and
(0∼n−1)
σ x         , t such that the nonlinear uncertainty f (·) ∈ Rr satisfies
f (·)       ρ x (0∼n−1) , t    x (0∼n−1) + σ x (0∼n−1) , t κ       z (0∼m−1)   , (12.48)
where κ (·) is a K∞ function.
When Assumption 12.9 is substituted with Assumption 12.11, Theorem 12.1
becomes the following.

## [163] `book_2026_volume1` (PDF p.407, L393)

Assumption 12.12 The following condition
B (·) B −1 (·) ≤ c < 1,                      (12.52)
holds for all the variables x (0∼n−1) , z (0∼m−1) , and t ≥ 0.

## [164] `book_2026_volume1` (PDF p.407, L393)

Assumption 12.13 There exist two nonnegative functions ρb (·) and σb (·) , such
that
B (·)  ρb (·) x (0∼n−1) + σb (·) κb z (0∼m−1) ,
where κb (·) is a K∞ function.
Still, as in Sect. 12.3.1, let the controller be in the form of
u = −B −1 (·) f (·) + A0∼n−1 +
ϑ PLT x (0∼n−1) (12.53)
εσmin
(PL )
Then the closed-loop system is
x (n) = − A0∼n−1 +                      ϑ PLT x (0∼n−1)
εσmin
(PL )
+h z 0∼m−1 +           f (·) +      f b (·) ,           (12.54)
where
f b (·) = − B (·) B −1 (·) f (·) + A0∼n−1 x (0∼n−1)
− 2             B (·) B −1 (·) PLT x (0∼n−1) (12.55)
εσmin (PL )
Thus it can be shown that
f b (·)       ≤     B(·) B −1 (·) f (·) + A0∼n−1 x (0∼n−1)
+ 2          ϑ B(·)B −1 (·) PLT x (0∼n−1)
εσmin (PL )
≤        B −1 (·) f (·) + A0∼n−1 x (0∼n−1)
× ρb (·) x (0∼n−1) + σb (·) κb z (0∼m−1)
c      1
+              ϑ PLT x (0∼n−1) (12.56)
ε σmin
(PL )

## [165] `book_2026_volume1` (PDF p.409, L395)

Assumption 12.14 There exists a nonnegative function ρ x (0∼n−1) , t such that
f (·)       ρ x (0∼n−1) , t   x (0∼n−1) .
As a direct corollary of Theorem 12.3, the following result holds.

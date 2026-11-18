# Sorted Remark Corpus Across 32 Duan First-Author Papers + Volume I (155 items)

## [1] `aaas_2024_subsfs` (PDF p.7, L747)

说明 由上述定理可见，当系统初值取自指
数吸引域 Rs时，亚全驱系统式（20）在所设计的亚
镇定控制器驱动下的闭环系统响应便指数收敛
到原点。一般说来，问题的指数吸引域都是比较
大的，能够满足实际应用问题的需要。如果一定
要将初值取在指数吸引域之外，可以设计一个预
设控制律 ，先将系统的响应驱动到指数吸引域
内 ，然后再由所设计的亚镇定控制律接管 。 同
样，由于指数吸引域较大，这种预设控制律往往
很容易求得。

## [2] `aaas_2024_subsfs` (PDF p.8, L800)

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

## [3] `aas_2020_part1` (PDF p.7, L687)

说明 1. 严格反馈系统的控制方法很多. 反步
法和滑模控制的优点是鲁棒性好, 但所获得的闭环
系统也多为非线性的. 由定理 2 知严格反馈系统可
以化为高阶全驱系统, 因此可以得到线性定常的闭
环系统.

## [4] `aas_2020_part1` (PDF p.9, L942)

说明 2. 上述定理的证明可参见文献 [38−39].
该定理给出的是矩阵 K 的整体形式. 可以进一步证
明其分量形式如下:

Ai = EGi + W∞Hi, i ∈ Nm−1 (58)

其中 Gi ∈ Rn×n, Hi ∈ R(n+n0)×(n+n0), i ∈ Nm−1
分别由下面二式决定:

H0 H1 · · · Hm−1 = diag(0, In)Ve−1(Z, F)
(59)

G0 G1 · · · Gm−1 =

ZFmdiag(I(m−1)n, 0)Ve−1(Z, F) (60)

当 E = In 时, 集合 F 化为

F∆ = {F|F ∈ Rnc×mn 且 ∃Z ∈ Rn×mn
s. t. det V (Z, F) ≠ 0}

此时基于上述定理 4 我们可得下述推论.

段广仁: 高阶系统方法 — I. 全驱系统与参数化设计

## [5] `aas_2020_part2` (PDF p.4, L407)

说明 1. 式 (10) 中的第二组方程也可称作关
联方程, 它给出的是高阶全驱系统的基础状态及其
各阶导数和原系统状态变量之间的关联关系, 它在
一定意义上也可以理解为系统 (11) 的输出方程. 应
用中, 它可以将原系统的输出和高阶全驱系统的基
础状态 x 及其各阶导数联系起来, 起到一个中间纽
带的作用.

## [6] `aas_2020_part2` (PDF p.9, L953)

说明 2. 由定义 2 可知, 全驱系统是一类以控制
变量为核心的系统, 本质上可以几乎显示解出控制
变量 u. 进一步由定义 3 可知, 完全能控的系统就是
可以求解出控制变量的系统. 控制系统的状态空间

段广仁: 高阶系统方法 — II. 能控性与全驱性

模型以系统的状态为核心, 对于求解系统的状态响
应、状态观测与估计等问题自然提供了方便, 但对于
求解系统的控制问题并没有提供多少益处. 由命题

## [7] `aas_2020_part2` (PDF p.9, L965)

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
现在考虑含有两个附加项的非线性系统

Ex(m) = f(x,x, · · · , x(m−1), t)+
˙
g(x,x, ˙ · · · , x(m−1), u, t) + f∗ + d (64)

在控制律 (62) 的作用下, 可得如下形式的闭环系统

Ex(m) + Am−1x(m−1) + · · · + A1x + A0x =
˙
ν + f∗ + d (65)

1) 如果 d 是未知干扰, 我们可以应用一些频域
方法处理系统 (65) 的干扰解耦和抑制问题, 也可以
用一些现代的方法, 比如 H 无穷方法, 处理相应的
干扰抑制问题;
2) 如果 f∗ 是非线性摄动或者线性摄动, 原系统
的某种鲁棒控制问题便转化成了线性系统 (65) 的相
应鲁棒控制问题, 可以应用已知的线性系统鲁棒控
制方法进行求解;
3) 如果 f∗ 是某种参考输入信号, 以用来解决原
系统的某类信号跟踪问题, 此时问题也转化成线性
系统 (65) 的相应信号跟踪问题.

## [8] `fasta_2026_roea` (PDF p.4, L475)

Remark 1. If no interior stationary point t∗ exists in
(ti−1, ti), then the maximum of g(t, x, y) over [ti−1, ti] is
attained at the endpoints. Hence, Ri reduces to the intersec-
tion of the two endpoint half-planes

Ri = R(ti−1) ∩ R(ti),

where

R(t) = {(x, y) ∈ ℝ2 | ϕ1(t)x + ϕ2(t)y < d}.

The feasible region obtained as the line

α(t)x + β(t)y = d

continuously evolves from t = ti−1 to t = ti. Therefore,
when no interior stationary point exists, the RoEA on this
subinterval is completely determined by the two endpoint
half-planes.

## [9] `fasta_2026_roea` (PDF p.4, L495)

Remark 2. If an interior stationary point t∗ = t∗(x, y) ex-
ists in (ti−1, ti), then the additional constraint

ϕ1(t∗)x + ϕ2(t∗)y < d

should also be imposed. Since t∗ generally depends on
(x, y), this constraint is not, in general, a fixed half-plane
constraint. Instead, it may generate a nonlinear boundary in
the (x, y) plane. Therefore, on each subinterval, the infinite
family of inequalities can be reduced to finitely many active
candidates, namely the two endpoints and, when it exists, the
state-dependent interior stationary point.

Then we can express the RoEA over entire time domain.

## [10] `fasta_2026_roea` (PDF p.6, L723)

Remark 3. Our previous works on the characterization of
the RoEA, including [3, 8, 11, 12], primarily relied on the
boundary evaluation at the initial and terminal time instants
of the functions ϕi (t). This leads to a polygonal outer ap-
proximation of the RoEA constructed from endpoint con-
straints, while the true RoEA is actually a subset of this re-
gion. The conservatism originates from neglecting the possi-
ble extrema of the constraint functions over the time domain.

In this paper, we address this limitation by incorporating
both the stationary points of ϕi (t) and the interior station-
ary points of the composite function g(t). By explicitly char-
acterizing these critical points, the time-infinite constraints
can be reduced to a finite but complete active set, which en-
ables an exact characterization of the RoEA.

## [11] `ijss_2021_part1` (PDF p.5, L475)

Remark 2.1: In the case that the condition (4) is
replaced by

rankB(x(0∼m−1), ζ) = n < r, ∀t > 0, (5)

the system (3) is called over-actuated. In the high-
order system representation, over-actuated systems
may be occasionally encountered. Such systems can
be similarly treated as fully actuated ones in terms of
control.

The importance of fully actuated systems (where
r = n) lies in the following simple fact (Duan, 2020a).

## [12] `ijss_2021_part1` (PDF p.8, L767)

Remark 3.1: It is clearly observed that the linear part
in each subsystem of the pseudo strict-feedback sys-
tem (23) has relation with zi but not its derivatives.
If this is not the case in an application, we can con-
vert certain related subsystems into lower order ones in
order to eliminate this phenomenon. It is easily noted
that in the extreme case that the related subsystems
are converted into first-order systems, such derivative
terms do not appear. On the other hand, it should be
noted that this operation naturally changes the pseudo
strict-feedback system with a fixed order into the one
with mixed orders (Duan, 2020d), but this change does
not affect our treatment.

## [13] `ijss_2021_part1` (PDF p.10, L1063)

Remark 3.2: It is seen from the above result that as
long as the matrix F is chosen stable, the closed-loop
system is stable. Clearly, there are quite some free-
dom in the selection of F, while on the other hand
we also have the parameter matrix Z, which provides
m2n degrees of freedom. All these degrees of freedom
can be further utilised to achieve additional perfor-
mance of the system (see, e.g. Duan, 1992, 1993; Duan
et al., 2002, 2000; Duan & Zhao, 2020.

To end this section, we give the following summing- and
up points: x3
⎡ ⎤
1 0
• In the case of n = qr, where q is an integer, the B (x) = 0 0 .
procedure finishes as soon as we get the higher- ⎢⎢⎣ ⎥⎥⎦
1 + x3 1
order fully actuated system (24). The controller
is given as in (36), and the closed-loop system is Let
given by (28). It is obvious that the single-input case −1 −1 0 1
⎡ ⎤
always belongs to this case. 0 0 1 0
Q = , (48)
• In the case of n0 ≠ 0, and condition (44) is met, the ⎢⎢⎣ 0 1 0 0⎥⎥⎦
procedure leads to two HOFA models of different 1 0 0 0
orders. Consequently, control of these HOFA mod- then it can be easily verified that
els produces two decoupled constant linear closed-
loop systems, one is of order n0, which is given 02×2
QB (x) = [ ],
by (37), the other is of order r − n0, which is given G (x)
by (46 ). The trick discovered for solving the prob-
lem is to divide the control into two parts, with each with
one controlling an fully actuated subsystem. 1 0
G (x) = [ ].
• In the case of n0 ≠ 0, and condition (44) is not met, x3 1
we need to re-organise system (43) into the form
Therefore, under the transformation
of (11), with certain elements of u2 being the con-
trol, while with u1 being taken as an external vector, z = Qx, (49)
and start over a new round with this much smaller
scale system. the example system (47) is equivalently converted into
the following two subsystems:

## [14] `ijss_2021_part1` (PDF p.12, L1201)

Remark 4.1: According to Isidori (1995, p. 358), this
example system has a zero dynamics defined on the

sub-manifold

Z∗ = x ∈ ℝ4 : x1 = x2 = 0 ,
{ }
with the representation, expressed in the (x3, x4) coor-
dinates of Z∗, as

{x˙3 = x32
x˙4 = −x4.

Therefore, the approach of non-interacting control
fails. Even with a modified design, a stable zero dynam-
ics still exists. While in our above design, a constant
linear closed-loop system is obtained with all its four
poles arbitrarily assignable.

## [15] `ijss_2021_part1` (PDF p.13, L1340)

Remark 4.2: This example system does not obey the
triangular structure of a strict-feedback system, hence
the well-know method of backstepping is generally
not applicable. Furthermore, with only the assump-
tion (56), the conditions for the well-known method
of feedback linearisation are also not met. Yet with the
proposed HOFA system approach the problem is well
solved in the sense that a constant linear closed-loop
system is obtained with a desired eigenstructure.

## [16] `ijss_2021_part2` (PDF p.5, L444)

Remark 2.1: The Assumption A1 is a global one, it
requires (4) to hold for xi ∈ ℝr, i = 1, 2, . . . , n. Relax-
ation of this assumption to a local one can be consid-
ered. If this assumption is valid only on a certain set
Ω ⊂ ℝnr, then the derived high-order system (6) is a
HOFA model on a certain set Ω′ determined from Ω
by the transformation (5).

## [17] `ijss_2021_part2` (PDF p.5, L452)

Remark 2.2: Once the HOFA model (6) is obtained,
the controller of the system can then be simply
designed as (Duan, 2020a, 2020d)

{u = −L−n1(A0∼n−1z(0∼n−1) + u∗)
(10)
u∗ = hn(z(0∼n−1), ζ, t) − v,

which gives the following constant linear closed-loop
system

z(n) + A0∼n−1z(0∼n−1) = v,

where v is some external signal, while A0∼n−1 is an
arbitrary matrix which makes Φ(A0∼n−1) stable. A
complete parametric approach for solving the matrix
A0∼n−1 is given in Duan (2020a) (see also the Propo-
sition 2 in Duan, 2020d).

## [18] `ijss_2021_part2` (PDF p.7, L701)

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

## [19] `ijss_2021_part2` (PDF p.7, L715)

Remark 2.4: Although it is apparent that the 1st- and
2nd-order SFSs (3) and (11) are the special cases of
the high-order one (18), it is hard to tell a similar rela-
tion among the outcomes of the converted high-order
systems of these systems.

## [20] `ijss_2021_part2` (PDF p.13, L1426)

Remark 4.1: It is clearly seen from the above two
examples that the solution processes of the HOFA
system approach are very simple. If the first exam-
ple system is converted into a first-order system with
two multivariable subsystems, and the second exam-
ple system is converted into a first order system with
5 subsystems, experience tells us that applications of
method of backsteppinig to the converted first-order
systems should turn out to be much more complicated.

## [21] `ijss_2021_part3` (PDF p.8, L815)

Remark 3.1: In applications, the radii of the ellipsoids
Θμ,ε(0) and Θμ,ε((x∗)(0∼n−1)) can be comprehen-
sively adjusted through two ways to make it as small as
desired: one is to increase the stability threshold μ of
the linear part of the system, the other is to reduce the
value of ε, or equivalently, to increase the magnitude
of the control.

## [22] `ijss_2021_part3` (PDF p.8, L823)

Remark 3.2: The proposed method can be extended
to some sub-fully actuated systems (Duan, 2020a,
2020c). One of the natural ideas of doing this is to
select properly a set of initial values and a reference
signal x∗(t) such that the solution of the system can
pass safely around the ‘dangerous’ area which possibly
make the matrix L(x(0∼n−1)) off-rank by following the
‘lead’ of the reference signal x∗(t), so as to preserve the
boundedness and realizability of the controller.

## [23] `ijss_2021_part3` (PDF p.8, L833)

Remark 3.3: When the nonlinear uncertainty is
removed, we can choose ρ(x(0∼n−1)) = 0. In this case
the closed-loop system is in the following constant
linear form:

x(n) + A0∼n−1x(0∼n−1) = 0,

which can be equivalently written in the following
state-space form:

x(0∼n−1) = Φ(A0∼n−1)x(0∼n−1).
˙

This tells us that, different from many other non-
linear control approaches, the proposed HOFA sys-
tem approach produces a constant linear closed-loop
system when the uncertainties do not present (see
also, Duan, 2020a, 2020b, 2020c). This huge advantage
eventually allows most of the theories and techniques
for linear control systems design to be applicable.

Regarding the solution of the matrix A0∼n−1, we
have the following result, which is the Corollary 1 in
Duan (2020b) (see, also Duan, 2020a, 2020d, 2020f).

## [24] `ijss_2021_part3` (PDF p.9, L882)

Remark 3.4: It is seen from the above result that in
order to meet the condition (9), it suffices only to select
a matrix F satisfying

μ
Reλi (F) < − , i = 1, 2, . . . , nr. (24)
2

Clearly, there are quite some degrees of freedom in the
selection of F, while on the other hand we also have
the parameter matrix Z, which provides r2n degrees of
freedom. All these degrees of freedom can be further
utilised to achieve additional performance of the sys-
tem (see, e.g. Duan, 1992, 1993; Duan et al., 2002, 2000;
Duan & Zhao, 2020).

## [25] `ijss_2021_part3` (PDF p.13, L1325)

Remark 4.1: The above proposed second-order back-
stepping method can be easily modified to suit the
other companion SFS (4). As a matter of fact, for
SFS (4), we can simply take P˜i(A0i∼1) = Pi(Ai0∼1), i =
1, 2, . . . , n, and in this case we also have theoret-
ically QiL(A0i∼1) ≠ 0, i = 1, 2, . . . , n, which ensure
Li(z1(0∼∼i1)) ≠ 0, i = 1, 2, . . . , n.

## [26] `ijss_2021_part3` (PDF p.16, L1702)

Remark 5.1: The above proposed mixed-order back-
stepping method can also be easily modified to
suit the other companion SFS (6). As a matter of
fact, for SFS (6), we can simply take P˜i(A0i∼mi−1) =
Pi(A0i∼mi−1), i = 1, 2, . . . , n, and in this case we also
have theoretically QiL(A0i∼mi−1) ≠ 0, i = 1, 2, . . . , n,
since QiL(A0i∼mi−1) can be easily shown to be a diago-
nal element of a positive definite matrix.

## [27] `ijss_2021_part3` (PDF p.16, L1711)

Remark 5.2: The second- and high-order (mixed-
order) backstepping methods discussed in the previ-
ous and the current sections can both be properly
modified to cope with the case of signal tracking.
Specifically, in order to let x1 track a given sufficiently
smooth signal x1∗(t), we need only to adjust the first
step of these second- and high-order methods of back-
stepping by substituting (30) or (81) by

z(0∼1) = x(0∼1) − x∗ (0∼1) ,
1 1 ( 1)

or

z(0∼m1−1) = x(0∼m1−1) − x∗ (0∼m1−1) ,
1 1 ( 1)

and then in the sequential steps treat the terms related
to the reference signal x1∗(t) properly.

## [28] `ijss_2021_part3` (PDF p.16, L1731)

Remark 5.3: The above high-order backstepping
method for high-order systems appears to be more
complicated in description. It should be noted that,
in many specific engineering applications, mi, i =
1, 2, . . . , n often take the values of 1 and 2. So the fact
is, in such applications, the mixed-order backstepping
method is even simpler than that of the second-order
systems.

## [29] `ijss_2021_part3` (PDF p.16, L1740)

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

## [30] `ijss_2021_part3` (PDF p.18, L1904)

Remark 6.1: If the system (109) is converted into
the first-order state-space model, then the converted
model is composed of 4 subsystems, and eventually
four steps of backstepping are needed to solve the
problem. Experience with normal first-order back-
stepping designs tells us that the design process for the
converted first-order systems with four steps of back-
stepping is definitely much more complicated than the
above process.

## [31] `ijss_2021_part4` (PDF p.7, L685)

Remark 3.1: The proposed method can be extended
to some sub-fully actuated systems (Duan, 2020d).
One of the natural ideas of doing this is to select prop-
erly a set of initial values and a reference signal x∗(t)
such that the solution of the system can pass safely
around the ‘dangerous’ areas which possibly make the
matrix L(x(0∼n−1)) off-rank by following the ‘leading’
signal x∗(t), so as to preserve the boundedness and
realizability of the controller.

## [32] `ijss_2021_part4` (PDF p.11, L1232)

Remark 4.1: The above proposed second-order back-
stepping method can be easily modified to suit the
other companion SFS (3). As a matter of fact, for
SFS (3), we can simply take P˜i(A0i∼1) = Pi(A0i∼1),
i = 1, 2, . . . , n, and in this case we also have theo-
retically QiL(A0i∼1) ≠ 0, i = 1, 2, . . . , n, which ensure
Li(z1(0∼∼i1)) ≠ 0, i = 1, 2, . . . , n.

## [33] `ijss_2021_part4` (PDF p.15, L1595)

Remark 5.1: The above proposed mixed-order back-
stepping method can also be easily modified to
suit the other companion SFS (5). As a matter of
fact, for SFS (5), we can simply take P˜i(A0i∼mi−1) =
Pi(A0i∼mi−1), i = 1, 2, . . . , n, and in this case we also
have theoretically QiL(A0i∼mi−1) ≠ 0, i = 1, 2, . . . , n,
since QiL(A0i∼mi−1) can now be shown to be a diagonal
element of a positive definite matrix.

## [34] `ijss_2021_part4` (PDF p.15, L1604)

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

## [35] `ijss_2021_part5` (PDF p.4, L388)

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

## [36] `ijss_2021_part5` (PDF p.5, L412)

Remark 2.2: Assumption A2, as well as the Assump-
tion thmA2’ which is imposed for the case of constant
unknown parameter vectors in Section 5, are both very
common ones. Further studies may consider the case
where the nonlinearities possess some structural prop-
erties. Theoretically, Assumption A3 also quite general
and allows the parameter θ(t) goes to infinity. How-
ever, it is clear that Assumption A3 holds for some
δ0 and δ1 when both θ(t) and its pre-estimation θ0(t)
are uniformly bounded with respect to t ∈ [0, ∞).

## [37] `ijss_2021_part5` (PDF p.5, L506)

Remark 2.3: In the following discussion, we often
omit some independent variables in the case of not
causing confusion, e.g. P(A0∼n−1) and PL(A0∼n−1) are
denoted by P and PL, respectively; H(x(0∼n−1)) and
L(x(0∼n−1)) are denoted by H and L, respectively.

## [38] `ijss_2021_part5` (PDF p.9, L861)

Remark 4.1: Obviously, the radius of the ellipsoid
Θ(μ,ε,δ)(0) and Θ(μ,ε,δ)((x˜∗)(0∼n−1)) can be compre-
hensively adjusted through three ways: one is to
increase the stability threshold μ of the linear part;
the second is to reduce the value of ε, or equivalently,
to increase the magnitude of control; the third is to
reduce the values of δ1 and δ2 by improving the pre-
estimation accuracy of the parameter vector. The first
two aspects can be adjusted at will, but the third aspect
cannot. Since the proposed method depends on the
pre-estimation θ0 of the parameter θ, it is very dif-
ficult to obtain δ1 and δ2 with very small values in
the absence of prior information. This leads to the
fact that the radius of the ellipsoids Θ(μ,ε,δ)(0) and
Θ(μ,ε,δ)((x˜∗)(0∼n−1)) cannot be arbitrarily small.

## [39] `ijss_2021_part5` (PDF p.9, L877)

Remark 4.2: When the unknown time-varying
parameter θ does not exist, we have δ = 0, and the
adaptive parts of the control laws ua and u ˆa vanish. In
such a case, the results in this paper reduce to those
in Duan (2020c). In this situation, the radius of the
final ellipsoid can be made as small as desired through
increasing the stability threshold μ and increasing
the magnitude of control (equally, reducing the value
of ε), that is, the desired accuracy of signal tracking
can be guaranteed. However, the situation becomes
complicated when there exist unknown time-varying
parameters in the system.

## [40] `ijss_2021_part5` (PDF p.11, L1148)

Remark 6.1: The adaptive control of nonlinear sys-
tems with time-varying unknown parameters has
always been a difficult problem in the field of sys-
tems and control. The result in Section 3 shows
that although there exist uncertain nonlinear terms
and time-varying unknown parameters in the system,
we can still obtain a control law which guarantees
the stability (boundedness) of the closed-loop sys-
tem. However, due to the time-varying nature of the
unknown parameters, asymptotical stability is gener-
ally not achievable.

## [41] `ijss_2021_part5` (PDF p.11, L1160)

Remark 6.2: Parallelly, it can also be seen that
the solution to the tracking problem considered in
Section 4 is not in an asymptotic sense, and the estab-
lished control law may not ensure a high tracking
accuracy. What the proposed control law can achieve
is to ensure that the actual operating state of the system
will not deviate too far away from the desired one. Such
kind of tracking requirements has numerous practi-
cal backgrounds, e.g. mid-course guidance of long-
distance missiles, monitoring and tracking of space

targets, etc. A common characteristic in these applica-
tions is to keep the system running with lower energy
while maintaining an endurable and controllable per-
formance before the time to take further ‘action’.

## [42] `ijss_2021_part5` (PDF p.12, L1178)

Remark 6.3: In the situation where the unknown
parameter is time-varying, generally speaking, it
is very difficult to realise asymptotic tracking or
arbitrary-precision tracking. To increase the tracking
accuracy, it is recommended to obtain as much as pos-
sible a priori information about unknown parameters
based on theoretical and technical analysis, numerical
experiments as well as man’s experience in order to
give smaller δ1 and δ2, so as to improve the tracking
accuracy. After all, it is not necessary to argue whether
the parameter estimation is realised or not, but only
to regard the proposed controller as a dynamic com-
pensator. The conclusion is that the stabilisation of the
system in the sense of global boundedness is achieved
under this dynamic compensator.

## [43] `ijss_2021_part5` (PDF p.12, L1194)

Remark 6.4: Disturbance attenuation or compensa-
tion has always been an important issue in control
systems design. The unknown parameter θ in HOFA
model (3) in this paper can also be regarded as an
unknown disturbance vector. The disturbance term
HTθ represents a structural perturbation of the sys-
tem. From this perspective, the work of this paper
can also be regarded as the robust control of systems
with structural disturbances. In particular, in distur-
bance compensation theory, constant disturbance is
an important case and is widely accepted. When the
parameter vector θ is constant, the work in this paper
can also be regarded as robust control with disturbance
compensation using a disturbance estimator.

## [44] `ijss_2021_part5` (PDF p.12, L1209)

Remark 6.5: The proposed method can be extended
to some sub-fully actuated systems. One of the natural
ideas of doing this is to select properly a set of initial
values and a reference signal x∗(t) such that the solu-
tion of the system can safely pass around the ‘danger-
ous area’ which possibly makes the matrix L(x(0∼n−1))
off-rank by following the ‘leading’ signal x∗(t), so as
to preserve the boundedness and realisability of the
controller. This idea will be demonstrated by several
examples in the Part VII (Duan, 2021d) of the series.

## [45] `ijss_2021_part6` (PDF p.6, L560)

Remark 2.1: It is clearly seen from (11) that some con-
stant disturbances, slope disturbances, etc., may auto-
matically disappear when the HOFA system method is
used for design. Therefore, the HOFA system approach
itself has certain ‘natural’ anti-disturbance character-
istics. In certain situations, the control of a system
subject to disturbances can be turned in a control
problem free of disturbances (see the examples in
Duan (2021a, 2021b, 2020a, 2020b)).

## [46] `ijss_2021_part6` (PDF p.6, L623)

Remark 2.2: For the HOFA model (8) with a deter-
ministic disturbance and the HOFA model (12)
and (13) with a dynamical disturbance, many practi-
cal examples exist at least for the second-order sys-
tem case. For the HOFA model (8) with a determin-
istic disturbance, we aim to consider the problem
of disturbance attenuation since no further informa-
tion about the disturbance is known. For the HOFA
model (12) and (13) with a dynamical disturbance, we
can realise asymptotical disturbance decoupling based
on the dynamical model of the disturbance.

## [47] `ijss_2021_part6` (PDF p.8, L842)

Remark 3.1: The above theorem clearly establishes
a general parametric solution of the controller (18),
which arbitrarily assigns the desired eigenstructure
of the closed-loop system (22). It is actually a result
on eigenstructure assignment in the linear system
[Φ(00∼n−1), Bc], which is termed as the ‘basic prob-
lem’ in Duan (2021a) (see, also the Corollary 1 in
Duan (2020b), or refer to Duan (2020b, 2020c)),

## [48] `ijss_2021_part6` (PDF p.12, L1290)

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

## [49] `ijss_2021_part6` (PDF p.14, L1478)

Remark 4.2: Note that, in the case of Cm = I,

Φ(00∼n−1) BcE Lx
Ace = [ ] + [ ][Cm 0]
0 Φ(S0∼k−1) Ld

Lx
= ΦE + [ ]CI, (90)
Ld

the above theorem gives a parametric approach to
design the gains Lx and Ld satisfying the first con-
dition in Theorem 4.3. Combining Theorems 4.3
and 4.5 gives a complete parametric approach for
asymptotic disturbance decoupling via dynamical state

feedback. The complete explicit degrees of freedom
are composed of the parameters F0 and F1, and Zi,
i = 0, 1, 2. These degrees of freedom can be further
properly utilised to achieve additional system per-
formance requirements (see, e.g.Duan, 1992a, 1993b;
Duan et al., 2002, 2000a; Duan & Zhao, 2020).

## [50] `ijss_2021_part6` (PDF p.14, L1501)

Remark 4.3: This whole series of papers are only
providing a demonstration of the HOFA approaches,
while control of sub-fully actuated systems will remain
to be a main future investigation topic. Certain ideas
about the control of sub-fully actuated systems have
been mentioned in the previous papers, and some
examples will be presented in the forthcoming Part
VII (Duan, 2021e). Eventually, disturbance attenua-
tion and decoupling in sub-fully actuated systems will
be certainly one of the research topics investigated in
the future.

## [51] `ijss_2021_part7` (PDF p.11, L1050)

Remark 3.1: For the more general fully actuated sys-
tem (19), a result similar to Proposition 3.1 still holds.
In this case, the controller can be obtained using the
differential homeomorphism property of the mapping
u˜ = g(xk(0∼μk−1)|k=1∼η, ζ, t, u), as

⎧u = g−1 xk(0∼μk−1)|k=1∼η, ζ, t,u ˜)
(
[A1] (0∼μ1−1)
⎛⎡ 0∼μ1−1 x1 ⎤ ⎞
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ [A ] (0∼μ2−1)
2 0∼μ2−1 x2
u˜ = − + u∗ (34)
⎜⎜⎜⎜⎜⎜⎝⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ ⎟⎟⎟⎟⎟⎟⎠
(0∼μη−1)
[Aη]0∼μη−1xη

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩u∗ = f (xk(0∼μk−1)|k=1∼η, ζ, t) − v,

and the same closed-loop system as in (31) is achieved.

Since the closed-loop system (31) is linear, for con-
venience we call the controller in the form of (30),
or (34), a linearising controller for the HOFA sys-
tem (8). When expanded, each subsystem in the above
linear closed-loop system (31) can be written as

xk(μk) + [Ak]μk−1x(μk−1)

+ · · · + [Ak]1x˙ + [Ak]0x = vk,

whose eigen-polynomial matrix obviously is

Pk (s) = Irksμk + [Ak]μk−1sμk−1

+ · · · + [Ak]1s + [Ak]0.

Due to the arbitrariness of the series of matrices
[Ak]i, ı = 0, 1, . . . , μk − 1, k = 1, 2, . . . , η, the eigen-
polynomial matrices of each subsystem in the linear
closed-loop system (31) can be arbitrarily assigned.
Therefore, a linear closed-loop system with desired
performance can be obtained by properly selecting
these matrices. Particularly, the closed-loop eigenval-
ues can be arbitrarily assigned by properly selecting
these matrices. Such a property of HOFA systems
totally reveals the meaning of controllability of control
systems.

## [52] `ijss_2021_part7` (PDF p.14, L1463)

Remark 4.1: The stability of the subsystem (49), when
it is nonlinear, is more complicated. It could be glob-
ally stable or locally stable, and could be asymptotically
stable or critically stable. Furthermore, the equilibrium
status may be also complicated. It is the stability of this
subsystem that determines the stability of the whole
closed-loop system. We mention that a well accepted
stability of the subsystem (49) is that it gives bounded
y(0∼p)(t) for arbitrary initial value y(0∼p)(0) and ζ ∈
ℝp, t ≥ 0.

## [53] `ijss_2021_part7` (PDF p.14, L1474)

Remark 4.2: For control of the type I system con-
sisting of subsystems (48) and (49), there are also

cases which do not require the stability of the sub-
system (49). For instance, in a general dynamical dis-
turbance decoupling problem, the subsystem (49) may
present the disturbance model which generates the dis-
turbance y(t), while the control purpose is to control
the subsystem (48) such that a system output

z = Cx(0∼μk−1)|k=1∼η
k

with C being a proper constant matrix, is decoupled
from the effect of y(t). For a simplified formulation of
such a problem, one can refer to Duan (2020e).

## [54] `ijss_2021_part7` (PDF p.16, L1674)

Remark 4.3: Obviously, the type II realisation of
a dynamical control system Σphysical or (26) is not
unique. A main task to realise stabilisation of the sys-
tem is to obtain a strongly stabilisable type II reali-
sation. Once such a realisation is sought, as a con-
sequence the system can be realised by designing a
linearising controller for the HOFA subsystem only.

## [55] `ijss_2021_part7` (PDF p.19, L1951)

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

## [56] `ijss_2021_part7` (PDF p.20, L2084)

Remark 6.1: It is pointed in Brocket (1983) that for
this example system there does not exist a continuous
control law which asymptotically stabilises the system
at the origin. On one side, the above treatment sup-
ports this fact more clearly in two ways. Firstly, the
design requires c0 = ˜y(0) > 0. Secondly, note a2 > 0,
we have from (92) limt→∞x ˜(t) ≠ 0 when x ˜0 ≠ 0 and
d0 = ˜z(0) ≠ 0. While on the other side, the above
treatment gives an ‘almost’ globally stabilising con-
troller, with a clearly asymptotical behaviour of all the
system variables.

## [57] `ijss_2021_part7` (PDF p.20, L2096)

Remark 6.2: We have to mention an important issue,
that is, the stability achieved in this example, or gener-
ally the stability achieved with the HOFA approaches
when the system is sub-fully actuated, is different from
the usual definition of stability since constraints on
the initial values, for instance, c0 = ˜y(0) > 0 in this
example system, are often imposed. We remark that
this kind of stability is, to an great extent, practically
acceptable, and will be further addressed elsewhere.

## [58] `ijss_2021_part7` (PDF p.23, L2306)

Remark 6.3: In Brocket (1983), a locally stabilising
controller for the example system (93) is proposed.
While Proposition 6.4 tells us that an ‘almost’ glob-
ally stabilising controller in fact exists for the system.
What is more, the system variables y and z are deter-
mined by a stable linear system, and the state x, like y
and z, also converges to zero exponentially. We point
out that the constraint y0 ≠ 0, on the initial value, is
not at all strict since initial values of a system can often
be altered according to one’s will.

## [59] `ijss_2021_part7` (PDF p.23, L2317)

Remark 6.4: It is obvious that the system variables x
and y are in a symmetry position. In the above design,
we have required y ≠ 0, and derived a HOFA system
with variables y and z. While using this symmetry
structure of the system, we can also require x ≠ 0, and
derive a HOFA system with variables x and z. Com-
bining both cases, we can give a solution to the system
under the much weaker condition

x02 + y02 ≠ 0.

## [60] `ijss_2022_part10` (PDF p.8, L786)

Remark 3.1: The above Theorem 3.4 obviously indi-
cates that a step forward HOFA system in the form
of (15) is equivalent to a step backward HOFA sys-
tem in the form of (16). While this is certainly
not true since the step forward HOFA system in
the form of (15) is in essence a time-delay sys-
tem as revealed above. Such an equivalence would
clearly contradict with the Law of Cause and Effect
⌊1∼μp−1⌋
since zp (k)|p=1∼η is generally considered to be
unknown. The Theorem is somehow misleading due
to an implicit reason behind this fact, that is, both
the step backward and the step forward systems are
converted under the assumption that the state vec-
tor x(k) of the controllable linear system (2) is avail-
able. When x(k) is available, so is z = T(x), hence
⌊0∼μp−1⌋
zp (k)|p=1∼η is also available. It is this hidden
hypothesis that has made this fact holds true. Without
this hypothesis, the step forward HOFA system (15)
and the step backward HOFA system (16) can be by
no ways equivalent.

## [61] `ijss_2022_part10` (PDF p.8, L809)

Remark 3.2: It is clearly seen that the step forward
HOFA system (15) and the step backward HOFA sys-
tem (16) are both time-delay systems. Particularly,
the step forward HOFA system in the form of (15)
is a discrete-time system with an input delay. There-
fore, this paper has actually included contents in
the scope of discrete-time delay systems. Since the
problem of controller design for the step forward
HOFA system in the form of (15) is essentially a
controller design problem for a system with delay
in the control vector, it turns out to be much more
complicated, and will be investigated in a separate
paper.

To end this section, we finally mention the following
two high-order discrete-time systems (self-recursive

model) frequently encountered in linear system the-
ory:

n−1 m
x (k + n) = ∑An−i−1x (k + i) + ∑Bm−iu (k + i) ,
i=0 i=0
(19)

and

n−1 m
x (k + 1) = ∑Aix (k − i) + ∑Biu (k − i) , (20)
i=0 i=0

It can be easily reasoned that, when B = B0 is a square
nonsingular matrix, the system (19) can be converted
equivalently into the following step forward HOFA
model:

n−1
x (k + n) = ∑Aix (k + i) + Bu′(k + m) ,
i=0

where
m
u′(k + m) = B−1∑Bm−iu (k + i)
i=0
m−1
= u (k + m) + ∑ B−1Bm−iu (k + i) ,
i=0
(21)

while the system (20) can be converted equivalently
into the following step backward HOFA model:

n−1
x (k + 1) = ∑Aix (k − i) + Bu′′(k) ,
i=0

where
m
u′′(k) = B−1∑Biu (k − i)
i=0
m
= u (k) + ∑B−1Biu (k − i) . (22)
i=1

In both cases, the original control vectors in the two
systems can be uniquely solved through (21) and (22),

## [62] `ijss_2022_part10` (PDF p.13, L1391)

Remark 5.1: When f (·) is restricted to be linear and
B(·) is a constant nonsingular matrix, the above result
turns to be the control of the linear multiple-order
HOFA system (16) or (18). For the more general non-
affine step backward HOFA system (40), a result sim-
ilar to Theorem 5.2 still holds. The controller can be
obtained using the differential homeomorphism prop-
⌈0∼μp−1⌉
erty of the mapping u ˜ = g(xp |p=1∼η, k, u), as

−1 ⌈0∼μp−1⌉
⎧u (k) = g (xp (k) |p=1∼η, k,u ˜ (k))

⌈0∼μp−1⌉ ∗
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨u˜ (k) = −f (xp (k) |p=1∼η, k) + u (k)

[A1]0∼ϖ1−1 x1⌈0∼ϖ1−1⌉(k)
⎡ ⌈0∼ϖ2−1⌉ ⎤
[A2]0∼ϖ2−1 x2 (k)
u∗(k) = + v (k) ,
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ ⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎦
⌈0∼ϖη−1⌉
[Aη]0∼ϖη−1xη (k)
(56)

and the same closed-loop system as in (49) is achieved.

## [63] `ijss_2022_part10` (PDF p.13, L1418)

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

## [64] `ijss_2022_part10` (PDF p.13, L1432)

Remark 5.3: Note that

Ψ (A0∼n−1) = Ψ (00∼n−1) + ΓcA0∼n−1,

and [Ψ(0), Γc] is controllable, the solution to the feed-
back gains in the proposed controllers really reduces
to a problem of finding a real matrix K such that
A + BK is Schur for some controllable matrix pair
[A, B]. This can be easily and completely solved by
using the Lemma 5.2 in Duan (2021c), where the
matrix F needs to be chosen Schur. Particularly, to find
an A0∼n−1 to make Ψ(A0∼n−1) Schur, the dual form of
Theorem 3.4 in Duan (2021b) can be readily used, with
the matrix F chosen Schur.

## [65] `ijss_2022_part10` (PDF p.13, L1447)

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

## [66] `ijss_2022_part10` (PDF p.13, L1465)

Remark 5.5: It is again clearly observed in the above
Theorems 5.1 and 5.2 that the linear closed-loop sys-
tems are obtained with desired coefficient matrices,
or equivalently, with desired eigenstructures. Such a

property of HOFA systems totally reveals the mean-
ing of controllability of dynamical control systems.
Therefore, following the general line in Duan (2021c),
controllability and stabilisability of general discrete-
time systems can be also readily defined. Specifically,
a dynamical system is called controllable if it can be
represented by either a step forward or a step back-
ward HOFA model. While a stabilisable dynamical
system can be represented by either a step forward or
a step backward HOFA model, together with a stable
autonomous dynamical system.

## [67] `ijss_2022_part10` (PDF p.14, L1484)

Remark 5.6: The feasibility requirements (47) and
(51) are essential for general HOFA systems. They
vanish only for global fully actuated systems. For
continuous-time HOFA systems, two types of feasi-
bility conditions are provided, one is dependent on
a Lyapunov matrix equation (see the Lemma 5.2 in
Duan, 2021d), the other is based on the closed-loop
eigenstructure (see the Lemma 6.1 in Duan, 2021e).
Both types of conditions turn out to be constraints on
the system initial values, and can be both parallelly
extended to the discrete-time system case.

## [68] `ijss_2022_part10` (PDF p.15, L1632)

Remark 6.1: As treated in Duan (2021f), the strict-
feedback system (63) can be also generalised to the

second-order case and the mixed-order case. Partic-
ularly, a second-order strict-feedback system in step
backward form can be represented as follows:

⎧x1 (k + 1) = f1(x1⌈0∼1⌉(k))+g1(x1⌈0∼1⌉(k))x2 (k)

x2 (k + 1) = f2(x1⌈0∼∼21⌉(k))+g2(x1⌈0∼∼21⌉(k))x3 (k)
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
...
xn−1 (k + 1) = fn−1(x1⌈0∼∼n1−⌉1(k))

+gn−1(x1⌈0∼∼n1−⌉1(k))xn (k)
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ ⌈0∼1⌉ ⌈0∼1⌉
xn (k + 1) = fn(x1∼n (k))+gn(x1∼n (k))u (k) ,
(64)

which can be also shown to be representable by an
HOFA model. Moreover, as in Duan (2021f), a second-
order backstepping design for the above second-order
strict-feedback system can be also proposed.

## [69] `ijss_2022_part10` (PDF p.15, L1656)

Remark 6.2: It follows from Theorem 3.4 that a
discrete-time controllable linear system can be equiv-
alently converted into a HOFA system. Now in this
section, it happens that both the feedback linearis-
able systems and strict-feedback systems can be equiv-
alently converted into HOFA systems. These facts
strongly demonstrate, to an extent, the generality
of the HOFA system approaches. With the HOFA
approaches, it is clearly seen in Section 5 that a
controller for a HOFA system can be immediately
designed. We point out that the designs can be also
easily generalised to systems with disturbances and
uncertainties, as done in the continuous-time cases
(see Duan, 2021g, 2021i, 2021a, 2021b, 2021e).

## [70] `ijss_2022_part8` (PDF p.5, L434)

Remark 2.1: The above HOFA model (3) might be
easily mistaken to represent a very small portion of
systems due to the full-actuation Assumption A1.
While as discussed in Duan (2020a), Duan (2020d)
and Duan (2020j), it serves as a general model for
dynamical control systems. Many systems which are
in state-space forms can be converted into HOFA sys-
tems (see Duan (2020a), Duan (2020b), Duan (2020d)
and Duan (2020e)), and practical systems can also be
modelled as HOFA systems.

If we denote

f (xk(0∼μk−1)|k=1∼η, ζ, t)

⎡ f1(xk(0∼μk−1)|k=1∼η, ζ, t) ⎤

f2(xk(0∼μk−1)|k=1∼η, ζ, t)
= ,
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
fη (xk(0∼μk−1)|k=1∼η, ζ, t)

then the HOFA system (1) can be compactly written as

xk(μk)|k=1∼η = f (xk(0∼μk−1)|k=1∼η, ζ, t)

+ B(xk(0∼μk−1)|k=1∼η, ζ, t)u. (3)

Recall that xk ∈ ℝrk, k = 1, 2, . . . , η, we have

x(0∼μk−1) ∈ ℝμkrk, k = 1, 2, . . . , η.
k

Denote
η
κ = ∑rkμk, (4)
k=1

then it is easy to see that

x(0∼μk−1)|k=1∼η ∈ ℝκ.
k
For the above system (3), we can impose the output
equation
y = Cx(0∼μk−1)|k=1∼η, (5)
k
where C ∈ ℝm×κ is a known matrix.
Particularly, in the case that the above system (3) has
the following set of output equations

yk = Ckxk(0∼μk−1), k = 1, 2, . . . , η, (6)

where Ck, k = 1, 2, . . . , η, are a set of constant matrices
of appropriate dimensions, we can define

y1
⎡ ⎤
y2
y =
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
yη

C = blockdiag (Ck, k = 1, 2, . . . , η) ,

which obeys the output Equation (5).

## [71] `ijss_2022_part8` (PDF p.6, L547)

Remark 2.2: Please note that a special case of the
above general HOFA model (1) is clearly the following
HOFA model with a single-order:

x(n) = f (x(0∼n−1), ζ, t) + B(x(0∼n−1), ζ, t)u, (10)

which forms the basic part of the system models
involved in the problems of robust control, adap-
tive control and disturbance rejection treated in
Duan (2020f), Duan (2020g), Duan (2020h) and
Duan (2020i).

## [72] `ijss_2022_part8` (PDF p.6, L559)

Remark 2.3: Most physical systems are governed by
certain physical laws, such as the Newton’s Law, the
Lagrangian Equation, the Theorem of Linear and
Angular Momentum, Kirchhoff’s Laws of Current and
Voltage. When such physical laws are used in mod-
elling, a series of second-order subsystems are origi-
nally obtained (Duan, 2020a). From this stage we can
further get a state–space model by variable extension,
and on the other side, we can get a HOFA model
by variable elimination if the system is controllable
(Duan, 2020j). It should be noted that many physically
fully actuated systems exist, which are already in the
form of second-order HOFA systems at the modelling
stage.

## [73] `ijss_2022_part8` (PDF p.7, L752)

Remark 3.1: In linear systems theory, time-varying
linear system context is a very important part. Dif-
ferent from constant linear ones, time-varying linear
systems are usually much more difficult to handle.
As a matter of fact, the well-known linear quadratic
optimal control problem is generally formulated with
time-varying linear systems. We point out that, with
HOFA approaches, problems related to time-varying
linear systems generally do not present since the time-
varying terms in the system may be included in the
nonlinear term of the HOFA system and hence can-
celled by using the full-actuation property.

## [74] `ijss_2022_part8` (PDF p.8, L808)

Remark 4.1: For the infinite-time optimal control
problem, considering tracking an arbitrary signal z(t),
as in the finite-time optimal control problem formu-
lated in Section 3, is generally not realisable. However,
for certain signal z(t) generated by a proper dynami-
cal system, infinite-time tracking problem can indeed
be well formulated and solved (see, e.g. Anderson
and Moore (1990)).

## [75] `ijss_2022_part8` (PDF p.9, L917)

Remark 4.2: Due to the above Theorem 4.3, the
optimal controller (35) may be viewed as a stabilis-
ing controller for the system (3). However, different
from a general stabilising controller for the system,
the controller (35) also assures that the state vector
xk(0∼μk−1)(0)|k=1∼η of the closed-loop system goes to
zero with a smooth and steady transient performance,
and, particularly, ‖xk(0∼μk−1)(t)|k=1∼η‖P converges to
zero monotonously.

## [76] `ijss_2022_part8` (PDF p.9, L927)

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

## [77] `ijss_2022_part9` (PDF p.5, L476)

Remark 2.1: The above HOFA model (2) might be
easily mistaken to represent a very small portion of
systems due to the full-actuation Assumption A1.
While as discussed in Duan (2020a, 2021c, 2021e),

it serves as a general model for dynamical con-
trol systems. Many systems which are in state-space
forms can be converted into HOFA systems (see
Duan, 2020a, 2020b, 2021e, 2021f), and practical sys-
tems can also be modelled as HOFA systems (see the
Remark 3 in Duan, 2021d).

## [78] `ijss_2022_part9` (PDF p.5, L488)

Remark 2.2: A special case of the above general
HOFA model (1) is clearly the following:

x(n) = f (x(0∼n−1), ζ, t) + B(x(0∼n−1), ζ, t)u, (6)

which forms the basic part of the system models
involved in the problems of robust control, adap-
tive control and disturbance rejection treated in
Duan (2021a, 2021b, 2021g, 2021h).

## [79] `ijss_2022_part9` (PDF p.8, L853)

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

## [80] `ijss_2022_part9` (PDF p.16, L1781)

Remark 6.1: It is easily recognised that the fea-
sibility conditions given in Theorems 6.3 and 6.4

may be conservative. In certain cases, e.g. when
det B(xk(0∼μk−1)|k=1∼η) is dependent on only some,
but not all, xk’s and their derivatives, less conserva-
tive initial value ranges can be provided by applying
decoupled design approaches (see Section 3.3, and also
Duan (2021d)). The next section gives a demonstra-
tion of this idea with an illustrative example.

## [81] `ijss_2022_part9` (PDF p.17, L1794)

Remark 6.2: The results presented in this subsec-
tion are conservative but are strictly correct. While in
many cases, the set of singular points is only a low-
dimensional hyperplane in the space ℝκ, in this case,
as long as the steady response of the closed-loop sys-
tem does not intersect with 𝕊, the probability that
the system response in the transient process intersects
with 𝕊 is very small. This is why some practical appli-
cations on control of sub-fully actuated systems simply
overlook such a feasibility analysis problem. However,
for applications of high-grade security or high cost, a
trial and test approach is certainly not acceptable.

## [82] `ijss_2024_underactuated4` (PDF p.6, L540)

Remark 2.1: It is well-known that a region of attrac-
tion for Lyapunov stability is a single-connected region
which contains a ball centered at the origin. How-
ever, the REA for sub-stability may be more com-
plicated, it may even do not contain the origin. The
following statements reveal the relation between sub-
stabilisation and stabilisation in the Lyapunov sense:

(1) when the REA coincides with the whole initial
value space, the derived sub-stabilising controller
becomes a globally exponentially stabilising con-
troller in the Lyapunov sense;
(2) when the REA contains the origin as an interior
point, the derived sub-stabilising controller is also
at least a local exponentially stabilising controller
in the Lyapunov sense; and
(3) when the origin is only a boundary point of the
largest REA, the derived sub-stabilising controller
still works in the way that it drives all the trajecto-
ries of the closed-loop system starting from REA
to the origin exponentially, but now it can by no
means be a stabilising controller for the system in
the Lyapunov sense.

## [83] `ijss_2024_underactuated4` (PDF p.6, L564)

Remark 2.2: For applications in which initial values
outside of the REA can not be avoided, a globally sta-
bilising controller can be easily designed based on the
designed sub-stabilising controller through the follow-
ing two ways:

(1) To apply the designed sub-stabilising controller
for initial values within the REA, and apply a glob-
ally (or locally) Lyapunov asymptotical stabilising
controller (if exists) for those initial values in the
complement of the REA. In this way, an initial
value-dependent globally (or locally) asymptoti-
cally stabilising controller is obtained.
(2) To design a pre-controller to first drive those tra-
jectories starting from the complement of the
REA into the REA, and then let the designed sub-
stabilising controller take over. Please note that
usually the REA is a very large unbounded field,

it is certainly much easier to design such a pre-
controller than to design a stabilising controller in
the Lyapunov sense, that requires the controller to
drive all the system trajectories to a single point
(usually the origin). From this point of view, we
can conclude that sub-stabilisation is the key step
to realise asymptotical stabilisation of a dynamical
system.

## [84] `ijss_2024_underactuated4` (PDF p.6, L614)

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

The treatment in this section requires the following
assumption:

## [85] `ijss_2024_underactuated4` (PDF p.7, L733)

Remark 3.2: For nonlinear systems, most of the
researches are focused on time invariant systems. Sta-
bilisation of time-varying nonlinear systems is gen-
erally an unsolved problem. While with the FAS
approach, time-varying properties can be easily han-
dled. Another almost insurmountable difficulty in
nonlinear control is the type of nonsmooth systems.
Yet, as we see above, the functions f0(x, y, t) ∈ ℝn and
B0(x, y, t) ∈ ℝn×n are only required to be piece-wise
continuous. What is more, let us point out that time-
delays can also be easily treated with FAS approach
(Duan, 2022d, 2022e, 2023b, 2023c). These statements
also apply to the following three sections.

Regarding the UAS (10), we have the following
corollary.

## [86] `ijss_2024_underactuated4` (PDF p.9, L929)

Remark 3.3: For the converted subsystem (31), x0 ≠
0 stands only for a parameter restriction. While for
the original system (28) or (29), it stands for a system
initial value restriction. As a matter of fact, the REA is

{ x1, x2, y | x1 ≠ 0, x1, x2, y ∈ ℝ}.
( )

Please note that this domain does not contain the
origin, but contains the origin as a boundary point.
This states that the designed system possesses a ‘non-
holonomic’ feature (Duan, 2023e). While as it is well-
known, the system (29) is indeed a typical nonholo-
nomic one.

To finish this section, let us give a further remark
regarding another generalisation.

## [87] `ijss_2024_underactuated4` (PDF p.9, L947)

Remark 3.4: It is important to point out that the
UAS (9) can in fact be generalised into the following
form:
x˙ = f0 x, y, t + g0 x, y, u, t
{ ( ) ( ) (34)
y˙ = g x, y, t ,
( )
where g0 is a piece-wise continuous function. It can be
easily shown that a sub-FAS for system (34) is given by

z¨ = f (z,z ˙, t) + ˜g (z,z ˙, u, t) , (35)

where f (z,z ˙, t) is given by (14), and

g˜ (z,z ˙, u, t) = Gx (h (z,z ˙, t) , z, t) g0 (h (z,z ˙, t) , z, u, t) .
(36)

In this case, the set of feasibility is still given by (16),
but with Ω2 being defined to be the region on which
g˜(z,z ˙, u, t) is a homeomorphism with respect to u.

## [88] `ijss_2024_underactuated4` (PDF p.16, L1803)

Remark 5.1: The UASs (73) and (74) can obviously be
generalised into the forms of

⎧q¨1 = fˇ0(q1, q(20∼1), t) + Bˇ0(q1, q(20∼1), t)u
⎨ (0∼1)
q¨2 = g (q1,q ˙1, q2 , t),
⎩
(112)

and

{q¨1 = u
(0∼1) (113)
q¨2 = g (q1,q ˙1, q2 , t),

respectively. Due to the complexity and paper length
limit, these more general cases will be treated in sepa-
rate papers.

## [89] `jssc_2022_casestudy` (PDF p.5, L242)

Remark 2.2 Obviously, the above singularity set 𝕊 is a line passing through the origin
in the ( ˙x, x) plane when v = 0. Therefore, the closed-loop system (9) can be by no means
stable at the origin in the Lyapunov sense. However, since the singularity set is only a line in
the whole state-space, the system possesses a kind of “weakened” global exponential stability
since, as easily predicted and technically shown in the next section, that most of the system
trajectories will go to the origin.

## [90] `jssc_2022_casestudy` (PDF p.5, L248)

Remark 2.3 This system falls into such a scope whose equivalent FAS model is a sub-FAS
with its singularity set containing the origin. In general, such systems are difficult to handle,
and many typical benchmark systems for feedback stabilization in the literature in fact fall into
such a scope. This particular feature makes the system not feedback linearizable, and makes
the linearized model of the system at the origin an uncontrollable one.

## [91] `jssc_2022_casestudy` (PDF p.7, L369)

Remark 3.3 For this example system (1), it is well-known that it is not feedback lineariz-
able by a smooth state feedback controller, and equivalently, it is not globally exponentially
stabilizable by a smooth state feedback controller. While in this section, it is clearly shown
that from which subset in the initial value space the trajectories of the closed-loop system can
be made decaying to the origin exponentially by a smooth state feedback controller.

## [92] `jssc_2022_freq` (PDF p.4, L200)

Remark 2.3 If the state feedback U(s) = K(s)Z(s) is applied on the PMD (4), the
closed-loop system is (P(s) − Q(s)K(s)) Z(s) = 0, whose characteristic equation is given by

γc(s) ≜ det (P(s) − Q(s)K(s)) = 0.

Thus, if (4) is a fully actuated PMD, for any desired Pc(s) ∈ ℝq×q(s), we can set

K(s) = Q−01(P(s) − Pc(s)) ,

such that the characteristic polynomial γc(s) can be arbitrarily assigned. Thus, for a fully
actuated PMD, pole assignment turns to be extremely easy.
By taking the Laplace transformation of the state-space model (1) with zero initial condition,
we obtain
(sIn − A) X(s) = BU(s), (5)

which is exactly in the form of PMD (4) with

(P(s), Q(s)) = (sIn − A, B) . (6)

Similarly, by taking the Laplace transformation of the HOFA system model (2) with zero initial
condition, we have immediately the following interpretation of Proposition 2.1.

## [93] `jssc_2022_freq` (PDF p.11, L542)

Remark 4.6 Notice that the frequency domain equation (23) can be rewritten in the
time-domain as

⎡ z1(h1)(t) ⎤ ⎡ zi (t) ⎤
z2(h2)(t) r zi(1)(t)
= −∑D0−1Di + D0−1u(t). (27)
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ i=1 ⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
zr(hr)(t) zi(hi−1)(t)

It follows from (24) and (27) that the generalized state vector z(t) is uniquely determined by
x(t) and the time-domain expression for the corresponding fully actuated PMD in (12) is a
conventional high-order linear state-space system, rather than a descriptor high-order linear
state-space system, namely, the two problems encountered in Section 3 have been solved.
Let us provide an example to illustrate the obtained results.

## [94] `odfas_2026_part1` (PDF p.6, L624)

Remark 2.1. In the case of r = 2, let us choose

2 0 2 0 3 0
F0∼1 = [ ], L = −[ ].
0 2 0 3 0 4

Following (14), we obtain a dynamical output
feedback controller as

−8 0 2 0
u0 = [ ]y − [ ]z
0 −14 0 3
{ −17 0 −5 0
z˙ = [ ]y + [ ]z,
0 −30 0 −7
(17)
which assigns the set of closed-loop eigenvalues

{−1 ± i, −1, −2, −3, −4}. (18)

Applying Proposition 2.1 and Lemma 2.1 to
the above system (11), immediately produces the
following result.

## [95] `odfas_2026_part1` (PDF p.14, L1631)

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

the angle of substabilization. The result turns Convert system (100) into state-space form
out to be finer and more intuitive.

Under the feasibility condition [ z˙1 ] = A (γ)[ z1 ], (101)
z˙2 z2

x1 (t) ≠ 0, t ≥ 0, (94) where

we can introduce the following transformation: z1 = z, z2 = ˙z,

## [96] `odfas_2026_part1` (PDF p.15, L1681)

Remark 4.2. By now we can give a reason to 1 e−γt + γet et − e−γt z10
explain why the example system (93) is so tough. = γ + 1 [ (γet − γe−γt) et + γe−γt ] [ z20 ].
Convert its OD-FAS (98) into the following state- ( ) ( )

space form Therefore, the solution of system (100) is given
by
z(0∼1) = [ 0 1 ]z(0∼1) − [ 0 ]u
{ 0 1 1 1
z (t) =
y = 1 −1 . γ + 1
[ ]
× e−γt + γet z10 + κ (t) z20 (102),
We then can find out that this linear system is [( ) ]
1
not observable. Therefore, the example system z˙ (t) =
(93) is not globally stabilizable because it is not γ + 1
completely observable. × γκ (t) z10 + et + γe−γt z20(103),
[ ( ) ]

For the above linear OD-FAS (98), choosing where
the following static output controller
κ (t) = et − e−γt,
u = −γy = −γ (z − z ˙) , γ > 0, (99)
and
produces the following linear closed-loop system
z10 = z1 (0) , z20 = z2 (0) ,
z¨ = (1 − γ) ˙z + γz, (100)
are the initial values. This immediately implies
with closed-loop eigenvalues
lim z (t) = ∞,
s1 = 1, s2 = −γ. t→∞

which equivalently gives, in view of transforma-
tion (95),

lim x1 (t) = 0. (104)
t→∞

Further, from (102) and (103), we can also ob-
tain

x2 (t) = z (t) − z ˙ (t)
= e−γt(z10 − z20)
→ 0, as t → ∞. (105)

It thus follows from (104) and (105) that the
output feedback controller (99) GUA stabilize
system (93) under the feasibility condition (94).
Next, let us treat the feasibility condition (94).
To do this, let us first examine the condition

x1 (t) = 0, t ≥ 0. (106)

This is clearly equivalent to, in view of (102), the
following

e−γt + γet z10 + et − e−γt z20 = 0, t ≥ 0
( ) ( )

or

a (γ, t) z10 + b (γ, t) z20 = 0, t ≥ 0. (107)

where

a (γ, t) = e−(γ+1)t + γ,

## [97] `odfas_2026_part1` (PDF p.20, L2273)

Remark 5.1. The normalized model of the so-
called disk inertia pendulum is (see [20], [21],

Figure 4. A Subset of the RoEA

Figure 5. Simulation results for the IWP system

[12])

¨x = a sin θ
{
θ¨ = u,

where x and θ are scalar variables, and a is a
scalar parameter. Under the following diffeomor-
phism

ξ = x
ξ˙ = ˙x
{ ξ¨... = a sin θ
ξ = aθ˙ cos θ,

and the following control transformation

1 2
u = (θ˙ sin θ + u0),
cos θ

we can get the linear system (124) when x and
θ(0∼1) are measured. Therefore, the problem can
be solved exactly in the same way.

## [98] `odfas_2026_part4` (PDF p.11, L722)

Remark 2.1. By imposing Assumption A0, we assume that system (2.3) is a global OD-FAS,

which can be more easily treated. Treatment of OD-subFASs and substabilization can be found in the

first three parts of this series of papers, namely, Duan (2026b,0,0).

## [99] `odfas_2026_part4` (PDF p.11, L728)

Remark 2.2. Assumption A1 assumes M (ϕ) to be nonsingular. In this case we actually can

simply assume M (ϕ) = Ir (by inverting M (ϕ)). However, as we know that the above form (2.4) is

often preferred in the second-order case. Furthermore, regarding the parameter vector ϕ ∈ ℝnϕ, we

point out that it can be either some external time-varying function or a vector determined by some

variables in the state vector x (t). An example of the latter is the marine vehicle model treated in

Section 8.

Due to the above Assumption A1, system (2.4) can be rewritten as

x¨ (t) = R (ϕ (t)) A0∼1(ϕ(0∼1)(t))x(0∼1)(t)

+ R (ϕ (t)) fy (y (t − σi (t))|i=1∼p , t)

{ + R (ϕ (t)) B(y (t − τj (t))|j=1∼q , t)u (t) (2.5)
+ R (ϕ (t)) d (t)
y (t) = h x(0∼1), t .
( )

The purpose of the paper is to solve the output feedback stabilization and signal tracking problems of

OD-FAS (2.4), or, equivalently, OD-FAS (2.5), with the output being only the position or the velocity.

## [100] `odfas_2026_part4` (PDF p.16, L982)

Remark 4.1. Assumption Aϕ1 seems too restrictive. On the one hand, we mention that in certain

applications, this assumption can indeed be satisfied by practically equipping in the system a certain

type of accelerometer. On the other hand, we point out that this assumption can be released, in the

case of

A0∼1(ϕ(0∼1)) = A0∼1 (ϕ) ,

to the following one:

Assumption Aϕ2 ϕ(0∼1)(t) , t ≥ 0, is available (measurable);

## [101] `odfas_2026_part4` (PDF p.22, L1327)

Remark 4.2. It is important to point out the following two facts:

1. In view of the output equation (4.33), the dynamical controller in the form of (4.36)-(4.37) are

actually the feedback of the original system state α (t).

2. Once the transformed state x(0∼1) is obtained via the design control system, the original system

states α and ωz can then be obtained using diffeomorphism (4.32). Furthermore, due to the form

of diffeomorphism (4.32), it is easily observed that GUA stabilization of the converted OD-FAS

also implies the GUA stabilization of the original system (4.30).

## [102] `odfas_2026_part4` (PDF p.50, L2861)

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

## [103] `odfas_2026_part4` (PDF p.50, L2881)

Remark 7.2. Similar to the treatment in Subsection 5.4, the output feedback tracking control of

system (7.1) with disturbance rejection can be also solved under certain conditions.

## [104] `odfas_2026_part4` (PDF p.56, L3192)

Remark 8.1. Let us mention that once x(0∼1)(t) is obtained through the designed control system,

the original system responses η (t) and v† (t) can be immediately given by the diffeomorphism (8.15).

Due to our GUA stabilization result, we know that

lim x(0∼1) (t) = 0.
t→+∞

Thanks to diffeomorphism (8.15) and (8.7), we also have

lim (η†(t) − η∗(t)) = lim η (t)
t→+∞ t→+∞
= lim x (t) = 0
t→+∞
lim v (t) − RT(φ) ˙η∗(t) = lim RT(φ (t)) ( ˙x (t) + ˙η∗(t)) − RT(φ) ˙η∗(t)
t→+∞( ) t→+∞[ ]
= lim RT(φ (t)) ˙x (t)
t→+∞[ ]
= 0.

The above first relation clearly implies

lim ζ (t) = lim ζ† (t) − ζ∗(t) = 0. (8.31)
t→+∞ t→+∞[ ]

## [105] `odfas_2026_part4` (PDF p.60, L3413)

Remark 8.2. We mention that this decoupled design can not be generalized to the case that the

disturbance is present because, in general, the disturbance model does not possess a decoupled form.

## [106] `scis_2022_discdelay1` (PDF p.12, L791)

Remark 1. For the more general non-affine time-delay FAS (37), a result similar to Theorem 1 still
holds. The controller can be obtained using the differential homeomorphism property of the mapping

Duan G R Sci China Inf Sci August 2022 Vol. 65 182201:13

⌈τp,1∼ζp (k)⌉
u˜ = g(xp (k) |p=1∼η, k, u) as

−1 ⌈τp,1∼ζp(k)⌉
u (k) = g (xp (k) |p=1∼η, k,u ˜ (k)),

⌈τp,1∼ζp(k)⌉ ∗
u˜ (k) = −f (xp (k) |p=1∼η, k)+ u (k) ,

[A1]0∼̟1−1 x1⌈0∼̟1−1⌉(k) (55)
{ [A2] 2⌈0∼̟2−1⌉(k)
∗ 0∼̟2−1 x
u (k) = + v (k) ,
...
[Aη] η⌈0∼̟η−1⌉(k)
0∼̟η−1 x
and the same closed-loop system as in (47) is obtained.

## [107] `scis_2022_discdelay1` (PDF p.13, L815)

Remark 2. The design given in Theorem 1 is a decoupled one, and u∗(k) given in the controller (46)
is in fact a decentralized one. This is adequate to show the advantage of the FAS approach. However, a
coupled design can also be carried out, with the expression of u∗(k) in (46) replaced by

u∗(k) = Kx⌈p0∼̟p−1⌉(k) |p=1∼η + v (k) ,

where K ∈ ℝr×κ with
κ = r1̟1 + r2̟2 + · · · + rη̟η
is a feedback gain. For details, one can refer to the coupled design given in [26] for the continuous-time
case.

## [108] `scis_2022_discdelay1` (PDF p.13, L825)

Remark 3. Another aspect associated with the control design of a discrete-time delay FAS is the
complete parameterization of the designs. Since constant linear closed-loop systems are obtained, as done
in the continuous-time case, complete parametric expressions for the feedback gains in the controllers as
well as the closed-loop systems can be established, which provide all the design degrees of freedom to be
used for further improving the system performance.

## [109] `scis_2022_discdelay1` (PDF p.16, L1047)

Remark 4. Clearly, the matrix A0∼̟−1, or the series of matrices [Ap]0∼̟p−1 , p = 1, 2, . . . , η, should
be chosen such that the state-space systems in (51) are asymptotically stable. Noting that

Ψ (A0∼n−1) = Ψ (00∼n−1) − ΓcA0∼n−1

and [Ψ (0) , Γc] is controllable, the solution to the feedback gains in the proposed controllers really reduces
to a problem of eigenstructure assignment, and hence can be easily solved (see [26] for the continuous-time
case).

Duan G R Sci China Inf Sci August 2022 Vol. 65 182201:17

## [110] `scis_2023_delay1` (PDF p.7, L491)

Remark 1. It is clearly seen from the above discussion that, in order to control the FAS (26), it
suffices only to control the standard FAS (30). However, such a fact fails for a sub-FAS, in which the full
actuation assumption, that is, Assumption A1, is not valid. In order to maintain the consistency in the
treatment of both FASs and sub-FASs, in the following we still treat the original FAS (26) in Section 5
for controller design.

Duan G R Sci China Inf Sci January 2023 Vol. 66 112201:8

## [111] `scis_2023_delay1` (PDF p.17, L1079)

Remark 2. Particularly, if we choose in the above controllers (90) and (93)

A = Blockdiag([Ai]0∼µi−1 , i = 1, 2, . . ., η),

where [Ai]0∼µi−1 ∈ ℝri×µiri, i = 1, 2, . . . , η, then the following set of decoupled constant linear closed-
loop systems is obtained:

x(iµi) + [Ai]0∼µi−1xi(0∼µi−1) = vi, i = 1, 2, . . . , η, (94)

with v being an external input vector given by

v1

v2 ri
v = , vi ∈ ℝ . (95)
...
vη

For a systematic parametric method to solve the controller parameter matrix A such that the closed-loop
linear system possesses a desired eigenstructure, please refer to [49].

## [112] `scis_2023_delay1` (PDF p.17, L1099)

Remark 3. Let

## [113] `scis_2023_delay1` (PDF p.20, L1294)

Remark 4. With this definition, the following is obvious:
(1) all dynamical control systems, not only those in state-space representations, possess the concepts
of controllability;
(2) the problem of controllability analysis and the problem of control are now highly consistent in the
sense that, once the controllability of a system is verified by obtaining the FAS model of the system, the
design problem is then easily solved in view of Theorems 1 and 2.
Like controllability, stabilizability is also one of the most important concepts in control systems theory.
This subsection further looks into the problem of stabilizability.
It is well-known that a stabilizable linear system can always be decomposed into a controllable sub-
system and an uncontrollable subsystem, but with the uncontrollable one stable. Inspired by such a fact,
we can now introduce the following definition.

## [114] `scis_2023_delay2` (PDF p.7, L432)

Remark 1. For an FAS with state delays only, that is, the case of h = 0, we can define the new control
under Assumption A1:

u˜ (t − h) = B x(0∼n−1)(t − σj (t)) |j=1∼γ, t u (t − h) , (25)
( )

or the following new one under Assumption A1′:

u˜ (t − h) = g x(0∼n−1)(t − σj (t)) |j=1∼γ, t, u (t − h) , (26)
( )

such that the affine FAS (21) or the non-affine one (23) is converted equivalently into the following
standard form:
x(n)(t) = f x(0∼n−1)(t − τj (t)) |j=1∼ζ, t + ˜u (t − h) . (27)
( )
However, we point out that this may be not realizable when h > 0 since future state information may
have been used in the transformations (25) and (26).

## [115] `scis_2023_delay2` (PDF p.8, L503)

Remark 2. In the case of h = 0, we can introduce the following new control vector for FAS (28) under

## [116] `scis_2023_delay2` (PDF p.10, L659)

Remark 3. For the single-order non-affine FAS (23), a result similar to Lemma 1 still holds. As a
matter of fact, for the FAS (23), the predictor (46) is clearly replaced with the following one:

Z˙(s) = Φ (00∼n−1) Z (s) + Bcf (Z (s − τj (s + t)) |j=1∼ζ, s + t)
+Bcg (Z (s − σj (s + t)) |j=1∼γ, s + t, u (s + t − h)) , s ∈ [0, h] , (55)

with the same initial value condition (49).

## [117] `scis_2023_delay2` (PDF p.10, L666)

Remark 4. Prediction of future states is a core procedure in the control of a system with input delays.
The approach provided in this subsection is a general one but may be subject to certain problems:
(1) in complicated cases the predictor equation (46) may not be solvable both analytically and numer-
ically;
(2) when the numerical solution is adopted, computation errors inevitably occur, which on one side
may reduce the control precision, and on the other side may even cause instability of the system; and
(3) for systems with a very long input delay h, the open-loop stability is also needed in order that the
designed predictor produces reasonable large prediction values.

## [118] `scis_2023_delay2` (PDF p.11, L732)

Remark 5. For the single-order non-affine FAS (23), a result similar to Theorem 1 still holds. In this
case, the controller can be obtained using the predictor (46) and the differential homeomorphism property
of the mapping (26) as

u (t) = −g−1(Z (h − σj (t + h)) |j=1∼γ, t + h,u ˜ (t)) ,
u˜ (t) = f (Z (h − τj (t + h)) |j=1∼ζ, t + h) + u∗(t) ,
u∗(t) = A0∼n−1Z (h) − v (t + h) , t ⩾ 0,
(62)
{Z˙(s) = Φ (00∼n−1) Z (s) + Bcf (Z (s − τj (s + t)) |j=1∼ζ, s + t)
+BcB (Z (s − σj (s + t)) |j=1∼γ, s + t, u (s + t − h)) , s ∈ [0, h] ,
Z (θ) = x(0∼n−1)(θ + t), θ ∈ [−τ (t) , 0] ,

and eventually, the same closed-loop linear system as (57) is resulted in.

## [119] `scis_2023_delay2` (PDF p.11, L745)

Remark 6. Let
0 I

...
Φ(A0∼n−1) = .
I
−A0 −A1 · · · −An−1

Duan G R Sci China Inf Sci February 2023 Vol. 66 122201:12

Then it can be easily checked that the closed-loop system (57) can be expressed by the following state-
space form:
x˙(0∼n−1) = Φ(A0∼n−1)x(0∼n−1) + Bcv.

Further note that
Φ(A0∼n−1) = Φ(00∼n−1) − BcA0∼n−1.
The solution to the gain matrix A0∼n−1 ∈ ℝr×nr in the controllers (59) and (62) can then be easily
carried out by conducting the eigenstructure assignment in the matrix pair (Φ(00∼n−1), −Bc) (see [46]).
We point out that specific parametric eigenstructure assignment designs have been proposed in [37], which
give the general expressions of the gain matrix, and provide all the degrees of freedom in the designs.
The full degrees of freedom can be further utilized to achieve additional system performance.

## [120] `scis_2024_chained1` (PDF p.6, L386)

Remark 1. An important development in the generalization of the chained form systems was made in
2000 by Jiang [50], in which the robust stabilization of the following closely related model was considered
with the method of backstepping:

x˙0 = ψ0 (t) u0 + ∆f0 (t, x0) ,
x˙1 = ψ1 (t) x2u0 + ∆f1 (t, x0∼n, u0) ,

{ ... (11)
x˙n−1 = ψn−1 (t) xnu0 + ∆fn−1 (t, x0∼n, u0) ,
x˙n = ψn (t) u + ∆fn (t, x0∼n, u0) ,

where ψ0 (t), ∆f0 (t, x), ψi (t), and ∆fi (t, x0∼n, u0) , i = 1, 2, . . ., n represent the system uncertainties
satisfying certain conditions. We point out that similar uncertainties can also be added to the model
(6), and the corresponding problem of robust stabilization can be also solved with the proposed FAS
approach (see [37,39,51]).

## [121] `scis_2024_chained1` (PDF p.9, L607)

Remark 2. Once a state feedback controller u = u (x0, x1∼n, t) to the above problem is found, a state
feedback controller for system (6) is obtained, under x0 (0) ≠ 0, as

u0 = −βx0,
{ (31)
u = u (x0∼n, t) .

As we will soon find that, when the functions ϕi (·) and ψi (·) , i = 1, 2, . . ., n − 1 are not time-varying,
the control u (x0∼n, t) is also not time-varying. In this case, the above controller (31) turns out to be a
time-invariant state feedback controller for system (6).
To conclude this subsection, let us finally point out that the requirement of x0 (0) ≠ 0 is not a crucial
restriction. Anyhow, to get rid of such a restriction, the idea of [22] can be adopted, and eventually a
time-varying continuous state feedback controller can be designed.

## [122] `scis_2024_chained1` (PDF p.11, L693)

Remark 3. Due to (25), the transformation (32) can be rewritten as

xn−i+1 eβ(n−i)t
zi = n−i = n−i xn−i+1, i = 1, 2, . . ., n, (42)
x0 x0 (0)

which is clearly a differentiable homeomorphism between z1∼n and x1∼n when x0 (0) is taken differently
from zero. Therefore, a stabilizing controller for system (28) can be immediately obtained via (42) when
a stabilizing controller for system (33) is designed.
Corresponding to Assumption A2 on the series of functions ψi (x0, xi+1∼n, t) , i = 1, 2, . . . , n − 1, we
have the following assumption on the functions hi (x0, z1∼i, t) , i = 1, 2, . . ., n − 1.

## [123] `scis_2024_chained1` (PDF p.11, L711)

Remark 4. When ϕi (·) and ψi (·) , i = 1, 2, . . . , n−1 are absent, the transformed system (39) is a time-
invariant linear controllable system, based on which the control u can then be easily designed as done
in [12]. However, when these functions are indeed present, the linear system design approach proposed
in [12] is no longer valid since the corresponding system (39) is no longer a constant linear one.

## [124] `scis_2024_chained1` (PDF p.14, L907)

Remark 5. Since the stabilizing controller (59) is designed via the FAS model (51), it technically
depends on the term z(0∼n−1). This often gives the reader the wrong impression that the controller is
relies on the high-order derivatives of the system variables and is thus difficult to apply due to problems
of measuring and implementing the derivative signals. While as a matter of fact, this is not the case.
When system (33) is transformed into FAS (51), as long as the state vector z1∼n of the original system

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:15

(33) is known, the derivative term z1(0∼n−1) = z(0∼n−1) can be immediately expressed by z1∼n via the
transformation (50). We do not really need to measure these high-order derivatives and implement them
practically, but instead, we use the measured state information z1∼n of the original system (33).
In Section 5, let us examine an important special case.

## [125] `scis_2024_chained1` (PDF p.16, L999)

Remark 6. Once z and ˙z are obtained, in view of (69), the variables z1 and z2 can be immediately
given by
z1 = z,
{ 1 (73)
z2 = h(x0,z1,t) [ ˙z − g (x0, z1, t)] .

Since bi, i = 0, 1 are positive, both z = z1 and ˙z converge to zero exponentially. Furthermore, since

g (x0, z1, t) = [β + ϕ (x0, x2, t)] z1 → 0,

from (73) we clearly have limt→∞ z1∼2 = 0.

## [126] `scis_2024_chained1` (PDF p.20, L1263)

Remark 7. In this section, we have given, for the case of n = 2, an explicit solution to the stabilizing
controller for the original system (6). However, to derive an explicit solution for a larger n is, although
theoretically feasible, practically very difficult. The main point is, for the case of n ⩾ 3, one may simply
use the general solution, that is, the implicit solution given by (59), with variables z1(0∼n−1) and z1∼n
being produced by the transformations (50) and (32), respectively.

## [127] `scis_2024_chained2` (PDF p.4, L274)

Remark 1. In [1], several extensions of the above model (1) have also been given. These include the
locally normal systems, sub-normal systems, the multivariable cases, and the time-delay cases. The time-
delay cases also include the multiple time-delay case and the distributed time-delay case. Furthermore,
adding three sets of system uncertainties, ∆ ˆϕi (·) , ∆ ψˆi (·) , i = 1, 2, . . ., n − 1, and ∆fi (x0∼n, u0, t) ,
i = 0, 1, . . . , n − 1, to the model (1), gives the following uncertain system:

x˙0 = u0,
x˙1 = u + ∆f0 (x0∼n, u0, t) ,
x˙2 = x2 [ ˆϕ1 (·) + ∆ ˆϕ1 (·)] + ρ1x1[ ψˆ1 (·) + ∆ ψˆ1 (·)] + ∆f1 (x0∼n, u0, t) ,
(7)
{x˙3 = x3 [ ˆϕ2 (·) + ∆ ˆϕ2 (·)] + ρ2x2[ ψˆ2 (·) + ∆ ψˆ2 (·)] + ∆f2 (x0∼n, u0, t) ,

...
x˙n = xn [ ˆϕn−1 (·) + ∆ ˆϕn−1 (·)] + ρn−1xn−1[ ψˆn−1 (·) + ∆ ψˆn−1 (·)] + ∆fn−1 (x0∼n, u0, t) .

Robust stabilization of the above system can also be solved with the proposed FAS approach (under
consideration).

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:5

## [128] `scis_2024_chained2` (PDF p.5, L328)

Remark 2. The above treatment also has the ability to decouple any constant disturbances in the first
subsystem (8). Specifically, when the subsystem (8) is replaced with

x˙0 = u0 + d, (14)

where d is a constant disturbance, after differentiating, the same system (10) is obtained. Hence, with
the above controller (12), any constant disturbance d in the subsystem (14) is automatically decoupled.
Regarding the response of the above system (13), we have the following result [44].

## [129] `scis_2024_chained2` (PDF p.11, L693)

Remark 3. As pointed out in [1], the above Problem 2 can be indeed solved by applying the well-
known backstepping technique. However, as it is well-known, the method of backstepping suffers from the
serious problem of “complexity explosion”, which renders the application of the method of backstepping
extremely difficult or even impossible when the dimension of the system is large. Furthermore, compared
with the FAS approach given in Section 5, the method of backstepping may have two drawbacks:
(1) It is not guaranteed that a UGE stable closed-loop system can be always obtained as the UGE
stabilizability of system (27) requires UGE stabilization of SFS (54);
(2) It does not always provide a linear closed-loop system like the FAS approach does.

## [130] `scis_2024_chained2` (PDF p.11, L701)

Remark 4. Please note that, although η0 is an initial value of system (10), relative to the original
Problem 1, it is only an external design parameter. Hence it can be allowed to be set to any desired
value. From this point of view, choosing η0 = −βζ0 may just sufficiently and perfectly solve the problem
in the above sense of converting the problem into Problem 2. However, as an initial value of system (10),
after all, η0 may affect the response of system (10), that is, x0 (t) and u0 (t) , and hence that of the whole
system.
Owing to the above Remark 4, let us now also give a treatment for the case of η0 ≠ −βζ0, which will
produce a continuous controller.

## [131] `tcyb_2023_robustdelay` (PDF p.3, L404)

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

B. Type I Systems
It is well known that a stabilizable linear system can be
decomposed into a controllable subsystem and a stable uncon-
trollable subsystem. A similar fact holds also for nonlinear
systems.
According to [34], nonlinear (affine) systems which are
not completely controllable generally fall into two main cate-
gories, one is the type of subcontrollable systems or sub-FASs
in which the full-actuation assumption is not met completely
but partially, and the other is the type I system in the following
form:

xk(μk)|k=1∼η = f˜(xk(0∼μk−1)|k=1∼η, ζX, ζu, zk(0∼γk−1)|k=1∼ξ, ζZ, t)

+ B˜(xk(0∼μk−1)|k=1∼η, ζX, ζu, zk(0∼γk−1)|k=1∼ξ, ζZ, t)u
(9)
zk(γk)|k=1∼ξ = ˜g(zk(0∼γk−1)|k=1∼ξ, ζZ, t) (10)

where γk, k = 1, 2, . . . , ξ, are a set of positive integers, zk ∈
ℝlk, k = 1, 2, . . . , ξ, are a set of vectors of proper dimensions,
ζX is given by (4), while ζZ is given by

⎡ zk(0∼γk−1)|k=1∼ξ(t − τz1(t)) ⎤
zk(0∼γk−1)|k=1∼ξ(t − τz2(t))
ζZ ≜ (11)
⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎦
zk(0∼γk−1)|k=1∼ξ t − τzγ (t)
( )
with τzi(t), i = 1, 2, . . . , γ, being a group of positive scalar
functions representing the time delays in the system, f˜(·) and
g˜(·) are two nonlinear vector functions, while the other vari-
ables are as stated before. It is required that zk(0∼γk−1)|k=1∼ξ
and xk(0∼μk−1)|k=1∼η are independent from each other. Under
this requirement, the extra subsystem (10) is obviously an
isolated unforced one.
The stability of the subsystem (10), when it is nonlinear,
is complicated. Note that a system in the form of (10) can

## [132] `tcyb_2023_robustdelay` (PDF p.6, L769)

Remark 2: In the special case that the functions f˜(·) and
B˜(·) are independent on (zk(0∼γk−1)|k=1∼ξ, ζZ), instead of the
full-state feedback controller (21), the following partial-state
feedback controller can be considered:

u = ˜α(xk(0∼μk−1)|k=1∼η, ζX, ζu, t). (32)

Similarly, in the special case that the functions f(·) and B(·)
are independent on (z(0∼m−1), ζz), instead of the full-state
feedback controller (23), the following partial-state feedback
controller can be considered:

u = α(x(0∼n−1), ζx, ζu, t). (33)

These two cases will be treated in Section VI-A.

## [133] `tcyb_2023_robustdelay` (PDF p.7, L878)

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

B. Case of Multiorder FASs
Let [Ai]0∼μi−1 ∈ ℝri×riμi, i = 1, 2, . . . , η, be a set of given
matrices satisfying
μ
Reλj(Φ([Ai]0∼μi−1)) ≤ −2 (44)
j = 1, 2, . . . , μiri,i = 1, 2, . . . , η.

Then, it follows from Lemma 3 again that there exists a set
of positive-definite matrices:

Pi ≜ P([Ai]0∼μi−1), i = 1, 2, . . . , η

satisfying

ΦT([Ai]0∼μi−1)Pi + PiΦ([Ai]0∼μi−1) ≤ −μPi
i = 1, 2, . . . , η. (45)

Then, following the procedure given in Section V-A, we can
define the matrices:

PLi ≜ PL([Ai]0∼μi−1), i = 1, 2, . . . , η.

Based on the defined matrices PLi, i = 1, 2, . . . , η, the fol-
lowing controller for the uncertain multiorder FAS in (17) can
be designed:

⎧u = −B˜−1(·)(f˜(·) + u∗)

⎪⎪⎪⎪⎪⎪⎨ ⎡u∗1⎤
u∗ = u∗2 , u∗i = [Ai]0∼μi−1+Θi xi(0∼μi−1) (46)
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ( )
⎪⎪⎪⎪⎪⎪⎩ u∗η

with

⎧Θi = 1εσ2 1(PLi)ϑiPTLi
⎪⎨ϑi = σmax2min(PLi)ρ ˜i(·) + 12σ˜i 2(·) (47)
i = 1, 2, . . . , η
⎪⎩
where ε is a positive number less than 1.

Substituting the above control law (46) into the FAS in (17)
gives the following closed-loop system:

xi(μi) = −[Ai]0∼μi−1xi(0∼μi−1) + φi(·) + h˜i(·) (48)
i = 1, 2, . . . , η

where

φi(·) = −Θixk(0∼μk−1) + Δf˜i(·), i = 1, 2, . . . , η.

The closed-loop system (48) can be written in the following
state-space form:

## [134] `tcyb_2023_robustdelay` (PDF p.8, L980)

Remark 4: The above design is called the decoupled design
since η number of decoupled subsystems (with respect to the
internal variables) are obtained in the closed-loop system (48).
In [34], a coupled design for controllers of nonlinear FASs is
also given, and we point out that the above approach can also
be extended to the coupled design case, in which a whole cou-
pled closed-loop system with an external input zk(0∼γk−1)|k=1∼ξ
is derived (see [35], [41]).

## [135] `tcyb_2023_robustdelay` (PDF p.8, L988)

Remark 5: In [26] and [30], [31], [32], [33], [34], nonlin-
ear FASs in nonaffine form are also introduced, and they are
then generalized to the discrete-time case [37], the discrete-
time delay system case [38], [39], and also the continuous-time
delay system case [40], [41]. We point out that the affine FAS
in the uncertain type I system proposed in this article can

also be substituted by a general nonaffine FAS, and the cor-
responding robust stabilization problem can be also similarly
treated.

## [136] `tcyb_2023_robustdelay` (PDF p.8, L1050)

Remark 6: The function Δf(·) in system (50) may be also
looked upon as a known function satisfying condition (51). In
this case, the above system (50) is no longer uncertain, but
a deterministic one. The problem turns to be a stabilization

one for the deterministic type I system (50) using output
feedback, with the output variables being the partial states
(x(0∼n−1), ζx). It is clearly seen from the above results that
this stabilization problem is solvable as long as Δf(·) satisfies
the condition (51), which divides out the information about
x(0∼n−1) and ζx, that is used for feedback.

B. Case of Perturbed B(·) Matrix
For simplicity and space limit, here we only consider the
single-order case, where the perturbed FAS is given by

x(n) = f(·) + Δf(·) + [B(·) + ΔB(·)]u + h(z0∼m−1) (54)

where the matrix B(·) and the function Δf(·) still satisfy
Assumptions B2 and B3, and the function h(z0∼m−1) satis-
fies Assumption B4. In addition, ΔB(·) is a perturbed matrix
satisfying the following two assumptions.

## [137] `tcyb_2023_subfas` (PDF p.6, L678)

Remark 1: In many cases, the matrix B(·, t) involves only a
few of the elements in the generalized state vector x(0∼n−1)(t−
σj(t))|j=1∼γ or xk(0∼μk−1)(t − σj(t) )|k=1∼η, j=1∼γ , while the
function of the structural distribution matrix T allows us to
“recognize” those variables really affecting the matrix B(·, t).
As a consequence, instead of considering a singular set in
ℝγ nr, we can now consider one in a much smaller dimension
space ℝm. In the extreme case that B(·, t) is affected by only
a single element of x(0∼n−1)(t −σj(t) )|j=1∼γ or xk(0∼μk−1)(t −
σj(t))|k=1∼η,j=1∼γ , the matrix T becomes only a row vector,
and now the singular set is a subset in the real axis.

## [138] `tcyb_2023_subfas` (PDF p.9, L1157)

Remark 2: Let us mention a method for solving the param-
eters Ψi, i = 1 ∼ l. Without loss of generality, let us only
demonstrate this with the solution of Ψ1. Define

A = blockdiag(Φk(00∼μk−1), k = 1 ∼ q1)
B = blockdiag(Bck, k = 1 ∼ q1)

where

Bck = 0 0 · · · Irk T, k = 1 ∼ q1.
[ ]
Then, it can be easily verified that the system matrix ΦE in
the state-space system (50) is given by

ΦE = A − BΨ1.

Therefore, the solution of Ψ1 is converted into a problem of
eigenstructure assignment, for which a basic complete para-
metric eigenstructure assignment result is available (see [50]).
The degrees of freedom provided in the parametric approach
can be properly utilized to achieve the additional performance
of the designed system.
For proper detailed examples demonstrating the above the-
ory of substabilization of a multiorder FAS, please refer to [39]
and [59].

C. Relation to Lyapunov Stabilization
Substabilization may not be stabilization in the Lyapunov
sense, but it has a close relation with stabilization in the
Lyapunov sense.

## [139] `tcyb_2024_overview` (PDF p.4, L433)

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

## [140] `tcyb_2024_overview` (PDF p.5, L571)

Remark 2: Some readers who are not yet familiar with the
FAS approach might be mistaken that the FAS approach is
nothing but feedback linearization. The above result can only
tell that feedback linearization is a special case of the FAS
approach, but not vice versa since the FAS approach also
treats systems not in the state-space form, and can solve the
stabilization of systems which have already been proven to
be not feedback linearizable. Indeed, the FAS approach really
does much more than the feedback linearization technique.

C. Strict-Feedback Systems
A typical nonlinear SFS is in the following form:

x˙1 = f1(x1) + G1(x1)x2
x˙2 = f2(x1, x2) + G2(x1, x2)x3
{ ...
x˙n−1 = fn−1(x1, . . . , xn−1) + Gn−1(x1, . . . , xn−1)xn
x˙n = fn(x1, . . . , xn) + Gn(x1, . . . , xn)u,
(15)
where xi ∈ ℝri, i = 1, 2, . . . , n, are the state vectors, u ∈ ℝr
is the control input, fi(x1∼i) ∈ ℝri and Gi(x1∼i) ∈ ℝri×ri+1,
i = 1, 2, . . . , n, are sufficiently smooth vector functions
and matrix functions, respectively. Furthermore, Gi(x1∼i) is
nonsingular for all xi ∈ ℝri, i = 1, 2, . . . , n.
The above SFS has been shown to be equivalent to a FAS.
Particularly,
1) it has been shown in [6] that, in the case of ri = r, i =
1, 2, . . . , n, the SFS (15) can be equivalently converted
into a single-order global FAS in the form of (1); and
2) it has been shown in [26] (see also [27] for the discrete-
time case) that, in the case of ri+1 ≥ ri, i = 1, 2, . . . , n,
the SFS (15) can be equivalently converted into a multi-
order global FAS in the form of (2).
More concretely, the f and B terms in FASs (1) or (2)
are finally obtained by iterative formulas using fi(x1∼i) and
Gi(x1∼i), i = 1, 2, . . . , n. Moreover, a discrete-time version
of similar results can be found in [14], and generalization of
the results to SFSs with time-varying delays can be found in
[16], [17].

D. Flat Systems
Consider the nonlinear system (13) again. It is well-known
that it is called (differentially) flat (see [28], [29]) if there
exists a so-called flat output

y = h(x, u(0∼p)), (16)

of appropriate dimension, such that

x = φ(y(0∼q−1)), (17)

u = ψ(y(0∼q)), (18)

where φ (·) and ψ (·) are two proper functions. Please note that
the highest-order derivative of y in (17) is of one order less
than that in (18) because of the dynamical system equation
(13).
Next, let us further express (17) in the following more
detailed form:

x = φ(yk(0∼µk−1)|k=1∼η), (19)

which suggests

y = yk(0∼µk−1)|k=1∼η, (20)

## [141] `tcyb_2024_overview` (PDF p.9, L1110)

Remark 3: With the above preparations, it is easily under-
stood that control of a continuous-time system, whether linear
or nonlinear, whether time-varying or time-invariant, whether
possessing time delays or not, is ultimately reduced to the
solution to the elementary problem, i.e., Problem 1. For the
case of discrete-time systems (see [14]), a similar conclusion
can be obtained, in which the matrix F needs to be Schur
instead of Hurwitz.

## [142] `tcyb_2024_overview` (PDF p.9, L1118)

Remark 4: It is often seen that one class of problems is
converted into another one in science research, but the above
particular conversion is special in two aspects: 1) the scope
of the problems can be converted is astonishingly wide, as
we have seen; 2) the finally converted problem turns out to
be not a class, but a single one, namely, the eigenstructure
assignment of a specific pair of matrices (Φ (00∼n−1) , Bc),
which is determined by only two parameters n and r.

E. A Basic Procedure for FAS Approach
Having seen the advantages of the FAS models in stabi-
lization in the above subsections, we can now give a basic
procedure for the FAS approach (see Fig. 2).
Suppose that we have got a so-called original system whose
model is derived by certain physical laws. To realize the
stabilization of this system, we carry out the following steps.
Step 1 find a homeomorphism φ under which the original
physical system is converted into a FAS or a sub-
FAS;
Step 2 design the standard controller in the form of (45) or
(49) for the obtained FAS or sub-FAS, and obtain a
(partially) linear closed-loop system;

Step 3 based on the controller obtained in Step 2 and the
homeomorphism φ−1, obtain the controller for the
original system;
Step 4 for the (partially) linear closed-loop system obtained
in Step 2, obtain its analytical expression for the
response starting from the RoEA;
Step 5 based on the response obtained in Step 4 and the
homeomorphism φ−1, obtain and analyze the re-
sponse of the closed-loop system corresponding to
the original system.
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
To conclude this section, let us point out that, In Fig. 2, the
dotted line with a single arrow represents a route which is hard
to complete, and the dotted line with two arrows represents a
route which is unnecessary to be carried out.

F. Finite-time sub-stabilization
A great advantage of the FAS approach is that the full-
actuation property of the FAS model allows us to cancel any

## [143] `tcyb_2024_overview` (PDF p.12, L1452)

Remark 5: For convenience, in this section, we have only
treated the case that the considered deterministic system (1)
and the uncertain system (71) are global FASs. As a matter of
fact, all the treatments can be extended to the case where the
considered deterministic system (1) and the uncertain system
(71) are sub-FASs. What is more, it is the latter case that really
reveals the advantage and power of the FAS approach.

## [144] `tcyb_2024_overview` (PDF p.17, L2001)

Remark 6: In addition, there have been numerous researches
on robust control based on the FAS approach. These involve
robust stabilization of time-varying nonlinear systems with
time-varying delays [31], robust high-order backstepping [7],
[125], robust adaptive control [9], robust command filtered
backstepping design for SFSs [126], robust adaptive dynamic
surface control of high-order SFSs [56], robust fault-tolerant
stabilization of uncertain high-order FASs with actuator faults
[95], robust control of impulsive systems [119], robust tracking
control [48], [74], [75], [78], and robust control of aircraft and
quadrotors [127]–[129].

## [145] `tcyb_2024_overview` (PDF p.18, L2198)

Remark 7: Except for the above several main categories, the
FAS approach has also been applied in many other practical
systems. Examples include, but are not limited to, under-
actuated mechanical systems [84], [87], inverted pendulum

systems [77], [112], intelligent vehicle systems [165], [166],
heterogeneous MASs [102], [167], thermoacoustic unstable
systems in Rijke tube [49], [71], [168], civil turbofan engines
[169], proton exchange membrane fuel cell air feed systems
[170], cold strip rolling mill systems [171], overhead cranes
[172], and so on.

## [146] `ucfas_2025_part1` (PDF p.5, L480)

Remark 3.1: Paying attention to only introducing the
basic idea and procedure, in this series of papers, we
have only demonstrated the presented approach with
the above FASs without time delays, while the FAS
approach has already been generalised to time-delay
systems (Duan, 2022a, 2022b, 2023b, 2023c, 2023d).
As a matter of fact, the work in Duan (2023e) really
presents the sub-stabilisation results for the gen-
eral nonlinear time-varying FASs with time-varying
delays. Furthermore, when nonlinear uncertainties,
unknown parameters and disturbances are added to
these basic FASs, robust and adaptive control as well as
disturbance rejection control have been investigated in
Duan (2021b, 2021d, 2021e, 2021g).

## [147] `ucfas_2025_part1` (PDF p.6, L574)

Remark 4.1: Let us point out that often a strongly
UC-FAS can be converted into a weakly UC-FAS by
certain control transformations. Examples support-
ing this point can be found in the Section 4.3.1 of
Duan (2025a), and the Section 4.1 of Duan (2025b).

## [148] `ucfas_2025_part1` (PDF p.9, L959)

Remark 5.1: Examples 4.1 and 5.1 indicate that there
indeed exist systems which cannot be converted into
global FASs or sub-FASs, but UC-FASs. In general,
once a model for a system, which is established using
mechanism modelling or system identification, has
been converted into a UC-FAS, then a substabilising
controller can be easily designed, as seen in the sec-
ond part (Duan, 2025a). We emphasise again that the
essence of the process of converting a system into
a UC-FAS is to find a homeomorphism that trans-
forms the system into a UC-FAS. Unfortunately, the
process of finding the homeomorphism is often case-
dependent, as demonstrated by these two examples.

## [149] `ucfas_2025_part1` (PDF p.10, L1094)

Remark 6.1: The commonly required typical condi-
tions (69) and (70) can be actually broken by the FAS
approach. When the determinant condition (69) and
the rank condition (70) do not hold on the whole state-
space, but only on a subset of the corresponding state
space, system (68) is no longer an SFS, but a sub-SFS,
as defined in Duan (2024a). The conclusions in this
subsection can be generalised to the case of sub-SFSs
(Duan, 2024b).

## [150] `ucfas_2025_part1` (PDF p.10, L1104)

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

## [151] `ucfas_2025_part1` (PDF p.11, L1123)

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

## [152] `ucfas_2025_part2` (PDF p.6, L551)

Remark 2.1: It is seen that sub-stabilisation requires
the system initial values to be chosen from the RoEA.
Generally speaking, this is not a strict restriction due
to the following aspects:

(1) In most applications, the designed RoEA is large
enough for practical initial value choices.
(2) In many cases, the set of allowable initial values
can be made much larger by moving the RoEAs
through applying some coordinate system trans-
lations to the original system (see the Remark 5.1
in Duan (2025a)).
(3) In those cases where the initial value must be
chosen outside the RoEA, a so-called problem
of state regional transfer needs to be solved in
order to find a pre-controller to drive the tra-
jectory of the system into the RoEA first, and
then let the sub-stabilising controller take over
(Duan, 2023a, 2023e, 2024c). Since the RoEA
is usually a very large region, the state regional
transfer problem is generally much easier to han-
dle, compared with the Lyapunov stabilisation
problem in which all trajectories from a neighbor-
hood of the origin must be transferred to a unique
point, the origin.

## [153] `ucfas_2025_part2` (PDF p.6, L577)

Remark 2.2: The type of closed-loop stability resulted
in by the above sub-stabilisation is called sub-stability
(see Duan, 2023e), which differs from the well-
known Lyapunov stability in the following aspects
(Duan, 2024c):

(1) The region of attraction for Lyapunov stability is
a simply-connected region containing the origin

as an interior point, and is usually regarded as
a ball centred at the origin, while the RoEA of
sub-stability may be much more complicated. It
may not be convex, or may not even be simply-
connected.
(2) Noting that only when the RoEA contains the
origin as an interior point, we can construct a
ball centred at the origin within the RoEA, which
serves as a region of attraction in the Lyapunov
sense. With this observation, we can immediately
conclude that sub-stability implies local Lyapunov
stability when the RoEA contains the origin as an
interior point.
(3) Clearly, in the case that the RoEA contains the
origin as an exterior point, the converted FAS
can not be stabilised by the proposed typical con-
troller. However, when the RoEA contains the ori-
gin as a boundary point, the converted FAS can
be sub-stabilised. As a matter of fact, the latter
case contains the so-called nonholonomic sys-
tems, and many difficult examples of nonlinear
systems belong to this category.

Furthermore, as stated in the Remark 3.1 in
Duan (2025b), the presented approach can also be gen-
eralised to time-delay systems (Duan, 2022b, 2022c,
2023b, 2023c, 2023d).

## [154] `ucfas_2025_part2` (PDF p.15, L1456)

Remark 4.1: Let us point out that all these five models
with application backgrounds can also be generalised
by adding function ϕ(·) to a certain equation. Fur-
thermore, it can also be proven that these generalised
models are also equivalent to system S1.

## [155] `ucfas_2025_part3` (PDF p.11, L1097)

Remark 5.1: It might be mistaken that the RoEA Rinpv
is a bit small and that may reduce the effect of this
design. The following comments assure that this worry
is unnecessary:

(1) This region is often big enough for the system
initial value choices in practical applications.
(2) Note that, for any pair of constants d1 and d2,
under the following coordinate translation:

xp = x + d1, xd = ˙xp + d2, (87)

we still havex ¨p = u1, i.e. system (73) still keeps the
same form. Therefore, in applications any desired
initial value (x10, x20) can be actually chosen with
the help of a coordinate system translation in the
form of (87).

Design the controller for FAS (85) as

⎧
1
⎪⎪⎪⎨u2 = −
b(X0, t)
×[b0∼3z(0∼3) + f˜ (z(2∼3), X0, t)] (88)
⎪⎪⎪⎩X0 ∈ Rinpv.

We obtain the closed-loop system (66). Again the
parameters bi, i = 0, 1, 2, 3, are selected to make sys-
tem (66) stable.
To summarise, we have the following three conclu-
sions:

(1) The sub-stabilising controller for UC-FAS (77) is
given by (81) and (88). As long as the system initial
value X0 lies within the RoEA Rinpv, the designed
controller produces a closed-loop system com-
posed of linear systems (53) and (66).
(2) Once state responses x(0∼1) and z(0∼3) of UC-
FAS (77) are obtained, y(0∼1) can be obtained
by (79) and (80). However, it needs to be noted
that the convergence rate of system (66) must be
made large enough so as to let y(0∼1) and u2 con-
verge to zero exponentially.
(3) Once the state responses of system (73), i.e. x(0∼1),
y(0∼1), and z(0∼1), are all obtained, the original
states q(0∼1), q(0∼1), and γ(0∼2)of the PVTOL sys-
1 2
tem (3) can be obtained via the two state transfor-
mations (68) and (71). Simultaneously, when u1
and u2 are obtained, the original control signals F1
and F2 can be obtained via transformations (69)
and (72).

# Sorted Corollary Corpus Across 32 Duan First-Author Papers + Volume I (65 items)

## [1] `aas_2020_part1` (PDF p.9, L967)

推论 1. 当 E = In 时, 问题 ESA 有解当且仅
当 F ∈ F∆, 并且在这种情况下, 所有矩阵 V (Z, F)
由式 (55) 给出, 而

K = ZFmV −1(Z, F) (61)

其中 Z ∈ Rn×mn 为满足

det V (Z, F) ≠ 0 (62)

的参数矩阵.

## [2] `aas_2020_part1` (PDF p.10, L1034)

推论 2. 当 E = In 时, F 非空当且仅当矩阵
F ∈ Rnc×nc 具有形如式 (64) 的若当标准型, 其中
任意两个 Ji ∈ Cn×n, i ∈ Nm−2 可交换且不具有共
同的特征值.

## [3] `aas_2020_part3` (PDF p.5, L505)

推论 1. 单输入单输出线性系统 (5) 能观的充
要条件是其等价于下述高阶全量测系统
n−1 n−1
z(n) + αiz(i) = βiu(i)
i=0 i=0 (27)
y = z

其中 αi, βi, i = 0, 1, · · · , n−1, 由式 (6), (7) 给出.

## [4] `aas_2020_part3` (PDF p.6, L668)

推论 2. 设 rankC = m, 则多输入多输出线性
定常系统 (16) 能观的充要条件是其等价于如下高阶
全量测系统
µ µ−1
Aiz(i) = Biu(i)
i=0 i=0 (40)
y = Cz

9 期

其中 z ∈ Rm,

b1k
Ak = αijk ∈ Rm×m, Bk = ... ∈ Rm×r

bmk
k = 0, 1, · · · , µ = max {µi, i = 1, 2, · · · , m}
(41)

1 0 · · · 0

c21 1 ... ...
C = (42)
... ... ... 0

cm1 · · · cm,m−1 1

而 µi, i = 1, 2, · · · , m, cij, j = 1, 2, · · · , i; i =
1, 2, · · · , m, 如前所述.
众所周知, 控制系统的能控、能观性是对于状态
空间描述的一阶系统定义的. 高阶系统没有直接的
能控、能观性定义. 文献 [1] 建立了控制系统的能控
性和高阶系统的全驱性的关系, 定义了控制系统的
完全能控性. 受上述定理 1 和定理 2 的启发, 我们
亦可给出高阶非线性系统的能观性定义.
现在考虑如下一般的动态系统

F(x,x, ˙ · · · , x(v); u,u, ˙ · · · , u(l); t) = 0
y = G(x,x, · · · , x(v)) (43)
˙

其中 x、y ∈ Rm 和 u ∈ Rr 分别为系统的状态、输
出和控制输入, F(·) 和 G(·) 为满足适当条件的向量
函数, v 和 l 为两个正整数, 一般情况下有 l ≤ v.

## [5] `fasta_2026_roea` (PDF p.4, L510)

Corollary 1. Under Condition 1, the infinite constraint set
defining R can be reduced to a finite intersection:
p
R = Ri,
i=1

where each Ri is determined in (19).
The above result converts the infinite time RoEA charac-
terization problem into a finite dimensional one. Next, we
reconsider the characterization of the RoEAs for the above
motivating examples.

## [6] `ijss_2021_part2` (PDF p.9, L900)

Corollary 3.3: If det G1 ≠ 0, and for x1, x2 ∈ ℝr, and
ζ ∈ ℝm there holds

det G2(x1(0∼∼12), x2(0∼1), ζ, t) ≠ 0,

then, in the case of n = 2, the SFS (11) can be trans-
formed into the following HOFA model

z(4) = h(z(0∼3), ζ, t) + L(z(0∼3), ζ, t)u, (39)

with

L(z(0∼3), ζ, t) = G1G2(x1(0∼2), x2(0∼1), ζ, t), (40)

and

(0∼3) [ f¨1(z(0∼1), ζ, t) ]
h(z , ζ, t) = [I G1] (0∼2) (0∼1) ,
f2(x1 , x2 , ζ, t)
(41)
where L0 = I, and in (40)–(41) the x2 and its derivative
are given and determined by

x2 = G−11[z¨ − f1(z(0∼1), ζ, t)].

## [7] `ijss_2021_part2` (PDF p.10, L1002)

Corollary 3.5: If det G1G2 ≠ 0, and for all xk ∈
ℝr, k = 1, 2, 3, and ζ ∈ ℝm, there holds

det G3(xi(0∼mi)|i=1∼2, x3(0∼m3−1), ζ, t) ≠ 0, ∀ t ≥ 0,

then, for the case of n = 3, the SFS (18) can be equiva-
lently turned into the following HOFA model

z(p) = h(z(0∼p−1), ζ, t) + L(z(0∼p−1), ζ, t)u, (50)

with p = m1 + m2 + m3, and

L(z(0∼p−1), ζ, t)

= G1G2G3(xi(0∼mi)|i=1∼2, x3(0∼m3−1), ζ, t), (51)

and

h(z(0∼p−1), ζ, t)

= [I G1 G1G2]

f(m2+m3)(z(0∼m1−1), ζ, t)
⎡ 1 ⎤
× f(m3)(x(0∼m1), x(0∼m2−1), ζ, t) , (52)
2 1 2
⎢⎣f3(xi(0∼mi)|i=1∼2, x3(0∼m3−1), ζ, t)⎥⎦

where in (51)–(52) the x2, x3 and their derivatives are
given and determined by

x2 = G−11[z(m1) − f1(z(0∼m1−1), ζ, t)]
{x3 = G−21G−11[z(p2) − h2(z(0∼p2−1), ζ, t)], (53)

with

h2(z(0∼p2−1), ζ, t)

f(m2)(z(0∼m1−1), ζ, t)
= [I G1][ 1(0∼m1) (0∼m2−1) ]. (54)
f2(x1 , x2 , ζ, t)

## [8] `ijss_2022_part10` (PDF p.14, L1571)

Corollary 6.3: Let system (57) be locally feedback lin-
earisable at (x0, u0) via the feedback (61)–(62). Then
the system (57) is equivalent to both a step forward
HOFA system in the affine form of (31) within a neigh-
bourhood of (x0, u0), and a step backward HOFA system
in the affine form of (32) within a neighbourhood of
(x0, u0).

The proof of the above corollary is also provided in
the appendix.

## [9] `ijss_2022_part8` (PDF p.7, L732)

Corollary 3.1: Let Assumption A1 be met, and Q, S ∈
ℝm×m be semi-positive definite, and R ∈ ℝr×r be pos-
itive definite. Then, for the system (3) with the output
Equation (5), a feedback controller in the form of (8),
which minimises the index J2, is given by

⎧ u = −B−1 xk(0∼μk−1)|k=1∼η, ζ, t)
(
⎪⎪⎨ ×[f (xk(0∼μk−1)|k=1∼η, ζ, t) − v] (27)

v = −R−1BTEP (t) xk(0∼μk−1)|k=1∼η
⎪⎪⎩

where P(t) ∈ ℝκ×κ is the solution to the differential
Riccati Equation (20) subject to the final value condition
(21).

To end this section, let us make the following
remark.

## [10] `ijss_2024_underactuated4` (PDF p.7, L750)

Corollary 3.1: Assume m = n, and let Assumption A1
be met. Then

(1) under the following diffeomorphism (x, y) → (z,z ˙):

x = h (z,z ˙, t)
{ (23)
y = z,

system (10) is equivalent to the following sub-FAS:

z¨ = f (z,z ˙, t) + B (z,z ˙, t) u, (24)

where
∂g
f (z,z ˙, t) = Gy (h (z,z ˙, t) , z, t)z ˙ + , (25)
∂t

B (z,z ˙, t) = Gx (h (z,z ˙, t) , z, t) ; (26)

(2) the feasible set of sub-FAS (24) is Ωo = Ω1 ∩ Ωo2,
with

Ωo2 = x, y det Gx h x, y, t , x, t ≠ 0 or ∞,
{( )|| ( ( ) )
x, y ∈ ℝn, and t ≥ 0 .
}

## [11] `ijss_2024_underactuated4` (PDF p.11, L1140)

Corollary 4.1: Assume m = n. Let Assumption A2 be
met. Then

(1) under the following diffeomorphism (x1, x2, x3) →
(x, y,y ˙) :

⎧x1 = x
⎨x2 = h(x, y,y ˙, t) (54)
x3 = y,
⎩
system (39) is equivalent to the following sub-FAS:

[x˙] = [ 0 ]
y¨ f (x, y,y ˙, t)

In 0 u1
+ [ ] [ ],
B1 x, y,y ˙, t B2 x, y,y ˙, t u2
( ) ( )
(55)

where

f x, y,y ˙, t = G3 x, h x, y,y ˙, t , y, t y ˙
( ) ( ( ) )
+ Gt x, y,y ˙, t , (56)
( )
B1 x, y,y ˙, t = G1 x, y,y ˙, t , (57)
( ) ( )
B2 x, y,y ˙, t = G2 x, y,y ˙, t ; (58)
( ) ( )

(2) the set of feasibility of the above sub-FAS (55) is
given by Uo = U1 ∩ U2o, with

U2o = x, y,y ˙ | det B2 x, y,y ˙, t ≠ 0 or ∞,
{( ) ( )
x ∈ ℝn , y,y ˙ ∈ ℝm , and t ≥ 0 .
}

## [12] `ijss_2024_underactuated4` (PDF p.15, L1758)

Corollary 5.1: Let Assumption A3 be met. Then,

(1) under the diffeomorphism (78), UAS (74) is equiv-
alent to the following sub-FAS:

q(4) = f (q(0∼3), t) + B(q(0∼3), t)u, (108)

where f (q(0∼3), t) and B(q(0∼3), t) given by (82)
and (83), respectively, with f0(·) and B0(·) being
given by (106) and (107), respectively;
(2) the set of feasibility of sub-FAS (108) is given by
Wo = W1 ∩ W2o, with

W2o = {X|detB(X, t) ≠ 0 or ∞, X ∈ ℝ4n and t ≥ 0}.

Regarding extensions of (73), let us mention the
following nonaffine form:

⎧q¨1 = fˇ0(q1, q(20∼1), t) + Bˇ0(q1, q(20∼1), u, t)
⎨ (0∼1)
q¨2 = g (q1, q2 , t),
⎩
(109)

whereBˇ0 is a piece-wise continuous function. It can be
easily shown that a sub-FAS for system (109) is given
by

q(24) = f (q(20∼3), t) + B(q(20∼3), u, t), (110)

where f (q(20∼3), t) is given by (79), and

(0∼3) ∂g(q1, q(20∼1), t) (0∼1)
B(q2 , u, t) = Bˇ0(q1, q2 , u, t).
∂q1
(111)

In this case, the set of feasibility is still given by (84),
but with W2 being defined to be the region on which
Bˇ0(q1, q(20∼1), u, t) is a homeomorphism with respect
to u.
To finish this section, let us further give a remark.

## [13] `ijss_2024_underactuated4` (PDF p.18, L2083)

Corollary 6.1: Let Assumption A4 be met, f0(·),
B10(·) and B20(·) be given by (130)–(132). Then

(1) under the diffeomorphism (119), system (115) is
equivalently converted into the following sub-FAS:

[ ¨(x4)] = [ (0∼1)0 (0∼3) ] + B (·)[v],
y f (x , y , t) u
(133)

where

I 0
B (·) = [B1(x(0∼1), y(0∼3), t) B2(x(0∼1), y(0∼3), t)],

and f (·), B1(·), and B2(·) are given by (124)–(126),
but with f0(·), B10(·), and B20(·) defined in
(130)–(132);
(2) the set of feasibility of sub-FAS (133) is given by
Ho = H1 ∩ H2o, with

H2o = {(X, Y) |detB2(X, Y, t) ≠ 0 or ∞,

X ∈ ℝ2n, Y ∈ ℝ4m and t ≥ 0 . (134)
}

## [14] `jssc_2022_casestudy` (PDF p.8, L383)

Corollary 4.1 Let a0 and a1 be determined by (17)–(18), with α and β, α > β, being a
pair of distinct positive scalars, and the controller for the system (1) be designed as (12). Then
the region of evaporation is given, in the original (x1, x2) plane, by 𝕎 = 𝕎1 ∪ 𝕎2, with

⎧ x320 ≤ 0 ⎫
𝕎1 = ⎨(x10, x20) 3 ⎬, (25)
|||||| (1 + α) x10 + x20 ≥ 0
⎩ ⎭
⎧ x320 ≥ 0 ⎫
𝕎2 = ⎨(x10, x20) 3 ⎬, (26)
|||||| (1 + α) x10 + x20 ≤ 0
⎩ ⎭
where x10 = x1 (0) and x20 = x2 (0) are the initial values of the system (1), which is a sector
field in the initial value plane x10, x320 as shown in Figure 2.
( )

Figure 2 Region of evaporation for the original system

## [15] `jssc_2022_casestudy` (PDF p.9, L430)

Corollary 4.2 Let a0 and a1 be determined by (17)–(18), with α and β, α > β, being
a pair of distinct positive scalars, and the controller be designed as in (12) for the system (1).
Then both xi (t) , i = 1, 2, and u (t) converge to zero exponentially as long as the system initial
values are taken from the region of attraction

ℚ = ℚ1 ∪ ℚ2,

with
⎧ x320 > 0 ⎫
ℚ1 = ⎨(x10, x20) 3 ⎬, (29)
|||||| (1 + α) x10 + x20 < 0
⎩ ⎭
⎧ x320 < 0 ⎫
ℚ2 = ⎨(x10, x20) 3 ⎬. (30)
|||||| (1 + α) x10 + x20 > 0
⎩ ⎭

## [16] `jssc_2022_freq` (PDF p.4, L221)

Corollary 2.4 The linear system (1) is controllable if and only if there exists a nonsingu-
lar matrix T ∈ ℝn×n such that (Z(s), U(s)) with z ∈ ℝr given by (3), satisfies the fully actuated
PMD
P(s)Z(s) = BU(s), (7)

where P(s) ∈ ℝr×r(s) is some polynomial matrix, and B ∈ ℝr×r is a square upper triangular
matrix with diagonal elements all being 1.
It follows that the PMD (5) is under-actuated in general since Q(s) = B is not square in
general, while the PMD (7) is fully actuated. Thus, the above Corollary 2.4 and Proposition 2.1
actually provide a method for transforming the under-actuated PMD (5) into a fully actuated

## [17] `odfas_2026_part1` (PDF p.25, L2736)

Corollary 8.1. The following second-order sys-
tem

Mx ¨ + D (t) ˙x + Kx = 0, (148)

is GUE stable if

M > 0, K > 0,
D (t) + DT(t) > 0, ∀t ≥ 0.

The above corollary is a straight forward ex-
tension of a result in Duan, Xu, and Huang
(1989).

## [18] `odfas_2026_part4` (PDF p.13, L842)

Corollary 3.1. Let A0 ∈ ℝn×n be Hurwitz. Then the following system

x˙ = Rs (t) A0Rs−1(t) x, (3.6)

is uniformly asymptotically stable if Rs (t) ∈ ℝn×n is uniformly bounded and uniformly positive definite.

For convenience, we also introduce the following definition.

## [19] `odfas_2026_part4` (PDF p.15, L926)

Corollary 3.2. The following system

{x˙ = A1x + G (x, t) z
(3.12)
z˙ = A2 (t) z,

is GUA stable if

## [20] `odfas_2026_part4` (PDF p.18, L1078)

Corollary 4.1. Let A1(ϕ(0∼1)) = A1 (ϕ). Furthermore, let Assumptions A1 and Aϕ2 be met,

and Ao1 ∈ ℝr×r be an arbitrary Hurwitz matrix. Then an observer giving the estimate of q2 can be

given as follows:
{z˙ = Ao1z + ΘIa(ϕ(0∼1))y + u0
(4.14)
qˆ2 = z − (Ao1 − R (ϕ) A1 (ϕ)) y,

where

ΘIa(ϕ(0∼1)) = L˙ (ϕ) − Ao1L (ϕ) , (4.15)

L (ϕ) = Ao1 − R (ϕ) A1(ϕ) . (4.16)

The observation error e = q2 −q ˆ2 is governed by the equation (4.10).

If, further, A1(ϕ(0∼1)) = A1 is constant, the matrix ΘIa(ϕ(0∼1)) can be further reduced to

ΘIa(ϕ(0∼1)) = Ao1R (ϕ) A1 −R ˙ (ϕ) A1 − [Ao1]2 . (4.17)

## [21] `odfas_2026_part4` (PDF p.21, L1219)

Corollary 4.2. Let A1(ϕ(0∼1)) = A1 (ϕ). Furthermore, let Assumptions A1-A2, Ap1, and Aϕ2

be satisfied, and F0∼1 ∈ ℝr×2r be a matrix making Φ(F0∼1) Hurwitz. Then a GUA stabilizing output

feedback controller for system (4.4) is given in the form of

{u0 = K11 (ϕ) y + K12 (ϕ) z
z˙ = K21(ϕ(0∼1))y + K22 (ϕ) z, (4.27)

with
K11 (ϕ) = −K12 (ϕ) (Ao1 − R (ϕ) A1 (ϕ)) − F0
K12 (ϕ) = − (F1 + R (ϕ) A1 (ϕ))
{K21(ϕ(0∼1)) = ΘIa(ϕ(0∼1))+ K11 (ϕ) (4.28)

K22 (ϕ) = Ao1 + K12 (ϕ) ,

where Ao1 is an arbitrary Hurwitz matrix, and ΘIa(ϕ(0∼1)) is defined by (4.15)-(4.16), which is further

reduced to (4.17) when A1(ϕ(0∼1)) = A1 is constant.

With the help of the above two propositions, we can finally obtain the following result.

## [22] `odfas_2026_part4` (PDF p.30, L1775)

Corollary 5.1. Let A1(ϕ(0∼1)) = A1 (ϕ). Furthermore, let Assumptions A1-A2, Aϕ2, Ap1 be

met. Then an observer producing simultaneously the estimates of q2 and d is given by

z˙ = AoI(ϕ) z − ΘIb(ϕ(0∼1))y +[Ir]u0
0
{ (5.27)
[qˆ2] = z − L (ϕ) y,
dˆ

where

ΘIb(ϕ(0∼1)) = L˙ (ϕ) − AoI(ϕ) L (ϕ) , (5.28)

AoI(ϕ) , AI (ϕ) + L (ϕ) CI, (5.29)

and L (ϕ) makes AoI(ϕ (t)) uniformly asymptotically stable. Furthermore, the observation error (5.15)

is governed by the following system

e˙ = AoI(ϕ (t)) e. (5.30)

Furthermore, when Assumption Ap2 is met, L (ϕ) can be taken as

[L1M (ϕ) − A1 (ϕ)]
L (ϕ) = RE (ϕ) , (5.31)
L2M (ϕ)

with Li ∈ ℝr×r, i = 1, 2, making (5.18) Hurwitz, and the error system (5.30) becomes the uniformly

asymptotically stable system (5.25).

## [23] `odfas_2026_part4` (PDF p.33, L1950)

Corollary 5.2. Let Assumptions A1-A2, Aϕ2 and Ap1 be satisfied, F0∼1 ∈ ℝr×2r be a matrix

making Φ (F0∼1) Hurwitz, AoI(ϕ(0∼1)) be given by (5.11), and L(ϕ(0∼1)) make AoI(ϕ(0∼1)) uniformly

asymptotically stable. Then a GUA stabilizing observer-based output feedback controller for system

(5.1) is given by

u (t) = −B−1(⋅, t)(fy (⋅, t) + A0(ϕ(0∼1))y (t) − M (ϕ) u0)

{u0 = K11 (ϕ) y + K12 (ϕ) z (5.40)
z˙ = K21(ϕ(0∼1))y + K22 (ϕ) z,

with
K11 (ϕ) = −F0 − K12 (ϕ) L (ϕ)
K12 (ϕ) = −⌊F1 + R (ϕ) A1 (ϕ) R (ϕ)⌋

{K21(ϕ(0∼1)) = −[Ir](F0 + K12 (ϕ) L (ϕ)) − ΘIb(ϕ(0∼1)) (5.41)
0

K22 (ϕ) = AoI(ϕ) +[Ir]K12 (ϕ) ,
0

where ΘIb(ϕ(0∼2)) and AoI(ϕ) are given by (5.28) and (5.29), respectively. Furthermore, when As-

sumption Ap2 is met, L (ϕ) can be given by (5.31) with Li ∈ ℝr×r, i = 1, 2, making AL Hurwitz.

## [24] `odfas_2026_part4` (PDF p.40, L2269)

Corollary 6.1. Let A0(ϕ(0∼1)) = A0 (ϕ) , Assumptions A1 and Av1 be met, Ao2 ∈ ℝr×r be an

arbitrary Hurwitz matrix, and define

L (ϕ) = Ao2A−01(ϕ) M (ϕ) , (6.16)

ΘIIa(ϕ(0∼1)) = L˙ (ϕ) − Ao2L (ϕ) + Ir. (6.17)

Then an observer giving the estimate of q1 can be given as follows:

{z˙ = Ao2z + ΘIIa(ϕ(0∼1))y + L (ϕ) u0
(6.18)
qˆ1 = z − L (ϕ) y.

Furthermore, the observation error e = q1 −q ˆ1 is governed by equation (6.11).

In the case of A0(ϕ(0∼1)) = A0 being constant, it is easily noted that ΘIIa(ϕ(0∼1)) in (6.17)

further reduces to

ΘIIa(ϕ(0∼1)) = Ao2A−01M˙ (ϕ) − (Ao2)2 A−01M (ϕ) + Ir. (6.19)

## [25] `odfas_2026_part4` (PDF p.43, L2433)

Corollary 6.2. Let A0(ϕ(0∼1)) = A0 (ϕ) , and L (ϕ) be given by (6.26). Further, let Assumptions

A1-A2 and Av1-Av2 be satisfied. Furthermore, let Ao2 ∈ ℝr×r be a Hurwitz matrix, and F0∼1 ∈ ℝr×2r

be a matrix making Φ (F0∼1) Hurwitz. Then a GUA stabilizing output feedback controller for system

(6.5) is given in the form of (4.27) with

K11 (ϕ) = −K12 (ϕ) L (ϕ) − F1
K12 (ϕ) = − (F0 + R (ϕ) A0 (ϕ))
{K21(ϕ(0∼1)) = ΘIIa(ϕ(0∼1)) + L (ϕ) K11 (ϕ) (6.27)

K22 (ϕ) = −L (ϕ) F0,

where Ao2 is an arbitrary Hurwitz matrix, and ΘIIa(ϕ(0∼1)) is given by (6.17)-(6.16), which reduces,

when A0(ϕ(0∼1)) = A0 is constant, to

ΘIIa(ϕ(0∼1)) = Ao2A−01M˙ (ϕ) − Ao2L (ϕ) + Ir. (6.28)

With the help of the above two propositions, we can finally obtain the following result.

## [26] `odfas_2026_part4` (PDF p.47, L2673)

Corollary 7.1. Let A0(ϕ(0∼1)) = A0 be a constant matrix. Furthermore, let Assumptions A1,

AD, Av1 and Av2 be met, and L] ∈ ℝ2r×r make AoII given by (7.11) Hurwitz. Then an observer

producing the estimates of q1 and d simultaneously is given by

z˙ = AoIIz + ΘIIb(ϕ(0∼1))y + L]M (ϕ) u0

{[qˆ1] = z − L]M (ϕ) y, (7.17)
dˆ

where

ΘIIb(ϕ(0∼1)) = L]M ˙ (ϕ) − AoIIL]M (ϕ) +[Ir]. (7.18)
0

Further, the observation error obeys the following equation

e˙ = AoIIe. (7.19)

## [27] `odfas_2026_part4` (PDF p.49, L2809)

Corollary 7.2. Let A0(ϕ(0∼1)) = A0 be a constant matrix, Assumptions A1-A2, Av1 and Av2

be met. Furthermore, L] ∈ ℝ2r×r make AoII ∈ ℝ2r×2r given by (7.11) Hurwitz, and F0∼1 ∈ ℝr×2r be a

matrix making Φ (F0∼1) Hurwitz. Then a GUA stabilizing output feedback controller for system (7.3)

is given in the form of
{u0 = K11 (ϕ) y + K12 (ϕ) z
z˙ = K21(ϕ(0∼1))y + K22 (ϕ) z, (7.27)

with
K11 (ϕ) = −K12 (ϕ) L]M (ϕ) − F1

K12 (ϕ) = −⌊F0 + R (ϕ) A0 R (ϕ)⌋

{K21(ϕ(0∼1)) = L]M (ϕ) K11 (ϕ) + ΘIIb(ϕ(0∼1)) (7.28)

K22 (ϕ) = AoII + L]M (ϕ) K12 (ϕ) ,

where ΘIIb(ϕ(0∼1)) is given by (7.18).

To summarize, we now have the following result regarding the output feedback control of the

nonlinear system (7.1).

## [28] `scis_2022_discdelay1` (PDF p.12, L763)

Corollary 1. Let Assumption 2 be met. Further, let ̟ ⩾ 1 be an integer, and A0∼̟−1 ∈ ℝ̟×r be an
arbitrarily given matrix. Then the following controller:

u (k) = B−1 x⌈τ1∼ζ(k)⌉(k) , k −f x⌈τ1∼ζ(k)⌉(k) , k + u∗(k) ,
{u∗(k) = A0∼ (̟−1x⌈0∼̟−1⌉(k) +) [ v ((k) ) ] (53)

for system (45) produces the following constant linear closed-loop system:

x (k + 1) = A0∼̟−1x⌈0∼̟−1⌉(k) + v (k) . (54)

For the control of the system (45), in the case of ̟ = 1, we have

u∗(k) = A0x (k) + v (k) ,

and the closed-loop system is
x (k + 1) = A0x (k) + v (k) .

While in the case of ̟ = n, we have

u∗(k) = A0∼n−1x⌈0∼n−1⌉(k) + v (k) ,

and the closed-loop system is

x (k + 1) = A0∼n−1x⌈0∼n−1⌉(k) + v (k) .

In practical applications, the integer ̟ may be chosen according to the requirement on the closed-loop
system. For example, if there is a requirement on both x (k) and x (k − 1), then ̟ should be chosen
greater than 2.

## [29] `scis_2024_chained1` (PDF p.15, L966)

Corollary 1. Let Assumption X be satisfied, bi, i = 1, 2, be two positive scalars, g (x0, z1, t) and
h (x0, z1, t) be differentiable with respect to all variables, and

h (x0, z1, t) ≠ 0, ∀x0, z1 ∈ ℝ and t ⩾ 0.

Then,
(1) under the following transformation:

z = z1,
{ (69)
z˙ = g (x0, z1, t) + h (x0, z1, t) z2,

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:16

the SFS (65) can be transformed into the following FAS:

z¨ = f2 (x0, z1∼2, t) + h (x0, z1, t) u, (70)

where f2 (x0, z1∼2, t) is given by (68);
(2) a stabilizing controller for the SFS (65) is given by

u = −h(x01,z1,t) (f2 (x0, z1∼2, t) + u∗) ,
{ (71)
u∗ = b0z1 + b1 [g (x0, z1, t) + h (x0, z1, t) z2] ,

which results in the following constant linear closed-loop system:

z¨ + b1z ˙ + b0z = 0. (72)

The following remark gives, in the case of n = 2, a more intuitive explanation of the third conclusion
of Theorem 3.

## [30] `scis_2024_chained1` (PDF p.20, L1244)

Corollary 2. Let bi, i = 0, 1 be two positive scalars, and x0 (0) ≠ 0. Then a controller for the nonholo-
nomic system (1) is given by

u0 = −βx0,
{u = − (β + b1) x1 − β2 + b0 + βb1 x x20, (92)
[ ]
which drives all the state variables xi, i = 0, 1, 2 to zero.
Parallelly, letting
u0 −βx0
ψˆ (x0, x2, u0, t) = = = −β,
x0 x0
in the above Theorem 6 gives the following corollary.

## [31] `scis_2024_chained1` (PDF p.20, L1256)

Corollary 3. Let bi, i = 0, 1 be two positive scalars, and x0 (0) ≠ 0. Then a controller for the Brockett
integrator (3) is given by
u0 = −βx0,
{u = − (β + b1) x1 + β1 β2 + b0 + βb1 x x20, (93)
[ ]
which drives all the state variables xi, i = 0, 1, 2 to zero exponentially.
Before ending this section, let us make the following remark.

## [32] `scis_2024_chained1` (PDF p.22, L1406)

Corollary 4. There exists an exponentially stabilizing controller for the sub-FAS (51) if and only if
one of the following conditions is met:
(1) the feasible set 𝔽z (x0) , or equivalently, the corresponding ROEA ℚ, contains the origin as an inner
point;
(2) the sub-FAS (51) is a local FAS; and
(3) the SFS (33) is locally normal.
For the case that 𝔽z (x0) or the corresponding ROEA ℚ does not contain the origin as an inner point,
there does not exist even a locally exponentially stabilizing controller for the second subsystem. Yet we do
have a so-called sub-stabilizing controller which drives, as mentioned above, all trajectories of the system
starting from the ROEA ℚ exponentially to the origin. In many practical applications, the feasible set
𝔽z (x0) or the corresponding ROEA ℚ is sufficiently large such that the singular case seldom or even
never happens. In such a case, although the designed controller is not even a locally stabilizing one in
the Lyapunov sense, it does work practically. This clearly suggests a kind of stability which is termed
sub-stability in [2,49], and the designed controller is called a sub-stabilizing controller.

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:23

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

## [33] `scis_2024_chained2` (PDF p.9, L590)

Corollary 1. The perturbed nonlinear system (38) is UGE stable if the following conditions are met:
(1) There exists a continuous function V (x, t) : ℝn × ℝ+ ↦ ℝ that satisfies the inequalities

µ1‖x‖2 ⩽ V (x, t) ⩽ µ2‖x‖2, (46)

∂V + ∂V f(x, t) ⩽ −µ3‖x‖2, (47)
∂t ∂x
∂V
⩽ ρv (t) ‖x‖, (48)
‖‖‖‖ ∂x‖‖‖‖

with µi, i = 1, 2, 3, being a set of positive scalars, and ρv (t) being a nonnegative scalar function;
(2) ∆f(x, t) ∈ ℝn satisfies
‖∆f(x, t)‖ ⩽ ρ∆(t)‖x‖, (49)

with ρ∆(t) being a nonnegative function satisfying (43).
When the assumption is further strengthened, the following corollaries can be given.

## [34] `scis_2024_chained2` (PDF p.9, L607)

Corollary 2. The perturbed nonlinear system (38) is UGE stable if the following conditions are met:
(1) There exists a continuous function V (x, t) : ℝn× ℝ+ ↦ ℝ that satisfies inequalities (46)–(48) with
ρv (t) = ρv being a nonnegative scalar;
(2) ∆f(x, t) ∈ ℝn satisfies (49) and

∞
∫ ρ∆(s)ds = M < ∞, (50)

with ρ∆(t) being a nonnegative function.

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:10

## [35] `scis_2024_chained2` (PDF p.10, L621)

Corollary 3. Suppose that f(x, t) ∈ ℝn is continuously differentiable with respect to t, and satisfies
one of the following conditions:
(1) The Jacobian matrix [∂f/∂x] is globally bounded, uniformly in t;
(2) f(x, t) is globally Lipschitz with respect to x, uniformly in t.
Furthermore, the system
x˙ = f(x, t), (51)

is UGE stable, and ∆f(x, t) ∈ ℝn satisfies (49), with ρ∆(t) being a nonnegative function satisfying (50);
then system (38) is UGE stable.

## [36] `scis_2024_chained2` (PDF p.14, L870)

Corollary 4. Suppose
ψ′(ζ0, η0, x2, t) ≠ 0, ∀ζ0, η0, x2 ∈ ℝ, and t ⩾ 0, (75)

and define

g′(ζ0, η0, z1, t) = [β + ϕ′(·)] z1, (76)
h′(ζ0, η0, z1, t) = γψ′(·) . (77)

Then, under the following transformation:

z = z1,
{ (78)
z˙ = g′(ζ0, η0, z1, t) + h′(ζ0, η0, z1, t) z2,

system (74) can be transformed into the following FAS:

z¨ = f2 (ζ0, η0, z1∼2, t) + h′(ζ0, η0, z1, t) u, (79)

where
f2 (ζ0, η0, z1∼2, t) = ˙g′(ζ0, η0, z1, t) + h˙′(ζ0, η0, z1, t) z2. (80)

## [37] `scis_2024_chained2` (PDF p.15, L932)

Corollary 5. Let bi, i = 1, 2, be two positive scalars, f2 (ζ0, η0, z1∼2, t) be given by (80), and

h′(ζ0, η0, z1, t) ≠ 0, ∀ζ0, z1 ∈ ℝ, and η0 ≠ −αζ0, t ⩾ 0.

Then a stabilizing controller for system (71) is given by

t
u0 = −a0 0 x0 (s) ds − a1 (x0 (t) − ζ0) + η0,
u = −h′(ζ0∫,η10,z1,t) (f2 (ζ0, η0, z1∼2, t) + u∗) , (84)
{
u∗ = b0z1 + b1 [g′(ζ0, η0, z1, t) + h′(ζ0, η0, z1, t) z2] ,

which results in the following constant linear closed-loop system:

x¨0 + a1x ˙0 + a0x0 = 0,
{ (85)
z¨ + b1z ˙ + b0z = 0,

with the following initial value conditions:

x0 (0) = ζ0, ˙x0 (0) = η0 ≠ −αζ0.

## [38] `scis_2024_chained2` (PDF p.16, L1051)

Corollary 6. Let Assumption C be satisfied, and f˘i(Z0, ζ0, η0, t), i = 1, 2, . . . , n−1, and B˘e(Z0, ζ0, η0, t)
be given by Algorithm 1. If B˘e(Z0, ζ0, η0, t) is uniformly lower bounded, f˘i(Z0, ζ0, η0, t), i = 1, 2, . . . , n−1,

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:17

uniformly and exponentially converge to zero for all Z0 ∈ ℝn, ζ0 ∈ ℝ, and η0 ≠ −βζ0, and further
∞
∫ ‖ρψ (s)‖ e−(α−β)sds = M < ∞, (101)
0

then u = u (ζ0, η0, z1∼n, t) given by (81) is a controller that UGE stabilizes the system (100).
Please note that the condition, f˘i(Z0, ζ0, η0, t), i = 1, 2, . . ., n − 1, uniformly and exponentially con-
verge to zero, is not very strict, because these functions have already been shown to converge to zero
asymptotically.

## [39] `tcyb_2023_robustdelay` (PDF p.6, L747)

Corollary 1: Let Assumptions B1–B4 be met. Then, there
exists a controller in the form of (23) that GUA stabilizes the
uncertain type I system (22) if there exists a controller in the
form of (23) that robustly input-to-state stabilizes, with respect
to the external input z(0∼m−1), the uncertain single-order FAS
in (22).
Due to the above Proposition 1, it is clear to see that the
robust GUA stabilizing controller for the uncertain type I
system (17) is the same with the robustly input-to-state sta-
bilizing controller for the uncertain FAS in (17). Therefore, a
solution to Problem 1 is immediately provided if the following
robustly input-to-state stabilization problem is solved.

## [40] `tcyb_2023_robustdelay` (PDF p.7, L862)

Corollary 2: Let A0∼n−1 ∈ ℝr×nr be a matrix satisfy-
ing (36), and h(z(0∼m−1)) is a K∞-bounded function. Then,
the following system:

x(n) = −A0∼n−1x(0∼n−1) + h(z(0∼m−1))

is input-to-state stable, with z(0∼m−1) being viewed as the
system external input.

Further applying Corollary 1, we immediately have the
following result, which gives the solution to Problem 2.

## [41] `tcyb_2023_robustdelay` (PDF p.7, L873)

Corollary 3: Let A0∼n−1 ∈ ℝr×nr be a matrix satisfy-
ing (36), and Assumptions B1–B4 hold. Furthermore, let
ε ∈ (0, 1) be an arbitrarily given number. Then, the con-
trol law (40)-(41) robustly GUA stabilizes the uncertain
system (22).

## [42] `tcyb_2023_robustdelay` (PDF p.8, L975)

Corollary 4: Let [Ai]0∼μi−1 ∈ ℝri×riμi, i = 1, 2, . . . , η be
a set of matrices satisfying (44), and Assumptions A1–A4 be
satisfied. Further, let ε ∈ (0, 1) be an arbitrarily given number.
Then, the control law (46)–(47) robustly GUA stabilizes the
uncertain type I system (17).

## [43] `tcyb_2023_robustdelay` (PDF p.8, L1043)

Corollary 5: Let A0∼n−1 ∈ ℝr×nr be a matrix satis-
fying (36), Assumptions B0, B1, B3′, and B4 be met.
Furthermore, let ε ∈ (0, 1) be an arbitrarily given number.
Then, the controller (52)-(53) robustly GUA stabilizes the
uncertain type I system (50).
To end this section, we make the following important
remark.

## [44] `tcyb_2023_subfas` (PDF p.5, L662)

Corollary 1: A state-space system is (globally) feedback
linearizable if and only if it can be equivalently converted
into a (global) FAS.

## [45] `tcyb_2023_subfas` (PDF p.6, L668)

Corollary 2: The following conclusions hold.
1) An irrational sub-FAS is not globally feedback
linearizable.
2) A critically rational sub-FAS is not feedback linearizable
in the Lyapunov stability sense, but may be feedback
linearized in the substability sense.
The above results reveal the nature of a (global) FAS.
It follows from the above corollary that a system which is
not equivalent to a (global) FAS is not globally feedback
linearizable.

## [46] `ucfas_2025_part3` (PDF p.10, L995)

Corollary 5.1: Restrict

u1(t) ≠ 0, t ≥ 0. (76)

Then the UC-FAS of system (73) is
{
x¨ = u1 − 1
z(4) = f (u(10∼2), z(2∼3)) + u1u2, (77)

where
( )
f (u(0∼2), z(2∼3)) = 2u˙1 ...z − ˙u1z + u¨1z. (78)
1 u1 u1¨ u1¨

Furthermore,

1
y = z¨, (79)
u1

( )
1 ... u1
y˙ = z − ˙ z¨ . (80)
u1 u1

Design the controller for the first subsystem
in (77) as

u1 = −a0∼1x(0∼1) + 1, a0, a1 > 0, (81)

which gives the closed-loop system (53).
Recalling again that the solution to system (53) is
given by (54), we have

u1(t) ≜ ξ0x(X0, t)

= −a0∼1 exp[Φ(a0∼1)t]X0 + 1, (82)

u˙1(t) ≜ ξ1x(X0, t)

= −a0∼1Φ(a0∼1) exp[Φ(a0∼1)t]X0, (83)

u¨1(t) ≜ ξ2x(X0, t)

= −a0∼1Φ2(a0∼1) exp[Φ(a0∼1)t]X0. (84)

Substituting (82)–(84) into the second equation in (77)
gives

z(4) = f˜ (z(2∼3), X0, t) + b(X0, t)u2, (85)

where

f˜ (z(2∼3), X0, t)

ξ1x(X0, t) ( ... 1x(X0, t) ) ξ2x(X0, t)
= 2 z − ξ z¨ + z¨,
b(X0, t) b(X0, t) b(X0, t)

b(X0, t)

= −a0∼1 exp[Φ(a0∼1)t]X0 + 1.

Thus the internal RoEA is given by
{ }
in a0∼1 exp[Φ(a0∼1)t]X0 ≠ 1,

## [47] `book_2026_volume1` (PDF p.93, L73)

Corollary 2.1 The linear system (2.65) is controllable if and only if there exists a
nonsingular matrix T ∈ Rn×n such that (Z (s), U (s)) with z ∈ Rr given by (2.82),
satisfies the fully actuated PMD
P(s)Z (s) = B0 U (s),               (2.102)
where P(s) ∈ Rr ×r (s) is some polynomial matrix, and B0 ∈ Rr ×r is a square upper
triangular matrix with diagonal elements all being 1.
In general, PMD (2.100) is underactuated since. Q(s) = B is not square in general.
Parallelly, we are interested in the following problem.

## [48] `book_2026_volume1` (PDF p.100, L80)

Corollary 2.2 For the LTV system (2.109) satisfying Assumptions 2.6 and 2.7, there
still exists a FAS model of the augmented system (2.122) in the form of
−1)
z k(μk )            = L (t) z k(0∼μk                  + Bz (t) u,         (2.123)
k=1∼η                              k=1∼η
where L (t) ∈ Rr ×(n+n e ) and Bz (t) ∈ Rr×r are two linear matrix functions, with
Bz (t) being nonsingular for all t ≥ t0 , μk , k = 1, 2, . . . , η, are a set of distinct
integers, and z k ∈ Rrk with rk satisfying
r + r2 + · · · + rη = r.
2.5.3 Controller Design
For the control of FAS (2.120), a controller can be readily designed as
⎛                                           ⎡  −1) ⎤⎞
[A1 ]0∼μ1 −1 z 1(0∼μ1
⎜                          ⎢ [A2 ]           (0∼μ2 −1) ⎥⎟
⎜                          ⎢       0∼μ2 −1 z 2         ⎥⎟
−1
u = −Bz (t) ⎜         (0∼μk −1)        ⎢
+⎢             .             ⎥⎟ ,
⎜ L (t) z k                              .
⎥⎟                         (2.124)
⎝                   k=1∼η  ⎣                           ⎦⎠
(0∼μη −1)
Aη 0∼μη −1 z η
which produces the following set of LTI closed-loop systems:
z (μk ) + [Ak ]0∼μk −1 z k(0∼μk −1) = 0, k = 1, 2, . . . , η,
k                                                                             (2.125)
where [Ak ]0∼μk −1 ∈ Rrk ×μk rk , k = 1, 2, . . . , η, are a series of arbitrarily given matri-
ces. In particular, the closed-loop eigenvalues can be arbitrarily assigned by properly
selecting these matrices. Such a property of FASs totally reveals the meaning of con-
trollability of dynamic control systems in the sense that a controller can be found such
that the closed-loop systems are LTI systems with arbitrarily desired eigenvalues.

## [49] `book_2026_volume1` (PDF p.225, L207)

Corollary 6.1 If det G 1             0, and, for x1 , x2 ∈ Rr , and ζ ∈ Rm , there holds
(0∼1)
det G 2 (x1∼2   , ζ, t)   0,
then, in the case of n = 2, SFS (6.18) can be transformed into the following FAS:
z (4) = h(z (0∼3) , ζ, t) + L(z (0∼3) , ζ, t)u,                (6.30)
with
(0∼1)
L(z (0∼3) , ζ, t) = G 1 G 2 (x1∼2      , ζ, t),                       (6.31)
(0∼3)
¨
f 1 (z (0∼1) , ζ, t)
h(z       , ζ, t) = [Ir G 1 ]           (0∼1)         ,              (6.32)
f 2 (x1∼2    , ζ, t)
where L 0 = Ir , and in (6.31)–(6.32) the x2 and its derivative are given and
determined by
−1             (0∼1)
x 2 = G 1 [z̈ − f 1 (z       , ζ, t)].
6.4 Mixed-Order SFSs
When modeling complex physical systems, there are systems governed by Newton’s
Law, the Lagrangian Equation, or the Theorem of Momentum, etc. Simultaneously,
there may also be subsystems governed by other physical or chemical laws which
produce the first-order or high-order differential equations. Therefore, there may
be subsystems of first-, second- and high-order. Moreover, by the FAS approach,
208                                                 6 Strict Feedback Systems with Uniform Dimensions
some of the subsystems may also be equivalently turned into high-order ones. Due to
these observations, we have also introduced in Duan (2021b) the so-called high-order
(mixed-order) SFSs.
6.4.1 Recursive Solution
The high-order (mixed-order) SFSs introduced in Duan (2021b) appear in the
following form:
⎧ (m 1 )

## [50] `book_2026_volume1` (PDF p.229, L211)

Corollary 6.2 If det G 1 G 2 0, and for all xk ∈ Rr , k = 1, 2, 3, and.ζ ∈ Rm , there
holds
(0∼m i −1)
det G 3 (x i          |i=1∼3 , ζ, t) 0, ∀t ≥ 0,
then, for the case of n = 3, SFS (6.33) can be equivalently turned into the following
FAS:
( p)
z      = h(z (0∼ p−1) , ζ, t) + L(z (0∼ p−1) , ζ, t)u,      (6.49)
with p = m 1 + m 2 + m 3 , and
L(z (0∼ p−1) , ζ, t) = G 1 G 2 G 3 (xi(0∼m i −1) |i=1∼3 , ζ, t),            (6.50)
and
h(z (0∼ p−1) , ζ, t)
⎡                                               ⎤
f 1(m 2 +m 3 ) (z (0∼m 1 −1) , ζ, t)
= Ir         G1    G1G2     ⎣ f (m 3 ) (x (0∼m 1 −1) , x (0∼m 2 −1) , ζ, t) ⎦ ,   (6.51)
2          1               2
f 3 (xi(0∼m i −1) |i=1∼3 , ζ, t)
where in (6.50)–(6.51) the x2 , x3 and their derivatives are given and determined by
x2 = G −1
1 [z
(m 1 )
− f 1 (z (0∼m 1 −1) , ζ, t)]
−1 −1 ( p2 )                                                  (6.52)
x3 = G 2 G 1 [z        − h 2 (z (0∼ p2 −1) , ζ, t)],
with
f 1(m 2 ) (z (0∼m 1 −1) , ζ, t)
h (z (0∼ p2 −1) , ζ, t) = Ir G 1                                                     (6.53)
f 2 (x1(0∼m 1 −1) , x2(0∼m 2 −1) , ζ, t)
212                                                 6 Strict Feedback Systems with Uniform Dimensions
6.5 Examples
6.5.1 Example 1: Cascade Systems

## [51] `book_2026_volume1` (PDF p.240, L222)

Corollary 6.3 Let Condition 6.1 be met, then there exists an invertible transforma-
tion
(0∼n−1)
x 1∼n = T (z         , ζ, t),                     (6.90)
such that the first-order SFS (6.1), with f k , k = 1, 2, . . . , n, given by (6.89), can be
equivalently transformed into the following FAS:
ω
z (n) =         h l (z (0∼n−1) , ζ, t) + L(z (0∼n−1) , ζ, t)u,         (6.91)
l=1
with
L(z (0∼n−1) , ζ, t) = G 1 G 2 · · · G n−1 G n (x1∼n , ζ, t),               (6.92)
and                                                           ⎡              ⎤
f 1l(n−1) (z, ζ, t)
⎢ f (n−2) (z, x2 , ζ, t) ⎥
⎢ 2l                      ⎥
(0∼n−1)                   ⎢              ..         ⎥
h l (z         , ζ, t) = L 0∼n−1 ⎢                         ⎥,                   (6.93)
⎢               .         ⎥
⎣ f˙                      ⎦
n−1,l (x 1∼n−1 , ζ, t)
f nl (x1∼n , ζ, t)
where. L 0 = I, and. L k ,.k = 1, 2, . . . , n − 1, are given by (6.88), and in (6.92)–(6.93)
the xk , k = 2, 3, . . . , n, and their derivatives are given by transformation (6.90).
Now let us consider the following SFS with uncertainties:
⎧
⎪
⎪ ẋ1 = f 1 (x1 , ζ, t) + f 1 (x1 , ζ, t) + G 1 x2
⎪
⎪
⎨ 2 = f 2 (x1∼2 , ζ, t) + f 2 (x1∼2 , ζ, t) + G 2 x 3
⎪ ẋ
.                                                                              (6.94)
⎪         .
⎪
⎪
⎪
⎪ ẋ n−1 =   f n−1 (x1∼n−1 , ζ, t) + f n−1 (x1∼n−1 , ζ, t) + G n−1 xn
⎩
ẋn = f n (x1∼n , ζ, t) + f n (x1∼n , ζ, t) + G n (x1∼n , ζ, t)u,

## [52] `book_2026_volume1` (PDF p.283, L265)

Corollary 8.1 Let Assumption 8.2 be satisfied, then, under the following transfor-
mation:
⎧
⎪ x1 = z −1
⎪
⎨
x2 = g1 (y1 , t) , y1 = ẋ1 − f 1 (x1 , ζ, t)
= lk−1 z (0∼k−1) , yk , ζ (0∼k−2) , t , yk = z (k) − h k (z (0∼k−1) , ζ (0∼k−1) , t),
⎪
⎪ x
⎩ k+1
k = 2, 3, . . . , n − 1,
(8.17)
the generalized strict-feedback nonlinear system (8.15) can be equivalently trans-
formed into the following FAS model:
z (n) = h n (z (0∼n−1) , ζ (0∼n−1) , t) + l n (z (0∼n−1) , u, ζ (0∼n−2) , t),               (8.18)
with the vector functions h n (z (0∼n−1) , ζ (0∼n−1) , t) and l n (z (0∼n−1) , u, ζ (0∼n−2) , t)
being recursively given by
⎧
⎪
⎪ h 2 (z (0∼1) , ζ (0∼1) , t) = ḣ 1 (z, ζ, t)+ ∂l 1 (z,x     ∂z
2 ,t)
ż + ∂l 1 (z,x
∂t
2 ,t)
⎪
⎪
⎪
⎪                             + ∂l 1 (z,x  2 ,t)
f 2 (x1∼2 , ζ, t)
⎪
⎪
∂ x2
⎪
⎪ h   (z (0∼k−1)
, ζ (0∼k−1)
, t)   =    ḣ  k−1 (z
(0∼k−2)
, ζ (0∼k−2) , t)
⎪
⎪

## [53] `book_2026_volume1` (PDF p.284, L266)

Corollary 8.2 Let Assumption 8.1 be satisfied, then, under the following transfor-
mation
⎧
⎪
⎪ x1 = z
⎨
x2 = g1−1 (z, y1 , ζ, t), y1 = ż
= lk−1 (z (0∼k−1) , yk , ζ (0∼k−2) , t), yk = z (k) − h k (z (0∼k−1) , ζ (0∼k−1) , t),
⎪
⎪ x
⎩ k+1
k = 2, 3, . . . , n − 1,
(8.24)
the generalized SFS (8.23) can be transformed into the following FAS:
z (n) = h n (z (0∼n−1) , ζ (0∼n−1) , t) + ln (z (0∼n−1) , u, ζ (0∼n−2) , t),        (8.25)
8.2 Second-Order Nonaffine SFSs                                                                                                 267
where the vector functions h n (z (0∼n−1) , ζ (0∼n−1) , t) and ln (z (0∼n−1) , u, ζ (0∼n−2) , t)
are recursively given by
⎧
⎪
⎪ h 2 (z (0∼1) , ζ (0∼1) , t) = ḣ 1 (z, ζ, t)+ ∂l 1 (z,x     ∂z
2 ,ζ,t)
ż+ ∂l 1 (z,x
∂ζ
2 ,ζ,t)
ζ̇
⎪
⎪                                     ∂l 1 (z,x2 ,ζ,t)
⎪
⎪                                +
⎪
⎨ h (z (0∼k−1) , ζ (0∼k−1) , t) = ḣ ∂t (z (0∼k−2) , ζ (0∼k−2) , t)
k                                       k−1
∂l k−1 (z (0∼k−2) ,xk ,ζ (0∼k−3) ,t) (0∼k−2)
⎪
⎪                                       +                                        ż
⎪
⎪
∂z (0∼k−2)
⎪
⎪                                       +    ∂l k−1 (z (0∼k−2) ,xk ,ζ (0∼k−3) ,t) (0∼k−3)

## [54] `book_2026_volume1` (PDF p.292, L274)

Corollary 8.3 Let condition (8.48) and Assumption 8.4 be satisfied, then, under the
following transformation
⎧
⎪
⎪ x1 = z
⎨
x2 = g1−1 (y1 , t) , y1 = z̈ − f 1 ( z (0∼1) , ζ, t),
⎪ xk+1 = lk−1 z (0∼2k−1) , yk , ζ (0∼2k−4) , t , yk = z (2k) − h k (z (0∼2k−1) , ζ (0∼2k−2) , t),
⎪
⎩
k = 2, 3, . . . , n − 1,
(8.51)
and             ⎧
⎨ ẋ1 = ż −1
⎪
dg (y ,t)
ẋ2 = 1 dt 1                                                              (8.52)
⎪
⎩          dl −1 (z (0∼2k−1) ,yk ,ζ (0∼2k−4) ,t)
ẋk+1 = k                 dt
, k = 2, 3, . . . , n − 1,
the generalized strict-feedback nonlinear system (8.29) can be equivalently trans-
formed into the following FAS model:
z (2n) = h n (z (0∼2n−1) , ζ (0∼2n−2) , t) + l n ( z (0∼2n−1) , u, ζ (0∼2n−4) , t),                      (8.53)
where for k = 2, 3, . . . , n − 1,
l k (z (0∼2k−1) , xk+1 , ζ (0∼2k−4) , t) = ∂g1∂(xx22 ,t) ∂g2∂(xx33 ,t) · · · ∂gk−1∂ x(xk k ,t) gk (xk+1 , t)
(0∼2n−3)
,xn ,ζ (0∼2n−6) ,t)
l n (z (0∼2n−1) , u, ζ (0∼2n−4) , t) = ∂l n−1 (z             ∂ xn
g n (u, t),
(8.54)
and for k = 2, 3, . . . , n,
h (z (0∼2k−1) , ζ (0∼2k−2) , t) = f˙˜k−1 (z (0∼2k−2) , ζ (0∼2k−3) , t)
k
(0∼1)
+g̃ k−1 (z (0∼2k−2) , ζ (0∼2k−4) , t) f k (x1∼k   , ζ, t)
˙
+g̃k−1 (z (0∼2k−2)
,ζ   (0∼2k−4)

## [55] `book_2026_volume1` (PDF p.294, L276)

Corollary 8.4 Let Assumption 8.4 and condition f i (x1∼i                 , ζ, t) = 0, i =
1, 2, . . . , n, be satisfied, then, under the following transformation:
8.2 Second-Order Nonaffine SFSs                                                                         277
⎧
⎪
⎪ x1 = z
⎨
x2 = g1−1 (y1 , t) , y1 = z̈,
= lk−1 z (0∼2k−1) , yk , ζ (0∼2k−4) , t , yk = z (2k) − h k (z (0∼2k−1) , ζ (0∼2k−2) , t),
⎪
⎪ x
⎩ k+1
k = 2, 3, . . . , n − 1,
(8.61)
and             ⎧
⎨ ẋ1 = ż −1
⎪
dg (y ,t)
ẋ2 = 1 dt 1                                                              (8.62)
⎪
⎩          dlk−1 (z (0∼2k−1) ,yk ,ζ (0∼2k−4) ,t)
ẋk+1 =                   dt
, k = 2, 3, . . . , n − 1,
the generalized strict-feedback nonlinear system (8.29) can be equivalently trans-
formed into the following FAS model:
z (2n) = h n (z (0∼2n−1) , ζ 0∼2n−2 , t) + l n ( z (0∼2n−1) , u, ζ (0∼2n−4) , t),          (8.63)
where the vector functions h n (z (0∼2n−1) , ζ (0∼2n−2) , t) and ln (z (0∼2n−1) , u,
ζ (0∼2n−4) , t) are recursively given by
h k (z (0∼2k−1) , ζ (0∼2k−2) , t)
= f˜˙k−1 (z (0∼2k−2) , ζ (0∼2k−3) , t) + g̃˙ k−1 (z (0∼2k−2) , ζ (0∼2k−4) , t)ẋk
(0∼1)
+g̃ k−1 (z (0∼2k−2) , ζ (0∼2k−4) , t) f k (x1∼k    , ζ, t),                         (8.64)
(0∼2k−1)            (0∼2k−4)
l k (z          , xk+1 , ζ          , t)
(0∼1)
= g̃k−1 (z (0∼2k−2) , ζ (0∼2k−4) , t)g k (x1∼k    , xk+1 , ζ, t),                     (8.65)
for k = 2, 3, . . . , n, with xn+1 = u, and
(0∼1)

## [56] `book_2026_volume1` (PDF p.303, L285)

Corollary 8.5 Let Assumption 8.6 be satisfied, then, under the following transfor-
mations
⎧
⎪
⎪ x1 = z
⎨
x2 = l1−1 (z (0∼m 1 −1) , y1 , ζ, t), y1 = z (m 1 ) − h 1 (z (0∼m 1 −1) , ζ, t)
(8.89)
= lk−1 (z (0∼ pk −1) , yk , ζ, t), yk = z ( pk ) − h k (z (0∼ pk −1) , ζ, t),
⎪
⎪ x
⎩ k+1
k = 2, 3, . . . , n − 1,
and
⎧ (i)
⎨ x1 = z (i) , i = 1, 2, . . . , m 1 − 1
x (i) = dtd i lk−1 (z (0∼ pk −1) , yk , ζ, t), yk = z ( pk ) − h k (z (0∼ pk −1) , ζ, t),
i
(8.90)
⎩ k+1
i = 1, 2, . . . , m k+1 − 1, k = 1, 2, . . . , n − 1,
the generalized nonlinear SFS (8.87) can be equivalently transformed into the
following FAS model:
z ( p) = h n (z (0∼ p−1) , ζ, t) + l n (z (0∼ p−1) , u, ζ, t),                       (8.91)
where the vector functions h n (z (0∼ p−1) , ζ, t) and l n (z (0∼ p−1) , u, ζ, t) are recursively
given by
h k (z (0∼ pk −1) , ζ, t)
(m k −1) (0∼ pk−1 )
= Fk−1       (z           , xk , ζ, t)
m k −2                                                                      (m k −1− j)
∂                                                   ( j+1)
+            C( j, m k − 1)                  l k−1 (z (0∼ pk−1 −1) , xk , ζ, t)             xk
j=0
∂ xk
∂l k−1 (z (0∼ pk−1 −1) , xk , ζ, t)
+                                       f k (xi(0∼m i ) |i=1∼k , ζ, t),                               (8.92)
∂ xk
k = 2, 3, . . . , n,

## [57] `book_2026_volume1` (PDF p.305, L287)

Corollary 8.6 Let Assumption 8.5 be satisfied, then, under the following transfor-
mations:
⎧
⎪
⎪ x1 = z
⎨
x2 = l1−1 (z (0∼m 1 −1) , y1 , ζ, t), y1 = z (m 1 ) − h 1 (z (0∼m 1 −1) , ζ, t)
(8.98)
= lk−1 (z (0∼ pk −1) , yk , ζ, t), yk = z ( pk ) − h k (z (0∼ pk −1) , ζ, t),
⎪
⎪ x
⎩ k+1
k = 2, 3, . . . , n − 1,
and
⎧ (i)
⎨ x1 = z (i) , i = 1, 2, . . . , m 1 − 1
x (i) = dtd i lk−1 (z (0∼ pk −1) , yk , ζ, t), yk = z ( pk ) − h k (z (0∼ pk −1) , ζ, t),
i
(8.99)
⎩ k+1
i = 1, 2, . . . , m k+1 − 1, k = 1, 2, . . . , n − 1,
the generalized nonlinear SFS (8.97) can be equivalently transformed into the
following FAS model:
z ( p) = h n (z (0∼ p−1) , ζ, t) + l n (z (0∼ p−1) , u, ζ, t),          (8.100)
288                                                                    8 Nonaffine Strict Feedback Systems
where the vector functions h n (z (0∼ p−1) , ζ, t) and l n (z (0∼ p−1) , ζ, u, t) are recursively
given by
h (z (0∼ pk −1) , ζ, t)
k
(m k −1) (0∼ pk−1 )
=Fk−1     (z          , xk , t)
m k −2                                                          (m k −1− j)
∂                                                ( j+1)
+            C( j, m k − 1)         l k−1 (z (0∼ pk−1 −1) , xk , t)             xk      ,   (8.101)
j=0
∂ xk
k = 2, 3, . . . , n,

## [58] `book_2026_volume1` (PDF p.380, L365)

Corollary 11.1 Let condition (11.37) be met. Then the closed-loop system consisting
of system (11.25) and reduced-order observer-based output feedback (11.58)–(11.59)
is given by
ẋ1(0∼n 1 −1)      x1(0∼n 1 −1)
(0∼n 2 −1) =                 ,               (11.61)
x2(0∼n 2 −1)
F
ẋ2
and
ė =
33 e,                            (11.62)
where F and 33 are given by (11.45) and (11.41), respectively.
The above result indicates that, in this case, the closed-loop system is stable if
and only if both F and 33 are Hurwitz.
Firstly, regarding the requirement that the matrix F is Hurwitz, we observe
0r1 ×n 1 r1 ) + B1 F11                B1 F12
F =
B2 F21                      0r2 ×n 2 r2 ) + B2 F22
=       0 + B E FD ,                                                 (11.63)
where
0r1 ×n 1 r1 )        0
0 =                                          .
0                0r2 ×n 2 r2 )
Since it is easily shown that ( 0 , B E ) is controllable, we can always find the matrix
FD such that F has arbitrarily prescribed eigenvalues. Therefore, we can often
choose a proper FD matrix by solving the pole assignment problem (11.63) and
adjusting the decomposition (11.26).
366                                                                              11 Observer-Based Control
Secondly, regarding the existence of an observer gain L such that 33 is Hurwitz,
the problem has been completely solved in Sect. 11.3.2.
Case of f0 (z1 , z2 ) Dependent on z2
Letting Ai j = 0, i, j = 1, 2, in the above Theorem 11.5, immediately gives the
following result.

## [59] `book_2026_volume1` (PDF p.381, L366)

Corollary 11.2 The closed-loop system consisting of system (11.25) and reduced-
order observer-based output feedback (11.58)–(11.59) is given by
ẋ1(0∼n 1 −1)                   x1(0∼n 1 −1)
=                    + BE     f0 ,            (11.64)
ẋ2(0∼n 2 −1)                   x2(0∼n 2 −1)
F
and
ė =
33 e + B L     f0 ,                       (11.65)
where
B L = L B1 B2 (11.66)
and F and B E are given by (11.45) and (11.46), respectively, and e, 33 , and f0
are given by (11.40), (11.41), and (11.36), respectively.
Regarding the exponential stability of the closed-loop system composed of
(11.64)–(11.65), obviously, Theorem 11.6 can be readily utilized to solve the prob-
lem, but setting. Ai j = 0,.i, j = 1, 2. However, in this special case, a more convenient
result can be provided.

## [60] `book_2026_volume1` (PDF p.400, L386)

Corollary 12.1 Let Assumptions 12.5–12.10 be met. Then, there exists a controller
in the form of (12.22) that GUA stabilizes the uncertain Type I system (12.21) if there
exists a controller in the form of (12.22) that robustly input-to-state stabilizes, with
respect to the external input z (0∼m−1) , the uncertain single-order FAS in (12.21).
Due to the above Proposition 12.1, it is clear to see that the robustly GUA stabiliz-
ing controller for the uncertain Type I system (12.16) is the same as the robustly input-
to-state stabilizing controller for the uncertain FAS in (12.16). Therefore, a solution
to Problem 12.1 is immediately provided if the following robustly input-to-state
stabilization problem is solved.
12.3 Robust Stabilization with Full State Feedback                                       387

## [61] `book_2026_volume1` (PDF p.403, L389)

Corollary 12.2 Let. A0∼n−1 ∈ Rr×nr be a matrix satisfying (12.33), and h z (0∼m−1)
is a K∞ -bounded function. Then the following system
x (n) = −A0∼n−1 x (0∼n−1) + h z (0∼m−1)
is input-to-state stable, with z (0∼m−1) being viewed as the system external input.
Further applying Corollary 12.1, we immediately have the following result, which
gives the solution to Problem 12.2.

## [62] `book_2026_volume1` (PDF p.403, L389)

Corollary 12.3 Let. A0∼n−1 ∈ Rr×nr be a matrix satisfying (12.33), and Assumptions
12.5–12.10 hold. Furthermore, let ε ∈ (0, 1) be an arbitrarily given number. Then,
control law (12.37)–(12.38) robustly GUA stabilizes the uncertain system (12.21).
12.3.2 Case of Multi-Order FASs
Let [Ai ]0∼μi −1 ∈ Rri ×ri μi , i = 1, 2, . . . , η, be a set of given matrices satisfying
μ
Reλ j
[Ai ]0∼μi −1     ≤−      ,                                     (12.41)
j =1, 2, . . . , μi ri , i = 1, 2, . . . , η,
for some μ > 0. Then it follows from Lemma 11.1 again that there exists a set of
positive definite matrices
Pi    P([ Ai ]0∼μi −1 ), i = 1, 2, . . . , η,
satisfying
T
([Ai ]0∼μi −1 )Pi + Pi          [ Ai ]0∼μi −1 ) ≤ −μPi ,               (12.42)
i = 1, 2, . . . , η.
Then, following the procedure given in Sect. 12.3.1, we can define the matrices
PLi      PL [ Ai ]0∼μi −1 , i = 1, 2, . . . , η.
Based on the defined matrices PLi , i = 1, 2, . . . , η, the following controller for the
uncertain multi-order FAS in (12.16) can be designed:
⎧
⎪
⎪
⎪ u = − B̃ −1 (·) f˜ (·) + u ∗
⎪
⎪      ⎡ ∗⎤
⎪
⎨        u1
⎢ u ∗2 ⎥                                                                 (12.43)

## [63] `book_2026_volume1` (PDF p.405, L391)

Corollary 12.4 Let [ Ai ]0∼μi −1 ∈ Rri ×ri μi , i = 1, 2, . . . , η, be a set of matrices sat-
isfying (12.41), and Assumptions 12.3–12.8 be satisfied. Further, let ε ∈ (0, 1) be an
arbitrarily given number. Then, control law (12.43)–(12.44) robustly GUA stabilizes
the uncertain Type I system (12.16).

## [64] `book_2026_volume1` (PDF p.406, L392)

Corollary 12.1:

## [65] `book_2026_volume1` (PDF p.406, L392)

Corollary 12.5 Let. A0∼n−1 ∈ Rr×nr be a matrix satisfying (12.33), and Assumptions
12.2, 12.5, 12.10, and 12.11 be met. Furthermore, let ε ∈ (0, 1) be an arbitrarily
given number. Then controller (12.49)–(12.50) robustly GUA stabilizes the uncertain
Type I system (12.47).
To end this subsection, we make the following important remark.

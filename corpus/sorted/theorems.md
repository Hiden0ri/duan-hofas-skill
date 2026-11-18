# Sorted Theorem Corpus Across 32 Duan First-Author Papers + Volume I (198 items)

## [1] `aaas_2024_subsfs` (PDF p.5, L511)

定理 2. 1 的证明思路，可给出如下结果。

## [2] `aaas_2024_subsfs` (PDF p.5, L512)

定理 1 假设 1 满足 ，变量 Bk(x(0~k - 1) ，t) 和

hk(x(0~k - 1) ，t) ( k = 1，2，…，n ) 由式（3）、式（4）和

式（11）给出，则当 x1~n ∈ 𝔽̂时，亚严反馈系统式（1）
在变换式（6）或式（17）下可等价地化为下述亚全
驱系统。
x( )n = hn(x(0~n - 1) ，t) + Bn(x(0~n - 1) ，t) u （20）

## [3] `aaas_2024_subsfs` (PDF p.7, L704)

定理 2 假设 1 成立 ，A 0~n - 1 ∈ ℝr × nr 是保证
Φ ( A 0~n - 1) 稳定的参数矩阵。那么，当 x(0~n - 1) ∈ 𝔽

时，式（39）是亚全驱系统式（20）的一个亚镇定控
制器，其对应的闭环系统为
⎧x( )n ( )t + A 0~n - 1 x(0~n - 1) ( )t = 0
⎨ (0~n - 1) t ≥ 0 （41）
⎩x ( )t ∈ 𝔽
对应的指数吸引域为

Rs={X0| X0∈ ℝnr，φ(eϕ(A0~n - 1) t X 0，t) ≠ 0，t ≥ 0}

（42）
式中 φ( ⋅ ) 是亚全驱系统式（20）的奇异函数。

## [4] `aaas_2024_subsfs` (PDF p.7, L777)

定理 3 假设 1 成立 ，A 0~n - 1 ∈ ℝr × nr 是保证
Φ ( A 0~n - 1) 稳定的参数矩阵。那么，当 x(0~n - 1) ∈ 𝔽

时，式（48）是亚严反馈系统式（1）的一个亚镇定
控制器，其闭环系统从集合 R s 中出发的状态响
应为

⎧x1~n( )t = Bĕ -1 (x(0~n- 1) ，t) [x(0~n- 1) - he(x(0~n- 1) ，t)]

⎪⎪⎪⎨x(0~n- 1) ( )t = eΦ (A0~n- 1) t x(0~n- 1) ( )0 ( 49 )
⎪⎪⎪⎪x(0~n- 1) ( )0 ∈ Rs
⎩
且满足 x1~n(t) ∈ 𝔽̂，t ≥ 0。
在定理 2 的基础上，通过设计控制器式（39），
亚全驱系统的状态 x(0~n - 1) (t) 一致指数收敛到原

点。借助变换式（17），若 he(x(1~n - 1) ，t) 指数收敛

到 0，Bĕ -1 (x(0~n - 1) ，t) 一致有界 ，则亚严反馈系统

式（1）的状态 x1~n(t) 同样指数收敛到原点。

## [5] `aas_2020_part1` (PDF p.5, L498)

定理 1[33]. 当假设 A1 和 A2 成立时, 由系统
(19)-(20) 构成的串联系统可表述为如下三阶模型
...
A3 (θ, x, x ˙) x + A2 (θ, x, x ˙) ¨x + A1 (θ, x, x ˙) ˙x+

A0 (θ, x, x ˙) x + η (θ, x, x ˙) = B (θ, x, x ˙) u
(22)

式中:

A3 (θ, x, x ˙) = M (θ, x, x ˙)
dM (θ, x, x ˙)
A2 (θ, x, x ˙) = + D (θ, x, x ˙) −
dt
dB (θ, x, x ˙) −1
B (θ, x, x ˙) M (θ, x, x ˙)
dt
dD (θ, x, x ˙)
A1 (θ, x, x ˙) = + K (θ, x, x ˙) −
dt
dB (θ, x, x ˙) −1
B (θ, x, x ˙) D (θ, x, x ˙)
dt
dK (θ, x, x ˙)
A0 (θ, x, x ˙) = −
dt
dB (θ, x, x ˙) −1
B (θ, x, x ˙) K (θ, x, x ˙)
dt
d
η (θ, x, x ˙) = ξ (θ, x, x ˙) −
dt
B (θ, x, x ˙) f (θ, x, x, ˙ x, t ¨) −
dB (θ, x, x ˙) −1
B (θ, x, x ˙) ξ (θ, x, x ˙)
dt
另外中间变量 τ 可由下述关联方程给出:

τ = B−1(θ, x, x ˙) [M (θ, x, x ˙) ¨x + D (θ, x, x ˙) ˙x+
K (θ, x, x ˙) x + ξ (θ, x, x ˙)]

而上述出现的 f (θ, x, x, ˙ x, t ¨) 是通过在 f (τ, t) 中
将上述 τ 代入之后的结果.

## [6] `aas_2020_part1` (PDF p.6, L561)

定理 2. 记

GiGi+1 · · · Gj, i ≤ j
G˜i∼j =
In, i > j

则严格反馈型系统 (23) 可以转化为如下高阶全驱形
式
n
x(1n) − G˜1∼i−1fi(n−i)(x1, h2(·), · · · , hi(·)) =
i=1 其中
G˜1∼nu (24)

其中 hi(·) = hi(x1,x ˙1, · · · , x(1i−1)) 由下述递推公式
获得:
i
hi(·) = − G˜−k−11∼i−1fk (i−−1k) h1(·), h2(·), · · · ,
k=2
hk−1(·) + G˜−1∼1i−1x(1i−1),

i = 2, 3, · · · , n − 1

其递推初值为 h1(x1) = x1, 且系统 (23) 中的其它
变量由下述关联方程给出:

xi = hi(x1,x ˙1, · · · , x1(i−1)), i = 2, 3, · · · , n (25)

## [7] `aas_2020_part1` (PDF p.7, L707)

定理 3. 如果存在控制律 (37), 其中 β(x) 恒可
逆, 以及微分同胚变换

xˆ = T(x) (38)

可将系统 (36) 化成下述能控线性系统

x˙ˆ = Axˆ + Bv (39)

则亦存在微分同胚变换将系统 (36) 化成高阶全驱系
统.

## [8] `aas_2020_part1` (PDF p.9, L930)

定理 4. 如果假设 A3 成立, 则问题 ESA 有
解当且仅当 F ∈ F, 并且在这种情况下, 所有矩阵
V (Z, F) 由式 (55) 给出, 而

K = EZFm W∞ Ve−1(Z, F) (56)

其中 Ve(Z, F) 由式 (54)-(55) 给出, 而 W∞ ∈ Rn×nc
为任意的参数矩阵, Z ∈ Rn×nc 为满足

det Ve(Z, F) ≠ 0 (57)

的参数矩阵.

## [9] `aas_2020_part1` (PDF p.9, L991)

定理 5. 设矩阵 E 形如式 (63) 所示, 则 F 非空
当且仅当矩阵 F ∈ Rnc×nc 具有下述形式的若当标
准型:

JF = Blockdiag(J0, J1, · · · , Jm−2, Jm−1) (64)

其中

Ji∆ 0 n×n
Ji = ∈ C , i ∈ Nm−2 (65)

## [10] `aas_2020_part1` (PDF p.10, L1048)

定理 6. 设矩阵 E 如式 (63) 所示, 则
1) Z0(F), F ∈ F0, 为 Rn×nc 中的一个 Zariski
开集;
2) 当 Yi ∈ Rn0×n0, i ∈ Nm−1 和 Yi+ ∈
R(n−n0)×(n−n0), i ∈ Nm−2 均为非奇异时, 对于任
意的 F ∈ F0,

Y = Y0e Y1e · · · Yme−2 Yme−1 ∈ Z0(F)

其中

Yie = Yi 0 , Yi ∈ Rn0×n0, i ∈ Nm−2

## [11] `aas_2020_part2` (PDF p.4, L352)

定理 1. 系统 (8) 能控的充要条件是存在变换
T
x¯ = P−1x = x¯1 x¯2 · · · x¯n
[ ] (10)
{x¯i = z(i−1), i = 1, 2, · · · , n

其中 P ∈ Rn×n 为一可逆矩阵, 使得在此变换下系
统 (8) 等价于如下形式的标准高阶全驱系统

z(n) + αn−1z(n−1) + · · · + α1z + α0z = u (11)
˙
其中 αi, i = 0, 1, · · · , n − 1, 由式 (9) 给出.

## [12] `aas_2020_part2` (PDF p.5, L472)

定理 2. 多输入线性定常系统 (17) ∼ (22) 在下
述变换下
T
z = z1 z2 · · · zr ∈ Rr
[ ]
{xˆij = zi(j−1), i = 1, 2, · · · , r, j = 1, 2, · · · , µi
(23)

段广仁: 高阶系统方法 — II. 能控性与全驱性

等价于下述形式的高阶全驱系统:

Aµz(µ) + Aµ−1z(µ−1) + · · · + A1z + A0z = Bu˜
˙
(24)

其中

µ = max {µi, i = 1, 2, · · · , r} (25)

这里, µi, i = 1, 2, · · · , r, 为一组正整数, 满足 µ1 +
µ2 + · · · + µr = n;

Ak = αijk r×r , k = 0, 1, · · · , µ (26)
[ ]

1 b12 b13 · · · b1r
0 1 b23 · · · b2r
B˜ = 0 0 1 · · · b3r (27)

... ... ... ... ...
0 0 0 · · · 1

这里, αijk, bij, j, k = 1, 2, · · · , µi, i = 1, 2, · · · , r,
同式 (20) ∼ (22) 给出, 但满足下述约定:

αijk = 0, j, k > µi, i = 1, 2, · · · , r
{ µi (28)
αii = 1, i = 1, 2, · · · , r

## [13] `aas_2020_part2` (PDF p.6, L629)

定理 3. 非线性系统 (35) ∼ (37) 在变换

x¯i = z(i−1), i = 1, 2, · · · , n (38)

下等价于下述形式的高阶标准全驱系统:

z(n) = f(z,z, · · · , z(n−1), t) + u (39)
˙

## [14] `aas_2020_part2` (PDF p.7, L709)

定理 4. 多输入非线性系统 (42) ∼ (47) 在下述
变换下
T
z = z1 z2 · · · zr
[ ]
{xˆij = zi(j−1), j = 1, 2, · · · , µi, i = 1, 2, · · · , r
(48)

等价于如下形式的高阶全驱系统:

Ez(m) = f˜(z,z, ˙ · · · , z(m−1), t) + Bu˜ (49)

段广仁: 高阶系统方法 — II. 能控性与全驱性

其中

f1(·, t)
m−1
(m−1) f2(·, t) (i)
f˜(z,z, ˙ · · · , z , t) = + Eiz
· · · i∑=m0
fr(·, t)
(50)

矩阵 E 和 Ei, i = m0, m0 + 1, · · · , m − 1 为一组对
角线元素为 0 或 1 的非零对角矩阵,

m = max {µi, i = 1, 2, · · · , r}
{ (51)
m0 = min {µi, i = 1, 2, · · · , r}

而 B˜ ∈ Rr×r 分别由式 (27) 定义.

## [15] `aas_2020_part3` (PDF p.4, L427)

定理 1. 单输入单输出非线性系统能观规范型
(2) 等价于下述高阶全量测系统:

(n) n−1 (i) n−1 (i)
z + αiz = βi (z, u)
i=0 i=0 (22)
y = c(z)

9 期

其中 αi, βi(z, u), i = 0, 1, · · · , n − 1, 同能观规范
型 (2) 中定义, y = c(z) 是由 z 到 y 的微分同胚.

## [16] `aas_2020_part3` (PDF p.5, L518)

定理 2. 多输入多输出非线性系统能观规范型
(9) ∼ (15) 等价于下述形式的高阶全量测系统:

µ (i) µ−1 (i)
Aiz = Bi (z, u)
i=0 i=0 (28)
y = C(z)

其中 z ∈ Rm, y = C(z) 是由 z 到 y 的微分同胚,

µ = max {µi, i = 1, 2, · · · , m} (29)

b1k(z, u)

Ak = αijk m×m, Bk = ...
(30)
bmk(z, u)
k = 0, 1, · · · , µ

而 µi, i = 1, 2, · · · , m 为一组正整数, 满足

µ1 + µ2 + · · · + µm = n

αijk, k, j = 1, 2, · · · , µi; i = 1, 2, · · · , m 和
bij(z, u), j = 1, 2, · · · , µi; i = 1, 2, · · · , m 均由
规范型 (9) ∼ (15) 决定, 这里约定

αijk = 0, k > µi, j ≠ k, j = 1, 2, · · · , µi
αiiµi = 1, i = 1, 2, · · · , m
(31)

## [17] `fasta_2026_roea` (PDF p.3, L403)

Theorem 1. Suppose Condition 1 holds. For each interval
[ti−1, ti), i = 1, 2, . . . , p, the Ri in (18) admits the equiva-
lent representation

x
Ri = {[y ϕ1(t)x + ϕ2(t)y < d, ∀ t ∈ Ti(x, y)},
]
(19)
where the finite active set is given by

Ti(·)={ti−1, ti} ∪ {t∗∈(ti−1, ti)|ϕ′1(t∗)x+ϕ′2(t∗)y=0} .

Moreover, if the interior stationary point t∗ exists, it is
uniquely determined by

∗ 1 λ1(α1x + α2y)
t = ln(− ).
λ2 − λ1 λ2(β1x + β2y)

## [18] `fasta_2026_roea` (PDF p.5, L646)

Theorem 2. Suppose Condition 2 holds. For each interval
[tk−1, tk), k = 1, 2, . . . , q, the set Rk in (21) admits the
equivalent representation

n
Rk = {z1∼n ∈ ℝn ∑ϕi(t)zi < d, ∀ t ∈ Tk(z1∼n)},
i=1

where the active set is given by

n
Tk(·)={tk−1, tk} ∪{t∗∈(tk−1, tk) ∑ϕ′i(t∗)zi=0}.
i=1

## [19] `ijss_2021_part2` (PDF p.4, L399)

Theorem 2.1: Let Assumption A1 be satisfied, then,
under the following transformation

x1 = z
⎧x2 = G−11(z, ζ, t)[z˙ − f1(z, ζ, t)]
⎪⎪⎨xk+1 = L−k1(z(0∼k−1), ζ, t)[z(k) − hk(z(0∼k−1), ζ, t)]
⎪⎪⎩ k = 2, 3, . . . , n − 1,
(5)
the generalised strict-feedback nonlinear system (3) can
be transformed into the following HOFA system

z(n) = hn(z(0∼n−1), ζ, t) + Ln(z(0∼n−1), ζ, t)u, (6)

where the matrix function Lk(z(0∼k−1), ζ, t) and the
vector function hk(z(0∼k−1), ζ, t) are recursively given

by

Lk(z(0∼k−1), ζ, t)

= Lk−1(z(0∼k−2), ζ, t)Gk(x1(0∼∼k1−)1, xk, ζ, t), (7)

and

hk(z(0∼k−1), ζ, t)

= h˙k−1(z(0∼k−2), ζ, t) + L˙k−1(z(0∼k−2), ζ, t)xk

+ Lk−1(z(0∼k−2), ζ, t)fk(x1(0∼∼k1−)1, xk, ζ, t),

k = 1, 2, . . . , n (8)

with the initial values

L0(ζ, t) = Ir, h0(ζ, t) = 0, (9)

where in (7)–(8) the xi, i = 2, 3, . . . , n and their deriva-
tives are all given or determined by the transformation
(5).

For a proof of the theorem, please refer to the
Appendix.

## [20] `ijss_2021_part2` (PDF p.5, L508)

Theorem 2.2: Let Assumption A2 be met, then, under
the following transformation

x1 = z
⎧x2 = G−11(z(0∼1), ζ, t)[z¨ − f1(z(0∼1), ζ, t)]
⎪⎪⎪⎪⎨xk+1 = L−k1(z(0∼2k−1), ζ, t) (12)
×[z(2k) − hk(z(0∼2k−1), ζ, t)],
⎪⎪⎪⎪⎩ k = 2, 3, . . . , n − 1

the SFS (11) can be equivalently converted into the
following HOFA model

z(2n) = hn(z(0∼2n−1), ζ, t) + Ln(z(0∼2n−1), ζ, t)u,
(13)
where the functions Lk(z(0∼2k−1), ζ, t) and hk
(z(0∼2k−1), ζ, t) are given recursively by

Lk(z(0∼2k−1), ζ, t)

= Lk−1(z(0∼2k−3), ζ, t)Gk(x(0∼2) , x(0∼1), ζ, t),
1∼k−1 k
(14)

and

hk(z(0∼2k−1), ζ, t)

= h¨k−1(z(0∼2k−3), ζ, t) + L¨k−1(z(0∼2k−3), ζ, t)xk

+ 2L˙k−1(z(0∼2k−3), ζ, t)x˙k

+ Lk−1(z(0∼2k−3), ζ, t)fk(x(0∼2) , x(0∼1), ζ, t),
1∼k−1 k
k = 1, 2, . . . , n, (15)

with the initial values

L0(ζ, t) = Ir, h0(ζ, t) = 0, (16)

where in (14)–(47) the xi, i = 2, 3, . . . , n, and their
derivatives are given or determined by the transforma-
tion (42).

For a proof of the theorem, please refer to the
Appendix.
It is noted that facts similar to those mentioned in
the Remarks 2.1 and 2.2 also hold true in this second-
order case.
The SFS (11) clearly has the following companion
form:

⎧x¨1 = f1(x1,x ˙1, ζ, t) + G1(x1,x ˙1, ζ, t)x˙2
x2 = f2(x1(0∼2), x2(0∼1), ζ, t)
¨
+G2(x1(0∼2), x2(0∼1), ζ, t)x3
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ ˙
...
(0∼2) (0∼1) (17)
x¨n−1 = fn−1(x1∼n−2, xn−1 , ζ, t)
+Gn−1(x1(0∼∼n2−)2, xn(0−∼11), ζ, t)x˙n
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩x¨n = fn(x1(0∼∼n2−)1, xn(0∼1), ζ, t)
+Gn(x1(0∼∼n2−)1, xn(0∼1), ζ, t)u.

Following the same procedure, the above SFS (17) can
also be converted into a HOFA model. We remark that
the derivation process is even simpler since for this

## [21] `ijss_2021_part2` (PDF p.6, L629)

Theorem 2.3: Let Assumption A3 hold, then, under the
following transformation

x1 = z
⎧x2 = G−11(z(0∼m1−1), ζ, t)
⎪⎪⎪⎪⎨ ×[z(m1) − f1(z(0∼m1−1), ζ, t)]
xi+1 = L−i1(z(0∼pi−1), ζ, t)[z(pi) − hi(z(0∼pi−1), ζ, t)],
⎪⎪⎪⎪⎩ i = 2, 3, . . . , n − 1,
(20)
the SFS (18) can be equivalently turned into the follow-
ing HOFA system

z(p) = hn(z(0∼p−1), ζ, t) + Ln(z(0∼p−1), ζ, t)u, (21)

where the functions Lk(z(0∼pk−1), ζ, t) and hk
(z(0∼pk−1), ζ, t) are recursively given by

Lk(z(0∼pk−1), ζ, t)

= Lk−1(z(0∼pk−1−1), ζ, t)

× Gk(xi(0∼mi)|i=1∼k−1, xk(0∼mk−1), ζ, t), (22)

and

hk(z(0∼pk−1), ζ, t)

= h(mk)(z(0∼pk−1−1), ζ, t)
k−1
mk−1
+ C(j, mk)L(mk−j)(z(0∼pk−1−1), ζ, t)x(j)
∑ k−1 k
j=0

+ Lk−1(x1(0∼pk−1−1), ζ, t)fk(xi(0∼mi)|i=1∼k−1,

x(0∼mk−1), ζ, t), k = 1, 2, . . . , n, (23)
k

with the initial values

L0(ζ, t) = Ir, h0(ζ, t) = 0, (24)

where in (22)–(23) the xk, k = 2, 3, . . . , n and their
derivatives are given or determined by the transforma-
tion (20).

Parallel to the second-order SFS (17), the mixed-
order SFS (18) also has the following generalised form:

x(m1) = f1(x(0∼m1−1), ζ, t)
⎧ 1 1 (0∼m1−1) (m◦1)
+G1(x1 , ζ, t)x2
x(m2) = f2(x(0∼m1), x(0∼m2−1), ζ, t)
2 1 2 ◦
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ +G2(x(0∼m1), x(0∼m2−1), ζ, t)x(m2)
1 2 3
...
xn(m−n1−1) = fn−1(xi(0∼mi)|i=1∼n−2, xn(0−∼1mn−1−1), ζ, t)
+Gn−1(xi(0∼mi)|i=1∼n−2,
(0∼mn−1−1) (m◦n−1)
xn−1 , ζ, t)xn
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩xn(mn) = fn(xi(0∼mi)|i=1∼n−1, xn(0∼mn−1), ζ, t)
+Gn(xi(0∼mi)|i=1∼n−1, xn(0∼mn−1), ζ, t)u,
(25)
where m◦i < mi, i = 1, 2, . . . , n − 1, are another set of

## [22] `ijss_2021_part2` (PDF p.7, L747)

Theorem 3.1: Let Condition C1 be satisfied, then,
under the following transformation

x1 = z
⎧x2 = G−11[z˙ − f1(z, ζ, t)]
⎪⎪⎨xk+1 = L−k1[z(k) − hk(z(0∼k−1), ζ, t)] (27)
⎪⎪⎩ k = 2, 3, . . . , n − 1,

the generalised strict-feedback nonlinear system (3) can
be equivalently transformed into the following HOFA

model

z(n) = hn(z(0∼n−1), ζ, t) + Ln(z(0∼n−1), ζ, t)u, (28)

with

{Lk = G1G2 · · · Gk, k = 1, 2, . . . , n − 1
Ln(z(0∼n−1), ζ, t) = Ln−1Gn(x1(0∼∼n1−)1, xn, ζ, t),
(29)
and

hk(z(0∼k−1), ζ, t)

f1(k−1)(z, ζ, t)
⎡ (k−2) (0∼1) ⎤
f2 (z , x2, ζ, t)

= L0∼k−1 ... ,
⎢⎢⎢⎢⎢⎢⎣f˙k−1(x1(0∼∼k1−)2, xk−1, ζ, t)⎥⎥⎥⎥⎥⎥⎦
fk(x1(0∼∼k1−)1, xk, ζ, t)

k = 1, 2, . . . , n, (30)

where L0 = I, and in (29)–(30) the xk, k = 2, 3, . . . , n
and their derivatives are all given or determined by the
transformation (27).

## [23] `ijss_2021_part2` (PDF p.8, L857)

Theorem 3.2: Let Condition C2 be met, then, under the
following transformation

x1 = z
⎧x2 = G−11[z¨ − f1(z(0∼1), ζ, t)]
⎪⎪⎨xk+1 = L−1[z(2k) − hk(z(0∼2k−1), ζ, t)], (35)
k
⎪⎪⎩ k = 2, 3, . . . , n − 1

the SFS (11) can be equivalently transformed into the
following HOFA model

z(2n) = hn(z(0∼2n−1), ζ, t) + Ln(z(0∼2n−1), ζ, t)u,
(36)
with

{Lk = G1G2 · · · Gk, k = 1, 2, . . . , n − 1
Ln(z(0∼2n−1), ζ, t) = Ln−1Gn(x1(0∼∼n2−)1, xn(0∼1), ζ, t),
(37)

and

hk(z(0∼2k−1), ζ, t)

f(2(k−1))(z(0∼1), ζ, t)
⎡ (2(k1−2)) (0∼2) (0∼1) ⎤
f2 (x1 , x2 , ζ, t)
= L(0∼k−1) ... ,
⎢⎢⎢⎢⎢⎢⎣ f¨k−1(x(0∼2) , x(0∼1), ζ, t) ⎥⎥⎥⎥⎥⎥⎦
1∼k−2 k−1
fk(x(0∼2) , x(0∼1), ζ, t)
1∼k−1 k
k = 1, 2, . . . , n, (38)

where L0 = I, and in (37)–(38) the xk, k = 2, 3, . . . , n,
and their derivatives are given or determined by the
transformation (35).

For the mostly encountered case of n = 2, the above
result becomes the following.

## [24] `ijss_2021_part2` (PDF p.9, L958)

Theorem 3.4: Let Condition C3 be met, then, under the
following transformation

x1 = z
⎧x2 = G−11[z(m1) − f1(z(0∼m1−1), ζ, t)]
⎪⎪⎨xk+1 = L−k1[z(pk) − hk(z(0∼pk−1), ζ, t)], (46)
⎪⎪⎩ k = 2, 3, . . . , n − 1,

the SFS (18) can be equivalently turned into the follow-
ing HOFA model

z(p) = hn(z(0∼p−1), ζ, t) + Ln(z(0∼p−1), ζ, t)u, (47)

with

Lk = G1G2 · · · Gk, k = 1, 2, . . . , n − 1
⎧⎨Ln(z(0∼p−1), ζ, t)
= Ln−1Gn(xi(0∼mi)|i=1∼n−1, xn(0∼mn−1), ζ, t),
⎩ (48)
and

hk(z(0∼pk−1), ζ, t)

= L0∼k−1

f(p2∼k)(z(0∼m1−1), ζ, t)
⎡ (p3∼k)1 (0∼m1−1) (0∼m2−1) ⎤
f2 (x1 , x2 , ζ, t)
× ...
⎢⎢⎢⎢⎢⎢⎣f(mk)(x(0∼mi)|i=1∼k−2, x(0∼mk−1−1), ζ, t)⎥⎥⎥⎥⎥⎥⎦
k−1 i k−1
fk(xi(0∼mi)|i=1∼k−1, xk(0∼mk−1), ζ, t)

k = 1, 2, . . . , n, (49)

where L0 = I, and in (48)–(49) the xk, k = 2, 3, . . . , n
and their derivatives are given or determined by the
transformation (46).

For the often encountered case of n = 3, the above
result reduces to the following.

## [25] `ijss_2021_part2` (PDF p.10, L1063)

Theorem 3.6: Let Condition C3 be met, then there
exists an invertible transformation

xk = Tk(z(0∼p−1), ζ, t), k = 1, 2, . . . , n, (56)

such that the mixed-ordr SFS (18), with fk’s given by
(55), can be equivalently transformed into the following
HOFA model

ω
z(p) = hl(z(0∼p−1), ζ, t) + L(z(0∼p−1), ζ, t)u,
∑
l=1
(57)
with

L(z(0∼p−1), ζ, t)

= G1G2 · · · Gn−1

× Gn(xi(0∼mi)|i=1∼n−1, xn(0∼mn−1), ζ, t), (58)

and

hl(z(0∼p−1), ζ, t)

= L0∼n−1

f(p2∼n)(z(0∼m1−1), ζ, t)
⎡ (p3∼n)1l (0∼m1−1) (0∼m2−1) ⎤
f2l (x1 , x2 , ζ, t)
× ...
⎢⎢⎢⎢⎢⎢⎣f(mn)(x(0∼mi)|i=1∼n−2, x(0∼mn−1−1), ζ, t)⎥⎥⎥⎥⎥⎥⎦
n−1,l i n−1
fn,l(xi(0∼mi)|i=1∼n−1, xn(0∼mn−1), ζ, t),
(59)

where L0 = I, and in (58)–(59) the xk, k = 2, 3, . . . , n
and their derivatives are given by the transformation
(56).

## [26] `ijss_2021_part2` (PDF p.10, L1105)

Theorem 2.3. With the relation (55), the formula (49)
becomes

hk(z(0∼pk−1), ζ, t)

⎡ f1(p2∼k)(z(0∼m1−1), ζ, t) ⎤
f(p3∼k)(x(0∼m1), x(0∼m2−1), ζ, t)
2 1 2
= L0∼k−1 ...
⎢⎢⎢⎢⎢⎢⎢⎣fk(−m1k)(xi(0∼mi)|i=1∼k−2, xk(0−∼1mk−1−1), ζ, t)⎥⎥⎥⎥⎥⎥⎥⎦
fk(xi(0∼mi)|i=1∼k−1, xk(0∼mk−1), ζ, t)

ω
⎡ f(p2∼k)(z(0∼m1−1), ζ, t) ⎤
∑ 1l
ω l=1
f(p3∼k)(x(0∼m1), x(0∼m2−1), ζ, t)
∑ 2l 1 2
l=1
= L0∼k−1 ...
⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎢⎣ ω ⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎥⎦
∑fk(−m1,k)l(xi(0∼mi)|i=1∼k−2, xk(0−∼1mk−1−1), ζ, t)
l=1ω
∑fk,l(xi(0∼mi)|i=1∼k−1, xk(0∼mk−1), ζ, t)
l=1
f(p2∼k)(z(0∼m1−1), ζ, t)
⎛ ⎡ (p3∼k1)l (0∼m1) (0∼m2−1) ⎤⎞
ω f2l (x1 , x2 , ζ, t)
= ∑ L0∼k−1 ...
l=1 ⎜⎜⎜⎜⎜⎜⎜⎝ ⎢⎢⎢⎢⎢⎢⎢⎣f(mk)(xi(0∼mi)|i=1∼k−2, x(0∼mk−1−1), ζ, t)⎥⎥⎥⎥⎥⎥⎥⎦⎟⎟⎟⎟⎟⎟⎟⎠
k−1,l (0∼mi) (k0−∼1mk−1)
fk,l(xi |i=1∼k−1, xk , ζ, t)
ω
= ∑hk,j(z(0∼pk−1), ζ, t),
l=1

which gives (59). While the other relations hold obvi-
ously. ■

The above result indicates an important fact: if the
nonlinear term in each subsystem of the SFS (18) is
the sum of several individual nonlinear terms, then
the nonlinear term in the obtained equivalent HOFA
model is also the sum of the same number of individual
ones correspondingly.

## [27] `ijss_2021_part3` (PDF p.6, L594)

Theorem 3.4: Suppose that system (2) satisfies
Assumption A1 and Condition 1. Let μ and ε be two
arbitrarily given positive numbers, and Ai ∈ ℝr×r, i =
0, 1, . . . , n − 1 be a set of matrices satisfying (9). Then,
the following control law

⎧u = −L−1(x(0∼n−1))(A0∼n−1x(0∼n−1) + u∗)

⎪⎪⎪⎨u∗ = f (x(0∼n−1))+ 1 ρ2(x(0∼n−1))
4ε
×PT(A0∼n−1)x(0∼n−1),
⎪⎪⎪⎩ L
(14)

for the uncertain system (2) guarantees that the state
x(0∼n−1) converges into the following ellipsoid centred
at the origin:

Θμ,ε(0)

= {x(0∼n−1) x(0∼n−1) TP(A0∼n−1)x(0∼n−1) ≤ ε }.
||||( ) μ

## [28] `ijss_2021_part3` (PDF p.8, L786)

Theorem 3.5: Suppose that system (2) satisfies Assump-
tion A1 and Condition 1. Let μ and ε be two arbi-
trarily given positive numbers, and Ai ∈ ℝr×r, i =
0, 1, . . . , n − 1 be a set of matrices satisfying (9). Then,
the following control law

u = −L−1(x(0∼n−1)) A0∼n−1x(0∼n−1) + u∗
( )

u∗ = 1 ρ2(x(0∼n−1))PT(A0∼n−1)x(0∼n−1)
4ε L
+f (x(0∼n−1)) − u0(x∗),

with

u0(x∗) = (x∗)(n) − A0∼n−1(x∗)(0∼n−1)

− 1 ρ2(x(0∼n−1))PT(A0∼n−1)(x∗)(0∼n−1),
4ε L

guarantees that the state x(0∼n−1) converges globally
into the following ellipsoidal belt-shaped region centred
at (x∗)(0∼n−1) :

Θμ,ε((x∗)(0∼n−1))

= {x(0∼n−1) ((x − x∗)(0∼n−1))TP(x − x∗)(0∼n−1) ≤ ε }.
|||| μ

## [29] `ijss_2021_part3` (PDF p.13, L1288)

Theorem 4.1: Suppose that Assumption A2 holds. Let
μ and ε be two arbitrarily given positive numbers, and
A0i∼1, Pi(A(i0∼1)) and PiL(A(i0∼1)), i = 1, 2, . . . , n − 1
be three sets of matrices as described above. Assume that
there exist a set of non-negative continuous scalar func-
tions ρi(x1(0∼∼i1)), i = 1, 2, . . . , n satisfying (65). Then,
the controller (66) for the uncertain second-order SFS
(3) guarantees that the transformed state z(0∼1) con-
1∼n
verges into the following ellipsoid:

{ (0∼1) n (0∼1) T (0∼1) (0∼1) nε }
z1∼n ∑[(z1∼i ) Pi(Ai )z1∼i ] ⩽ .
|||||i=1 μ

It follows from the above theorem that the state
zi(0∼1), i = 1, 2, . . . , n of each subsystem eventually
converges into the following ellipsoid centred at the
origin:

μ,ε
Θi (0)

= {z(0∼1) z(0∼1) TPi(A(0∼1))z(0∼1)⩽ nε },
i ||||( i ) i i μ

which implies that the state x(0∼1) of the original sys-
1
tem also converges into the following ellipsoid centred
at the origin:

μ,ε
Θ1 (0)

= {x(0∼1) x(0∼1) TP1(A(0∼1))x(0∼1)⩽ nε }.
1 ||||( 1 ) 1 1 μ

## [30] `ijss_2021_part3` (PDF p.16, L1665)

Theorem 5.1: Suppose that Assumption A3 holds.
Let μ and ε be two arbitrarily given positive num-
bers, and A0i∼mi−1 ∈ ℝ1×mi, i = 1, 2, . . . , n be a set
of matrices satisfying (77). Assume that there exist
a set of non-negative continuous scalar functions
ρk(zi(0∼mi−1)|i=1∼k), k = 1, 2, . . . , n satisfying (102).
Then, the controller (103) for the uncertain high-
order SFS (5) guarantees that the transformed states
z(0∼mi−1), i = 1, 2, . . . , n finally converge into the fol-
i
lowing ellipsoid:

Θμ,ε(0)

= {z(0∼mi−1)|i=1∼n n z(0∼mi−1) TPiz(0∼mi−1) ≤nε },
i |||||∑( i ) i μ
i=1

where Pi = Pi(A0i∼mi−1).

It is known from the above theorem that the states
z(0∼mi−1), i = 1, 2, . . . , n of each subsystem eventually
i
converge into the following ellipsoid centred at the
origin:

Θμ,ε(0) = {z(0∼mi−1) z(0∼mi−1) TPiz(0∼mi−1) ≤ nε }.
i i ||||( i ) i μ

Since z1 = x1, the state x1(0∼m1−1) converges into the
following ellipsoid centred at the origin:

Θμ,ε(0) = {x(0∼m1−1) x(0∼m1−1) TP1x(0∼m1−1) ≤ nε }.
1 1 ||||( 1 ) 1 μ

To end this section, we make a few remarks.

## [31] `ijss_2021_part4` (PDF p.6, L522)

Theorem 3.1: Suppose that Assumption A1 holds. Let
Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1 be a set of matrices such
that the matrix Φ(A0∼n−1) is stable, and PL(A0∼n−1)
be given by (6)–(8). Then, for any unknown constant
vector θ ∈ ℝm, there exists an adaptive control law

θ˙ˆ = H(x(0∼n−1))PT(A0∼n−1)x(0∼n−1)
⎧ L
⎪⎪⎪⎨ u = −L−1(x(0∼n−1)) A0∼n−1x(0∼n−1) + u∗
( )

⎪⎪⎪⎩u∗ = HT(x(0∼n−1))θˆ + q(x(0∼n−1)),
(9)
for the system (1) such that the states of the closed-loop
system satisfy

(1) x(0∼n−1) → 0, t → ∞;
(2) ‖θ − θˆ‖ is bounded.

## [32] `ijss_2021_part4` (PDF p.7, L663)

Theorem 3.2: Suppose that the system (1) satisfies

## [33] `ijss_2021_part4` (PDF p.11, L1214)

Theorem 4.1: Let Assumption A2 hold, and A0i∼1 ∈
ℝ1×2, i = 1, 2, . . . , n be a set of matrices such that
Φ(A0i∼1) ∈ ℝ2×2, i = 1, 2, . . . , n are stable. Then, for
any set of unknown constant parameters ϑi ∈ ℝ, i =
1, 2, . . . , n, the adaptive control law (54) for the second-
order SFS (2) guarantees that

(1) zi(0∼1) → 0, t → ∞, i = 1, 2, . . . , n;
(2) ‖θi − θˆi‖, i = 1, 2, . . . , n are bounded.

It follows from the above theorem that x1 →
0, t → ∞. However, if the state transformation
(57) is a diffeomorphism from x1∼n to z1∼n, and
x1∼n(0) = z1∼n(0), or equivalently, αi−1(x1∼i(0)) =
0, i = 2, 3, . . . , n, then we also have

xi(0∼1) → 0, t → ∞, i = 1, 2, . . . , n.

## [34] `ijss_2021_part4` (PDF p.14, L1554)

Theorem 5.1: Let Assumption A3 hold, and A0∼mi−1∈
i
ℝ1×mi, i = 1, 2, . . . , n be a set of matrices which make
Φ(A0i∼mi−1), i = 1, 2, . . . , n stable. Then, for any set of
unknown constant parameters ϑi ∈ ℝ, i = 1, 2, . . . , n,
the adaptive control law (87) for the system (4) guaran-
tees that

(1) zi(0∼mi−1) → 0, t → ∞, i = 1, 2, . . . , n;
(2) ‖θi − θˆi‖, i = 1, 2, . . . , n are bounded.

Since z1 = x1, we have
x(0∼m1−1) → 0, t → ∞.
1

In order to let x1(t) track asymptotically some suf-
ficiently smooth reference signal x1∗(t), it suffices to

substitute, in the second- or high-order methods of
backstepping, the equation (21) or (66) by

z(0∼1) = x(0∼1) − x∗ (0∼1) ,
1 1 ( 1)

or

z(0∼m1−1) = x(0∼m1−1) − x∗ (0∼m1−1) ,
1 1 ( 1)

and then deal with the terms related to the reference
signal x1∗(t) properly in the sequential processes.
In description, the above backstepping method of
high-order systems appears to be much more com-
plicated. Yet it should be noted that in many specific
engineering applications, mi, i = 1, 2, . . . , n often take
the values of 1 and 2, and in such applications, the
mixed-order backstepping method is in fact simpler
than the second-order backstepping method.

## [35] `ijss_2021_part5` (PDF p.6, L556)

Theorem 3.1: Suppose that HOFA system (3), together
with the pre-estimation θ0 of the unknown parameter
vector θ, satisfies Assumptions A1–A3 . Let μ and ε be
two arbitrarily selected non-negative real numbers, and
Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1, be a set of matrices sat-
isfying (7). Then, control law (12)–(15) for system (3)
guarantees that the state x(0∼n−1) of the closed-loop sys-

tem and the parameter estimation error θ˜ converge to
the following ellipsoid:

Θ(μ,ε,δ)(0)

x(0∼n−1) (0∼n−1) 2 2 ε + δ
= {[ x + θ ˜ ≤ 2 },
θ˜ ]||||‖‖‖ ‖‖‖P ‖‖‖ ‖‖‖ μ

where

δ = 1 δ12 + (μ + 1) δ2 . (16)
( )

## [36] `ijss_2021_part5` (PDF p.9, L840)

Theorem 4.1: Suppose that HOFA system (3), together
with a pre-estimation θ0 of the unknown parameter
vector θ, satisfies Assumptions A1–A3. Let μ and ε
be two arbitrarily selected positive real numbers, and
Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1, be a set of matrices sat-
isfying (7). Then, control law (41)–(66) for uncertain
system (3) guarantees that the tracking errorx ˜ = x − x∗
and the parameter estimation error θ˜ converge to the
following ellipsoid:

x(0∼n−1)
Θ(μ,ε,δ)([˜ ])
θ˜

x˜(0∼n−1) (0∼n−1) 2 2 ε + δ
= {[ x˜ + θ ˜ ⩽ 2 }.
θ˜ ] ||||‖‖‖ ‖‖‖P ‖‖‖ ‖‖‖ μ

To end this section, we further present some related
remarks.

## [37] `ijss_2021_part5` (PDF p.10, L967)

Theorem 5.1: Suppose that HOFA system (3) satis-
fies Assumptions A1 and A2’, and the parameter vector
θ is constant. Let μ and ε be two selected positive real
numbers, with ε ≤ 1, and Ai ∈ ℝr×r, i = 0, 1, . . . , n −
1, be a set of matrices satisfying (7). Then, the control
law given by (12)–(13) and (48)–(49), for system (3),
guarantees

• limt→∞ ‖x(0∼n−1)‖= 0;
• ‖ θ˜‖ is bounded.

## [38] `ijss_2021_part6` (PDF p.8, L809)

Theorem 3.4: For an arbitrarily selected matrix F ∈
ℝnr×nr, all the matrices A0∼n−1 and V ∈ ℝnr×nr sat-
isfying det V ≠ 0 and

Φ(A0∼n−1) = VFV−1 (29)

are given by

A0∼n−1 = −ZFnV−1(Z, F) (30)

and (26), with Z ∈ ℝr×nr being a parameter matrix
satisfying

det V(Z, F) ≠ 0. (31)

## [39] `ijss_2021_part6` (PDF p.9, L859)

Theorem 3.5: Let F ∈ ℝnr×nr be a given Hurwitz
matrix, and fi ∈ ℝ and Fi ∈ ℝnr×nr, i = 0, 1, 2, . . . , nr
are determined by
nr
det(sI + F) = ∑fisi, (35)
i=0

and
nr−1
adj(sI + F) = ∑ Fisi, (36)
i=0
respectively. If the control law for the HOFA system (17)
is taken as (18), with A0∼n−1 being given by (30), then
we have

‖Gdy(s)‖22 = trace((CV)P1(CV)T)

= trace((V−1BcE)TP2(V−1BcE)), (37)

where V is given by (26), and

nr−1
⎧P1 = − Fi(V−1BcE)(V−1BcE)TP10−1(FT)i
∑
⎪⎪⎪⎪⎪⎨ i=0
nr−1
P2 = − ∑ FiT(CV)T(CV)P20−1Fi,
⎪⎪⎪⎪⎪⎩ i=0
(38)
with
nr nr
P10 = ∑fi(FT)i, P20 = ∑fiFi. (39)
i=0 i=0

## [40] `ijss_2021_part6` (PDF p.11, L1159)

Theorem 4.3: Let the HOFA system (44), with the
disturbance d(t) generated by (13), satisfies Assump-
tion A1. If the control law is taken as (59)–(61), with
the parameter matrices Lx, Ld, F1, Z1 and Z2 satisfying
the following conditions:

(1) Lx and Ld are any matrices making

Φ(00∼n−1) BcE
Ace = [ ]
0 Φ(S0∼k−1)

Lx
+ [ ][Cm 0] (62)
Ld

stable;
(2) the parameter F1 is Hurwitz, and also satisfies,
together with the parameter Z1, the condition
det V(F1, Z1) ≠ 0; and
(3) the parameter Z2 in the expressions of Π and Γ
given by (61) satisfies

Z2
⎡ ⎤
Z2Φ(S0∼k−1)
Cr 0. (63)
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ =
Z2Φk−1(S0∼k−1)

Then the following closed-loop system is internally
asymptotically stable:

x(0∼n−1)
⎡˙ ⎤
x˙ˆ(0∼n−1)

⎢⎢⎣d˙ˆ(0∼k−1)⎥⎥⎦

Φ(00∼n−1) −BcK0∼n−1 Ac2
⎡ ⎤
= −LxCm Ac1 BcE + Ac2
⎣ −LdCm LdCm Φ(S0∼k−1)⎦
x(0∼n−1)
× ⎡x(0∼n−1)⎤ (64)
ˆ
⎣dˆ(0∼k−1)⎦

where

Ac1 = Φ(00∼n−1) + LxCm − BcK0∼n−1,

Ac2 = Bc(Γ + K0∼n−1Π.

Furthermore, for any initial values x(0∼n−1)(0),
ζ(0) and d(0∼k−1)(0), the following asymptotic
output regulation requirement is always met

lim yr(t) = 0. (65)
t→∞

## [41] `ijss_2021_part6` (PDF p.13, L1328)

Theorem 4.4: The matrix pair (ΦE, CI) defined by (72)
is observable (detectable) if and only if (Φ(S0∼k−1), E)
is observable (detectable).

## [42] `ijss_2021_part6` (PDF p.13, L1396)

Theorem 4.5: Suppose that ΦE and CI are given
by (72) and (Φ(S0∼k−1), E) is observable. Let N(s) and
D(s) be a pair of right coprime polynomial matrices in
the form of (79) and satisfy the RCF (77), and F0 ∈
R(nr+kp)×(nr+kp)be a given Hurwitz matrix. Then all the

gain matrices Lx and Ld and the nonsingular matrix T
satisfying

T
(ΦE + [Lx]CE) = TF0T−1, (80)
Ld

can be given by

⎧[Lx] = T−TGT
Ld
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ ω [Di] i
T = ∑ Z0F0 (81)
i=0 Ni
ω+1
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩G = ∑[Di−1 − ΦT(00∼n−1)Di]Z0F0i,
i=0

where

Dω+1 = D−1 = 0, (82)

and Z0 ∈ ℝnr×(nr+kp) is a parameter matrix satisfying

ω
det( [Di]Z0Fi) ≠ 0. (83)
∑ Ni
i=0

## [43] `ijss_2021_part7` (PDF p.17, L1763)

Theorem 5.1: Let k ∈ {1, 2, . . . , η}. Then, for an arbi-
trarily selected matrix Fk ∈ ℝμkrk×μkrk, all the matrices
[Ak]0∼μk−1 and Vk ∈ ℝμkrk×μkrk satisfying det Vk ≠
0 and

Φk [Ak]0∼μk−1 = VkFkVk−1 (70)
( )
are given by

[Ak]0∼μk−1 = −ZkFkμkVk−1(Zk, Fk) , (71)

and
Zk
⎡ ⎤
ZkFk
Vk = Vk (Zk, Fk) = (72)
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
ZkFμk−1
k
with Zk ∈ ℝrk×μkrk being a parameter matrix satisfying

det Vk (Zk, Fk) ≠ 0. (73)

The above theorem clearly establishes a general
parametric solution of the controller for each sub-
system in (65), which arbitrarily assigns the desired
eigenstructure of the closed-loop subsystem (68). Fur-
ther, let

F = blockdiag F1, F2, . . . , Fη ,
( )
V = blockdiag V1, V2, . . . , Vη ,
( )
the whole closed-loop system can be obtained as

x(0∼μk−1)| VFV−1 x(0∼μk−1)| , (74)
˙k k=1∼η = ( ) k k=1∼η

which has a clear arbitrarily assignable eigenstructure.
Particularly, the closed-loop eigenvalues (or poles) are
given by the eigenvalues of the matrix F, or equiva-
lently, given by the eigenvalues of Fk, k = 1, 2, . . . , η.
The design degrees of freedom provided in the whole
design are composed of two parts, the first part lies in
the choice of the matrix F, and the second part is given
by Zk ∈ ℝrk×μkrk, k = 1, 2, . . . , η, which accounts

dfreedomd = μ1r12 + μ2r22 + · · · + μηrη2. (75)

These degrees of freedom can be properly utilised
to achieve additional system performance (see, e.g.
Duan, 1992, 1993; Duan et al., 2000, 2002, and Duan
& Zhao, 2020).

## [44] `ijss_2022_part10` (PDF p.7, L772)

Theorem 3.4: The linear system (2) is controllable if
and only if it can be converted equivalently into both a

step forward HOFA system in the form of (15), and a
step backward HOFA system in the form of (16).

The above theorem is a very important and insight-
ful discovery, which indicates that the step forward
and the step backward HOFA models are in fact
the controllability canonical forms of the state-space
system (2).

## [45] `ijss_2022_part10` (PDF p.12, L1255)

Theorem 5.1: Let ∅ ≠ 𝔽 ⊂ 𝔹nrℕ be the set of feasible
trajectories of the system (29). Further, let ϖ be an inte-
ger satisfying 1 ≤ ϖ ≤ n, and A0∼ϖ−1 ∈ ℝϖ×r be an
arbitrarily given matrix. Then the following controller

u (k) = B−1 (·) −f x⌈0∼n−1⌉(k) , k + u∗(k)
{u∗(k) = A0∼ϖ−[1x⌈0(∼ϖ−1⌉(k) + v ()k) , ]
(46)

for system (32) produces the following constant linear
closed-loop system

x (k + 1) = A0∼ϖ−1x⌈0∼ϖ−1⌉(k) + v (k) ,

provided that the states of the above closed-loop system
(49) are all feasible trajectories, that is,

x⌈0∼ϖ−1⌉(k) ∈ 𝔽. (47)

In the case of ϖ = 1, we have

u∗(k) = A0x (k) + v (k) ,

and the closed-loop system is

x (k + 1) = A0x (k) + v (k) .

While in the case of ϖ = n, we have

u∗(k) = A0∼n−1x⌈0∼n−1⌉(k) + v (k) ,

and the closed-loop system is

x (k + 1) = A0∼n−1x⌈0∼n−1⌉(k) + v (k) .

In practical applications, the integer ϖ may be cho-
sen according to the requirement on the closed-loop

system. For e.g. if there is a requirement on both x(k)
and x(k − 1), then ϖ should be chosen at least greater
than 2.

## [46] `ijss_2022_part10` (PDF p.12, L1303)

Theorem 5.2: Let ∅ ≠ 𝔽 ⊂ 𝔹κℕ be the set of feasi-
ble trajectories of the system (32). Further, let ϖi, i =
1, 2, . . . , η, be a set of integers satisfying

1 ≤ ϖi, i = 1, 2, . . . , η,

and [Ai]0∼ϖi−1 ∈ ℝri×ϖiri, i = 1, 2, . . . , η, be a set of
arbitrarily given matrices. Then the following controller

⎧u (k) = B−1
⌈0∼μp−1⌉ ∗
(·)[−f (xp (k) |p=1∼η, k) + u (k)]
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ ⌈0∼ϖ1−1⌉
⎡[A1]0∼ϖ1−1 x1 (k)⎤
[A2]0∼ϖ2−1 x2⌈0∼ϖ2−1⌉(k)
u∗(k) = + v (k) ,
⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎦
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ ⌈0∼ϖη−1⌉
[Aη]0∼ϖη−1xη (k)
(48)

for system (32) produces the following constant linear
closed-loop system

⌈0∼ϖp−1⌉
xp (k + 1) = [Ap]0∼ϖp−1xp (k) + vp (k) ,

p = 1, 2, . . . , η, (49)

with vp, p = 1, 2, . . . , η, being defined by

v1
⎡ ⎤
v2 rp
v = vp ∈ ℝ , (50)
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
vη

provided that the closed-loop system (49) gives all feasi-
ble trajectories, that is,

⌈0∼ϖp−1⌉
xp |p=1∼η (k) ∈ 𝔽. (51)

Please note that in this multiple order case, the set of
integers ϖi, i = 1, 2, . . . , η, may be chosen to be equal
to each other, that is,

ϖ1 = ϖ2 = · · · = ϖη = ϖ.

In this case, we get a closed-loop system with a single-
order ϖ.
Define

AE = blockdiag([Ap]0∼ϖp−1, p = 1, 2, . . . , η),
(52)

then, obviously, the controller (48) can be more com-
pactly written as

u (k) = B−1
⎧
⌈0∼μp−1⌉ ∗
⎪⎪⎪⎨ (·)[−f (xp (k) |p=1∼η, k) + u (k)]

∗ ⌈0∼ϖp−1⌉

## [47] `ijss_2022_part10` (PDF p.16, L1792)

Theorem 7.2: Let ∅ ≠ 𝔽 ⊂ 𝔹κℕ+mr be the set of fea-
sible trajectories of the system (65), and ϖp, p =
1, 2, . . . , η, be a set of integers greater than 1. Then the

following controller

u (k) = B−1
⎧
(·)[−f (xp⌈0∼μp−1⌉(k) |p=1∼η, u⌈1∼m⌉(k) , k)
⎪⎪⎪⎪⎪⎪⎪⎨

+ u∗(k)]

⎪⎪⎪⎪⎪⎪⎪⎩ ∗ ⌈0∼ϖp−1⌉
u (k) = K1∼ηxp (k) |p=1∼η + v (k) ,
(72)

for system (65) produces the following constrained con-
stant linear closed-loop system

⎧xp (k + 1) |p=1∼η
⌈0∼ϖp−1⌉
⎪⎪⎪⎨ = K1∼ηxp (k) |p=1∼η + v (k) (73)
(xp⌈0∼ϖp−1⌉|p=1∼η, u⌈1∼m⌉(k)) ∈ 𝔽,
⎪⎪⎪⎩

where K1∼η ∈ ℝr×κ′, κ′ = ηp=1ϖprp, is the designed
∑
feedback gain matrix.

As a constrained linear system, the closed-loop sys-
tem (73) can be easily made stable by properly selecting
the feedback gain K1∼η. For a systematic method, one
can refer to Duan (2021c). Particularly, when K1∼η is
chosen as

K1∼η = blockdiag([Ap]0∼ϖp−1, p = 1, 2, . . . , η),

the closed-loop system (73) reduces to (49) or equiv-
alently the state-space form (54). Furthermore, the
constraints in the closed-loop system (73) vanishes if
𝕊 =∅, or equivalently, the relation in (69) holds.
Parallel to the extended step backward affine HOFA
system (65), the following extended non-affine one can
also be defined:

x1∼η (k + 1)

= f (xp⌈0∼μp−1⌉(k) |p=1∼η, u⌈1∼m⌉(k) , k)

+ g (xp⌈0∼μp−1⌉(k) |p=1∼η, u⌈1∼m⌉(k) , k, u (k)),

(74)

where f (·), g(·) ∈ ℝr are two proper nonlinear func-
tions, and g(·, u) forms a differential homeomorphism
with respect to u.
Parallel to Definition 7.1, the following one can also
be proposed.

## [48] `ijss_2022_part8` (PDF p.7, L701)

Theorem 3.1: Let Assumption A1 be met. Then a solu-
tion to Problem 2.1 is given by

⎧ u = −B−1 xk(0∼μk−1)|k=1∼η, ζ, t)
(
⎪⎪⎨ ×[f (xk(0∼μk−1)|k=1∼η, ζ, t) − v]

v = −R−1BTEP (t) xk(0∼μk−1)|k=1∼η+R−1BTEg (t) ,
⎪⎪⎩
(25)

where P(t) ∈ ℝκ×κ is the solution to the differential
Riccati Equation (20) subject to the final value condi-
tion (21), and g(t) ∈ ℝκ is a vector function satisfying
the differential Equations (22)–(23) and the final value
condition (24).

In the case of output regulation, that is, the case of
z(t) = 0, the index J1 becomes

1 tf 2 (μk) 2
J2 = ∫ (‖‖y Q + xk |k=1∼η )dt
2 0 ‖‖ ‖‖‖ ‖‖‖R
1 2
+ y(tf S . (26)
2 ‖‖ )‖‖

In this special case, correspondingly the function
g(t) vanishes, and obviously the above Theorem 3.1
becomes the following result.

## [49] `ijss_2022_part8` (PDF p.9, L893)

Theorem 4.3: Let Assumptions A1 and A2 be met, and
Q ∈ ℝm×m be semi-positive definite, and R ∈ ℝr×r be
positive definite. Then, for the system (3) with the output
Equation (5), a feedback controller in the form of (8),
which minimise the index J3, is given by

⎧ u = −B−1 xk(0∼μk−1)|k=1∼η, ζ, t)
(
⎪⎪⎨ ×[f (xk(0∼μk−1)|k=1∼η, ζ, t) − v] (35)
v = −R−1BTEPx(0∼μk−1)|k=1∼η
⎪⎪⎩ k

where P ∈ ℝκ×κ is the unique solution to the algebraic
Riccati Equation (32). Furthermore, the closed-loop sys-
tem (34) is linear and asymptotically stable, and the
minimum index is given by

∗ 1 (0∼μk−1) 2
J = xk (0) |k=1∼η . (36)
2 ‖‖‖ ‖‖‖P

Regarding the above result, we make the following
remark.

## [50] `ijss_2022_part8` (PDF p.11, L1145)

Theorem 5.3: Let Assumptions A2 and A3 be met, and
Q ∈ ℝm×m be semi-positive definite, and R ∈ ℝr×r be
positive definite. Further, let the feedback controller in
the form of (8) for the system (3) be given by (35), with
P ∈ ℝκ×κ being the unique solution to the algebraic
Riccati Equation (32). If, further, the initial values are
chosen to satisfy

ν (P) xk(0∼μk−1)(0) |k=1∼η < d0, (44)
‖‖‖ ‖‖‖
then the two requirements in Problem 5.1 are both met.

## [51] `ijss_2022_part9` (PDF p.8, L835)

Theorem 3.3: Consider the system (2) with the output
equation (5). If

(1) Assumption A1 and condition (21) are satisfied;
(2) the disturbance vector d is constant; and
(3) the two gain matrices KPD and KI make the matrix
A˜c in (24) Hurwitz,

then the controller (7) guarantees the asymptotical
tracking relations (8) and (27)–(28).

It is well-known that PID is a very popular con-
trol technique, and has been widely and success-
fully used in various practical processes. The above
Lemma 3.2 and Theorem 3.3 reveal theoretically the
reason behind such a fact, as given in the following
remark.

## [52] `ijss_2022_part9` (PDF p.10, L1018)

Theorem 4.2: Consider the system (2) with the output
equation (5). Let

(1) Assumptions A1 and A2 be met, and d = 0;
(2) KFB be a matrix making AcE in (41) Hurwitz, and
KFF be given by

KFF = H − KFBG. (42)

Then the controller

⎧u = −B−1 xk(0∼μk−1)|k=1∼η, ζ, t)
(

⎪⎪⎪⎪⎨ × [f (xk(0∼μk−1)|k=1∼η, ζ, t) − v] (43)

⎪⎪⎪⎪⎩ v = KFBxk(0∼μk−1)|k=1∼η + KFFxm,

guarantees

lim y (t) − ym (t) = 0, (44)
t→∞[ ]

and

lim [xk(0∼μk−1)|k=1∼η − Gxm] = 0. (45)
t→∞

In the above controller (43), clearly, K x(0∼μk−1)
FB k
|k=1∼η is a state-plus-derivative feedback term, while
KFFxm is a feed-forward term.

## [53] `ijss_2022_part9` (PDF p.10, L1089)

Theorem 4.3: Consider the system (2) with the output
equation (5). Let

(1) Assumptions A1 and A2 be met, and d and yc be
constant vectors;
(2) KPD and KI be matrices makingA˜c in (24) Hurwitz,
and KFF be given by

KFF = H − KPDG. (51)

Then the controller

⎧u = −B−1 xk(0∼μk−1)|k=1∼η, ζ, t)
(

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ × [f (xk(0∼μk−1)|k=1∼η, ζ, t) − v]

(0∼μk−1) (52)
v = KPDxk |k=1∼η + KFFxm
t
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ + KI ∫ y (σ) − ym (σ) − yc dσ,
0 [ ]

guarantees

lim y (t) − ym (t) = yc, (53)
t→∞[ ]

lim (xk(1∼μk)|k=1∼η − Gx˙m) = 0, (54)
t→∞

and

lim x1∼η (t) − CGxm = −CA˜−c1[ BEΓd ].
t→∞( ) −yc
(55)

Obviously, the three relations (53)–(55) are, respec-
tively, the interpretations of the relations (47)–(49) in
terms of the original system variables.

It can be easily recognised that the above MRT result
is a generalisation of the generalised PID control result
given in Theorem 3.3. The above result clearly reduces
to that in Theorem 3.3 when xm does not exist, or,
equivalently, p = 0.

## [54] `ijss_2022_part9` (PDF p.15, L1636)

Theorem 6.3: Consider the system (2) with the output
equation (5). Let Assumptions A2 and A3 and condition
(21) be met, and d be absent, K = [KPD KI] be given
by (80), with F˜ ∈ ℝ(κ+m)×(κ+m) being chosen to be a
stable diagonal matrix, and Z˜ ∈ ℝr×(κ+m) be an arbi-
trary parameter matrix satisfying the constraint (81).
Further, if the initial values are chosen to satisfy

[ xk(0∼μk−1)|k=1∼η (0) ] Xe ‖
ν V ˜ − [ ] d0,
( )‖‖‖‖‖ q (0) qe ‖‖‖‖ ≤
(97)
where d0 is the maximum number such that

Ω = {z | z ∈ ℝκ, ‖z − Xe‖ ≤ d0} ⊂ 𝔽, (98)

then the controller (7) for the system (2) guarantees
(26)–(28) and the feasibility requirement (85).

## [55] `ijss_2022_part9` (PDF p.16, L1736)

Theorem 6.4: Consider the system (2) with the output
equation (5). Let Assumptions A2′, A3 and A4 be met,
and d = 0; KFB be given by (78), with F ∈ ℝκ×κ being
chosen to be a stable diagonal matrix, and Z ∈ ℝr×κ be
an arbitrary parameter matrix satisfying the constraint
(65). Further, if the initial values are chosen to satisfy

Figure 1. Geometric relation between Ω and 𝕊.

xm(0) ∈ Ω0 and

ν (V) xk(0∼μk−1)|k=1∼η (0) − Gxm (0) ≤ d0, (104)
‖‖‖ ‖‖‖
where V is given by (78), then the controller (43) for the
system guarantees (44)–(45) and the feasibility require-
ment (85).

## [56] `ijss_2024_underactuated4` (PDF p.5, L488)

Theorem 2.1: Let Ak,0∼μk−1 ∈ ℝrk×μkrk, k = 1, 2, be
such that Φ(Ak,0∼μk−1), k = 1, 2, are Hurwitz. Then a
sub-stabilising controller for the multi-order affine sub-
FAS (6) is given by

⎧ −1 ([f1 (·, t)] ∗)
u (t) = −B (·, t) + u
⎪⎪⎪⎪⎪⎨ f2 (·, t)

∗ [A1,0∼μ1−1 0 ] (0∼μk−1)
u = xk ,
⎪⎪⎪⎪⎪⎩ 0 A2,0∼μ2−1 |||k=1∼2
(7)

which results in the following constrained linear closed-
loop system

x1(μ1) + A1,0∼μ1−1x1(0∼μ1−1) = 0
⎧
⎪⎪⎪⎨x2(μ2) + A2,0∼μ2−1x2(0∼μ2−1) = 0 (8)

x(0∼μk−1) ∈ 𝔽m.
⎪⎪⎪⎩ k |||k=1∼2

Furthermore, the REA of the designed system is given by

Rm = (X10, X20) |ϕ (X10, X20, t) ≠ 0 or ∞,
{
Xk0 ∈ ℝμkrk, k = 1, 2, and t ≥ 0 ,
}

where

ϕ (X10, X20, t)

= det B(eΦ(A1,0∼μ1−1)tX10, eΦ(A2,0∼μ2−1)tX20, t).

Again, as a consequence, all the closed-loop system
trajectories starting from Rm go to the origin expo-
nentially within 𝔽m. In the case of 𝔽s = ℝμ1r1+μ2r2, the
constraint in (8) vanishes, and in this case we also have
Rm = ℝμ1r1+μ2r2.

For detailed treatment on sub-stabilisation of sub-
FASs, please refer to Duan (2022g), Duan (2023b),
Duan (2023c), Duan (2023a), Duan (2023f), Duan
(2023g), particularly, Duan(2023e).
The following two remarks explain the relation
between sub-stability and Lyapunov stability.

## [57] `ijss_2024_underactuated4` (PDF p.7, L654)

Theorem 3.1: Assume m = n, and let Assumption A1
be met. Then

(1) under the following diffeomorphism (x, y) →
(z,z ˙):

x = h (z,z ˙, t)
{ (12)
y = z,

system (9) is equivalent to the following sub-FAS:

z¨ = f (z,z ˙, t) + B (z,z ˙, t) u, (13)

where

f (z,z ˙, t) = Gy (h (z,z ˙, t) , z, t)z ˙

∂g (h (z,z ˙, t) , z, t)
+
∂t
+ Gx (h (z,z ˙, t) , z, t) f0 (h (z,z ˙, t) , z, t) ,
(14)

B (z,z ˙, t) = Gx (h (z,z ˙, t) , z, t) B0 (h (z,z ˙, t) , z, t) ;
(15)

(2) the feasible set of sub-FAS (13) is

Ω = Ω1 ∩ Ω2, (16)

where

Ω2 = x, y det B x, y, t ≠ 0 or ∞,
{( )|| ( )
x, y ∈ ℝn, and t ≥ 0 .
}

## [58] `ijss_2024_underactuated4` (PDF p.10, L1013)

Theorem 4.1: Assume m = n, and let Assumption A2
be met. Then

(1) under the following diffeomorphism (x1, x2, x3) →
(x, y,y ˙) :

⎧x1 = x
⎨x2 = h(x, y,y ˙, t) (40)
x3 = y,
⎩
system (37) is equivalent to the following sub-FAS:

x˙ f0(x, y,y ˙, t)
[ ] = [ ]
y¨ f (x, y,y ˙, t)

B0(x, y,y ˙, t) 0 u1
+ [ ] [ ],
B1 x, y,y ˙, t B2 x, y,y ˙, t u2
( ) ( )
(41)

where

f0(x, y,y ˙, t) = fˆ1 x, h x, y,y ˙, t , y, t , (42)
( ( ) )
B0(x, y,y ˙, t) = Bˆ1 x, h x, y,y ˙, t , y, t , (43)
( ( ) )
and

f x, y,y ˙, t = G3 x, h x, y,y ˙, t , y, t y ˙
( ) ( ( ) )
+ Gt(x, h(x, y,y ˙, t), y, t)

+ G1(x, h(x, y,y ˙, t), y, t)

× fˆ1(x, h(x, y,y ˙, t), y, t)

+ G2(x, h(x, y,y ˙, t), y, t)

× fˆ2(x, h(x, y,y ˙, t), y, t), (44)

B1 x, y,y ˙, t = G1(x, h(x, y,y ˙, t), y, t)
( )
× Bˆ1(x, h(x, y,y ˙, t), y, t), (45)

B2 x, y,y ˙, t = G2(x, h(x, y,y ˙, t), y, t)
( )
× Bˆ2(x, h(x, y,y ˙, t), y, t); (46)

(2) the set of feasibility of the above sub-FAS (41) is
given by

U = U1 ∩ U2 (47)

with

U2 = x, y,y ˙ | det B0(x, y,y ˙, t)B2 x, y,y ˙, t
{( ) ( ( ))

≠ 0 or ∞, x ∈ ℝn , y,y ˙ ∈ ℝm , and t ≥ 0 .
}
(48)

## [59] `ijss_2024_underactuated4` (PDF p.13, L1501)

Theorem 5.1: Let Assumption A3 be met. Then,

(1) under the diffeomorphism (78), UAS (73) is equiv-
alent to the following sub-FAS

q(4) = f (q(0∼3), t) + B(q(0∼3), t)u, (81)

where

f (q(0∼3), t) = f0(h1(·), h2(·), q(0∼3), t), (82)

B(q(0∼3), t) = B0(h1(·), h2(·), q(0∼3), t), (83)

with f0(·) and B0(·) being given by (79) and (80),
and

hi(·) ≜ hi(q(0∼3), t), i = 1, 2;

(2) the set of feasibility of sub-FAS (81) is given by

W = W1 ∩ W2, (84)

with

W2 = {X|detB(X, t) ≠ 0 or ∞,

X ∈ ℝ4n and t ≥ 0}.

## [60] `ijss_2024_underactuated4` (PDF p.17, L1935)

Theorem 6.1: Let Assumption A4 be met, f0(·),
B10(·) and B20(·) be given by (120)–(122). Then

(1) under the diffeomorphism (119), system (114) is
equivalently converted into the following sub-FAS:

¨x f˘1 x(0∼1), y(0∼3), t v
[y(4)] = [ ( (0∼1) (0∼3) )] + B (·)[u],
f (x , y , t)
(123)

where

B (·)

B˘1 x(0∼1), y(0∼3), t
≜ [B1((x(0∼1), y(0∼3), t)) B2(x(0∼1), y(0∼3), t)],

and

f x(0∼1), y(0∼3), t
( )

= f0(x(0∼1), h1 (·) , h2 (·) , y(0∼3), t), (124)

B1(x(0∼1), y(0∼3), t)

= B10(x(0∼1), h1 (·) , h2 (·) , y(0∼3), t),

(125)

B2(x(0∼1), y(0∼3), t)

= B20(x(0∼1), h1 (·) , h2 (·) , y(0∼3), t),

(126)

with

hi (·) ≜ hi(x(0∼1), y(0∼3), t), i = 1, 2;

(2) the set of feasibility of sub-FAS (123) is given by

H = H1 ∩ H2, (127)

with

H2 = (X, Y) |det B˘1 (X, Y, t) B2(X, Y, t)
{ [ ]
≠ 0 or ∞, X ∈ ℝ2n, Y ∈ ℝ4m and t ≥ 0 .
}
(128)

## [61] `jssc_2022_freq` (PDF p.10, L501)

Theorem 4.5 Let (A, B) be controllable, and (N (s) , D(s)) ∈ (ℝn×r(s), ℝr×r(s)) be right
coprime and such that (11) is satisfied. Moreover, assume that D(s) is column reduced and
(N(s), D(s)) is expressed by (20)–(21). Let the generalized state vector Z(s) satisfy the fully
actuated PMD model

(Δ(s) + D0−1[ D1l1(s) D2l2(s) · · · Drlr(s) ])Z(s) = D0−1U(s), (23)

then the state of the state-space model (1) can be given by (13). Moreover, the generalized state
vector z(t) can be uniquely determined from x(t) according to

⎡ z1 (t) ⎤ ⎡ eT1 ⎤

z2 (t) eT2 ˇ−1
z (t) = = N x (t) . (24)
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ ⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
zr (t) eTr

## [62] `jssc_2022_freq` (PDF p.13, L637)

Theorem 5.1 Let (A, B) be controllable, (N(q), D(q)) ∈ (ℝn×r(q), ℝr×r(q)) be right co-
prime and satisfy
(qIn − A)−1B = N(q)D−1(q). (33)

Assume that D(q) is column reduced with the degrees of columns given by {h1, h2, · · · , hr}, and
(N(q), D(q)) is expressed by

D(q) = D0Δ(q) +[ D1l1(q) D2l2(q) · · · Drlr(q) ], (34)

N(q) = NˇΨ(q) = [ N1l1(q) N2l2(q) · · · Nrlr(q) ]. (35)

Let the generalized state vector z(k) satisfy the fully actuated PMD model

(qIr + D0−1[ D1E1l1 q−1 D2E2l2 q−1 · · · DrErlr q−1) ])z (k) = D0−1u(k), (36)
( ) ( ) (
where, for i = 1, 2, · · · , r,

⎡ 1 ⎤

Ei = 1 ∈ ℝhi×hi.
⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎦
1

Then the state of the state-space model (32) can be given by

x(q) = [ N1E1l1 q−1 N2E2l2 q−1 · · · NrErlr q−1) ]z(q). (37)
( ) ( ) (
Moreover, the generalized state vector z(k) ∈ ℝr can be uniquely determined from x(k) according
to
⎡ z1(k) ⎤ ⎡ εT1 ⎤

z2 (k) εT2 ˇ−1
z (k) = = N x (k) . (38)
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ ⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
zr(k) εTr

## [63] `odfas_2026_part1` (PDF p.6, L648)

Theorem 2.1. Let system (11) be a global OD-
FAS. Then an output feedback stabilizing con-
troller for the system is given by

u (t) = −B−1(·, t) (fy (·, t) − u0)
{ u0 = K11y + K12z (19)
z˙ = K21y + K22z,

where Kij, i, j = 1, 2, are given by (14) with
L ∈ ℝr×r being a Hurwitz matrix, and Fi ∈ ℝr×r,
i = 0, 1, being matrices making Φ (F0∼1) Hur-
witz. Furthermore, the corresponding closed-loop

system is given by (15)-(16) with the set of eigen-
values eig (Φ (F0∼1)) ∪ eig (L) .

To end this subsection, let us consider an ex-
ample in the form of (11) using the above Theo-
rem 2.1.

## [64] `odfas_2026_part1` (PDF p.11, L1231)

Theorem 3.1. The spacecraft rendezvous sys-
tem (48)-(50) has a uniformly globally asymptot-
ically stabilizing controller in the following form

u = −fy (y,θ,˙θ¨) + u0
u0 = −K1z − (K1L + K0) y
{ (64)
z˙ = Az( θ˙)z + (Az( θ˙)L − K0)y
Az( θ˙) = D( θ˙) − L − K1,

and the corresponding closed-loop system is given
by (59)-(60), where all the variables are defined
above, and L, K1, and K0 are three symmetric
positive definite matrices.

## [65] `odfas_2026_part1` (PDF p.13, L1511)

Theorem 4.1. Let (82) be a stabilizing con-
troller for linear system (81). Then, under the
feasibility condition

X0 = x(0∼n−1)(0) ∈ R, (85)

the following output feedback controller

u (t) = −B−1(·, t) [fy (·, t) − u0 (t)]
{ (86)
u0 (t) = K (t) y (t)

for OD-FAS (25) makes sense and drives the
closed-loop response x(0∼n−1)(t) exponentially to
zero.

## [66] `odfas_2026_part1` (PDF p.14, L1602)

Theorem 4.2. Let (87) be a stabilizing con-
troller for linear system (81). Then, under the
feasibility condition

X0 x(0∼n−1)(0)
[ ] = [ ] ∈ R, (91)
z0 z (0)

the following output feedback controller

u (t) = −B−1(·, t) [fy (·, t) − u0 (t)]
{ u0 (t) = K11 (t) y (t) + K12 (t) z (t) (92)
z˙ (t) = K21 (t) y (t) + K22 (t) z (t)

for OD-FAS (25) makes sense and drives the
closed-loop responses z (t) and x(0∼n−1)(t) both
exponentially to zero.

## [67] `odfas_2026_part1` (PDF p.19, L2107)

Theorem 5.1. Under the feasibility condition
(121), or equivalently, |y2| < c, the OD-FAS
(114) has an output feedback substabilizing con-
troller of the following form:

u = −B(1y2) [f (y2∼3) − u0]
{ u0 = −a1z − (a0 + a1l) y1 − a2y2 − a3y3
z˙ = −lz − l2y1 + y2,
(131)
where l > 0, and a0∼3 makes Φ (a0∼3) Hurwitz.
Furthermore, the closed-loop system is linear and
is given by (128)-(130) with the set of eigenvalues
eig (Φ (a0∼3)) ∪ {−l}.

Please note

y1 = ξ = b2θ + b1x
{ y2 = ξ¨... = c sin θ
y3 = ξ = cθ˙ cos θ,

the above controller for the initial wheel pendu-
lum indeed uses the feedback of θ(0∼1) and x only.

## [68] `odfas_2026_part1` (PDF p.24, L2665)

Theorem 8.1. System (141) is uniformly
asymptotically stable if, for arbitrary t ≥ 0,

M (t) > 0, K (t) > 0, K˙ (t) ≤ 0, (142)
M˙ (t) − D (t) + DT(t) < 0. (143)
( )

## [69] `odfas_2026_part4` (PDF p.13, L805)

Theorem 3.1. Suppose system

x˙ = A0 (t) x, A0 (t) ∈ ℝn×n (3.4)

is uniformly asymptotically stable. If Rs (t) ∈ ℝn×n is uniformly bounded and uniformly positive

definite, then system (3.2)-(3.3) is uniformly asymptotically stable.

## [70] `odfas_2026_part4` (PDF p.15, L916)

Theorem 3.2. The origin of system (3.10)-(3.11) is GUA stable if

1. g (z, t) ∈ ℝm and G(x, t) ∈ ℝn×m are piecewise continuous in t and locally Lipschitz in x and z;

2. system (3.11) is GUA stable; and

3. all the conditions in Lemma 3.3 hold.

The above theorem clearly has the following corollary.

## [71] `odfas_2026_part4` (PDF p.19, L1123)

Theorem 4.1. Let Assumptions A1-A2, Aϕ1, and Ap1 be satisfied, and F0∼1 ∈ ℝr×2r be a matrix

making Φ (F0∼1) Hurwitz. Then a GUA stabilizing output feedback controller for system (4.4) is given

in the form of
u0 = K11(ϕ(0∼1))y + K12(ϕ(0∼1))z

{z˙ = K21(ϕ(0∼2))y + K22(ϕ(0∼1))z, (4.20)

with
K11(ϕ(0∼1)) = −K12(ϕ(0∼1))L(ϕ(0∼1))− F0

K12(ϕ(0∼1)) = −(F1 + R (ϕ) A1(ϕ(0∼1)))

{K21(ϕ(0∼2)) = ΘIa(ϕ(0∼2)) + K11(ϕ(0∼1)) (4.21)

K22(ϕ(0∼1)) = Ao1 + K12(ϕ(0∼1)),

where Ao1 is an arbitrary Hurwitz matrix, ΘIa(ϕ(0∼2)) is defined in (4.8).

## [72] `odfas_2026_part4` (PDF p.21, L1241)

Theorem 4.2. Let Assumptions A0-A2 and Aϕ1, and Ap1 be satisfied, and F0∼1 ∈ ℝr×2r be a

matrix making Φ (F0∼1) Hurwitz. Then a GUA stabilizing output feedback controller for system (4.1)

is given by
u (t) = −B−1 y (t − τj (t))|j=1∼q , t)(u′(t) − M (ϕ (t)) u0)
(
u′(t) = fy (y (t − σi (t))|i=1∼p , t) + A0(ϕ(0∼1))y (t)

{u0 = K11(ϕ(0∼1))y + K12(ϕ(0∼1))z (4.29)

z˙ = K21(ϕ(0∼2))y + K22(ϕ(0∼1))z,

where Kij (⋅) , i, j = 1, 2, are given by (4.21) with Ao1 being an arbitrary Hurwitz matrix. Particularly,

in the case of A1(ϕ(0∼1)) = A1 (ϕ), the u0 in the above controller (4.29) is reduced to (4.27), with

Kij (⋅) , i, j = 1, 2, being given by (4.28).

To demonstrate the result, let us consider an example.

## [73] `odfas_2026_part4` (PDF p.23, L1380)

Theorem 4.3. Let Assumptions Aϕ2 and Ap1 be satisfied, Ao1 ∈ ℝ2n×2n be an arbitrary Hurwitz

matrix, and F0∼1 ∈ ℝ2n×4n be a matrix making Φ (F0∼1) Hurwitz. Then an output feedback GUA

stabilizing controller for system (4.38) is given by

u = G(y0∼1, y0∼1 (t − τ)) + M(y1)u0
{u0 = K11 (y1) y0 + K12 (y1) z (4.41)
z˙ = K21 (y) y0 + K22 (y1) z,

where
K11 (y1) = −K12 (ϕ) (Ao1 + R (y1) C (y1)) − F0
K12 (y1) = −F1 + R (y1) C(q2)
{ (4.42)
K21 (y) = ΘIa (y) + K11 (y1)
K22 (y1) = Ao1 + K12 (y1) ,

with

ΘIa (y) = L˙ (y1) − Ao1L (y1) , (4.43)

L (y1) = Ao1 + R (y1) C (y1) . (4.44)

## [74] `odfas_2026_part4` (PDF p.31, L1831)

Theorem 5.1. Let Assumptions A1-A2, Aϕ1 and Ap1 be satisfied, F0∼1 ∈ ℝr×2r be a matrix

making Φ (F0∼1) Hurwitz, AoI(ϕ(0∼1)) be given by (5.11), and L(ϕ(0∼1)) make AoI(ϕ(0∼1)) uniformly

asymptotically stable. Then a GUA stabilizing output feedback controller for system (5.4) is given in

the form of
u0 = K11(ϕ(0∼1))y + K12(ϕ(0∼1))z

{z˙ = K21(ϕ(0∼2))y + K22(ϕ(0∼1))z, (5.34)

with
K11(ϕ(0∼1)) = −F0 − K12(ϕ(0∼1))L(ϕ(0∼1))

K12(ϕ(0∼1)) = −⌊F1 + R (ϕ) A1(ϕ(0∼1)) R (ϕ)⌋

{K21(ϕ(0∼2)) = −[Ir] (F0 + K12(ϕ(0∼1))L(ϕ(0∼1)))− ΘIb(ϕ(0∼2)) (5.35)
0

K22(ϕ(0∼1)) = AoI(ϕ(0∼1))+[Ir]K12(ϕ(0∼1)),
0

where ΘIb(ϕ(0∼2)) is given by (5.14). Furthermore, when Assumption Ap2 is met, L(ϕ(0∼1)) can be

given by (5.23) and with Li ∈ ℝr×r, i = 1, 2, making AL Hurwitz.

## [75] `odfas_2026_part4` (PDF p.33, L1924)

Theorem 5.2. Let Assumptions A0-A2, AD, Aϕ1, and Ap1 be met, F0∼1 ∈ ℝr×2r be a matrix

making Φ (F0∼1) Hurwitz, AoI(ϕ(0∼1)) be given by (5.11), and L(ϕ(0∼1)) make AoI(ϕ(0∼1)) uniformly

asymptotically stable. Then a GUA stabilizing observer-based output feedback controller for system

(5.1) is given by

u (t) = −B−1(⋅, t)(fy (⋅, t) + A0(ϕ(0∼1))y (t) − M (ϕ) u0)

{u0 = K11(ϕ(0∼1))y + K12(ϕ(0∼1))z (5.39)

z˙ = K21(ϕ(0∼2))y + K22(ϕ(0∼1))z,

where Kij (⋅) , i, j = 1, 2, are given by (5.35) with ΘIb(ϕ(0∼2)) being given by (5.14). Furthermore,

when Assumption Ap2 is added, L(ϕ(0∼1)) can be given by (5.23) and with Li ∈ ℝr×r, i = 1, 2, making

AL Hurwitz.

to add

5.2.2. Case of A1(ϕ(0∼1)) = A1 (ϕ) In the case of A1(ϕ(0∼1)) = A1 (ϕ) , the matrix AI (ϕ(0∼1))

is given by (5.26), and the following result follows from Propositions 4.1 and 5.2.

## [76] `odfas_2026_part4` (PDF p.43, L2455)

Theorem 6.1. Let Assumptions A0-A2 and Av1-Av2 be satisfied, Ao2 be an arbitrary Hurwitz ma-

trix, and F0∼1 ∈ ℝr×2r be a matrix making Φ (F0∼1) Hurwitz. Then a GUA stabilizing output feedback

controller for system (6.2) is given by (6.4) and (4.27) with Kij (⋅) , i, j = 1, 2, being given by (6.22),

which reduces, in the case of A0(ϕ(0∼1)) = A0 (ϕ), to (6.27) with ΘIIa(ϕ(0∼1)) given by (6.17)-(6.16),

or by (6.28) when A0(ϕ(0∼1)) = A0 is constant.

to add

## [77] `odfas_2026_part4` (PDF p.50, L2836)

Theorem 7.1. Let Assumptions A0-A2, Av1-Av3 be met. Then a GUA stabilizing observer-based

output feedback controller for system (7.1) is given by

u (t) = −B−1(⋅, t)(fy (⋅, t) + A1(ϕ(0∼1))y (t) − M (ϕ (t)) u0)

{u0 = K11(ϕ(0∼1))y + K12(ϕ(0∼1))z (7.29)

z˙ = K21(ϕ(0∼2))y + K22(ϕ(0∼1))z,

where Kij (⋅) , i, j = 1, 2, are given by (7.23) with L(ϕ(0∼1)) ∈ ℝ2r×r making system (7.9) uniformly

asymptotical stable, and F0∼1 ∈ ℝr×2r being a matrix making Φ (F0∼1) Hurwitz. In the special case

of A0(ϕ(0∼1)) = A0 being a constant matrix, a GUA output feedback stabilizing controller for system

(7.1) is given by

u (t) = −B−1(⋅, t)(fy (⋅, t) + A1(ϕ(0∼1))y (t) − M (ϕ (t)) u0)

{u0 = K11 (ϕ) y + K12 (ϕ) z (7.30)
z˙ = K21(ϕ(0∼1))y + K22 (ϕ) z,

where Kij (⋅) , i, j = 1, 2, are given by (7.28) with AoII ∈ ℝ2r×2r being a Hurwitz matrix

## [78] `odfas_2026_part4` (PDF p.55, L3118)

Theorem 8.1. Let Assumptions Aφ and AG be met, F0∼1 ∈ ℝ3×6 be a matrix making Φ(F0∼1)

Hurwitz, and Ao2 ∈ ℝ3×3 be an arbitrary Hurwitz matrix. Then a GUA stabilizing output feedback

controller, which guarantees the tracking performance (8.4), for the marine vehicle system (8.1) with

Δτ† ≡ 0, is given by

τ† = Mu + D† y† + G†η∗ − hφ
u = RT(φ) u0 − ( fy) φ(0∼1), t
{ († ) ∗ (8.23)
u0 = K11 (φ) R (φ) y + K12 (φ) z − K11 (φ) ˙η
z˙ = K21 φ(0∼1) R (φ) y† + K22 (φ) z − K21 φ(0∼1) η˙∗,
( ) ( )
where
K11 (φ) = −K12 (φ) L (φ) − F1
K12 (φ) = − (F0 + R (φ) A0)
{K21 φ(0∼1) = Θ1 φ(0∼1) + L (φ) K11 (φ) (8.24)
( ) ( )
K22 (φ) = −L (φ) F0,

with

Θ1(φ(0∼1)) = −φA ˙o2A−01ERT (φ) − Ao2L (φ) + Ir, (8.25)

L (φ) = Ao2A−01RT (φ) . (8.26)

Secondly, let us treat the case that Δτ† is present and governed by

Δ˙τ† = AτΔτ†, (8.27)

where Aτ ∈ ℝ3×3 is a Hurwitz matrix. It follows from (8.27) that disturbance d (t) admits the following

model:

d˙ = ADd, (8.28)

where

AD = M−1AτM.

Based on the above discussion, the problem is converted into one of finding an output feedback

stabilizing controller for system (8.19).

By Theorem 7.1, we can also immediately obtain the following result.

## [79] `odfas_2026_part4` (PDF p.56, L3167)

Theorem 8.2. Let Assumptions Aφ and AG be met, Aτ ∈ ℝ3×3 be a Hurwitz matrix, L] ∈ ℝ6×3

make

AoII = [0 −10 ] + L] A0 I3⌋

## [80] `odfas_2026_part4` (PDF p.60, L3397)

Theorem 8.3. Let Assumptions Aφ and AG be met. Furthermore, Let Assumption Aφ be satisfied,

Ao2 be an arbitrary Hurwitz matrix, and F0∼1 ∈ ℝ2×4 be a matrix making Φ (F0∼1) Hurwitz. Then a

GUA stabilizing output feedback controller, which guarantees the tracking performance (8.4), for the

marine vehicle system (8.1) with Δτ ≡ 0, is given by

τ† = M ([u1]+ D y† + Gη∗)− hφ
u2 ( )
{ † (8.51)
u1 = uζ − A12φ − fy1(y , φ, t)
u2 = uφ − A22φ − fy2 y†, φ, t ,
( )
where uζ is given by (8.43)-(8.45), and uφ is given by (8.46).

## [81] `scis_2022_discdelay1` (PDF p.11, L707)

Theorem 1. Let Assumption 3 be met. Further, let ̟i ⩾ 1, i = 1, 2, . . ., η be a set of integers, and
[Ai]0∼̟i−1 ∈ ℝri×̟iri, i = 1, 2, . . ., η be a set of arbitrarily given matrices. Then the following controller:

−1 ⌈τp,1∼ζp(k)⌉ ⌈τp,1∼ζp(k)⌉ ∗
u (k) = B (xp (k) |p=1∼η, k) [−f (xp (k) |p=1∼η, k)+ u (k)],

[A1]0∼̟1−1 x⌈10∼̟1−1⌉(k)
{ [A2]0∼̟2−1 x⌈20∼̟2−1⌉(k) (46)
u∗(k) = + v (k)
...
[Aη] ⌈η0∼̟η−1⌉(k)
0∼̟η−1 x

for system (44) produces the following constant linear closed-loop system:

xp (k + 1) = [Ap]0∼̟p−1xp⌈0∼̟p−1⌉(k) + vp (k) , p = 1, 2, . . ., η, (47)

with vp, p = 1, 2, . . ., η being defined as

v1

v2 rp
v = , vp ∈ ℝ . (48)
...
vη

Duan G R Sci China Inf Sci August 2022 Vol. 65 182201:12

If we define
AE = blockdiag([Ap]0∼̟p−1 , p = 1, 2, . . ., η), (49)

then, obviously, the controller (46) can be more compactly written as

−1 ⌈τp,1∼ζp(k)⌉ ⌈τp,1∼ζp(k)⌉ ∗
u (k) = B (xp (k) |p=1∼η, k) [−f (xp (k) |p=1∼η, k)+ u (k)],
(50)
{u∗(k) = AEx⌈p0∼̟p−1⌉(k) |p=1∼η + v (k) .

Furthermore, if written in a state-space form, the closed-loop system (47) appears as

x⌈p0∼̟p−1⌉(k + 1) = Ψ [Ap]0∼̟p−1 x⌈p0∼̟p−1⌉(k) + Γcpvp (k) , p = 1, 2, . . . , η, (51)
( )
where
Irp
0
Γcp = , p = 1, 2, . . . , η. (52)
...
0

Please note that in this interconnected case, the set of integers ̟i, i = 1, 2, . . ., η may be chosen to be
equal to each other, that is,
̟1 = ̟2 = · · · = ̟η = ̟.

Specially, letting η = 1 in the above theorem, we have the following corollary.

## [82] `scis_2022_discdelay1` (PDF p.14, L878)

Theorem 2. Let Assumption 4 be met. Further, let ̟ be an integer satisfying 1 ⩽ ̟ ⩽ n, and
[A]0∼̟−1 ∈ ℝr×̟r be an arbitrarily given matrix. Then the following controller:

u (k − h) = B−1 x⌈τ1∼ζ(k)⌉(k) , k −f x⌈τ1∼ζ(k)⌉(k) , k + u∗(k − h) ,
u∗(k − h) = A0∼ (̟−1x⌈0∼̟−1⌉(k) +) [ v ((k) , ) ]
{x (k) = f x⌈τ1∼ζ(k−1)⌉(k − 1) , k − 1 + B x⌈τ1∼ζ(k−1)⌉(k − 1) , k − 1 u (k − h − 1) , (63)
( ) ( )
k ⩾ h,

for system (29) produces the following constant linear closed-loop system:

x (k + 1) = A0∼̟−1x⌈0∼̟−1⌉(k) + v (k) , k ⩾ h. (64)

Please note that the initial value of the closed-loop system is x⌈0∼̟−1⌉(h), which is provided by the
first h steps self-running of the system.

## [83] `scis_2022_discdelay1` (PDF p.15, L961)

Theorem 3. Let Assumption 5 be met. Further, let ̟i ⩾ 1, i = 1, 2, . . ., η be a set of integers, and
[Ai]0∼̟i−1 ∈ ℝri×̟iri, i = 1, 2, . . ., η be a set of arbitrarily given matrices. Then the controller (65) for
system (32) produces the following constant linear closed-loop system:

xp (k + 1) = [Ap]0∼̟p−1x⌈p0∼̟p−1⌉(k) + vp (k) , k ⩾ h, p = 1, 2, . . ., η (66)

with vp, p = 1, 2, . . ., η being defined by (48).
Theoretically, any discrete-time delay FAS in the form of (32) with interconnections can be written in
the form of (29) for a discrete-time delay FAS without interconnections; just like a discentralized large-
scale system can always be written into a centralized system form with a large dimension. As a matter
of fact, the discrete-time delay FAS in the form of (32) with interconnections is often used to describe
complicated large-scale systems. However, for only the purpose of demonstrating the proposed approach,
let us present a simple example.

## [84] `scis_2022_discdelay2` (PDF p.10, L616)

Theorem 1. Let 𝔽k be the set of feasible points of system (41) at time k. Further, let ̟ ⩾ 1 be an
integer, and A0∼̟−1 ∈ ℝr×̟r be an arbitrarily given matrix. Then the following controller:

u (k) = B−1(x⌈p0∼γp(k)⌉(k) , k)[−f (ψ (k) , k) + u∗(k)] ,
|||p=1∼r (42)
{u∗(k) = A0∼̟−1x⌈0∼̟−1⌉(k) + v (k) ,

for system (41), with v (k) being an external input, produces the following constant linear closed-loop
system:
x (k + 1) = A0∼̟−1x⌈0∼̟−1⌉(k) + v (k) (43)

subject to the following constraint:

x⌈1−ρ(k)⌉(k) ∈ 𝔽k, k ⩾ h. (44)

As pointed out in [1], the integer ̟ may be chosen within the range of

1 ⩽ ̟ ∈ max{ρ (k) , k ⩾ h}.

In practical applications, the integer ̟ may be chosen according to the requirement on the closed-loop
system. For example, if there is a requirement on both x (k) and x (k − 1), then ̟ should be chosen
greater than 2.
For the non-affine time-delay FAS with state delays only:

x (k + 1) = f (ψ (k) , k) + g(x⌈p0∼γp(k)⌉(k) , k, u (k)), (45)
|||p=1∼r

a result similar to Theorem 1 still holds. The controller can be obtained using the differential homeo-
morphism property of the mapping ˜u = g (X, k, u) , as

u (k) = g−1(x⌈p0∼γp(k)⌉(k) , k,u (k)),
p=1∼r ˜
|||
{u˜ (k) = −f (ψ (k) , k) + u∗(k) , (46)

u∗(k) = A0∼̟−1x⌈0∼̟−1⌉(k) + v (k) ,

and the same closed-loop system as in (43) is obtained.
When the linear closed-loop system (43) is written in state-space form, it appears as follows:

x⌈0∼̟−1⌉(k + 1) = Ψ (A0∼̟−1) x⌈0∼̟−1⌉(k) + Γcv (k) , (47)

where
Ir
Γc = [ ].
0r(̟−1)×r

Therefore, the linear system (43), or equivalently, (47), is stable if and only if the matrix Ψ (A0∼̟−1) is
Schur. Such a fact gives a design method for the feedback gain matrix A0∼̟−1. Noting that

Ψ (A0∼̟−1) = Ψ (00∼̟−1) + ΓcA0∼̟−1,

Duan G R Sci China Inf Sci September 2022 Vol. 65 192201:11

and [Ψ (00∼̟−1) , Γc] is controllable, the solution to the feedback gain in the proposed controllers really
reduces to a problem of eigenstructure assignment, hence can be easily solved. Particularly, a complete
parameterization of the designs can be given. Specifically, as done in the continuous-time case, complete
parametric expressions for the feedback gain A0∼̟−1 in the controllers as well as the eigenstructure of
the closed-loop system can be established, which provides all the design degrees of freedom to be used
for further improving the system performance (see [13,22–24] for the continuous-time case).
Regarding the feasibility requirement, that is, the constraint (44), we remark that it is essential for
control of sub-FASs. It vanishes only for global FASs. Noticing that an eigenstructure assignment
problem has the same formulation in the algebra level, for treatment of this constraint, there are at least
two methods:
(1) Method based on Lyapunov matrix equation. It is well-known that, for constant stable linear
systems, there exists a converged exponential trajectory envelope which is represented by the solution to

## [85] `scis_2022_discdelay2` (PDF p.12, L779)

Theorem 2. Let 𝔽k be the set of feasible points of system (27) at time k. Further, let ̟ be an integer
greater than 1, and A0∼̟−1 ∈ ℝr×̟r be an arbitrarily given matrix. Then the following controller:

u (k − h) = B−1(x⌈p0∼γp(k)⌉(k) , k)[−f (ψ (k) , k) + u∗(k − h)] ,
|||p=1∼r
u∗(k − h) = A0∼̟−1x⌈0∼̟−1⌉(k) + v (k) ,
(56)
{ ⌈0∼γp(k−1)⌉
x (k) = f (ψ (k − 1) , k − 1) + B(xp (k − 1) , k − 1)u (k − h − 1) ,
|||p=1∼r
k ⩾ h,

for system (27) produces the same constant linear closed-loop system (43) provided that the constraint
(44) is met, where v (k) is an external input.

Duan G R Sci China Inf Sci September 2022 Vol. 65 192201:13

Please note that the initial value of the closed-loop system is x⌈0∼̟−1⌉(h), which is provided by the
first h steps self-running of the open-loop system (27).

## [86] `scis_2023_delay1` (PDF p.15, L980)

Theorem 1. ( Let 𝔽 ⊂ ℝm, m ⩽) γnr be the set of feasible points of single-order affine sub-FAS (62),
and A0∼n−1 ∈ ℝr×nr be an arbitrarily given matrix. Design the following controller:

u (t) = −B−1 T x(0∼n−1)(t − σj (t)) |j=1∼γ, t f x(0∼n−1)(t − τj (t)) |j=1∼ζ, t + u∗(t) ,
{u∗(t) = A0∼n− (1x(0∼n−1)(t) − v (t) , t ⩾ 0 ) [ ( ) ] (81)

for the single-order affine sub-FAS (62), where v (t) is an external input vector. Then the following
constant linear closed-loop system

x(n)(t) + A0∼n−1x(0∼n−1)(t) = v (t) , t ⩾ 0 (82)

is obtained provided that the following state constraint is met:

T x(0∼n−1)(t − σj (t)) |j=1∼γ ∈ 𝔽. (83)

For the single-order non-affine sub-FAS (63), a result similar to Theorem 1 still holds. In this case, the
controller can be obtained using the differential homeomorphism property of the mapping g (·) as

u (t) = g−1 T x(0∼n−1)(t − σj (t)) |j=1∼γ, t,u ˜ (t) ,
u˜ (t) = −f (x(0∼n−1)(t − τj (t)) |j=1∼ζ, t − u∗(t)) , (84)
{u∗(t) = A0(∼n−1x(0∼n−1)(t) − v (t) , t ⩾) 0,

and eventually, the same closed-loop linear system as (82) is resulted in.
To demonstrate the above proposed controller, let us consider two examples treated in Sections 2 and 4.

## [87] `scis_2023_delay1` (PDF p.16, L1047)

Theorem 2. Let 𝔽 ⊂ ℝM be the set of feasible points of the sub-FAS (71), and A ∈ ℝr×κ0 be an
arbitrarily given matrix. Then the following controller

u (t) = −B−1 T x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, t
( (0∼µk−1) ) ∗
× f xk (t − τj (t)) |k=1∼η, j=1∼ζ, t − u (t) , (90)
{ [ ( ) ]
u∗(t) = Ax(0k∼µk−1)(t) |k=1∼η + v (t) ,

with v (t) being an external input, produces the constant linear system

x(kµk)|k=1∼η (t) = Axk(0∼µk−1)(t) |k=1∼η + v (t) , (91)

provided that the following state constraint is met:

T x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ ∈ 𝔽. (92)

For the multi-order non-affine FAS (72), a result similar to Theorem 2 still holds. In this case, the
controller is given as

u (t) = −g−1 T xk(0∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, t,u ˜ (t) ,
(0∼ (µk−1) ∗ )
u˜ (t) = f xk (t − τj (t)) |k=1∼η, j=1∼ζ, t − u (t) , (93)
{ ( )
u∗(t) = Ax(0k∼µk−1)(t) |k=1∼η + v (t) ,

and the same closed-loop system as (91) is achieved.

Duan G R Sci China Inf Sci January 2023 Vol. 66 112201:17

## [88] `scis_2023_delay1` (PDF p.22, L1416)

Theorem 3. Let Ac be stable, T ∈ ℝm×n be a given matrix. Then, for the system (114) there exists a
constant number κ > 0 satisfying (115). Particularly,
(1) when T = In, an estimate of κ can be given as

κ = ‖P‖ ‖P−1‖, (117)

where P is the solution to the following Lyapunov equation:

ATcP + PAc = −In; (118)

(2) when Ac is non-defective, that is, it has a diagonal Jordan matrix, an estimate of κ can be given as
κ = ‖T V ‖ V −1 , (119)
‖‖ ‖‖
where V is an eigenvector matrix of the matrix Ac;
(3) when Ac is non-defective, an estimate of κ can also be given as
κ = √n bcs V−T ⊗ (T V ) , ∗ = 2 or F. (120)
‖‖ ( )‖‖∗
Recall that Ac = A + BK, all the estimates (117)–(120) are dependent on the feedback gain K.
Particularly, when parametric eigenstructure assignment is applied to the solution of K, the design
degrees of freedom can be used to minimize the number κ through formulas (119) and (120).

## [89] `scis_2023_delay1` (PDF p.23, L1481)

Theorem 4. Let v = 0, d be a positive scalar, T ∈ ℝm×n be a given matrix, 𝔽 ⊂ ℝm be a region
containing the origin, and
𝔹 = {z | ‖z‖ ⩽ d, z ∈ ℝm} ⊂ 𝔽.

If Eq. (124) holds for some κ > 0, then

y (0) ∈ 𝔹0 =⇒ T y (t − σ (t)) ∈ 𝔹, ∀t ⩾ 0, (125)

where
𝔹0 = {y | ‖y‖ ⩽ d, y ∈ ℝn}.
κ

## [90] `scis_2023_delay1` (PDF p.24, L1525)

Theorem 5. Let v ∈ ℝr be a constant vector, ye be given by (126), d be a positive scalar, T ∈ ℝm×n,
𝔽 ⊂ ℝm, and
𝔹 = {z | ‖z − T ye‖ ⩽ d, z ∈ ℝm} ⊂ 𝔽.
If Eq. (128) holds for some κ > 0, then

y (0) ∈ 𝔹0 =⇒ y (t − σ (t)) ∈ 𝔹, ∀t ⩾ σmax, (129)

where
𝔹0 = {y | ‖y − ye‖ ⩽ d, y ∈ ℝn}.
κ
The above result may suit the case that the set 𝔽 ⊂ ℝn may not contain the origin.

## [91] `scis_2023_delay1` (PDF p.24, L1562)

Theorem 6. Let v = 0, d be a positive scalar, TE be defined by (131) and (132), 𝔽 ⊂ ℝm be a region
containing the origin, and
𝔹 = {z | ‖z‖ ⩽ d, z ∈ ℝm} ⊂ 𝔽.
Furthermore, assume that Eq. (124) holds for some κ > 0. Then

y (0) ∈ 𝔹0 =⇒ TEy (t − σj (t)) |j=1∼γ ∈ 𝔹, ∀t ⩾ 0, (134)

where
𝔹0 = {y | ‖y‖ ⩽ d , y ∈ ℝn}.
κs
Corresponding to Theorem 5, we also have the following more general result.

## [92] `scis_2023_delay1` (PDF p.24, L1573)

Theorem 7. Let v ∈ ℝr be a constant vector, ye be given by (126), ze be defined as

T1ye
ze = ... ,

Tγye

d be a positive scalar, TE be defined by (131) and (132), 𝔽 ⊂ ℝm, and

𝔹 = {z | ‖z − ze‖ ⩽ d, z ∈ ℝm} ⊂ 𝔽.

Duan G R Sci China Inf Sci January 2023 Vol. 66 112201:25

x.(t) x.(t) = x(t−τ)

𝔽

𝔹

𝔹0
0 5
x(t−d)

Figure 3 The allowable state regions.

Furthermore, assume that Eq. (130) holds. Then

y (0) ∈ 𝔹0 =⇒ TEy (t − σj (t)) |j=1∼γ ∈ 𝔹, ∀t ⩾ 0, (135)
where
𝔹0 = {y | ‖y − ye‖ ⩽ d , y ∈ ℝn}. (136)
κs
The above result may suit the case that the set 𝔽 ⊂ ℝn may not contain the origin.

## [93] `scis_2023_delay1` (PDF p.27, L1723)

Theorem 8. Let Assumption A5 be satisfied. Further, let [Ai]0∼µi−1 ∈ ℝri×µiri, i = 1, 2, . . . , η be a
set of arbitrarily given matrices. Then the following controller for system (138):

u (t) = −B−1 x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, u (t − ωj (t)) |j=1∼ξ, t u˜ (t) ,

u˜ (t) = f x(0k∼ (µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, u (t − ωj (t)) |j=1∼ξ, t + u)∗(t) ,
( )
[A1]0∼µ1−1 x(01∼µ1−1)(t)
{ [A2]0∼µ2−1 x(02∼µ2−1)(t) (144)
u∗(t) = − v (t) ,
...
[Aη]0∼µη−1 x(0η∼µη−1)(t)

where v is an external input vector, produces the constant linear closed-loop system (94).
Parallelly, the controller for the non-affine FAS (141) is given as

u (t) = −g−1 x(0k∼µk−1)(t − σj (t)) |k=1∼η, j=1∼γ, u (t − ωj (t)) |j=1∼ξ, t,u ˜ (t) ,

u˜ (t) = f x(0k∼ (µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, u (t − ωj (t)) |j=1∼ξ, t + u∗(t)) ,
( )
[A1]0∼µ1−1 x(01∼µ1−1)(t)
{ [A2]0∼µ2−1 x(02∼µ2−1)(t) (145)
u∗(t) = − v (t) ,
...
[Aη]0∼µη−1 x(0η∼µη−1)(t)

and the same closed-loop system as in (94) is achieved.
For the standard multi-order FAS (140), the controller (144) reduces to

u (t) = −f x(0k∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, u (t − ωj (t)) |j=1∼ξ, t − u∗(t) ,
( )
[A1]0∼µ1−1 x(01∼µ1−1)(t)
[A2]0∼µ2−1 x(02∼µ2−1)(t) (146)
{u∗(t) = − v (t) ,
...
[Aη]0∼µη−1 x(0η∼µη−1)(t)

which can also be written as

ui (t) = −fi x(0k∼µk−1)(t − τj (t)) |k=1∼η, j=1∼ζ, u (t − ωj (t)) |j=1∼ξ, t
( )
− [Ai]0∼µi−1 xi(0∼µi−1)(t) + vi (t) , i = 1, 2, . . . , η. (147)

To conclude this section, we remark that the concepts and results proposed in this section can also
be generalized into the case of sub-FASs. Also, the concepts of controllability and stabilizability of the
generalized FASs (138) and (141) can also be defined.

## [94] `scis_2023_delay2` (PDF p.11, L708)

Theorem 1. Let Assumptions A1 and A3 be satisfied, and A0∼n−1 ∈ ℝr×nr be an arbitrarily given
matrix. Then the following controller:

u (t) = −B−1(Z (h − σj (t + h)) |j=1∼γ, t + h) [f (Z (h − τj (t + h)) |j=1∼ζ, t + h) + u∗(t)] ,
u∗(t) = A0∼n−1Z (h) − v (t + h) , t ⩾ 0,
{Z˙(s) = Φ (00∼n−1) Z (s) + Bcf (Z (s − τj (s + t)) |j=1∼ζ, s + t) (59)
+BcB (Z (s − σj (s + t)) |j=1∼γ, s + t) u (s + t − h) , s ∈ [0, h] ,
Z (θ) = x(0∼n−1)(θ + t), θ ∈ [−τ (t) , 0] ,

for the single-order affine system (21) produces the constant linear closed-loop system (57), where v (t)
is an external input vector.

## [95] `scis_2023_delay2` (PDF p.13, L875)

Theorem 2. Let Assumptions A2 and A4 be satisfied, and τ (t) be defined in (68). Further, let
A ∈ ℝr×ηκ0 be an arbitrarily given matrix. Then the following controller:

u (t) = −B−1(Z (h − σj (t + h)) |j=1∼γ, t + h)
× [f (Z (h − τj (t + h)) |j=1∼ζ, t + h) − u∗(t)] ,
u∗(t) = AZ (h) + v (t + h) , t ⩾ 0,
(77)
{Z˙(s) = ΦEZ (s) + BcEf (Z (s − τj (s + t)) |j=1∼ζ, s + t)
+ BcEB (Z (s − σj (s + t)) |j=1∼γ, s + t) u (s + t − h) , s ∈ [0, h] ,
Z (θ) = x(0k∼µk−1)(θ + t)|k=1∼η, θ ∈ [−τ (t) , 0] ,

with the coefficients ΦE and BcE defined in (63)–(65), produces the constant linear system (75).

Duan G R Sci China Inf Sci February 2023 Vol. 66 122201:14

For the multi-order non-affine FAS (32), a result similar to Theorem 2 still holds. In this case, the
controller can be obtained using the differential homeomorphism property of the mapping (35) as

u (t) = −g−1(Z (h − σj (t + h)) |j=1∼γ, t + h,u ˜ (t)) ,
u˜ (t) = f (Z (h − τj (t + h)) |j=1∼ζ, t + h) − u∗(t) ,
u∗(t) = AZ (h) + v (t + h) , t ⩾ 0,
(78)
{Z˙(s) = ΦEZ (s) + BcEf (Z (s − τj (s + t)) |j=1∼ζ, s + t)
+ BcEB (Z (s − σj (s + t)) |j=1∼γ, s + t, u (s + t − h)) , s ∈ [0, h] ,
Z (θ) = x(0k∼µk−1)(θ + t)|k=1∼η, θ ∈ [−τ (t) , 0] ,

and the same closed-loop system as (75) is achieved.
Particularly, if we choose in the above controllers (77) and (78)

A = blockdiag([Ai]0∼µi−1 , i = 1, 2, . . . , η),

where [Ai]0∼µi−1 ∈ ℝri×µiri, i = 1, 2, . . ., η. Then the following set of decoupled constant linear closed-
loop systems are obtained:

x(iµi) = [Ai]0∼µi−1xi(0∼µi−1) + vi, i = 1, 2, . . . , η, (79)

with v being an external input vector given by

v1

v2 ri
v = , vk ∈ ℝ . (80)
...
vη

For a systematic parametric method to solve the controller parameter matrix A such that the closed-loop
linear system possesses a desired eigenstructure, please refer to [39].

## [96] `scis_2024_chained1` (PDF p.10, L629)

Theorem 1. Let Assumption X be met. Then, under the following transformation:
xn−i+1
zi = n−i , i = 1, 2, . . ., n, (32)
x0
system (28) is equivalently transformed into the following system:

z˙1 = g1 (x0, z1, t) + h1 (x0, z1, t) z2,
z˙2 = g2 (x0, z1∼2, t) + h2 (x0, z1∼2, t) z3,

{ ... (33)
z˙n−1 = gn−1 (x0, z1∼n−1, t) + hn−1 (x0, z1∼n−1, t) zn,
z˙n = u,
where

gi (x0, z1∼i, t) = [(n − i) β + ϕn−i (x0, xn−i+1∼n, t)] zi, (34)
hi (x0, z1∼i, t) = γn−iψn−i (x0, xn−i+1∼n, t) , i = 1, 2, . . ., n − 1. (35)

## [97] `scis_2024_chained1` (PDF p.12, L764)

Theorem 2. Let Assumptions X and A3 be satisfied, and gk (x0, z1∼k, t) and hk (x0, z1∼k, t) , k =
1, 2, . . . , n − 1, be differentiable with respect to all variables. With the convention of gn (x0, z1∼n, t) = 0,
let
k
Bk (x0, z1∼k, t) = hi (x0, z1∼i, t) , k = 1, 2, . . . , n − 1, (46)
i∏=1
Bn (x0, z1∼n, t) = Bn−1 (x0, z1∼n−1, t) , (47)

and

fk(x0, z1∼k, t) = f˙k−1(x0, z1∼k−1, t) + B˙k−1(x0, z1∼k−1, t)zk
+Bk−1(x0, z1∼k−1, t)gk (x0, z1∼k, t) , k = 2, 3, . . . , n, (48)

with the initial value
f1 (x0, z1, t) = g1 (x0, z1, t) . (49)
Then, under the following transformation:

z1
f1 (x0, z1, t) + B1 (x0, z1, t) z2
z(0∼n−1) = f2(x0, z1∼2, t) + B2(x0, z1∼2, t)z3 , (50)

...
fn−1(x0, z1∼n−1, t) + Bn−1(x0, z1∼n−1, t)zn

the SFS (33)–(35) is equivalently transformed into the following FAS:

z(n) = fn(x0, z1∼n, t) + Bn(x0, z1∼n, t)u. (51)

The following result confirms some properties of the above transformation (50).

## [98] `scis_2024_chained1` (PDF p.12, L793)

Theorem 3. Let the assumptions in Theorem 2 be met. Then the transformation (50)
(1) is one-to-one;
(2) keeps the origin unmoved; and
(3) guarantees
lim z(0∼n−1) = 0 =⇒ lim z1∼n = 0.
t→∞ t→∞

## [99] `scis_2024_chained1` (PDF p.14, L879)

Theorem 4. Let Assumption A3 be met, β > 0, x0 (0) ≠ 0, and b0∼n−1 be an arbitrary vector making
Φ(b0∼n−1) Hurwitz. Then,
(1) a stabilizing controller for system (6) is given by

u0 = −βx0,
{u = −Bn(x0,z11∼n,t) fn(x0, z1∼n, t) + b0∼n−1z1(0∼n−1) , (59)
[ ]

where z1(0∼n−1) is given by (50), and z1∼n is given by (32); and
(2) the corresponding closed-loop system is a constant linear one given by

x˙0 = −βx0,
{ (n) (0∼n−1) (60)
z1 + b0∼n−1z1 = 0.

Please note that the closed-loop system (60) can also be equivalently written in the following state-space
form:
x˙0 = −βx0,
{ (0∼n−1) (0∼n−1) (61)
z˙1 = Φ(b0∼n−1)z1 .

Since Φ(b0∼n−1) is Hurwitz, z1(0∼n−1) converges to zero exponentially. Therefore, by Theorem 3, z1∼n
also converges to zero.
Obviously, the well-known technique of pole assignment can be applied to solve for the vector b0∼n−1.
Particularly, the complete parametric approach proposed in [31] (see also the Proposition 2 in [35])
can be readily applied. Please note that the controller (59) is smooth under the condition x0 (0) ≠ 0.
Furthermore, when the open-loop system (6) is time-invariant, that is, when all the functions gi (·) and
hi (·) , i = 1, 2, . . ., n − 1 are time-invariant, the above controller (59) is also time-invariant.

## [100] `scis_2024_chained1` (PDF p.16, L1013)

Theorem 5. Let bi, i = 0, 1 be two positive scalars, x0 (0) ≠ 0, and

ψ (x0, x2, t) ≠ 0, ∀x0, x2 ∈ ℝ and t ⩾ 0. (74)

Further, let g (x0, z1, t) and h (x0, z1, t) be defined by (66). Then the following controller for the nonholo-
nomic system (62) drives all the state variables xi, i = 0, 1, 2 to zero:

u0 = −βx0,
{u = −γψ(x01,x2,t) [f2(x0∼2, t) + u∗] , (75)
u∗ = b1γψ (x0, x2, t) x1 + (b0 + b1 [β + ϕ (x0, x2, t)]) xx20,

where f2(x0∼2, t) is given,
(1) when g (x0, z1, t) and h (x0, z1, t) are differentiable with respect to all variables, by

f2 (x0, z1∼2, t) = ˙g (x0, z1, t) + h˙ (x0, z1, t) z2,
{z1 = xx20, (76)
z2 = x1;

(2) when ϕ (x0, x2, t) and ψ (x0, x2, t) are differentiable with respect to all variables, explicitly by

f2(x0∼2, t) = ∆1x1 + ∆2x2,
{∆1 = γ [β + ϕ (x0, x2, t)] ψ (x0, x2, t) + γψ˙ (x0, x2, t) , (77)
∆2 = x0( ˙ϕ (x0, x2, t) + [β + ϕ (x0, x2, t)]2).

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:17

## [101] `scis_2024_chained1` (PDF p.20, L1239)

Theorem 6. Let the assumptions in Theorem 5 be met. Then a controller for the nonholonomic
system (88) is given by (75), with f2(x0∼2, t) being defined as in (91), which drives all the state variables
xi, i = 0, 1, 2 to zero.
If, further, letting ψ (x0, x2, t) ≡ 1 in addition to (87), following the above Theorem 6, we obtain the
following corollary.

## [102] `scis_2024_chained1` (PDF p.21, L1322)

Theorem 7. Let Assumption X be met. Then, under transformation (32), the sub-normal system (28)
with singular set 𝕊x (x0) is equivalently transformed into system (33)–(35) with the following singular
set:
𝕊z (x0) = {z1∼n |hi (x0, z1∼i, t) = 0, z1∼n ∈ ℝn, t ⩾ 0, i = 1, 2, . . ., n − 1} . (97)

Similarly, define the feasible set for the transformed system (33)–(35) as

𝔽z (x0) = ℝn\𝕊z (x0) .

Then, there holds
hi (x0, z1∼i, t) ≠ 0, ∀z1∼n ∈ 𝔽z (x0) , i = 1, 2, . . ., n − 1. (98)

With this understanding, following the proof of Theorem 2, we can also prove the following result.

## [103] `scis_2024_chained1` (PDF p.21, L1335)

Theorem 8. Let Assumption X be satisfied, gk (x0, z1∼k, t) and hk (x0, z1∼k, t) , k = 1, 2, . . ., n be
differentiable with respect to all variables, and Bk(x0, z(0∼k−1), t) and fk(x0, z(0∼k−1), t), k = 1, 2, . . . , n
be given by (46)–(49). Then, for z1∼n ∈ 𝔽z (x0), the transformation (50) is one-to-one, guarantees
limt→∞ z1∼n = 0 if limt→∞ z(0∼n−1) = 0, and transforms the SFS (33)–(35) into the sub-FAS (51) with
the singular set 𝕊z (x0) defined in (97).

## [104] `scis_2024_chained1` (PDF p.21, L1354)

Theorem 9. Let gk (x0, z1∼k, t) and hk (x0, z1∼k, t) , k = 1, 2, . . . , n be differentiable with respect to all
variables. Further, let β > 0, x0 (0) ≠ 0 and b0∼n−1 be an arbitrary vector making Φ(b0∼n−1) Hurwitz.
Then, under the condition of z1∼n ∈ 𝔽z (x0) ,

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:22

(1) a sub-stabilizing controller for system (6) is given by

u0 = −βx0,
{u = −Bn(x0,z11∼n,t) fn(x0, z1∼n, t) + b0∼n−1z(0∼n−1) , (99)
[ ]
where z(0∼n−1) is given by (50), and all zi, i = 1, 2, . . ., n are given by (32); and
(2) the resultant closed-loop system is a constrained constant linear one given by

x˙0 = −βx0,
z(n) + b0∼n−1z(0∼n−1) = 0, (100)
{
z1∼n ∈ 𝔽z (x0) .

By standard notations for the FAS approach, the constrained linear system can also be represented in
the following state-space form:

x˙0 = −βx0,
z˙(0∼n−1) = Φ(b0∼n−1)z(0∼n−1), (101)
{
z1∼n ∈ 𝔽z (x0) .

Recall that, in the globally normal case treated in Sections 4 and 5, a UGE stabilizing controller for
the SFS (33), or equivalently, the second subsystem (28), has been derived. For the sub-normal case,
one may wonder what the function of the designed sub-stabilizing controller (99) is. When 𝔽z (x0) is
not empty, the designed sub-stabilizing controller (99) is no longer a UGE stabilizing controller in the
Lyapunov sense, it may even not be a locally asymptotically stabilizing controller. To better understand
the above result, let us introduce the following definition.

## [105] `scis_2024_chained1` (PDF p.23, L1469)

Theorem 10. Let Assumption X be met. Then, under transformation (32), the time-delay system
described by (103)–(105) is equivalently transformed into the following system:

z˙1 = g1d(·) + hd1(·) z2,
z˙2 = g2d(·) + hd2(·) z3,

{ ... (106)
z˙n−1 = gnd−1(·) + hdn−1(·) zn,
z˙n = u,

where
gid(·) = (n − i) β + ϕdn−i(·) zi, hdi(·) = γn−iψnd−i(·) , i = 1, 2, . . . , n − 1,
with ϕdi(·) and ψid(·) , i[ = 1, 2, . . . , n − 1, given by (104) and (105).]

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:24

The above result can be proven similarly as Theorem 1.
It can be easily figured out that gid(·) is a function of the arguments x0 (t − τn−i,0), z1∼i(t−
τn−i,j)|j=n−i+1∼n, and t − τn−i, while hdi(·) is a function of the arguments x0 (t − σn−i,0), z1∼i(t−
σn−i,j)|j=n−i+1∼n, and t − σn−i, for i = 1, 2, . . ., n − 1. Furthermore, corresponding to Assumptions C1
and C2 on the series of functions ψˆid(·) and ψid(·) , i = 1, 2, . . . , n − 1, we have the following assumption
on the functions hdi(·) , i = 1, 2, . . . , n − 1.

## [106] `scis_2024_chained1` (PDF p.24, L1507)

Theorem 11. Let Assumptions X and C3 be satisfied, and with the convention of gnd(·) = 0, define
k
B˜k ([x0]t , [z1∼k]t , t) = hdi(·) , k = 1, 2, . . ., n − 1, (107)
i∏=1
B˜n ([x0]t , [z1∼n]t , t) = ˜Bn−1 ([x0]t , [z1∼n−1]t , t) , (108)
and
· ·
f˜k ([x0]t , [z1∼k]t , t) = f˜k−1 ([x0]t , [z1∼k−1]t , t) +B˜k−1 ([x0]t , [z1∼k−1]t , t) zk
+ B˜k−1 ([x0]t , [z1∼k−1]t , t) gkd(·) , k = 2, 3, . . . , n, (109)
with the initial value
f˜1 ([x0]t , [z1]t , t) = g1d(·) . (110)
Then, under the following transformation:

z = z1,
z˙ = f˜1 (·) + B˜1 (·) z2,
(111)
{ ...

z(n−1) = f˜n−1 (·) + B˜n−1 (·) zn,

the time-delay SFS (33)–(35) can be transformed into the following FAS with time delays:

z(n) = f˜n ([x0]t , [z1∼n]t , t) + B˜n ([x0]t , [z1∼n]t , t) u. (112)
Clearly, it follows from (107) that Assumption C3 is equivalent to

B˜n ([x0]t , [z1∼n]t , t) ≠ 0,
for all involved variables. Therefore, under Assumption C3, the above system (112) is a global FAS.

## [107] `scis_2024_chained1` (PDF p.24, L1534)

Theorem 12. Let Assumption C3 be met, β > 0, x0 (0) ≠ 0 and b0∼n−1 be an arbitrary vector making
Φ(b0∼n−1) Hurwitz. Then,
(1) a stabilizing controller for system (15)–(17) is given by

u0 = −βx0,

{u = −B˜n([x0]t,[z1∼n]t,t) [f˜n ([x0]t , [z1∼n]t , t) + b0∼n−1z(0∼n−1)], (113)

where z(0∼n−1) is given by (111), and z1∼n is given by (32); and
(2) the resultant closed-loop system is a constant linear one given by (60) or (61).

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:25

To end this subsection, let us point out that the above FAS approach for stabilization of the globally
normal system (15)–(17) with time delays can also be generalized to the time-delay locally normal and
sub-normal cases.

## [108] `scis_2024_chained2` (PDF p.6, L409)

Theorem 1. Let Assumption B be met. Then, under the following transformation:

zi = xn−n−i+1i, i = 1, 2, . . ., n, (26)
σ0

system (25) is equivalently transformed into the following system:

z˙1 = g1′(·) + h′1(·) z2 + ∆f1 (·) ,
z˙2 = g2′(·) + h′2(·) z3 + ∆f2(·) ,

{... (27)
z˙n−1 = gn′−1(·) + h′n−1(·) zn + ∆fn−1 (·) ,
z˙n = u,

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:7

where

gi′(·) ≜ gi′(ζ0, η0, z1∼i, t) = (n − i) β + ϕ′n−i(ζ0, η0, xn−i+1∼n, t) zi, (28)
h′i(·) ≜ h′i(ζ0, η0, z1∼i, t) =[ γn−iψn′−i(ζ0, η0, xn−i+1∼n, t) , ] (29)
∆fi (·) ≜ ∆fi (ζ0, η0, z1∼i+1, t) = −ϑn−iωψn′−i(ζ0, η0, xn−i+1∼n, t) zi+1, (30)

i = 1, 2, . . . , n − 1.

## [109] `scis_2024_chained2` (PDF p.12, L759)

Theorem 2. Let Assumption C be satisfied, u = u (z1∼n, t) be a UGE stabilizing controller for system
(54) such that, with f (x, t) and ∆f (x, t) being given by (58) and (59), respectively, there exist a contin-
uous function V (x, t) : ℝn × ℝ ↦ ℝ and a positive function ρv (t) satisfying the inequalities (46)–(48).
Further, if
∞
∫ ρv (s) ‖ρψ (s)‖ e−(α−β)sds = M < ∞, (63)
0
then u = u (z1∼n, t) is also a controller that UGE stabilizes system (27).
Similarly, using Corollary 3, the following result can also be immediately obtained.

## [110] `scis_2024_chained2` (PDF p.12, L768)

Theorem 3. Let Assumption C be satisfied, gi′(·) and h′i(·) , i = 1, 2, . . ., n − 1, be continuously
differentiable with respect to t, and satisfy one of the following conditions:
(1) The Jacobian matrices ∂g∂zi′(·) and ∂h∂z′i(·), i = 1, 2, . . . , n − 1, are globally bounded, uniformly in t;
1∼i 1∼i
(2) gi′(·) and h′i(·) zi+1, i = 1, 2, . . ., n−1, are globally Lipschitz with respect to z1∼i+1, uniformly in t.
If system (54) is UGE stabilizable with a controller u = u (z1∼n, t), and

∞
∫ ‖ρψ (s)‖ e−(α−β)sds = M < ∞, (64)
0

then system (27) is also UGE stabilizable with the same controller u = u (z1∼n, t).
Conditions (63) and (64) are not strict at all. They allow ρv (t) ‖ρψ (t)‖ or ‖ρψ (t)‖ to diverge with
exponential rates. Specifically, Eq. (63) allows

ρv (t) ‖ρψ (t)‖ < e(α−β)t,

and Eq. (64) allows
‖ρψ (t)‖ < e(α−β)t.

For given functions ψi′(·) , i = 1, 2, . . . , n − 1, these conditions are often satisfied or can be satisfied by
adjusting the design parameters α and β. Therefore, roughly speaking, in most cases the stabilization of
system (27) can be realized by finding a UGE stabilizing controller of system (54).
With the above understanding, again, to solve Problem 1, under Assumption C and the mild condition
(63) or (64), it often suffices to solve Problem 2.

## [111] `scis_2024_chained2` (PDF p.13, L808)

Theorem 4. Let Assumption A′′ be satisfied, and gk′(ζ0, η0, z1∼k, t) and h′k(ζ0, η0, z1∼k, t) , k = 1, 2, . . .,
n − 1, be differentiable with respect to all variables. With the convention of gn′(ζ0, η0, z1∼n, t) = 0, let
k
Bk (ζ0, η0, z1∼k, t) = h′i(ζ0, η0, z1∼i, t) , k = 1, 2, . . . , n − 1, (65)
i∏=1
Bn (ζ0, η0, z1∼n, t) = Bn−1 (ζ0, η0, z1∼n−1, t) , (66)

and

fk(ζ0, η0, z1∼k, t) = f˙k−1(ζ0, η0, z1∼k−1, t) + B˙k−1(ζ0, η0, z1∼k−1, t)zk
+Bk−1(ζ0, η0, z1∼k−1, t)gk′(ζ0, η0, z1∼k, t) , k = 2, 3, . . ., n, (67)

with the initial value
f1 (ζ0, η0, z1, t) = g1′(ζ0, η0, z1, t) . (68)
Then, under the following transformation:

z1
f1 (ζ0, η0, z1, t) + B1 (ζ0, η0, z1, t) z2
z(0∼n−1) = f2(ζ0, η0, z1∼2, t) + B2(ζ0, η0, z1∼2, t)z3 , (69)

...
fn−1(ζ0, η0, z1∼n−1, t) + Bn−1(ζ0, η0, z1∼n−1, t)zn

the SFS (54) is equivalently transformed into the following FAS:

z(n) = fn(ζ0, η0, z1∼n, t) + Bn(ζ0, η0, z1∼n, t)u, (70)

with
Bn(ζ0, η0, z1∼n, t) ≠ 0, ∀ζ0 ∈ ℝ, z1∼n ∈ ℝn, η0 ≠ −αζ0, and t ⩾ 0.
To complete this subsection, let us now consider the case of n = 2. For convenience, in the rest of this
subsection let us omit the subscript in the variables ρ1 (γ1), ˆϕ1 (·), ψˆ1 (·) , ϕ′1(·), ψ1′(·) , g1′(·), and h′1(·).
Then the original system (1) reduces to

x˙0 = u0,
{x˙1 = u, (71)
x˙2 = x2ϕ ˆ (ζ0, η0, x2, u0, t) + ρx1ψˆ (ζ0, η0, x2, u0, t) ,

which is a generalized form of the Brockett’s first example system [2,3]

x˙0 = u0,
{x˙1 = u, (72)
x˙2 = x0x1,

and also the well-known Brockett’s integrator [2,4]

x˙0 = u0,
{x˙1 = u, (73)
x˙2 = x1u0.

Design for the first scalar subsystem of system (71) the controller u0 = −βx0. Then the second
subsystem of system (71), corresponding to (25), is

x˙1 = u,
{ (74)
x˙2 = x2ϕ′(ζ0, η0, x2, t) + ρx1ψ′(ζ0, η0, x2, t) .

Applying the above Theorem 4, immediately gives the following result.

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:14

## [112] `scis_2024_chained2` (PDF p.14, L896)

Theorem 5. Let Assumptions A′′, B, and C be met, a0 and a1 be determined by (15), with α > β > 0,
and b0∼n−1 be an arbitrary vector making Φ(b0∼n−1) Hurwitz. Then (1) a stabilizing controller for
system (1) is given by
t
u0 = −a0 0 x0 (s) ds − a1 (x0 (t) − ζ0) + η0,
u = −Bn(ζ∫0,η10,z1∼n,t) [fn(ζ0, η0, z1∼n, t) + u∗] , (81)
{
u∗ = b0∼n−1z(0∼n−1),

where z1∼n is given by (69), ζ0 = x0 (0) , and η0 ≠ −αζ0 is a design parameter; and (2) the corresponding
closed-loop system is given by

x¨0 + a1x ˙0 + a0x0 = 0, ζ0 = x0 (0) , ˙x0 (0) = η0,
{z(n) + b0∼n−1z(0∼n−1) = 0, (82)

or equivalently, by
x¨0 + a1x ˙0 + a0x0 = 0, ζ0 = x0 (0) , ˙x0 (0) = η0,
{z(0∼n−1) = Φ(b0∼n−1)z(0∼n−1). (83)
˙

It should be noted that the states of the original system (1) include only x0∼n, but not ˙x0. It can be
recognized that the designed controller (81) is, in nature, a feedback of the system states x0∼n. Relative
to the original system (1), η0 is an external design parameter. It is only required to meet the condition
η0 ≠ −αζ0 = −αx0 (0) , and can be almost arbitrarily chosen.
Obviously, the well-known technique of pole assignment can be applied to solve for the vector b0∼n−1.
Particularly, the complete parametric approach proposed in [24] (see also the Proposition 2 in [27]) can
be readily applied. Please note that the controller (81) is smooth under Assumption B. Different from
the discontinuous controller designed in [1], even when the open-loop system (1) is time-invariant, that
is, when all the functions gi (·) and hi (·) , i = 1, 2, . . ., n − 1, are time-invariant, the above controller (81)
is still time-varying.
In the case of n = 2, we immediately have the following result.

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:15

## [113] `scis_2024_chained2` (PDF p.16, L1034)

Theorem 6. Let Assumption C be satisfied, and z1∼n(Z0, ζ0, η0, t) given by Algorithm 1 UGE converge
to zero for all Z0 ∈ ℝn, ζ0 ∈ ℝ, and η0 ≠ −βζ0. If, further,
∞
∫ ‖ρψ (s)‖ e−(α−β)sds = M < ∞, (99)
0

then u = u (ζ0, η0, z1∼n, t) given by (81) is a controller that UGE stabilizes the system

z˙1 = g1′(·) + h′1(·) z2 + ∆f1(·) ,
z˙2 = g2′(·) + h′2(·) z3 + ∆f2 (·) ,

{... (100)
z˙n−1 = gn′−1(·) + h′n−1(·) zn + ∆fn−1(·) .
z˙n = u (ζ0, η0, z1∼n, t) .

Through examining (98), we can conclude that in many cases z1∼n(Z0, ζ0, η0, t) exponentially converges
to zero. The following corollary reveals a particular case.

## [114] `tcyb_2023_robustdelay` (PDF p.7, L828)

Theorem 1: Let A0∼n−1 ∈ ℝr×nr be a matrix satisfy-
ing (36), and Assumptions B2–B4 be met. Then, a control
law that robustly input-to-state stabilizes the uncertain FAS
in (22), with z(0∼n−1) being viewed as the system external
input, is given by
u = −B−1(·)(f(·) + u∗)
{u∗ = (A0∼n−1 + Θ)x(0∼n−1) (40)

with
{Θ = 1εσ2 1(PL)ϑPTL
min 1 (41)
ϑ = σmax(PL)ρ(·)+2σ 2(·)
where ε ∈ (0, 1) is an arbitrarily chosen number.
Substituting the control law (40) into the FAS in (22) gives
the following closed-loop system:
x(n) = −(A0∼n−1 + Θ) x(0∼n−1)
+ Δf(·) + h(z(0∼m−1)) (42)

which has the following equivalent state-space form:
x(0∼n−1) = Φ(A0∼n−1 + Θ) x(0∼n−1)
˙
+ [ 0(n−1()0r∼m−1) ]. (43)
Δf(·) + h z
( )
Therefore, Theorem 1 immediately follows from the following
technical lemma.

## [115] `tcyb_2023_robustdelay` (PDF p.8, L966)

Theorem 2: Let [Ai]0∼μi−1 ∈ ℝri×riμi, i = 1, 2, . . . , η, be
a set of matrices satisfying (44), Assumptions A2–A4 be met.
Then, a control law that robustly input-to-state stabilizes the
uncertain FAS in (17), with zk(0∼γk−1)|k=1∼ξ being viewed as
the system input, is given by (46)-(47) with ε ∈ (0, 1) being
an arbitrarily given number.
In view of Proposition 1, we immediately have from the
above result the following corollary, which gives the solution
to Problem 1.

## [116] `tcyb_2023_robustdelay` (PDF p.8, L1026)

Theorem 3: Let A0∼n−1 ∈ ℝr×nr be a matrix satisfy-
ing (36), Assumptions B0, B3′, and B4 hold. Then, a controller
that robustly input-to-state stabilizes the uncertain FAS in (50),
with z(0∼m−1) being viewed as the system external input, is
given by
u = −B−1 x(0∼n−1), ζx, ζu, t u′
⎧⎨u′ = f x(0∼(n−1), ζx, ζu, t + u)∗ (52)
u∗ = (A0∼n−1 + Θ x(0∼)n−1)
⎩ [ ]
with
⎧Θ = 1εσ2 1(PL)ϑPTL(A0∼n−1)
⎪⎨ϑ = σmax2min(PL)ρ x(0∼n−1), ζx, ζu, t (53)
+ 12σ 2 x((0∼n−1), ζx, ζu, t )
⎪⎩ ( )
where ε ∈ (0, 1) is an arbitrarily given number.
The following result immediately follows from Theorem 3
and Corollary 1.

## [117] `tcyb_2023_robustdelay` (PDF p.9, L1141)

Theorem 4: Let A0∼n−1 ∈ ℝr×nr be a matrix satisfy-
ing (36), and Assumptions B2–B6 be met. Then, a control
law that robustly input-to-state stabilizes the uncertain FAS
in (54), with z(0∼m−1) being viewed as the system external
input, is given by (56) and (62), with ε ∈ (0, 1 − c) being an
arbitrary scalar.
To end this section, we point out that the above results can
be also generalized into the multiorder FAS case.

C. Robust Control of FASs
Again here we only demonstrate the case of single-order
FASs.
When the second subsystem in (50) does not exist, the type I
system (50) becomes the following uncertain FAS:

x(n) = f(x(0∼n−1), ζx, ζu, t)+ Δf(x(0∼n−1), ζx, ζu, t)

+ B(x(0∼n−1), ζx, ζu, t)u (63)

where the matrix B(x(0∼n−1), ζx, ζu, t) still satisfies the full-
actuation Assumption B0, while Assumption B3′ on the
nonlinear uncertainty Δf(·) becomes the following assump-
tion.

## [118] `tcyb_2023_robustdelay` (PDF p.9, L1171)

Theorem 5: Let A0∼n−1 ∈ ℝr×nr be a matrix satisfy-
ing (36), Assumptions B0 and B3′′ be met. Then, a controller
that robustly and globally stabilizes the uncertain FAS in (63)
is given by (52)-(53) with σ(x(0∼n−1), ζx, ζu, t) being set to
zero.
It is easy to note that, in the case of ρ(x(0∼n−1), ζx,
ζu, t) ≡ 0, the uncertainty Δf(·) does not exist, and the
FAS (63) becomes the following deterministic one:

x(n) = f(·) + B(·)u (65)

while the controller simply reduces to
u = −B−1(·) f(·) + u∗
{u∗ = A0∼n−1x((0∼n−1). ) (66)

As a consequence, the controller (66) serves as a controller for
the above FAS (65). This is clearly a direct extension to [34,
Proposition 3.1], and also a restatement of the result in [40].
Meantime, it follows from Corollary 1 that the control law (66)
GUA stabilizes the type I system (12)–(13). Such a fact gives
a clear explanation of the concept of stabilizability proposed
in [34, Sec. 4.1].

D. Solution of A0∼n−1
It is seen from the above sections that our solutions to the
formulated robust stabilization problems depend heavily on
the parameter matrix A0∼n−1 satisfying (36), or the series of
parameter matrices [Ai]0∼μi−1 ∈ ℝri×riμi, i = 1, 2, . . . , η,
satisfying (44). Now in this section let us state an existing
parametric solution to these parameter matrices.
Without loss of generality, here we only quote a result on
the parametric solution of the matrix A0∼n−1 satisfying (36),
which is actually [28, Corollary 1] (see [30]–[32]).

## [119] `tcyb_2023_subfas` (PDF p.7, L835)

Theorem 1: Let 𝔽 ⊂ ℝm, m ≤ γ nr, be the feasible set of
the single-order affine sub-FAS (18), and A0∼n−1 ∈ ℝr×nr be
an arbitrarily given matrix which makes Φ(A0∼n−1) stable.
Then
1) a substabilizing controller for the single-order affine sub-
FAS (18) is given by (30);
2) the resulting closed-loop system is given by
x(n)(t) + A0∼n−1x(0∼n−1)(t) = 0
{Tx(0∼n−1) t − σj(t) |j=1∼γ ∈ 𝔽, t ≥ 0 (32)
( )
3) the ROEA of the system is given by

⎧ ϕ(TeΦ(A0∼n−1)(t−σj(t))X0 , t) ≠ 0 ⎫
Rs = ⎨X0 |||j=1∼γ ⎬
||||||X0 ∈ ℝnr and t ≥ 0
⎩ ⎭
where ϕ(·) is the singularity function of the sub-
FAS (18).

## [120] `tcyb_2023_subfas` (PDF p.8, L931)

Theorem 2: Let Assumption 1 be met, 𝔽 ⊂ ℝm1, m1 ≤
γ nr1, be the feasible set of the single-order affine sub-
FAS (18), and Ai,0∼n−1 ∈ ℝri×nri, i = 1, 2, be two arbitrarily
given matrices which make Φ(Ai,0∼n−1), i = 1, 2, stable.
Then
1) a substabilizing controller for the single-order affine sub-
FAS (18) is given by (38);
2) the resulting closed-loop system is composed of the
following constrained linear system:

{x1(n) + A1,0∼n−1x1(0∼n−1) = 0
T1x1(0∼n−1) t − σj(t) |j=1∼γ ∈ 𝔽, t ≥ 0 (39)
( )
and the following constraint-free linear system:

x2(n) + A2,0∼n−1x2(0∼n−1) = 0, t ≥ 0 (40)

3) the ROEA of the closed-loop system is given by

R0s = X2| X2 ∈ ℝnr2
{ }
⎧ ϕ(T1 eΦ(A1,0∼n−1)(t−σj(t))X1 , t) ≠ 0 ⎫
×⎨X1 |||j=1∼γ ⎬.
||||||X1 ∈ ℝnr1, and t ≥ 0
⎩ ⎭
In order to solve eΦ(A0∼n−1)t or eΦ(Ai,0∼n−1)t, i = 1, 2, a basic
parametric result quoted in [40], [44], and [49] can be readily
applied.
For a proper detailed example demonstrating the above the-
ory of substabilization of a single-order FAS, please refer
to [38].

## [121] `tcyb_2023_subfas` (PDF p.8, L977)

Theorem 3: Let AE ∈ ℝM be a Hurwitz matrix. Then, a
substabilizing controller for the multiorder affine sub-FAS (25)
is given by

u(t) =
⎧−B−1(Txk(0∼μk−1) t − σj(t) |k=1∼η, j=1∼γ , t)u′(t)
⎪⎪⎪⎪⎪⎪⎨ ( )
u′(t) = (42)
f(xk(0∼μk−1) t − τj(t) |k=1∼η, j=1∼ζ, t)+ u∗(t)
( )
⎪⎪⎪⎪⎪⎪⎩u∗(t) = AExk(0∼μk−1)(t)|k=1∼η

which results in the following constrained linear closed-loop
system:

{xk(μk)|k=1∼η = −AExk(0∼μk−1)|k=1∼η
Txk(0∼μk−1) t − σj(t) |k=1∼η, j=1∼γ ∈ 𝔽. (43)
( )
Furthermore, the ROEA of the designed system is given by

⎧ ϕ(T eAE(t−σj(t))X0 , t) ≠ 0 ⎫
Rm = ⎨X0 |||j=1∼γ ⎬.
||||||X0 ∈ ℝκ, and t ≥ 0.
⎩ ⎭
Obviously, when AE is particularly chosen as

AE = diag(Ai, 0∼μi−1, i = 1 ∼ η)
where Ai, 0∼μi−1 ∈ ℝri×riμi, i = 1 ∼ η, the controller (42)
becomes
u(t) =
⎧−B−1(Txk(0∼μk−1) t − σj(t) |k=1∼η, j=1∼γ , t)u′(t)
( )
u′(t) =
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨f(xk(0∼μk−1) t − τj(t) |k=1∼η, j=1∼ζ, t)+ u∗(t)
( )
u∗1(t) (44)
⎡u∗2(t)⎤
u∗(t) =
⎢⎢⎢⎣ ... ⎥⎥⎥⎦
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ u∗η(t)
u∗i(t) = Ai, 0∼μi−1xi(0∼μi−1)(t), i = 1 ∼ η
and the closed-loop system is now composed of η number of
constant linear ones
xi(μi) = −Ai, 0∼μi−1xi(0∼μi−1), i = 1 ∼ η (45)

which need to satisfy the feasibility constraint (41). This gives
a natural decoupled design in correspondence to the structure
of the multiorder affine sub-FAS (25). In the next section, let
us propose another decoupled solution which separates the free
state variables from the constrained ones.

B. Block Decoupled Design
To carry out the general design, we need to define a
sequence qi, i = 0 ∼ l, as q0 = 0, and

1 ≤ q1 < q2 < · · · < ql = η.

The following set of numbers are also needed:
qk qk
ϱk = ∑ ri, κk = ∑ riμi, k = 1 ∼ l.
i=qk−1+1 i=qk−1+1
The idea of the design can be described as follows.
1) The first q1 number of states, namely, xk, k = 1 ∼
q1, are grouped together as xk(μk)|k=1∼q1 ∈ ℝϱ1,
xk(0∼μk−1)|k=1∼q1 ∈ ℝκ1 and will be produced by a
single linear system in the closed loop.

## [122] `tcyb_2023_subfas` (PDF p.9, L1090)

Theorem 4: Let Assumption 2 be met, and 𝔽 ⊂ ℝM be the
feasible set of the sub-FAS (25), and Ai ∈ ℝϱi×κi, i = 1 ∼ l,
be a series of arbitrarily given block-diagonal companion
matrices. Then
1) a substabilizing controller for the multiorder affine sub-
FAS (25) is given by (47);
2) the resulting closed-loop system is composed of the
following constrained linear system:

{xk(μk)(t)|k=1∼q1 = −Ψ1xk(0∼μk−1)(t)|k=1∼q1
Txk(0∼μk−1) t − σj(t) |k=1∼q1, j=1∼γ ∈ 𝔽 ∀t ≥ 0 (48)
( )
and the following unconstrained ones:

xk(μk)(t)|k=qi−1+1∼qi
= −Ψixk(0∼μk−1)(t)|k=qi−1+1∼qi
i = 2 ∼ l (49)

3) the ROEA of the closed-loop system is given by

0 ⎧⎡X2⎤ Xi ∈ ℝκi,⎫
Rm = ⎪⎨ ... |||||||i = 2 ∼ l ⎪⎬
⎢⎣Xl ⎥⎦
⎪⎩ ⎪⎭
⎧ ϕ(T eΦE(t−σj(t))X1 , t) ≠ 0 ⎫
×⎨X1 |||j=1∼γ ⎬
||||||X1 ∈ ℝκ1, and t ≥ 0
⎩ ⎭
where
X1 = xk(0∼μk−1)(0)|k=1∼q1
Xi = xk(0∼μk−1)(0)|k=qi−1+1∼qi, i = 2 ∼ l

are the initial values of the system, and ΦE is the system
matrix of the following linear system:

x˙k(0∼μk−1)(t)|k=1∼q1 = ΦExk(0∼μk−1)(t)|k=1∼q1 (50)

which is the equivalent state-space form of the linear
system in (48).

## [123] `tcyb_2024_overview` (PDF p.4, L508)

Theorem 1: The linear system (11) is controllable if and
only if it can be converted equivalently into the following
multi-order global FAS:

x(1µ1) L1(x(0k∼µk−1)|k=1∼η)

x(2µ2) L2(x(0k∼µk−1)|k=1∼η)
= + Bu,˜ (12)
... ...
x(ηµη) Lη (x(0k∼µk−1)|k=1∼η)

where η ≥ 1 is an integer, µk, k = 1, 2, . . . , η, are a set of
integers, xk ∈ ℝrk, k = 1, 2, . . . , η, are a set of state vectors,

with rk, k = 1, 2, . . . , η, being a set of distinct integers
satisfying (3). Further, Lk (·) , k = 1, 2, . . . , η, are a set of
linear functions, and B˜ ∈ ℝr×r is a constant square upper-
triangular matrix with diagonal elements all being 1.
The above result is firstly proved in [3] based on a con-
trollability form of system (11). A frequency-domain version
of the proof is given in [24]. It was revealed in [24] that the
integers µk, k = 1, 2, . . . , η, are actually the controllability
indices of system (11). A discrete-time version of the above
result can be found in [14], and for generalization to discrete-
time systems with both state and input constant delays, please
refer to [20], [21].
The above result is a fundamental contribution to linear
system theory. It is important because of the following two
aspects:
1) It actually reveals that the FAS is really a canonical
controllability form of a general multi-variable linear system,
which cannot be derived within the state-space framework;
2) It provides a natural, and extremely easy and robust
way to realize control of linear systems by means of pole
assignment (see Subsection IV-D).

B. Feedback Linearizable Systems

Consider the nonlinear system

x˙ = f (x, u) , (13)

where x ∈ ℝn and u ∈ ℝr are the state vector and input
vector, respectively, f (·) ∈ ℝn is a sufficiently smooth
function satisfying the initial condition f (x0, u0) = ˙x0. A
strict definition can be found in [25] for system (13) to be
locally feedback linearizable at (x0, u0) via the differentiable
feedback:

∂
u = ξ (x, v) , ξ (x0, 0) = u0, rank ξ (x0, 0) = r. (14)
∂v

The following result indicates that a feedback linearizable
system can be represented by a FAS model (a modified version
of that in [2]).

## [124] `tcyb_2024_overview` (PDF p.5, L566)

Theorem 2: Let system (13) be locally feedback linearizable
at (x0, u0) via the feedback (14). Then it is equivalent to a
FAS in the form of (2) within a neighborhood of (x0, u0).
A discrete-time version of the above result can be found in
[14].

## [125] `tcyb_2024_overview` (PDF p.6, L689)

Theorem 3: Let system (13) possess, on 𝕏 ⊂ ℝn, a control-
oriented flat output y in the form of (20) satisfying (19) and
(23). Then system (13) can be equivalently converted on 𝕏 ⊂
ℝn, with the homeomorphism transformation (19), into a sub-
FAS in the form of (27) with the feasible set

𝔽 = φ−1(𝕏) ∩ 𝔾.

From the above we can reveal the following different views
from the points of the state-space approach and the FAS
approach:
1) Flat system theory was motivated by the problem of
path planning, and looks upon y as an output and the
two equations (17) and (18) as a pair of solutions to the
differential equation (13) ([28], [29]), dispite of the fact
that y is often chosen by the designer but not produced
by practical observations.

2) FAS approach aims to find a homeomorphism trans-
formation with which the original system (13) can be
equivalently converted into a FAS, and looks upon
equation (17) as a transformation from x to a new
variable y, and (18) as the transformed system.
To end this subsection, let us point out that the above
development can be generalized to more complex systems,
such as time-varying systems. A description of a nonaffine
sub-FAS can also be provided.

E. Systems with A Full Set of Relative Degrees
Again, let us consider system (13). When an output of the
system is prescribed, relative degrees of the system associated
with this output are well defined (see [25], [30]). The following
definition clarifies a full set of relative degrees of a nonlinear
system associated with an output.

## [126] `tcyb_2024_overview` (PDF p.7, L777)

Theorem 4: Let y ∈ ℝr be an output of system (13) having
a set of control-oriented relative degrees µk, k = 1, 2, . . . , η,
on 𝕏 ⊂ ℝn. Then, the mapping φ1∼η defined by (31) is
a homeomorphism, under which system (13) is equivalently
converted into the following sub-FAS:

yk(µk)|k=1∼η = f (yk(0∼µk−1)|k=1∼η)+B(yk(0∼µk−1)|k=1∼η)u,
(34)
with

f (·) = f1∼η (φ−1∼1η (yk(0∼µk−1)|k=1∼η)), (35)

B (·) = b1∼η (φ−1∼1η (yk(0∼µk−1)|k=1∼η)), (36)

and the following feasible set:

𝔽 = φ−1∼1η (𝕏) ∩ 𝔽b, (37)

where

𝔽b = {Y |det B (Y ) ≠ 0 or ∞, Y ∈ ℝn} . (38)

Again, the results in this section can be generalized to more
complicated systems. We also point out that a more concrete
and positive result can be obtained for the single-input system
case.
In the case that the set of relative degrees is not full, an
extra subsystem appears. System control in such a case can
also be solved with the FAS approach [11], [31]. Please note
that the FAS approach is not an approach treating only FASs;
it is an approach treating systems involving FASs.

F. Further Examples
Let us mention that some more general types of nonlinear
systems can be converted into FASs [3], [5], [14]. Particularly,
in [32], we present ways to convert four types of UASs
equivalently into FASs. The first two types of treated UASs
are briefly described below. Please note that our generalized
FASs are not restricted to second-order systems, and neither
are the UASs.

## [127] `tcyb_2024_overview` (PDF p.7, L876)

Theorem 5: Let A0∼n−1 ∈ ℝr×nr be a set of arbitrarily
given matrices. Then the following controller
u = −B−1 (·) A0∼n−1x(0∼n−1) + u∗
{ u∗ = f(x(0∼n−(1), t) − v, ) (45)

for system (1), with v ∈ ℝr being an external signal, produces
the time-invariant linear closed-loop system
x(n) + A0∼n−1x(0∼n−1) = v. (46)

It should be noted that the linear system (46) is equivalent
to the following state-space form:
x˙(0∼n−1) = Φ (A0∼n−1) x(0∼n−1) + Bcv, (47)

where
T
Bc = [ 0 · · · Ir ] . (48)

Note that the coefficient matrix A0∼n−1 in (46) is at the
designer’s choice. The above result indicates that a controller
for a FAS can be easily designed, which results in a time-
invariant linear closed-loop system with an arbitrarily desired
eigenstructure.
Furthermore, it can be easily observed that, when all Ai,
i = 0, 1, . . . , n − 1, are chosen to be diagonal, r number
of decoupled systems can be immediately obtained. This
fact states that system decoupling, as a hard problem in the
nonlinear control field, can also be easily solved with the FAS
approach. Also, we remark that the above comments also apply
to the case of sub-FAS control discussed in Subsection IV-B.

## [128] `tcyb_2024_overview` (PDF p.8, L914)

Theorem 6: Let Ak,0∼µk−1 ∈ ℝrk×µkrk, k = 1, 2, . . . , η,
be a set of arbitrarily given matrices. Then the following
controller

A1,0∼µ1−1x(01∼µ1−1)
A2,0∼µ2−1x(02∼µ2−1)
u = −B−1(·) + u∗
{ ...
Aη,0∼µη−1x(0η∼µη−1)
u∗ = f (x(0k∼µk−1)|k=1∼η, t)− v,
(49)
for system (2), with

v = v1T v2T · · · vηT T , vk ∈ ℝrk, (50)
[ ]
being an external signal, produces the following set of time-
invariant linear closed-loop systems:

x(kµk) + Ak,0∼µk−1x(0k∼µk−1) = vk, k = 1, 2, . . . , η. (51)

The stability and performance of the closed-loop sys-
tem can be achieved by properly selecting the coefficients
Ak,0∼µk−1, k = 1, 2, . . . , η (see Subsection IV-D).

B. Sub-Stabilization of Sub-FASs

## [129] `tcyb_2024_overview` (PDF p.8, L947)

Theorem 7: Let 𝔽 be the set of feasibility of FAS (1), and
A0∼n−1 ∈ ℝr×nr be an arbitrarily given matrix. Then, when
the system initial value X0 ≜ x(0∼n−1)(0) is restricted within
the RoEA R0, the controller (45) for system (1), with v = 0,
produces the time-invariant linear closed-loop system

x(n) + A0∼n−1x(0∼n−1) = 0, (52)

whose response satisfies

x(0∼n−1)(t) ∈ 𝔽, ∀t ≥ 0. (53)

It should be noted that the condition (53) guarantees the
effectiveness of the controller (45).
It is seen that sub-stabilization requires the system initial
value to be chosen from the RoEA. Generally speaking, this
is not a strict restriction since in most applications the RoEA
is large enough. In those cases where the initial value must
be chosen outside the RoEA, a pre-controller can be usually
easily designed to drive the trajectory of the system into the
RoEA first, and then let the sub-stabilizing controller take over.

## [130] `tcyb_2024_overview` (PDF p.8, L982)

Theorem 8: Let 𝔽 ⊂ ℝκ be the set of feasibility of the
system (2), whose dimension is greater than 1. Further, let
Ak,0∼µk−1 ∈ ℝrk×µkrk, k = 1, 2, . . . , η, be a set of arbitrarily
given matrices. Then, when the system initial values Xk0 ≜
x(0k∼µk−1)(0), k = 1, 2, . . . , η, are restricted within the RoEA
R, the controller (49) for system (2), with v = 0, produces
the following set of time-invariant linear closed-loop systems

x(kµk) + Ak,0∼µk−1x(0k∼µk−1) = 0, k = 1, 2, . . . , η, (54)

whose responses satisfy

x(0k∼µk−1)|k=1∼η (t) ∈ 𝔽, ∀t ≥ 0. (55)

Let
Q = ℝκ\R,

then Q is called the region of dead zone, since for an initial
value X0 ≜ x(0k∼µk−1)|k=1∼η (0) ∈ Q, we have

x(0k∼µk−1)|k=1∼η (t) ∈ 𝕊, ∀t ≥ 0. (56)

In this case, the controller (49) becomes invalid.
The type of closed-loop stability resulted in by the above
sub-stabilization is called sub-stability (see [15]), which differs
from the well-known Lyapunov stability in the following
aspects.
1) The region of attraction for Lyapunov stability is a
simply-connected region containing the origin as an
interior point, and is usually regarded as a ball centered
at the origin, while the RoEA R of sub-stability may be
much more complicated. It may not be convex, or may
not even be simply-connected.
2) Note that only when R, the RoEA, contains the origin
as an interior point, we can construct a ball centered
at the origin within R, which serves as a region of

attraction in the Lyapunov sense. With this observation,
we can immediately conclude that sub-stability implies
local Lyapunov stability when the RoEA R contains the
origin as an interior point.
To end this subsection, we point out that the work in [15]
really presents the sub-stabilization results for the general
nonlinear time-varying FAS with time-varying delays.

C. Stabilization of Possibly Uncontrollable Systems
The FAS approach is not only suitable for investigation
of systems which can be converted into FASs, but is also
applicable to systems which involve FASs as only sub-systems.
In [31], stabilization of a complicated type of uncertain
systems is effectively treated with the FAS approach. Due to
the page limit, here we only describe a simple case in which
the dynamical systems appear in the following form:
x(n) = f (·) + ∆f (·) + B (·) u + h z(0∼m−1)
{ z(m) = g z(0∼m−1), t , ( ) (57)
( )
where
f (·) = f (x(0∼n−1), z(0∼m−1), t),

∆f (·) = ∆f (x(0∼n−1), z(0∼m−1), t),

B (·) = B(x(0∼n−1), z(0∼m−1), t),

are piece-wise continuous functions, and h z(0∼m−1) is a
( )
K∞-bounded function (see the Definition 3 in [31]). The

## [131] `tcyb_2024_overview` (PDF p.10, L1204)

Theorem 9: Let f0 x(0∼n−1), t ∈ ℝr be a desired function
( )
in certain sense. 𝔽 be the set of feasibility of sub-FAS (1).
Then the following controller

u = −B−1(·)(f(x(0∼n−1), t) − f0(x(0∼n−1), t)) (63)

for sub-FAS (1) produces the following constrained closed-
loop system
x(n) = f0 x(0∼n−1), t
{ x(0∼n−1)((t) ∈ 𝔽, t ≥) 0. (64)

Let us point out that the saying that f0 x(0∼n−1), t ∈ ℝr
( )
is a desired function in the above result means that the closed-
loop system (64) possesses some desired features.
With our notations, the above closed-loop system in (64) is
equivalent to the following state-space form:

x˙(0∼n−1) = Φ (00∼n−1) x(0∼n−1) + Bcf0(x(0∼n−1), t),
(65)
where Bc is given by (48). When expended, the above system
(65) can be equivalently converted into the following one:

x˙1 = x2
x˙2 = x3 (66)
{ x˙n−1 = xn
x˙n = f0 (x1∼n, t) ,
under the differential homeomorphism

xi = x(i−1), i = 1, 2, ..., n,

which permits the relation

f0(x(0∼n−1), t) = f0 (x1∼n, t) .

In the rest of this subsection, let us concentrate on the
specific problem of finite-time stabilization (see [37], and the
review paper [38]). For convenience of presentation, let us
introduce the following definition.

## [132] `tcyb_2024_overview` (PDF p.11, L1290)

Theorem 10: The controller (63) is a finite-time sub-
stabilizing controller for sub-FAS (1) if f0 (x1∼n, t) is a func-
tion permitting finite-time stability. Furthermore, the closed-
loop system is given by (64), with the initial values being
chosen within the region of finite-time attraction Rf.
To end this subsection, let us make the following comments:
1) Following the ideas in this subsection, we can consider
control of the single-order FAS (1), or the multi-order
FAS (2), with other properties by similarly defining
functions permitting certain other properties.
2) Different from the design of a sub-linearizing controller,
the defined region of finite-time attraction Rf may be
hard to derive. However, for a global FAS, there does not
exist a singularity condition, and the problem of solving
this region of finite-time attraction Rf is not needed. As
a matter of fact, many researches on nonlinear systems

are focused on the well-known strict-feedback systems,
which have been proven to be global FASs ([3], [42]).

## [133] `tcyb_2024_overview` (PDF p.13, L1607)

Theorem 11: Let the variables B˘k x(0∼k−1), t and
h˘k x(0∼k−1), t , k = 1, 2, . . . , n, be given by (79), (80)()
( )

and (83). Then, when x1∼n ∈ 𝔽ˆ, the sub-SFS (77) can be
equivalently converted into the following sub-FAS under the
transformation (82):
x(n) = h˘n(x(0∼n−1), t)+ B˘n(x(0∼n−1), t)u. (84)

Therefore, stabilization of the sub-SFS (77) can be realized
by carrying out the sub-stabilization of the sub-FAS (84).

## [134] `ucfas_2025_part1` (PDF p.10, L1071)

Theorem 6.1: Let systems (72)–(74) be all SFSs with
respect to variables x1∼nx, y1∼ny and z1∼nz, respectively.
Then

(1) in the case that the individual SFSs (72)–(74) all
have consistent dimensions, the overall UC-SFS
(72)–(74) can be equivalently converted into a
single-order UC-FAS; and
(2) in the case that one of the individual SFSs (72), (73)
or (74) has increasing dimensions, the overall UC-
SFS (72)–(74) can be equivalently converted into a
multi-order UC-FAS.

(0∼γ1 x)
When ux is not present in (73), system (72)–
(73) can be actually converted into a FAS, instead of a
(0∼γ1x) (0∼γ2x) (0∼γy)
UC-FAS. When ux , ux and uy are all not
present, the whole UC-SFS (72)–(74) can be converted
into a FAS instead of a UC-FAS.
To conclude this subsection, let us give the following
remarks.

## [135] `ucfas_2025_part2` (PDF p.5, L451)

Theorem 2.1: Let ∅ ≠ 𝔽 ⊂ ℝnr be the set of feasibil-
ity of the constrained FAS (1) and (2), defined by (11),
and A0∼n−1 ∈ ℝr×nr be an arbitrarily given matrix.
Then, when the system initial value X0 ≜ x(0∼n−1)(0) is
restricted within the RoEA R, the controller (6) produces
the linear closed-loop system (7), whose response is given
by (12) and satisfies the constraint (2) and x(0∼n−1)(t) ∈
𝔽in.

## [136] `ucfas_2025_part2` (PDF p.5, L528)

Theorem 2.2: Let ∅ ≠ 𝔽 ⊂ ℝκ be the set of feasi-
bility of the constrained FAS (3) and (4). Further,

let Ak,0∼μk−1 ∈ ℝrk×μkrk, k = 1, 2, . . . , η, be a set of
arbitrarily given matrices. Then, when the system ini-
tial value X0 ≜ xk(0∼μk−1)|k=1∼η(0) ∈ R, the controller
(16) produces the closed-loop systems in (18), whose
responses are given by

x(0∼μk−1)|k=1∼η (t)
k
[ [ ( ) ] ]
= exp Φ Ak,0∼μk−1 t Xk0 |k=1∼η ∈ 𝔽,

t ≥ 0, k = 1, 2, . . . , η. (21)

For solution of the parameter matrices Ak,0∼μk−1 ∈
ℝrk×μkrk, k = 1, 2, . . . , η, a thorough study has been
given in Duan et al. (2024).
To end this section, let us give a few remarks.

## [137] `ucfas_2025_part2` (PDF p.9, L973)

Theorem 3.1: The UC-FAS (22)–(24) has a sub-
stabilising controller if Rxyz is not empty, and in this
case, the controller is given by (33), (43), and (52),
with (X†0, Y†0, Z†0) ∈ Rxyz. Furthermore, the closed-
loop system is composed of linear systems (34), (44) and
(53), with responses satisfying

( )
x(0∼nx−1)(t) , y(0∼ny−1) (t) , z(0∼nz−1)(t) ∈ 𝔽xyz.

We mention again, in view of Remark 2.1, that
the requirement (X†0, Y†0, Z†0) ∈ Rxyz is not a prob-
lem in many applications since Rxyz is usually big
enough. In the case that an initial value must be cho-
sen from the complement of Rxyz, often a coordinate
translation can solve the problem (see the Remark 5.1
in Duan, 2025a). Otherwise, a state regional transfer
problem, which is usually easy to handle, needs to be
solved to find a pre-controller to drive the trajectory
into Rxyz.
The above sub-stabilisation process is illustrated
in Figure 1, where Σi represents the i-th subsystem,
i = 1, 2, 3.

Figure 1. Illustration of the sub-stabilisation process for weakly UC-FASs.

## [138] `ucfas_2025_part3` (PDF p.6, L485)

Theorem 3.1: Restrict
π
|θ(t)| < , t ≥ 0. (24)
2
Then all Models I to V are equivalent to each other.

## [139] `ucfas_2025_part3` (PDF p.9, L893)

Theorem 4.1: The sub-stabilising controller for UC-
FAS (49) is given by (52) and (65). As long as
[ ]
X0 ∈ Rin ,
Z0 mo

the designed controller satisfies

u′1 ≠ g((x, z)(0∼1), t), t ≥ 0,

or equivalently,

u1(t) ≠ 0, t ≥ 0,

and produces a closed-loop system composed of linear
systems (53) and (66), with response converging to zero
within 𝔽inmo.

Once x(0∼1) and z(0∼3) are obtained, y(0∼1) can then
be obtained by (43) and (44). Please note that the
convergence rate of system (66) must be made large
enough so as to let y(0∼1) and u2 converge to zero
exponentially (will be seen clearly in the following
section).

## [140] `book_2026_volume1` (PDF p.63, L42)

Theorem 1.1 Let A ∈ Rn×n , B ∈ Rn×r be two matrices satisfying Assumptions 1.1
and 1.2, and N (s) and D (s) be a pair of right coprime polynomial matrices given
by (1.15) and satisfy RCF (1.14). Then, the solution to Problem 1.1 is generally given
by                     ⎧
⎨ K = W V −1
V = N0 Z + N1 Z F + · · · + Nω Z F ω                   (1.16)
⎩
W = D 0 Z + D1 Z F + · · · + D ω Z F ω ,
where. Z ∈ Rr ×n is an arbitrary parameter matrix satisfying the following constraint:
1.6 Preliminaries                                                                         43
det (N0 Z + N1 Z F + · · · + Nω Z F ω ) = 0.                   (1.17)
The meaning of equation (1.13) is very clear. If F is chosen to be a stable matrix,
then K turns to be a stabilizing gain matrix for the state feedback controller (1.11).
Therefore, Theorem 1.1 has given all the stabilizing state feedback controllers for sys-
tem (1.10). The parameter matrix Z in the above lemma represents the design DOFs
in the design, and can be properly utilized to achieve additional system performance
(Duan et al., 2002; Duan, 1992a, 1993a, 2024a, 2024b, 2025a).
1.6.3 Eigenstructure Assignment
Nondefective ESA—Solution based on RCF
In this subsection, let us consider the important case that the matrix F is in the
diagonal form of
F = diag (si , i = 1, 2, . . . , n) ,             (1.18)
where si , i = 1, 2, . . . , n, are clearly the closed-loop eigenvalues to be assigned.
This subsection treats the case that the closed-loop eigenvalues are allowed to be
undetermined and sought later according to some system requirements.

## [141] `book_2026_volume1` (PDF p.64, L43)

Theorem 1.2 Let A ∈ Rn×n , B ∈ Rn×r be two matrices satisfying Assumptions 1.1
and 1.2, and. N (s) and. D (s) be a pair of right coprime polynomial matrices satisfying
RCF (1.14). Then, for a diagonal matrix F ∈ Cn×n in the form of (1.18), all the
solutions to Problem 1.1 are given by
⎧        −1
⎨ K = WV
⎩ V = N (s1 ) z 1 N (s2 ) z 2 · · · N (sn ) z n
(1.19)
W = D (s1 ) z 1 D (s2 ) z 2 · · · D (sn ) z n ,
where z i ∈ Cr , i = 1, 2, . . . , n, are a group of parameter vectors satisfying the
following constraints:
Constraint 1.1 det N (s1 ) z 1 N (s2 ) z 2 · · · N (sn ) z n = 0,
Constraint 1.2 z i = z̄l , if si = s̄l and Im (si ) = 0, i, l = 1, 2, . . . , n.
The above general complete parametric solution formula given in (1.19) to the
generalized ESA problem for the case of F being a diagonal matrix turns out to be
extremely simple. Yet this case is also the mostly encountered one in applications.
What is more, with the help of similarity transformations, this diagonal case can also
be applied to the case that F is nondefective since a nondefective matrix is similar to
a diagonal matrix. For the same reason, the system resulted in by the above controller
(1.19) is nondefective.
44                                                                             1 Introduction

## [142] `book_2026_volume1` (PDF p.65, L44)

Theorem 1.3 Let A ∈ Rn×n , B ∈ Rn×r be two matrices satisfying Assumptions 1.1
and 1.2, F ∈ Cn×n be a diagonal matrix in the form of (1.18). Further, let N̂i ∈ Rn×r
and D̂i ∈ Rr ×r , i = 1, 2, . . . , n, be given by (1.22)–(1.23). Then all the solutions to

## [143] `book_2026_volume1` (PDF p.84, L64)

Theorem 2.1 System (2.66) is controllable if and only if it can be equivalently
converted into the following linear FAS:
z (n) + αn−1 z (n−1) + · · · + α1 ż + α0 z = u,               (2.71)
with αi , i = 0, 1, . . . , n − 1, given by (2.67).

## [144] `book_2026_volume1` (PDF p.86, L66)

Theorem 2.2 System (2.74) is controllable if and only if it can be equivalently
converted into the following linear multi-order FAS:
2.4 Linear Time-Invariant FASs                                                                    67
−1)
z k(μk )                = L̃ z k(0∼μk                 + B̃u,   (2.81)
k=1∼r                              k=1∼r
where μk , k = 1, 2, . . . , r, are a set of integers satisfying
μ1 + μ2 + · · · + μr = n,
z = [z 1 , z 2 , · · · , zr ]T ∈ Rr is some vector satisfying
x = T z k(0∼μk −1) |k=1∼r ,                (2.82)
for some nonsingular matrix T ∈ Rn×n Furthermore, if system (2.74) is reduced to
the Luenberger controllability canonical form (2.75)–(2.76), then
⎡             μ −1                     μ −1 ⎤
−α110
· · · −α111 · · · −α1r0
· · · −α1rr
⎢ −α 0 · · · −α 1 · · · −α 0 · · · −α μr −1 ⎥
μ  −1
⎢     21         21            2r         2r   ⎥
L̃ = ⎢  ..            ..         ..            ..   ⎥,                 (2.83)
⎣ .               .          . ···         .   ⎦
μ1 −1                    μ −1
−αr01 · · · −αr1       · · · −αrr
· · · −αrrr
⎡                      ⎤
1 b12 b13 · · · b1r
⎢ 1 b23 · · · b2r ⎥
⎢                      ⎥
⎢        1 · · · b3r ⎥
B̃ = ⎢                      ⎥,
⎢             . .   .. ⎥
⎣                 . . ⎦

## [145] `book_2026_volume1` (PDF p.98, L78)

Theorem 2.3 Let the LTV system (2.109) satisfy Assumptions 2.5 and 2.6. Under
the state transformation
(0∼μk −1)
zk           = P (t) x,
k=1∼η
with P (t) given by (2.117), it can be equivalently converted into a FAS in the form
of
(μk )                       −1)
zk          = L (t) z k(0∼μk        + Bz (t) u,           (2.120)
k=1∼η                           k=1∼η
where L (t) ∈ Rr ×n and Bz (t) ∈ Rr×r are two linear matrix functions, with Bz (t)
being nonsingular for all t ≥ t0 .
2.5 Linear Time-Varying FASs                                                                 79
For the proof of Theorem 2.3, please refer to the Appendix in detail.
Non-lexicographically-fixed case
Compared to the lexicography-fixed case, the significant difference is that the
reordered controllability matrix Q̄ (t) given by (2.112) becomes
Q̃ (t) = Q̃ 1 (t) Q̃ 2 (t) · · · Q̃ r (t) ,
Q̃ i (t) = q̃1i q̃2i · · · q̃μi i max , i = 1, 2, . . . , r,   (2.121)
where
q̃ i = bi , i = 1, 2, . . . , r,
q̃ ij+1 = A (t) q̃ ij − q̃˙ ij , j = 1, 2, . . . , μi max − 1,
with μi max , i = 1, 2, . . . , r, given by (2.114). Note that Q̃ (t) is clearly not square,
making the transformation problem more difficult. However, following the idea in
Valášek and Olgaç (1999), Mutoh and Kimura (2011), we could construct an auxiliary
system such that the augmented system is lexicography-fixedly controllable.
Denote
r
n =
e           μi max − n.
i=1

## [146] `book_2026_volume1` (PDF p.100, L80)

Theorem 2.4 Let Assumptions 2.5 and 2.6 be satisfied,.[ Ak ]0∼μk −1 ,.k = 1, 2, . . . , η,
be a series of given matrices, and the state transformation
−1)
z k(0∼μk                 = P (t) x                     (2.126)
k=1∼η
2.5 Linear Time-Varying FASs                                                                81
be defined as in (2.117). Controller (2.124) based on the FAS model (2.120) such
that the eigenvalues of the closed-loop subsystems (2.125) are arbitrarily assigned
and the state response of the original LTV system (2.109) is determined by
x (t) = P −1 (t) exp (    0 t) Z 0 ,            (2.127)
−1)
with Z 0 = z k(0∼μk         |k=1∼η (0) and
0 = diag          [ Ai ]0∼μi −1 , i = 1, 2, . . . , η .

## [147] `book_2026_volume1` (PDF p.105, L85)

Theorem 2.5 Let system (2.132) be feedback linearizable via (2.133). Then system
(2.132) is equivalent to the following global FAS:
−1)                                 −1)
z k(μk )              = fz           z k(0∼μk                   + Bz      z k(0∼μk                 u,   (2.135)
k=1∼η                                        k=1∼η                              k=1∼η
where
−1)                                                        −1)
Bz     z k(0∼μk                          = B̂β −1 T          P −1 z k(0∼μk                     ,    (2.136)
k=1∼η                                                  k=1∼η
μk , k = 1, 2, . . . , η (1 ≤ η ≤ r ) , are a set of distinct integers, z k ∈ Rrk , k =
1, 2, . . . , η, are a set of state vectors, with rk , k = 1, 2, . . . , η, being a set of distinct
integers satisfying (2.91), f z (·) ∈ Rr is a function, and B̂ ∈ Rr ×r is a nonsingular
matrix.

## [148] `book_2026_volume1` (PDF p.107, L87)

Theorem 2.6 If system (2.141) is globally feedback linearizable, then it is equivalent
to a globally nonaffine FAS in the form of
−1)                                     −1)
z k(μk )           = fz       z k(0∼μk                     + gz       z k(0∼μk                 ,u ,   (2.146)
k=1∼η                                   k=1∼η                               k=1∼η
where f z (·) ∈ Rr is a function, and gz (z, u) is one-to-one with respect to u for all
z ∈ R and u ∈ R .
n              r
Again, we mention that essence of the conversion from a feedback linearizable
system to a FAS is finding a homeomorphism under which the system can be trans-
formed into the FAS and vice versa. This actually can be seen from the above proof
of Theorem 2.5, and also the proof of the above Theorem 2.6 given in Duan (2026b).

## [149] `book_2026_volume1` (PDF p.120, L100)

Theorem 3.1 Let A0∼n−1 ∈ Rr×nr be a set of arbitrarily given matrices. Then the
following controller
u = −g −1 x (0∼n−1) , u , t
(3.25)
u = f x (0∼n−1) , t + A0∼n−1 x (0∼n−1) − v,
for system (3.4), with v ∈ Rr being an external signal, produces the linear time-
invariant (LTI) closed-loop system
x (n) + A0∼n−1 x (0∼n−1) = v.               (3.26)
Please note that, for the affine single-order FAS (3.1),
g x (0∼n−1) , u, t = B x (0∼n−1) , t u,
the above controller (3.25) reduces to
u = −B −1 x (0∼n−1) , t A0∼n−1 x (0∼n−1) + u ∗
(3.27)
u ∗ = f x (0∼n−1) , t − v.
It should be noted that the linear system (3.26) is equivalent to the following
state-space form:
(0∼n−1)
ẋ         = (A0∼n−1 ) x (0∼n−1) + Bc v,               (3.28)
where
3.3 Feedback Linearization                                                                      101
T
Bc = 0 · · · 0 Ir       (3.29)
Note that the coefficient matrix A0∼n−1 in (3.26) is at the designer’s choice. The
above result indicates that a controller for a FAS can be easily designed, which results
in an LTI closed-loop system with an arbitrarily desired eigenstructure.
Furthermore, it can be easily observed that, when all Ai , i = 0, 1, . . . , n − 1,
are chosen to be diagonal, r decoupled systems can be immediately obtained. This

## [150] `book_2026_volume1` (PDF p.121, L101)

Theorem 3.2 Let Ak,0∼μk −1 ∈ Rrk ×μk rk , k = 1, 2, . . . , η, be a set of arbitrarily
given matrices. Then the following controller
⎧
−1)
⎪
⎪
⎪ u = −g −1 xk(0∼μk |k=1∼η , u , t
⎪
⎪                                 ⎡                        ⎤
⎪
⎪                                   A1,0∼μ1 −1 x1(0∼μ1
−1)
⎨
⎢A             (0∼μ2 −1) ⎥
⎢ 2,0∼μ2 −1 x2           ⎥                          (3.30)
⎪          (0∼μk −1)              ⎢                        ⎥ − v,
⎪ u = f xk
⎪
⎪
|k=1∼η , t + ⎢           ..           ⎥
⎪
⎪                                 ⎣            .           ⎦
⎪
⎩                                                ( η )
0∼μ  −1
Aη,0∼μη −1 xη
for the nonaffine FAS (3.12), with
T
v = v1T v2T · · · vηT
, vk ∈ Rrk ,                     (3.31)
being an external signal vector, produces the following set of decoupled LTI closed-
loop systems:
x (μk ) + Ak,0∼μk −1 xk(0∼μk −1) = vk , k = 1, 2, . . . , η.
k                                                                        (3.32)
In the case of
−1)                                      −1)
g xk(0∼μk         |k=1∼η , u, t = B xk(0∼μk                |k=1∼η , t u,   (3.33)
the nonaffine FAS (3.12) becomes affine FAS (3.9), and controller (3.30) reduces to

## [151] `book_2026_volume1` (PDF p.122, L102)

Theorem 3.3 Let A E ∈ Rr×κ0 be an arbitrarily given matrix. Then the following
controller
⎧
⎨ u = −g −1 x (0∼μk −1) |k=1∼η , u , t
k
(3.37)
⎩u = f x   (0∼μ k −1)                         −1)
|k=1∼η , t − A E xk(0∼μk |k=1∼η − v,
k
for system (3.12), with v ∈ Rr being an external signal, produces the following
closed-loop system:
3.4 Parametric Solutions of Controller Parameters                                       103
−1)
x (μk ) |k=1∼η = A E xk(0∼μk
k                                         |k=1∼η + v.      (3.38)
When (3.33) holds, the above controller (3.37) reduces to the following one for
the affine FAS (3.9):
⎧
⎨ u = −B −1 x (0∼μk −1) |k=1∼η , t −A E x (0∼μk −1) |k=1∼η + u ∗
k                         k
(3.39)
⎩u = f x
∗        (0∼μ k −1)
|k=1∼η , t − v.
k
3.4 Parametric Solutions of Controller Parameters
In this section, let us further present parametric solutions of the parameters involved
in the feedback linearizing controllers. To save space, here only the multi-order case
is treated.
3.4.1 Decoupled Design
In Sect. 3.3.2, the proposed decoupled controller (3.30) for nonaffine FAS (3.12), or

## [152] `book_2026_volume1` (PDF p.123, L103)

Theorem 3.4 Let k ∈ {1, 2, · · · , η}. Then, for an arbitrary matrix Fk ∈ Rμk rk ×μk rk ,
all the matrices Ak,0∼μk −1 and Vk ∈ Rμk rk ×μk rk , satisfying det Vk 0 and
k   Ak,0∼μk −1 = Vk Fk Vk−1 ,                 (3.40)
are given by
μ
Ak,0∼μk −1 = −Z k Fk k Vk−1 (Z k , Fk ) ,               (3.41)
and                                                       ⎡                 ⎤
Zk
⎢        Z k Fk      ⎥
⎢                    ⎥
Vk = Vk (Z k , Fk ) = ⎢           ..       ⎥,       (3.42)
⎣            .       ⎦
Z k Fkμk −1
with Z k ∈ Rrk ×μk rk being a parameter matrix satisfying
det Vk (Z k , Fk ) = 0.                              (3.43)
The above theorem clearly establishes a general parametric solution of the con-
troller parameters Ak,0∼μk −1 , k = 1, 2, · · · , η, which arbitrarily assign the desired
eigenstructure of the closed-loop system (3.35). Further, let
F = diag F1 , F2 , · · · , Fη ,
V = diag V1 , V2 , · · · , Vη ,
the whole closed-loop system can be obtained as
−1)                                     −1)
ẋ (0∼μk
k              |k=1∼η = V F V −1 xk(0∼μk               |k=1∼η ,             (3.44)
which has a clear arbitrarily assignable eigenstructure. Particularly, the closed-loop
eigenvalues (or poles) are given by the eigenvalues of the matrix F, or equivalently,
given by the eigenvalues of Fk , k = 1, 2, . . . , η. The design degrees of freedom
(DOFs) provided in the whole design are composed of two parts, the first part lies
in the choice of the matrix F, and the second part is given by Z k ∈ Rrk ×μk rk , k =
1, 2, . . . , η, which accounts for
dd
freedom     = μ1r12 + μ2 r22 + · · · + μη rη2 (3.45)

## [153] `book_2026_volume1` (PDF p.154, L135)

Theorem 4.1 For an arbitrarily selected matrix F ∈ Rnr ×nr , all the matrices
A 0∼n−1 and V ∈ R
nr×nr
satisfying detV 0 and
(A0∼n−1 ) = V F V −1                (4.30)
are given by (4.27) and
A0∼n−1 = −Z F n V −1 (Z , F) ,                 (4.31)
with Z ∈ Rr ×nr being a parameter matrix satisfying
detV (Z , F) = 0.               (4.32)

## [154] `book_2026_volume1` (PDF p.154, L135)

Theorem 4.2 Let F ∈ Rnr×nr be a given Hurwitz matrix, and f i ∈ R and Fi ∈
Rnr×nr , i = 0, 1, 2, . . . , nr, are determined by
136                                                            4 Disturbance Attenuation and Decoupling
nr
det (s I + F) =          fi s i ,                    (4.36)
i=0
and
nr−1
adj (s I + F) =
Fi s i ,                    (4.37)
i=0
respectively. If the control law for FAS (4.18) is taken as (4.19), with A0∼n−1 being
given by (4.31), then we have
G dy (s) 2 = trace (C V ) P1 (C V )T
T
= trace       V −1 Bc E         P2 V −1 Bc E         ,   (4.38)
where V is given by (4.27), and
⎧       nr−1
⎪
⎪
⎪
⎪ P = −      Fi V −1 Bc E                    V −1 Bc E
T    −1
P10 FT
i
⎨ 1
i=0
(4.39)
⎪
⎪
nr−1
⎪
⎪ P  = −                          −1 i
FiT (C V )T (C V ) P20 F,
⎩  2
i=0

## [155] `book_2026_volume1` (PDF p.160, L141)

Theorem 4.3 Consider FAS (4.45), with the disturbance d (t) generated by (4.13),
and let Assumptions 4.1 and 4.4 be met. If the control law is taken as (4.60)–
(4.62), with the parameter matrices L x , L d , F1 , Z 1 and Z 2 satisfying the following
conditions:
1. L x and L d are any matrices making
(00∼n−1 )       Bc E       Lx
Ace =                                     +       Cm 0           (4.63)
0            (S0∼k−1 )   Ld
stable;
2. the parameter F1 is Hurwitz, and also satisfies, together with the parameter Z 1 ,
the condition detV (F1 , Z 1 ) = 0; and
3. the parameter Z 2 in the expressions of and given by (4.62) satisfies
⎡                       ⎤
Z2
⎢ Z2               ⎥
(S0∼k−1 )
⎢                  ⎥
Cr ⎢              ..  ⎥ + Er = 0.                   (4.64)
⎣               .  ⎦
Z2 k−1
(S0∼k−1 )
Then the following closed-loop system is internally asymptotically stable:
⎡             ⎤ ⎡                                   ⎤ ⎡ (0∼n−1) ⎤
ẋ (0∼n−1)      (00∼n−1 ) −Bc K 0∼n−1     Ac2        x
⎢ ˙ (0∼n−1) ⎥ ⎣
⎣ x̂          ⎦=  −L x Cm      Ac1      Bc E + Ac2 ⎦ ⎣ x̂ (0∼n−1) ⎦ ,
d̂˙ (0∼k−1)     −L d Cm     L d Cm      (S0∼k−1 )    d̂ (0∼k−1)
(4.65)
where
Ac1 = (00∼n−1 ) + L x Cm − Bc K 0∼n−1 ,
Ac2 = Bc ( + K 0∼n−1 ) .
Furthermore, for any initial values x (0∼n−1) (0) , ζ (0) and d (0∼k−1) (0), the
following asymptotical output regulation requirement is always met:
142                                                      4 Disturbance Attenuation and Decoupling
lim yr (t) = 0.                          (4.66)
t→∞

## [156] `book_2026_volume1` (PDF p.162, L143)

Theorem 4.3 in the case of dynamical state feedback.
Firstly, let us give a necessary and sufficient condition for the observability
(detectability) of the matrix pair ( E , C I ) defined by
(00∼n−1 )    Bc E
E =                           , C I = Inr 0 (4.73)
0         (S0∼k−1 )

## [157] `book_2026_volume1` (PDF p.162, L143)

Theorem 4.4 The matrix pair ( E , C I ) defined by (4.73) is observable (detectable)
if and only if ( (S0∼k−1 ) , E) is observable (detectable).

## [158] `book_2026_volume1` (PDF p.163, L144)

Theorem 4.5 Suppose that E and C I are given by (4.73) and ( (S0∼k−1 ) , E)
is observable. Let N (s) and D (s) be a pair of right coprime polynomial matrices
in the form of (4.78) and satisfy RCF (4.76), and F0 ∈ R (nr +kp)×(nr +kp) be a given
Hurwitz matrix. Then all the gain matrices L x and L d and the nonsingular matrix
T satisfying
T
Lx
E +          CI     = T F0 T −1 ,                  (4.79)
Ld
can be given by
4.3 Asymptotical Disturbance Decoupling                                                            145
⎧
⎪
⎪   Lx
= T −T G T
⎪
⎪
⎪
⎪   L d
⎪
⎪        ω
⎨            Di
T =             Z 0 F0i                                           (4.80)
Ni
⎪
⎪       i=0
⎪
⎪       ω+1
⎪
⎪
⎪
⎩G =
⎪            Di−1 − T (00∼n−1 ) Di Z 0 F0i ,
i=0
where
Dω+1 = D−1 = 0,                              (4.81)
and Z 0 ∈ Rnr ×(nr+kp) is a parameter matrix satisfying
ω
Di
det                               Z 0 F0i   = 0.         (4.82)

## [159] `book_2026_volume1` (PDF p.175, L156)

Theorem 4.5. Again, for simplicity, only a specific pair of solutions is given, as
follows:
⎡                                   ⎤
−12 0 −1 0               0 0
⎢ 0 −13 0 −1 0 0 ⎥
⎢                                   ⎥
⎢ 0       0 −14 0 −1 0 ⎥
L x = ⎢                                   ⎥,               (4.155)
⎢ 0       0   0 −11 0 −1 ⎥
⎢                                   ⎥
⎣ 0       0   0     0 −25 0 ⎦
0     0   0     0      0 −9
0 0 0 0 50 0
Ld =                    (4.156)
0 0 0 0 −510 0
In such a case, the set of eigenvalues of Ace is
eig (Ace ) = {−7, −8, . . . , −14} .
(4.157)
Simulation results
According to Theorem 4.3, the control law is finally designed as
4.4 An Illustrative Example                                                           157
Fig. 4.4 The regulated
angles
⎧
⎪
⎪
⎪ θ̂˙ (0∼2)        (00∼2 ) Bc E 0∼1    θ̂ (0∼2)   Bc
⎪             =                           (0∼1) +    v
⎪
⎪
⎪
⎪ d̂˙ (0∼1)         0       (S0∼1 )    d̂         0
⎪
⎨                       Lx
+      θ̂ (0∼2) − θ (0∼2)                        (4.158)

## [160] `book_2026_volume1` (PDF p.183, L164)

Theorem 5.1 Suppose that system (5.2) satisfies Assumptions 5.1 and 5.2. Let.μ and
ε be two arbitrarily given positive numbers, and Ai ∈ Rr ×r , i = 0, 1, . . . , n − 1, be
a set of matrices satisfying (5.5). Then, the following control law
u = −L −1 (x (0∼n−1) ) A0∼n−1 x (0∼n−1) +u ∗
(5.10)
u ∗ = f (x (0∼n−1) )+ 4ε1 ρ 2 (x (0∼n−1) )PLT ( A0∼n−1 )x (0∼n−1) ,
for the uncertain system (5.2) guarantees that the state x (0∼n−1) converges into the
following ellipsoid centered at the origin:
T                               ε
μ,ε (0) =        x (0∼n−1) x (0∼n−1)           P( A0∼n−1 )x (0∼n−1) ≤          .
μ
For a proof of the above result, please refer to Appendix B.
In the case of n = 1, system (5.2) becomes
ẋ = f (x) +   f (x) + L(x)u,                             (5.11)
and the robust control law turns into
1 2
u = L −1 (x) −Ax − f (x) −
ρ (x)PLT ( A)x (5.12)
4ε
In such a case, the state x of the uncertain control system eventually converges into
the following ellipsoid:
ε
μ,ε (0) =   x x T P( A)x ≤            .
μ
5.1 Robust Control                                                                                       165
5.1.2 Robust Tracking
Let x ∗ (t) ∈ Rr be a reference signal to be tracked by the state x (t), and define

## [161] `book_2026_volume1` (PDF p.184, L165)

Theorem 5.2 Suppose that system (5.2) satisfies Assumptions 5.1 and 5.2. Let.μ and
ε be two arbitrarily given positive numbers, and Ai ∈ Rr ×r , i = 0, 1, . . . , n − 1, be
a set of matrices satisfying (5.5). Then, the following control law
u = −L −1 (x (0∼n−1) ) A0∼n−1 x (0∼n−1) + u ∗
u ∗ = 4ε1 ρ 2 (x (0∼n−1) )PLT ( A0∼n−1 )x (0∼n−1) + f (x (0∼n−1) ) − u 0 (x ∗ ),
with
u (x ∗ ) = (x ∗ )(n) + A0∼n−1 (x ∗ )(0∼n−1)
+ ρ 2 (x (0∼n−1) )PLT ( A0∼n−1 )(x ∗ )(0∼n−1) ,
4ε
guarantees that the state x (0∼n−1) converges globally into the following ellipsoidal
belt-shaped region centered at (x ∗ )(0∼n−1) :
166                                                                         5 Robust and Adaptive Control
T                          ε
μ,ε   (x ∗ )(0∼n−1) = x (0∼n−1)            (x − x ∗ )(0∼n−1)       P(x − x ∗ )(0∼n−1) ≤       .
μ

## [162] `book_2026_volume1` (PDF p.189, L170)

Theorem 5.3 Suppose that Assumption 5.1 holds. Let. Ai ∈ Rr ×r , i = 0, 1, . . . , n −
1, be a set of matrices such that the matrix A0∼n−1 ) is stable, and PL ( A0∼n−1 ) be
given by (5.28)–(5.30). Then, for any unknown constant vector θ ∈ Rm , there exists
an adaptive control law
⎧
⎨ θ̂˙ = H (x (0∼n−1) )PLT ( A0∼n−1 )x (0∼n−1)
⎪
u = −L −1 (x (0∼n−1) ) A0∼n−1 x (0∼n−1) +u ∗                              (5.31)
⎪
⎩ u ∗ = H T (x (0∼n−1) )θ̂ + q(x (0∼n−1) ),
for system (5.27) such that the states of the closed-loop system satisfy
1. x (0∼n−1) → 0, t → ∞;
2. θ − θ̂ is bounded.
For a proof of the above result, please refer to Appendix B.
5.2.2 Adaptive Tracking
Let x ∗ (t) ∈ Rr be a reference signal to be tracked by x (t), and let
z = x − x ∗.
Then
(i)
z (i) = x (i) − x ∗         , i = 0, 1, . . . , n,                (5.32)
and H x (0∼n−1) , q x (0∼n−1) and L x (0∼n−1) can be transformed into functions
with respect to z (0∼n−1) and t, that is,
⎧
⎨ H x (0∼n−1) = H z (0∼n−1) , t
q x (0∼n−1) = q z (0∼n−1) , t                                 (5.33)
⎩
L x (0∼n−1) = L z (0∼n−1) , t .
5.2 Adaptive Control                                                                            171
Thus system (5.27) turns into
(n)
z (n) = H T z (0∼n−1) , t θ + q z (0∼n−1) , t + L z (0∼n−1) , t u − x ∗              (5.34)
Applying Theorem 5.3 to the above system, we can obtain the following adaptive

## [163] `book_2026_volume1` (PDF p.190, L171)

Theorem 5.4 Suppose that system (5.27) satisfies Assumption 5.1. Let Ai ∈
Rr ×r , i = 0, 1, . . . , n − 1, be a set of matrices such that A0∼n−1 ) is stable, and
PL (A 0∼n−1 ) be given by (5.28)–(5.30). Then, the following control law
⎧˙
⎪
⎪ θ̂ = H (x (0∼n−1) )PLT ( A0∼n−1 ) x (0∼n−1) − (x ∗ )(0∼n−1)
⎨
u = −L −1 x (0∼n−1) A0∼n−1 x (0∼n−1) +u ∗
⎪   ∗      T (0∼n−1)            (0∼n−1)
) + u 0 (x ∗ )
⎩ u =∗ H (x ∗ (n) )θ̂ + q(x
⎪
∗ (0∼n−1)
u 0 (x ) = −(x ) − A0∼n−1 (x )               ,
when applied to system (5.27), guarantees the following:
1. x (0∼n−1) − (x ∗ ) (0∼n−1) → 0, t → ∞;
2. θ − θ̂ is bounded.

## [164] `book_2026_volume1` (PDF p.199, L180)

Theorem 5.5 Suppose that FAS (5.49), together with the pre-estimation θ0 of
the unknown parameter vector θ, satisfies Assumptions 5.1, 5.2 and 5.3. Let μ
and ε be two arbitrarily selected non-negative real numbers, and Ai ∈ Rr ×r , i =
0, 1, . . . , n − 1, be a set of matrices satisfying (5.51). Then, control law (5.53)–(5.56)
for system (5.49) guarantees that the state x (0∼n−1) of the closed-loop system and
the parameter estimation error θ̃ converge to the following ellipsoid:
x (0∼n−1)                        2         2        ε+δ
(μ,ε,δ) (0) =                             x (0∼n−1) P + θ̃             ≤2       ,
θ̃                                                μ
where
1 2
δ=      δ + (μ + 1) δ02 (5.57)
2 1
For a proof of the above result, please refer to Appendix B.
In the case of n = 1, system (5.49) turns into
ẋ = f (x) +          f (x) + H T (x)θ + L(x)u,                         (5.58)
and the corresponding robust adaptive control law is turned into
⎧
⎨ θ̂˙ = H (x)P T ( A)x − (μ + 1) θ̂ − θ0 + θ̇0
L
(5.59)
⎩ u = L −1 (x) −Ax − f (x) − 1 ρ 2 (x)P T ( A)x − H T (x)θ̂ .
4ε        L
In such a case the state x and the parameter estimation error θ̃ eventually converge
into the following ellipsoid:
x                                    ε+δ
(μ,ε,δ) (0) =                 x T P( A)x + θ̃ T θ̃ ≤ 2                .
θ̃                                    μ
5.3.2 Robust Adaptive Tracking
Let x ∗ (t) ∈ Rr be a sufficiently smooth reference signal to be tracked by x (t), and
put
∗
x̃ = x − x ,

## [165] `book_2026_volume1` (PDF p.201, L182)

Theorem 5.6 Suppose that FAS (5.49), together with a pre-estimation θ0 of the
unknown parameter vector θ, satisfies Assumptions 5.1–5.3. Let μ and ε be two
arbitrarily selected positive real numbers, and Ai ∈ Rr ×r , i = 0, 1, . . . , n − 1, be
a set of matrices satisfying (5.51). Then, control law (5.67)–(5.69) for the uncer-
tain system (5.49) guarantees that the tracking error x̃ = x − x ∗ and the parameter
estimation error θ̃ converge to the following ellipsoid:
x̃ (0∼n−1)
(μ,ε,δ)
θ̃
x̃ (0∼n−1)                  2          2         ε+δ
=                       x̃ (0∼n−1) P + θ̃         2            .
θ̃                                           μ
To end this section, we further present some related remarks.

## [166] `book_2026_volume1` (PDF p.203, L184)

Theorem 5.7 Suppose that FAS (5.49) satisfies Assumptions 5.1 and 5.4, and the
parameter vector.θ is constant. Let.μ and.ε be two selected positive real numbers, with
ε ≤ 1, and Ai ∈ R    , i = 0, 1, . . . , n − 1, be a set of matrices satisfying (5.51).
r×r
Then, the control law given by (5.53)–(5.54) and (5.74)–(5.75), for system (5.49),
guarantees
• limt→∞ x (0∼n−1) = 0;
• θ̃ is bounded.
For a proof of the above result, please refer to Appendix B.
In the case that the state x (t) is required to track a given signal x ∗ (t), the robust
adaptive tracking control law for the system turns into
u = −L −1 (x (0∼n−1) ) u 0 + u r + u a ,
(5.76)
where          ⎧
⎪
⎪                        ∗ (0∼n−1)
+ f (x (0∼n−1) ) − (x ∗ )(n)
⎨ u 0 = A0∼n−1 (x − x )
⎪ u r = 1ε ρ(x (0∼n−1) )PLT ( A0∼n−1 )(x − x ∗ )(0∼n−1)                (5.77)
⎪
⎩
u a = H T (x (0∼n−1) )θ̂,
and θ̂ is given by the adaptation law
θ̂˙ = H (x (0∼n−1) )PLT ( A0∼n−1 ) x − x ∗
(0∼n−1)
.              (5.78)
When this robust adaptive control law is applied to FAS (5.49), .||θ̃|| is guaranteed
to be bounded, and
(0∼n−1)
lim   x − x∗           = 0.                        (5.79)
t→∞
Therefore, asymptotical tracking of the system state vector to the reference signal
can be realized in such a case. In the particular case of f (x (0∼n−1) ) = 0, this result
reduces to the one given in Duan (2021d).

## [167] `book_2026_volume1` (PDF p.218, L200)

Theorem 6.1 Let Assumption 6.1 be satisfied, then, under the following transfor-
mation       ⎧
⎪
⎪ x1 = z
⎨
x2 = G −1
1 (z, ζ, t)[ż − f 1 (z, ζ, t)]                         (6.3)
L −1
(0∼k−1)
⎪
⎪ x k+1 =   k (z         , ζ, t)[z (k) − h k (z (0∼k−1) , ζ, t)],
⎩
k = 2, 3, . . . , n − 1,
the generalized SFS (6.1) can be transformed into the following FAS:
z (n) = h n (z (0∼n−1) , ζ, t) + L n (z (0∼n−1) , ζ, t)u,              (6.4)
6.2 First-Order SFSs                                                                           201
where the matrix function L k (z (0∼k−1) , ζ, t) and the vector function h k (z (0∼k−1) , ζ, t)
are recursively given by
L k (z (0∼k−1) , ζ, t) = L k−1 (z (0∼k−2) , ζ, t)G k (x1∼k , ζ, t),   (6.5)
and
h (z (0∼k−1) , ζ, t) = ḣ k−1 (z (0∼k−2) , ζ, t) + L̇ k−1 (z (0∼k−2) , ζ, t)xk
k
+L k−1 (z (0∼k−2) , ζ, t) f k (x1∼k , ζ, t),              (6.6)
k = 1, 2, . . . , n,
with the initial values
L 0 (ζ, t) = Ir , h 0 (ζ, t) = 0,                  (6.7)
where in (6.5)–(6.6) xi , i = 2, 3, . . . , n, and their derivatives are all given or
determined by transformation (6.3).
For a proof of the theorem, please refer to Appendix B. Please note that the above
iteration (6.5)–(6.7) gives
h (x1 , ζ, t) = f 1 (x1 , ζ, t) , L 1 (x1 , ζ, t) = G 1 (x1 , ζ, t) .

## [168] `book_2026_volume1` (PDF p.221, L203)

Theorem 6.2 Let Condition 6.1 be satisfied, then, under the following transforma-
tion               ⎧
⎪
⎪ x1 = z
⎨
x2 = G −1
1 [ż − f 1 (z, ζ, t)]                          (6.11)
L −1
(k)
⎪
⎪ x   =    k [z     − h k (z (0∼k−1) , ζ, t)],
⎩ k+1
k = 2, 3, . . . , n − 1,
the generalized SFS (6.1) can be equivalently transformed into the following FAS:
z (n) = h n (z (0∼n−1) , ζ, t) + L n (z (0∼n−1) , ζ, t)u,     (6.12)
with
L k = G 1 G 2 · · · G k , k = 1, 2, . . . , n − 1
(6.13)
L n (z (0∼n−1) , ζ, t) = L n−1 G n (x1∼n , ζ, t),
and                                                     ⎡                    ⎤
f 1(n−1) (z, ζ, t)
⎢ f (n−2) (z, x2 , ζ, t) ⎥
⎢ 2                        ⎥
(0∼n−1)                   ⎢             ..           ⎥
h n (z         , ζ, t) = L 0∼n−1 ⎢                          ⎥,      (6.14)
⎢              .           ⎥
⎣ f˙ (x            , ζ, t) ⎦
n−1   1∼n−1
f n (x1∼n , ζ, t)
where L 0 = Ir , and in (6.13)–(6.14) the xk , k = 2, 3, . . . , n, and their derivatives
are all given or determined by transformation (6.11).

## [169] `book_2026_volume1` (PDF p.223, L205)

Theorem 6.3 Let Assumption 6.2 be met, then, under the following transformation
⎧
⎪
⎪ x1 = z
⎨
x2 = G −1
1 (z
(0∼1)
, ζ, t)[z̈ − f 1 (z (0∼1) , ζ, t)]
−1 (0∼2k−1)                                                        (6.19)
⎪
⎪ x   = L k (z            , ζ, t)[z (2k) − h k (z (0∼2k−1) , ζ, t)],
⎩ k+1
k = 2, 3, . . . , n − 1,
SFS (6.18) can be equivalently converted into the following FAS:
z (2n) = h n (z (0∼2n−1) , ζ, t) + L n (z (0∼2n−1) , ζ, t)u,           (6.20)
where the functions L k (z (0∼2k−1) , ζ, t) and h k (z (0∼2k−1) , ζ, t) are given recursively
by
(0∼1)
L k (z (0∼2k−1) , ζ, t) = L k−1 (z (0∼2k−3) , ζ, t)G k (x1∼k
, ζ, t),           (6.21)
(0∼2k−1)                     (0∼2k−3)                      (0∼2k−3)
h k (z          , ζ, t) = ḧ k−1 (z          , ζ, t) + L̈ k−1 (z            , ζ, t)xk
(0∼2k−3)
+2 L̇ k−1 (z            , ζ, t)ẋk
(0∼1)
+L k−1 (z (0∼2k−3) , ζ, t) f k (x1∼k   , ζ, t),    (6.22)
k = 1, 2, . . . , n,
with the initial values
L 0 (ζ, t) = Ir , h 0 (ζ, t) = 0,                    (6.23)
206                                            6 Strict Feedback Systems with Uniform Dimensions
where in (6.21)–(6.22) the xi , i = 2, 3, . . . , n, and their derivatives are given or
determined by transformation (6.19).
For a proof of the theorem, please refer to Appendix B.
It is noted that facts similar to those mentioned in Remarks 6.2 and 6.3 also hold
true in this second-order case.
SFS (6.18) clearly has the following companion form:
⎧
⎪

## [170] `book_2026_volume1` (PDF p.224, L206)

Theorem 6.4 Let Condition 6.2 be met, then, under the following transformation
⎧
⎪
⎪ x1 = z
⎨
x2 = G −1
1 [z̈ − f 1 (z
(0∼1)
, ζ, t)]
−1 (2k)              (0∼2k−1)                     (6.26)
⎪
⎪ x     = L    [z     −   h   (z          , ζ, t)],
⎩   k+1     k               k
k = 2, 3, . . . , n − 1,
SFS (6.18) can be equivalently transformed into the following FAS:
z (2n) = h n (z (0∼2n−1) , ζ, t) + L n (z (0∼2n−1) , ζ, t)u,       (6.27)
6.4 Mixed-Order SFSs                                                                            207
with
L k = G 1 G 2 · · · G k , k = 1, 2, . . . , n − 1
(0∼1)                        (6.28)
L n (z (0∼2n−1) , ζ, t) = L n−1 G n (x1∼n     , ζ, t),
and                                                       ⎡                     ⎤
f 1(2(n−1)) (z (0∼1) , ζ, t)
⎢ (2(n−2)) (0∼1)               ⎥
⎢ f2          (x1∼2 , ζ, t) ⎥
⎢               ..             ⎥
h n (z
(0∼2n−1)
, ζ, t) = L 0∼n−1 ⎢
⎢                .
⎥,
⎥             (6.29)
⎢ ¨           (0∼1)            ⎥
⎣ f n−1 (x1∼n−1 , ζ, t) ⎦
(0∼1)
f n (x1∼n   , ζ, t)
where L 0 = Ir , and in (6.28)–(6.29) the xk , k = 2, 3, . . . , n, and their derivatives
are given or determined by transformation (6.26).

## [171] `book_2026_volume1` (PDF p.226, L208)

Theorem 6.5 Let Assumption 6.3 hold, then, under the following transformation
⎧
⎪
⎪ x1 = z
⎨
x2 = G −1
1 (z
(0∼m 1 −1)
, ζ, t)[z (m 1 ) − f 1 (z (0∼m 1 −1) , ζ, t)]
−1 (0∼ pi −1)                                                     (6.35)
⎪ xi+1 = L i (z
⎪                          , ζ, t)[z ( pi ) − h i (z (0∼ pi −1) , ζ, t)],
⎩
i = 2, 3, . . . , n − 1,
SFS (6.33) can be equivalently turned into the following FAS:
z ( p) = h n (z (0∼ p−1) , ζ, t) + L n (z (0∼ p−1) , ζ, t)u,        (6.36)
6.4 Mixed-Order SFSs                                                                            209
where the functions L k (z (0∼ pk −1) , ζ, t) and h k (z (0∼ pk −1) , ζ, t) are recursively given
by
L k (z (0∼ pk −1) , ζ, t)
= L k−1 (z (0∼ pk−1 −1) , ζ, t)G k (xi(0∼m i −1) |i=1∼k , ζ, t),        (6.37)
(0∼ pk −1)
h k (z          , ζ, t)
(m k ) (0∼ pk−1 −1)
= h k−1   (z            , ζ, t)
m k −1
(m − j)                           ( j)
+            C( j, m k )L k−1k        (z (0∼ pk−1 −1) , ζ, t)xk
j=0
+L k−1 (z (0∼ pk−1 −1) , ζ, t) f k (xi(0∼m i −1) |i=1∼k , ζ, t),     (6.38)
k = 1, 2, . . . , n,
with the initial values
L 0 (ζ, t) = Ir , h 0 (ζ, t) = 0,                  (6.39)
where in (6.37)–(6.38) the xk , k = 2, 3, . . . , n, and their derivatives are given or
determined by transformation (6.35).
For a proof of the above result, please refer to Appendix B.

## [172] `book_2026_volume1` (PDF p.228, L210)

Theorem 6.6 Let Condition 6.3 be met, then, under the following transformation
⎧
⎪ x1 = z
⎪
⎨
x2 = G −1
1 [z
(m 1 )
− f 1 (z (0∼m 1 −1) , ζ, t)]
−1 ( pk )                                                  (6.45)
⎪ xk+1 = L k [z
⎪                     − h k (z (0∼ pk −1) , ζ, t)],
⎩
k = 2, 3, . . . , n − 1,
SFS (6.33) can be equivalently turned into the following FAS:
z ( p) = h n (z (0∼ p−1) , ζ, t) + L n (z (0∼ p−1) , ζ, t)u,             (6.46)
with
L k = G 1 G 2 · · · G k , k = 1, 2, . . . , n − 1
(6.47)
L n (z (0∼ p−1) , ζ, t) = L n−1 G n (xi(0∼m i ) |i=1∼n−1 , xn(0∼m n −1) , ζ, t),
6.4 Mixed-Order SFSs                                                                                  211
and
⎡       (p )
⎤
f 1 2∼n (z (0∼m 1 −1) , ζ, t)
⎢ ( p3∼n ) (0∼m 1 −1) (0∼m 2 −1)               ⎥
⎢ f2      (x1             , x2         , ζ, t) ⎥
⎢                      ..                      ⎥
h n (z
(0∼ pn −1)
, ζ, t) = L 0∼n−1 ⎢
⎢                       .
⎥,
⎥         (6.48)
⎢    (m n ) (0∼m i −1)                         ⎥
⎣ f n−1     (xi            |i=1∼n−1 , ζ, t) ⎦
f n (xi(0∼m i −1) |i=1∼n , ζ, t)

## [173] `book_2026_volume1` (PDF p.238, L220)

Theorem 6.7 Let Condition 6.3 be met, then there exists an invertible transformation
x
1∼n   = T (z (0∼ p−1) , ζ, t),                           (6.84)
such that the mixed-order SFS (6.33), with f k , k = 1, 2, . . . , n, given by (6.83), can
be equivalently transformed into the following FAS:
ω
z ( p) =         h l (z (0∼ p−1) , ζ, t) + L(z (0∼ p−1) , ζ, t)u,           (6.85)
l=1
with
L(z (0∼ p−1) , ζ, t) = G 1 G 2 · · · G n−1 G n (xi(0∼m i −1) |i=1∼n , ζ, t),               (6.86)
and
⎡   (p )
⎤
f 1l 2∼n (z (0∼m 1 −1) , ζ, t)
⎢ ( p3∼n ) (0∼m 1 −1) (0∼m 2 −1)                 ⎥
⎢ f 2l       (x1            , x2         , ζ, t) ⎥
⎢                        ..                      ⎥
h l (z
(0∼ p−1)
, ζ, t) = L 0∼n−1 ⎢
⎢                         .
⎥,
⎥             (6.87)
⎢      (m n )    (0∼m i −1)                      ⎥
⎣ f n−1,l (xi                |i=1∼n−1 , ζ, t) ⎦
(0∼m i −1)
f n,l (xi            |i=1∼n , ζ, t)
where L 0 = I, and
L k = G 1 G 2 · · · G k , k = 1, 2, . . . , n − 1,                  (6.88)
and in (6.86)–(6.87) the xk , k = 2, 3, . . . , n, and their derivatives are given by
transformation (6.84).
6.6 Additional Principle                                                                         221

## [174] `book_2026_volume1` (PDF p.247, L229)

Theorem 7.1 Let Assumption 7.1 be satisfied, then under the transformation
(i− p)                           (0∼i−1− p)
x = Ḡ −1
i1   1∼i−1 x p2                             − L i−1 x p2                           ,    (7.8)
p=1∼i−1                                p=1∼i−1
i = 2, 3, . . . , n
SFS (7.7) can be equivalently transformed into the following HOFAS model:
(n+1− p)                         (0∼n− p)
x
p2                      = L n x p2                     + Ḡ 1∼n u 1 ,          (7.9)
p=1∼n                            p=1∼n
where L i (·) and Ḡ 1∼i are given iteratively by
(0∼i+1− p)                            L̇ i + Ḡ 1∼i f i+1,1 (x2∼i+1,1 , x1∼i+1,2 )
L i+1 x p2                               =                                                 ,   (7.10)
p=1∼i+1                       f i+1,2 (x2∼i+1,1 , x1∼i+1,2 )
Ḡ 1∼i 0
Ḡ 1∼i+1 =                         Q i−1 Ḡ i+1 ,                 (7.11)
0 Iri+1 −ri
i = 1, 2, . . . , n − 1.
with L 1 (·) = f 1 (x12 ) and Ḡ 1∼1 = Ḡ 1 .

## [175] `book_2026_volume1` (PDF p.253, L235)

Theorem 7.2 Let Assumption 7.2 be satisfied, then under the following transforma-
tion
(i− p)                             (0∼i−1− p)
x̄ = Ḡ −1
i1    1∼i−1 x̄ p2                             − L i−1 x̄ p2                              ,     (7.34)
p=1∼i−1                                  p=1∼i−1
i = 2, 3, . . . , n
SFS (7.33) can be equivalently transformed into the following HOFAS model:
(0∼n+1− p)                               (0∼n− p)                                (0∼n− p)
x̄
p2                               = L n x̄ p2                        + Ḡ 1∼n x̄ p2                       ū 1 , (7.35)
p=1∼n                           p=1∼n                                   p=1∼n
where L i (·) and Ḡ 1∼i (·) are given iteratively by
(0∼i+1− p)
L i+1 x̄ p2
p=1∼i+1
L̇ i (·) + Ḡ˙ 1∼i (·) x̄i+1,1 + Ḡ 1∼i (·) f¯i+1,1 (·)
=                                                                  ,                           (7.36)
f¯i+1,2 (·)
(0∼i+1− p)
Ḡ 1∼i+1 x̄ p2
p=1∼i+1
236                                         7 Strict Feedback Systems with Increasing Dimensions
Ḡ 1∼i (·) 0
=                           Q̄ i−1 (·) Ḡ i+1 (·) , i = 1, 2, . . . , n − 1,
0     Iri+1 −ri
with L 1 = f¯1 (x̄12 ) and Ḡ 1∼1 = Ḡ 1 (x̄12 ).
For a proof of the above theorem, please refer to Appendix B.
7.2 Second-Order SFSs with Increasing Dimensions
In Duan (2021b), the author proposes more generalized second-order and high-order

## [176] `book_2026_volume1` (PDF p.255, L237)

Theorem 7.3 Let Assumption 7.1 be satisfied, then under the following transforma-
tion
(2i−2 p)                          (0∼2i−1−2 p)
x = Ḡ −1
i1   1∼i−1 x p2                                 − L i−1 x p2                           , (7.39)
p=1∼i−1                               p=1∼i−1
i = 2, 3, . . . , n,
SFS (7.38) can be equivalently transformed into the following HOFAS model:
(2n+2−2 p)                      (0∼2n+1−2 p)
x
p2                      = L n x p2                         + Ḡ 1∼n u 1 ,     (7.40)
p=1∼n                             p=1∼n
where L i (·) and G 1∼i are given iteratively by
L̈ i (·) + Ḡ 1∼i f i+1,1 (·)
L i+1 (·) =                                     ,                               (7.41)
f i+1,2 (·)
238                                              7 Strict Feedback Systems with Increasing Dimensions
Ḡ 1∼i 0
Ḡ 1∼i+1 =                       Q i−1 Ḡ i+1 , i = 1, 2, . . . , n − 1,   (7.42)
0 Iri+1 −ri
(0∼1)
with L 1 = f 1 x12    and Ḡ 1∼1 = Ḡ 1 .
For a proof of the above theorem, please refer to the Appendix B.
7.2.2 Case of State-Dependent Gains
Next, similar to the first-order SFSs, the more general case where G i , i =
1, 2, . . . , n, are assumed to be matrix functions can be also considered. In particular,
the following second-order SFS is discussed:
⎧
⎪
⎪
⎪ ẍ1 = f 1 x1(0∼1) + G 1 x1(0∼1) x2

## [177] `book_2026_volume1` (PDF p.259, L241)

Theorem 7.4 Let Assumption 7.3 be satisfied, then under the following transforma-
tion
(2i−2 p)                             (0∼2i−1−2 p)
x̄ = Ḡ −1
i1    1∼i−1 x̄ p2                           − L i−1 x̄ p2                               , (7.51)
p=1∼i−1                                   p=1∼i−1
242                                                7 Strict Feedback Systems with Increasing Dimensions
i = 2, 3, . . . , n,
SFS (7.48) can be equivalently transformed into the following HOFAS model:
(2i+2−2 p)                     (0∼2n+1−2 p)
x̄
p2                      = L n x̄ p2
p=1∼i                             p=1∼n
(0∼2n+1−2 p)
+Ḡ 1∼n x̄ p2                            ū 1 ,   (7.52)
p=1∼n
where L i (·) and Ḡ 1∼i (·) are given iteratively by
L i+1 (·)
L̈ i (·) + Ḡ¨ 1∼i (·) x̄i+1,1 + 2Ḡ˙ 1∼i (·) x̄˙i+1,1 + Ḡ 1∼i (·) f¯i+1,1 (·)
=                                                                                     ,       (7.53)
f¯i+1,2 (·)
Ḡ 1∼i+1 (·)
Ḡ 1∼i (·) 0
=                                 Q̄ i−1 (·) Ḡ i+1 (·) , i = 1, 2, . . . , n − 1,            (7.54)
0     Iri+1 −ri
with L 1 = f¯1 x̄12
(0∼1)                          (0∼1)
and Ḡ 1∼1 (·) = Ḡ 1 x̄12    .
The above theorem can be similarly proven.
7.3 High-Order Case with Increasing Dimensions

## [178] `book_2026_volume1` (PDF p.262, L244)

Theorem 7.5 Let Assumption 7.1 be satisfied, then under the following transforma-
tion
(q          )                            (0∼q p∼i−1 −1)
x = Ḡ −1
i1    1∼i−1 x p2
p∼i−1
− L i−1 x p2                              , (7.57)
p=1∼i−1                                   p=1∼i−1
i = 2, 3, . . . , n,
SFS (7.56) can be equivalently transformed into the following HOFAS model:
(q p∼n )                            (0∼q p∼n −1)
x
p2                          = L n x p2                             + Ḡ 1∼n u 1 ,      (7.58)
p=1∼n                                  p=1∼n
where L i (·) and Ḡ 1∼i are given iteratively by
(m       )
L i i+1 (·) + Ḡ 1∼i f i+1,1 (·)
L i+1 (·) =                                               ,                                       (7.59)
f i+1,2 (·)
Ḡ 1∼i 0
Ḡ 1∼i+1 =                                  Q i−1 Ḡ i+1 , i = 1, 2, . . . , n − 1,           (7.60)
0 Iri+1 −ri
7.3 High-Order Case with Increasing Dimensions                                                    245
(0∼m 1 −1)
with L 1 = f 1 x12         and Ḡ 1∼1 = Ḡ 1 .
For a proof of the above theorem, please refer to Appendix B.
7.3.2 Case of State-Dependent Gains
Similar to the first-order and second-order SFSs, we can also consider the following
more general high-order SFS with G i , i = 1, 2, . . . , n, being matrix functions:
⎧
⎪
⎪
⎪ x1(m 1 ) = f 1 x1(0∼m 1 −1) + G 1 x1(0∼m 1 −1) x2

## [179] `book_2026_volume1` (PDF p.266, L248)

Theorem 7.6 Let Assumption 7.4 be satisfied, then under the transformation
(q        )                                (0∼q p∼i−1 −1)
x̄ = Ḡ −1
i1    1∼i−1 x̄ p2
p∼i−1
− L i−1 x̄ p2                                 , (7.69)
p=1∼i−1                                   p=1∼i−1
i = 2, 3, . . . , n,
SFS (7.66) can be equivalently transformed into the following HOFAS model:
(q p∼n )
x̄
p2                        = L n (·) + Ḡ 1∼n (·) u 1 ,                          (7.70)
p=1∼n
where L i (·) and Ḡ 1∼i (·) are given iteratively by
L i+1 (·)
⎡                   m i+1
⎤
(m i+1 )                            (k)        (m i+1 −k)
⎣ iL          (·) +       C k
(·) Ḡ     (·) x̄            + Ḡ 1∼i (·) f i+1,1 (·) ⎦
=                          k=1
m i+1        1∼i        i1
,     (7.71)
f i+1,2 (·)
Ḡ 1∼i+1 (·)
Ḡ 1∼i (·) 0
=                                   Q i−1 (·) Ḡ i+1 (·) , i = 1, 2, . . . , n − 1,                              (7.72)
0     Iri+1 −ri
with L 1 = f¯1 x̄12
(0∼m 1 −1)
and Ḡ 1∼1 = Ḡ 1 x̄1(0∼m 1 −1) .
Again, this theorem can be similarly proven.

## [180] `book_2026_volume1` (PDF p.280, L262)

Theorem 8.1 Let Assumption 8.1 be satisfied, then, under the following transfor-
mation:
⎧
⎪
⎪ x1 = z
⎨
x2 = g1−1 (z, y1 , ζ, t), y1 = ż − f 1 (z, ζ, t)
−1 (0∼k−1)
⎪ xk+1 = lk (z
⎪                        , yk , ζ (0∼k−2) , t), yk = z (k) − h k (z (0∼k−1) , ζ (0∼k−1) , t),
⎩
k = 2, 3, . . . , n − 1,
(8.7)
the generalized strict-feedback nonlinear system (8.1) can be transformed into the
following FAS:
z (n) = h n (z (0∼n−1) , ζ (0∼n−1) , t) + ln (z (0∼n−1) , u, ζ (0∼n−2) , t),                             (8.8)
where the vector functions h n (z (0∼n−1) , ζ (0∼n−1) , t) and ln (z (0∼n−1) , u, ζ (0∼n−2) , t)
are recursively given by
⎧
⎪ h 2 (z
⎪        (0∼1)
, ζ (0∼1) , t) = ḣ 1 (z, ζ, t)+ ∂l 1 (z,x     ∂z
2 ,ζ,t)
ż + ∂l 1 (z,x
∂ζ
2 ,ζ,t)
ζ̇
⎪
⎪                                     ∂l 1 (z,x2 ,ζ,t)        ∂l 1 (z,x2 ,ζ,t)
⎪
⎪                                 +                      +                     f   (x        , ζ,   t)
⎪
⎪                                            ∂t                      ∂ x2        2 1∼2
⎪
⎪ h   (z (0∼k−1)
, ζ (0∼k−1)
, t)  =   ḣ       (z  (0∼k−2)
, ζ  (0∼k−2)
, t)
⎨ k                                         k−1
(0∼k−2)
,xk ,ζ (0∼k−3) ,t) (0∼k−2)
+ ∂l k−1 (z ∂z (0∼k−2)                    ż

## [181] `book_2026_volume1` (PDF p.288, L270)

Theorem 8.2 Let Assumption 8.3 be satisfied, then, under the following transfor-
mations
⎧
⎪
⎪ x1 = z
⎨
x2 = g1−1 (z (0∼1) , y1 , ζ, t), y1 = z̈ − f 1 (z (0∼1) , ζ, t)
⎪ xk+1 = lk−1 (z (0∼2k−1) , yk , ζ (0∼2k−4) , t), yk = z (2k) − h k (z (0∼2k−1) , ζ (0∼2k−2) , t),
⎪
⎩
k = 2, 3, . . . , n − 1,
(8.35)
and             ⎧
⎨ ẋ1 = ż −1 (0∼1)
⎪
dg (z      ,y ,ζ,t)
ẋ2 = 1 dt 1                                                              (8.36)
⎪
⎩               −1 (0∼2k−1)
dl (z         ,yk ,ζ (0∼2k−4) ,t)
ẋk+1 = k                dt
, k = 2, 3, . . . , n − 1,
the generalized nonaffine strict-feedback nonlinear system (8.29) can be transformed
into the following FAS:
8.2 Second-Order Nonaffine SFSs                                                                                271
z (2n) = h n (z (0∼2n−1) , ζ (0∼2n−2) , t) + ln (z (0∼2n−1) , u, ζ (0∼2n−4) , t),                 (8.37)
where the vector functions h n (z (0∼2n−1) , ζ (0∼2n−2) , t) and ln (z (0∼2n−1) , u, ζ (0∼2n−4) , t)
are recursively given by
h k (z (0∼2k−1) , ζ (0∼2k−2) , t)
= f˙˜ (z (0∼2k−2) , ζ (0∼2k−3) , t) + g̃˙
k−1                              k−1 (z
(0∼2k−2)
, ζ (0∼2k−4) , t)ẋk
(0∼1)
+g̃ k−1 (z (0∼2k−2) , ζ (0∼2k−4) , t) f k (x1∼k    , ζ, t),                               (8.38)
l k (z (0∼2k−1) , xk+1 , ζ (0∼2k−4) , t)
(0∼1)
= g̃k−1 (z (0∼2k−2) , ζ (0∼2k−4) , t)g k (x1∼k    , xk+1 , ζ, t),                           (8.39)

## [182] `book_2026_volume1` (PDF p.299, L281)

Theorem 8.3 Let Assumption 8.5 hold, then, under the transformations
⎧
⎪
⎪ x1 = z,
⎨
x2 = l1−1 (z (0∼m 1 −1) , y1 , ζ, t), y1 = z (m 1 ) − h 1 (z (0∼m 1 −1) , ζ, t),
(8.76)
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
(8.77)
⎩ k+1
i = 1, 2, . . . , m k+1 − 1, k = 1, 2, . . . , n − 1,
the generalized SFS (8.69) can be equivalently turned into the following FAS:
z ( p) = h n (z (0∼ p−1) , ζ, t) + l n (z (0∼ p−1) , u, ζ, t),          (8.78)
282                                                                    8 Nonaffine Strict Feedback Systems
where the vector functions h n (z (0∼ p−1) , ζ, t) and l n (z (0∼ p−1) , u, ζ, t) are recursively
given by
m k −2
(0∼ pk −1)              (m k −1) (0∼ pk−1 )
h (z
k                   , ζ, t) = Fk−1     (z          , xk , ζ, t) +              C( j, m k − 1)
j=0
(m k −1− j)
∂l k−1 (z (0∼ pk−1 −1) , xk , ζ, t)                   ( j+1)
×                                                        xk
∂ xk
(0∼ pk−1 −1)
∂l k−1 (z              , xk , ζ, t)
+
∂ xk

## [183] `book_2026_volume1` (PDF p.331, L314)

Theorem 9.1 Suppose that Assumption 9.1 holds. Let μ and ε be two arbitrarily
given positive numbers, and Ai0∼1 , Pi ( Ai(0∼1) ) and Pi L ( Ai(0∼1) ), i = 1, 2, . . . , n − 1,
be three sets of matrices as described above. Assume that there exist a set of non-
(0∼1)
negative continuous scalar functions ρi (x1∼i          ), i = 1, 2, . . . , n, satisfying (9.48).
Then, controller (9.49) for the uncertain second-order SFS (9.1) guarantees that the
(0∼1)
transformed state z 1∼n   converges into the following ellipsoid:
n
(0∼1)
T                                  nε
z 1∼n                 z i(0∼1)              Pi ( Ai(0∼1) )z i(0∼1)                   .
i=1
μ
It follows from the above theorem that the state z i(0∼1) , i = 1, 2, . . . , n, of each
subsystem eventually converges into the following ellipsoid centered at the origin:
μ,ε
T                             nε
i (0) =           z i(0∼1)            z i(0∼1)       Pi ( Ai(0∼1) )z i(0∼1)                 ,
μ
which implies that the state x1(0∼1) of the original system also converges into the
following ellipsoid centered at the origin:
μ,ε
T                                 nε
1 (0) =            x1(0∼1)             x1(0∼1)        P1 ( A(0∼1) )x1(0∼1)                   .
μ
9.3 Backstepping for Mixed-Order SFSs                                                                315

## [184] `book_2026_volume1` (PDF p.337, L320)

Theorem 9.2 Suppose that Assumption 9.2 holds. Let μ and ε be two arbitrarily
given positive numbers, and Ai0∼m i −1 ∈ R1×m i , i = 1, 2, . . . , n, be a set of matrices
satisfying (9.60). Assume that there exist a set of non-negative continuous scalar
functions ρk (z i(0∼m i −1) |i=1∼k ), k = 1, 2, . . . , n, satisfying (9.85). Then, controller
(9.86) for the uncertain high-order SFS (9.3) guarantees that the transformed states
(0∼m i −1)
z i          , i = 1, 2, . . . , n, finally converge into the following ellipsoid:
n
T                        nε
μ,ε
(0) = z i(0∼m i −1) |i=1∼n            z i(0∼m i −1)       Pi z i(0∼m i −1) ≤          ,
i=1
μ
where Pi = P i (Ai0∼m i −1 ).
It is known from the above theorem that the states z i(0∼m i −1) , i = 1, 2, . . . , n,
of each subsystem eventually converge into the following ellipsoid centered at the
origin:
9.3 Backstepping for Mixed-Order SFSs                                                                     321
μ,ε
T                        nε
i (0) =        z i(0∼m i −1)   z i(0∼m i −1)       Pi z i(0∼m i −1) ≤        .
μ
Since z 1 = x1 , the state x1(0∼m 1 −1) converges into the following ellipsoid centered at
the origin:
μ,ε
T                        nε
1 (0) =        x1(0∼m 1 −1)    x1(0∼m 1 −1)        P1 x1(0∼m 1 −1) ≤             .
μ
To end this section, we make a few remarks.

## [185] `book_2026_volume1` (PDF p.352, L336)

Theorem 10.1 Let Assumption 10.1 hold, and Ai0∼1 ∈ R1×2 , i = 1, 2, . . . , n, be a
set of matrices such that. Ai0∼1 ∈ R2×2 , i = 1, 2, . . . , n, are stable. Then, for any
10.3 Backstepping for High-Order SFSs                                                                   337
set of unknown constant parameters .ϑi ∈ R, i = 1, 2, . . . , n, the adaptive control
law (10.40) for the second-order SFS (10.1) guarantees that
1. z i(0∼1) → 0, t → ∞, i = 1, 2, . . . , n;
2. θi − θ̂i , i = 1, 2, . . . , n are bounded.
It follows from the above theorem that x1 → 0, t → ∞. However, if the state
transformation (10.43) is a diffeomorphism from x1∼n to z 1∼n , and x1∼n (0) =
z 1∼n (0), or equivalently, αi−1 (x1∼i (0)) = 0, i = 2, 3, . . . , n, then we also have
x (0∼1) → 0, t → ∞, i = 1, 2, . . . , n.
i

## [186] `book_2026_volume1` (PDF p.358, L342)

Theorem 10.2 Let Assumption 10.2 hold, and Ai0∼m i −1 ∈ R1×m i , i = 1, 2, . . . , n,
be a set of matrices which make.   Ai0∼m i −1 , i = 1, 2, . . . , n, stable. Then, for any
set of unknown constant parameters .ϑi ∈ R, i = 1, 2, . . . , n, the adaptive control
law (10.73) for system (10.3) guarantees that
10.3 Backstepping for High-Order SFSs                                                      343
1. z i(0∼m i −1) → 0,. t → ∞,. i = 1, 2, . . . , n;
2. θi − θ̂i , i = 1, 2, . . . , n, are bounded.
Since z 1 = x1 , we have
x (0∼m 1 −1) → 0, t → ∞.
In order to let x1 (t) track asymptotically some sufficiently smooth reference signal
x ∗ (t), it suffices to substitute, in the second- or high-order methods of backstepping,
equation (10.7) or (10.52) by
(0∼1)
z (0∼1) = x1(0∼1) − x1∗
1                                ,
or
(0∼m 1 −1)
z (0∼m 1 −1) = x1(0∼m 1 −1) − x1∗
1                                               ,
and then deal with the terms related to the reference signal x1∗ (t) properly in the
sequential processes.
In description, the above backstepping method of high-order systems appears to
be much more complicated. Yet it should be noted that in many specific engineering
applications,.m i ,.i = 1, 2, . . . , n, often take the values of.1 and.2, and in such applica-
tions, the mixed-order backstepping method is in fact simpler than the second-order
backstepping method.

## [187] `book_2026_volume1` (PDF p.368, L353)

Theorem 11.1 Suppose that Assumptions 11.1–11.3 hold. Let
1. μc and μo be two positive numbers;
2. A0∼n−1 ∈ Rr ×nr and L ∈ Rnr×m be two matrices satisfying (11.11) and (11.13),
respectively; and
3. P c and P o be two matrices satisfying (11.12), (11.14) and
354                                                                       11 Observer-Based Control
⎧
⎨ μc − λmax (P c ) > 0
2ρ P o Bc       LC 0∼n−1 2                                (11.24)
⎩ μo −              −              > 0.
λmin (P o )    λmin (P o )
Then, the observer-based controller (11.3) guarantees that system (11.23) is
uniformly exponentially stable.
For a proof of the above result, please refer to Appendix B.

## [188] `book_2026_volume1` (PDF p.372, L357)

Theorem 11.2 Let condition (11.37) be met. Then the closed-loop system consisting
of system (11.25) and reduced-order observer-based output feedback (11.33)–(11.34)
is given by               ⎡ (0∼n 1 −1) ⎤          ⎡ (0∼n 1 −1) ⎤
ẋ1                     x1
⎣ ẋ
(0∼n 2 −1) ⎦       ⎣
= A C   x2(0∼n 2 −1) ⎦ ,       (11.38)
ė                     e
where                                              ⎡                          ⎤
11     12 B1 A12
AC = ⎣        21     22 B2 A22 ⎦ ,                       (11.39)
0     0         33
and
e = x2(0∼n 2 −1) − x̂2(0∼n 2 −1) ,                               (11.40)
33 =     0r2 ×n 2 r2 ) + B2 F22 + L B1 F12 (11.41)

## [189] `book_2026_volume1` (PDF p.373, L358)

Theorem 11.3 The matrix pair (                       F , B E ) defined by (11.45)–(11.46) is controllable.
11.3 Reduced-Order Observer-Based Control                                                                          359

## [190] `book_2026_volume1` (PDF p.375, L360)

Theorem 11.4 There exists an observer gain L such that 33 is Hurwitz if and only
if one of the following conditions holds:
f             f
1. the matrix pair 22         is detectable;
2. the matrix pair (          F , C M ) is detectable; and
3. there exists
[0]  [1]        [n 2 −1]
F12                 F12  F12  · · · F12
=     [0]  [1]        [n 2 −1] ,
F22                 F22  F22  · · · F22
[i]                [i]
with F12  ∈ Rr1 ×r2 , F22  ∈ Rr2 ×r2 , i = 1, 2, . . . , n 2 − 1, satisfying
⎡               n 2 −1
⎤
[i]
⎢                   −             s i F12        ⎥
rank ⎢
⎣
i=0
n 2 −1
⎥ = r2 , ∀s ∈
⎦           / C− (11.48)
[i]
s Ir2 −
n2                       i
s F22
i=0
f    f

## [191] `book_2026_volume1` (PDF p.377, L362)

Theorem 11.5 The closed-loop system consisting of system (11.25) and reduced-
order observer-based output feedback (11.33)–(11.34) is given by
⎡                ⎤      ⎡ (0∼n 1 −1) ⎤ ⎡                       ⎤
ẋ1(0∼n 1 −1)          x1                      B1 f 1
⎣ ẋ
(0∼n 2 −1) ⎦
= AC ⎣ x2(0∼n 2 −1) ⎦ + ⎣      B2 f 2       ⎦,                             (11.50)
ė                    e             L B1 f 1 + B2 f 2
where AC , e, and 33 are given by (11.39)–(11.41).

## [192] `book_2026_volume1` (PDF p.378, L363)

Theorem 11.6 Let Assumptions 11.4 and 11.5 be met, condition (11.48) be satisfied,
and the feedback and observer gains A F and L be designed such that AC is Hurwitz.
Then the closed-loop system (11.54) is globally exponentially stable if there exist
scalars k > 0,.ε > 0, and a positive definite matrix. P ∈ Rn×n such that the following
LMI
ACT P + P AC + kα 2 In P Bc
< −εI                  (11.55)
BcT P            −k Ir
is satisfied.

## [193] `book_2026_volume1` (PDF p.381, L366)

Theorem 11.7 Let Assumptions 11.4 and 11.5 be met, condition (11.48) be satisfied,
and the feedback and observer gains A F and L be designed such that F and 33
are Hurwitz. Then the closed-loop system (11.64)–(11.65) is globally exponentially
stable if there exist positive constants k and ε and a positive definite matrix P ∈
Rm 0 ×m 0 , m 0 = n 2 r2 , such that the following LMI
33 P + P             33 + kα
T                              2
In P B L
< −εI               (11.67)
B LT P                −k Ir
is satisfied.
The proof of the above result is given in Appendix B.
Please note that the usage of the above result needs only to check a single LMI
of order n 2 r2 .
11.4 Example: Full-Order Observer-Based Control                                                 367
11.4 Example: Full-Order Observer-Based Control
The thermoacoustic instability system in Zhao et al. (2023b) is used to illustrate
the effectiveness of the proposed observer-based controller. Consider a Rijke tube
without time delays
⎧
⎨ η̈1 = f 1 η(0∼1) (t) + q1 η(0∼1) (t) + u 1
1∼2             1
(11.68)
⎩ η̈2 = f 2 η(0∼1) (t) + q2 η(0∼1) (t) + u 2 ,
1∼2             2
T
where η = η1 η2 , with ηi , η̇i denoting the amplitude of velocity and pressure
fluctuation of the i-th order acoustic mode, respectively, u 1 , u 2 are the control inputs,
and             ⎧
⎨ f i η(0∼1) (t) = −2iπ (γ − 1) Q̇ si (t) sin iπ x f
1∼2
⎩ qi η(0∼1) (t) = − (iπ)2           i   ηi(0∼1) , i = 1, 2,
i
with γ being the specific heat ratio of the medium, x f being the location of the heat

## [194] `book_2026_volume1` (PDF p.402, L388)

Theorem 12.1 Let. A0∼n−1 ∈ Rr×nr be a matrix satisfying (12.33), and Assumptions
12.6–12.10 be met. Then, a control law that robustly input-to-state stabilizes the
uncertain FAS in (12.21), with z (0∼n−1) being viewed as the system external input, is
given by
−1
u = −B      (·) f (·) + (A0∼n−1 + ) x (0∼n−1) ,               (12.37)
with
1                         1
=                σmax (PL ) ρ (·) + σ 2 (·) PLT ,               (12.38)
εσmin
(PL )                   2
where ε ∈ (0, 1) is an arbitrarily chosen number.
Substituting control law (12.37) into the FAS in (12.21) gives the closed-loop
system
x (n) = − ( A0∼n−1 +           ) x (0∼n−1) +     f (·) + h z (0∼m−1) ,          (12.39)
which has the following equivalent state-space form:
0(n−1)r
ẋ (0∼n−1) =           A0∼n−1 +         x (0∼n−1) +                              (12.40)
f (·) + h z (0∼m−1)
Therefore, the above Theorem 12.1 immediately follows from the following technical
lemma.

## [195] `book_2026_volume1` (PDF p.404, L390)

Theorem 12.2 Let [ Ai ]0∼μi −1 ∈ Rri ×ri μi , i = 1, 2, . . . , η, be a set of matrices sat-
isfying (12.41), Assumptions 12.4–12.8 be met. Then, a control law that robustly
(0∼γ −1)
input-to-state stabilizes the uncertain FAS in (12.16), with z k k |k=1∼ξ being
12.4 Extended and Simplified Cases                                                         391
viewed as the system input, is given by (12.43)–(12.44) with ε ∈ (0, 1) being an
arbitrarily given number.
In view of Proposition 12.1, we immediately have from the above result the
following corollary, which gives the solution to Problem 12.1.

## [196] `book_2026_volume1` (PDF p.406, L392)

Theorem 12.3 Let. A0∼n−1 ∈ Rr×nr be a matrix satisfying (12.33), and Assumptions
12.2, 12.10, and 12.11 hold. Then a controller that robustly input-to-state stabilizes
the uncertain FAS in (12.47), with z (0∼m−1) being viewed as the system external input,
is given by
u = −B −1 x (0∼n−1) , t f x (0∼n−1) , t + u ∗
(12.49)
u ∗ = A0∼n−1 +         x (0∼n−1) ,
with
= εσ 2 1(P ) ϑ PLT ( A0∼n−1 )
min   L
(12.50)
ϑ = σmax
(PL ) ρ    x (0∼n−1) , t + 21 σ 2 x (0∼n−1) , t ,
where ε ∈ (0, 1) is an arbitrarily given number.
The following result immediately follows from the above Theorem 12.3 and

## [197] `book_2026_volume1` (PDF p.408, L394)

Theorem 12.4 Let A0∼n−1 ∈ Rr×nr be a matrix satisfying (12.33), and Assumptions
12.6–12.13 be met. Then, a control law that robustly input-to-state stabilizes the
uncertain FAS (12.51), with z (0∼m−1) being viewed as the system external input, is
given by (12.53) and (12.59), with ε ∈ (0, 1 − c) being an arbitrary scalar.
To end this subsection, we point out that the above results can be also generalized
into the multi-order FAS case.
Again here we only demonstrate with the case of single-order FASs.
When the second subsystem in (12.47) does not exist, the Type I system (12.47)
becomes the following uncertain FAS:
x (n) = f x (0∼n−1) , t +         f x (0∼n−1) , t + B x (0∼n−1) , t u,         (12.60)
where the matrix B x (0∼n−1) , t still satisfies the full-actuation Assumption 12.2,
while Assumption 12.11 on the nonlinear uncertainty f (·) becomes
12.4 Extended and Simplified Cases                                                        395

## [198] `book_2026_volume1` (PDF p.409, L395)

Theorem 12.5 Let. A0∼n−1 ∈ Rr×nr be a matrix satisfying (12.33), and Assumptions
12.2 and 12.11 be met. Then a controller that robustly and globally stabilizes the
uncertain FAS (12.60) is given by (12.49)–(12.50) with σ x (0∼n−1) , t being set to
zero.
It is easy to note that, in the case of ρ x (0∼n−1) , t ≡ 0, the uncertainty f (·)
does not exist, and FAS (12.60) becomes the following deterministic one:
x (n) = f (·) + B (·) u,                  (12.61)
while the controller simply reduces to
u = −B −1 (·) f (·) + A0∼n−1 x (0∼n−1) .
(12.62)
As a consequence, controller (12.62) serves as a controller for the above FAS (12.61).
This is clearly a direct extension of the Proposition 3.1 in Duan (2021g), and also a
restatement of the result in Duan (2023b). Meantime, it follows from Corollary 12.1
that control law (12.62) GUA stabilizes the Type I system (12.11)–(12.12). Such a
fact gives a clear explanation of the concept of stabilizability proposed in section 4.1
in Duan (2021g).
It is seen from the above sections that our solutions to the formulated robust
stabilization problems depend heavily on the parameter matrix A0∼n−1 satisfying
(12.33), or the series of parameter matrices [Ai ]0∼μi −1 ∈ Rri ×ri μi , i = 1, 2, . . . , η,
satisfying (12.41). Now in this subsection let us state an existing parametric solution
to these parameter matrices.
It is seen from the above result that in order to meet condition (12.33), it suffices
only to select a matrix F satisfying
μ
Reλi (F) ≤ − , i = 1, 2, . . . , nr.
(12.63)
Clearly, there are quite some degrees of freedom (DOFs) in the selection of F, while
on the other hand we also have the parameter matrix Z , which provides r 2 n DOFs.
All these DOFs can be further utilized to achieve additional performance of the
system [see, e g., Duan (1992a, 1993a)].
12.5 Two Illustrative Examples
12.5.1 Example 1: Full State Feedback
Consider the following system:
⎧

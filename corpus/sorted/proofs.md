# Sorted Proof Corpus Across 32 Duan First-Author Papers (126 items)

## [1] `aaas_2024_subsfs` (PDF p.4, L462) | Types: `Direct-Algebraic/Citation` | Closer: `证毕。`

证明 对于任一 x1~n ∈ 𝔽̂，由变换式（6）可以
给出一个唯一的 x(0~n - 1) 。反之，由式（7）~式（12）
所给出的推导过程，可根据任一 x(0~n - 1) 得到一个

唯一的 x1~n ∈ 𝔽̂。因此，变换式（6）在 𝔽̂上是一个
一一映射。
根据假设 1 可知，亚严反馈系统式（1）在可行
集 𝔽̂上满足：
ẋ i| x1~n = 0 = 0 i = 1，2，…，n （13）

且 fi( x1~i，t) 的导数为
i ∂fi(x1~i，t) ∂fi(x1~i，t)
fi̇( x1~i，t) =∑ ẋ j + （14）
j = 1 ∂xj ∂t
则根据式（13）和假设 1，进一步有：

fi̇( x1~i，t)| x1~n = 0 = 0 i = 1，2，…，n （15）
根据以上关系，并结合式（4），有：

hi( x1~i，t)| x1~n = 0 = 0 i = 1，2，…，n （16）

因此 ，由变换式（6）可知 x1~n = 0 意味
着 x(0~n - 1) = 0。
令 x(0~n - 1) = 0，再次根据式（16）和变换式（6）

可得 x1~n = 0。证毕。
事实上，变换式（6）还可写为式（17）所示的
形式：
x1~n = Bĕ -1 (x(0~n - 1) ，t)[ x(0~n - 1) - he(x(1~n - 1) ，t) ]

（17）
式中：

⎡⎢ 0 ⎤⎥⎥
⎢⎢⎢⎢ h1(x，t) ⎥⎥

he(x(0~i - 1) ，t) =⎢⎢⎢⎢ h2(x(0~1) ，t) ⎥⎥⎥⎥ （18）
⎢⎢ ⎥⎥
⎢⎢⎢ ⋮ ⎥⎥
⎢⎢hn - 1(x(0~n - 2) ，t)⎥⎥
⎣ ⎦

Be(x(0~n - 1) ，t) = diag( Ir，B1(x，t)，B2(x(0~1) ，t)，⋯，

Bn - 1(x(0~n - 2) ，t)) （19）

基于变换式（6）或式（17），采用文献［27］中

## [2] `aaas_2024_subsfs` (PDF p.5, L521) | Types: `Direct-Substitution` | Closer: `证毕。`

证明 首先，考虑 n = 1 的情形。此时，系统
式（1）可写为

ẋ 1 = f1( x1，t) + G 1( x1，t) u （21）
可行集为

𝔽1={x1| det G 1(x1，t) ≠ 0 或 ∞，x1 ∈ ℝr，t ≥ 0}

根据式（3）、式（5）和式（8）有：
⎧x = x1
⎪⎪⎪⎨B1(x，t) = G 1(x1，t) （22）

⎪⎪⎪⎩h1(x，t) = f1(x1，t)

因此，当 x1 ∈ 𝔽1时，式（21）可另写为
ẋ = h1(x，t)+ B1(x，t)u （23）
接下来考虑 n = 2 的情形，此时亚严反馈系
统式（1）为

⎧ẋ 1 = f1(x1，t) + G 1(x1，t) x2
⎨ （24）
⎩ẋ 2 = f2(x1，x2，t) + G 2(x1，x2，t) u

可行集为

𝔽2={x1~2| x1~2∈ ℝ2r，

det G i(x1~i，t) ≠ 0 或 ∞，t ≥ 0，i = 1，2}

当 x1~2 ∈ 𝔽2时，根据式（24）中的第 1 式，有：
x2 = G-11 (x1，t)[ẋ1- f1(x1，t) ] （25）

并结合式（22），有如式（26）所示的变换：
⎧⎪x1 = x
⎨ -1 （26）
⎪⎩x2 = B̆1 (x，t) [ẋ - h1(x，t)]

对式（24）中的第 1 式两侧进行求导，并代入
第 2 式，同时考虑到递推关系式（3）和式（4），可得
ẍ 1 = ḟ1( x1，t) + Ġ1( x1，t) x2 +
G 1( x1，t) f2( x1，x2，t) +
G 1( x1，t) G 2( x1，x2，t) u =
h2( x1~2，t) + B 2( x1~2，t) u （27）
根据式（10）所示的定义，式（27）可等价地写为
ẍ = h2(x(0~1) ，t) + B2(x(0~1) ，t) u （28）

现在假设 n = k 时定理成立 ，为了方便 ，记
u = xk + 1，此时系统式（1）为

⎧⎪⎪ẋ 1 = f1(x1，t) + G 1(x1，t) x2
⎪⎪⎪⎪ẋ 2 = f2(x1，x2，t) + G 2(x1，x2，t) x3
⎨ （29）
⎪⎪ ⋮
⎪⎪⎪⎪⎩ẋ k = fk(x1~k，t) + G k(x1~k，t) xk + 1

可行集为

𝔽k={x1~k| x1~k∈ ℝkr，det Gi(x1~i，t) ≠ 0或∞；t ≥ 0；

i = 1，2，…，k}

且通过式（30）所述变换：
⎧x1 = x
⎪⎪⎪⎨xi + 1 = Bĭ -1 (x(0~i - 1) ，t) [x( )i- hi(x(0~i - 1) ，t)]（30）

⎪⎪⎪⎩ i = 1，2，…，k - 1

系统式（29）在可行集 𝔽k上可等价转换为式
（31）所示的亚严反馈系统：
x( )k = hk(x(0~k - 1) ，t) + Bk(x(0~k - 1) ，t) xk + 1 （31）

当 n = k + 1 时，系统式（1）的可行集为
𝔽k + 1={x1~k + 1| x1~k + 1∈ ℝ(k + 1) r，det G i(x1~i，t) ≠ 0

或 ∞；t ≥ 0；i = 1，2，…，k + 1}

注意到前 k 个子系统即为式（29），在

x1~k + 1 ∈ 𝔽k + 1条件下，系统式（1）可等价地写为
⎧⎪x( )k = hk(x(0~k - 1) ，t) + Bk(x(0~k - 1) ，t) xk + 1
⎨ （32）
⎪⎩ẋ k + 1 = fk + 1(x1~k + 1，t) + G k + 1(x1~k + 1，t) u
且由式（32）中的第 1 式，可得
xk + 1 = Bk̆ -1 (x(0~k - 1) ，t)[ x( )k - hk(x(0~k - 1) ，t) ]（33）

并结合式（30），可给出 x1~k + 1 ∈ 𝔽k + 1 时的变
换为
⎧x1 = x
⎪⎪⎪⎨xi + 1 = Bĭ -1 (x(0~i - 1) ，t) [x( )i- hi(x(0~i - 1) ，t)]（34）

⎪⎪⎪⎩ i = 1，2，…，k
对式（32）中的第 1 式两侧进行求导，并代入
第 2 式，有：

x(k + 1) = hk(x(0~k - 1) ，t) + Bk(x(0~k - 1) ，t) xk + 1 +

Bk(x(0~k - 1) ，t) fk + 1( x1~k + 1，t) +

Bk(x(0~k - 1) ，t) G k + 1( x1~k + 1，t) u （35）

基于关系式（11）以及递推式（3）和式（4），此
时式（35）可等价写为
x(k + 1) = hk + 1(x(0~k) ，t) + Bk + 1(x(0~k) ，t) u （36）

最终，当 n = k + 1 时，在可行集 𝔽k + 1上，亚严
反馈系统式（1）仍可等价地化为亚全驱系统
式（36），即此时定理仍然成立。证毕。
为了更好地描述全驱系统的奇异集，引入奇
异函数的概念［28］。

## [3] `aaas_2024_subsfs` (PDF p.7, L718) | Types: `Direct-Substitution, State-Space-Conversion` | Closer: `证毕。`

证明 基于前述分析，定理 2 的结论式（41）显
然成立。为了证明对应的指数吸引域，首先将系统
式（41）转化为如式（43）所示的状态空间形式：
x(0~n - 1) = Φ ( A 0~n - 1) x(0~n - 1) （43）
̇
式（43）的解可以写为
x(0~n - 1) (t) = eΦ (A 0~n - 1) t X 0 （44）

式中：X 0 = x(0~n - 1) (0) 是系统初始值。

将式（44）代入矩阵 Bn(x(0~n - 1) ，t)，可得如

式（45）所示的可行性条件：
det Bn(eΦ (A0~n - 1) t X 0，t) ≠ 0 或 ∞ （45）

式中：t ≥ 0，上述约束可以转化为对系统初始值
X 0 的约束。因此，定义集合：
Ra={X0| X0∈ ℝnr，detBn(eΦ (A0~n - 1) t X 0，t) ≠ 0 或∞，

t ≥ 0} （46）

则闭环系统所有从初始值集合 R a 中出发的轨迹
都指数收敛到原点。

进一步 ，利用亚全驱系统式（20）的奇异函
数，式（45）所示的可行性条件可以写为
φ(eΦ (A0~n - 1) t X 0，t) ≠ 0 t ≥ 0 （47）

因此 Ra= Rs。证毕。

## [4] `aas_2020_part1` (PDF p.6, L588) | Types: `Direct-Substitution` | Closer: `QED-symbol-only (□/▪)`

证明. 为了书写方便, 记 D = ddt, 则由式 (23)
的第一个方程可知,

x2 = G−11[Dx1 − f1(x1)] ≜ h2(x1, Dx1) (26)
其中
对式 (26) 求导, 并结合 x ˙2 表达式可得

x˙2 = G−11 D2x1 − Df1(x1) = G2x3 + f2(x1, x2)
(27)

因此由式 (27) 可以直接求得

x3 = G−21G−11 D2x1 − Df1(x1) −

G−21f2(x1, h2(x1, Dx1)) ≜
h3(x1, Dx1, D2x1) (28)

再对式 (28) 两端求导并利用式 (23), 有

x˙3 = G−21G−11 D3x1 − D2f1(x1) −
G−21Df2(x1, h2(x1, Dx1)) =
G3x4 + f3(x1, x2, x3) (29)

将式 (26), (28) 代入式 (29), 经整理又得

x4 = G˜−1∼13 D3x1 − D2f1(x1) −
G−31G−21Df2(x1, h2(·))−

G−31f3(x1, h2(·), h3(·)) ≜ h4(·) (30)

46 卷

依此类推, 重复上述过程不难得到

xn = G˜−1∼1n−1 Dn−1x1 − Dn−2f1(x1) −

G˜−2∼1n−1Dn−3f2(x1, h2(·)) − · · · −
G−n−11G−n−12Dfn−2(x1, h2(·), · · · , hn−2(·)) −

G−n−11fn−1(x1, h2(·), · · · , hn−1(·)) ≜ hn(·)
(31)

Dn−ifi−1(x1, · · · , hi(·)) =
T
ξi−1,1, ξi−1,2, · · · , ξi−1,n ,

i = 2, 3, · · · , n − 2

且右端分量为

ξi−1,j = Dn−ifi−1,j(x1, · · · , hi(·)),
j = 1, 2, · · · , n

从而有

x˙n = G˜−1∼1n−1 Dnx1 − Dn−1f1(x1) −

G˜−2∼1n−1Dn−2f2(x1, h2(·)) − · · · −
G−n−11G−n−12D2fn−2(x1, h2(·), · · · , hn−2(·))−
G−n−11Dfn−1(x1, h2(·), · · · , hn−1(·)) =
fn(x1, h2(·), · · · , hn(·)) + Gnu (32)

Dn−ifi(x1, · · · , hi(·)) = [ξi,1, ξi,2, · · · , ξi,n]T ,
i = 1, 2, · · · , n − 1

类似地,

ξi,j = Dn−ifi,j(x1, · · · , hi(·)), j = 1, 2, · · · , n

显然, 式 (32) 即等价于式 (24). 再由式
(26)、(28)、(30) 和 (31) 可得式 (25). □
为简单起见, 上述仅考虑了系统 (23) 中控制系
数 Gi 为常数矩阵情形. 事实上, 对于 Gi 为矩阵函
数, 即 Gi = Gi(x1, · · · , xi) 的严格反馈型系统, 我
们依然可以利用上述类似过程将其转化为高阶全驱
形式. 特别地, 对于下述常规的积分型系统[35]

x˙1 = x2

...
x˙n−1 = xn (33)
x˙n = f(x1, · · · , xn, t)+
B(x1, · · · , xn, t)u

7 期

由其前 n − 1 个方程可得

xi = x(1i−1), i = 1, 2, · · · , n − 1 (34)

将上述各式代入到系统的最后一个方程可得积分型
系统 (33) 的如下高阶全驱形式:

x(1n) − f(x1,x ˙1, · · · , x(1n−1), t) =

B(x1,x ˙1, · · · , x(1n−1), t)u (35)

## [5] `aas_2020_part1` (PDF p.7, L718) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `QED-symbol-only (□/▪)`

证明. 由于系统 (39) 能控, 根据文献 [28] 中定
理 2 可知, 存在微分同胚变换

z = T1(ˆx) (40)

使得系统 (39) 可以等价地化为下述高阶全驱系统
µ
Aiz(i) = Bv˜ (41)
i=0

其中 Ai ∈ Rr×r, i = 0, 1, · · · , µ, B˜ ∈ Rr×r 为一个
可逆矩阵.
另一方面, 由 β(x) 的可逆性有

v = β−1(x)[u − α(x)]

段广仁: 高阶系统方法 — I. 全驱系统与参数化设计

以此代入式 (41) 可得
µ
Aiz(i) + Bβ˜−1(x)α(x) = Bβ˜−1(x)u (42)
i=0
其中

x = T−1(ˆx) = T−1(T1−1(z))

记

B0(z) = Bβ˜−1(x)
ξ(z) = Bβ˜−1(x)α(x)

则式 (42) 可改写为
µ
Aiz(i) + ξ(z) = B0(z)u (43)
i=0
此即说明存在同胚变换

z = T2(x)

将系统 (36) 化成了高阶全驱系统 (43). □
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

## [6] `aas_2020_part2` (PDF p.4, L364) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `QED-symbol-only (□/▪)`

证明. 周知, 系统 (8) 能控的充要条件是下述能
控性矩阵

Qc = b Ab · · · An−1b (12)
[ ]

46 卷

可逆. 作线性非奇异变换 x ¯ = P−1x, 其中

P = Qc (13)

则根据线性系统能控规范型理论[50] 可知, 系统 (8)
可化为如下 Luenberger 第二能控规范型:

x˙¯ = Acx¯ + bcu (14)

其中

0

...
Ac = , bc =
0
1
(15)

将式 (14) ∼ (15) 写成下述分量形式:

x˙¯1 = ¯x2
x˙¯2 = ¯x3

{ ...
x˙¯n−1 = ¯xn
x˙¯n = −α0x¯1 − α1x¯2 − · · · − αn−1x¯n + u
(16)

记 z = ¯x1, 再联合式 (16) 中的前 n − 1 个方程可得
式 (10) 中的第二组方程. 将式 (10) 中的方程代入
到式 (16) 中的最后一个方程, 可得式 (11) 表述的标
准高阶全驱系统.
最后注意到上述过程的可逆性, 可得定理结
论. □

## [7] `aas_2020_part2` (PDF p.5, L512) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `可得定理结论 / 得证`

证明. 将式 (17) 中的方程分组写成分量形式,
有

x˙ˆk1 = ˆxk2
x˙ˆk2 = ˆxk3

...

x˙ˆk(µk−1) = ˆxkµk
{ µk i−1 r µk j−1
x˙ˆkµk = − αkk xˆki − αki xˆij+
i∑=1 i∑ = 1 j∑=1
i= ̸ k
r
uk + bklul, k = 1, 2, · · · , r
l=∑k+1
(29)

由式 (29) 中的前 µk − 1 个方程可得

xˆk2 = xˆ˙k1
xˆk3 = x¨ˆk1
(30)
{ ...

xˆkµk = ˆxk(µ1k−1), k = 1, 2, · · · , r

将上述关系式 (30) 代入到式 (29) 中的最后一式可

得
(µ1) µ1 i−1 (i−1) r
xˆ11 = − α11 xˆ11 − γ1 + u1 + b1lul
i∑µ=12 l∑=2r
xˆ(21µ2) = − α22i−1xˆ21(i−1) − γ2 + u2 + b2lul
i∑=1 l∑=3
...
{ (µr−1) µr−1 i−1 (i−1)
xˆr−1,1 = − αr−1,r−1xˆr−1,1 − γr−1+
i∑=1r
ur−1 + br−1,lul
µr l∑=r
xˆr(µ1r) = − αrri−1xˆ(ri1−1) − γr + ur
i∑=1
(31)

其中
r µk
γi = αikj−1xˆ(kj1−1), i = 1, 2, · · · , r
k∑ = 1 ∑j=1
k = ̸ i

再注意到约定式 (28), 可将式 (31) 进一步写为

µ1+1 i−1 (i−1) r
α11 xˆ11 + γ1 = u1 + b1lul
i∑=1 l∑=2
µ2+1 i−1 (i−1) r
α22 xˆ21 + γ2 = u2 + b2lul
i∑=1 l∑=3
...
{µr−1+1 i−1 (i−1) (32)
αr−1,r−1xˆr−1,1 + γr−1 = ur−1+
i∑=1 r
br−1,lul
l∑=r
µr+1 i−1 (i−1)
αrr xˆr1 + γr = ur
i∑=1
最后定义
T
z = [xˆ11 xˆ21 · · · xˆr1] (33)

再使用式 (25) ∼ (27) 中的记号, 系统 (32) 可表为
式 (24) 所表达的高阶全驱系统, 同时式 (30) 给出式
(23) 中的第二式.
注意到上述过程的可逆性, 可得定理结论. □

## [8] `aas_2020_part2` (PDF p.6, L638) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `QED-symbol-only (□/▪)`

证明. 将非线性系统 (35) ∼ (37) 写成分量形
式, 有

x˙¯1 = ¯x2

...
(40)
{x˙¯n−1 = ¯xn
x˙¯n = f(¯x, t) + u

记 z = ¯x1, 并联合 (40) 中的前 n − 1 个方程可得式
(38) 中的方程. 再将这些方程代入到式 (40) 中的最
后一个方程, 可得式 (39) 描述的高阶标准全驱系统.
最后注意到上述过程的可逆性, 可得定理结
论. □

## [9] `aas_2020_part2` (PDF p.7, L741) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `QED-symbol-only (□/▪)`

证明. 将式 (42) 中的方程分组写成分量形式,
有

x˙ˆk1 = ˆxk2
x˙ˆk2 = ˆxk3

...
(52)
{x˙ˆk,µk−1 = ˆxkµk
r
x˙ˆkµk = fk(ˆx, t) + uk + bklul,
l=∑k+1
k = 1, 2, · · · , r

由上式中的前 µk − 1 个方程可得

xˆk2 = xˆ˙k1
xˆk3 = x¨ˆk1
(53)
{ ...

xˆkµk = ˆxk(µ1k−1) , k = 1, 2, · · · , r

将该组方程代入到式 (52) 中的最后一式可得

(µ1) r
xˆ11 = f1(ˆx, t) + u1 + b1lul
l∑=2r
xˆ(21µ2) = f2(ˆx, t) + u2 + b2lul
l∑=3
{ ...
(µr−1) r
xˆr−1,1 = fr−1(ˆx, t) + ur−1 + br−1,lul
l∑=r
xˆr(µ1r) = fr(ˆx, t) + ur
(54)

记
T
z = z1 z2 · · · zr
[ ] (55)
{zk = ˆxk1, k = 1, 2, · · · , r

再注意到 B˜ ∈ Rr×r 的表达式和式 (51), 可将式
(54) 写成如下矩阵形式
m−1
Ez(m) − Eiz(i) = f(z,z, · · · , z(m−1), t) + Bu˜
∑ ˙
i=m0
(56)

其中矩阵 E 和 Ei, i = m0, m0 + 1, · · · , m − 1 为一
组对角线元素为 0 或 1 的非零对角矩阵,

f1(·, t)

(m−1) f2(·, t)
f(z,z, ˙ · · · , z , t) =
...
fr(·, t)

将式 (56) 改写成
m−1
Ez(m) = f(z,z, · · · , z(m−1), t) + Eiz(i) + Bu˜
˙ ∑
i=m0

再利用式 (50) 便得式 (49) 所表达的高阶全驱系统,
同时式 (53) 和 (55) 联合给出式 (48) 中第二式.
最后注意到上述过程的可逆性, 可得定理结
论. □
上述定理将系统 (42) ∼ (47) 的等价高阶全驱系
统表成多变量广义系统 (49) 的形式. 但由定理的证
明可见, 原系统等价于系统 (54). 如果令

u˜ = Bu˜

则系统 (54) 又可以等价地化成下述形式的一组高阶
全驱系统

xi(ui) = fi(x, t) + ˜ui, i = 1, 2, · · · , r

也即多输入非线性系统 (42) ∼ (47) 可以等价地化为
一组高阶全驱系统. 对于这组高阶全驱系统, 显然存
在控制律使得闭环系统由 r 个相互独立的线性定常
系统构成. 这种将一个系统化成若干个高阶全驱系
统来实现其控制的方法, 就是该系列论文所讨论的
高阶全驱系统方法.

## [10] `aas_2020_part3` (PDF p.5, L441) | Types: `Observer/Error-Dynamics` | Closer: `QED-symbol-only (□/▪)`

证明. 我们先证明能观规范型系统 (2) 可以表
示为系统 (22) 的形式.
将式 (2) 写成下述分量形式

x˙¯1 = −α0x¯n + β0(¯xn, u)
x˙¯2 = ¯x1 − α1x¯n + β1(¯xn, u)

... (23)

x˙¯n−1 = ¯xn−2 − αn−2x¯n + βn−2(¯xn, u)
x˙¯n = ¯xn−1 − αn−1x¯n + βn−1(¯xn, u)

再对上式中的第 i 式求 i − 1 阶导数, 可得

x˙¯1 = −α0x¯n + β0(¯xn, u)
x¨¯2 = ˙¯x1 − α1x ˙¯n + β˙1(¯xn, u)

...
x¯(nn−−11) = ¯x(nn−−22) − αn−2x¯(nn−2) + βn(n−−22)(¯xn, u)
x¯(nn) = ¯x(nn−−11) − αn−1x¯(nn−1) + βn(n−−11)(¯xn, u)
(24)

将上式中等号两边的各项对应相加, 可得

n−1 n−1
x¯(nn) + αix¯(ni) = βi(i)(¯xn, u)
i=0 i=0

最后记 z = ¯xn, 上式便给出式 (22) 表述的标准高阶
全量测系统.
另一方面, 设式 (22) 成立, 往证式 (2).
令

n−1 n−1
ρ =∆ z(n) + αiz(i) − βi(i)(z, u)=0 (25)
i=0 i=0

再记 αn = 1, 并取状态向量如下:

x¯n = z
x¯n−1 = αnz ˙ + αn−1z − βn−1(z, u)

...
n (i−2) n−1 (i−2) (26)
x¯2 = αiz − βi (z, u)
i=2 i=2
n (i−1) n−1 (i−1)
x¯1 = αiz − βi (z, u)
i=1 i=1

段广仁: 高阶系统方法 — III. 能观性与观测器设计

利用式 (26) 中各式和式 (25) 容易验证

x˙¯1 − ρ = −α0x¯n + β0(z, u)
x˙¯2 − x ¯1 = −α1x¯n + β1(z, u)

...

x˙¯n−1 − x ¯n−2 = −αn−2x¯n + βn−2(z, u)
x˙¯n − x ¯n−1 = −αn−1x¯n + βn−1(z, u)

此即是规范型 (2) 的分量形式. □
借助于命题 1, 我们易得定理 1 的下述推论.

## [11] `aas_2020_part3` (PDF p.5, L549) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

证明. 我们先证明规范型 (9) ∼ (15) 可以表为
式 (28) 的形式.

将式 (9) 中的方程分组写成分量形式, 有
m
x˙˜k1 = − αkj0x˜jµj + bk0(·, u)
j=1
m
x˙˜k2 = ˜xk1 − αkj1x˜jµj + bk1(·, u)
j=1

...
m µk−2
x˙˜k,µk−1 = ˜xk,µk−2 − αkj x˜jµj+ (32)
j=1
bk,µk−2(·, u)
m µk−1
x˙˜kµk = ˜xk,µk−1 − αkj x˜jµj+
j=1
bk,µk−1(·, u)
k = 1, 2, · · · , m

然后对上式中的第 i 式求 i − 1 阶导数, 可得
m
x˙˜k1 = − αkj0x˜jµj + bk0(·, u)
j=1
m
x¨˜k2 = ˙˜xk1 − αkj1x˙˜jµj + ˙bk1(·, u)
j=1

...
x(µk−1) = ˜x(µk−2) − m αµk−2x(µk−2)+
˜k,µk−1 k,µk−2 kj ˜jµj (33)
j=1
b(k,µµkk−−2)2(·, u)
x(µk) = ˜x(µk−1) − m αµk−1x(µk−1)+
˜kµk k,µk−1 kj ˜jµj
j=1
b(k,µµkk−−1)1(·, u)

k = 1, 2, · · · , m

再将上式各方程中等号两边各项对应相加, 可得
µk−1 m µk−1
x(kµµkk) + αkjix(jµi)j = b(kii)(·, u)
˜ ˜
i=0 j=1 i=0
k = 1, 2, · · · , m (34)

注意到式 (31), 可将式 (34) 进一步写为
µk m µk−1
αkjix˜(jµi)j = b(kii)(·, u)
i=0 j=1 i=0
k = 1, 2, · · · , m (35)

令

T
z = x˜1µ1 x˜2µ2 · · · x˜mµm (36)

再利用式 (30) ∼ (31) 便可将式 (35) 表示成式 (28).
反过来, 设式 (28) 成立, 下面证明式 (9) ∼ (15)
成立.

46 卷

利用式 (30) ∼ (31) 及式 (36) 可将式 (28) 写为
式 (34) 给出的分量形式. 基于式 (34) 再补充定义
下述变量:
µk i (i−µk+1)
x˜k,µk−1 = αkkx˙˜kµk + γµk−1−
i=µk−1
bµk−1(z, u)

...
µk i (i−2) µk−1 (i−2)
x˜k2 = αkkx˙˜kµk + γ2 − bi (z, u)
i=2 i=2
µk i (i−1) µk−1 (i−1)
x˜k1 = αkkx˙˜kµk + γ1 − bi (z, u)
i=1 i=1
k = 1, 2, · · · , m
(37)

其中
µk−1 m
γl = αkjix˜(jµi)j, l = 1, 2, . . . , µk − 1
i=l j = 1
j ≠ k

然后利用定理 1 的充分性证明中的技巧, 令
µk m µk−1
ρk =∆ αkjix˜(jµi)j − b(kii)(z, u) = 0 (38)
i=0 j=1 i=0

利用式 (37) 中各式和式 (38), 经过一定的推导容易
验证
m
x˙˜k1 − ρk = − αkj0x˜jµj + bk0(z, u)
j=1
m
x˙˜k2 − x ˜k1 = − αkj1x˜jµj + bk1(z, u)
j=1

...
m µk−2
x˙˜k,µk−1 − x ˜k,µk−2 = − αkj x˜jµj+ (39)
j=1
bk,µk−2(z, u)
m µk−1
x˙˜kµk − x ˜k,µk−1 = − αkj x˜jµj+

## [12] `fasta_2026_roea` (PDF p.3, L422) | Types: `Stationary-Point-Reduction` | Closer: `This completes the proof.`

Proof. For any fixed (x, y) ∈ ℝ2, define

g(t, x, y) = ϕ1(t)x + ϕ2(t)y. (20)

Since ϕ1(t) and ϕ2(t) admit exponential representations,
g(t, x, y) can be written as

g(t, x, y) = (α1x + α2y)eλ1t + (β1x + β2y)eλ2t,

which is continuously differentiable on [ti−1, ti).
The derivative of g(t, x, y) is given by

g′(t, x, y) = λ1(α1x + α2y)eλ1t + λ2(β1x + β2y)eλ2t.

Since λ1 ≠ λ2, the equation g′(t, x, y) = 0 admits at most
one solution in (ti−1, ti), implying that g(t, x, y) has at most
one interior stationary point on this interval.
Therefore, the maximum of g(t, x, y) over [ti−1, ti) can
only be attained either at the endpoints ti−1 and ti, or at the
unique interior stationary point t∗, if it exists.
Hence, the inequality

g(t, x, y) < d, ∀t ∈ [ti−1, ti)

is equivalent to requiring that

g(t, x, y) < d, ∀t ∈ Ti(x, y),

where Ti(x, y) consists of the endpoints and the interior sta-
tionary point when it exists.
This completes the proof.

For the interior stationary point t∗, the constraint

ϕ1(t∗)x + ϕ2(t∗)y < d

is equivalent to

(α1x + α2y)eλ1t∗ + (β1x + β2y)eλ2t∗ < d.

Using the stationary condition, it can be further reduced to

(1 − λ2)(β1x + β2y) eλ2t∗ < d,
λ1

which admits a fully explicit form

λ2 λ1(α1x + α2y) λ2λ−2λ1
(1 − )(β1x + β2y)(− ) < d.
λ1 λ2(β1x + β2y)

## [13] `ijss_2021_part2` (PDF p.8, L787) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: According to (7), the matrix Lk(z(0∼k−1), ζ, t)
is given recursively by

Lk(z(0∼k−1), ζ, t)

= Lk−1(z(0∼k−2), ζ, t)Gk(x1(0∼∼k1−)1, xk, ζ, t),

k = 1, 2, . . . , n, (31)

with the initial value L0 = I. This is obviously equiva-
lent to (29).
Simultaneously, using (8), and takingL˙k = 0, k = 1,
2, . . . , n − 1 into consideration, we can write the recur-
sive formula for hk(z(0∼k−1), ζ, t) as

hk(z(0∼k−1), ζ, t)

= h˙k−1(z(0∼k−2), ζ, t) + Lk−1fk(x1(0∼∼k1−)1, xk, ζ, t)

k = 1, 2, . . . , n, (32)

with the initial value h0(ζ, t) = 0. Thus, we further
have, from the above formula,

h1(z, ζ, t) = f1(z, ζ, t),

h2(z(0∼1), ζ, t) = h˙1(z, ζ, t) + L1f2(x1(0∼∼11), x2, ζ, t)

[ f˙1(z, ζ, t) ]
= [I L1] (0∼1) ,
f2(x1∼1 , x2, ζ, t)

h3(z(0∼2), ζ, t) = h˙2(z(0∼1), ζ, t)

+ L2f3(x1(0∼∼21), x3, ζ, t)

[ f¨1(z, ζ, t) ]
= [I L1] (0∼1)
f˙2(x1∼1 , x2, ζ, t)

+ L2f3(x1(0∼∼21), x3, ζ, t)

⎡ f¨1(z, ζ, t) ⎤
= L0∼2 f˙2(x1(0∼∼11), x2, ζ, t) . (33)
⎢⎣ f3(x1(0∼∼21), x3, ζ, t) ⎥⎦

Continuing this process, we can finally get for-
mula (30). Note that (27) can be obtained easily, we
then complete the proof. ■

## [14] `ijss_2021_part2` (PDF p.10, L1104) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: The result can be easily proven by applying

## [15] `ijss_2021_part3` (PDF p.6, L533) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: It follows from (7) that the matrix A + γ2I is
stable, thus there exists a matrix P satisfying

γ T γ
(A + I) P + P(A + I) < 0.
2 2

Expanding the above equation gives the Equation (8).
■

## [16] `ijss_2021_part3` (PDF p.6, L549) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: In view of

n−1
det sI − Φ A0∼n−1 = det(snIr + Aisi),
( ( )) ∑
i=0

the eigenvalues of Φ(A0∼n−1) can be arbitrarily
assigned by properly choosing Ai, i = 0, 1, . . . , n − 1,
thus the conclusion holds. ■

It is known from Lemma 3.1 that, when the condi-
tion in (9) holds for some μ > 0, there exists a positive
definite matrix P(A0∼n−1) satisfying

ΦT(A0∼n−1)P(A0∼n−1) + P(A0∼n−1)Φ(A0∼n−1)

< −μP(A0∼n−1). (10)

Partition P(A0∼n−1) as

P(A0∼n−1) = P1 P2 · · · Pn , Pi ∈ ℝnr×r,
[ ]
(11)
we can further introduce the following notation which
will be frequently used in the paper:

PL(A0∼n−1) = P(A0∼n−1)[0] = Pn. (12)
Ir

Finally, let us state the following simple result.

## [17] `ijss_2021_part3` (PDF p.6, L617) | Types: `Direct-Substitution, Lyapunov, State-Space-Conversion` | Closer: `QED-symbol-only (□/▪)`

Proof: Substituting the control law (14) into sys-
tem (2), gives the following closed-loop system

x(n) + A0∼n−1x(0∼n−1) = φ(x(0∼n−1)), (15)

where

φ(x(0∼n−1))

= − 1 ρ2(x(0∼n−1))PT(A0∼n−1)x(0∼n−1)
4ε L
+ Δf (x(0∼n−1)). (16)

The closed-loop system (15) can be written in the
following state-space form:

x(0∼n−1) = Φ(A0∼n−1)x(0∼n−1) + [ 0(n−1)r ].
˙ φ(x(0∼n−1))
(17)
Since Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1 satisfy the con-
dition (9), there exists a positive definite matrix
P(A0∼n−1) satisfying (10). Then the following Lya-
punov function can be chosen for the system (17):

V = 1 x(0∼n−1) TP(A0∼n−1)x(0∼n−1).
2( )

In view of (10), (12) and (17), we have

V = 1 x(0∼n−1) TPx(0∼n−1) + 1 x(0∼n−1) T
˙ 2(˙ ) 2( )
× Px(0∼n−1)
˙
T
= 1(Φx(0∼n−1) + [ 0(n−1)r ]) Px(0∼n−1)
2 φ(x(0∼n−1))

+ 1 x(0∼n−1) T
2( )

× P(Φx(0∼n−1) + [ 0(n−1)r ])
φ(x(0∼n−1))

= 1 x(0∼n−1) T ΦTP + PΦ x(0∼n−1)
2( ) ( )

+ x(0∼n−1) TP[ 0(n−1)r ]
( ) φ(x(0∼n−1))

≤ −μ x(0∼n−1) TPx(0∼n−1) + x(0∼n−1) T
2( ) ( )

× PLφ(x(0∼n−1))

= −μV + x(0∼n−1) TPLφ(x(0∼n−1)).
( )

Next, let us consider the last term of the above
equation. It follows from Condition 1, Lemma 3.3 and
Equation (16) that

x(0∼n−1) TPLφ(x(0∼n−1))
( )
ρ2(x(0∼n−1)) T
= − [(x(0∼n−1) PLPTx(0∼n−1)]
4ε ) L

+ x(0∼n−1) TPLΔf (x(0∼n−1))
( )
ρ2(x(0∼n−1)) 2
= − PTx(0∼n−1)
4ε ‖‖‖ L ‖‖‖

+ x(0∼n−1) TPLΔf (x(0∼n−1))
( )
ρ2(x(0∼n−1)) 2
≤ PTx(0∼n−1)
4ε ‖‖‖ L ‖‖‖
+ Δf (x(0∼n−1)) PTx(0∼n−1)
L
‖‖‖ ‖‖‖‖‖‖ ‖‖‖
ρ2(x(0∼n−1)) 2
≤ PTx(0∼n−1)
4ε ‖‖‖ L ‖‖‖
+ρ(x(0∼n−1)) PTx(0∼n−1)
L
‖‖‖ ‖‖‖
≤ ε.

Combining the above two equations, gives

V˙ ≤ −μV + ε. (18)

It thus follows from the Comparison Theorem that

V ≤ V (0) e−μt + ε 1 − e−μt ,
μ ( )

which gives

V ≤ (V (0) − ε )e−μt + ε → ε , t → ∞.
μ μ μ

Thus the state x(0∼n−1) eventually converges into the
ellipsoid Θμ,ε(0). The proof is then completed. ■

In the case of n = 1, the system (2) becomes

x˙ = f (x) + Δf (x) + L(x)u, (19)

and the robust control law turns into

## [18] `ijss_2021_part3` (PDF p.19, L1962) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: Since

∂Δf1(z) ′
Δf¨1(z) = ( z˙)
∂z

∂2Δf1(z) 2 ∂Δf1(z)
= 2 z˙ + z¨,
∂z ∂z

we have, using (112) and (113),

∂2Δf1(z) 2 ∂Δf1(z)
Δf¨1(z) ≤ 2 z + |¨z|
|| || |||| ∂z |||| ˙ |||| ∂z ||||

≤ γ1 |˙z| + γ2z˙2 |¨z| .
( )

Further using (111), gives

Δf2(z, z¨ − z2 + Δf1(z) ′)
||| ( ) |||
... f1(z)
≤ σ2 |z| z − 2zz˙ + ∂Δ z˙
|||| ∂z ||||
... ∂Δf1(z)
≤ σ2 |z|(|z − 2zz˙| + |˙z|)
|||| ∂z ||||

≤ σ2 |z| |...z − 2zz˙| + γ1 |˙z|2 .
( )

Finally, using the above two relations and the definition

(130), yields

Δf z(0∼3)
||| ( )||
| 2
≤ Δf¨1(z) + Δf2(z,z ¨ − z + Δf1(z))
|| || || ||
≤ γ1 |˙z| + γ2z˙2 |¨z|
( )
+ σ2 |z| |...z − 2zz˙| + γ1 |˙z|2 .
( )

Thus the conclusion holds. ■

Using the function ρ(z(0∼3)) defined in the above
proposition, we can design for the system (109) the
following robust stabilising control law

u = −(A0∼3z(0∼3) + f (z(0∼2)) + u∗)

u∗ = 1 ρ2(z(0∼3))PLT(A0∼3)z(0∼3), (131)
4ε

where A0∼3 is chosen to satisfy

Reλi Φ A0∼3 < −μ, i = 1, 2, 3, 4, (132)
( ( )) 2

μ and ε are two arbitrarily given positive numbers. The
controller guarantees that the vector z(0∼3) converges
into the following ellipsoid centred at the origin:

Θμ,ε(0) = {z((0∼3)) (z(0∼3))TPz(0∼3) ≤ ε },
|||| μ

where P = P(A0∼3) and PLT(A0∼3) are determined
by (10) and (12).
The above design process demonstrates that the
design based on a single HOFA model is even simpler
than the proposed high-order method of backstep-
ping, but it should be noted that the two approaches
need different prior knowledge of the nonlinear uncer-
tainties.

## [19] `ijss_2021_part4` (PDF p.6, L541) | Types: `Direct-Substitution, Lyapunov, State-Space-Conversion` | Closer: `Thus the conclusion follows.`

Proof: Substituting the control law (9) into (1), gives
a closed-loop system composed of

θ˙ˆ = H(x(0∼n−1))PT(A0∼n−1)x(0∼n−1),
L

and

x(n) + A0∼n−1x(0∼n−1) = HT(x(0∼n−1))θ˜, (10)

where

θ˜ = θ − ˆθ. (11)

The part of closed-loop system (10) can be expressed
in the following state-space form:

x(0∼n−1) = Φ(A0∼n−1)x(0∼n−1)
˙

+ [ 0(n−1)r ]. (12)
HT(x(0∼n−1))θ˜

Since Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1 are a set of
matrices such that Φ(A0∼n−1) is stable, there exists
a positive definite matrix P(A0∼n−1) satisfying (6).
Therefore, the following Lyapunov function can be
selected for system (12):

V = x(0∼n−1) TP(A0∼n−1)x(0∼n−1) + θ˜Tθ ˜.
( )

In view of (6), the first equation in (9), and also

θ˙˜ = ˙θ − ˙ˆθ = − ˙ˆθ,

we have

V = x(0∼n−1) TPx(0∼n−1) + x(0∼n−1) TPx(0∼n−1)
˙ (˙ ) ( ) ˙

+ θ˙˜Tθ ˜ + ˜θTθ ˙˜
T
= (Φx(0∼n−1) + [ 0(n−1)r ]) Px(0∼n−1)
HT(x(0∼n−1))θ˜

+ x(0∼n−1) T
( )

× P(Φx(0∼n−1) + [ 0(n−1)r ])
HT(x(0∼n−1))θ˜

T
− 2θ˙ˆ θ ˜

= x(0∼n−1) T ΦTP + PΦ x(0∼n−1) − 2θ˙ˆTθ ˜
( ) ( )

+ 2 x(0∼n−1) TP(A0∼n−1)[ 0(n−1)r ]
( ) HT(x(0∼n−1))θ˜

≤ − x(0∼n−1) Tx(0∼n−1)
( )

+ 2[(x(0∼n−1) TPL(A0∼n−1)
)

× HT(x(0∼n−1)) − θ˙ˆT]θ˜

= − x(0∼n−1) 2.
‖‖‖ ‖‖‖
Thus the conclusion of the theorem holds following
from the Lyapunov Theorem. ■

## [20] `ijss_2021_part5` (PDF p.5, L444) | Types: `Multi-Conclusion` | Closer: `QED-symbol-only (□/▪)`

Proof: The first conclusion can be easily verified. In
view of

T 2 2
θ˜r0θ˜ ≤ 1 θ ˜r0 + θ ˜ ),
2 (‖‖‖ ‖‖‖ ‖‖‖ ‖‖‖
T 2 2
θ˙˜r0θ˜ ≤ 1 θ ˙˜r0 + θ ˜ ),
2 (‖‖‖ ‖‖‖ ‖‖‖ ‖‖‖

and Assumption A3, the second and the third conclu-
sions can be immediately derived. ■

Secondly, the following three lemmas given in
Duan (2021b) are also needed.

## [21] `ijss_2021_part5` (PDF p.6, L578) | Types: `Multi-Step, Multi-Conclusion, Direct-Substitution, Lyapunov, State-Space-Conversion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: The proof is composed of four steps.

Step 1: The Lyapunov function

Substituting control law (12)–(15) into system (3)
gives part of the closed-loop system as

x(n) + A0∼n−1x(0∼n−1)

= φr(x(0∼n−1)) + φa(x(0∼n−1)), (17)

where

φr(x(0∼n−1)) = Δf (x(0∼n−1))

− 1 ρ2(x(0∼n−1))
4ε
× PT(A0∼n−1)x(0∼n−1), (18)
L
φa(x(0∼n−1)) = HT(x(0∼n−1))θ˜. (19)

Closed-loop system (17) can be expressed in the fol-
lowing state-space form:

x(0∼n−1) = Φ(A0∼n−1)x(0∼n−1) + [ 0(n−1)r ]. (20)
˙ φr + φa

When Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1, satisfy condi-
tion (7), we know that there exists a positive definite
matrix P = P(A0∼n−1) satisfying Equation (9). Thus,
the following Lyapunov function can be chosen for
system (20):

V = 1(x(0∼n−1))TPx(0∼n−1) + 1θ˜Tθ˜. (21)
2 2

It follows from (7) that Equation (9) holds. Then, in
view of (9) and Equations (20)–(21), we have

V = 1 x(0∼n−1) TPx(0∼n−1)
˙ 2(˙ )

+ 1 x(0∼n−1) TPx(0∼n−1)
2( ) ˙

+ 1θ˙˜Tθ ˜ + 1θ˜Tθ˜ ˙
2 2
T
= 1(Φx(0∼n−1) + [ 0(n−1)r ]) Px(0∼n−1)
2 φr + φa

+ 1 x(0∼n−1) TP(Φx(0∼n−1) + [ 0(n−1)r ])
2( ) φr + φa
T
+ θ˙˜ θ ˜

= 1 x(0∼n−1) T ΦTP + PΦ x(0∼n−1)
( ) ( )

+ x(0∼n−1) TP[0(n−1)r] + θ˙˜Tθ Step 3: Dealing with Va
( ) φr+φa ˜

≤ −μ x(0∼n−1) TPx(0∼n−1) It follows from (25) that
2( ) μ T
Va + θ˜ θ˜
(0∼n−1) T ˙˜T 2
+ (x ) PL (φr + φa) + θ θ ˜ T T
= (x(0∼n−1)) PLφa + θ˙˜ θ ˜ + μθ˜Tθ˜
= −V0 + Vr + Va, (22) 2
= [(x(0∼n−1))TPLHT + θ˙˜T]θ˜ + μθ˜Tθ˜. (28)
where 2

V0 = μ x(0∼n−1) TPx(0∼n−1), (23) Further using the first conclusion in Lemma 2.1 gives
2( )

(0∼n−1) T ξ = Δθ˜r0 − θ˜e0 − θ˜ = 0,
Vr = (x ) PLφr, (24)
and
and μ
(0∼n−1) T ˙˜T Va + 2θ˜Tθ˜
Va = (x ) PLφa + θ θ ˜. (25)
= [(x(0∼n−1))TPLHT + θ˙˜T]θ˜ + μθ˜Tθ˜
Step 2: Dealing with V0 and Vr 2
+ (μ + 1) ξTθ ˜
Adding and subtracting μ2θ˜Tθ ˜ in the last step of T
Equation (22) yields = [(x(0∼n−1)) PLHT − θ˙˜eT0 + ˙˜θrT0]θ˜

V˙ ≤ −V0 − μθ˜Tθ˜ + Vr + Va + μθ˜Tθ˜ + (μ + 1)(− θ˜eT0 + ˜θrT0 − ˜θT)θ˜ + μθ˜Tθ˜
2 2 2

= −μV + Vr + Va + μθ˜Tθ˜. (26) = [(x(0∼n−1) TPLHT − θ˙˜T]θ˜ + θ˙˜Tθ˜
2 ) e0 r0

Using Assumption A1 and Lemma 2.4, we have − (μ + 1)θ˜eT0θ˜ + (μ + 1)(θ˜rT0θ˜ − ˜θTθ ˜)

Vr = (x(0∼n−1))TPLφr + μθTθ
˜ ˜
2
ρ2(x(0∼n−1)) (0∼n−1) T T (0∼n−1) (0∼n−1) T T T T
= − [(x ) PLPLx ] = [(x ) PLH − θ˙˜e0 − (μ + 1)θ ˜e0]θ˜
4ε

+ (x(0∼n−1))TPLΔf + θ˙˜rT0θ˜ + (μ + 1)θrT0θ˜ − μ + 2θ˜Tθ˜. (29)
˜ 2
ρ2(x(0∼n−1)) 2
= − PTx(0∼n−1) Then, using adaptive control law (15), and in view
4ε ‖‖‖ L ‖‖‖ of (16) and the last two conclusions in Lemma 2.1, we

+ x(0∼n−1) TPLΔf obtain
( )
ρ2(x(0∼n−1)) 2 Va + μθ˜Tθ˜

## [22] `ijss_2021_part5` (PDF p.10, L978) | Types: `Multi-Step, Lyapunov` | Closer: `QED-symbol-only (□/▪)`

Proof: For clarity, we divide the proof into three steps.

Step 1: The Lyapunov function

It can be easily observed that this step is exactly the
same as Step 1 in the proof of Theorem 3.1. We thus
need only to start from (22) to (25).

Step 2: Dealing with Vr

Similar to Step 2 in the proof of Theorem 3.1, using
Assumption thmA2’, we have

Vr = (x(0∼n−1))TPLφr

ρ(x(0∼n−1)) T
= − [(x(0∼n−1) PLPTx(0∼n−1)]
ε ) L

+ x(0∼n−1) TPLΔf
( )
ρ(x(0∼n−1)) 2
= − PTx(0∼n−1)
ε ‖‖‖ L ‖‖‖

+ x(0∼n−1) TPLΔf
( )

ρ(x(0∼n−1))
≤ − PTx(0∼n−1)
ε ‖‖‖ L ‖‖‖
+ Δf PTx(0∼n−1)
L
‖‖ ‖‖‖‖‖ ‖‖‖
ρ(x(0∼n−1)) 2
≤ − PTx(0∼n−1)
ε ‖‖‖ L ‖‖‖

+ ρ(x(0∼n−1)) PTx(0∼n−1) 2
L
‖‖‖ ‖‖‖
= (−1 + 1)ρ(x(0∼n−1)) PTx(0∼n−1) 2
ε ‖‖‖ L ‖‖‖

= −1−ερ(x(0∼n−1)) PTx(0∼n−1) 2. (50)
ε ‖‖‖ L ‖‖‖

Step 3: Dealing with Va and V

Recalling that the parameter vector θ is constant, we
have

θ˙˜ = ˙θ− ˙ˆθ = − ˙ˆθ.

It thus follows from (19) and (49) that

Va = (x(0∼n−1))TPLφa + θ˙˜Tθ ˜

= [(x(0∼n−1))TPLHT + θ˙˜T]θ˜

= [(x(0∼n−1))TPLHT − θ˙ˆT]θ˜

= 0. (51)

Using (22), (23) and (50)–(51), we obtain

V ≤ −μ x(0∼n−1)
˙ 2 ‖‖‖ ‖‖‖P
− 1−ερ(x(0∼n−1)) PTx(0∼n−1) 2
ε ‖‖‖ L ‖‖‖
≤ 0,

when ε ≤ 1. Therefore, it follows from the Lyapunov
Theorem that the conclusion holds. ■

In the case that the state x(t) is required to track a
given signal x∗(t), the robust adaptive tracking control
law for the system turns into

u = −L−1(x(0∼n−1)))(⌢u0 + ⌢ur + ⌢ua), (52)

where

⎧⌢u0 = A0∼n−1(x − x∗)(0∼n−1) + f (x(0∼n−1))

⎪⎪⎪⎪⎪⎪⎨ − (x∗)(n),

⌢ur = 1ρ(x(0∼n−1))PT(A0∼n−1)(x − x∗)(0∼n−1),
ε L
⎪⎪⎪⎪⎪⎪⎩⌢ua = HT(x(0∼n−1))θ,
ˆ
(53)

where θˆ is given by the adaptation law

θ˙ˆ = −H(x(0∼n−1))PT(A0∼n−1) x − x∗ (0∼n−1).
L ( )
(54)

When this robust adaptive control law is applied to
HOFA system (3), ‖ θ˜‖ is guaranteed to be bounded,
and
∗ (0∼n−1)
lim x − x = 0. (55)
t→∞‖‖‖( ) ‖‖
‖
Therefore, asymptotic tracking of the system state vec-
tor to the reference signal can be realised in such a case.
In the particular case of Δf (x(0∼n−1)) = 0, this result
reduces to the one given in Duan (2021c).

## [23] `ijss_2021_part6` (PDF p.8, L824) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: Write Equation (29) as

Φ(A0∼n−1)V = VF. (32)

Further, introducing the variable

W = −A0∼n−1V, (33)

and in view of

Φ(A0∼n−1) = Φ(00∼n−1) − BcA0∼n−1, (34)

we can convert equivalently the above equation (32)
into the form of (25). Therefore, it follows from
Lemma 3.1 that all the matrices V and W are given
by (26), and equation (30) can then be further solved
from (33). ■

## [24] `ijss_2021_part6` (PDF p.9, L893) | Types: `Direct-Substitution, Lyapunov, State-Space-Conversion` | Closer: `QED-symbol-only (□/▪)`

Proof: When the control law (18), with A0∼n−1 cho-
sen as in (30), applied to system (17), the closed-loop
system can be obtained and rewritten in the state-space
form (22). It follows from Theorem 3.4 that (29) holds.
Thus, substituting (29 ) into (24), yields

Gdy(s) = CV(sI − F)−1V−1BcE. (40)

Considering that the matrix F is Hurwitz, there exists
unique positive definite solutions P1 and P2 satisfying
the following Lyapunov equations

FP1 + P1FT = −V−1BcEETBTcV−T (41)

and

FTP2 + P2F = −VTCTCV, (42)

respectively. According to Lemma 3.3, the matrices P1
and P2 given by (38) – (39) are, respectively, the solu-
tions to the Lyapunov equations (41) and (42). There-
fore, it follows from Lemma 3.2 that ‖Gdy(s)‖22 is given
by (37)–(39). The proof is then completed. ■

With the help of the above two theorems, solution
to the disturbance problem in system (17) via the con-
troller (18) can then be solved by optimising the design
parameters F and Z to minimise ‖Gdy(s)‖22. Clearly,
an advantage of the parametric approach is that it is
easy to have additional indices to be comprehensively
optimised together with this H2 index.
In applications, it suffices to choose F to be a diago-
nal matrix with negative diagonal elements. In the case
that complex eigenvalues are expected, we may have
such a block

−a −b
[ ], (43)
b −a

with a and b being two positive scalars, included as a
diagonal block in F.
Clearly, there are quite some degrees of freedom
in the selection of F, while on the other hand we
also have the parameter matrix Z, which provides
r2n degrees of freedom. All these degrees of freedom
can be further utilised to achieve additional perfor-
mance of the system (see, e.g.Duan, 1992a, 1993b;
Duan et al., 2002, 2000a; Duan & Zhao, 2020).

## [25] `ijss_2021_part6` (PDF p.11, L1089) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: Obviously, the homogeneous equation of the
above GSE (54) is Equation (25). Let (V, W) be a
general solution to the homogeneous GSE (25), and
(Π0, Γ0) be a particular solution to the above GSE (54),
then it is easily known that the general solution (Π, Γ)
to the above nonhomogeneous equation (54) is given
by

Π = Π0 + V, Γ = Γ0 + W. (56)

It follows from Lemma 3.1 that a general solution to
the homogeneous GSE (25) is given by (26). Further, it
can be easily verified that a particular solution to the
above nonhomogeneous GSE (54) is given by

Π0 = 0, Γ0 = R. (57)

Therefore, the general solution (55) immediately fol-
lows from (26), (56) and (57). ■

## [26] `ijss_2021_part6` (PDF p.12, L1222) | Types: `State-Space-Conversion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: If we take the following control law

u = −B−1(ym, ζ, t)(f (ym, ζ, t) − v), (66)

then the corresponding closed-loop system is given by

x(n) = Ed(0∼k−1) + v
⎧
⎪⎨ym = Cmx(0∼n−1) (67)
yr = Crx(0∼n−1) + Erd(0∼k−1).
⎪⎩

The above Equation (67) can be also equivalently
rewritten in the following state-space form:

⎧x˙(0∼n−1) = Φ(00∼n−1)x(0∼n−1) + Bcv
+BcEd(0∼k−1)
⎪⎪⎪⎪⎨ (68)
ym = Cmx(0∼n−1)
⎪⎪⎪⎪⎩yr = Crx(0∼n−1) + Erd(0∼k−1).

It is noted that the above (68) is now a constant linear
system. Applying Lemma 4.1 to the above system (68),
we can design the following controller v to meet the
asymptotic output regulation requirement (45):

x˙ˆ(0∼n−1) Φ(00∼n−1) BcE x(0∼n−1)
⎧[ ] = [ ] [ˆ ]
d˙ˆ(0∼k−1) 0 Φ(S0∼k−1) dˆ(0∼k−1)
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨
+[Bc]v +[Lx](Cmx(0∼n−1) − ym)

## [27] `ijss_2021_part6` (PDF p.13, L1332) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: In view of the expression of Bc given in (21), we
have

sI − ΦE
rank[ ]
CI

sInr − Φ(00∼n−1) −BcE
⎡ ⎤
= rank 0 sIkp − Φ(S0∼k−1)
⎣ Inr 0 ⎦
(73)

## [28] `ijss_2021_part6` (PDF p.14, L1433) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: If we take

D(s)
Nˆ(s) = [ ] (84)
N(s)

and

Dˆ(s) = [sInr − ΦT(00∼n−1)]D(s), (85)

then it can be easily verified using the relation (77) that

(sI − ΦTE)N ˆ(s) = CITDˆ(s). (86)

Further note that

D(s)
N ˆ(s) ⎡ ⎤
[ ] = N(s) , (87)
Dˆ(s) ⎣(sInr − ΦT(00∼n−1))D(s)⎦

Nˆ(s) and ˆD(s) are clearly right coprime since D(s)
and N(s) are right coprime. Thus the above (86) is a
generalised RCF of the matrix pair (ΦTE, CIT).
In view of (82), Nˆ(s) and Dˆ(s) can be obviously
rewritten into the form of
ω
Nˆ(s) = [Di]si (88)
∑ Ni
i=0

and
ω
Dˆ(s) = [sInr − ΦT(00∼n−1)]∑Disi
i=0
ω+1
= ∑[Di−1 − ΦT(00∼n−1)Di]si, (89)
i=0

respectively. Thus it follows from the Theorems 2.1
and 4.3 in Duan (2015) that all the matrices Lx and
Ld satisfying (80) can be given by (81), where Z0 ∈
ℝnr×(nr+kp) is a parameter matrix satisfying the con-
straint (83). Then the proof is completed. ■

## [29] `ijss_2021_part7` (PDF p.22, L2246) | Types: `Direct-Algebraic/Citation` | Closer: `The proof is completed.`

Proof: Under Assumption A2, we clearly know that
z(t) converges exponentially to zero. Further, follow-
ing from the second equation in (103), we have

y = y0 e−tβ. (105)

Therefore, y(t) converges exponentially to zero in view
of β > 0.
Since

z˙ = −c1α1 e−tα1 − c2α2 e−tα2, (106)

we have, from (94),

x = − 1 (c1α1 e−t(α1−β) + c2α2 e−t(α2−β)),
y0
which is also clearly seen to converge exponentially to
zero.

Figure 3. Simulation results for Example 6.2.

Next, let us consider the controller (102). Using
(105), we have

v = −yβ = −y0β e−tβ, (107)

which converges exponentially to zero. Further, using
(104) and (106), we can easily derive

za0 + (a1 − β)z ˙
= d1 e−tα1 + d2 e−tα2,

with

d1 = c1 (a0 − βα1 + α1a1) ,

d2 = c2 (a0 − βα2 + α2a1) .

Thus

d1 e−tα1 + d2 e−tα2
u = − y −tβ
0 e

= − 1 (d1 e−t(α1−β) + d2 e−t(α2−β)), (108)
y0

which also goes to zero exponentially. The proof is
completed. ■

For the case of a0 = 6, a1 = 5, and β = 1, simula-
tion of the designed control system has been carried

out and shown in Figure 3, where the initial values are
taken as

x (0) = −15, y (0) = 10, z (0) = −20.

## [30] `ijss_2022_part8` (PDF p.10, L1075) | Types: `Multi-Conclusion` | Closer: `QED-symbol-only (□/▪)`

Proof: Under given conditions, the first conclusion
can be easily proven, now we need only to show that
the feasibility requirement (38) is met when condi-
tion (40) holds.
First of all, since ν(Pc) ≥ 1, it follows from (40) that

(0∼μk−1) 1
xk (0) |k=1∼η < √ d0 ≤ d0. (41)
‖‖‖ ‖‖‖ ν (Pc)

Thus we have

xk(0∼μk−1)|k=1∼η (0) ∈ 𝔽. (42)

Next, let us define

(0∼μk−1) 2
V (t) = xk (t) |k=1∼η ,
‖‖‖ ‖‖‖Pc

then, following a typical treatment in stability analysis
of linear systems, we can prove that

V˙ (t) ≤ 0.

Therefore,

V (t) ≤ V (0) , ∀ t ≥ 0,

that is,

x(0∼μk−1)(t) |k=1∼η
‖‖‖ k ‖‖‖Pc

≤ xk(0∼μk−1)(0) |k=1∼η , ∀t ≥ 0. (43)
‖‖‖ ‖‖‖Pc
From this we obtain, for t ≥ 0,

(0∼μk−1) 2
λmin (Pc) xk (t) |k=1∼η
‖‖‖ ‖‖‖
(0∼μk−1) 2
≤ λmax (Pc) xk (0) |k=1∼η ,
‖‖‖ ‖‖‖
which further gives, together with condition (40), the
following

(0∼μk−1) 2
xk (t) |k=1∼η
‖‖‖ ‖‖‖
λmax (Pc) (0∼μk−1) 2
≤ xk (0) |k=1∼η
λmin (Pc) ‖‖‖ ‖‖‖

= ‖Pc‖ Pc−1 x(0∼μk−1)(0) |k=1∼η 2
‖‖ ‖‖‖‖‖ k ‖‖‖
(0∼μk−1) 2
= ν (Pc) xk (0) |k=1∼η
‖‖‖ ‖‖‖
≤ d02.

This implies the relation (38). The proof is then
completed. ■

Based on Theorem 4.3 and the above lemma, a
solution to the above Problem 5.1 can be given as
follows.

## [31] `ijss_2022_part8` (PDF p.11, L1157) | Types: `Lyapunov` | Closer: `Thus the conclusion follows.`

Proof: Denote

K = −R−1BTEP, (45)

Ac = AE + BEK, (46)

then, by Theorem 4.3, Ac is Hurwitz. Further note

ATcP + PAc = ATEP + PAE − 2PBER−1BTEP,

it is clear that the Riccati Equation (32) is equivalent to
the following Lyapunov matrix equation

ATcP + PAc+Qc = 0, (47)

with

Qc = CTQC + PBER−1BTEP. (48)

Due to Assumption A2, we have Q = DTD, and
[AE, DC] is observable. Further let

R−1 = TTT,

we can write

Qc = (DC)TDC + PBETTTBTEP

= [(DC)T PBET] [ DC T ]. (49)
(PBET)

Remembering that [AE, DC] is observable, by the well-
known PBH criterion we have

sI − AE
rank[ ] = κ, ∀ s ∈ ℂ.
DC

Using this relation, we immediately have

sI − AE
⎡ ⎤
rank DC = κ, ∀ s ∈ ℂ, (50)
⎣ (PBET)T ⎦

that is, the matrix pair

DC
[AE,[ T ]]
(PBET)

is also observable by the PBH criterion again.
Therefore, the conclusion of the theorem can now
be easily drawn by combining Theorem 4.3 and

## [32] `ijss_2022_part9` (PDF p.7, L688) | Types: `Multi-Conclusion` | Closer: `QED-symbol-only (□/▪)`

Proof: Since [Φk(00∼μk−1), Bkc], k = 1, 2, . . . , η, are
all controllable, it is easy to show that [AE, BE] is also
controllable. Therefore, the first conclusion follows
immediately from the Theorem 7.3.2 in Duan (2016).
Now let us show the second conclusion. When con-
dition (22) is met, partition C as

C = [ C1 ], C1 ∈ ℝr×κ.
C2

Then

rank[sI − A˜ B˜]

sI − AE 0 0 BE
⎡ ⎤
= rank −C1 sIr 0 0 .
⎣ −C2 0 sIm−r 0 ⎦

Clearly, the existence of C2 adds m−r number of trans-
mission zeros {0}. It follows from the first conclusion
that these added transmission zeros are not the con-
trollable modes of the matrix pair [A˜,B˜]. Since they are
not (asymptotically) stable ones, the system is then not
stabilisable. ■

The first conclusion in the above Lemma 3.1 implies
m ≤ r, while the second conclusion further indicates
that the system is even not stabilisable when m > r.
Therefore, the case of m>r is after all of no neces-
sity of consideration. This clearly gives a very impor-
tant insight, that is, the maximum number of signals
(counting by scalar dimension) that the system can
track is not greater than the number of the system
inputs.
Under the condition (21), a feedback controller can
be designed for the above compound system (19) as
follows:

v = KPDxk(0∼μk−1)|k=1∼η + KIq
t
= KPDxk(0∼μk−1)|k=1∼η + KI ∫ y (σ) − yc dσ.
0 [ ]
(23)

Further denote

A˜c = ˜A + ˜B[ KPD KI ]

AE + BEKPD BEKI
= [ ], (24)
C 0

and

C = C1 C2 · · · Cη
{ [ ] (25)
Ck = [Irk 0(μk−1)rk×rk].

Then, the following lemma can be proven, which gives
the property of the above controller (23).

## [33] `ijss_2022_part9` (PDF p.7, L766) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: When the controller (23) is applied to the sys-
tem (16), the closed-loop system is obtained as

x(0∼μk−1)| x(0∼μk−1)|
[ ˙k k=1∼η ] = A˜c[ k k=1∼η ]
q˙ q

BEΓ 0
+ [ ]d − [ ],
yc
(29)

where A˜c is given by (24), which can be made Hur-
witz by selecting the gain matrices KPD and KI due to

## [34] `ijss_2022_part9` (PDF p.15, L1655) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: It follows from Lemma 6.2 that, under condi-
tion (97), there also holds

[xk(0∼μk−1)|k=1∼η (t)] Xe ‖
− [ ] d0, ∀ t ≥ 0.
‖‖‖‖‖ q (t) qe ‖‖‖‖ ≤
(99)
Thus we have

xk(0∼μk−1)|k=1∼η (t) − Xe
‖‖‖ ‖‖‖
[ xk(0∼μk−1)|k=1∼η (t) ] Xe ‖
≤ − [ ]
‖‖‖‖‖ q (t) qe ‖‖‖‖

≤ d0, ∀ t ≥ 0. (100)

This shows

xk(0∼μk−1)|k=1∼η (t) ∈ Ω ⊂ 𝔽.

The proof is done. ■

## [35] `ijss_2022_part9` (PDF p.16, L1753) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: Recall that, under given conditions, the con-
troller (43) results in the closed-loop system given
by (40), with

AcE = VFV−1.

Applying Lemma 6.2, we have, due to (104), the fol-
lowing relation:

xk(0∼μk−1)|k=1∼η (t) − Gxm (t) ≤ d0, ∀ t ≥ 0.
‖‖‖ ‖‖‖
(105)
On the other hand, since xm(0) ∈ Ω0, there holds
Gxm ∈ Ω. Further, recalling Ω ⊂ 𝔹, we obviously have

‖Gxm − xc‖ ≤ dc. (106)

Therefore, using (105) and (106), gives

xk(0∼μk−1)|k=1∼η (t) − xc
‖‖‖ ‖‖‖
≤ xk(0∼μk−1)|k=1∼η (t) − Gxm + ‖Gxm − xc‖
‖‖‖ ‖‖‖
≤ d0 + dc, ∀ t ≥ 0.

This clearly implies (85) (see Figure 1).
■

## [36] `ijss_2024_underactuated4` (PDF p.7, L692) | Types: `Multi-Conclusion, Equivalence/Homeomorphism` | Closer: `QED-symbol-only (□/▪)`

Proof: Taking the differential of the second equation
in (9), yields

∂g g g
y¨ = y˙ + ∂ x˙ + ∂
∂y ∂x ∂t

= Gy x, y, t y ˙ + Gx x, y, t f0 x, y, t
( ) ( ) ( )
∂g
+ Gx x, y, t B0 x, y, t u +
( ) ( ) ∂t

= f1 x, y, t + B1 x, y, t u, (17)
( ) ( )
where

f1 x, y, t = Gy x, y, t y ˙
( ) ( )
∂g
+ Gx x, y, t f0 x, y, t + , (18)
( ) ( ) ∂t
B1 x, y, t = Gx x, y, t B0 x, y, t . (19)
( ) ( ) ( )
Note that, under diffeomorphism (12), we can
write (11) as

x = h (z,z ˙, t) , (20)

and define

f (z,z ˙, t) = f1 (h (z,z ˙, t) , z, t) , (21)

B (z,z ˙, t) = B1 (h (z,z ˙, t) , z, t) . (22)

Then, (14) and (15) are obtained from (18)–(19)
and (21)–(22). While system (13) is obtained from
(12), (17) and (21)–(22). This proves the first conclu-
sion.
The second conclusion is obvious. ■

## [37] `ijss_2024_underactuated4` (PDF p.10, L1077) | Types: `Multi-Conclusion, Direct-Substitution, Equivalence/Homeomorphism` | Closer: `QED-symbol-only (□/▪)`

Proof: Differentiating the third equation in (37), gives

∂g ∂g ∂g ∂g
x¨3 = x˙1 + x˙2 + x˙3 +
∂x1 ∂x2 ∂x3 ∂t

= G1 (x1, x2, x3, t)fˆ1(x1, x2, x3, t)

+ G1 (x1, x2, x3, t)Bˆ1(x1, x2, x3, t)u1

+ G2 (x1, x2, x3, t)fˆ2(x1, x2, x3, t)

+ G2 (x1, x2, x3, t)Bˆ2(x1, x2, x3, t)u2

+ G3 (x1, x2, x3, t)y ˙ + Gt (x1, x2, x3, t) . (49)

On the other side, under the diffeomorphism (40),
equation (38) can be written as

x2 = h x, y,y ˙, t . (50)
( )

Note that, under the diffeomorphism (50) and using
the notations defined in (42)–(43), the first equation
in (37) can be written as

x˙ = fˆ1 x, h x, y,y ˙, t , y, t
( ( ) )
+ Bˆ1 x, h x, y,y ˙, t , y, t u1
( ( ) )
= f0(x, y,y ˙, t) + B0(x, y,y ˙, t)u1. (51)

Furthermore, substituting (50) into (49), and using
(40), yield

y¨ = G3(x, h(x, y,y ˙, t), y, t)y˙ + Gt(x, h(x, y,y ˙, t), y, t)

+ G1(x, h(x, y,y ˙, t), y, t)fˆ1(x, h(x, y,y ˙, t), y, t)

+ G1(x, h(x, y,y ˙, t), y, t)Bˆ1(x, h(x, y,y ˙, t), y, t)u1

+ G2(x, h(x, y,y ˙, t), y, t)fˆ2(x, h(x, y,y ˙, t), y, t)

+ G2(x, h(x, y,y ˙, t), y, t)Bˆ2(x, h(x, y,y ˙, t), y, t)u2.
(52)

With the notations defined in (44)–(46), equation (52)
can be immediately written into the form of

y¨ = f (x, y,y ˙, t) + B1(x, y,y ˙, t)u1 + B2(x, y,y ˙, t)u2.
(53)

Finally, combining the above (53) with (51), gives the
sub-FAS model (41). The first conclusion is proven.
The second conclusion is obvious. ■

## [38] `ijss_2024_underactuated4` (PDF p.14, L1531) | Types: `Multi-Conclusion, Direct-Substitution` | Closer: `QED-symbol-only (□/▪)`

Proof: Taking the differential of equation (75), and
using the definition of f0 and B0 defined in (79)
and (80), yield

(4) {∂2g ∂2g (1∼2) d ∂g }
q2 = ∂q2q˙1 + (0∼1)q2 + dt ∂q q˙1
1 ∂q1∂q2 1

{ ∂2g ∂2g (1∼2) d ∂g }
+ ∂q2∂q1q˙1 + ∂q ∂q(0∼1)q2 + dt ∂q2 q˙2
2 2

{ ∂2g ∂2g (1∼2) d ∂g }
+ ∂q2∂q1q˙1 + ∂q ∂q(0∼1)q2 + dt ∂q2 q¨2
˙ ˙2 2 ˙

+ ∂g (fˇ0(q1, q(20∼1), t) + Bˇ0(q1, q(20∼1), t)u)
∂q1
∂g ∂g ... 2g
+ q¨2 + q2 + ∂ 2
∂q2 ∂q ˙2 ∂t

= f0(q1,q ˙1, q(20∼3), t) + B0(q1,q ˙1, q(20∼1), t)u.

(85)

Using (77), we can define

f q(0∼3), t
( 2 )

= f0(h1(q(20∼3), t), h2(q(20∼3), t), q(20∼3), t),

B q(0∼3), t
( 2 )

= B0(h1(q(20∼3), t), h2(q(20∼3), t), q(20∼3), t).

Then (85) can be written into the form of

q(4) = f q(0∼3), t + B q(0∼3), t u.
2 ( 2 ) ( 2 )

Finally, substituting q2 with q, gives the sub-FAS (81).
The first conclusion is proven.

The second conclusion is obvious. ■

## [39] `ijss_2024_underactuated4` (PDF p.17, L1988) | Types: `Multi-Conclusion, Equivalence/Homeomorphism` | Closer: `QED-symbol-only (□/▪)`

Proof: Taking the differential of equation (116) and
invoking (120)–(122), yield

(4) (∂2g ∂2g ∂2g (1∼2))
q2 = ∂q2q˙0 + ∂q ∂q q˙1 + (0∼1)q2 q˙0
0 0 1 ∂q0∂q2

( ∂2g ∂2g ∂2g (1∼2))
+ ∂q ∂q q˙0 + ∂q2q˙1 + (0∼1)q2 q˙1
1 0 1 ∂q1∂q2

( ∂2g ∂2g ) (1∼2)
+ (0∼1) q˙0 + (0∼1) q˙1 q2
∂q2 ∂q0 ∂q2 ∂q1

∂2g (1∼2) (1∼2)
+ (0∼1) (0∼1)q2 q2
∂q2 ∂q2
∂g
+ [f˘1 (·) + ˘B1 (·) v]
∂q0
∂g
+ [f˘2 (·) + ˘B2 (·) u]
∂q1
d ∂g d ∂g d ∂g (1∼2)
+ dt ∂q0q˙0 + dt ∂q1q˙1 + dt ∂q(0∼1)q

∂g (2∼3) ∂2g
+ (0∼1)q + ∂t2
∂q

= f0 q(0∼1), q(0∼3), t
( 0∼1 2 )

+ B10(q(0∼1), q(0∼3), t)v
0∼1 2
+ B20(q(0∼1), q(0∼3), t)u. (129)
0∼1 2

Using the diffeomorphism transformation (119), we
have (124)-(126).
Finally, applying (119) to (129) and the first
equation in (114), gives the following sub-FAS:

x = f˘1(x(0∼1), y(0∼3), t) + B˘1(x(0∼1), y(0∼3), t)v
¨
y(4) = f (x(0∼1), y(0∼3), t) + B1(x(0∼1), y(0∼3), t)v

+ B2(x(0∼1), y(0∼3), t)u.

which can also be rewritten as (123) in view of the
transformation (119). The first conclusion is proven.
The second conclusion is obvious. ■

Let us now examine the simple form (115). Parallel
to (120)–(122), let us define

f0 q(0∼1), q(0∼3), t
( 0∼1 2 )

(∂2g ∂2g ∂2g (1∼2))
≜ ∂q2q˙0 + ∂q ∂q q˙1 + (0∼1)q2 q˙0
0 0 1 ∂q0∂q2

( ∂2g ∂2g ∂2g (1∼2))
+ ∂q ∂q q˙0 + ∂q2q˙1 + (0∼1)q2 q˙1
1 0 1 ∂q1∂q2

( ∂2g ∂2g ) (1∼2)
+ (0∼1) q˙0 + (0∼1) q˙1 q2
∂q2 ∂q0 ∂q2 ∂q1

∂2g (1∼2) (1∼2)
+ (0∼1) (0∼1)q2 q2
∂q2 ∂q2
d ∂g d ∂g d ∂g (1∼2)
+ dt ∂q0q˙0 + dt ∂q1q˙1 + dt ∂q(0∼1)q2
2
∂g (2∼3) ∂2g
+ (0∼1)q2 + ∂t2 , (130)
∂q2

(0∼1) (0∼3) ∂g(q0, q1, q(20∼1), t)
B10(q0∼1 , q2 , t) ≜ , (131)
∂q0

(0∼1) (0∼3) ∂g(q0, q1, q(20∼1), t)
B20(q0∼1 , q2 , t) ≜ . (132)
∂q1

Then, regarding the sub-FAS model of system (115),
we have the following result.

## [40] `jssc_2022_casestudy` (PDF p.8, L401) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof From the transformation (11), we can get

⎧ x = x1,
⎨ 3 (27)
y = x1 + x2.
⎩
Therefore, we have
⎧ x0 = x10,
⎨ 3 (28)
y0 = x10 + x20,
⎩
and this produces

y0 − x0 = x10 + x320 − x10 = x320

STABILIZATION VIA FAS APPROACH: A CASE STUDY 739

and

y0 + αx0 = x10 + x320 + αx10
= (1 + α) x10 + x320.

Finally, in view of the fact that the initial value transformation (28) is linear in x10 and x320, it
can then be concluded that the two expressions for the region of evaporation 𝕎 in (20) and (25)
are equivalent.
Corresponding to Corollary 4.1, we also have the following result for control of the original
system (1).

## [41] `jssc_2022_freq` (PDF p.9, L459) | Types: `Contradiction` | Closer: `The proof is finished.`

Proof By assuming x(0) = 0 and using (11) we get

X(s) = (sIn − A)−1BU(s)
= N(s)D−1(s)U(s)
= NˇΨ(s)D−1(s)U (s) . (22)

Suppose that Nˇ is singular. Then there exists an elementary (nonsingular) matrix T such that

TNˇ = ⎡ 0 ⎤ , Nˇ1 ∈ ℝ(n−1)×n.
⎣ Nˇ1 ⎦

Let X(s) = T X(s). Then it follows from (22) that

X(s) = T X(s)
= TNˇΨ(s)D−1(s)U (s)

⎡ 0 ⎤ −1
= Ψ(s)D (s)U (s)
⎣ Nˇ1 ⎦

⎡ 0 ⎤
= ,
⎣ Nˇ1Ψ(s)D−1(s)U (s) ⎦

FULLY ACTUATED SYSTEM APPROACH IN FREQUENCY-DOMAIN 2055

from which it follows that

⎡ x1(t) ⎤ −1 ⎡ 0 ⎤
x (t) ≜ ≜ L (X(s)) = ,
⎣ x2(t) ⎦ ⎣ L−1 N ˇ1Ψ(s)D−1(s)U(s) ⎦
( )
in which x1(t) ∈ ℝ. Therefore, x1 (t) cannot be controlled by u. On the other side, it follows
from x (t) = T x (t) and (1) that

x˙ (t) = T (Ax (t) + Bu (t)) = T AT−1x (t) + T Bu (t) ,

which means that x1(t) can indeed be controlled by u. This yields a contradiction. Thus Nˇ is
nonsingular. The proof is finished.
Next let us state our main result in the following theorem.

## [42] `jssc_2022_freq` (PDF p.10, L518) | Types: `Multi-Conclusion` | Closer: `The proof is finished.`

Proof Notice that, by Equation (20), (23) can be equivalently written as D(s)Z(s) =
U(s). Thus, by Proposition 3.3, the generalized state vector Z(s) satisfies (13). It remains to
show (24). According to (13) and (21), we have

⎡ l1(s)Z1(s) ⎤
l2(s)Z2(s)
X(s) = NˇΨ(s)Z(s) = Nˇ . (25)
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
lr(s)Zr(s)

As Nˇ is nonsingular (Lemma 4.4), it follows from the above equation that

⎡ eT1l1(s)Z1(s) ⎤ ⎡ eT1 ⎤⎡ l1(s)Z1(s) ⎤
eT2l2(s)Z2(s) eT2 l2(s)Z2(s)
Z(s) = = , (26)
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ ⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
eTrlr(s)Zr(s) eTr lr(s)Zr(s)

which is just (24). The proof is finished.

## [43] `jssc_2022_freq` (PDF p.13, L673) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Let

⎡ q1−h1 ⎤

⎡ N ′′(q) ⎤ ⎡ N(q) ⎤ q1−h2
= Λ(q), Λ(q) = , (39)
⎣ D′′(q) ⎦ ⎣ D(q) ⎦ ⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
q1−hr

which implies that (N′′(q), D′′(q)) also satisfies (33). Notice that, for any i = 1, 2, · · · , r,

⎡ 1 ⎤ ⎡ q−(hi−1) ⎤

q1−hili(q) = q1−hi q = ... = Eili q−1 . (40)
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ ⎢⎢⎢⎢⎢⎢⎣ q−1 ⎥⎥⎥⎥⎥⎥⎦ ( )
qhi−1 1

FULLY ACTUATED SYSTEM APPROACH IN FREQUENCY-DOMAIN 2059

It follows from (34)–(35), (39), and (40) that

N′′(q) = [ N1l1(q) N2l2(q) · · · Nrlr(q) ]Λ(q)

= [ N1q1−h1l1(q) N2q1−h2l2(q) · · · Nrq1−hrlr(q) ]

= [ N1E1l1 q−1 N2E2l2 q−1 · · · NrErlr q−1) ] (41)
( ) ( ) (
and

D′′(q) = (D0Δ(q) +[ D1l1(q) D2l2(q) · · · Drlr(q) ])Λ(q)

= qD0 +[ D1E1l1 q−1 D2E2l2 q−1 · · · DrErlr q−1) ]. (42)
( ) ( ) (
Similar to Proposition 3.3, if z (k) satisfies the fully actuated PMD model

D′′(q)z (k) = u (k) , (43)

then the state of the linear state-space system (32) can be expressed as

x (k) = N′′(q)z (k) . (44)

The above two equations are respectively equivalent to (36) and (37) in view of (41) and (42).
We finally show (38). It is obtained from (41) that

⎡ E1l1 q−1 z1(k) ⎤
( )
′′ E2l2 q−1 z2(k)
N (q)z(k) = Nˇ ( ) . (45)
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
Erlr q−1 zr(k)
( )
Similar to (25) and (26), we have from (44) and (45) that

⎡ εT1E1l1 q−1 z1(k) ⎤ ⎡ εT1 ⎤⎡ E1l1 q−1 z1 (k) ⎤
( ) ( )
εT2E2l2 q−1 z2(k) εT2 E2l2 q−1 z2 (k)
z (k) = ( ) = ( ) ,
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ ⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦
εTrErlr q−1 zr(k) εTr Erlr q−1 zr (k)
( ) ( )
which is exactly in the form of (38). The proof is thus finished.
We use an example to illustrate the above theorem.

## [44] `jssc_2023_brockett2` (PDF p.6, L256) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof In the following, a proof of the above theorem is given by showing

Form 0
⇕
Form I ⇐⇒ Form V ⇐⇒ Form III
⇕ ⇕
Form II Form IV

a) Equivalence between Forms I and II
Forms I and II are easily shown to be equivalent to each other under the following control
variable transformation
⎧ v = v1 + v2,
⎨
w = v1 − v2.
⎩
b) Equivalence between Forms I and V
This is a well-known fact (e.g., [41]). The equivalence can be established under the following
state transformation
⎧ z1 = θ,
⎪⎪⎨ z2 = x1 cos θ + x2 sin θ, (8)

⎪⎪ z3 = x1 sin θ − x2 cos θ,
⎩
and the following control transformation

⎧ u1 = w,
⎨ (9)
u2 = v − z3w.
⎩

c) Equivalence between Forms III and IV
Clearly, under the following state transformation:

⎧ x1 = q1,
⎪⎪⎨ x2 = q2 + gt,

⎪⎪ θ = γ,
⎩

BROCKETT’S SECOND EXAMPLE: A FAS APPROACH TREATMENT 1795

model (4) is equivalent to
⎧ x˙1 = −F1 sin θ + F2 cos θ,
⎪⎪⎨ x˙2 = F1 cos θ + F2 sin θ, (10)

⎪⎪ θ˙ = F2.
⎩
Further, applying the control transformation

⎧ u1 = −F1 sin θ + F2 cos θ,
⎨ (11)
u2 = F1 cos θ + F2 sin θ,
⎩
proves the equivalence between (10) and Form IV system (6).

d) Equivalence between Forms III and V
Define
⎡ − sin θ cos θ ⎤
G (θ) = , (12)
⎣ cos θ sin θ ⎦

then the system (10) can be further equivalently written as

⎧ ⎡ x˙1 ⎤ ⎡ F1 ⎤
⎪ = G (θ) ,
⎪⎪⎨ ⎣ x˙2 ⎦ ⎣ F2 ⎦ (13)

⎪⎪⎪ θ˙ = F2.
⎩
Regarding the matrix G (θ) defined in (12), the following properties can be easily shown:

det G (θ) = −1,
G−1(θ) = G (θ) ,

and
⎡0 −1⎤
GG˙ = θ. ˙
⎣1 0⎦

Due to these properties, we can introduce the following one-to-one transformation

⎡y1⎤ ⎡x1⎤
= G (θ) , (14)
⎣y2⎦ ⎣x2⎦

which gives

⎡y˙1⎤ ⎡x1⎤ ⎡x˙1⎤
= ˙G + G
⎣y˙2⎦ ⎣x2⎦ ⎣x˙2⎦

−1⎡y1⎤ ⎡F1⎤
= GG˙ + GG
⎣y2⎦ ⎣F2⎦

## [45] `jssc_2023_brockett2` (PDF p.12, L577) | Types: `Multi-Conclusion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Proof of Conclusion 1)
Under given assumptions, the matrix Φ given by (36) also admits the following expression:

⎡−α 0 ⎤ −1
Φ = V V , (46)
⎣ 0 −β⎦

with
⎡ 1 1 ⎤
V = . (47)
⎣−α −β⎦

Therefore, the solution (37) to the system (35) can be given by

⎡z1 (t)⎤ ⎡e−αt 0 ⎤ −1⎡x0⎤
= V V . (48)
⎣z˙1 (t)⎦ ⎣ 0 e−βt⎦ ⎣y0⎦

Therefore,

⎡e−αt 0 ⎤ −1⎡x0⎤
z˙1 (t) = [−α −β] −βt V
⎣ 0 e ⎦ ⎣y0⎦

= 1 αe−αt − βe−βt y0 + e−αt − e−βt αβx0]
α − β[ ( ) ( )

= e−βt [(αe−(α−β)t − β)y0 +(e−(α−β)t − 1)αβx0], (49)
α − β

thus the singularity condition is equivalent to

(αe−(α−β)t − β)y0 +(e−(α−β)t − 1)αβx0 = 0, (50)

which can be written in the form of (40). The first conclusion is proven.

BROCKETT’S SECOND EXAMPLE: A FAS APPROACH TREATMENT 1801

## [46] `odfas_2026_part1` (PDF p.5, L585) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Note that the closed-loop system is given
by

(0∼1) (0∼1)
[ x˙1 ] = AE [ x1 ], (15)
z˙ z

where

## [47] `odfas_2026_part1` (PDF p.10, L1159) | Types: `Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Applying controller (58) to the time-
varying linear system (57), produces the follow-

ing closed-loop system

z˙ z
x˙1 = AE( ˙θ) x1 , (59)
x˙2 x2

where

AE11( θ˙) AE11( θ˙)L − K0 0
AE( θ˙) = 0 0 I3 .
−K1 − (K0 + K1L) D( θ˙)
(60)
with

AE11( θ˙) = D( θ˙) − L − K1.

Define a constant nonsingular matrix

## [48] `odfas_2026_part1` (PDF p.11, L1300) | Types: `Equivalence/Homeomorphism` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Let

x(i) ≤ βie−αit, i = 0, 1, 2, 3.

Noting

|sin x| ≤ |x| , |x ˙ cos x| ≤ |x ˙| ,

we have, under diffeomorphism (69),

|θ| ≤ β0e−α0t,

θ ≤ β1e−α1t,
˙

|ϕ| ≤ J1β2e−α2t + (Mgl + 1)β0e−α0t,
k k

ϕ ≤ J1β3e−α3t + (Mgl + 1)β1e−α1t.
˙ k k

The conclusion holds.

Using the above diffeomorphism (68), we can
derive the OD-FAS of system (65).

## [49] `odfas_2026_part1` (PDF p.12, L1359) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. From the last equation in (68), we can
obtain k
u0 = fy (y1∼2) + u. (73)
(4) Mgl Mgl 2 k k J1J2
x = θ¨ cos θ − θ˙ sin θ − θ¨ + ϕ¨
J1 J1 J1 J1 OD-FAS (70) is further reduced to
Mgl k
= ( cos θ − )θ¨ (4)
J1 J1 x = A2 (y1) ¨x + u0
Mgl 2 k { y = x(0∼1). (74)
− θ˙ sin θ + ϕ.¨
J1 J1
For stabilization of system (74), we can prove
Substituting (65) into the above, yields the following result (see Appendix B).

(4) Mgl k Proposition 3.3. Let F0∼3 ∈ ℝ1×4 be a matrix
x = ( J cos θ − J ) making Φ (F0∼3) Hurwitz. Then a GUE stabiliz-
1 1
ing output feedback controller for system (74) is
Mgl k
×( sin θ − (θ − ϕ)) given in the form of
J1 J1
Mgl 2 k2 k u0 = K11 (y1) y + K12 (y1) z
− θ˙ sin θ + (θ − ϕ) + u {
J1 J1J2 J1J2 z˙ = K21 (y1) y + K22 (y1) z + K23 (y2) sin y1,
Mgl k Mgl k (75)
= ( cos θ − ) ( sin θ − θ) with
J1 J1 J1 J1

−Mglθ˙2sin θ + k2 θ K11 (y1) = −[ F0 F1 − G (y1) ]
J1 J1J2 K12 (y1) = − F2 + A2 (y1) F3
k Mgl 1 1 [ 2 ]
+ [ cos θ − k( + )]ϕ [ 0 L1(y1) + L2 − A2 (y1) ]
J1 J1 J1 J2 K21 (y1) = − F0 L1L2 + F1 − G (y1)
k {
+ u. L1 1
J1J2 K22 (y1) = [ L2 − F2 − A2 (y1) −F3 ]

Further, using (69), gives K23 (y2) = [ Mgl0 ]y22,
J1
(4) Mgl k Mgl k (76)
x = ( cos x − ) ( sin x − x)
J1 J1 J1 J1
Mgl 2 k2
− x˙ sin x + x
J1 J1J2

where

G (y1) = [F2 + A2 (y1)] L1 + F3 [L2 − A2 (y1)] .
(77)

Based on the above, we finally obtain the
following GUE stabilizing output feedback con-
troller for system (70):

z˙ = K21 (y1) y + K22 (y1) z + K23 (y2) sin y1
{ u0 = K11 (y1) y + K12 (y1) z
u = J1kJ2 (u0 − fy (y1∼2)) ,
(78)
where fy (y1∼2) is given by (72), and Kij (y1) ,
i, j = 1, 2, and K23 (y2) are given by (76) with
F0∼3 ∈ ℝ1×4 being a matrix making Φ (F0∼3)
Hurwitz, and A2 (y1) being given by (71). Please
note that once the state x(0∼3) is obtained, the
state of the original system (65), namely, θ(0∼1)
and ϕ(0∼1), can be obtained through diffeomor-
phism (69). Furthermore, it follows from Lemma
3.3 that both θ(0∼1) and ϕ(0∼1) also converge to
zero uniformly exponentially. This means that
controller (78) is also a GUE stabilizing con-
troller for the original system (65).

## [50] `odfas_2026_part1` (PDF p.18, L1953) | Types: `Multi-Conclusion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. We need only to show the third conclu-
sion since all the other conclusions have been
given in Duan (2024b). For this purpose, we as-
sume

ξ(i) ≤ αie−βit, i = 0, 1, 2, 3, (119)

where αi, βi, i = 0, 1, 2, 3, are positive scalars.
Firstly, recalling θ ∈ −π2, π2 , we then have
( )

π 1 2π −β2t
|θ| ≤ sin θ = π ξ¨ ≤ α e . (120)
2 2 c 2c

Secondly, noting from the third equation in
(111) that

ξ¨ = c |sin θ| < c, (121)

we need to modify the relation in (119), corre-
sponding to i = 2, as

ξ¨ (t) ≤ α2e−β2t ≤ c, ∀t ≥ 0.

Thus, for any t0 > 0, we have

ξ¨ (t) ≤ α2e−β2t0 < c, t ∈ [t0, +∞).

This further implies

1

c2 − ξ¨2(t)

≤ α∗ = 1 ∈ [t0, +∞).
c2 − α22e−2β2t0 , t

Therefore,

θ (t) = 1 ...ξ (t)
˙ c2 − ξ¨2(t)

≤ α∗α3e−β3t, t ∈ [t0, +∞). (122)

Finally, it is easy to get from (111), (120) and
(122) that

1 b2 1
|x| ≤ |ξ| + arcsin( ξ¨
b1 b1 c )

≤ α0e−β0t + b2 |θ|
b1 b1
≤ α0e−β0t + α2b2πe−β2t,
b1 2cb1

and

1 2 1 ...
|x ˙| ≤ ξ ˙ + b ξ
b1 b1 c2 − ξ¨2

≤ α1e−β1t + α∗α3e−β3t, t ∈ [t0, +∞).
b1

Thus the equations in (118) hold.

## [51] `odfas_2026_part1` (PDF p.19, L2056) | Types: `Direct-Substitution` | Closer: `Thus the conclusion follows.`

Proof. Note that the closed-loop system is given
by

˙ξ(0∼3) ξ(0∼3)
[ ] = AE [ ], (128)
z˙ z

where

A [ Φ (00∼3) + bcK11C bcK12 ]. (129)
E = K21C K22

Denote

Ca = −a0 − a1l −a2 −a3 C,
[ ]
Cb = −a0 − a1l 0 −a2 −a3 .
[ ]

Substituting the expressions of Kij, i, j, = 1, 2,
in (125)-(126) into the above (129), yields

AE
= [ Φ (00∼3) + bcCa −bca1 ]
−l2 1 0 C −l
[ ]
= [ Φ (00∼3) + bcCb −bca1 ]
−l2 0 1 0 −l
[ ]
0 1 0 0 0
0 0 1 0 0
= 0 0 0 1 0 .
−a0 − a1l 0 −a2 −a3 −a1
−l2 0 1 0 −l
(130)

Since it can be easily verified that

det (sI5 − AE)
= (s + l) s4 + a3s3 + a2s2 + a1s + a0 ,
( )

there holds

eig (AE) = eig (Φ (a0∼3)) ∪ {−l}.

Thus the conclusion follows.

Based on the above, we now have the following
result.

## [52] `odfas_2026_part1` (PDF p.24, L2672) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. It can be easily observed that system
(141) is equivalent to

x(0∼1) = AE (t) x(0∼1), (144)
˙

where

## [53] `odfas_2026_part1` (PDF p.25, L2752) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

### 9.1. Proof of Proposition 3.3

## [54] `odfas_2026_part1` (PDF p.25, L2830) | Types: `Observer/Error-Dynamics` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Let us design a full-state observer for
system (150) as

·
qˆ3∼4
0 1
= [ A2 (y1) 0 ]qˆ3∼4

L1 0
+[ L A y ) ](coqˆ3∼4 − q ˙2) + [ 1 ]u0
2 − 2 ( 1
L1 0
= ALqˆ3∼4 − [ L A y ) ]y˙2 + [ 1 ]u0,
2 − 2 ( 1
(158)

where L = [ L1 L2 ]T is the observer gain,
which makes AL Hurwitz.
Further define

z = ˆq3∼4 + [ L1 ]y2.
L2 − A2 (y1)

Then we have

z˙ = ALqˆ3∼4 + [ −A y ) ]y2 + [ 1 ]u0
˙2 ( 1
0 2 0
= ALqˆ3∼4 + [ Mgl ]y2 sin y1 + [ 1 ]u0.
J1

Therefore the observer is finally given by (156).
Next, note

·
e˙ = q˙3∼4 − qˆ3∼4
0 1 0
= [ ]q3∼4 + [ ]u0
A2 (y1) 0 1
L1 0
−(ALqˆ3∼4 − [ L A y ) ]y˙2 + [ 1 ]u0
2 − 2 ( 1
0 1 L1
= [ A2 (y1) 0 ]q3∼4 + [ L2 − A2 (y1) ]y˙2

−ALqˆ3∼4
L1 1
= [ L 0 ]q3∼4 − ALqˆ3∼4
2
= ALe.

This gives (157).

## [55] `odfas_2026_part1` (PDF p.26, L2972) | Types: `Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

### 9.2. Proof of Lemma 3.1

It is firstly reminded that the notations intro-
duced in (35) are used.
When controller (43) is applied to system (42),
the closed-loop system is given by

x(0∼1) x(0∼1)
[ ˙ ] = AE [ ], (161)
z˙ z

where

Ir
AE = K11 (y, ·) H (y, ·) K12 (y, ·) .
K21 (y, ·) 0 K22 (y, ·)
(162)
Substituting (44) into the above AE, gives

AE = [ AE1 AE2 AE3 ],

where

0
AE1 = −F0 + ρ∗K12 (y, ·) ,
ρ∗H′(y, ·) + K11 (y, ·)

Ir
AE2 = H (y, ·) ,
0

0
AE3 = − (F1 + H (y, ·)) .
H (y, ·) − ρ∗Ir + K12 (y, ·)

Define the state transformation

x(0∼1) x(0∼1)
[ ∗ ] = T [ ],
z∗ z

where

Ir 0 0
T = 0 Ir 0 .
ρ∗Ir −Ir Ir

Then it can be verified that

## [56] `odfas_2026_part2` (PDF p.9, L1025) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: Takingderivativeofthethirdequationin(39),
and using the first two equations in (36), give

x(4) = A1ξ¨1 + A2ξ¨2 + A3ξ¨3

∑︂
= A1f1(ξ1∼3) + A2f2(ξ1∼3) + A3 Aiξi
i=1

+ [A1B1(ξ1∼3) + A2B2(ξ1∼3)]u

= f3(ξ1∼3) + B3(ξ1∼3)u

= f3(y) + B3(y)u, (47)

where f3(y) and B3(y) are given by (42) and (43),
respectively.
Combining(47)withthefirstequationin(36),gives
⎧ [︃ ]︃
⎨ ξ¨1
(4) = f (y) + B(y)u
x (48)
⎩
y = ξ1∼3,

where f (y) and B(y) are given by (41). Further, using
the output transformation (44), we then get the OD-
FAS (46).
Finally, since
[︃ ]︃
B1(y)
B(y) =
A1B1(y) + A2B2(y)
[︃ ]︃ [︃ ]︃
Ir 0 B1(y)
= ,
A1 Ir A2B2(y)

itfollowsfromcondition(37)thatB(y)isnon-singular.
Therefore, OD-FAS (46) is a global one.
■

## [57] `odfas_2026_part2` (PDF p.11, L1260) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `QED-symbol-only (□/▪)`

Proof: Thesecondequationin(63)isclearlyobtained
by substituting the output transformation (44).
Since the closed-loop system of the first subsystem
is still in coordinate (ξ1, za), and remains unchanged
under the new controller (63), it is still linear and
with the set of closed-loop eigenvalues given by
eig((F0a∼1)) ∪ eig(La).
For the second subsystem, the closed-loop sys-
tem in coordinate (x(0∼3), zb) is given by (A4)–(A6),
which is linear with the set of closed-loop eigenvalues

givenbyeig((F0b∼3)) ∪ eig(Lb).Sincethestatetrans-
formation (39) is also linear, the closed-loop system
in coordinate (ξ2(0∼1), ξ3(0∼1), zb) is also linear and is
equivalent to (A4)–(A6). Hence, it possesses also the
setofclosed-loopeigenvalueseig((F0b∼3)) ∪ eig(Lb).
Therefore, the whole set of closed-loop eigenvalues is
given by . The conclusion is proven.
■

Please note that the response (ξ(0∼1), ξ(0∼1)) of the
2 3
closed-loopsystemof(36)undercontroller(63)canbe
easilygiventhroughdiffeomorphism(40)whenx(0∼3)
is derived.

## [58] `odfas_2026_part2` (PDF p.15, L1692) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: From the first equation in (88), we can obtain

1
ξ2 = (m1ξ¨1 + d1ξ̇1 + (k1 + k2)ξ1). (104)
k2
Using the last equation in (91), and with the help
of (89) and (104), we have
(︃ 2 )︃
(4) 1 d k2
x = − (k1 + k2) ξ¨1 + ξ¨2
m1 m1 m1

d1 d1 1 [︃(︃ d1 d2 )︃ d3 ]︃
+ 2(k1 + k2)ξ̇1 − 2k2ξ̇2 + − (k1 + k2) − 2 ẋ
m m m1 m1 m2 m
(︃ 2 )︃
1 d1 k2 k2
= 2 − (k1 + k2) + h1(ξ1∼3) + h2(ξ1∼2) + u1
m1 m1 m1m2 m1m2

× [k2ξ2 − (k1 + k2)ξ1 − d1ξ̇1] = −Gb1∼3x(1∼3) + fy b(y) + k2 u1, (105)
m1m2
k2d2 d1 d1
− ξ̇2 + 2(k1 + k2)ξ̇1 − 2k2ξ̇2 where Gb is given by (101)–(103).
m1m2 m1 m1 1∼3
Next, combining (105) with the output equation
k2
+ (h1(ξ1∼3) + u1) (98), gives the OD-FAS
m1m2 ⎧
1 (︃ d12 )︃ k2d2 ⎨ x(4) = −Gb1∼3x(1∼3) + fy b(y) + k2 u1
= 2 − (k1 + k2) (−d1ξ̇1) − ξ̇2 m1m2 (106)
m1 m1 m1m2 ⎩ yb = Cx(0∼3).
d1 d1
+ 2(k1 + k2)ξ̇1 − 2k2ξ̇2 Finally, combining the last two equations in sys-
m1 m1 tem (88) with the above system (106), we obtain

+ h2(ξ1∼2) + k2 (h1(ξ1∼3) + u1) ⎧ 1 a
m1m2 ξ¨3 = − d3ξ̇3 + fy (y) + 1 u2
[︃ 2 ]︃ ⎪⎪⎪⎪⎪⎨ m3 m3
= d1 2(k1 + k2) − d1 ξ̇1 x(4) = −Gb1∼3x(1∼3) + fy b(y) + k2 u1 (107)
m21 m1 m1m2
(︃ )︃ ⎪⎪⎪⎪⎪⎩ ya = ξ3
− k2 d1 + d2 ξ̇2 yb = Cx(0∼3),
m1 m1 m2
which can be rearranged into the form of (100).
k2 k2
+ h1(ξ1∼3) + h2(ξ1∼2) + u1. ■
m1m2 m1m2

## [59] `odfas_2026_part2` (PDF p.22, L2394) | Types: `Multi-Conclusion` | Closer: `QED-symbol-only (□/▪)`

Proof: Fromthethirdequationin(146),wecanobtain

1
(x¨ − c0 sin θ1) + sin 2θ1 = sin 2θ2.
c11

This immediately gives, in view of (144), Equation
(148). Thus we further have (149). Further, due
to (149), conditions (150) and (151) are obviously
equivalent. Therefore, the first two conclusions hold.
Next, from (149), we immediately have
(︃ )︃
1 1
θ2 = arcsin φ(x,x ¨) . (154)
2 c11

Simultaneously, from the fourth equation in (146), we
can obtain

...
x − ω(θ1,θ ̇1) = 2c11θ ̇2 cos 2θ2.

From this, and Equation (149), we can obtain, under
the condition (150) or (151), the following:

...
x − ω(θ1,θ ̇1)
θ̇2 =
2c11 cos 2θ2
...
x − ω(x,x ̇)
=
2c11 cos 2θ2
...
x − ω(x,x ̇)
= √︂ . (155)
2 c112 − φ2(x,x ¨)

Combining (146), (154) and (155), gives the inverse
(152). Conclusion 3 is proven.

Finally, it is easily seen from the first two equations
in (152) that

lim θ(0∼1) = 0, (156)
x(0∼3)→0 1

and it follows from the third equation in (152) that

lim θ2 = 0. (157)
x(0∼3)→0

Further noting from (144) that

lim φ(x,x ¨) = 0,
x(0∼3)→0

we have

1 1
lim √︂ = .
x(0∼3)→0 2 c2 − φ2x,x) 2c1
11 ¨

Therefore,inviewofthelastequationin(152),wealso
have

lim θ̇2 = 0. (158)
x(0∼3)→0

Combining (156), (157) and (158), gives (153).
■

Basedontheaboveresult,wecannowgivetheOD-
FAS of system (143).

## [60] `odfas_2026_part2` (PDF p.23, L2509) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: Differentiating the last equation in (146), and
using (148)–(149), give

x(4) = θ¨1(c0 cos θ1 − 2c11 cos 2θ1)

− θ̇12(c0 sin θ1 − 4c11 sin 2θ1)

+ 2c11θ¨2 cos 2θ2 − 4c11θ̇22sin 2θ2

= ¨x(c0 cos x − 2c11 cos 2x)

−ẋ2(c0 sin x − 4c11 sin 2x)

− 4c11θ̇22sin 2θ2

+ 2c11(ha(θ1∼3) + τ2) cos 2θ2

= ¨x(c0 cos x − 2c11 cos 2x)

−ẋ2(c0 sin x − 4c11 sin 2x)

φ(x,x ¨) ... 2
− √︂ [x − ω(x,x ̇)]
c11 c112 − φ2(x,x ¨)
√︂
+ 2 c112 − φ2(x,x ¨)ha(θ1∼3)
√︂
+ 2 c112 − φ2(x,x ¨)τ2.

This gives

x(4) = fy(x(0∼3), θ2∼3) + b(x,x ¨)τ2, (163)

where f (x(0∼3), θ2∼3) and b(x,x ¨) are given by (160)
– (161).
Combining the above equation with the third
equation in (143), and adding the output equation
(147), yield the output-dependent sub-FAS (159).
It follows from (160) that b(x,x ¨) ≠ 0 is equivalent
to

φ2(x,x ¨) < c112.

Thus, we can conclude that the set of feasibility of the
system is given by (162).
■

## [61] `odfas_2026_part2` (PDF p.30, L3254) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: Inviewofthenotationsin(A7)and(A8),system(110)
AE(2, 1) = 1 (−F0a + (F1a − d3Ir)L˜a), canbewritteninthefollowingstate-spaceform:
m3 ⎧ [︃ ]︃
1 a a 2 ⎨ q̇1∼4 = (G˜b0∼3)q1∼4 + 03r×r ub
AE(3, 1) = (−F0 + F1L˜a) − ˜La. ⎩ Ir (A10)
m3 yb = Cq1∼4.
Let
⎡ ⎤ Usingthenotationsin(A8),from(A10),wehave
Ir 0 0
T = ⎣ 0 Ir 0 ⎦ . q̇13 = q24, (A11)
−L˜a −Ir Ir [︃ ]︃
Then,itcanbeeasilyverifiedthat q̇24 = − G˜b − G˜b q24

[︃ ]︃ [︃ ]︃ (︃ [︃ ]︃ )︃

## [62] `odfas_2026_part4` (PDF p.13, L813) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Since Rs (t) ∈ ℝn×n is uniformly bounded and uniformly positive definite, so is Rs−1(t).
Then, in view of the uniform asymptotical stability of (3.4), we know that the following system

x˙ = AT0(t) x, A0(t) ∈ ℝn×n (3.5)

is also uniformly asymptotically stable. Choosing P0 (t) = Rs−1(t) , and applying Lemma 3.1 to the
above system, yield

Q0 (t) = −(P˙0 (t) + A0 (t) P0 (t) + P0 (t) AT0(t))

= −(R˙s−1(t) + A0 (t) Rs−1(t) + Rs−1(t) AT0(t)),

which is also uniformly bounded and uniformly positive definite.
Next, let us show the stability of system (3.2)-(3.3) by applying Lemma 3.1. To do this, let us
choose
P (t) = Rs−1(t) , Q (t) = Q0 (t) ,

which are both uniformly bounded and uniformly positive definite. Since

P˙ (t) + ATs(t) P (t) + P (t) As(t)
= R˙s−1(t) + Rs−1(t) AT0(t) Rs(t) P (t) + P (t) Rs(t) A0(t) Rs−1(t)
[ ] [ ]
= R˙s−1(t) + Rs−1(t) AT0(t) + A0(t) R−s1(t)
= −Q (t) .

It again follows from Lemma 3.1 that the LTV system (3.2)-(3.3) is uniformly asymptotically stable.

The above theorem obviously has the following corollary.

## [63] `odfas_2026_part4` (PDF p.14, L902) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. to be added

Finally, let us consider the stability of the following unidirectionally connected system

x˙ = Ax + G (x, t) z (3.10)

z˙ = g (z, t) , (3.11)

where x ∈ ℝn, z ∈ ℝm, A ∈ ℝn×n, and G(x, t) ∈ ℝn×m. For stability of the above system (3.10)-(3.11),

the following result can be easily shown based on the above Lemmas 3.2 and 3.3.

## [64] `odfas_2026_part4` (PDF p.17, L1032) | Types: `Observer/Error-Dynamics` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Design a full-order observer for system (4.6) as

⃗q2 = R (ϕ) A1(ϕ(0∼1))qˆ2 + u0 + L(ϕ(0∼1))(ˆq2 −y ˙) , (4.11)

where L(ϕ(0∼1)) is the observer gain given by (4.9). Let

z = ˆq2 + L(ϕ(0∼1))y.

We further obtain

z˙ = (R (ϕ) A1(ϕ(0∼1)) + L(ϕ(0∼1)))qˆ2 + u0 + L˙(ϕ(0∼1))y

= Ao1qˆ2 + u0 + ˙L(ϕ(0∼1))y

= Ao1(z − L(ϕ(0∼1))y)+ u0 + L˙(ϕ(0∼1))y

= Ao1z +(L˙(ϕ(0∼1))− Ao1L(ϕ(0∼1)))y + u0

= Ao1z + ΘIa(ϕ(0∼2))y + u0, (4.12)

and
qˆ2 = z − L(ϕ(0∼1))y. (4.13)

Combining (4.12) and (4.13), gives the observer (4.7).
Next, using (4.6), (4.7) and (4.11), we obtain

e˙ = ˙q2 − ⃗q2

= ˙q2 −(R (ϕ) A1(ϕ(0∼1))+ L(ϕ(0∼1)))qˆ2 − u0 + L(ϕ(0∼1))y˙

= −(R (ϕ) A1(ϕ(0∼1)) + L(ϕ(0∼1)))qˆ2 − u0 + L(ϕ(0∼1))y˙ + R (ϕ) A1(ϕ(0∼1))q2 + u0

= (L(ϕ(0∼1))+ R (ϕ) A1(ϕ(0∼1)))q2 −(R (ϕ) A1(ϕ(0∼1))+ L(ϕ(0∼1)))qˆ2

= (R (ϕ) A1(ϕ(0∼1)) + L(ϕ(0∼1)))e

= Ao1e.

This gives equation (4.10).

Particularly, when A1(ϕ(0∼1)) = A1 (ϕ), the above result is reduced to the following one which

does not require the availability of ϕ¨.

## [65] `odfas_2026_part4` (PDF p.19, L1143) | Types: `Observer/Error-Dynamics` | Closer: `The proof is completed.`

Proof. Based on Proposition 4.1, we can get the following observer-based controller:

u0 = −F0y −(F1 + R (ϕ) A1(ϕ(0∼1)))qˆ2

{qˆ2 = z − L(ϕ(0∼1))y (4.22)

z˙ = Ao1z + ΘIa(ϕ(0∼2))y + u0.

Firstly, let us show that the above controller GUA stabilizes system (4.4).
Using (4.13), yields

e = q2 −q ˆ2
= q2 − z + L(ϕ(0∼1))y.

Thus we have
z = q2 + L(ϕ(0∼1))y − e.

Using this and (4.20)-(4.21), we can obtain

x¨ = R (ϕ) A1(ϕ(0∼1))x˙ + u0

= R (ϕ) A1(ϕ(0∼1))x˙ + K11(ϕ(0∼1))y + K12(ϕ(0∼1))z

= R (ϕ) A1(ϕ(0∼1))x˙ + K11(ϕ(0∼1))y + K12(ϕ(0∼1)) ⌊q2 + L(ϕ(0∼1))y − e⌋

= R (ϕ) A1(ϕ(0∼1))x˙ + K11(ϕ(0∼1))y + K12(ϕ(0∼1))q2 + K12(ϕ(0∼1))L(ϕ(0∼1))y − K12(ϕ(0∼1))e

= ⌊K11(ϕ(0∼1))+ K12(ϕ(0∼1))L(ϕ(0∼1))⌋x +(R (ϕ) A1(ϕ(0∼1)) + K12(ϕ(0∼1)))x˙ − K12(ϕ(0∼1))e

= −F0x − F1x − K12(ϕ(0∼1))e.
˙

Thus the closed-loop system is given by

{x¨ = −F0x − F1x − K12(ϕ(0∼1))e
˙ (4.23)
e˙ = Ao1e,

or, equivalently,
0
x˙(0∼1) = Φ (F0∼1) x(0∼1) −[ (0∼1) ]e
{ K12(ϕ ) (4.24)
e˙ = Ao1e.

In view of (4.21) and Assumptions A2 and Ap1 we know that K12(ϕ(0∼1)) is also uniformly
bounded. Further, since Ao1 is Hurwitz, and Fi, i = 0, 1, are matrices making Φ (F0∼1) Hurwitz,
according to Corollary 3.2, we can conclude that the closed-loop system (4.24) is GUA stable.
Secondly, let us equivalently convert controller (4.22) into (4.20)-(4.21).
With this set of equations and the last two equations in (4.21), we can further derive

u0 = −F0y −(F1 + R (ϕ) A1(ϕ(0∼1)))qˆ2

= −F0y −(F1 + R (ϕ) A1(ϕ(0∼1))) ⌊z − L(ϕ(0∼1))y⌋

= ⌊(F1 + R (ϕ) A1(ϕ(0∼1)))L(ϕ(0∼1))− F0⌋y −(F1 + R (ϕ) A1(ϕ(0∼1)))z

= K11(ϕ(0∼1))y + K12(ϕ(0∼1))z. (4.25)

Furthermore, we have

z˙ = Ao1z + ΘIa(ϕ(0∼2))y + u0

= Ao1z + ΘIa(ϕ(0∼2))y + K11(ϕ(0∼1))y + K12(ϕ(0∼1))z

= (Ao1 + K12(ϕ(0∼1)))z +⌊ΘIa(ϕ(0∼2))+ K11(ϕ(0∼1))⌋y

= K21(ϕ(0∼2))y + K22(ϕ(0∼1))z. (4.26)

Combining (4.25) and (4.26), yields (4.20). The proof is completed.

The above result clearly has the following corollary which does not require the availability of ϕ¨.

## [66] `odfas_2026_part4` (PDF p.26, L1553) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Take
(0∼1) [AoI − R (ϕ) A1(ϕ(0∼1))]
L(ϕ ) = .
0

Then

AoI(ϕ) = AI (ϕ(0∼1))+ L(ϕ(0∼1))CI

[R (ϕ) A1(ϕ(0∼1)) R (ϕ)] [AoI − R (ϕ) A1(ϕ(0∼1))
= + ] ⌊Ir 0⌋

## [67] `odfas_2026_part4` (PDF p.28, L1610) | Types: `Observer/Error-Dynamics` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Based on system (5.8), and using Lemma 5.1, we can design the following observer:

[⃗q2] = AI ϕ(0∼1)) [qˆ2] +[Ir]u0
⃗d ( dˆ 0

+L(ϕ(0∼1)) (CI [qˆ2]−y)
dˆ ˙

= (AI (ϕ(0∼1)) + L(ϕ(0∼1))CI) [qˆ2]
dˆ

+[Ir]u0 − L(ϕ(0∼1))y
0 ˙

= AoI(ϕ(0∼1)) [⃗q2] +[Ir]u0 − L(ϕ(0∼1))y, (5.17)
⃗d 0 ˙

where AoI (ϕ(0∼1)) is given by (5.11).
Secondly, let

z = [qˆ2]+ L ϕ(0∼1) y.
dˆ ( )

Then we have

z = AoI(ϕ(0∼1)) [qˆ2] +[Ir]u0 + L˙(ϕ(0∼1))y
˙ dˆ 0

= AoI(ϕ(0∼1)) (z − L(ϕ(0∼1))y) +[Ir]u0 + L˙(ϕ(0∼1))y
0

= AoI(ϕ(0∼1))z −(AoI(ϕ) L(ϕ(0∼1)) −L˙(ϕ(0∼1)))y +[Ir]u0
0

= AoI(ϕ(0∼1))z + ΘIb(ϕ(0∼2))y +[Ir]u0.
0

Thus the observer is finally given by (5.13).
Thirdly, using (5.8), (5.15), and (5.17), we have

e = AI ϕ(0∼1)) [q2]+[Ir]u0 −[⃗q2]
˙ ( d 0 ⃗d

= AI ϕ(0∼1)) [q2]+[Ir]u0
( d 0

−(AoI(ϕ(0∼1)) [qˆ2]+[Ir]u0 − L(ϕ(0∼1))q2)
dˆ 0

= AI ϕ(0∼1)) [q2]+ L ϕ(0∼1) CI [q2] − AoI ϕ(0∼1)) [qˆ2]
( d ( ) d ( dˆ

= Ao ϕ(0∼1)) [q2]− Ao ϕ(0∼1)) [qˆ2]
I ( d I ( dˆ

= AoI(ϕ(0∼1))e.

This system is uniformly asymptotically stable following from Lemma 5.1.

5.1.2. A particular solution Next, let us give a particular choice of L(ϕ(0∼1))under the following

extra assumption.

## [68] `odfas_2026_part4` (PDF p.29, L1690) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Denote

A∗ = [0 Ir ], L = [L1]. (5.19)
I 0 AD L2

Then
AL = A∗I + LCI. (5.20)

Further, noting the observability of the matrix pair (A∗I, CI), we immediately get the conclusion that

the eigenvalues of AL can be arbitrarily assigned by selecting matrix L.

Further, introduce the following notation:

[R (ϕ) 0 ]
RE (ϕ) = . (5.21)

## [69] `odfas_2026_part4` (PDF p.30, L1728) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. In view of (5.10) and (5.22), we have

AI (ϕ(0∼1))+ L(ϕ(0∼1))CI

([A1(ϕ(0∼1)) Ir ] [L1M (ϕ) − A1(ϕ(0∼1)) )
= RE (ϕ) + ] ⌊Ir 0⌋

## [70] `odfas_2026_part4` (PDF p.30, L1751) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Firstly, recall equation (5.24). Secondly, it follows from Assumption Ap2 and equation

(5.21) that RE (ϕ) is also uniformly bounded and uniformly positive definite. Therefore, the conclusion

simply follows from Theorem 3.1.

Based on the above preliminary results, we now immediately have the following result.

## [71] `odfas_2026_part4` (PDF p.32, L1859) | Types: `Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Using (5.33) and (5.13), we obtain

u0 = −F0y −(F1 + R (ϕ) A1(ϕ(0∼1)))qˆ2 − R (ϕ) dˆ

= −F0y −⌊F1 + R (ϕ) A1(ϕ(0∼1)) R (ϕ)⌋ [qˆ2]
dˆ

= −F0y −⌊F1 + R (ϕ) A1(ϕ(0∼1)) R (ϕ)⌋ (z − L(ϕ(0∼1))y)

= K12(ϕ(0∼1))z −(F0 + K12(ϕ(0∼1))L(ϕ(0∼1)))y. (5.36)

Substituting (5.36) into (5.13), gives

z˙ = AoI(ϕ) z −(AoI(ϕ) L(ϕ(0∼1)) −L˙(ϕ(0∼1)))y +[Ir]u0
0

= AoI(ϕ) z −(AoI(ϕ) L(ϕ(0∼1)) −L˙(ϕ(0∼1)))y

+[Ir]K12(ϕ(0∼1))z −[Ir] (F0 + K12(ϕ(0∼1))L(ϕ(0∼1)))y
0 0

= (AoI(ϕ) +[Ir]K12(ϕ(0∼1)))z
0

−([Ir] (F0 + K12(ϕ(0∼1))L(ϕ(0∼1))) + ΘIb(ϕ(0∼2)))y
0

= K21(ϕ(0∼2))y + K22(ϕ(0∼1))z.

Therefore, (5.34)-(5.35) hold.
Again, using (5.33), we can rewrite (5.4) as

x¨ = R (ϕ) A1(ϕ(0∼1))q2 + R (ϕ) d + u0

= R (ϕ) A1(ϕ(0∼1))q2 + R (ϕ) d − F0x −(F1 + R (ϕ) A1(ϕ(0∼1)))qˆ2 − R (ϕ) dˆ

= −F0x − F1q2 +(F1 + R (ϕ) A1(ϕ(0∼1)))(q2 −q ˆ2) + R (ϕ)(d −dˆ)

= −F0x − F1x + Q(ϕ(0∼1))e,
˙

where
Q(ϕ(0∼1)) = ⌊F1 + R (ϕ) A1(ϕ(0∼1)) R (ϕ)⌋. (5.37)

Therefore, the closed-loop system is given by

x(0∼1) = Φ(F0∼1) x(0∼1) +[ 0 ]Q(ϕ(0∼1))e
{ ˙ Ir (5.38)
e˙ = AoI(ϕ) e.

According to Lemma 5.1, the second subsystem in (5.38), i.e., system (5.16), is GUA stable under
given assumptions. Further, note that Φ (F0∼1) is Hurwitz, and Q(ϕ(0∼1)) given by (5.37) is also (a)
locally Lipschitz and (b) uniformly bounded or sublinearly grows with respect to ϕ due to Assumptions
Ap2 and Ap1. It thus follows from Corollary 3.2 that the closed-loop system (5.38) is GUA stable.

When L(ϕ(0∼1)) is given by (5.23) and with Li ∈ ℝr×r, i = 1, 2, making AL Hurwitz, the conclusion

also holds in view of Proposition 5.2.

To summarize, we now have the following result regarding the output feedback control of the

nonlinear system (5.1).

## [72] `odfas_2026_part4` (PDF p.39, L2226) | Types: `Observer/Error-Dynamics` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Clearly, due to Assumption Av1, system (6.7) is observable. Thus we can design a
full-state observer for system (6.7) as

⃗q1 = y + L(ϕ(0∼1)) (R (ϕ) A0(ϕ(0∼1))qˆ1 −y ˙ + u0),

where L(ϕ(0∼1)) is given by (6.8) is the observer gain. Thus we have

⃗q1 = Ao2qˆ1 + y − L(ϕ(0∼1))y˙ + L(ϕ(0∼1))u0. (6.12)

Further, let
z = ˆq1 + L(ϕ(0∼1))y. (6.13)

We have
qˆ1 = z − L(ϕ(0∼1))y, (6.14)

and

z˙ = Ao2qˆ1 +(L˙(ϕ(0∼1)) + Ir)y + L(ϕ(0∼1))u0

= Ao2z +(L˙(ϕ(0∼1))− Ao2L(ϕ(0∼1))+ Ir)y + L(ϕ(0∼1))u0

= Ao2z + ΘIIa(ϕ(0∼2))y + L(ϕ(0∼1))u0, (6.15)

where ΘIIa(ϕ(0∼2)) is given by (6.9). Combining (6.15) and (6.14), gives the observer (6.10).
Next, it follows from (6.7), (6.9) and (6.12) that

e˙ = ˙q1 − Ao2qˆ1 − y + L(ϕ(0∼1))y˙ − L(ϕ(0∼1))u0

= −Ao2qˆ1 + L(ϕ(0∼1))y˙ − L(ϕ(0∼1))u0

= −Ao2qˆ1 + L(ϕ(0∼1)) (R (ϕ) A0(ϕ(0∼1))q1 + u0)− L(ϕ(0∼1))u0

= −Ao2qˆ1 + L(ϕ(0∼1))R (ϕ) A0(ϕ(0∼1))q1

= Ao2q1 − Ao2qˆ1
= Ao2e.

This gives the error equation (6.11).

For the case that A0(ϕ(0∼1)) = A0 (ϕ) , we immediately have the following corollary.

## [73] `odfas_2026_part4` (PDF p.41, L2330) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. It follows from Proposition 6.1 that a GUA stabilizing output feedback controller for
system (6.5) is given by

u0 = −(F0 + R (ϕ) A0(ϕ(0∼1)))xˆ − F1y

{qˆ1 = z − L(ϕ(0∼1))y (6.23)

z˙ = Ao2z + ΘIIa(ϕ(0∼2))y + L(ϕ(0∼1))u0.

Using (6.10), yields

e = q1 −q ˆ1
= q1 − z + L(ϕ(0∼1))y.

Thus we have
z = q1 + L(ϕ(0∼1))y − e.

Using this, (4.20), and (6.22), we can obtain

x¨ = R (ϕ) A0(ϕ(0∼1))x + u0

= R (ϕ) A0(ϕ(0∼1))x + K11(ϕ(0∼1))y + K12(ϕ(0∼1))z

= R (ϕ) A0(ϕ(0∼1))x + K11(ϕ(0∼1))y + K12(ϕ(0∼1)) ⌊q1 + L(ϕ(0∼1))y − e⌋

= R (ϕ) A0(ϕ(0∼1))x + K11(ϕ(0∼1))y + K12(ϕ(0∼1))x + K12(ϕ(0∼1))L(ϕ(0∼1))y − K12(ϕ(0∼1))e

= (R (ϕ) A0(ϕ(0∼1))+ K12(ϕ(0∼1)))x +(K11(ϕ(0∼1)) + K12(ϕ(0∼1))L(ϕ(0∼1)))y − K12(ϕ(0∼1))e

= −F0x − F1x − K12(ϕ(0∼1))e.
˙
Thus the closed-loop system is given by

{x¨ = −F0x − F1x ˙ − K12(ϕ(0∼1))e
(6.24)
e˙ = Ao2e,

or, equivalently,
0
x˙(0∼1) = Φ (F0∼1) x(0∼1) −[ (0∼1) ]e
{ K12(ϕ ) (6.25)
e˙ = Ao2e.

Since Φ (F0∼1) and Ao2 are both Hurwitz, and K12(ϕ(0∼1)) is also uniformly bounded or sublinearly
grows with respect to ϕ because of Assumptions A2 and Av2, it follows from Corollary 3.2 that the
closed-loop system (6.24), or, equivalently, (6.25), is GUA stable.
Next, let us show that the controller (6.23) can be equivalently converted into the form of (4.20)
with Kij (ϕ) , i, j = 1, 2, being given by (6.22).
Using (6.21), (6.10) and (6.22), we have

u0 = −(F0 + R (ϕ) A0(ϕ(0∼1)))xˆ − F1y

= −(F0 + R (ϕ) A0(ϕ(0∼1))) (z − L(ϕ(0∼1))y) − F1y

= −(F0 + R (ϕ) A0(ϕ(0∼1)))z +⌊(F0 + R (ϕ) A0(ϕ(0∼1)))L(ϕ(0∼1)) − F1⌋y

= K12(ϕ(0∼1))z +⌊−K12(ϕ(0∼1))L(ϕ(0∼1))− F1⌋y

= K11(ϕ(0∼1))y + K12(ϕ(0∼1))z.

Further, using the above relation and (6.10) again, and observing
Since

L(ϕ(0∼1))K12(ϕ(0∼1))

= −Ao2A−01(ϕ(0∼1))M (ϕ)(F0 + R (ϕ) A0(ϕ(0∼1)))

= −Ao2A−01(ϕ(0∼1))M (ϕ) F0 − Ao2

= −L(ϕ(0∼1))F0 − Ao2,

we have

Ao2 + L(ϕ(0∼1))K12(ϕ(0∼1))

= Ao2 − L(ϕ(0∼1))F0 − Ao2

= −L(ϕ(0∼1))F0.

Thus

z˙ = Ao2z + ΘIIa(ϕ(0∼2))y + L(ϕ(0∼1)) (K11(ϕ(0∼1))y + K12(ϕ(0∼1))z)

= Ao2z + L(ϕ(0∼1))K12(ϕ(0∼1))z + ΘIIa(ϕ(0∼2))y + L(ϕ(0∼1))K11(ϕ(0∼1))y

= (Ao2 + L(ϕ(0∼1))K12(ϕ(0∼1)))z +(ΘIIa(ϕ(0∼2)) + L(ϕ(0∼1))K11(ϕ(0∼1)))y

= (ΘIIa(ϕ(0∼2))+ L(ϕ(0∼1))K11(ϕ(0∼1)))y − L(ϕ(0∼1))F0z

= K21(ϕ(0∼2))y + K22(ϕ(0∼1))z.

These two equations give (4.20). The conclusion holds.

For the case that A0(ϕ(0∼1)) = A0 (ϕ) , we have

L(ϕ(0∼1)) = L (ϕ) = Ao2A−01(ϕ) M (ϕ) , (6.26)

and the above result clearly has the following corollary.

## [74] `odfas_2026_part4` (PDF p.44, L2543) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Choose
AoA−1 ϕ(0∼1)
L] ϕ(0∼1) = [ 0 0 ( )],
( )

where Ao0 is Hurwitz. We have

AoII = [0 0 ]+ L] ϕ(0∼1)) ⌊A0(ϕ(0∼1)) Ir⌋.

## [75] `odfas_2026_part4` (PDF p.46, L2610) | Types: `Observer/Error-Dynamics` | Closer: `The proof is completed.`

Proof. Firstly, it can be easily observed that the above system (7.8) is observable if Assumption
Av1 and Av2 are met. Based on system (7.8), we can design the following observer:

[⃗q1] = AII ϕ(0∼1)) [qˆ1]+[Ir]y
⃗d ( dˆ 0

+L] ϕ(0∼1)) (CII (ϕ(0∼1)) [qˆ1]− w)
( dˆ

= Ao ϕ(0∼1)) [qˆ1]+[Ir]y
II ( dˆ 0

−L(ϕ(0∼1))y˙ + L(ϕ(0∼1))u0, (7.15)

where L(ϕ(0∼1)) ∈ ℝ2r×r is the observer gain.
Secondly, let

z = [qˆ1]+ L ϕ(0∼1) y.
dˆ ( )

Then we have

z = AoII (ϕ(0∼1)) [qˆ1]+[Ir]y + L˙(ϕ(0∼1))y + L(ϕ(0∼1))u0
˙ dˆ 0

= AoII (ϕ(0∼1)) (z − L(ϕ(0∼1))y)+(L˙(ϕ(0∼1)) +[Ir])y + L(ϕ(0∼1))u0
0

= AoII (ϕ(0∼1))z +(L˙(ϕ(0∼1)) − AoII (ϕ(0∼1))L(ϕ(0∼1))+[Ir])y + L(ϕ(0∼1))u0
0

= AoII (ϕ(0∼1))z + ΘIIb(ϕ(0∼2))y + L(ϕ(0∼1))u0.

Thus the observer is finally given by (7.12).
Finally, using (7.5), (7.8), and (7.15), we have

e = AII [q1] +[Ir]y −[⃗q1]
˙ d 0 ⃗d

= AII [q1] − AoII (ϕ(0∼1)) [qˆ1]+ L(ϕ(0∼1))q2 − L(ϕ(0∼1))u0
d dˆ ˙

= AII [q1] − Ao ϕ(0∼1)) [qˆ1]
d II ( dˆ

+L(ϕ(0∼1)) (R (ϕ) A0(ϕ(0∼1))q1 + u0 + R (ϕ) d)− L(ϕ(0∼1))u0

= AII [q1] − AoII ϕ(0∼1)) [qˆ1]+ L] ϕ(0∼1) CII ϕ(0∼1)) [q1]
d ( dˆ ( ) ( d

= Ao ϕ(0∼1)) [q1]− Ao ϕ(0∼1)) [qˆ1]
II ( d II ( dˆ

= AoII (ϕ(0∼1))e. (7.16)

The proof is completed.

In the special case of A0(ϕ(0∼1)) = A0 being a constant matrix, the following result clearly follows

from the above theorem.

## [76] `odfas_2026_part4` (PDF p.48, L2736) | Types: `Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. It follows from Proposition 7.1 that a reasonable output feedback controller for system
(7.3) is given by
u0 = −(F0 + R (ϕ) A0(ϕ(0∼1)))xˆ − F1y − R (ϕ) dˆ

{[qˆ1] = z − L(ϕ(0∼1))y (7.24)
dˆ
z˙ = AoII (ϕ(0∼1))z + ΘIIb(ϕ(0∼1))y + L(ϕ(0∼1))u0.

Firstly, let us show that the above controller GUA stabilizes system (7.3).
Again, using (7.21), we can rewrite (7.3) as

x¨ = R (ϕ) A0(ϕ(0∼1))x + R (ϕ) d + u0

= R (ϕ) A0(ϕ(0∼1))x + R (ϕ) d −(F0 + R (ϕ) A0(ϕ(0∼1)))xˆ − F1y − R (ϕ) dˆ

= −F0xˆ + R (ϕ) A0(ϕ(0∼1))(x −x ˆ) + R (ϕ)(d −dˆ)− F1y

= −F0x + F0 (x −x ˆ) + R (ϕ) A0(ϕ(0∼1))(x −x ˆ) + R (ϕ)(d −dˆ)− F1y

= −F0x − F1x ˙ +⌊F0 + R (ϕ) A0(ϕ(0∼1))⌋(x −x ˆ) + R (ϕ)(d −dˆ)

= −F0x − F1x + Q(ϕ(0∼1))e,
˙

where
Q(ϕ(0∼1)) = ⌊F0 + R (ϕ) A0(ϕ(0∼1)) R (ϕ)⌋.

Therefore, the closed-loop system is given by

x(0∼1) = Φ(F0∼1) x(0∼1) +[ 0 ]Q(ϕ(0∼1))e
{ ˙ Ir (7.25)
e˙ = AoII (ϕ(0∼1))e.

Recall that the second subsystem in (7.25) is GUA stable. Further, recall that Φ (F0∼1) is Hurwitz,
and Q (ϕ) is either uniformly bounded or sublinearly grows with respect to ϕ because of Assumption
A2, we can conclude that the first subsystem in (7.25) is input-to-state stable when e is taken as the
input. Therefore, it follows from Corollary 3.2 that the closed-loop system (7.25) is GUA stable.
Next, let us show that the controller can be equivalently written in the form of (7.22) with Kij (⋅) ,
i, j = 1, 2, being given by (7.23).

Using (7.21) and (7.12), we obtain

u0 = −(F0 + R (ϕ) A0(ϕ(0∼1)))xˆ − F1y − R (ϕ) dˆ

= −⌊(F0 + R (ϕ) A0(ϕ(0∼1))) R (ϕ)⌋ [xˆ]− F1y
dˆ

= −⌊(F0 + R (ϕ) A0(ϕ(0∼1))) R (ϕ)⌋ ⌊z − L(ϕ(0∼1))y⌋− F1y

= −⌊(F0 + R (ϕ) A0(ϕ(0∼1))) R (ϕ)⌋z

−(F1 −⌊(F0 + R (ϕ) A0(ϕ(0∼1))) R (ϕ)⌋L(ϕ(0∼1)))y

= K12(ϕ(0∼1))z −(K12(ϕ(0∼1))L(ϕ(0∼1))+ F1)y. (7.26)

Substituting (7.26) into (7.12), gives

z˙ = AoII (ϕ(0∼1))z + ΘIIb(ϕ(0∼1))y + L(ϕ(0∼1))u0

= AoII (ϕ(0∼1))z + ΘIIb(ϕ(0∼1))y + L(ϕ(0∼1)) (K11(ϕ(0∼1))y + K12(ϕ(0∼1))z)

= AoII (ϕ(0∼1))z + L(ϕ(0∼1))K12(ϕ(0∼1))z + L(ϕ(0∼1))K11(ϕ(0∼1))y + ΘIIb(ϕ(0∼1))y

= (AoII (ϕ(0∼1))+ L(ϕ(0∼1))K12(ϕ(0∼1)))z +(L(ϕ(0∼1))K11(ϕ(0∼1)) + ΘIIb(ϕ(0∼1)))y.

Therefore, (7.22)-(7.23) hold.

Again, in the special case of A0(ϕ(0∼1)) = A0 being a constant matrix, the following result clearly

follows from the above theorem.

## [77] `odfas_2026_part4` (PDF p.54, L3069) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Taking derivative of the second equation in (8.14), and substituting equation (8.12) into
the result and simultaneously using (8.16)-(8.17), yield

RT(φ) ¨x = RT(φ)⌊R˙ (φ) v + R (φ) ˙v† −η ¨∗(t)⌋

= RT(φ) [ ˙φR (φ) Ev + R (φ) [−G[η + u + d] −η ¨∗(t)]
= ˙φEv − G[η + u + d − RT(φ) ¨η∗(t)
= ˙φEy† − G[x + −RT(φ) ¨η∗(t) + u + d

= A0x + fy (y†, φ, t)+ u + d, (8.20)

i.e.,
RT(φ) ¨x = A0x + fy (y†, φ, t) + u + d. (8.21)

Next, it follows from the second equation in (8.12) that

v = RT(φ) (˙η + ˙η∗) .

Then, under the output transformation (8.18) and diffeomorphism (8.14), we have

y = R (φ) v −η ˙∗
= ˙x.

Combining this with (8.21), gives the OD-FAS (8.19).

## [78] `odfas_2026_part4` (PDF p.57, L3259) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Firstly, rewrite R (φ) as

[R0 (φ) 0]
R (φ) = , (8.36)
0 1

[cos φ − sin φ]
R0 (φ) = . (8.37)
sin φ cos φ

Secondly, recall

x = η = [ζ ].
φ

Thirdly, let us define the output vector

y′ = RT(φ) (y + ˙η∗) .

Then

y′ = RT(φ) ( ˙x + ˙η∗)
= RT(φ) [(R (φ) v −η ˙∗) + ˙η∗]
= v

= [ζ ˙ ].
φ˙

Further counting Assumption Aφ in, gives the output equations

y1∗ = ˙ζ,
y2∗ = φ(0∼1).

Based on the above facts, and using the control transformations

u∗i = ui + fyi(y, φ, t) , i = 1, 2, (8.38)

we can decompose system (8.32) into the following two subsystems:

{RT0(φ) ¨ζ = A11ζ + A12φ + u∗1
(8.39)
y1 = ζ,˙

and
{φ¨ = A21ζ + A22φ + u∗2
y2 = φ(0∼1). (8.40)

Further, let

uζ = A12φ + u∗1, (8.41)
uφ = A22φ + u∗2. (8.42)

The above subsystems (8.39) and (8.40) are further written in the forms of (8.34) and (8.35), respec-
tively.

Finally, combining (8.38) with (8.41)-(8.42), gives the control transformation (8.33).

8.4.2. Controller design For output control of subsystem (8.34), Proposition 6.2 (or Corollary

6.2) is readily applied, and the following result is obtained.

## [79] `odfas_2026_part4` (PDF p.59, L3365) | Types: `Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. We need to show that the closed-loop system is GUA stable.
Firstly, it follows from the proof of Proposition 6.2 that the closed-loop system produced by applying
controller (8.43)-(8.45) to system (8.34) is given by

ζ(0∼1) ζ(0∼1)
[ ˙ ] = S (φ)[ ], (8.49)
e˙ e

where

## [80] `scis_2023_delay1` (PDF p.5, L307) | Types: `Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Due to Assumption A, we can obtain (7) from the first equation in (1). Further, taking the
derivatives of both sides of the first equation in (1), we have

x¨1 (t) = ˙α(x1 (t − τj (t))|j=1∼ζ , t)+ B˙1(x1 (t − σj (t))|j=1∼γ, t)x2 (t)

+B1(x1 (t − σj (t))|j=1∼γ, t)x˙2 (t) . (8)

It follows from the second one in (1) that

x˙2 (t) = β(xk (t − τj (t))|j=1∼ζ,k=1,2 , t)

+B2(xk (t − σj (t))|j=1∼γ,k=1,2 , t)u (t) . (9)

Substituting the above equation into (8) yields

x¨1 (t) = ˙α(x1 (t − τj (t))|j=1∼ζ , t)+ B˙1(x1 (t − σj (t))|j=1∼γ, t)x2 (t)

+B1(x1 (t − σj (t))|j=1∼γ, t)β(xk (t − τj (t))|j=1∼ζ,k=1,2 , t)

+B1(x1 (t − σj (t))|j=1∼γ, t)B2(xk (t − σj (t))|j=1∼γ,k=1,2 , t)u (t) . (10)

This can clearly be written into the form of (4)–(6), which turns out to be a system with only the variable
x1 when the x2 related terms therein are converted into x1 related ones by using (7).
Let
𝔽 = (Ω1 × ℝγr) ∩ Ω2 ⊂ ℝ2γr,
and then we clearly have

det B (Y, t) ≠ 0 or ∞ for all Y ∈ 𝔽 and t ⩾ 0. (11)

When this set 𝔽 is not empty, the above relation (11) represents an incomplete full-actuation condition,
and in this case we call the system (4)–(6) a sub-FAS.
In the special case of
Ω1 = ℝγr and Ω2 = ℝ2γr,
we have 𝔽 = ℝ2γr, and the above relation (11) turns into the following complete full-actuation condition:

det B (Y, t) ≠ 0 or ∞ for all Y ∈ ℝ2γr and t ⩾ 0. (12)

In this case we call the system (4)–(6) a (global) FAS.
In fact, based on the form of a usual continuous-time strict-feedback system ([42]), we can further
propose the following strict-feedback system with time delays:

x˙1 (t) = α1(x1 (t − τ1j (t))|j=1∼ζ1 , t)+ B1(x1 (t − σ1j (t))|j=1∼γ1 , t)x2 (t) ,

x˙2 (t) = α2(x1∼2 (t − τ2j (t))|j=1∼ζ2 , t)+ B2(x1∼2 (t − σ2j (t))|j=1∼γ2 , t)x3 (t) ,

...
(13)
{x˙n−1 (t) = αn−1(x1∼n−1 (t − τn−1,j (t))|j=1∼ζn−1 , t)

+ Bn−1(x1∼n−1 (t − σn−1,j (t))|j=1∼γn−1 , t)xn (t) ,

x˙n (t) = αn(x1∼n (t − τnj (t))|j=1∼ζn , t)+ Bn(x1∼n (t − σnj (t))|j=1∼γn , t)u (t) ,

where xi ∈ ℝr, i = 1, 2, . . ., n are the state vectors, u ∈ ℝr is the control vector, τij (t) , j = 1, 2, . . . , ζi,
and σij (t) , j = 1, 2, . . . , γi, i = 1, 2, . . ., n are all nonnegative scalar functions representing the time
delays in the system. Furthermore, αi (·, t) , i = 1, 2, . . ., n are a set of nonlinear vector functions, and
Bi (·, t) , i = 1, 2, . . . , n are a set of matrix functions.
If the following full-actuation condition

det Bi(x1∼i (t − σij (t))|j=1∼γi, t) ≠ 0 or ∞, i = 1, 2, . . . , n (14)

Duan G R Sci China Inf Sci January 2023 Vol. 66 112201:6

is met for all possible values of x1∼i (t − σij (t))|j=1∼γi, i = 1, 2, . . . , n, and t ⩾ 0, then the general time-
delay strict-feedback system can be converted into a high-order FAS. When the above condition (14) is
not met for all, but part of, the possible values of x1∼i (t − σij (t))|j=1∼γi, i = 1, 2, . . . , n, and t ⩾ 0, the
general time-delay strict-feedback system can be still converted into a high-order sub-FAS. A detailed
deduction will be given elsewhere.
In order to demonstrate the multi-layer case, let us give an example.

## [81] `scis_2023_delay1` (PDF p.23, L1492) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Note that

y (0) ∈ 𝔹0 ⇐⇒ κ ‖y (0)‖ ⩽ d =⇒ ‖T y (t)‖ ⩽ d =⇒ ‖T y (t − σ (t))‖ ⩽ d ⇐⇒ T y (t − σ (t)) ∈ 𝔹.

The conclusion immediately follows.
The meaning of the above result is that, in order that the constraint (123) is satisfied it is sufficient
to select the system initial values within the allowable region 𝔹0. Furthermore, it can be easily observed
that, the smaller the number κ is, the larger the allowable region 𝔹0 is. Therefore, the nature in the
above state constrained problem, i.e., Problem 1, is to find a gain matrix K such that the closed-loop
system is stable and meanwhile a smaller κ is provided. This can be done by the well-known parametric
eigenstructure assignment technique with which a parameterization of the feedback gain K that stabilizes
the open-loop system is given, and the design degrees of freedom can be further used to seek a smaller κ.
In the case that v is a nonzero constant, the equilibrium point of the system (112) is

ye = −A−c1Bv. (126)

Let
z = y − ye,

and then the system (112) is transformed into

z˙ = Acz. (127)

Now the relation (124) becomes

‖T (y (t) − ye)‖ ⩽ κ ‖y (0) − ye‖ . (128)

Now applying Theorem 4 to the system (127), we have the following more general result.

Duan G R Sci China Inf Sci January 2023 Vol. 66 112201:24

## [82] `scis_2023_delay1` (PDF p.29, L1911) | Types: `Multi-Conclusion, Lyapunov` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof of conclusion (1).
Let T
V (x) = x P x,
and then by the Lyapunov equation it is easily shown V˙ (x) < 0. Therefore, we have

V (x (t)) = xT(t) P x (t) ⩽ xT(0) P x (0) = V (x (0)) . (A1)

Since

λmin (P ) ‖x (t)‖2 ⩽ xT(t) P x (t) ,
xT(0) P x (0) ⩽ λmax (P ) ‖x (0)‖2,

we have from (A1) λmin (P ) ‖x (t)‖2 ⩽ λmax (P ) ‖x (0)‖2,
which gives
‖x (t)‖ ⩽ λmax (P ) ‖x (0)‖ = ‖P ‖ ‖P−1‖ ‖x (0)‖ .
λmin (P )

Duan G R Sci China Inf Sci January 2023 Vol. 66 112201:30

With this the first conclusion is proven.

## [83] `scis_2023_delay1` (PDF p.30, L1933) | Types: `Multi-Conclusion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof of conclusion (2).
Let Ac = V ΛV−1,
where Λ is a diagonal matrix with the diagonal elements being the eigenvalues of the matrix Ac, and V the eigenvector matrix.
Then we have x (t) = eActx (0) = V eΛtV−1x (0) , (A2)
which gives

‖T x (t)‖ ⩽ ‖T V ‖ V −1 eΛt ‖x (0)‖
‖‖‖ 1‖‖‖‖‖‖ ‖‖‖
⩽ ‖T V ‖ V − ‖x (0)‖ .
‖‖‖ ‖‖‖
With this the second conclusion is also proven.

## [84] `scis_2023_delay1` (PDF p.30, L1944) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof of conclusion (3).
It follows from (A2) that

‖T x (t)‖ ⩽ T V eΛtV −1 ‖x (0)‖
‖‖‖ Λt‖‖‖F−1
= vec(T V e V ‖x (0)‖ . (A3)
‖‖‖ )‖‖‖
Noting that

vec T V eΛtV−1 = V−T⊗ (T V ) vec eΛt
( ) [ ] ( )
eλ1t
eλ2t
= bcs V−T⊗ (T V ) , (A4)
( ) ...
eλnt

where λi, i = 1, 2, . . . , n are the eigenvalues of matrix Ac, we have

eλ1t
eλ2t
vec T V eΛtV−1 ⩽ bcs V−T⊗ (T V )
( ) ‖‖‖ ( )‖‖‖∗‖‖‖‖‖‖‖‖‖‖‖‖ ... ‖‖‖‖‖‖‖‖‖‖‖‖
eλnt

⩽ bcs V−T⊗ (T V ) n e2λit
‖‖‖ ( )‖‖‖∗ ∑i=1
⩽ bcs V−T⊗ (T V ) √n,
‖‖‖ ( )‖‖‖∗
where * represents either 2 or F.
Combining the above relation with (A3) immediately proves this conclusion.

## [85] `scis_2023_delay2` (PDF p.5, L301) | Types: `Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Due to Condition C1, we can obtain (12) from the first equation in (6). Further, taking the
derivatives of both sides of the first equation in (6) gives

x¨1 (t) = ˙α(x1 (t − τj (t))|j=1∼ζ , t)+ B˙1(x1 (t − σj (t))|j=1∼γ, t)x2 (t − δ (t))

+B1 x1 (t − σj (t))|j=1∼γ, t x˙2 (t − δ (t)) . (13)
( )

It follows from the second one in (6) that

x˙2 (t − δ (t)) = β(xk (t − δ (t) − τj (t − δ (t)))|j=1∼ζ,k=1,2 , t − δ (t))

+B2 xk (t − δ (t) − σj (t − δ (t)))|j=1∼γ,k=1,2 , t − δ (t) u (t − δ (t) − h) . (14)
( )

Substituting the above equation into (13) yields

x¨1 (t) = ˙α(x1 (t − τj (t))|j=1∼ζ , t)+ B˙1(x1 (t − σj (t))|j=1∼γ, t)x2 (t − δ (t))

+B1(x1 (t − σj (t))|j=1∼γ, t)β(xk (t − δ (t) − τj (t − δ (t)))|j=1∼ζ,k=1,2 , t − δ (t))

+B1(x1 (t − σj (t))|j=1∼γ, t)

×B2 xk (t − δ (t) − σj (t − δ (t)))|j=1∼γ,k=1,2 , t − δ (t) u (t − δ (t) − h) . (15)
( )

This can clearly be written into the form of (9)-(11), which turns out to be a system with only the variable
x1 when the x2 related terms therein are converted into x1 related ones by using (12).
Due to Conditions C1 and C2, we obviously have

det B (Y, t) ≠ 0 or ∞ for all Y ∈ ℝ2γr and t ⩾ 0. (16)

## [86] `scis_2024_chained1` (PDF p.5, L311) | Types: `Contradiction` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. For simplicity, let

Fi (x0, xi+1∼n, u0, ρi, t) = xi+1ϕ ˆi (·) + ρixiψˆi (·) .

Since

∂Fi
= 0,
∂u
∂Fi
= 0, 1 ⩽ p ⩽ i − 1,
∂xp
∂Fi
= ρiψˆi (·) ,
∂xi
∂Fi ∂ ∂
= ˆϕi (·) + xi+1 ϕˆi (·) + ρixi ψˆi (·) ,
∂xi+1 ∂xi+1 ∂xi+1
∂Fi ∂ ∂
= xi+1 ϕˆi (·) + ρixi ψˆi (·) , i + 1 < q ⩽ n,
∂xq ∂xq ∂xq

and

∂Fi|ρi=u0 ∂ ∂
= xi+1 ϕˆi (·) + u0xi ψˆi (·) ,
∂x0 ∂x0 ∂x0
∂Fi|ρi=x0 ∂ ∂
= xi+1 ϕˆi (·) + xiψˆi (·) + x0xi ψˆi (·) ,
∂x0 ∂x0 ∂x0
∂Fi|ρi=x0 ∂ ∂
= xi+1 ϕˆi (·) + x0xi ψˆi (·) ,
∂u0 ∂u0 ∂u0
∂Fi|ρi=u0 ∂ ∂
= xi+1 ϕˆi (·) + xiψˆi (·) + u0xi ψˆi (·) ,
∂u0 ∂u0 ∂u0

the linearized model of (6) at xi = 0, i = 0, 1, 2, . . ., n, and u0 = 0, u = 0, is obviously given by

x˙0 = u0,
{x˙1 = u, (9)
x˙i+1 = ˆϕoi(t) xi+1, i = 1, 2, . . ., n − 1,

where
ϕˆoi(t) ≜ ϕ ˆi (x0, xi+1∼n, u0, t) |x0∼n=0, u0=0, i = 1, 2, . . ., n − 1.
Since the above linear system (9) is not controllable, the nonlinear system (6)–(8) does not have a
smooth exponentially stabilizing controller.
To proceed, let
u0
u
f (x0∼n, u0, u) = x2ϕ ˆ1 (·) + ρ1x1ψˆ1 (·) .

...
xnϕ ˆn−1 (·) + ρn−1xn−1ψˆn−1 (·)

Then, for an arbitrarily small positive scalar ε, under either condition of the proposition, setting

T
f (x0∼n, u0, u) = 0 0 ε · · · ε ,
[ ]

gives
u0 = u = 0,

and
0 = ε. (10)

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:6

Recall that ε is a positive scalar. The above equation (10) gives a contradiction which states that
the mapping f (x0∼n, u0, u) : ℝn+1 × ℝ × ℝ ↦ ℝn+1 is not a surjection onto an open set containing 0.
Therefore, by the well-known Brockett Theorem [1], under either condition of the proposition, the system
does not have a time-invariant continuous stabilizing controller.

## [87] `scis_2024_chained1` (PDF p.10, L645) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Firstly, as in [12], let us introduce the following transformation:
xi
yi = i−1, i = 1, 2, . . ., n. (36)
x0
Then, noting (24) and

x˙i = xiϕi−1 (·) + γi−1x0xi−1ψi−1 (·) , i = 2, 3, . . ., n,
we have
y˙1 = ˙x1 = u, (37)
and
x˙ixi0−1 − xi (i − 1) xi0−2x˙0
y˙i = 2(i−1)
x0
[xiϕi−1 (·) + γi−1x0xi−1ψi−1 (·)] xi0−1 + (i − 1) βxixi0−1
= 2(i−1)
x0
xi−1ψi−1 (·) (i − 1) βxi + xiϕi−1 (·)
= γi−1 i−2 + i−1
x0 x0
= γi−1ψi−1 (·) yi−1 + [(i − 1) β + ϕi−1 (·)] yi, i = 2, 3, . . ., n. (38)
Combining (37) and (38) gives the following equivalent system of the original system (28):

y˙1 = u,
y˙2 = [β + ϕ1 (·)] y2 + γ1ψ1 (·) y1,
y˙3 = [2β + ϕ2 (·)] y3 + γ2ψ2 (·) y2, (39)
{
...
y˙n = [(n − 1) β + ϕn−1 (·)] yn + γn−1ψn−1 (·) yn−1.

Secondly, applying the following state transformation:

zi = yn−i+1, i = 1, 2, . . . , n, (40)
the above system (39) is equivalently transformed into

z˙1 = [(n − 1) β + ϕn−1 (·)] z1 + γn−1ψn−1 (·) z2,
z˙2 = [(n − 2) β + ϕn−2 (·)] z2 + γn−2ψn−2 (·) z3,

{ ... (41)
z˙n−1 = [β + ϕ1 (·)] zn−1 + γ1ψ1 (·) zn,
z˙n = u,

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:11

which can be further written in the form of (33) with gi (x0, z1∼i, t) and hi (x0, z1∼i, t) , i = 1, 2, . . . , n− 1
defined as in (34) and (35).
Finally, combining the transformations (36) and (40) gives the transformation (32).

## [88] `scis_2024_chained1` (PDF p.12, L799) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. For each z1∼n, Eq. (50) clearly gives a unique z(0∼n−1). Conversely, let z(0∼n−1) be given; then
we have

z1 = z,
z2 = B−1(x0, z1, t) [ ˙z−f1 (x0, z1, t)]
= B−1(x0, z, t) [ ˙z−f1 (x0, z, t)] ,
z3 = B2−1(x0, z1∼2, t) [¨z − f2(x0, z1∼2, t)]

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:13

= B2−1(x0, z(0∼1), t)[¨z − f2(x0, z(0∼1), t)],
· · · .

Therefore, Eq. (50) also gives a unique z1∼n in the way described in Figure 1. Thus the transformation (50)
is one-to-one.
Next, from (34) we have

gi (x0, z1∼i, t) |z1∼n=0 = 0, i = 1, 2, . . ., n − 1, (52)

and

g˙i (x0, z1∼i, t) = ˙ϕn−i (x0, xn−i+1∼n, t) zi
+ [(n − i) β + ϕn−i (x0, xn−i+1∼n, t)] ˙zi, i = 1, 2, . . ., n − 1. (53)

Combining (52) with (33) gives

z˙i|z1∼n=0 = 0, i = 1, 2, . . . , n − 1. (54)

Substituting (52) and (54) into (53) further produces

g˙i (x0, z1∼i, t) |z1∼n=0 = 0, i = 1, 2, . . ., n − 1. (55)

These relations in (55), together with (48), finally yield the relations

fi (x0, z1∼i, t) |z1∼n=0 = 0, i = 1, 2, . . . , n − 1. (56)

Now rewrite the transformation (50) as

0
f1 (x0, z1, t)
z(0∼n−1) = Be(x0, z1∼n−1, t)z1∼n + f2(x0, z1∼2, t) , (57)

...
fn−1(x0, z1∼n−1, t)

where
Be(x0, z1∼n−1, t) = diag (1, B1 (x0, z1, t) , . . . , Bn−1(x0, z1∼n−1, t)) .
With (56), it is clearly seen that the transformation (57), or equivalently (50), keeps the origin unmoved.
Finally, let us prove the conclusion (3). Since gk (x0, z1∼k, t) and hk (x0, z1∼k, t) , k = 1, 2, . . . , n are
differentiable with respect to all variables, from the relations in (56) we can get

lim fi (x0, z1∼i, t) = 0, i = 1, 2, . . . , n − 1. (58)
z1∼n→0

Using (58) and Assumption A3, we have

z1 = z → 0, as z(0∼n−1) → 0,
z2 = B1−1(x0, z1, t) [ ˙z−f1 (x0, z1, t)]
= B1−1(x0, z, t) [ ˙z−f1 (x0, z, t)]
→ 0, as z(0∼n−1) → 0,
z3 = B2−1(x0, z1∼2, t) [¨z − f2(x0, z1∼2, t)]
= B2−1(x0, z(0∼1), t)[¨z − f2(x0, z(0∼1), t)]
→ 0, as z(0∼n−1) → 0,
· · · .

Therefore, following the chart given in Figure 1, we can also get limt→∞ z1∼n = 0. Thus the whole proof
is completed.

Duan G-R Sci China Inf Sci February 2024, Vol. 67, Iss. 2, 122201:14

Figure 1 Solution flow chart.

## [89] `scis_2024_chained1` (PDF p.17, L1041) | Types: `Direct-Substitution` | Closer: `The proof is completed.`

Proof. Firstly, it follows from Corollary 1 that a stabilizing controller for the SFS (65) is given by (71),
which only depends on x0, z1, and z2.
Secondly, note that in this case the state transformation (32) is (64). Therefore, from (35), we have

h (x0, z1, t) = γψ (x0, x2, t) , (78)
x2
g (x0, z1, t) = βz1 + ϕ (x0, x2, t) z1 = [β + ϕ (x0, x2, t)] . (79)
x0
Substituting (64), (78) and (79) into (71) gives

u∗ = b0z1 + b1([β + ϕ (x0, x2, t)] x2 + γψ (x0, x2, t) z2)
x0
x2
= b1γψ (x0, x2, t) x1 + (b0 + b1 [β + ϕ (x0, x2, t)]) . (80)
x0

Therefore, substituting (80) into (71), and incorporating with the controller u0 = −βx0, yield the con-
troller (75) for the original system (62).
When g (x0, z1, t) and h (x0, z1, t) are differentiable with respect to all variables, Eq. (76) can be
immediately derived by (64) and (68).
When ϕ (x0, x2, t) and ψ (x0, x2, t) are differentiable with respect to all variables, substituting (63),
(64), (78), and (79) into (68) gives

d x2
f2(x0, z1∼2, t) = ([β + ϕ (x0, x2, t)] )+ γψ˙ (x0, x2, t) x1
dt x0

= ˙ϕ (x0, x2, t) x2 + γψ˙ (x0, x2, t) x1 + [β + ϕ (x0, x2, t)] x˙2x0 −2 x2x ˙0
x0 x0
x2
= ˙ϕ (x0, x2, t) + γψ˙ (x0, x2, t) x1
x0
1
+ [β + ϕ (x0, x2, t)] (x2ϕ (x0, x2, t) + γx0x1ψ (x0, x2, t) + βx2)
x0
1 2
= ( ˙ϕ (x0, x2, t) + [β + ϕ (x0, x2, t)] )x2
x0
+(γ [β + ϕ (x0, x2, t)] ψ (x0, x2, t) + γψ˙ (x0, x2, t))x1,

which can be arranged into (77).
Finally, let us show the convergence of xi, i = 0, 1, 2. Note that the exponential convergence of x0 is
guaranteed by (25). Since system (72) is stable, z and ˙z converge to zero. Therefore, we can obtain from
either Theorem 3 or Remark 6 that zi, i = 1, 2 also converge to zero. In the end, the convergence of xi,
i = 1, 2 can then be deduced from that of zi, i = 1, 2, and the relation (64). The proof is completed.

## [90] `scis_2024_chained1` (PDF p.21, L1340) | Types: `Equivalence/Homeomorphism` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Following the same line of the proof of Theorem 3, we can show the fact that the transformation
(50) is one-to-one in view of (98), and limt→∞ z1∼n = 0 if limt→∞ z(0∼n−1) = 0. Again, similar to the
proof of the Theorem 2.1 in [36], it can be shown that the transformation (50) turns the SFS (33)–(35)
into the sub-FAS (51) for z1∼n ∈ 𝔽z (x0).
By the FAS theory, the singular set of the sub-FAS (51) is defined to be [41,47,48]

𝕊 = {z1∼n |det Bn (x0, z1∼n, t) = 0, z1∼n ∈ ℝn, t ⩾ 0} ,

which, in view of the expression of Bn (x0, z1∼n, t) in (46) and (47), is obviously coincident with 𝕊z (x0) .

## [91] `scis_2024_chained2` (PDF p.7, L434) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Recalling the definition of σ0 (t) in (19), we have

σ˙0 (t) = −βσ0 (t) . (31)

As in [15], let us introduce the following transformation:
xi
yi = i−1, i = 1, 2, . . . , n. (32)
σ0
Then, noting (22), (31), and

x˙i = xiϕ′i−1(·) + ρi−1 (γi−1, ϑi−1, t) xi−1ψi′−1(·) , i = 2, 3, . . ., n,

we have
y˙1 = ˙x1 = u, (33)
and
x˙iσ0i−1 − xi (i − 1) σ0i−2σ˙0
y˙i = 2(i−1)
σ0
[xiϕ′i−1(·) + ρi−1 (γi−1, ϑi−1, t) xi−1ψi′−1(·)]σ0i−1 (i − 1) βxiσ0i−1
= 2(i−1) + 2(i−1)
σ0 σ0
= (γi−1 − ϑi−1ω) ψi′−1(·) xii−−12 + (i − 1) β + ϕ′i−1(·) xi−i1
σ0 [ ] σ0
= (γi−1 − ϑi−1ω) ψi′−1(·) yi−1 + (i − 1) β + ϕ′i−1(·) yi, (34)
[ ]
i = 2, 3, . . ., n.
Combining (33) with (34), gives the following equivalent system of the original system (25):

y˙1 = u,
y˙2 = [β + ϕ′1(·)] y2 + (γ1 − ϑ1ω) ψ1′(·) y1,
y˙3 = [2β + ϕ′2(·)] y3 + (γ2 − ϑ2ω) ψ2′(·) y2, (35)
{
...
y˙n = (n − 1) β + ϕ′n−1(·) yn + (γn−1 − ϑn−1ω) ψn′−1(·) yn−1.
[ ]
Secondly, applying the following state transformation:

zi = yn−i+1, i = 1, 2, . . . , n, (36)

the above system (35) is equivalently transformed into

z˙1 = (n − 1) β + ϕ′n−1(·) z1 + (γn−1 − ϑn−1ω) ψn′−1(·) z2,
z˙2 = [(n − 2) β + ϕ′n−2(·)]z2 + (γn−2 − ϑn−2ω) ψn′−2(·) z3,
[ ]
{... (37)
z˙n−1 = [β + ϕ′1(·)] zn−1 + (γ1 − ϑ1ω) ψ1′(·) zn,
z˙n = u,

which can be further written in the form of (27) with gi′(ζ0, η0, z1∼i, t), h′i(ζ0, η0, z1∼i, t) , and ∆fi(ζ0, η0,
z1∼i, t), i = 1, 2, . . . , n − 1, defined as in (28)–(30).
Finally, combining the transformations (32) and (36) gives the transformation (26).

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:8

Corresponding to Assumptions A and A′ on the series of functions ψi′(ζ0, η0, xi+1∼n, t) , i = 1, 2, . . . , n−
1, we have the following assumption on the functions h′i(ζ0, η0, z1∼i, t) , i = 1, 2, . . . , n − 1.

## [92] `scis_2024_chained2` (PDF p.8, L535) | Types: `Lyapunov` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Take the continuous function V (x, t) : ℝn× ℝ+ ↦ ℝ as a Lyapunov function for the perturbed
system (38). Using (39)–(42), we have

∂V
V˙ (x, t) = + ∂V (f(x, t) + ∆f(x, t))
∂t ∂x

⩽ −µ3‖x‖µ0 + ∂V ‖∆f(x, t)‖
‖‖‖‖∂x‖‖‖‖
⩽ −µ3‖x‖µ0 + ρv (t) ρ∆(t)‖x‖µ0
µ3 1
⩽ − V (x, t) + ρv (t) ρ∆(t)V (x, t)
µ2 µ1
µ3 1
= (− + ρv (t) ρ∆(t))V (x, t) . (44)
µ2 µ1

Duan G-R Sci China Inf Sci March 2024, Vol. 67, Iss. 3, 132201:9

By the Comparison Lemma (see the Lemma 3.4 of [45]), V (x, t) is bounded above by the solution of
the following first-order linear differential equation:

µ3 1
y˙(t) = (− + ρv (t) ρ∆(t))y(t), (45)
µ2 µ1

with the initial value
y(0) = V (x(0), 0).

Since

t µ3 1
y (t) = y (0) exp(∫ (− + ρv (s) ρ∆(s))ds)
0 µ2 µ1

= y (0) e−µ µ32texp( 1 ∫ tρv (s) ρ∆(s)ds)
µ1 0

⩽ y (0) e−µ µ32texp( 1 ∫ ∞ρv (s) ρ∆(s)ds)
µ1 0
⩽ y (0) eµ11Me−µ µ23t,

we have
V (x, t) ⩽ y (t) ⩽ y (0) eµ11Me−µ µ32t.

This gives, in view of (39),
‖x‖µ0 ⩽ 1 V (x, t) ⩽ ce−µ µ23t,
µ1
where
c = 1 y (0) eµ11M.
µ1
Therefore, system (38) is UGE stable.
Taking µ0 = 2 and ϑ = 21 in the above lemma, immediately gives the following corollary.

## [93] `scis_2024_chained2` (PDF p.10, L630) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof. Firstly, note that the uniform global exponential stability of system (51) and the first condition
in the corollary implies (see the Theorem 4.14 of [45]) the existence of a continuous function V (x, t) :
ℝn × ℝ+ ↦ ℝ that satisfies the inequalities (46)–(48), with ρv (t) being a constant. Therefore, when
Eq. (50) is valid, the conclusion immediately follows from Corollary 1.
Secondly, in view of the fact that the second condition on the global Lipschitz property of f(x, t) is
equivalent to the first condition, the whole proof is completed.

## [94] `scis_2025_chained3` (PDF p.5, L311) | Types: `Contradiction, Multi-Conclusion` | Closer: `The proof is completed.`

Proof. Since, for i = 1, 2, . . ., n − 1,

0, 1 ⩽ k < i,
∂ ρiΨTi(·) , k = i,
∂x [Φi (·) xi+1 + ρiΨi (·) xi] = { T Φi(·) ∂Ψi(·)
k Φi (·) + ∂∂xk xi+1 + ρi ∂xk xi, k = i + 1,
∂∂xΦi(·)xi+1 + ρi∂∂xΨi(·)xi, k > i + 1,
k k

and
∂
[Φi (·) xi+1 + ρiΨi (·) xi] = 0,
∂u
∂ ∂ ∂ρi ∂Ψi (·)
[Φi (·) xi+1 + ρiΨi (·) xi] = Φi (·) xi+1 + Ψi (·) xi + ρi xi,
∂x0 ∂x0 ∂x0 ∂x0
∂ ∂ ∂ρi ∂Ψi (·)
[Φi (·) xi+1 + ρiΨi (·) xi] = Φi (·) xi+1 + Ψi (·) xi + ρi xi,
∂u0 ∂u0 ∂u0 ∂u0
the linearized model of (9) at xi = 0, i = 0, 1, 2, . . ., n, and u0 = u = 0, is obviously given by

x˙0 = u0 + d,
{x˙1 = u, (14)
x˙i = ΦTi−1(0, 0, 0, t)xi, i = 2, 3, . . . , n,

which is clearly not controllable. Further, it can be easily seen that it is (uniformly) asymptotically
stabilizable if and only if
x˙i = ΦTi−1(0, 0, 0, t)xi, i = 2, 3, . . . , n
are (uniformly) asymptotically stable. Thus the first conclusion is proven.
Because of conclusion (1) of Proposition 1, the nonlinear system (9)–(11) does not have a smooth
time-invariant exponentially stabilizing controller.
To proceed with the proof of the third conclusion, let us define

u0
u
f (x0∼n, u0, u) = Φ1 (·) x2 + ρ1 (x0, u0) Ψ1 (·) x1 .

...
Φn−1 (·) xn + ρn−1 (x0, u0) Ψn−1 (·) xn−1

For a set of arbitrarily small positive scalars εi, i = 1, 2, . . . , n − 1, let us set
T
f (x0∼n, u0, u) = 0 0 ε1 · · · εn−1 . (15)
[ ]

Then, we have u0 = u = 0, and

Φi (·) xi+1 + ρi (x0, u0) Ψi (·) xi = εi, i = 1, 2, . . ., n − 1. (16)

If condition (12) is met for some 1 ⩽ i ⩽ n − 1, we immediately have

[Φi (·) xi+1 + ρi (x0, u0) Ψi (·) xi]u0=0 = 0,

Duan G-R Sci China Inf Sci June 2025, Vol. 68, Iss. 6, 162201:6

which, together with (16), produces
0 = εi. (17)
Similarly, when condition (13) is met for 1 ⩽ i ⩽ n − 1, we have

[Φi (·) xi+1 + ρi (x0, u0) Ψi (·) xi]u0=0 = Φi (·) xi+1 + diΓTiu0Ψi(·) xi u0=0 = [Φi (·) xi+1]u0=0 = 0.
[ ]
Again, Eq. (17) is produced from (16).
Recalling that εi is a positive scalar, the above equation (17) gives a contradiction which states that the
mapping f (x0∼n, u0, u) : ℝ(n+1)r×ℝr×ℝr ↦ ℝ(n+1)r is not a surjection onto an open set containing 0.
Therefore, by the well-known Brockett Theorem [1], under either of the two conditions of Proposition 1,
the system does not have a time-invariant continuous stabilizing controller. The proof is completed.
The purpose of the paper is to design a stabilizing controller for the multi-vector nonholonomic system
(9) satisfying Assumptions A1 and A2.

## [95] `tcyb_2023_subfas` (PDF p.3, L338) | Types: `Multi-Conclusion, Lyapunov` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: When the above controller (7) is applied to
system (1), the following asymptotically stable closed-loop
system is obtained:

[x ˙0] = Φ[ x0] (8)
x˙1 x1
where
0
Φ = [ ]. (9)
−a0 − a1

Since the solution of the closed-loop system (8)–(9) is given
by

[x0(t)] = eΦt[ x0(0)] (10)
x1(t) x1(0)
it can be easily seen that the feasibility condition (5) or (6) is
met if and only if

(x0(0), x1(0)) ≠ (0, 0). (11)
Furthermore, since Φ is Hurwitz under the given conditions,
the first conclusion clearly holds.
The second conclusion can be shown similarly to that of
[38, Proposition 3.2].
The fact revealed by this example is interesting and impor-
tant. Normally, when a system is theoretically claimed to be
not stabilizable by state feedback in the Lyapunov sense, the
problem is then considered to be a “dead” one, and people
will turn around and walk away, and choose to investigate
controllers of more complicated structures, such as switched
controllers and time-varying controllers. While the above anal-
ysis tells us that a smooth state feedback controller does exist
which “almost” globally stabilizes the system. How far away is
this almost stabilization from the usual Lyapunov global stabi-
lization? The answer is only the single point of the origin! How
seriously does this prevent the result from the application?

B. Practical Examples

## [96] `tcyb_2023_subfas` (PDF p.5, L646) | Types: `Sufficiency-Necessity` | Closer: `Combining the above two aspects...`

Proof: Sufficiency: Once a system is equivalently converted
into a 0-type sub-FAS in a neighborhood of the origin, denoted
by 𝔹(0), a controller can be immediately constructed by a stan-
dard procedure such that the closed-loop system is a constant
linear closed-loop one on 𝔹(0) with an arbitrarily assignable
eigen-polynomial.
Necessity: Suppose that a state-space system is feedback lin-
earizable on some neighborhood 𝔹(0) (say, in the framework
of Isidori [5]), then, as proven in [53], the system can be con-
verted equivalently into a (global) FAS. In fact, [53] proves the
corresponding conclusion of a general discrete-time nonaffine
nonlinear system, while the proof for the continuous-time case
can be easily carried out almost in the same way.
Combining the above two aspects gives the complete proof
of the result.
The above result clearly has the following two corollaries.

## [97] `tcyb_2023_subfas` (PDF p.7, L854) | Types: `Multi-Conclusion, Direct-Substitution, State-Space-Conversion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: The first two conclusions are obvious. To show the
third condition, we first convert system (32) into the following
state-space form:
x(0∼n−1) = Φ(A0∼n−1)x(0∼n−1)
˙
whose solution is clearly given by
x(0∼n−1)(t) = eΦ(A0∼n−1)tX0 (33)

where X0 = x(0∼n−1)(0) is the initial value.
Substituting (33) into the matrix B(Tx(0∼n−1)(t −
σj(t) )|j=1∼γ , t), gives the following feasibility conditions:

det B(T eΦ(A0∼n−1)(t−σj(t))X0 , t) ≠ 0 (34)
|||j=1∼γ

det B(T eΦ(A0∼n−1)(t−σj(t))X0 , t) ≠ ∞ (35)
|||j=1∼γ
where t ≥ 0. These are obviously constraints on the system
initial value X0. Therefore, the set

⎧ det B(TeΦ(A0∼n−1)(t−σj(t))X0|j=1∼γ , t) ≠ 0 ⎫
Ra = ⎪⎪⎨X0 det B(TeΦ(A0∼n−1)(t−σj(t))X0|j=1∼γ , t) ≠ ∞ ⎪⎪⎬
||||||||
X0 ∈ ℝnr and t ≥ 0
⎪⎪⎩ ⎪⎪⎭
gives the whole set of allowable initial values from which the
trajectories of the closed-loop system converge to the origin.
Further, by definitions of normal and abnormal singu-
larity functions of the sub-FAS (18), the above feasibility
condition (34), (35) can also be written into

ϕ0(T eΦ(A0∼n−1)(t−σj(t))X0 , t) ≠ 0, t ≥ 0
|||j=1∼γ

ϕ∞(T eΦ(A0∼n−1)(t−σj(t))X0 , t) ≠ 0, t ≥ 0
|||j=1∼γ
which is clearly equivalent to

ϕ(T eΦ(A0∼n−1)(t−σj(t))X0 , t) ≠ 0, t ≥ 0. (36)
|||j=1∼γ
This proves Ra = Rs.

B. Decoupled Design
Denote

x(t) = [x1(t)], xi(t) ∈ ℝri, i = 1, 2
x2(t)
and let the following assumption hold.

## [98] `tcyb_2023_subfas` (PDF p.9, L1129) | Types: `Multi-Conclusion, State-Space-Conversion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: The first two conclusions can be easily derived. Here,
we only show the third one.
Since the subsystems in (49) are subject to no singularity
conditions, their initial values are allowed to choose in their
associated whole subspaces. Thus, here, we need only to treat
the constrained subsystem (48).
The linear system in (48) can always be converted into
a state-space form, and particularly in the form of (50).
Therefore
xk(0∼μk−1)(t)|k=1∼q1 = eΦEtX01.

Eventually, we have

xk(0∼μk−1) t − σj(t) |k=1∼q1, j=1∼γ
( )
= (eΦE(t−σj(t))X01)| j=1∼γ

and the feasibility condition in (48) becomes

T(eΦE(t−σj(t))X1)| j=1∼γ ∈ 𝔽 ∀t ≥ 0

which is equivalent to

ϕ(T(eΦE(t−σj(t))X1 , t) ≠ 0 ∀t ≥ 0.
)|||j=1∼γ
This condition clearly determines the initial values from which
the solution of the closed-loop system converges to the origin.
Hence, R0m forms the whole region of attraction.

## [99] `tcyb_2023_subfas` (PDF p.11, L1400) | Types: `Multi-Conclusion, State-Space-Conversion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: The state-space form of system (65) is clearly
given by

x1(0∼2) = Φ(a0∼2)x1(0∼2). (73)
˙
Further, it follows from a typical result on eigenstructure
assignment (see [40], [44], [49]) that, when a0∼2 is given as
in (69) and (70), there holds

Φ(a0∼2) = Vdiag −s1, − s2, − s3 V−1.
( )
Hence, the solution to system (73) is given by
x(0∼2)(t) = Vdiag e−s1t, e−s2t, e−s3t V−1x(0∼2)(0)
e−(s1t e−s2t e )−s3t
= ⎡−s1e−s1t − s2e−s2t − s3e−s3t⎤X0
⎣ s21e−s1t s22ee−s2t s23e−s3t ⎦

where

X0 = V−1x1(0∼2)(0). (74)

Particularly, we have

x1(t) = e−s1t e−s2t e−s3t X0.
[ ]
Therefore, the singularity condition (68) becomes
e−s1(t−σ) e−s2(t−σ) e−s3(t−σ) X0 = e−γ (t−σ) + 1
[ ]
which becomes (72) when denoting

X0 = [x0 y0 z0]T.

Finally, noting that (71) can be obtained from (74), we
complete the proof of the first conclusion.
When the system initial values are chosen within the
ROEA, all the state variables converge to the origin expo-
nentially. Therefore, the vector u′(t) in (63) converges to zero
exponentially.
Further, note from (61) that

B−1(x1(t − σ), t) = − 1 adjB(x1(t − σ), t). (75)
g(x1(t − σ), t)
When g(x, t) is given by (67), there holds

lim g(x, t) = lim x(t) − e−γ t − 1 = −1. (76)
t→∞ t→∞( )
We can then conclude from (75) and (76) that

lim B−1(x1(t − σ), t) = C (77)
t→∞
is a constant matrix. Since x(0∼2) , y1, and y(0∼1) all converge
3
to zero, it can be easily proven that f2(·, t), h1(·), and h2(·)
all converge to zero. Therefore, it follows from (63) that u′(t)
converges to zero, and so is

u(t) = −B−1(x1(t − σ), t)u′(t).

With this, we complete the whole proof.
Obviously
e−s1(t−σ)x0 + e−s2(t−σ)y0 + e−s3(t−σ)z0 = e−γ (t−σ) + 1 (78)

represents a plane determined by the following three points:

(ω1(t), 0, 0), (0, ω2(t), 0), (0, 0, ω3(t))

where

ωi(t) = e−(γ −si)(t−σ) + esi(t−σ), i = 1, 2, 3.

In the case of min{si, i = 1, 2, 3} > γ, we have

ωi(0) = e(γ −si)σ + e−siσ ≤ ωi(t) ≤ ∞ = ωi(∞).

Thus, the region of attraction of the closed-loop subsys-
tem (65), with the singularity condition (68), is as follows:
es1σx0 + es2σy0 + es3σz0 < eγ σ + 1
⎧ es1σx0 + es2σy0 < eγ σ + 1 ⎫
ℚ = ⎪⎪⎨(x0, y0, z0) es1σx0 + es3σz0 < eγ σ + 1 ⎪⎪⎬.
||||||||
es2σy0 + es3σz0 < eγ σ + 1
⎪⎪⎩ ⎪⎪⎭
This region is illustrated in Fig. 1.

Fig. 1. Region of attraction.

Fig. 2. State variables.

Fig. 3. Input variables.

In our simulation, the closed-loop parameters are chosen as
c0 = 2 and c1 = b = 3, and the time delays are chosen as

σ = 4, γ = 3, τ1 = 1, τ2 = 2, τ3 = 3
δ1(t) = 0.5|sin t|, δ2(t) = e−t
δ3(t) = 1 + cos 2t, δ4(t) = 0.5.

With the following initial value functions:

y1(s) = 2, y3(s) = 1, ˙y3(s) = −3, s ≤ 0

the simulation of the system is carried out and the results are
shown in Figs. 2 and 3.

## [100] `ucfas_2025_part2` (PDF p.17, L1691) | Types: `Direct-Algebraic/Citation` | Closer: `QED-symbol-only (□/▪)`

Proof: Under given conditions, we have

1
x3 =
s2 − s1
]
× [s2e−s1t − s1e−s2t e−s1t − e−s2t] [x30 .
x3d

To treat constraint (96), let us first consider the condi-
tion x3 = 0, which is equivalent to

(e−s1t − e−s2t)x3d = (s1e−s2t − s2e−s1t)x30,

t ≥ 0.

Write the above equation into the following form

x3d = k (t) x30, t > 0,

where
s1e−(s2−s1)t − s2
k (t) = 1 − e−(s2−s1)t .

Noticing

k (0) = −∞, k (∞) = −s2,

and k(t) is an increasing function, we know that x3 =
0 if and only if (x30, x3d) is chosen within the area
between the x3d axis and the line

x3d + s2x30 = 0.

The conclusion therefore holds. ■

Figure 3. Illustration of RoEA Rexb.

An illustration of the RoEA Rexb is given in Figure 3.
Finally, the overall RoEA of the constrained system is
given by

R0nh = Rina ⊕ Rexb
⎧⎡ ⎤ ⎫
⎨ x10 x10 ≠ 0, ⎬
= ⎣x30⎦ x3d + s2x30 > 0, ,
⎩ |||||| ⎭
x3d x30 > 0

where ⊕ represents the direct sum.
To summarise, the designed controller is given
by (120), which produces the closed-loop system (121).
As long as the initial value (x10, x30, x3d) is chosen
from R0nh, the controller works and the closed-loop
response converges to zero exponentially while satis-
fying constraint (96).
Once x1(t), x3(t) and ˙x3(t) are obtained, x2(t)
can be obtained from (103). It can be clearly noted
from (120) that ˙x3 should be made convergent faster
than e−at, by properly selecting b0 and b1, so as to
guarantee the convergence of x2 and u2.
To conclude this section, let us mention sub-
stabilisation of UC-FASs (109).
Due to the equivalence relations stated in Exam-
ple 4.1, a sub-stabilising controller for UC-FAS (109)

can be immediately given by
⎧
u1 = −ax1 − ϕ (x1, x3, t)

⎪⎪⎪⎪⎪⎪⎨u2 = − 1
[b2(x3, x10, t) ( )] (123)
× b0x3 + b1x˙3 + f x3(0∼1), x10, t

⎪⎪⎪⎪⎪⎪⎩x10 ∈ R0nh,

which produces the closed-loop system
{
x˙1 + ax1 = 0
(124)
x¨3 + b1x˙3 + b0x3 = 0.

In the special case of ϕ(x1, x3, t) = 0, we can get
( )
f x3(0∼1), x10, t = −ax˙3,

b2(x3, x10, t) = a2e−2atx102.

Thus the controller (123) reduces to
⎧
u1 = −ax1
⎪⎪⎪⎨ 1 2at
u2 = − 2 2 e (b0x3 + b1x˙3 − ax˙3) (125)
a x10
⎪⎪⎪⎩x10 ∈ R0nh,

which produces the same closed-loop system as
in (124).
Sub-stabilisation of UC-FAS (110) can be similarly
realised, either by using the equivalence relation, or by
direct deduction.

## [101] `ucfas_2025_part3` (PDF p.6, L491) | Types: `Direct-Substitution, Equivalence/Homeomorphism` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof: A proof of the above theorem is given by
showing

Model II ⇐⇒ Model I ⇐⇒ Model V
⇕ ⇕
Model III Model IV

(a) Equivalence Between Models I and II

Using the one-to-one state transformation T1:
q1∼2 ↦ x1∼2 (Olfati-Saber, 2002; Ye et al., 2007;
Zavala-Rio et al., 2003):
{
x1 = q2 + ε(cos γ − 1)
(25)
x2 = −q1 + ε sin γ ,

and

θ = γ ,

we can obtain
⎧ 2
⎨x¨1 = ¨q2 − εγ ˙ cos γ − εγ ¨ sin γ
x¨2 = −¨q1 − εγ ˙2sin γ + εγ ¨ cos γ (26)
⎩
θ¨ = ¨γ .

Substituting Model II into (26) gives

⎧⎨x¨1 = F1 cos γ + gq((q1∼2)(0∼1), t) − εγ ˙2cos γ
x¨2 = F1 sin γ + hq((q1∼2)(0∼1), t) − εγ ˙2sin γ
⎩
θ¨ = F2.
(27)
Further, introduce the new control variables

v = F1 − εγ ˙2, w = F2.

System (27) can then be arranged into the form of
Model I, with

g(x1(0∼∼21), t) = gq((T1−1(x1∼2))(0∼1), t),

h(x1(0∼∼21), t) = hq((T1−1(x1∼2))(0∼1), t).

(b) Equivalence Between Models I and V
Under condition (24), we can introduce a one-to-
one transformation T2: (x1∼2, θ) ↦ z1∼3, given by
⎧
⎨z1 = x1
z2 = tan θ (28)
⎩
z3 = x2.

Then we have
⎧
⎪⎪⎨z¨1 = ¨x(1 )
z¨2 = d tan2 θ θ˙2 + (1 + tan2θ)θ ¨ (29)
dθ
⎪⎪⎩
z¨3 = ¨x2.

Substituting Model I into (29) yields

⎧ (0∼1)
z¨1 = ( v cos θ + g()x1∼2 , t)
⎪⎪⎨ d
z¨2 = tan2 θ θ˙2 + (1 + tan2θ)w (30)
dθ
⎪⎪⎩ (0∼1)
z¨3 = v sin θ + h(x1∼2 , t).

Further, substituting the new control variables
⎧
⎨u1 = ( v cos θ )

⎩u2 = d tan2 θ θ˙2 + (1 + tan2θ)w
dθ

into (30), produces Model V, with

gz(z(0∼1), z(0∼1), t) = g(z(0∼1), z(0∼1), t),
1 3 1 3
hz(z(0∼1), z(0∼1), t) = h(z(0∼1), z(0∼1), t).
1 3 1 3
(c) Equivalence Between Models II and III
Define
[ ]
− sin θ cos θ
G(θ) = .
cos θ sin θ

Then it is easy to verify G−1(θ) = G(θ). Let
[ ] [ ]
u1 F1
= G(θ)
u2 εF2
[ ]
−F1 sin θ + εF2 cos θ
= . (31)
F1 cos θ + εF2 sin θ

We can obtain
[ ] [ ]
F1 u1
= G(θ)
εF2 u2
[ ]
u2 cos θ − u1 sin θ
= .

## [102] `ucfas_2025_part3` (PDF p.8, L724) | Types: `Direct-Substitution` | Closer: `QED-symbol-only (□/▪)`

Proof: Taking the differential of the third equation
in (37) gives

...z = ˙yu1 + yu˙1 + ˙h((x, z)(0∼1), t), (45)

z(4) = ¨yu1 + 2y˙u˙1 + yu¨1

+ h¨((x, z)(0∼1), t). (46)

Combining Equation (45) with the third equation
in (37) gives
[ ] [ ] [ ]
u1 0 y ϖ0(·)
= , (47)
u˙1 u1 y˙ ϖ1(·)

where ϖ0(·) and ϖ1(·) are given by (41) and (42),
respectively. Using (47), we immediately get (43)
and (44) under u1 ≠ 0 (will be guaranteed in the
design).
Substituting the second equation in (37), and
also (43) and (44), into (46), gives

z(4) = f0(x(0∼3), z(0∼3), u(10∼2)) + u1u2, (48)

where

f0(·) = 2y˙u˙1 + yu¨1 + h¨((x, z)(0∼1), t)
( )
u˙1 u˙1
= 2 ϖ1(·) − ϖ0(·)
u1 u1

+ u¨1ϖ0(·) + h¨((x, z)(0∼1), t),
u1

which gives (40). Combining (48) with the first
equation in (37) yields the UC-FAS (39). ■

System (39) is obviously a strongly UC-FAS. How-
ever, if we introduce the following control transforma-
tion:

u′1 = g((x, z)(0∼1), t) + u1,

then the strongly UC-FAS (39) is turned into the fol-
lowing weakly UC-FAS:
⎧
⎨x¨ = u′1
z(4) = f (x(0∼3), z(0∼3), (u′1)(0∼2), t) (49)
⎩ +b((x, z)(0∼1), u′1, t)u2,

where

f (x(0∼3), z(0∼3), (u′1)(0∼2), t)

= f0(x(0∼3), z(0∼3), (u′1 − g(·, t))(0∼2)), (50)

b((x, z)(0∼1), u′1, t)

= u′1 − g((x, z)(0∼1), t). (51)

## [103] `book_2026_volume1` (PDF p.84, L64) | Types: `Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Firstly, according to Proposition 2.1, system (2.66) is controllable if and only
if the coordinate transformation x = P x̄, with. P given by (2.68) being invertible, and
under which system (2.66) is reduced into the Luenberger controllability canonical
form (2.69)–(2.70).
Secondly, rewrite the above the Luenberger controllability canonical form (2.69)–
(2.70) into the form of
⎧
⎪
⎪ x̄˙1 = x̄2
⎪
⎪  ˙
⎨ x̄2 = x̄3
⎪
.                                                          (2.72)
⎪       .
⎪
⎪  ˙n−1 = x̄n
⎪
⎪ x̄
⎩˙
x̄n = −α0 x̄1 − α1 x̄2 − · · · − αn−1 x̄n + u.
If we denote z = x̄1 , then the first n − 1 equations of (2.72) yield
x̄ = z (i−1) , i = 1, 2, . . . , n.
i                                                   (2.73)
Substituting (2.73) into the last equation of (2.72) gives FAS (2.71). Finally, in view
of the fact that the above process is invertible, the proof is completed. .
The above result states that the above single-order FAS (2.71) can be viewed as a
controllability canonical form for the single-input LTI (2.66).
2.4 Linear Time-Invariant FASs                                                      65
Multi-input case
Let us consider the LTI multi-input system
ẋ = Ax + Bu,                      (2.74)
where x ∈ Rn and u ∈ Rr are the state vector and the input vector, respectively, and
A ∈ R      , B ∈ Rn×r are the system matrices.
n×n
In parallel to Proposition 2.1, we have the following result.

## [104] `book_2026_volume1` (PDF p.87, L67) | Types: `Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Firstly, according to Proposition 2.2, system (2.74) is controllable if and only
if it can be equivalently the coordinate transformation x = P x̄, with P given by
(2.80) being invertible, and under which system (2.74) is reduced into the Luenberger
controllability canonical form (2.75)–(2.76).
Secondly, in accordance with canonical form (2.75)–(2.76), the state vector x̂ and
the control vector u can be partitioned into
⎡⎤     ⎡ ⎤
x̂1         u1
⎢ x̂2 ⎥     ⎢ u2 ⎥
⎢ ⎥         ⎢ ⎥
x̂ = ⎢ . ⎥ , u = ⎢ . ⎥ ,
⎣ .. ⎦      ⎣ .. ⎦
x̂r                ur
with
∈ Rμi
T
x̂ = x̂i1 x̂i2 · · · x̂iμi
i
68                                                                               2 Models of Global FASs
and μi , i = 1, 2, . . . , r, satisfying
μ1 + μ2 + · · · + μr = n.
Thus we can rewrite (2.75)–(2.76) into the following explicit forms:
⎧
⎪
⎪ x̂˙k1 = x̂k2
⎪
⎪
⎪
⎪
⎪ x̂˙k2 = x̂k3
⎪
⎨         ..
(2.85)
⎪ x̂˙k,μ −1 = x̂kμ
⎪
⎪
⎪          k       k
⎪
⎪  ˙kμ = − μk α i−1 x̂ki − r                μi        j−1
⎪
⎪ x̂                                         j=1 αki x̂ i j
⎩       k         i=1 kk
r
i=1,i k
+u k + l=k+1 bkl u l , k = 1, 2, . . . , r.
It then follows from the first μk − 1 equations of (2.85) that the following relations
hold:                     ⎧
⎪
⎪ x̂k2 = x̂˙k1
⎪
⎨ x̂k3 = x̂¨k1
⎪      ..                                              (2.86)
⎪
⎪       .
⎩            (μk −1)
x̂kμk = x̂k1       , k = 1, 2, . . . , r,
Substituting the above into the last equation of (2.85) gives
μk
(μk )             i−1 (i−1)
x̂ k1    =−         αkk x̂k1
i=1
r      μi                                 r
j−1 ( j−1)
−                      αki x̂i1       + uk +           bkl u l , k = 1, 2, . . . , r. (2.87)
i=1,i k j=1                               l=k+1
Finally, define
z = x̂k1 , k = 1, 2, . . . , r.
k
Combining this with the equations in (2.86) gives transformation (2.84), or
equivalently,
( j−1)
x̂ k j = z k      , j = 1, 2, . . . , μk , k = 1, 2, . . . , r. (2.88)
Substituting these into Eq. (2.87) produces the multi-order FAS (2.81). Note that the
above process is invertible. The proof is then completed. .
Suppose there are η (.η ≤ r ) number of distinct integers among μk , k =
1, 2, . . . , r, which are assumed, without loss of generality, to be μk , k = 1, 2, . . . , η.
By combining together the equations with the same maximum differential order in
(2.81), we can write the linear FAS (2.81) into the following multi-order global FAS:
2.4 Linear Time-Invariant FASs                                                                 69
−1)
z k(μk )           = L̂ z k(0∼μk                  + B̂u,      (2.89)
k=1∼η                         k=1∼η
which can also be more explicitly written as
⎡ (μ ) ⎤ ⎡                  −1)    ⎤
z1 1        L̂ 1 z k(0∼μk |k=1∼η
⎢ (μ2 ) ⎥ ⎢
⎢ z 2 ⎥ ⎢ L̂ 2 z k k |k=1∼η ⎥
(0∼μ −1)
⎥
⎢       ⎥ = ⎢                      ⎥ + B̂u,
⎢ .. ⎥ ⎣                   ..
⎦
(2.90)
⎣ . ⎦                       .
(μ )

## [105] `book_2026_volume1` (PDF p.105, L85) | Types: `Equivalence/Homeomorphism` | Closer: `The proof is completed.`

Proof Suppose that, under x̂ = T −1 (x) and (2.133), system (2.132) can be converted
into the LTI system (2.134) with (A, B) controllable. Then, by Theorem 2.2, we
further know that there exists a state homeomorphism transformation of the following
form:
(0∼μk −1)
zk            = P x̂,                       (2.137)
k=1∼η
where P is an invertible matrix, under which the controllable LTI system (2.134) can
be equivalently converted into a global FAS in the form of
−1)
z k(μk )           = L̂ z k(0∼μk                 + B̂v,                 (2.138)
k=1∼η                         k=1∼η
86                                                                                     2 Models of Global FASs
where L̂ ∈ Rr ×n and B̂ ∈ Rr×r are two constant matrices, but with B̂ being
nonsingular.
Noting
(0∼μk −1)
zk          = P T −1 (x) ,                   (2.139)
k=1∼η
we have
−1)
x=T     P −1 z k(0∼μk                     ,
k=1∼η
and
v = β −1 (x) u − β −1 (x) α (x)
−1)
= β −1 T         P −1 z k(0∼μk
k=1∼η
−1)
× u−α T              P −1 z k(0∼μk                         (2.140)
k=1∼η
Therefore, system (2.132) can be equivalently converted by (2.133) and the
variable transformation (2.139) into (2.135), with
−1)
fz   z k(0∼μk
k=1∼η
−1)
= L̂ z k(0∼μk
k=1∼η
−1)                                             −1)
−β −1 T          P −1 z k(0∼μk                     α T           P −1 z k(0∼μk                 ,
k=1∼η                                          k=1∼η
and Bz (·) being given by (2.136).
Finally, noting the one-to-one property of T (·) and β (·) , and the nonsingularity
of P, we can immediately conclude that Bz (x) is invertible for all x ∈ Rn Thus
(2.135) is a global FAS. The proof is completed. .
2.6.2 Nonaffine Systems
Consider the nonlinear system
ẋ = f (x, u) ,                                         (2.141)
where x ∈ Rn and. u ∈ Rr are the state vector and input vector, respectively,. f (·) ∈
Rn is a sufficiently smooth function satisfying the initial condition f (x0 , u 0 ) = ẋ0 .
Regarding when system (2.141) is locally equivalent to a controllable linear system,
we introduce the following definition (Van Der Schaft, 1984).
2.6 Feedback Linearizable Systems                                                                                  87

## [106] `book_2026_volume1` (PDF p.154, L135) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Write Eq. (4.30) as
( A0∼n−1 ) V = V F.             (4.33)
Further, introducing the variable
W = −A0∼n−1 V,                  (4.34)
and in view of
(A0∼n−1 ) =                 (00∼n−1 ) − Bc A0∼n−1 ,    (4.35)
we can convert equivalently the above Eq. (4.33) into the form of (4.26). Therefore,
it follows from Lemma 4.1 that all the matrices V and W are given by (4.27), and
Eq. (4.31) can then be further solved from (4.34).

## [107] `book_2026_volume1` (PDF p.155, L136) | Types: `Direct-Substitution, Lyapunov, State-Space-Conversion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof When control law (4.19), with. A0∼n−1 chosen as in (4.31), is applied to system
(4.18), the closed-loop system can be obtained and rewritten in the state-space form
(4.23). It follows from Theorem 4.1 that (4.30) holds. Thus, substituting (4.30) into
(4.25), yields
−1 −1
G dy (s) = C V (s I − F)   V Bc E.                    (4.41)
Considering that the matrix F is Hurwitz, there exist unique positive definite
solutions P1 and P2 satisfying the Lyapunov equations
F P1 + P1 F T = −V −1 Bc E E T BcT V −T ,                            (4.42)
and
F T P2 + P2 F = −V T C T C V,                             (4.43)
respectively. According to Lemma 4.3, the matrices. P1 and. P2 given by (4.39)–(4.40)
are respectively the solutions to the Lyapunov equations (4.42) and (4.43). Therefore,
2
it follows from Lemma 4.2 that G dy (s) 2 is given by (4.38)–(4.40). The proof is
then completed.
4.3 Asymptotical Disturbance Decoupling                                              137
With the help of the above two theorems, the solution to the disturbance attenuation
problem in system (4.18) via controller (4.19) can then be founded by optimizing the
2
design parameters F and Z to minimize G dy (s) 2 Clearly, an advantage of the
parametric approach is that it is easy to have additional indices to be comprehensively
optimized together with this H.2 index.
In applications, it suffices to choose F to be a diagonal matrix with negative
diagonal elements. In the case that complex eigenvalues are expected, we may have
such a block
−a −b
,                              (4.44)
b −a
with a and b being two positive scalars, included as a diagonal block in F.
Clearly, there are quite some degrees of freedom (DOFs) in the selection of F,
while on the other hand, we also have the parameter matrix Z , which provides r 2 n
DOFs. All these DOFs can be further utilized to achieve additional performance of
the system (Duan, 1992a, 1993a; Duan et al., 2000; Duan & Zhao, 2020).
4.3 Asymptotical Disturbance Decoupling
Adding two output equations to system (4.12), and replacing the state x (0∼n−1) in the
system with the measured output ym , give the following FAS:
⎧
⎨ x (n) = f (ym , ζ, t) + B (ym , ζ, t) u + Ed (0∼k−1) (t)
ym = Cm x (0∼n−1)                                              (4.45)
⎩
yr = Cr x (0∼n−1) + Er d (0∼k−1) (t) ,
where. ym ∈ Rm 1 is the measured output,. yr ∈ Rm 2 is the regulated output,.Cm ,.Cr and
E r are the coefficient matrices of appropriate dimensions, and the disturbance d ∈ R
p
is generated by the exogenous system (4.13), or equivalently, the state-space system
(4.14).
In this section, asymptotical disturbance decoupling in the above system (4.45) is
considered via dynamical output feedback. The aim is to find a control law, employing
the feedback of the measured output. ym , for the given FAS (4.45) with the disturbance
d generated by the exogenous system (4.13), such that the following asymptotical
output regulation requirement
lim yr (t) = 0                            (4.46)
t→∞
is met for arbitrary initial values x (0∼n−1) (0) , ζ (0) and d (0∼k−1) (0) .
To solve this problem, we also need some preliminary results.
138                                                  4 Disturbance Attenuation and Decoupling
4.3.1 Preliminary Results
Let us first state a result about disturbance decoupling in linear systems.
Disturbance decoupling in linear systems
Consider the following linear system:
⎧
⎨ ẋ = Ax + Bu + E w w
y = Cy x                                      (4.47)
⎩
e = Ce x + Dew w,
where E w , C y , Ce , and Dew are known matrices of appropriate dimensions; x ∈ Rn
and. u ∈ Rr are the state and the control input, respectively; y ∈ Rm 1 and e ∈ Rm 2 are
the measured output and the regulated output, respectively;.w ∈ R p is the disturbance
generated by the exogenous system
ẇ = Sw,                                (4.48)
where the matrix S is usually not Hurwitz since otherwise the disturbance w dies
out itself. Furthermore, the system coefficient matrices are assumed to satisfy the
following conditions.

## [108] `book_2026_volume1` (PDF p.159, L140) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Obviously, the homogeneous equation of the above GSE (4.55) is Eq. (4.26).
Let (V, W ) be a general solution to the homogeneous GSE (4.26), and ( 0 0 ) be
a particular solution to the above GSE (4.55), then it is easily known that the general
solution (     ) to the above nonhomogeneous equation (4.55) is given by
=       0+V        =    0 + W.                         (4.57)
It follows from Lemma 4.1 that a general solution to the homogeneous GSE (4.26)
is given by (4.27). Further, it can be easily verified that a particular solution to the
above nonhomogeneous GSE (4.55) is given by
0 =0      0 = R.                               (4.58)
Therefore, the general solution (4.56) immediately follows from (4.27), (4.57) and
(4.58).
4.3.2 Parametric Solution
It is obvious that ( (00∼n−1 ) , Bc ) is controllable. Further denote
(00∼n−1 )     Bc E
E =                                 , C E = Cm 0 ,                    (4.59)
0          (S0∼k−1 )
then we also need the following assumption:

## [109] `book_2026_volume1` (PDF p.161, L142) | Types: `State-Space-Conversion` | Closer: `Thus the conclusion follows.`

Proof If we take the following control law
u = −B −1 (ym , ζ, t) ( f (ym , ζ, t) − v) ,
(4.67)
then the corresponding closed-loop system is given by
⎧ (n)
⎨ x = Ed (0∼k−1) + v
ym = Cm x (0∼n−1)                                       (4.68)
⎩
yr = Cr x (0∼n−1) + Er d (0∼k−1) .
The above Eq. (4.68) can be also equivalently rewritten in the following state-space
form:        ⎧ (0∼n−1)
⎨ ẋ       = (00∼n−1 ) x (0∼n−1) + Bc v + Bc Ed (0∼k−1)
ym = Cm x (0∼n−1)                                              (4.69)
⎩
yr = Cr x (0∼n−1) + Er d (0∼k−1) .
It is noted that the above (4.69) is now an LTI system. Applying Lemma 4.4
to the above system (4.69), we can design the following controller v to meet the
asymptotical output regulation requirement (4.46):
⎧
⎪
⎪ x̂˙ (0∼n−1)          (00∼n−1 )         Bc E        x̂ (0∼n−1)   Bc
⎪
⎪               =                                               +    v
⎪
⎪
⎪ d̂˙ (0∼k−1)            0              (S0∼k−1 )    d̂ (0∼k−1)   0
⎨
Lx
⎪             +        Cm x̂ (0∼n−1) − ym                                       (4.70)
⎪
⎪                L d
⎪
⎪                               x̂ (0∼n−1)
⎪
⎪
⎩ v = −K 0∼n−1 + K 0∼n−1                   ,
d̂ (0∼k−1)
where the matrices L x and L d satisfy the first condition in the theorem, K 0∼n−1
makes the matrix (K 0∼k−1 ) stable, while and are two matrices satisfying the
equations
(00∼n−1 ) + Bc =              (S0∼k−1 ) − Bc E,              (4.71)
and
Cr        + Er = 0.                              (4.72)
Combining the above controller (4.70) with (4.67) gives controller (4.60). Further,
it is easy to see that the following three facts hold:
1. according to Theorem 4.1, the matrix K 0∼n−1 which makes (K 0∼k−1 ) stable
is given by (4.61) with the parameter F1 Hurwitz and the parameter matrices F1
and Z 1 satisfying the condition detV (F1 , Z 1 ) = 0;
4.3 Asymptotical Disturbance Decoupling                                                143
2. applying Lemma 4.5, with F and R substituted by (S0∼k−1 ) and .−E, respec-
tively, it is easily proven that the matrices and given by (4.62) satisfy the
above nonhomogeneous GSE (4.71); and
3. with the matrices and given by (4.62), the matrix Eq. (4.72) is equivalent
to condition (4.64).
With the above three facts, we immediately have the conclusion of the
theorem.

## [110] `book_2026_volume1` (PDF p.162, L143) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof In view of the expression of Bc given in (4.22), we have
s Inr+kp − E
rank
CI
⎡                                     ⎤
s Inr − (00∼n−1 )        −Bc E
= rank ⎣           0       s Ikp − (S0∼k−1 ) ⎦
Inr              0
⎡                       ⎤
0           Bc E
= rank ⎣ 0 s Ikp − (S0∼k−1 ) ⎦
Inr           0
144                                                             4 Disturbance Attenuation and Decoupling
⎡            ⎤
0        0
⎢ 0         E         ⎥
= rank ⎢                     ⎥
⎣ 0 s Ikp − (S0∼k−1 ) ⎦ , ∀s ∈ C.                                       (4.74)
Inr       0
This implies
s Inr+kp −        E
rank
CI
s Ikp −        (S0∼k−1 )
= nr + rank                                 , ∀s ∈ C.                 (4.75)
E
Therefore, the conclusion holds according to the well-known PBH (Popov-Belevitch-
Hautus) criterion.
If the matrix pair ( (S0∼k−1 ) , E) is observable, then it follows from Duan
(2015) that there exists a pair of polynomial matrices N (s) ∈ Rkp×nr [s] and
nr ×nr
D (s) ∈ R        [s] satisfying the following generalized right coprime factorization
(RCF):
s Ikp −     (S0∼k−1 ) N (s) = E T D (s) .
T
(4.76)
If we denote D (s) = di j (s) and
ω = max deg di j (s) , i, j = 1, 2, . . . , nr ,
(4.77)
then N (s) and D (s) can be written in the form of
⎧            ω
⎪
⎪
⎪ N (s) =
⎪               Ni s i , Ni ∈ Rkp×nr
⎨
i=0
ω                                                (4.78)
⎪
⎪
⎪                                     nr ×nr
⎩ D (s) =          Di s , Di ∈ R               .
i
⎪
i=0
With the above preparations, the following result can be stated.

## [111] `book_2026_volume1` (PDF p.164, L145) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof If we take
D (s)
N̂ (s) =                                 (4.83)
N (s)
and
D̂ (s) = s Inr −                    T
(00∼n−1 ) D (s) ,      (4.84)
then it can be easily verified using relation (4.76) that
s Inr+kp −              T
E    N̂ (s) = C IT D̂ (s) (4.85)
Further note that
⎡                                            ⎤
D (s)
N̂ (s)
=⎣                                     N (s)            ⎦,   (4.86)
D̂ (s)    s Inr −                            T
(00∼n−1 ) D (s)
N̂ (s) and D̂ (s) are clearly right coprime since D (s) and N (s) are right coprime.
Thus the above (4.85) is a generalized RCF of the matrix pair TE , C IT .
In view of (4.81), N̂ (s) and D̂ (s) can be obviously rewritten into the form of
ω
Di i
N̂ (s) =                        s,                (4.87)
Ni
i=0
146                                                      4 Disturbance Attenuation and Decoupling
and
ω
D̂ (s) = s Inr −     T
(00∼n−1 )          Di s i
i=0
ω+1
=          Di−1 −      T
(00∼n−1 ) Di s i ,            (4.88)
i=0
respectively. Thus it follows from Theorems 2.1 and 4.3 in Duan (2015) that all the
matrices L x and L d satisfying (4.79) can be given by (4.80), where Z 0 ∈ Rnr ×(nr +kp)
is a parameter matrix satisfying constraint (4.82). Then the proof is completed.

## [112] `book_2026_volume1` (PDF p.182, L163) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof It follows from (5.3) that the matrix A + γ2 I is stable, thus there exists a
positive definite matrix P satisfying
γ T          γ
A+     I P + P A + I < 0.
2            2
Expanding the above equation gives Eq. (5.4).

## [113] `book_2026_volume1` (PDF p.182, L163) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof In view of
n−1
det (s I nr −          (A0∼n−1 )) = det s n Ir +         Ai s i ,
i=0
the eigenvalues of ( A0∼n−1 ) can be arbitrarily assigned by properly choosing
Ai , i = 0, 1, . . . , n − 1, thus the conclusion holds.
It is known from Lemma 5.1 that, when the condition in (5.5) holds for some
μ > 0, there exists a positive definite matrix P( A0∼n−1 ) satisfying
T
(A0∼n−1 )P(A0∼n−1 ) + P( A0∼n−1                  A0∼n−1 ) < −μP( A0∼n−1 ).    (5.6)
Partitioning P(A0∼n−1 ) as
P( A0∼n−1 ) = P1 P2 · · · Pn , Pi ∈ Rnr ×r ,                 (5.7)
we can further introduce the following notation which will be frequently used in this
chapter:
164                                                                                5 Robust and Adaptive Control
0
PL ( A0∼n−1 ) = P(A0∼n−1 )                    = Pn (5.8)
Ir
To conclude this subsection, let us state the following simple result.

## [114] `book_2026_volume1` (PDF p.187, L168) | Types: `Lyapunov` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Since
d         f 1 (z)
f¨1 (z) =                   ż
dt       ∂z
∂ 2 f 1 (z) 2              f 1 (z)
=             ż +                   z̈,
∂z 2                    ∂z
we have, using (5.20),
∂ 2 f 1 (z) 2                    f 1 (z)
f¨1 (z) ≤             ż +                         |z̈|
∂z 2                          ∂z
≤ γ1 |ż| + γ2 ż 2 |z̈| .
Further using (5.19) gives
..
f 2 z, z − 2z ż +f˙1 (z)
..              f 1 (z)
≤ σ2 |z| z − 2z ż +                ż
∂z
..                 f 1 (z)
≤ σ2 |z| | z − 2z ż| +                 |ż|
∂z
..
≤ σ2 |z| | z − 2z ż| + γ1 |ż|2 .
Finally, using the above two relations and definition (5.24) yields
..
f z (0∼3)              ≤          f¨1 (z) +f 2 z, z − 2z ż + f˙1 (z)
..
≤ γ1 |ż| + γ2 ż 2 |z̈| + σ2 |z| | z − 2z ż| + γ1 |ż|2 .
Thus the conclusion holds.
Using the function ρ z (0∼3) defined in the above proposition, we can design for
system (5.18), or FAS (5.22)–(5.24), the robust stabilizing control law
5.2 Adaptive Control                                                                        169
u = − A0∼3 z (0∼3) + f (z (0∼2) )+u ∗
(5.25)
u ∗ = 4ε1 ρ 2 (z (0∼3) )PLT ( A0∼3 )z (0∼3) ,
where A0∼3 is chosen to satisfy
μ
Re λi ( (A0∼3 )) < − , i = 1, 2, 3, 4,
(5.26)
2
μ and ε are two arbitrarily given positive numbers. The controller guarantees that
the vector z (0∼3) converges into the following ellipsoid centered at the origin:
T                 ε
μ,ε (0) =    z (0∼3) z (0∼3)        P z (0∼3) ≤       ,
μ
where. P = P(A0∼3 ) and. PLT ( A0∼3 ) are determined by (5.6) and (5.8), respectively..
The above design process demonstrates that the design based on a single FAS
model is even simpler than the proposed high-order method of backstepping, but
it should be noted that the two approaches need different prior knowledge of the
nonlinear uncertainties.
5.2 Adaptive Control
5.2.1 Adaptive Stabilization
Consider the following FAS with an unknown parameter vector:
x (n) = H T (x (0∼n−1) )θ + q(x (0∼n−1) ) + L(x (0∼n−1) )u,           (5.27)
where x,.u ∈ Rr are the state vector and the control input vector, respectively,.θ ∈ Rm
is an unknown constant vector, q(x (0∼n−1) ) ∈ Rr is a sufficiently smooth vector
function, H (x (0∼n−1) ) ∈ Rm×r and L(x (0∼n−1) ) ∈ Rr ×r are two sufficiently smooth
matrix functions, and L(x (0∼n−1) ) satisfies the full-actuation Assumption 5.1.
The above FAS (5.27) represents a quite general model for “completely control-
lable” systems, and can either be obtained through physical modeling, or through
conversion from other types of models (Duan, 2020a, 2020b, 2021a, 2021b).
In order to establish the control law of FAS (5.27) with unknown parameters, we
need the following preparations.
When the matrix A0∼n−1 is so chosen that the matrix A0∼n−1 ) is stable, it
follows from the well-known Lyapunov Theorem that there exists a positive definite
matrix P(A0∼n−1 ) satisfying
T
(A0∼n−1 )P(A0∼n−1 ) + P( A0∼n−1                  A0∼n−1 ) ≤ −Inr (5.28)
170                                                                       5 Robust and Adaptive Control
Partition P(A0∼n−1 ) as
P( A0∼n−1 ) = P1 P2 · · · Pn , Pi ∈ Rnr ×r (5.29)
Again, for convenience, we introduce the following notation which is frequently used
in this chapter:
0
PL ( A 0∼n−1 ) P( A0∼n−1 )       = Pn (5.30)
Ir
Regarding the control of FAS (5.27) with unknown parameters, we have the
following theorem.

## [115] `book_2026_volume1` (PDF p.197, L178) | Types: `Multi-Conclusion` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof The first conclusion can be easily verified. In view of Assumption 5.3, we
have
θ̃ T θ̃ ≤ θ̃r0
r0              θ̃
1         2       2
≤          θ̃r0 + θ̃
2
1 2          2
≤      δ0 + θ̃    ,
2
θ̃˙rT0 θ̃ ≤ θ̃˙r0 θ̃
θ̃˙r0 + θ̃
1       2       2
≤
2
1 2       2
≤   δ1 + θ̃     .
2
5.3 Robust Adaptive Control                                                                   179
Thus the second and the third conclusions also hold.
Secondly, if for any μ > 0, there exists a set of matrices Ai ∈ Rr ×r ,
i = 0, 1., . . . ,.n − 1, satisfying the following condition
μ
Re λi ( ( A0∼n−1 )) < − , i = 1, 2, . . . , nr.
(5.51)
2
Then, it follows from Lemmas 5.1 and 5.2 that, for any μ > 0, there exists a positive
definite matrix P (A0∼n−1 ) satisfying
T
(A0∼n−1 )P(A0∼n−1 ) + P(A0∼n−1               A0∼n−1 ) ≤ −μP(A0∼n−1 ).   (5.52)
As done in the previous two sections, we can then define the matrix PL ( A0∼n−1 ),
which will be often used in the following sections.

## [116] `book_2026_volume1` (PDF p.221, L203) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof According to (6.5), we have
L 0 = Ir ,
L 1 = L 0 G1 = G1,
L 2 = L 1G2 = G1G2,
.
L k = L k−1 G k = G 1 G 2 · · · G k .
204                                                6 Strict Feedback Systems with Uniform Dimensions
Thus the matrix L k (z (0∼k−1) , ζ, t) can be given recursively by
L k (z (0∼k−1) , ζ, t) = L k−1 (z (0∼k−2) , ζ, t)G k (x1∼k , ζ, t),     (6.15)
k = 1, 2, . . . , n,
with the initial value L 0 = Ir This is obviously equivalent to (6.13).
Simultaneously, using (6.6), and taking L̇ k = 0, k = 1, 2., . . . ,.n − 1, into consid-
eration, we can write the recursive formula for h k (z (0∼k−1) , ζ, t) as
h (z (0∼k−1) , ζ, t) = ḣ k−1 (z (0∼k−2) , ζ, t) + L k−1 f k (x1∼k , ζ, t),
k                                                                               (6.16)
k = 1, 2, . . . , n,
with the initial value h 0 (ζ, t) = 0. Thus, we further have, from the above formula,
h (z, ζ, t) = f 1 (z, ζ, t),
1                                                 (6.17)
h (z (0∼1) , ζ, t) = ḣ 1 (z, ζ, t) + L 1 f 2 (x1∼2 , ζ, t)
2
f˙1 (z, ζ, t)
= [Ir       L 1]                       ,
f 2 (x1∼2 , ζ, t)
h 3 (z (0∼2) , ζ, t)
= ḣ 2 (z (0∼1) , ζ, t) + L 2 f 3 (x1∼3 , ζ, t)
f¨ (z, ζ, t)
= [Ir        L 1] ˙ 1                   + L 2 f 3 (x1∼3 , ζ, t)
f 2 (x1∼2 , ζ, t)
⎡                      ⎤
f¨1 (z, ζ, t)
= L 0∼2 ⎣ f˙2 (x1∼2 , ζ, t) ⎦ .
f 3 (x1∼3 , ζ, t)
Continuing this process, we can finally get formula (6.14). Noting that (6.11) can be
obtained easily, we then complete the proof.
6.3 Second-Order SFSs
Lagrangian Equation and Theorem of Momentum (moment) are often used in model-
ing physical systems. As a result in such applications, the models of the obtained sub-
systems are of second-order. For this reason, we introduce the following second-order
SFS:
6.3 Second-Order SFSs                                                                             205
⎧                (0∼1)
⎪
⎪ ẍ1 = f 1 (x1        , ζ, t) + G 1 (x1(0∼1) , ζ, t)x2
⎪
⎪
⎪                (0∼1)                  (0∼1)
⎨ ẍ2 = f 2 (x1∼2 , ζ, t) + G 2 (x1∼2 , ζ, t)x3
⎪
.                                                             (6.18)
⎪            .
⎪
⎪                      (0∼1)                      (0∼1)
⎪
⎪ ẍ     =    f n−1 (x1∼n−1   , ζ, t) + G n−1 (x1∼n−1   , ζ, t)xn
⎪
⎩
n−1
(0∼1)                  (0∼1)
ẍn = f n (x1∼n , ζ, t) + G n (x1∼n , ζ, t)u,
where xi ∈ Rr , i = 1, 2, . . . , n, are the state vectors, u ∈ Rr is the control input
(0∼1)
vector, ζ ∈ Rm is a parameter vector; f i (x1∼i   , ζ, t) ∈ Rr , i = 1, 2, . . . , n, are a set
(0∼1)
of sufficiently smooth vector functions, G i (x1∼i , ζ, t) ∈ Rr ×r , i = 1, 2, . . . , n, are
a set of sufficiently smooth matrix functions, and satisfy the following assumption:

## [117] `book_2026_volume1` (PDF p.239, L221) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof The result can be easily proven by applying Theorem 6.5. With relation (6.83),
formula (6.48) becomes
⎡         (p )
⎤
f 1 2∼k (z (0∼m 1 −1) , ζ, t)
⎢ ( p3∼k ) (0∼m 1 −1) (0∼m 2 −1)               ⎥
⎢ f2      (x1             , x2         , ζ, t) ⎥
⎢                      ..                      ⎥
h k (z
(0∼ pk −1)
, ζ, t) = L 0∼k−1 ⎢
⎢                       .
⎥
⎥
⎢    (m k ) (0∼m i −1)                         ⎥
⎣ f k−1 (xi                |i=1∼k−1 , ζ, t) ⎦
f k (xi(0∼m i −1) |i=1∼k , ζ, t)
⎡         ω                                      ⎤
(p     )
⎢               f 1l 2∼k (z (0∼m 1 −1) , ζ, t)        ⎥
⎢                                                     ⎥
⎢ ω l=1                                               ⎥
⎢                                                     ⎥
⎢        ( p3∼k ) (0∼m 1 −1)
(x1           , x2(0∼m 2 −1)
, ζ, t) ⎥
⎢     f 2l                                            ⎥
⎢ l=1                                                 ⎥
⎢                                                     ⎥
⎢                           ..                        ⎥
= L 0∼k−1 ⎢                            .                        ⎥
⎢ ω                                                   ⎥
⎢                                                     ⎥
⎢           (m k )    (0∼m i −1)                      ⎥
⎢         f k−1,l (xi            |i=1∼k−1 , ζ, t) ⎥
⎢                                                     ⎥
⎢ l=1 ω                                               ⎥
⎢                                                     ⎥
⎣            f k,l (xi(0∼m i −1)
|i=1∼k , ζ, t)       ⎦
l=1
⎛            ⎡      (p )
⎤⎞
f 1l 2∼k (z (0∼m 1 −1) , ζ, t)
⎜         ⎢ ( p3∼k ) (0∼m 1 −1) (0∼m 2 −1)                 ⎥⎟
ω ⎜          ⎢ f 2l      (x1             , x2         , ζ, t) ⎥⎟
⎜         ⎢                        ..                      ⎥⎟
=     ⎜ L 0∼k−1 ⎢                                                ⎥⎟
⎜         ⎢                         .                      ⎥⎟
⎜         ⎢      (m k )                                    ⎥⎟
l=1
⎝         ⎣ f k−1,l     (xi(0∼m i −1) |i=1∼k−1 , ζ, t) ⎦⎠
f k,l (xi(0∼m i −1) |i=1∼k , ζ, t)
ω
=         h k,l (z (0∼ pk −1) , ζ, t),
l=1
which gives (6.87), while the other relations hold obviously.
It is reminded that the notation of pi∼ j is given by (6.42).
The above result indicates an important fact: if the nonlinear term in each subsys-
tem of SFS (6.33) is the sum of several individual nonlinear terms, then the nonlinear
term in the obtained equivalent FAS model is also the sum of the same number of
individual ones correspondingly.
222                                                   6 Strict Feedback Systems with Uniform Dimensions
6.6.2 Case of First-Order SFSs
For the case of first-order SFSs, correspondingly, we assume
ω
f (x1∼k , ζ, t) =
k                                  f kl (x1∼k , ζ, t) , k = 1, 2, . . . , n,   (6.89)
l=1
where.ω ≥ 1 is an integer,. f kl (x1∼i , ζ, t) ∈ Rr , i = 1, 2., . . . ,.n, l = 1, 2., . . . ,.ω, are
a group of sufficiently smooth vector functions. Applying Theorem 6.7, immediately
yields the following corollary.

## [118] `book_2026_volume1` (PDF p.247, L229) | Types: `Induction, Multi-Step, Direct-Substitution` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof We prove the theorem via the n-step induction.
Step 1: For the first subsystem, we already have that
ẋ
12   = f 1 (x12 ) + Ḡ 1 x21
= L 1 (x12 ) + Ḡ 1∼1 x21 (7.12)
Step i (.2 ≤ i ≤ n − 1): Assume that
230                                                       7 Strict Feedback Systems with Increasing Dimensions
(i− p)                                     (0∼i−1− p)
x
p2                             = L i−1 x p2                                  + Ḡ 1∼i−1 xi1 ,        (7.13)
p=1∼i−1                                       p=1∼i−1
then we prove that
(i+1− p)                           (0∼i− p)
x
p2                        = L i x p2                           + Ḡ 1∼i xi+1,1 .
p=1∼i                           p=1∼i
It follows from (7.13) that
(i− p)                             (0∼i−1− p)
x = Ḡ −1
i1   1∼i−1 x p2                                    − L i−1 x p2                                    (7.14)
p=1∼i−1                                   p=1∼i−1
We also have, by recalling system (7.7), the following equations:
−1
ẋi1 = f i1 (x2∼i,1 , x1∼i,2 ) + Iri−1 0 Q i−1  Ḡ i xi+1,1
−1                                      (7.15)
ẋi2 = f i2 (x2∼i,1 , x1∼i,2 ) + 0 Iri −ri−1 Q i−1   Ḡ i xi+1,1 .
Next, taking the derivatives of both sides of Eq. (7.13) and substituting the first
equation of (7.15) into the result, one has that
(i+1− p)
x p2
p=1∼i−1
= L̇ i−1 + Ḡ 1∼i−1 ẋi1
−1
= L̇ i−1 + Ḡ 1∼i−1 f i1 (x2∼i,1 , x1∼i,2 ) + Iri−1 0 Q i−1 Ḡ i xi+1,1
= L̇ i−1 + Ḡ 1∼i−1 f i1 (x2∼i,1 , x1∼i,2 )
−1
+ Ḡ 1∼i−1 0 Q i−1       Ḡ i xi+1,1 (7.16)
By combining (7.16) with the last equation of (7.15), it can be obtained that
(i+1− p)                          (0∼i− p)
x
p2                         = L i x p2                       + Ḡ 1∼i xi+1,1 ,
p=1∼i                          p=1∼i
where
L̇ i−1 + Ḡ 1∼i−1 f i1 (x2∼i,1 , x1∼i,2 )
Li =                                                ,                   (7.17)
f i2 (x2∼i,1 , x1∼i,2 )
Ḡ 1∼i−1 0               −1
Ḡ 1∼i =                               Q i−1 Ḡ i (7.18)
0   Iri −ri−1
Step n: Based on the previous n − 1 steps, we can obtain
(i− p)                             (0∼i−1− p)
x = Ḡ −1
i1   1∼i−1 x p2                                    − L i−1 x p2                                    ,   (7.19)
p=1∼i−1                                   p=1∼i−1
7.1 First-Order SFSs with Increasing Dimensions                                                                 231
i = 2, 3, . . . , n − 1,
and
(n− p)                                        (0∼n−1− p)
x
p2                                = L n−1 x p2                              + Ḡ 1∼n−1 xn1 ,      (7.20)
p=1∼n−1                                       p=1∼n−1
where L i (·) and Ḡ 1∼i are given iteratively by
(0∼i+1− p)                                L̇ i + Ḡ 1∼i f i+1,1 (x2∼i+1,1 , x1∼i+1,2 )
L i+1 x p2                                        =                                                 ,   (7.21)
p=1∼i+1                    f i+1,2 (x2∼i+1,1 , x1∼i+1,2 )
Ḡ 1∼i 0
Ḡ 1∼i+1 =                      Q i−1 Ḡ i+1 ,                  (7.22)
0 Iri+1 −ri
i = 1, 2, . . . , n − 1.
We recall the following equations from (7.7):
ẋn1 = f n1 (x2∼n,1 , x1∼n,2 ) + Irn−1 0 Q −1n−1 Ḡ n u 1                         (7.23)
ẋn2 = f n2 (x2∼n,1 , x1∼n,2 ) + 0 Irn −rn−1 Q −1
n−1 Ḡ n u 1 .
Similar to the discussion in the previous steps, taking the derivative of both sides of
(7.20) and substituting the first equation of (7.23) into the result, we obtain
(n+1− p)
x p2
p=1∼n−1
= L̇ n−1 + Ḡ 1∼n−1 f n1 (x2∼n,1 , x1∼n,2 ) + Irn−1 0 Q −1
n−1 Ḡ n u 1
= L̇ n−1 + Ḡ 1∼n−1 f n1 (x2∼n,1 , x1∼n,2 ) + Ḡ 1∼n−1 0 Q −1
n−1 Ḡ n u 1 (7.24)
Combining (7.24) with the last equation of (7.23), gives
(n+1− p)                           (0∼n− p)
x
p2                         = L n x p2                       + Ḡ 1∼n u 1 ,       (7.25)
p=1∼n                        p=1∼n
where
L̇ n−1 + Ḡ 1∼n−1 f n1 (x2∼n,1 , x1∼n,2 )
Ln =                                                ,                (7.26)
f n2 (x2∼n,1 , x1∼n,2 )
Ḡ 1∼n−1     0
Ḡ 1∼n =                              Q −1
n−1 Ḡ n (7.27)
0    Irn −rn−1

## [119] `book_2026_volume1` (PDF p.372, L357) | Types: `State-Space-Conversion, Observer/Error-Dynamics` | Closer: `The proof is finished.`

Proof Since f 0 ≡ 0, Eq. (11.35) reduces to
x1(n 1 )             F11 − A11 F12                x1(0∼n 1 −1)   −A12 x̂2(0∼n 2 −1)
=                                        (0∼n 2 −1) +                    ,
x2(n 2 )                                                         −A22 x̂2(0∼n 2 −1)
F21 − A21 F22                x2
whose state-space form is given by
ẋ1(0∼n 1 −1)                      x1(0∼n 1 −1)
=
ẋ2(0∼n 2 −1)                      x2(0∼n 2 −1)
FA
B1 A12 (x2(0∼n 2 −1) − x̂2(0∼n 2 −1) )
+                                              (11.42)
B2 A22 (x2(0∼n 2 −1) − x̂2(0∼n 2 −1) )
358                                                                                  11 Observer-Based Control
In view of (11.33) and (11.42), the dynamics of the observer error e can be obtained
as
ė = ẋ2(0∼n 2 −1) − x̂˙2(0∼n 2 −1)
= ẋ2(0∼n 2 −1) − ż + L ẏ
(0∼n 1 −1)                  (0∼n 2 −1)
=     21 x 1          +           22 x 2          + B2 A22     x2(0∼n 2 −1) − x̂2(0∼n 2 −1)
−(    22 + L           12 )   x̂2(0∼n 2 −1) + L y − (L        11 − (      22 + L     12 ) L +    21 ) y
(0∼n 1 −1)                  (0∼n 2 −1)
+L        11 x 1          +           12 x 2          + B1 A12    x2(0∼n 2 −1) − x̂2(0∼n 2 −1)
(0∼n 2 −1)
=    22 x 2          + B2 A22 e − 22 x̂2(0∼n 2 −1)
−L 12 x̂2(0∼n 2 −1) + L 12 x2(0∼n 2 −1) + L B1 A12 e
=     22 e + B2 A22 e + L              12 e + L B1 A12 e
=        0r2 ×n 2 r2 ) + B2 F22 − B2 A22 e + B2 A22 e + L B1 (F12 − A12 ) e + L B1 A12 e
=        0r2 ×n 2 r2 ) + B2 F22 + L B1 F12 e
=     33 e.                                                                                           (11.43)
Combining (11.42) and (11.43) gives (11.38). The proof is finished. .
Clearly, it follows from Theorem 11.2 that the closed-loop system (11.38) is
asymptotically stable if and only if AC is Hurwitz. This is equivalent to requiring:
• the matrix F A is Hurwitz; and
• the matrix 33 =         0r2 ×n 2 r2 ) + B2 F22 + L B1 F12 is Hurwitz.
These two subproblems are addressed below, respectively.
Solution of Matrix A F
Define
f      f
11     12                                                        (11.44)
F              f      f
21     22
0r1 ×n 1 r1 ) + B1 F11           B1 F12
=                                                             ,            (11.45)
B2 F21                 0r2 ×n 2 r2 ) + B2 F22
B1 0
BE =              (11.46)
0 B2
Then, the following result shows the controllability of (                         F , BE ) .

## [120] `book_2026_volume1` (PDF p.374, L359) | Types: `Observer/Error-Dynamics` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Observe
rank s In 1 r1 +n 2 r2 −         F BE
s In 1 r 1 −   0r1 ×n 1 r1 ) − B1 F11             −B1 F12                B1 0
= rank
−B2 F21                s In 2 r2 − 0r2 ×n 2 r2 ) − B2 F22 0 B2
s In 1 r1 − 0r1 ×n 1 r1 )           −B1 F12         B1 0
= rank
−B2 F21         s In 2 r2 − 0r2 ×n 2 r2 ) 0 B2
s In 1 r 1 −       0r1 ×n 1 r1 )                  0                 B1 0
= rank
0                   s In 2 r 2 −       0r2 ×n 2 r2 ) 0 B2
s In 1 r 1 −       0r1 ×n 1 r1 ) B1           0              0
= rank                                                                        .
0                 0 s In 2 r2 − 0r2 ×n 2 r2 ) B2
Since 0r1 ×n 1 r1 ), B1 and 0r2 ×n 2 r2 ), B2 are both controllable, we then have
rank s I −            F   B E = n 1 r1 + n 2 r2 .
Therefore, the conclusion holds. .
In view of
0r1 ×n 1 r1 ) + B1 F11 − B1 A11                           B1 (F12 − A12 )
FA =
B2 (F21 − A21                                 0r2 ×n 2 r2 ) + B2 F22 − B2 A22
=       F − B  E AF ,                                                                           (11.47)
and the fact of ( F , B E ) being controllable, the solution of A F is turned into an ESA
problem, while the controllability of ( F , B E ) ensures arbitrary assignment of the
eigenvalues of F A .
Solution of Observer Gain L
Recalling (11.44)–(11.45), we have
⎡⎤
0 Ir2
⎢ ..      ..    ⎥
⎢            .  ⎥
0r2 ×n 2 r2 ) + B2 F22 = ⎢ .
f
22 =                                             ⎥,
⎣ 0 · · · 0 Ir2 ⎦
F22
⎡       ⎤
0
⎢ .. ⎥
f                 ⎢ . ⎥
12 = B1 F12 = ⎢           ⎥.
⎣ 0 ⎦
F12
360                                                                                                11 Observer-Based Control
Further, define
CM
In 1 r 1 0 .
Then, regarding solution of the observer gain L , we have the following results.

## [121] `book_2026_volume1` (PDF p.375, L360) | Types: `Observer/Error-Dynamics` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Firstly, the detectability of the matrix pair.                                 22   12    obviously follows from
well-known linear system theories.
Secondly, noting
s I(n 1 r1 +n 2 r2 ) − F
rank
CM
⎡                                                                       ⎤
s In 1 r1 − 0r1 ×n 1 r1 ) − B1 F11             −B1 F12
= rank ⎣                    −B2 F21         s In 2 r2 − 0r2 ×n 2 r2 ) − B2 F22 ⎦
In 1 r 1                     0
s In 2 r 2 −          0r2 ×n 2 r2 ) − B2 F22
= rank                                                 + n 1 r1
−B1 F12
f
s In 2 r 2 −
= rank                f
22        + n 1 r1 ,
12
we know immediately that the detectability of F , C M ) is equivalent to that of
f    f
22   12 ).
Finally, by the well-known PBH criterion, the last condition follows from
11.3 Reduced-Order Observer-Based Control                                                                    361
⎡                                         ⎤
s Ir2 −Ir2
⎢        ..        ..                        ⎥
⎢            .        .                      ⎥
f           ⎢                                            ⎥
s In 2 r 2 −               ⎢                 s I            −I          ⎥
rank
22   = rank ⎢                    r2            r2        ⎥
f
⎢ −F [0] · · · −F [n 2 −2] s Ir − F [n 2 −1] ⎥
12                ⎢     22           22          2    22       ⎥
⎣              0(n −1)r ×n r                 ⎦
1     1    2 2
−F12
⎡                                                        ⎤
s Ir2 −Ir2
⎢            ..             ..                              ⎥
⎢                .             .                            ⎥
⎢                                                           ⎥
= rank ⎢                          s I              −I              ⎥
⎢                             r2                 r2         ⎥
⎣ −F [0] · · · −F [n 2 −2] −F [n 2 −1] ⎦
12                    12               12
[0]                   [n 2 −2]              [n 2 −1]
−F22       · · · −F22               s Ir2 − F22
⎡                                                           ⎤
0                    −Ir2
⎢                  ..                        ..             ⎥
⎢                   .                            .          ⎥
⎢                                                           ⎥
⎢                 0                                 −Ir2 ⎥
⎢                                                           ⎥
= rank ⎢        n 2 −1                                             ⎥,
⎢ −               F   [i] n i −i
s               ∗   · ·  ·     ∗   ⎥
⎢                     12                                    ⎥
⎢          i=0                                              ⎥
⎣              n 2 −1
[i] n i −i
⎦
s Ir2 −
n2
F22 s            ∗ ··· ∗
i=0
where we have used the elementary transformation, and .∗ symbols represent some
matrices that are not of interest. .
11.3.3 Case of f0 (z1 , z2 ) Dependent on z2
In the case that f 0 (z 1 , z 2 ) is dependent on z 2 , we impose the following assumption.

## [122] `book_2026_volume1` (PDF p.377, L362) | Types: `State-Space-Conversion, Observer/Error-Dynamics` | Closer: `The proof is finished.`

Proof Write the state-space form of (11.35) as
ẋ1(0∼n 1 −1)                 x1(0∼n 1 −1)
=
ẋ2(0∼n 2 −1)                 x2(0∼n 2 −1)
FA
B1 A12 (x2(0∼n 2 −1) − x̂2(0∼n 2 −1) )   B1 f 1
+                                             +        (11.51)
B2 A22 (x2(0∼n 2 −1) − x̂2(0∼n 2 −1) )   B2 f 2
In view of (11.33) and (11.51), the dynamics of the observer error e can be obtained
as
ė = ẋ2(0∼n 2 −1) − x̂˙2(0∼n 2 −1)
= ẋ2(0∼n 2 −1) − ż + L ẏ
(0∼n 1 −1)              (0∼n 2 −1)
=       21 x 1          +       22 x 2          + B2 A22     x2(0∼n 2 −1) − x̂2(0∼n 2 −1) + B2 f 2
−(       22 + L      12 )   x̂2(0∼n 2 −1) + L y − (L        11 −     22 + L      12 )L +        21 ) y
(0∼n 1 −1)             (0∼n 2 −1)
+L         11 x 1          +      12 x 2          + B1 A12     x2(0∼n 2 −1) − x̂2(0∼n 2 −1) + B1 f 1
(0∼n 2 −1)                                             (0∼n 2 −1)            (0∼n 2 −1)
=    22 x 2          + B2 A22 e + B2 f 2 −                 22 x̂ 2          −L   12 x̂ 2
(0∼n 2 −1)
+L 12 x2             + L B1 A12 e + L B1      f1
=       22 e +  B     A
2 22  e +  B2  f 2 + L 12 e + L B1 A12 e + L B1 f 1
=          0r2 ×n 2 r2 ) + B2 F22 − B2 A22 e + B2 A22 e
+L B1 (F12 − A12 ) e + L B1 A12 e + L B1 f 1 + B2 f 2
=    0r2 ×n 2 r2 ) + B2 F22 + L B1 F12 e + L B1 f 1 + B2 f 2
=       33 e + L B1       f 1 + B2 f 2 (11.52)
Combining (11.51) and (11.52) gives (11.50). The proof is finished. .
11.3 Reduced-Order Observer-Based Control                                              363
Robust Stability
Now we study the exponential stability of the overall nonlinear system (11.50).
Denote
n   n 1r1 + 2n 2 r2 , r r1 + r2 ,
and                         ⎡              ⎤                    ⎡        ⎤
x1(0∼n 1 −1)                        B1 0
ξ
⎣ x (0∼n 2 −1) ⎦ ∈ Rn , BC          ⎣ 0 B2 ⎦ ∈ Rn×r (11.53)
2
e                             L B1 B2
Then the closed-loop system (11.50) can be rewritten in the compact form:
ξ̇ = AC ξ + BC           f0 ,          (11.54)
for which the following simple result can be obtained.

## [123] `book_2026_volume1` (PDF p.378, L363) | Types: `Lyapunov, Observer/Error-Dynamics` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Define a candidate Lyapunov function as
V (ξ ) = ξ T Pξ,
whose time derivative along the trajectory of system (11.54) is
V̇ (ξ ) = ξ T ACT P + P AC ξ + 2ξ T P Bc f 0 .
By Assumption 11.5, we have
f 0 ≤ α x2(0∼n 2 −1) − x̂2(0∼n 2 −1) = α e ≤ α ξ ,
which is equivalent to
f 0 )T f 0 − α 2 ξ T ξ ≤ 0.            (11.56)
364                                                                              11 Observer-Based Control
Therefore, we have, using (11.55) and (11.56), the following:
V̇ (ξ ) ≤ ξ T ACT P + P AC ξ + 2ξ T P Bc f 0 − k                        f 0 )T f 0 − α 2 ξ T ξ
T
ξ            ACT P + P AC + kα 2 In P Bc                  ξ
=
f0                  BcT P          −k Ir                  f0
T
ξ           ξ
≤ −ε
f0          f0
= −ε           ξ 2         f0 2
≤ −ε ξ 2 .
This immediately completes the proof. .
We point out that the inequality (11.55) is linear if the observer gain. L is prescribed.
However, it might fail to hold for a given. L. In practice, a trial-and-error approach can
be employed to identify a feasible L. First, we choose an observer gain L such that
33 is Hurwitz. Next, we attempt to solve the LMI (11.55). If this LMI is solvable,
the chosen L is valid; otherwise, we refine our selection of L and repeat the process.
11.3.4 Case of A F = 0
In this section, the case of A F = 0, or equivalently, Ai j = 0, i, j = 1, 2, is
specifically considered. In this case, system (11.32) reduces into the following one:
⎧ (0∼n 1 −1)
⎨ ẋ1                       x1(0∼n 1 −1)
=
ẋ (0∼n 2 −1)            x2(0∼n 2 −1)
F
(11.57)
⎩ 2 (0∼n 1 −1)
y = x1          ,
where F is given by (11.45). Likewise, instead of designing an observer for the
nonlinear system (11.25), we can design for the linear system (11.57) the following
reduced-order observer:
⎧
⎪
⎪ ż =     0r2 ×n 2 r2 ) + B2 F22 + L B1 F12 z
⎨      +L        0r1 ×n 1 r1 ) + B1 F11 y
(11.58)
⎪
⎪      −        0r2 ×n 2 r2 ) + B2 F22 + L B1 F12 L − B2 F21 y
⎩ (0∼n 2 −1)
x̂2        = z − L y,
where L ∈ Rn 2 r2 ×n 1 r1 is the observer gain to be determined. Then, we can design the
output feedback controller as
u = −B −1 x1(0∼n 1 −1) , t
f 0 (x1(0∼n 1 −1) , x̂2(0∼n 2 −1) ).         (11.59)
11.3 Reduced-Order Observer-Based Control                                                         365
Applying the above controller (11.59) to FAS (11.25), yields
x1(n 1 )            x1(0∼n 1 −1)
= FD                  +          f0 ,         (11.60)
x2(n 2 )            x2(0∼n 2 −1)
where FD is given by (11.27), and f 0 is given by (11.36). Please note that there is
quite some DOFs to choose FD via the decomposition (11.26). The stability of the
closed-loop system can be guaranteed by adjusting, to a certain extent, the matrix
FD .
Based on the above description, similarly, two cases where f 0 (z 1 , z 2 ) is inde-
pendent on z 2 and f 0 (z 1 , z 2 ) is dependent on z 2 are considered in the following
subsections. Let us start with the simple case where f 0 (z 1 , z 2 ) is independent on z 2 .
Case of f0 (z1 , z2 ) Independent on z2
Letting Ai j = 0, i, j = 1, 2, in the above Theorem 11.2, immediately gives the
following result.

## [124] `book_2026_volume1` (PDF p.422, L405) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof It follows from Lemma A.1 that the solution to Problem A.2 is given by (A.11)
with
R    I
= Z Fn,                            (A.17)
and                                                        ⎡             ⎤
Z
⎢    ZF       ⎥
⎢             ⎥
VR VI = ⎢     ..      ⎥.         (A.18)
⎣      .      ⎦
Z F n−1
Define
αi βi
2,i =             , i = 1 ∼ m2,           (A.19)
−βi αi
then the matrix F can be given by
F = diag         1   2,i , i = 1 ∼ m 2   (A.20)
In accordance with the structure of the above matrix F, let us denote the parameter
matrix Z in the following form:
⎧
⎨ Z = Z1 Z2
⎪
Z 1 = Z 1,1 · · · Z 1,m 1                          (A.21)
⎪
⎩
Z 2 = Z 2,1
a      b
Z 2,1  · · · Z 2,m
a
2
b
Z 2,m 2
,
where. Z 1,k , Z 2,i
a
, Z 2,i
b
∈ Rr , k = 1 ∼ m 1 , i = 1 ∼ m 2 Then, it follows from (A.18)
that the matrices V and V I can be obtained by
R
410                                           Appendix A: Specific Solutions for Controller Parameterization
⎡               ⎤
V10 · · · Vm01
⎢ V11 · · · Vm1 ⎥
⎢                    1 ⎥
V
R
= ⎢ .       ..     .. ⎥ ,                                                   (A.22)
⎣ ..       .      . ⎦
V1n−1 · · · Vmn−1
⎡ 0                1
⎤
Va1 Vb01 · · · Va0m Vb0m
⎢ V1 V1 ··· V1 V1 ⎥          2      2
⎢ a1          b1          am 2   bm 2 ⎥
V = ⎢                                  .. ⎥ ⎥,
I
⎢ ..         ..     ..    ..                                              (A.23)
⎣ .           .      .     .      . ⎦
Van−1
1
Vbn−1 1
· · · Van−1
m
Vbn−1
m                   2         2
where
j                  j
Vk = Z 1,k sk , k = 1 ∼ m 1 , j = 0 ∼ n − 1,
Va0i Vb0i =                   a
Z 2,i   b
Z 2,i ,
Va1i Vb1i =                 Va0i Vb0i             2,i
αi βi
=         Va0i Vb0i
−βi αi
=         αi Va0i − βi Vb0i βi Va0i + αi Vb0i ,
.
j+1          j+1                    j     j
Vai             Vbi            =         Vai Vbi                2,i
j     j            αi βi
=         Vai Vbi
−βi αi
j        j      j        j
=         αi Vai − βi Vbi βi Vai + αi Vbi ,
i = 1 ∼ m 2 , j = 0 ∼ n − 1.
R                I
Then, using (A.17), the matrices and are, respectively, given by (A.12) and
I
=           Z2     n−1
2             2
=           Van−1
1
Vbn−1
1

## [125] `book_2026_volume1` (PDF p.428, L405) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Simply choosing
Z 1,k = 1, k = 1 ∼ m 1 ,
a
Z 2,i = Z 2,i
b
= 1, i = 1 ∼ m 2 ,
in Theorem A.1 immediately gives equations (A.45)–(A.49). Furthermore, it can be
also easily proven that in such a case the matrix V is nonsingular.          .
According to the number of self-conjugate poles, three specific cases, that is,
m 2 = 0, 1, 2 in (A.8), are considered in the following. Based on Theorem A.2, the
following corollary can be immediately derived.

## [126] `book_2026_volume1` (PDF p.434, L422) | Types: `Direct-Algebraic/Citation` | Closer: `Direct-final-equation/sentence (no verbal closer)`

Proof Noticing the expressions of Q̄ (t) and Q̄ −1 (t) , we have
Q̄ −1 (t) Q̄(t)
⎡ T ⎤
q̄10
⎢ .. ⎥
⎢ . ⎥
⎢ T            ⎥
⎢ q̄1,μ −1 ⎥
⎢        1     ⎥
⎢              ⎥
= ⎢ ... ⎥ q̄11 · · · q̄μ1 1 · · · q̄1r · · · q̄μr r
⎢              ⎥
⎢ q̄ T ⎥
⎢ r0 ⎥
⎢ . ⎥
⎣ .. ⎦
T
q̄r,μ r −1
⎡ T 1                                                                                    ⎤
q̄10 q̄1 · · · q̄10     T 1
q̄μ1 · · · q̄10   T r
q̄1 · · · q̄10     T r
q̄μr
⎢         ..       ..            ..       ..          ..          ..            ..       ⎥
⎢                      .                      .                       .                  ⎥
⎢ T 1                           .                    .                         .       ⎥
⎢ q̄1,μ −1 q̄1 · · · q̄1,μ  T
q̄ · · · q̄1,μ1 −1 q̄1 · · · q̄1,μ1 −1 q̄μr ⎥
1          T            r          T           r ⎥
⎢        1                     1 −1 μ1
⎢          ..      ..             ..      ..           ..         ..             ..      ⎥
= ⎢           .          .           .          .         .             .           .      ⎥.
⎢                                                                                        ⎥
⎢ q̄ T q̄ 1 · · · q̄ T q̄ 1 · · · q̄ T q̄ r · · · q̄ T q̄ r ⎥
⎢ r0 1                        r 0 μ1                 r0 1                    r 0 μr      ⎥
⎢           .      .               .      .             .         .               .      ⎥
⎣           .
. .           .
. .         .
. .           .
⎦
T
q̄r,μ      q̄
r −1 1
1
· · · q̄ T
r,μr −1 μ1q̄ 1
· · · q̄ T
r,μr −1 1  q̄ r
· · · q̄ T
r,μr −1 μrq̄ r
Therefore,
q̄i,T j−1 q̄ ij = 1, j = 1, 2, · · · , μi , i = 1, 2, · · · , r
(B.5)
T l
q̄i,k  q̄ j = 0, i l, or k        j − 1.

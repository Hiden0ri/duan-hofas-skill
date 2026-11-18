# Sorted Lemma Corpus Across 32 Duan First-Author Papers + Volume I (80 items)

## [1] `ijss_2021_part3` (PDF p.6, L522)

Lemma 3.1: Let A ∈ ℝn×n satisfy

γ
Reλi (A) ≤ − , i = 1, 2, . . . , n, (7)
2

where γ > 0, then there exists a positive definite matrix
P ∈ ℝn×n satisfying

ATP + PA ≤ −γ P. (8)

## [2] `ijss_2021_part3` (PDF p.6, L543)

Lemma 3.2: For any μ > 0, there exist a set of matrices
Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1 satisfying

Reλi Φ A0∼n−1 < −μ, i = 1, 2, . . . , nr. (9)
( ( )) 2

## [3] `ijss_2021_part3` (PDF p.6, L581)

Lemma 3.3: Let a, b be two real numbers, and b>0.
Then the following relation holds:

a2
a − ⩽ b. (13)
4b

## [4] `ijss_2021_part5` (PDF p.5, L436)

Lemma 2.1: Suppose that Assumption A3 is met, then,
for the variables defined in (4), the following relations
hold:

(1) θ˜ = θ˜r0 − θ˜e0;
(2) θ˜rT0θ˜ ≤ 12(δ02 + ‖ ˜θ‖2);
(3) θ˙˜rT0θ˜ ≤ 12(δ12 + ‖ ˜θ‖2).

## [5] `ijss_2021_part5` (PDF p.5, L460)

Lemma 2.2: Suppose that A ∈ ℝn×n satisfies

μ
Reλi (A) < − , i = 1, 2, . . . , n, (5)
2

where μ > 0, then there exists a positive definite matrix
P ∈ ℝn×n satisfying

ATP + PA ≤ −μP. (6)

## [6] `ijss_2021_part5` (PDF p.5, L471)

Lemma 2.3: For any μ > 0, there exist a set of matrices
Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1 satisfying the following
condition

Reλi Φ A0∼n−1 < −μ, i = 1, 2, . . . , nr. (7)
( ( )) 2

## [7] `ijss_2021_part5` (PDF p.5, L478)

Lemma 2.4: Let a, b be two real numbers, and b>0,
then the following relation holds:

a2
a − ≤ b. (8)
4b

When condition (7) holds, it follows from Lem-
mas 2.2 and 2.3 that, for any μ > 0, there exists a
positive definite matrix P(A0∼n−1) satisfying

ΦT(A0∼n−1)P(A0∼n−1) + P(A0∼n−1)Φ(A0∼n−1)

≤ −μP(A0∼n−1). (9)

Partition P(A0∼n−1) into

P(A0∼n−1) = P1 P2 · · · Pn , Pi ∈ ℝnr×r.
[ ]
(10)

For convenience, we introduce the following notation

PL(A0∼n−1) = P(A0∼n−1)[0] = Pn, (11)
Ir

which will be often used in the following sections.

## [8] `ijss_2021_part6` (PDF p.7, L728)

Lemma 3.1: For an arbitrarily selected matrix F ∈
ℝq×q, all the matrices W ∈ ℝr×q and V ∈ ℝnr×q sat-
isfying the above equation (25) are given by

⎧ ⎡ Z ⎤
ZF
⎪⎪⎪⎪⎪⎪⎪⎨V = V(Z, F) =
⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎦ (26)
ZFn−1

⎪⎪⎪⎪⎪⎪⎪⎩W = W(Z, F) = ZFn,

where Z ∈ ℝr×q is an arbitrary parameter matrix.

The above result can be easily proven using the
Theorem 4.3 in Duan (2015, p. 120), about the para-
metric solution to a general GSE.

The second preliminary result gives an analytical
expression of the H2 norm of a transfer function in
terms of solutions to Lyapunov matrix equations (see,
e.g. the Lemma 5.1 in Duan and Yu (2013, p. 140)).

## [9] `ijss_2021_part6` (PDF p.8, L753)

Lemma 3.2: Let A ∈ ℝn×n,B ∈ ℝn×r, C ∈ ℝm×n and
A be Hurwitz. Then

‖C(sI − A)−1B‖22 = trace(CP1CT) = trace(BTP2B),

where P1 and P2 are the unique positive definite solu-
tions to the following Lyapunov equations

AP1 + P1AT = −BBT,

and

ATP2 + P2A = −CTC,

respectively.

Introduce the following notations related to a square
matrix Φ ∈ ℝn×n:

n
det(sI + Φ) ≜ ∑ciΦsi,
i=0
n−1
adj(sI + ΦT) ≜ ∑CiΦsi.
i=0

Then we have the following result which is simplified
from the Theorem 9.2 in Duan (2015, p. 356).

## [10] `ijss_2021_part6` (PDF p.8, L782)

Lemma 3.3: If Φ ∈ ℝn×n is Hurwitz, then, for an arbi-
trary positive definite matrix Q ∈ ℝn×n, the following
Lyapunov equation

ΦTP + PΦ = −Q

has a unique solution given by

n−1
P = −∑CiΦQP0−1Φi, (27)
i=0

with
n
P0 = ∑ciΦΦi. (28)
i=0

## [11] `ijss_2021_part6` (PDF p.10, L1017)

Lemma 4.1: Suppose that the system (46) satisfies Con-
ditions C1–C2. Let the control law for the system be
designed as

⎧[x ˙ˆ]=[A Ew] [xˆ]+[B]u + [KA](Cyx − y)
⎪⎪⎪⎪⎨ w˙ˆ 0 S wˆ 0 KS ˆ

u = [K Γ − KΠ][xˆ],
⎪⎪⎪⎪⎩ wˆ
(48)

where K, KA and KS are arbitrary matrices making

[A + KACy Ew]
A + BK and (49)
KSCy S

both Hurwitz; Γ and Π are the solutions to the following
matrix equations:

AΠ + BΓ + Ew = ΠS, (50)

CeΠ + Dew = 0. (51)

Then,

(1) the following closed-loop system is internally
asymptotically stable

x˙ ⎡ A BK A2 ⎤ x
⎡ ⎤ ⎡ ⎤
x˙ˆ = −KACy A1 Ew + A2 xˆ ,
⎣w˙ˆ⎦ ⎢⎣−KSCy KSCy S ⎥⎦⎣wˆ⎦
(52)
where

A1 = A + KACy + BK,

and

A2 = B(Γ − KΠ);

(2) the following asymptotic output regulation require-
ment

lim e(t) = 0, (53)
t→∞

is met for arbitrary initial values x(0),x ˆ(0) and
w(0).

## [12] `ijss_2021_part6` (PDF p.10, L1074)

Lemma 4.2: Let F ∈ ℂq×q, R ∈ ℝr×q. Then all the
matrices Π ∈ ℂnr×q and Γ ∈ ℂr×q satisfying Equation
(54) are given by

Z
⎡ ⎤
ZF n
Π = Γ = R + ZF , (55)
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
ZFn−1

where Z ∈ ℝr×q is an arbitrary parameter matrix.

## [13] `ijss_2021_part7` (PDF p.18, L1863)

Lemma 5.2: Let (A, B) be controllable, and N(s) and
D(s) be a pair of right coprime polynomial matrices
given by (78) and satisfy the RCF (77). Then, for an arbi-
trarily chosen F ∈ ℝn×n, all the matrices K ∈ ℝr×n and

V ∈ ℝn×n satisfying det V ≠ 0 and

A + BK = VFV−1,

are given by

K = WV−1
⎧ ω
⎨V = N0Z + N1ZF + · · · + NωZF (79)
W = D0Z + D1ZF + · · · + DωZFω,
⎩
where Z ∈ ℝr×n is an arbitrary parameter matrix satis-
fying the following constraint:

det N0Z + N1ZF + · · · + NωZFω ≠ 0. (80)
( )

The parameter matrix Z in the above result repre-
sents the design degrees of freedom in the design.

## [14] `ijss_2022_part10` (PDF p.21, L2304)

Lemma A.1: Let [A, B] be controllable. Then, there exists a state
transformation z = T(x), under which the above system (2) can
be transformed into

⎧zi1 (k + 1) = zi2 (k)
zi2 (k + 1) = zi3 (k)

⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ ...
zi,μi−1 (k + 1) = ziμi (k) (A1)
r μl r
ziμi (k + 1) = ∑∑a(lji)zlj (k) +∑bijuj (k) ,
⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ l=1 j=1 j=i
i = 1, 2, . . . , r,

where μi, i = 1, 2, . . . , r are the controllability indices of [A, B],
and a(lji), bil, j = 1, 2, . . . , μl, i, l = 1, 2, . . . , r, with bii = 1, i =
1, 2, . . . , r, are some real numbers.

Based on the above lemma, the result can be proven as
follows.
Using the first r−1 equations in (A1), we can obtain

zij (k) = zi1(k + j − 1), j = 1, 2, . . . , μi, i = 1, 2, . . . , r,
(A2)

substituting these into the last one in system (A1), yields
r μl r
zi1 (k + μi) = ∑∑a(lji)zlj (k) +∑bijuj (k)
l=1 j=1 j=i
r μl
= ∑∑a(lji)zl1 k + j − 1
( )
l=1 j=1
r
+∑bijuj (k) , i = 1, 2, . . . , r,
j=i

which can be written in the form of

zp⌊1μp−1⌋(k + 1) = Li(zi⌊10∼μi−1⌋(k) , i = 1, 2, . . . , r)

r
+∑bpjuj (k) ,
j=p
p = 1, 2, . . . , r,

where each Li(·) is a linear function. Clearly, the above sys-
tem can be written into the form of the following step forward
HOFA model:

zp⌊1μp−1⌋(k + 1) = L(zp⌊10∼μp−1⌋(k) )+ Buˆ (k) ,
||||p=1∼r ||||p=1∼r
(A3)

where L(·) is an extended vector of linear functions, andBˆ is an
upper triangular matrix with diagonal elements all being 1.
On the other side, it can also be obtained from the first r−1
equations in (A1) that

zij (k) = ziμi (k − μi + j), j = 1, 2, . . . , μi, i = 1, 2, . . . , r.
(A4)

Substituting these into the last one in (A1), gives
r μl r
ziμi (k + 1) = ∑∑a(lji)zlj (k) +∑bijuj (k)
l=1 j=1 j=i

## [15] `ijss_2022_part8` (PDF p.8, L823)

Lemma 4.2: Let A ∈ ℝn×n, B ∈ ℝn×r, and [A, B] be
controllable. Further let R>0, and Q = DTD, [A, D] be
observable. Then

(1) the particular solution P(t) to the Riccati differen-
tial equation

−P˙ = PA + ATP − PBR−1BTP + Q, (31)

satisfying the final value condition P(tf ) = P con-
verges uniquely to a constant matrix P, that is,

lim P (t) = P;
tf →∞

(2) this limit matrix P is the unique positive definite
solution to the following Riccati algebraic equation

ATP + PA − PBR−1BTP + Q = 0;

(3) the following matrix

Ac = A − BR−1BTP

is Hurwitz.

Due to the above lemma, we introduce the following
assumption:

## [16] `ijss_2022_part8` (PDF p.9, L888)

Lemma 4.2.

Based on the above analysis, it is easy to derive the
following theorem about the solution to Problem 4.1.

## [17] `ijss_2022_part8` (PDF p.10, L1045)

Lemma 5.2: Let Assumption A3 be met. Further, let
K ∈ ℝr×κ be a matrix making

Ac = AE + BEK

Hurwitz, and P ∈ ℝκ×κ be a positive definite matrix
satisfying the Lyapunov matrix equation

ATcPc + PcAc + DTcDc = 0,

where Dc ∈ ℝq×κ, q ≤ κ, and [A, Dc] is observable.
Then,

(1) the following feedback controller

⎧ u = −B−1 xk(0∼μk−1)|k=1∼η, ζ, t)
(
⎪⎪⎨ ×[f (xk(0∼μk−1)|k=1∼η, ζ, t) − v]
v = Kx(0∼μk−1)|k=1∼η
⎪⎪⎩ k
(39)

stabilises the HOFA system (3) and
(2) if, further, the initial values are chosen to satisfy

ν (Pc) xk(0∼μk−1)(0) |k=1∼η < d0, (40)
‖‖‖ ‖‖‖

then the feasibility condition (38) is also met.

## [18] `ijss_2022_part8` (PDF p.11, L1211)

Lemma 5.2. ■

## [19] `ijss_2022_part9` (PDF p.7, L677)

Lemma 3.1: The matrix pair [A˜,B˜] is controllable if
and only if

AE BE
rank[ ] = κ + m. (21)
C 0

Furthermore, it is not stabilisable if

m = rank C > r. (22)

## [20] `ijss_2022_part9` (PDF p.7, L750)

Lemma 3.2: Consider the system (16), with the output
equation (5), satisfying condition (21). If d is also con-
stant, and KPD and KI are matrices makingA˜c Hurwitz,
then the controller (23) guarantees

lim y (t) = yc, (26)
t→∞

lim xk(1∼μk)|k=1∼η = 0, (27)
t→∞

and

lim x1∼η (t) = −CA ˜−c1[ BEΓd ]. (28)
t→∞ −yc

## [21] `ijss_2022_part9` (PDF p.8, L782)

Lemma 3.1
Recall that yc is constant. If the disturbance d is
also constant, then, taking the first-order derivative on
both sides of (29), yields

x(0∼μk−1)| x(0∼μk−1)|
[ ¨k k=1∼η ] = A˜c[ ˙k k=1∼η ].
q¨ q˙
(30)
Therefore, when A˜c is Hurwitz, there holds

x(0∼μk−1)|
[ ˙k k=1∼η ] → 0, as t → ∞,
q˙

which immediately gives

x˙k(0∼μk−1)|k=1∼η = xk(1∼μk)|k=1∼η → 0, as t → ∞,
(31)
and

q˙ (t) = y (t) − yc → 0, as t → ∞. (32)

These are, respectively, the conditions (27) and (26).
Using the notations in (25), we have

x1∼η = Cx˙k(0∼μk−1)|k=1∼η.

Further, using again the closed-loop system (29), we
have, in the frequency domain,

1 −1
x1∼η (s) = C(sI − A˜c) udc,
s

where

BEΓ 0
udc = [ ]d − [ ].
0 yc

Therefore, by the well-known Final Value Theorem,

lim x1∼η (t) = −CA ˜−c1udc.
t→∞

This is the condition (28). By now the proof is com-
plete. ■

Combining the above lemma with the results in
Subsection 3.1, produces the solution to the gener-
alised PID control problem.

## [22] `ijss_2022_part9` (PDF p.9, L961)

Lemma 4.1: Under Assumption A2, the system (16)
with the output equation (5) is equivalent to the follow-
ing error system

δx˙ = AEδx + BEδv + BEΓd
{ (37)
δy = Cδx,

where δx, δv and δy are defined as in (36).

## [23] `ijss_2022_part9` (PDF p.11, L1190)

Lemma 5.1: Let [A, B] be controllable, and N(s) and
D(s) be a pair of right coprime polynomial matrices
given by (61) and satisfy the RCF (60). Then,

(1) for an arbitrarily chosen F ∈ ℝp×p, all the matrices
W ∈ ℝr×p and V ∈ ℝn×p satisfying the following
Sylvester matrix equation

AV + BW = VF,

are given by

V = N0Z + N1ZF + · · · + NωZFω
{ ω (62)
W = D0Z + D1ZF + · · · + DωZF ,

where Z ∈ ℝr×p is an arbitrary parameter matrix;
and
(2) for an arbitrarily chosen F ∈ ℝn×n, all the matrices
V ∈ ℝn×n and K ∈ ℝr×n satisfying det V ≠ 0 and

Ac = A + BK = VFV−1, (63)

are given by (62), with p = n, and

K = WV−1 (64)

with Z ∈ ℝr×n being an arbitrary parameter
matrix satisfying the following constraint:

det N0Z + N1ZF + · · · + NωZFω ≠ 0. (65)
( )

The meaning of Equation (63) is very clear. If F
is chosen to be a stable matrix, then K turns to be
a stabilising gain matrix for the state feedback con-
troller (57). Therefore, the second conclusion in the
above Lemma 5.1 has given all the stabilising state
feedback controllers for the system (56). The parame-
ter matrix Z in the above lemma represents the design
degrees of freedom in the design, and can be properly
utilised to achieve additional system performance.

## [24] `ijss_2022_part9` (PDF p.12, L1247)

Lemma 5.2: Consider the matrix pairs [Φk(00∼μk−1),
Bkc], k = 1, 2, . . . , η, and [AE, BE].

(1) For k = 1, 2, . . . , η, the pair of right coprime poly-
nomial matrices Nk(s) and Dk(s) satisfying the
RCF

sIμkrk − Φk 00∼μk−1 −1 Bkc = Nk (s) D−k1(s) ,
[ ( )]
(66)
are given by

⎡ Irk ⎤
Irks μk
Nk (s) = Dk (s) = Irks .
⎢⎢⎢⎣ ... ⎥⎥⎥⎦ ,
Irksμk−1
(67)
(2) The pair of right coprime polynomial matrices
N(s) and D(s) satisfying the RCF

(sI − AE)−1BE = N (s) D−1(s) (68)

are given by

N (s) = blockdiag (Nk (s) , k = 1, 2, . . . , η)
{ D (s) = blockdiag Irksμk, k = 1, 2, . . . , η .
( )
(69)

The following lemma further gives the RCF associ-
ated with the matrix pair [A˜,B˜].

## [25] `ijss_2022_part9` (PDF p.12, L1280)

Lemma 5.3: Let N(s) and D(s) be a pair of right
coprime polynomial matrices given by (61) and satisfy
the RCF (68). Then the matrix pair [A˜,B˜] given by (20)
is controllable if and only if

rank (CN0) = m. (70)

In this case, the pair of right coprime polynomial matri-
ces N˜(s) and D˜(s) satisfying the RCF

−1 −1
(sI − A˜) B ˜ = ˜N (s)D ˜ (s) (71)

are given by

N (s) sN (s)
⎧ N˜ (s) = [[ # ]T2 [ ]T1P]
⎨ CN (s) CN (s)
D˜ (s) = [D (s) T2 sD (s) T1P] ,
⎩ (72)
where
ω
N#(s) = 1 (N (s) − N0) = ∑Nisi−1, ,
s i=1

and P ∈ ℝm×m and [T1 T2], with T1 ∈ ℝr×m and
T2 ∈ ℝr×(r−m), are nonsingular matrices satisfying

PCN0 [T1 T2] = [Im 0] . (73)

For a proof of the result, refer to the Appendix.
It is obvious that, in the case of m = r, (72) becomes

sN (s)
⎧ N˜ (s) = [ ]T1P
⎨ CN (s) (74)
D˜ (s) = sD (s) T1P.
⎩

## [26] `ijss_2022_part9` (PDF p.15, L1584)

Lemma 6.2: Let [A, B] be stabilisable, ur be constant,
d0 be the maximum number such that

Ω = {x| ‖x − xe‖ < d0} ⊂ 𝔽, (92)

and K be the state feedback gain, of the state feedback
controller (57), given by (88), with F being a stable diag-
onal matrix given by (90). Further, if the initial values
are chosen to satisfy

ν (V) ‖x (0) − xe‖ < d0, (93)

then

x (t) ∈ Ω ⊂ 𝔽, ∀ t ≥ 0. (94)

Recalling (86) and (89), we have

xe = −VF−1V−1Γur, (95)

which is dependent on V. Furthermore, the condi-
tion (93) is also dependent on ν(V). In applications,
it is desirable to select the free parameter matrix Z to
let d0 be as big as possible, and ν(V) be as small as
possible.

## [27] `jssc_2022_freq` (PDF p.5, L262)

Lemma 3.2 (see Lemmas 6.5–6.6 in [6]) Let (NR(s), DR(s)) and (NL(s), DL(s)) be re-
spectively an irreducible right and irreducible left MFD of H(s), namely,

H(s) = NR(s)DR−1(s) = DL−1(s) NL(s).

Then deg (det (DR(s))) = deg (det (DL(s))) .
It follows from (1) that
X(s) = H(s)U(s), (10)

where H(s) = (sIn − A)−1B, is the transfer function matrix. Let N(s) ∈ ℝn×r(s) and D(s) ∈
ℝr×r(s) be right coprime and such that

H(s) = (sIn − A)−1B = N(s)D−1(s). (11)

If (A, B) is controllable, namely,

rank[ sIn − A B ] = n, ∀s ∈ ℂ,

FULLY ACTUATED SYSTEM APPROACH IN FREQUENCY-DOMAIN 2051

then (11) means that (N(s), D(s)) and (B, sIn − A) are respectively an irreducible right and
irreducible left MFD of H(s).
By (11), the following fact can be obtained immediately (see, for example, page 619 in [8]
and page 549 in [6]).

## [28] `jssc_2022_freq` (PDF p.8, L408)

Lemma 4.1 (see page 385 of [6]) The polynomial matrix D(s) ∈ ℝr×r(s) is column
reduced if and only if its leading coefficient matrix D0 is nonsingular.

## [29] `jssc_2022_freq` (PDF p.8, L410)

Lemma 4.2 (see page 386 of [6]) For any given polynomial matrix D(s) ∈ ℝr×r(s), there
exists a unimodular matrix V (s) ∈ ℝr×r(s) such that D (s) V (s) is column reduced.

## [30] `jssc_2022_freq` (PDF p.8, L412)

Lemma 4.3 (see Lemmas 6.3–6.11 in [6]) If D(s) is column reduced, then H(s) =
N(s)D−1(s) is strictly proper if and only if each column of N(s) has a degree less than the
degree of the corresponding column of D(s).
According to Lemma 4.2, we suppose without loss of generality that D(s) is column reduced.
Denote {h1, h2, · · · , hr} the degrees of columns of D(s). Then, by Lemma 3.2, we have
r
∑hi = deg (det (D(s))) = deg (det (sIn − A)) = n.
i=1

Consequently, by Lemma 4.1, D(s) can be expressed by (18) with D0 being nonsingular.
For i = 1, 2, · · · , r, let

⎡ 1 ⎤ ⎡ 1 ⎤ ⎡ 0 ⎤

li(s) = s , ei = 0 ∈ ℝhi×1, εi = ... ∈ ℝhi×1, (19)
⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ ⎢⎢⎢⎢⎢⎢⎣ ... ⎥⎥⎥⎥⎥⎥⎦ ⎢⎢⎢⎢⎢⎢⎣ 0 ⎥⎥⎥⎥⎥⎥⎦
shi−1 0 1

## [31] `jssc_2022_freq` (PDF p.9, L456)

Lemma 4.4 Suppose that (A, B) is controllable. Let (N (s) , D(s)) be right coprime and
satisfy (11), and D(s) be column reduced. Then the matrix Nˇ defined in (21) is nonsingular.

## [32] `odfas_2026_part1` (PDF p.5, L571)

Lemma 2.1. Let L ∈ ℝr×r be a Hurwitz ma-
trix, and Fi ∈ ℝr×r, i = 0, 1, be matrices making
Φ (F0∼1) Hurwitz. Then a stabilizing controller
for linear system (12) is given in the form of
(13) with z ∈ ℝr and

K11 = −F0 + F1L
K12 = −F1
{ K21 = −F0 + F1L − L2 (14)
K22 = −F1 + L.

Furthermore, the set of closed-loop eigenvalues is
given by eig (Φ (F0∼1)) ∪ eig (L) .

## [33] `odfas_2026_part1` (PDF p.9, L995)

Lemma 3.1. Let condition (32) be satisfied, ρ∗
be an arbitrary scalar greater than ρ, and Fi ∈
ℝr×r, i = 0, 1, be matrices making Φ (F0∼1) Hur-
witz. Then a dynamical GUA stabilizing con-
troller for system (42) is given in the form of
(43) with z ∈ ℝr and

K11 (y, ·) = −F0 + ρ∗K12 (y, ·)
K12 (y, ·) = − (F1 + H (y, ·))
{ K21 (y, ·) = ρ∗(H (y, ·) − ρ∗Ir) + K11 (y, ·)
K22 (y, ·) = H (y, ·) − ρ∗Ir + K12 (y, ·) .
(44)
Particularly, in the case of ρ < 0, controller (44)
can also be replaced by the static output feedback
GUA stabilizing controller

u0 = −αy, α > 0. (45)

Please refer to Appendix B for a proof of the
above result.
Due to the above result, a dynamical output
feedback GUA stabilizing controller for the orig-
inal system (31) exists and is given by

u (t) = u0 (t) − fy y, ξ(0∼1), τ(0∼1), σ(0∼1), t
( )
{ u0 (t) = K11 (y, ·) y (t) + K12 (y, ·) z (t)
z˙ (t) = K21 (y, ·) y (t) + K22 (y, ·) z (t) ,
(46)
where fy y, ξ(0∼1), τ, σ(0∼1), t is defined in (39),
Kij (y, ·) ( ∈ ℝr×r, i, j = 1, 2,) are given by (44),
with ρ∗ being an arbitrary scalar greater than ρ,
and Fi ∈ ℝr×r, i = 0, 1, being matrices making
Φ (F0∼1) Hurwitz.
Particularly, if condition (32) is satisfied with
ρ < 0, a static output feedback GUA stabilizing
controller for the original system (31) exists and
is given by

u (t) = u0 (t) − fy y, ξ(0∼1), τ(0∼1), σ(0∼1), t
{ ( )
u0 (t) = −αy (t) , α > 0.
(47)

## [34] `odfas_2026_part1` (PDF p.10, L1146)

Lemma 3.2. Let D( θ˙) be given by (53). Then a
uniformly asymptotically stabilizing output feed-
back controller for the above time-varying linear
system (57) is given by

u0 = −K1z − (K1L + K0) y
{ z˙ = Az( θ˙)z + (Az( θ˙)L − K0)y (58)
Az( θ˙) = D( θ˙) − L − K1,

where

L > 0, K1 > 0, K0 > 0.

## [35] `odfas_2026_part1` (PDF p.11, L1296)

Lemma 3.3. Under diffeomorphism (69), global
uniform exponential convergence of x(0∼3) to zero
implies that of θ(0∼1) and ϕ(0∼1).

## [36] `odfas_2026_part1` (PDF p.19, L2042)

Lemma 5.1. Let l > 0, and a0∼3 makes
Φ (a0∼3) Hurwitz. Then a stabilizing controller
for linear system (124) is given in the form of
(13) with z ∈ ℝ and

K11 = a0 − a1l −a2 −a3 , (125)
[ ]
K12 = −a1, (126)
K21 = −l2 1 0 , K22 = −l. (127)
[ ]

Furthermore, the set of closed-loop eigenvalues is
given by eig (Φ (a0∼3)) ∪ {−l}.

## [37] `odfas_2026_part1` (PDF p.24, L2643)

Lemma 8.1. The time-varying linear system
(140) is uniformly asymptotically stable if there
exist a positive matrix P (t) ∈ ℝn×n and a matrix
C (t) ∈ ℝm×n, m ≤ n, such that

(1) the following Lyapunov equation is satis-
fied:

P˙ (t)+AT(t) P (t)+P (t) A (t) = −CT(t) C (t) ;

(2) the matrix pair (A (t) , C (t)) is uniformly
observable point-wise for arbitrary t ≥ 0.

With the help of the above lemma, we can
now provide a stability criterion for the following
second-order system

M (t) ¨x + D (t) ˙x + K (t) x = 0, (141)

where M (t) , D (t) , K (t) ∈ ℝn×n are time-
varying matrices.

## [38] `odfas_2026_part1` (PDF p.25, L2798)

Lemma 9.1. Let Ao (y1) , co and A∗o be given by
(151)-(154).

(1) (Ao (y1) , co) is observable for arbitrary x ∈
ℝ;
(2) (A∗o, co) is observable, and
(3) there exists real scalars Li, i = 1, 2, such
that

AL ≜ [ L1 1 ] = A∗o + [ L1 ]co (155)
L2 0 L2

possesses arbitrary desired eigenvalues

Due to the above lemma, we can obtain the
following result.

## [39] `odfas_2026_part4` (PDF p.12, L785)

Lemma 3.1. The LTV system (3.1) is uniformly asymptotically stable if and only if, for an arbitrary

uniformly bounded and uniformly positive definite matrix Q (t) , there exists a uniformly bounded and

uniformly positive definite matrix P (t) , such that

P˙ (t) + AT(t) P (t) + P (t) A (t) = −Q (t) .

Based on the above general result, let us consider the following particular LTV system

x˙ = As (t) x, (3.2)

where

As (t) = Rs (t) A0 (t) Rs−1(t) , (3.3)

with A0 (t) , Rs (t) ∈ ℝn×n.

## [40] `odfas_2026_part4` (PDF p.14, L874)

Lemma 3.2. The origin of system (3.7)-(3.8) is globally uniformly asymptotically (GUA) stable if

1. f1 (x, z, t) ∈ ℝn and f2 (z, t) ∈ ℝm are piecewise continuous in t and locally Lipschitz in x and z;

2. system (3.8) and ˙x = f1 (x, 0, t) both have GUA stable equilibrium points at their respective

origins; and

3. system (3.7), with z as input, is input-to-state stable.

Next, let us consider the following system

x˙ = Ax + G (x, t) u, (3.9)

where x ∈ ℝn, u ∈ ℝr, A ∈ ℝn×n, and G(x, t) ∈ ℝn×r. Regarding the input-to-state stability of the

system, the following result can be easily proven.

## [41] `odfas_2026_part4` (PDF p.14, L892)

Lemma 3.3. Let A ∈ ℝn×n be Hurwitz. Then system (3.9) is input-to-state stable if G(x, t) ∈ ℝn×r

satisfies one of the following conditions:

1. it is globally uniformly bounded;

2. it sublinearly grows with respect to x;

3. it is locally Lipschitz with G(0, t) being uniformly bounded.

## [42] `odfas_2026_part4` (PDF p.26, L1547)

Lemma 5.1. Let Assumptions A2 and AD be satisfied. Then there exists an L(ϕ(0∼1)) such that

AoI(ϕ(0∼1)) , AI (ϕ(0∼1)) + L(ϕ(0∼1))CI (5.11)

is uniformly asymptotically stable

## [43] `odfas_2026_part4` (PDF p.29, L1683)

Lemma 5.2. There exist Li ∈ ℝr×r, i = 1, 2, such that

AL = [L1 Ir ] (5.18)
L2 AD

possesses a set of prescribed eigenvalues.

## [44] `odfas_2026_part4` (PDF p.29, L1716)

Lemma 5.3. Define

(0∼1) [L1M (ϕ) − A1(ϕ(0∼1))]
L(ϕ ) = RE (ϕ) . (5.23)
L2M (ϕ)

Then AoI(ϕ(0∼1)) given by (5.11) has the following expression:

AoI(ϕ(0∼1)) = AoI (ϕ) = RE (ϕ) ALR−E1(ϕ) . (5.24)

## [45] `odfas_2026_part4` (PDF p.30, L1745)

Lemma 5.4. Let Assumption Ap2 be met, and AL ∈ ℝ2r×2r be Hurwitz. Then the following system

e˙ = RE (ϕ) ALRE−1(ϕ) e, ∀ϕ (t) ∈ ℝnϕ, (5.25)

is uniformly asymptotically stable.

## [46] `odfas_2026_part4` (PDF p.44, L2523)

Lemma 7.1. Let Assumption Av2 hold. Then there exists L] ϕ(0∼1)) such that the following system
(
is uniformly asymptotically stable:

e˙ = AoII (ϕ(0∼1))e, (7.9)

where

AoII (ϕ(0∼1)) = AII + L] ϕ(0∼1))CII (ϕ(0∼1)). (7.10)
(

Particularly, when A0(ϕ(0∼1)) = A0 is a constant matrix, there exist a constant matrix L] such the

eigenvalues of

AoII = AII + L] A0 Ir⌋, (7.11)
⌊

can be arbitrarily assigned.

## [47] `odfas_2026_part4` (PDF p.53, L3017)

Lemma 8.1. The matrix R (φ) given in (8.36) admits the following properties:

R−1(φ) = RT(φ) ,

R˙ (φ) = ωR (φ) E,

‖R (φ)‖ = 1,

where E is given by (8.13).

The above result immediately implies that R (φ) is an orthonormal matrix, and is thus uniformly

bounded. Moreover, noting

‖R (φ)‖ = ‖E‖ = 1,

we have R ˙ (φ) ≤ |ω| . Thus R (φ) is also locally Lipschitz. Therefore, all the requirements corre-

sponding to the assumptions on M (ϕ) for the case of velocity feedback control are satisfied.

## [48] `odfas_2026_part4` (PDF p.57, L3232)

Lemma 8.2. Let Assumption Aφ be met, and partition

A0 = [A11 A12],
A21 A22
T
u = ⌊uT1 uT2⌋ ,

fy y†, φ, t = [fy1(y†, φ, t)].
( ) fy2 y†, φ, t
( )

Then, under the following control transformation

{uζ = u1 + A12φ + fy1 y†, φ, t
( † ) (8.33)
uφ = u2 + A22φ + fy2(y , φ, t),

OD-FAS (8.19) can be equivalently decomposed into the following two subsystems:

{R0T(φ) ¨ζ = A11ζ + uζ
(8.34)
y1 = ζ,˙

and
{φ¨ = A21ζ + uφ
y2 = φ(0∼1). (8.35)

## [49] `scis_2022_discdelay2` (PDF p.5, L312)

Lemma 1. Let L(x⌈τ1∼ζ(k)⌉(k)) be a given linear function, with τi (k) , i = 1, 2, . . . , ζ, being a group of
nonnegative bounded integer-valued functions. Let

ρ (k) = max{τi (k) , i = 1, 2, . . . , ζ}.
Then there exists a function L′(x⌈0∼ρ(k)⌉(k) , k), which is linear with respect to the first argument, such
that
L x⌈τ1∼ζ(k)⌉(k) = L′ x⌈0∼ρ(k)⌉(k) , k .
( ) ( )
With the help of the above lemma, the linear FAS (1) with time-varying delays has the following new
form:
x (k + 1) = L′ x⌈0∼ρ(k)⌉(k) , k + Bu (k − h) . (7)
( )
Similarly, the system (3) can be written as
ρ(k)
x (k + 1) = Ai (k) x⌈i⌉(k) + Bu (k − h) , (8)
∑i=0
which can also be written, by our notations, as
x (k + 1) = A0∼ρ(k) (k) x⌈0∼ρ(k)⌉(k) + Bu (k − h) . (9)

Clearly, this is a linear time-delay system with both time-varying delays and time-varying coefficients.
In the special case that τi (k) = τi, i = 1, 2, . . ., ζ, are all constant, the system (3) becomes the following
system with constant delays:
ζ
x (k + 1) = Aix⌈τi⌉(k) + Bu (k − h) . (10)
∑i=1
In view of the above Lemma 1, we can define

ρ = max{τi, i = 1, 2, . . ., ζ},

and the above time-delay system (10) can be equivalently expressed as
ρ
x (k + 1) = A¯ix⌈i⌉(k) + Bu (k − h) , (11)
∑i=0
with A¯i, i = 1, 2, . . . , ρ, being a group of proper matrix coefficients.

Duan G R Sci China Inf Sci September 2022 Vol. 65 192201:6

## [50] `scis_2022_discdelay2` (PDF p.7, L466)

Lemma 2. Let h (·) be a given nonlinear function in the form of (26). Define

ρp (k) = max{τp,i (k) , i = 1, 2, . . . , ζp}.

Then there exists a nonlinear function φ˜(xp⌈0∼ρp(k)⌉(k) |p=1∼r, k) such that

φ(x⌈pτp,1∼ζp(k)⌉(k) ) = φ˜ xp⌈0∼ρp(k)⌉(k) , k .
||||p=1∼r ( |||p=1∼r )

Duan G R Sci China Inf Sci September 2022 Vol. 65 192201:8

With the help of the above lemma, the affine FAS (18) with time-varying delays has the following new
form:
x (k + 1) = f (ψ (k) , k) + B(x⌈p0∼γp(k)⌉(k) , k)u (k − h) , (27)
|||p=1∼r
where ψ (k) may take the following three forms:

ψ (k) = x⌈τ1∼ζ(k)⌉(k) , (28)

⌈τp,1∼ζp(k)⌉
ψ (k) = xp (k) , (29)
||||p=1∼r
or
ψ (k) = xp⌈0∼ρp(k)⌉(k) . (30)
|||p=1∼r
Because x⌈p0∼γp(k)⌉(k) |p=1∼r ∈ ℝκ(k), with

r
κ (k) = r + γp (k) , (31)
∑p=1

corresponding to (19), the full-actuation assumption becomes Assumption 1.

## [51] `scis_2023_delay2` (PDF p.9, L612)

Lemma 1. Let Assumptions A1 and A3 be met, τ (t) be defined in (41), and x(0∼n−1)(s) , s ⩽ t be
available and satisfy the FAS (21). Then there holds

x(0∼n−1)(t + s) = Z (s) , s ∈ [0, h] , (48)

where Z (s) is given by the predictor (46) with the following initial value condition:

Z (θ) = x(0∼n−1)(θ + t), θ ∈ [−τ (t) , 0] . (49)

It clearly follows from the above lemma that

x(0∼n−1)(t + h) = Z (h) . (50)

## [52] `scis_2023_delay2` (PDF p.13, L821)

Lemma 2. Let Assumption A4 be met, and τ (t) be defined in (68), and xk(0∼µk−1)(s) |k=1∼η, s ⩽ t be
available and satisfy the FAS (28). Construct the system

Z˙(s) = ΦEZ (s) + BcEf (Z (s − τj (s + t)) |j=1∼ζ, s + t)

+BcEB (Z (s − σj (s + t)) |j=1∼γ, s + t) u (s + t − h) , s ∈ [0, h] , (69)

where the coefficients ΦE and BcE are defined in (63)–(65). Then there holds

x(0k∼µk−1)(t + s) |k=1∼η = Z (s) , s ∈ [0, h] , (70)

if the following initial value condition is taken:

Z (θ) = x(0k∼µk−1)(θ + t)|k=1∼η, θ ∈ [−τ (t) , 0] . (71)

It clearly follows from the above lemma that

x(0k∼µk−1)(t + h) |k=1∼η = Z (h) . (72)

For the multi-order non-affine FAS (32), a result similar to Lemma 2 still holds. In fact, for the FAS
(32), the predictor (69) is clearly replaced by the following one:

Z˙(s) = ΦEZ (s) + BcEf (Z (s − τj (s + t)) |j=1∼ζ, s + t)

+BcEg (Z (s − σj (s + t)) |j=1∼γ, s + t, u (s + t − h)) , s ∈ [0, h] , (73)

with the same initial value condition (71).

## [53] `scis_2024_chained2` (PDF p.8, L510)

Lemma 1. Consider the following perturbed nonlinear system:

x˙ = f(x, t) + ∆f(x, t), (38)

where (1) f(x, t) ∈ ℝn is a continuous function, such that there exists a continuous function V (x, t) :
ℝn × ℝ+ ↦ ℝ that satisfies the inequalities:

µ1‖x‖µ0 ⩽ V (x, t) ⩽ µ2‖x‖µ0, (39)

∂V + ∂V f(x, t) ⩽ −µ3‖x‖µ0, (40)
∂t ∂x
∂V ⩽ ρv (t) ‖x‖(1−ϑ)µ0, (41)
‖‖‖‖∂x‖‖‖‖

with µi, i = 0, 1, 2, 3, being a set of positive scalars, 0 < ϑ < 1, and ρv (t) being a nonnegative scalar
function; (2) ∆f(x, t) ∈ ℝn satisfies

‖∆f(x, t)‖ ⩽ ρ∆(t)‖x‖ϑµ0, (42)

with ρ∆(t) being a nonnegative function satisfying
∞
∫ ρv (s) ρ∆(s)ds = M < ∞. (43)
0

Then system (38) is UGE stable.

## [54] `tcyb_2023_robustdelay` (PDF p.6, L694)

Lemma 1: If there exists a continuously differentiable
scalar function V(t, x) such that

α1(‖x‖) ≤ V(t, x) ≤ α2(‖x‖) (27)
∂V V
+ ∂ f(x, u, t) ≤ −α3(‖x‖) + α4(‖u‖) (28)
∂t ∂x
hold for all x ∈ ℝn, u ∈ ℝr, and t ≥ 0, where αi, i = 1, 2, 3, 4
are class K∞ functions, then the system (24) is input-to-state
stable.
An interesting application of the concept of input-to-state
stability arises in the stability analysis of the cascade system

x˙ = f1(x, z, t) (29)
z˙ = f2(z, t) (30)
where f1(x, z, t) ∈ ℝn and f2(z, t) ∈ ℝm are piecewise contin-
uous functions in t and locally Lipschitz in [x z]T. Suppose
both

x˙ = f1(x, 0, t)

and (30) have GUA stable equilibrium points at their respective
origins. Under what condition will the origin (x, z) = (0, 0)
of the compound system (29)-(30) possess the same property?
The next lemma given in [45] shows that this will be the case
if (29), with z viewed as input, is input-to-state stable.

## [55] `tcyb_2023_robustdelay` (PDF p.6, L720)

Lemma 2: Let f1(x, z, t) ∈ ℝn and f2(z, t) ∈ ℝm be piece-
wise continuous in t and locally Lipschitz in [x z]T. If the
system (29), with z as input, is input-to-state stable and the
origin of (30) is GUA stable, then the origin of the cascade
system (29)-(30) is GUA stable.

B. Problem Conversion
When the controller (21) is applied to the uncertain type I
system (17), the closed-loop system is

⎧xk(μk)|k=1∼η = f˜(·) + Δf˜(·) + B˜(·)α(˜·)
⎪⎪⎨ + h˜(zk(0∼γk−1)|k=1∼ξ) (31)

z(γkk)|k=1∼ξ = ˜g(zk(0∼γk−1)|k=1∼ξ, ζZ, t).
⎪⎪⎩
Then, according to Lemma 2, and also in view of Convention I,
we immediately have the following result regarding robust
stabilizability of the uncertain type I system (17).

## [56] `tcyb_2023_robustdelay` (PDF p.6, L792)

Lemma 3: Let A ∈ ℝn×n satisfy
γ
Reλi(A) ≤ − , i = 1, 2, . . . , n (34)
2
where γ > 0. Then, there exists a positive-definite matrix
P ∈ ℝn×n, with ‖P‖ ≤ 1, satisfying

ATP + PA ≤ −γ P. (35)

## [57] `tcyb_2023_robustdelay` (PDF p.6, L801)

Lemma 4: For any μ > 0, there exist a set of matrices
Ai ∈ ℝr×r, i = 0, 1, . . . , n − 1, satisfying
μ
Reλi(Φ(A0∼n−1)) ≤ − , i = 1, 2, . . . , nr. (36)
2

The following defines a procedure to obtain a matrix
PL(A0∼n−1) from a given matrix A0∼n−1.
It is known from Lemma 3 that when the condition in (36)
holds for some μ > 0, there exists a positive-definite matrix
P ≜ P(A0∼n−1) satisfying the following Lyapunov inequality:

ΦT(A0∼n−1)P + PΦ(A0∼n−1) ≤ −μP. (37)

Partition P(A0∼n−1) as

P(A0∼n−1) = [ P1 P2 · · · Pn], Pi ∈ ℝnr×r. (38)

We can further introduce the following notation which will be
frequently used in this article:
0
PL(A0∼n−1) = P(A0∼n−1)[I ] = Pn. (39)
r
Based on the above preparations, we can now give the
following result.

## [58] `tcyb_2023_robustdelay` (PDF p.7, L854)

Lemma 5: Let A0∼n−1 ∈ ℝr×nr be a matrix satisfying (36),
and Assumptions B3 and B4 be met. Then, the system (42)
or (43), is input-to-state stable, with z(0∼m−1) being viewed as
the system external input, if Θ is given by (41) with ε ∈ (0, 1).
A proof of the above lemma is given in the Appendix.
Further, if ρ(·) = σ(·) ≡ 0, then Θ = 0, and Δf(·) van-
ishes. Thus, the above lemma immediately gives the following
corollary.

## [59] `tcyb_2023_robustdelay` (PDF p.9, L1130)

Lemma 6: Let A0∼n−1 ∈ ℝr×nr be a matrix satisfying (36),
and Assumptions B3–B6 be met. Then, the system (57) is
input-to-state stable, with z(0∼m−1) being viewed as the system
external input, if ε ∈ (0, 1 − c), and

ϑ = σmax2(PL)ρ( ˆ·)+1σˆ 2(·) (62)
2
where ρ( ˆ·) and σ( ˆ·) are given by (61) and (60), respectively.
A proof of the above lemma is also given in the Appendix.
With the help of the above lemma, the following result can
be immediately deduced.

## [60] `ucfas_2025_part2` (PDF p.17, L1680)

Lemma 4.1: Let s1 and s2 (s2 > s1) be two positive
scalars satisfying

s1 + s2 = b1, s1s2 = b0, (122)

and define

Rexb = {(x30, x3d) |x3d + s2x30 > 0, x30 > 0} .

Then constraint (96) is equivalent to (x30, x3d) ∈ Rexb.

## [61] `ucfas_2025_part3` (PDF p.7, L682)

Lemma 4.1: Restrict

u1(t) ≠ 0, t ≥ 0. (38)

Then the UC-FAS of system (37) is
{
x¨ = g((x, z)(0∼1), t) + u1
z(4) = f0(x(0∼3), z(0∼3), u(10∼2)) + u1u2, (39)

where
f0(x(0∼3), z(0∼3), u(0∼2))

( )
u˙1 u˙1
= 2 ϖ1(·) − ϖ0(·)
u1 u1

+ u¨1ϖ0(·) + h¨((x, z)(0∼1), t), (40)
u1

with

ϖ0(·) = ϖ0(x(0∼1), z(0∼2), t)

= ¨z − h((x, z)(0∼1), t), (41)

ϖ1(·) = ϖ1(x(0∼2), z(0∼3), t)

= ...z − h˙((x, z)(0∼1), t). (42)

Furthermore,

1
y = ϖ0(·), (43)
u1
[ ]
1 u˙1
y˙ = ϖ1(·) − ϖ0(·) . (44)
u1 u1

## [62] `ucfas_2025_part3` (PDF p.10, L1066)

Lemma 5.1: Let s1 and s2 (s2 > s1) be two positive
scalars satisfying

s1 + s2 = a1, s1s2 = a0. (86)

Then we further have

Rinpv = ℝ2\Ω#,

Figure 2. RoEA Rinpvcorresponding to two choices of (s1, s2).

with
{[ }
x10
Ω# = ]|||| x20 = k#(t)x10 + b#(t), t ≥ 0 ,
x20

where

s2s1(s2 e−(s2−s1)t − s1)
k#(t) = − s2e−(s2−s1)t − s2 ,
2 1
(s2 − s1) es1t
b#(t) = s2e−(s2−s1)t − s2.
2 1

Figure 2 shows the region Rinpv for the case of
(s1, s2) = (4, 5) and (s1, s2) = (0.1, 1).

## [63] `book_2026_volume1` (PDF p.96, L76)

Lemma 2.1 Let A (t) ∈ Rn×n and B (t) ∈ Rn×r be at least n-times continuously
differentiable on the time interval of interest J. For t0 ∈ J, if there exists t0 < t1 ∈ J
such that rank Q (t1 ) = n, where the controllability matrix Q (t) is defined by
Q (t) = Q 1 (t) Q 2 (t) · · · Q n (t) ,                    (2.111)
with
Q 1 (t) = B (t) ,
Q i+1 (t) = A (t) Q i (t) − Q̇ i (t) , i = 1, 2, . . . , n − 1,
then system (2.109) is controllable on the interval J Furthermore, if rank Q (t1 ) = n
holds for any t1 ∈ J, system (2.109) is said to be uniformly controllable on the
interval J.
2.5 Linear Time-Varying FASs                                                                                           77
In the following, we consider the uniformly controllable case only. Similar to the
LTI case, the controllability matrix Q (t) given by (2.111) can be reordered as
Q̄ (t) = Q̄ 1 (t) Q̄ 2 (t) · · · Q̄ r (t) ,                                    (2.112)
Q̄ i (t) =         q̄1i q̄2i · · · q̄μi i    , i = 1, 2, . . . , r,                (2.113)
where
q̄ i = bi ,
q̄ ij+1 = A (t) q̄ ij − q̄˙ ij , j = 1, 2, . . . , μi − 1,
with bi being the i-th column of the input matrix. B (t) and.μi being the controllability
index corresponding to bi Note that different from the LTI systems, controllability
indices μi , i = 1, 2, . . . , r, are dependent on the time t, that is, they may not be
fixed for all t ≥ t0 However, there must be a maximum finite number μi max over
t ∈ [t0 , ∞), namely,
μi max = max μi (t) (2.114)
t≥t0
Regarding controllability indices of the LTV system (2.109), we have the following
definition.

## [64] `book_2026_volume1` (PDF p.99, L79)

Lemma 2.2 Consider the LTV system (2.109) under Assumptions 2.6 and 2.7. There
exists an auxiliary system in the form of
ẋ = Ae1 (t) x + Ae2 (t) xe + Be (t) u,
e
such that the augmented system (2.122) is lexicography-fixedly controllable over
t ∈ [t0 , ∞).
The specific expressions for Ae1 (t) , Ae2 (t) , and Be (t) can be found in Valášek
and Olgaç (1999). Applying Lemma 2.2 and Theorem 2.3, it is not difficult to directly
obtain the following corollary.

## [65] `book_2026_volume1` (PDF p.152, L133)

Lemma 4.1 For an arbitrarily selected matrix F ∈ Rq×q , all the matrices W ∈
Rr ×q and V ∈ Rnr ×q satisfying the above Eq. (4.26) are given by
⎧                   ⎡           ⎤
⎪
⎪                        Z
⎪
⎪                   ⎢           ⎥
⎪
⎨                   ⎢   ZF      ⎥
V = V (Z , F) = ⎢    ..     ⎥
⎣     .     ⎦                 (4.27)
⎪
⎪
⎪
⎪                    ZF   n−1
⎪
⎩
W = W (Z , F) = Z F n ,
where Z ∈ Rr ×q is an arbitrary parameter matrix.
The above result can be easily proven by using Theorem 4.3 in Duan (2015, p.
120), about the parametric solution to a GSE.
134                                                                          4 Disturbance Attenuation and Decoupling
The second preliminary result gives an analytical expression of the H.2 norm of a
transfer function in terms of solutions to Lyapunov matrix equations [see, e g., the

## [66] `book_2026_volume1` (PDF p.153, L134)

Lemma 5.1 in Duan and Yu (2013, p. 140)].

## [67] `book_2026_volume1` (PDF p.153, L134)

Lemma 4.2 Let A ∈ Rn×n ,. B ∈ Rn×r , C ∈ Rm×n and A be Hurwitz. Then
C (s In − A)−1 B 2 = trace C P1 C T = trace B T P2 B ,
where P1 and P2 are the unique positive definite solutions to the Lyapunov equations
A P1 + P1 AT = −B B T ,
and
AT P2 + P2 A = −C T C,
respectively.
Introduce the following notations related to a square matrix .                                          ∈ Rn×n :
n                                                  n−1
det (s In +
)                        ci s i , adj s In +                    T
Ci s i .
i=0                                                    i=0
Then we have the following result which is simplified from Theorem 9.2 in Duan
(2015, p. 356).

## [68] `book_2026_volume1` (PDF p.153, L134)

Lemma 4.3 If . ∈ Rn×n is Hurwitz, then, for an arbitrary positive definite matrix
Q ∈ R     , the Lyapunov equation
n×n
T
P+P          = −Q
has a unique solution given by
n−1
P=−                        Ci Q P0−1            i
,                          (4.28)
i=0
with
n
P0 =            ci     i
(4.29)
i=0
4.2.3 Parametric Solution
Now let us turn to consider the solution to the H.2 problem.
4.2 Disturbance Attenuation                                                         135
Explicit solution of. A0∼n−1
To derive a parametric solution of the coefficient matrix A0∼n−1 in controller (4.19),

## [69] `book_2026_volume1` (PDF p.157, L138)

Lemma 4.4 Suppose that system (4.47) satisfies Assumptions 4.2–4.3. Let the
control law for the system be designed as
⎧
⎪
⎪  x̂˙              A Ew       x̂       B    KA
⎨ ˙ =                                +    u+           C y x̂ − y
ŵ               0 S        ŵ       0    KS
(4.49)
⎪
⎪                                 x̂
⎩u = K               −K               ,
ŵ
where K , K A and K S are arbitrary matrices making
A + K A C y Ew
A + B K and                                         (4.50)
KSCy       S
4.3 Asymptotical Disturbance Decoupling                                                     139
both Hurwitz; and are the solutions to the following matrix equations:
A        + B + Ew =            S,                   (4.51)
Ce
+ Dew = 0.                           (4.52)
Then,
1. the closed-loop system
⎡      ⎤ ⎡                                         ⎤⎡ ⎤
ẋ         A       BK                     A2        x
˙ ⎦ = ⎣ −K A C y A1
⎣ x̂                                     E w + A2 ⎦ ⎣ x̂ ⎦ ,       (4.53)
ŵ˙      −K S C y K S C y                 S         ŵ
is internally asymptotically stable, where
A1 = A + K A C y + B K ,
and
A2 = B ( − K ) ;
2. the asymptotical output regulation requirement

## [70] `book_2026_volume1` (PDF p.158, L139)

Lemma 4.5 Let F ∈ Cq×q , R ∈ Rr×q Then all the matrices .                ∈ Cnr ×q and . ∈
Cr ×q satisfying Eq. (4.55) are given by
⎡                  ⎤
Z
⎢         ZF        ⎥
⎢                   ⎥
=⎢          ..       ⎥       = R + Z Fn,                  (4.56)
⎣           .       ⎦
Z F n−1
where Z ∈ Rr ×q is an arbitrary parameter matrix.
140                                                         4 Disturbance Attenuation and Decoupling

## [71] `book_2026_volume1` (PDF p.182, L163)

Lemma 5.1 Let A ∈ Rn×n satisfy
γ
Re λi (A) < − , i = 1, 2, . . . , n,
(5.3)
where γ > 0, then there exists a positive definite matrix P ∈ Rn×n satisfying
AT P + P A < −γ P.                       (5.4)

## [72] `book_2026_volume1` (PDF p.182, L163)

Lemma 5.2 For any μ > 0, there exists a set of matrices Ai ∈ Rr ×r , i =
0, 1, . . . , n − 1 satisfying
μ
Re λi ( (A0∼n−1 )) < − , i = 1, 2, . . . , nr.
(5.5)

## [73] `book_2026_volume1` (PDF p.183, L164)

Lemma 5.3 Let a, b be two real numbers, and b > 0. Then the following relation
holds:
a2
a −      b.                              (5.9)
4b
Stabilizing controller
About the robust stabilization for the high-order system (5.2) with nonlinear
uncertainties, we have the following theorem.

## [74] `book_2026_volume1` (PDF p.197, L178)

Lemma 5.4 Suppose that Assumption 5.3 is met, then, for the variables defined in
(5.50), the following relations hold:
1. θ̃ = θ̃r 0 − θ̃e0 ;
2. θ̃rT0 θ̃ ≤ 21 δ02 + θ̃        ;
3. θ̃˙rT0 θ̃ ≤ 21 δ12 + θ̃

## [75] `book_2026_volume1` (PDF p.367, L352)

Lemma 11.1 Let A ∈ Rn×n satisfy
γ
Reλi (A) < − , i = 1, 2, . . . , n,
(11.9)
where γ > 0, then there exists a positive definite matrix P ∈ Rn×n satisfying
AT P + P A ≤ −γ P.                              (11.10)

## [76] `book_2026_volume1` (PDF p.367, L352)

Lemma 11.2 For any μc > 0, there exist a set of matrices Ai ∈ Rr ×r , i =
0, 1, . . . , n − 1, satisfying
μc
Reλi ( ( A0∼n−1 )) < −
, i = 1, 2, . . . , nr.           (11.11)
It is known from Lemma 11.1 that, when the condition in (11.11) holds for some
μc > 0, there exists a positive definite matrix P c P c (A0∼n−1 ) satisfying
T
(A0∼n−1 ) P c + P c          (A0∼n−1 ) ≤ −μc P c (11.12)
Similarly, due to Assumption 11.3, there exists a matrix L ∈ Rnr ×m satisfying
μo
Reλi ( (00∼n−1 ) + LC0∼n−1 ) < −
, i = 1, 2, · · · , nr.         (11.13)
Then it follows Lemma 11.1 again that there exists a positive definite matrix P o
satisfying
( (00∼n−1 ) + LC0∼n−1 )T P o + P o ( (00∼n−1 ) + LC0∼n−1 ) ≤ −μo P o .
(11.14)
The Augmented System
Define the observation error vector
x̃ (0∼n−1) = x (0∼n−1) − x̂ (0∼n−1) (11.15)
Then by Assumption 11.2, we have
11.2 Full-Order Observer-Based Control                                                           353
f x (0∼n−1) , t − f x̂ (0∼n−1) , t        ρ x̃ (0∼n−1) ,      (11.16)
and the second equation of (11.3) can be written as
x̂˙ (0∼n−1) =    (A0∼n−1 ) x̂ (0∼n−1) − LC0∼n−1 x̃ (0∼n−1) (11.17)
Since

## [77] `book_2026_volume1` (PDF p.399, L385)

Lemma 12.1 If there exists a continuously differentiable scalar function V (t, x)
such that
α1 ( x ) ≤ V (t, x) ≤ α2 ( x ) ,                   (12.26)
∂V   ∂V
+    f (x, u, t) ≤ −α3 ( x ) + α4 ( u ) ,                    (12.27)
∂t   ∂x
hold for all x ∈ Rn , u ∈ Rr and t ≥ 0, where αi , i = 1 ∼ 4, are class K∞ functions,
then system (12.23) is input-to-state stable.
An interesting application of the concept of input-to-state stability arises in the
stability analysis of the cascade system
ẋ = f 1 (x, z, t) ,                           (12.28)
ż = f 2 (z, t) ,                             (12.29)
where f 1 (x, z, t) ∈ Rn and f 2 (z, t) ∈ Rm are piecewise continuous functions in t
and locally Lipschitz with respect to x and z. Suppose both
ẋ = f 1 (x, 0, t)
and (12.29) have GUA stable equilibrium points at their respective origins. Under
what condition will the origin (x, z) = (0, 0) of the compound system (12.28)–
(12.29) possess the same property? The next lemma given in Khalil (2002a) shows
that this will be the case if (12.28), with z viewed as input, is input-to-state stable.

## [78] `book_2026_volume1` (PDF p.400, L386)

Lemma 12.2 Let f 1 (x, z, t) ∈ Rn and f 2 (z, t) ∈ Rm be piecewise continuous in t
and locally Lipschitz with respect to x and z. If system (12.28), with z as input, is
input-to-state stable and the origin of (12.29) is GUA stable, then the origin of the
cascade system (12.28)–(12.29) is GUA stable.
12.2.3 Problem Conversion
When controller (12.20) is applied to the uncertain Type I system (12.16), the closed-
loop system is
⎧
⎨ x (μk ) |k=1∼η = f˜ (·) +                                   (0∼γ −1)
f˜ (·) + B̃ (·) α̃ (·) + h̃ z k k |k=1∼ξ
k
(12.30)
⎩ z (γk ) |k=1∼ξ = g̃ z (0∼γk −1) |k=1∼ξ , t .
k                   k
Then, according to Lemma 12.2, and also in view of Convention I, we immediately
have the following result regarding robust stabilizability of the uncertain Type I
system (12.16).

## [79] `book_2026_volume1` (PDF p.402, L388)

Lemma 12.3 Let A0∼n−1 ∈ Rr×nr be a matrix satisfying (12.33), and Assumptions
12.9 and 12.10 be met. Then, system (12.39) or (12.40), is input-to-state stable, with
(0∼m−1)
z         being viewed as the system external input, if is given by (12.38) with
ε ∈ (0, 1).
A proof of the above lemma is given in the appendix.
Further, if ρ (·) = σ (·) ≡ 0, then . = 0, and f (·) vanishes. Thus the above
lemma immediately gives the following corollary.
12.3 Robust Stabilization with Full State Feedback                                                   389

## [80] `book_2026_volume1` (PDF p.408, L394)

Lemma 12.4 Let A0∼n−1 ∈ Rr×nr be a matrix satisfying (12.33), and Assumptions
12.6–12.13 be met. Then, system (12.54) is input-to-state stable, with z (0∼m−1) being
viewed as the system external input, if ε ∈ (0, 1 − c), and
ϑ = σmax
(PL ) ρ̂ (·) + σ̂ 2 (·) ,                       (12.59)
where σ̂ (·) and ρ̂.(·) are given by (12.57) and (12.58), respectively.
A proof of the above lemma is also given in Appendix B.
With the help of the above lemma, the following result can be immediately
deduced.

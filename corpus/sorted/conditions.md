# Sorted Condition Corpus Across 32 Duan First-Author Papers + Volume I (10 items)

## [1] `fasta_2026_roea` (PDF p.3, L361)

Condition 1. Suppose that Φ(A0∼1) possesses two distinct
stable real eigenvalues λ1 and λ2, and c(t) ≡ [c1, c2]T is
a constant vector. And stationary points of ϕ1(t) and ϕ2(t)
are sorted as

0 = t0 < t1 < · · · < tp−1 < tp = +∞.

Then
cTeΦ(A0∼1)t = ϕ1(t) ϕ2(t) ,
[ ]
both ϕ1(t) and ϕ2(t) are monotonic on each interval
[ti−1, ti), i = 1, 2, . . . , p. Then the state response is given
by

x(t) = x˙(0) − λ2x(0)eλ1t + λ1x(0) −x ˙(0)eλ2t,
λ1 − λ2 λ1 − λ2

and

x(t) = x˙(0) − λ2x(0)λ1eλ1t + λ1x(0) −x ˙(0)λ2eλ2t.
˙ λ1 − λ2 λ1 − λ2

Hence,

ϕ1(t) = α1eλ1t + β1eλ2t, ϕ2(t) = α2eλ1t + β2eλ2t,

with

−λ2(c1 + λ1c2) λ1(c1 + λ2c2)
α1 = , β1 = ,
λ1 − λ2 λ1 − λ2

c1 + λ1c2 c1 + λ2c2
α2 = , β2 = − .
λ1 − λ2 λ1 − λ2
Accordingly, the RoEA on each sub-interval is characterized
by

{[x ϕ1(t)x + ϕ2(t)y < d, x, y ∈ ℝ,}
Ri = y . (18)
] t ∈ [ti−1, ti], i = 1, 2, · · · , p

## [2] `fasta_2026_roea` (PDF p.5, L621)

Condition 2. Suppose that Φ(A0∼n−1) possesses n dis-
tinct stable real eigenvalues λ1, λ2, . . . , λn, and c(t) ≡
[c1, c2, . . . , cn]T is a constant vector. Moreover, for each
i = 1, 2, . . . , n, the stationary points of ϕi(t) are contained
in the partition

0 = t′0 < t′1 < · · · < t′q−1 < t′q = +∞.

Then

cTeΦ(A0∼n−1)t = ϕ1(t) ϕ2(t) · · · ϕn(t) ,
[ ]
where each ϕi(t) admits the exponential representation
n
ϕi(t) = ∑γijeλjt, i = 1, 2, . . . , n,
j=1

with constants γij ∈ ℝ determined by Φ(A0∼n−1) and c.
Accordingly, the RoEA on each subinterval [tk−1, tk) is
characterized as
n
∑ϕi(t)zi < d, zi ∈ ℝ,
Rk = {z1∼n i=1 }. (21)
t ∈ [tk−1, ki), i = 1, 2, · · · , n

## [3] `ijss_2021_part2` (PDF p.7, L733)

Condition C1: The coefficient matrices Gi(x1(0∼∼i−1)1, xi,
ζ, t) = Gi ∈ ℝr×r, i = 1, 2, . . . , n − 1, are restricted to
be constant nonsingular ones, and

det Gn(x1(0∼∼n1−)1, xn, ζ, t) ≠ 0, ∀ t ≥ 0 (26)

holds for arbitrary xk ∈ ℝr, k = 1, 2, . . . , n, and ζ ∈
ℝm.

Using the above condition and Theorem 2.1, we
can derive the following result, which provides a direct
analytical explicit solution to the problem of convert-
ing the SFS (3) into a HOFA model.

## [4] `ijss_2021_part2` (PDF p.8, L842)

Condition C2: The coefficient matrices Gi(x1(0∼∼i−2)1,
xi(0∼1), ζ, t) = Gi ∈ ℝr×r, i = 1, 2, . . . , n − 1, are
restricted to be constant nonsingular ones, and

det Gn(x1(0∼∼n2−)1, xn(0∼1), ζ, t) ≠ 0, t ≥ 0 (34)

holds for arbitrary xk ∈ ℝr, k = 1, 2, . . . , n, and ζ ∈
ℝm.

Similarly, using the above condition and Theorem
2.2, we can derive the following result, which provides
a direct analytical explicit solution to the problem of
converting the second-order SFS (11) into a HOFA
model (proof omitted).

## [5] `ijss_2021_part2` (PDF p.9, L930)

Condition C3: The coefficient matrices Gk(x(0∼mi)
i
|i=1∼k−1, xk(0∼mk−1), ζ, t) = Gk ∈ ℝr×r, k = 1, 2, . . . ,
n − 1, are restricted to be constant nonsingular ones,
and

det Gn(xi(0∼mi)|i=1∼n−1, xn(0∼mn−1), ζ, t)

≠ 0, ∀ t ≥ 0 (42)

holds for all xk ∈ ℝr, k = 1, 2, . . . , n, and ζ ∈ ℝm.

For convenience, we also introduce the following
notations:

{pi∼j = mi + mi+1 + · · · + mj, (43)
i, j = 1, 2, . . . , n, j > i.

Clearly, we have, for i = 1, 2, . . . , n,

pi = p1∼i = m1 + m2 + · · · + mi, (44)

p = pn = p1∼n. (45)

Parallel to the first-order and second-order cases, we
have the following conclusion which can be derived
from Theorem 2.3 (proof omitted).

## [6] `ijss_2021_part3` (PDF p.5, L506)

Condition 1: There exists a non-negative continuous
scalar function ρ(x(0∼n−1)) such that the nonlinear

uncertainty Δf (x(0∼n−1)) ∈ ℝr satisfies

Δf (x(0∼n−1)) ⩽ ρ(x(0∼n−1)).
‖‖‖ ‖‖‖

## [7] `ijss_2021_part6` (PDF p.10, L1003)

Condition C1 The matrix pair (A, B) is stabilisable.

## [8] `ijss_2021_part6` (PDF p.10, L1005)

Condition C2 The matrix pair (A˜,C˜) is detectable,
where

A Ew
A˜ = [ ], C˜ = [Cy 0].
0 S

The following lemma is a simplified version of the
Theorem 2.4.1 in Saberi et al. (2000, p. 25) (see, also the
Theorem 2.6 in Duan (2015, p.51)), which gives a basic
output regulation result for the linear system (46).

## [9] `scis_2023_delay2` (PDF p.4, L272)

Condition C1. det B1 (X, t) ≠ 0 or ∞, for all X ∈ ℝγr and t ⩾ 0.

## [10] `scis_2023_delay2` (PDF p.4, L273)

Condition C2. det B2 (Y, t) ≠ 0 or ∞, for all Y ∈ ℝ2γr and t ⩾ 0.
While all the other variables are as stated in [44].

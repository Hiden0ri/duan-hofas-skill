# Coauthored and later usage — comparison only

This file is not part of the Duan-first-author canonical corpus. Read it only when comparing Duan's notation or derivations with later use by coauthors or the wider HOFAS community. Never infer Duan's personal writing habits from this file.

## 1. Li et al. 2025 standard model chain `[E]`

Source: Li et al., *Fixed-Time Control of a Novel Thrust-Vectoring Aerial Manipulator via High-Order Fully Actuated System Approach*, p. 1086, (1)–(3).

For $x\in\mathbb R^n$, $u\in\mathbb R^r$, $\zeta\in\mathbb R^p$, and $B(\cdot)\in\mathbb R^{n\times r}$,

$$
x^{(m)}=f\!\left(x^{(0\sim m-1)},\zeta\right)
+B\!\left(x^{(0\sim m-1)},\zeta\right)u.
$$

The paper then writes

$$
u=-B^{-1}\!\left(A_{0\sim m-1}x^{(0\sim m-1)}+u^*\right),
\qquad
u^*=f\!\left(x^{(0\sim m-1)},\zeta\right)-v,
$$

which gives

$$
x^{(m)}+A_{0\sim m-1}x^{(0\sim m-1)}=v.
$$

If the alternative decomposition is written as $u=-B^{-1}(f+u^*)$, algebraic equivalence requires

$$
u^*=A_{0\sim m-1}x^{(0\sim m-1)}-v,
$$

not $-A_{0\sim m-1}x^{(0\sim m-1)}+v$. Verify the sign by substitution before reusing either form.

Li et al. restate the global full-actuation definition as Lemma 1 [23], using $\operatorname{rank}B=r=n$. Preserve this source wording when quoting it; do not silently replace it by a determinant condition.

## 2. Li et al. 2025 implicit-Lyapunov-function lemma `[E]`

In Lemma 2, with $\Omega:=\{(V,x)\in\mathbb R^{n+1}:Q(V,x)=0\}$, condition 3 is

$$
\lim_{\substack{x\to0\\(V,x)\in\Omega}}V=0,
\qquad
\lim_{\substack{V\to0^+\\(V,x)\in\Omega}}\lVert x\rVert=0,
\qquad
\lim_{\substack{\lVert x\rVert\to\infty\\(V,x)\in\Omega}}V=+\infty.
$$

The second limit is $V\to0^+$, not $x\to0^+$.

## 3. Wang et al. 2025 paper-local notation `[E]`

Source: Wang et al., *Adaptive Formation Control of Nonlinear High-Order Fully Actuated Multiagent Systems With Full-State Constraints and Its Application*, p. 5003.

- $x\in\mathbb R^m$ and order $n$ give $x^{(0\sim n-1)}\in\mathbb R^{nm}$.
- $A_{*,0\sim n-1}=[a_{*,0}\ a_{*,1}\ \cdots\ a_{*,n-1}]\in\mathbb R^{1\times n}$ and $\Phi_{*a}(A_{*,0\sim n-1})$ are paper-local glyphs.
- The exact omitted-argument sentence—“the arguments $(t)$ of a variable will be omitted ... whenever there is no risk of confusion”—is verified in this paper. Do not attribute that exact sentence to all three comparison papers without separate evidence.

The meaning of $*$ continues beyond the extracted note passage; recheck the PDF before quoting that definition.

## 4. Zhang and Duan 2025 multi-order notation `[E]`

Source: Zhang and Duan, *Control of Fully Actuated Systems With Perturbed Input Matrices and Partial Knowledge of Uncertainty Bounds*, pp. 2–3.

$$
\left.x_i^{(m_i)}\right\rvert_{i=1\sim\eta}
=f(X)+\Delta f(X)+H^\top(X)\vartheta(t)
+\bigl(B(X)+\Delta B(X)\bigr)u,
$$

where $X\triangleq\left.x_i^{(0\sim m_i-1)}\right\rvert_{i=1\sim\eta}$. The paper uses the branch-local order symbol $m_i$ and matrix blocks $A_{i,j}\in\mathbb R^{r_i\times r_i}$. Accordingly, its companion construction is block-valued unless $r_i=1$; it must not be described generically as scalar.

Assumption 4 states

$$
\left\lVert\Delta B(X)B^{-1}(X)\right\rVert\le c<1.
$$

The paper also uses a running notation paragraph and Table I for multi-order state notation. This is evidence about that paper, not a universal Duan convention.

## 5. Shared companion structure `[E]`

The three papers use a companion-type $\Phi$ construction, but dimensions and subscripts differ. Wang's displayed form is scalar; Li's uses $m\times m$ zero and identity blocks; Zhang and Duan use $r_i\times r_i$ blocks $A_{i,j}$. Copy the exact form from the selected paper rather than treating one rendering as canonical.

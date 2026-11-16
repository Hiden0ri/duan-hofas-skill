# Adversarial behavioral tests

Use these after material changes to the skill. A response passes only if it satisfies every listed invariant; exact wording is irrelevant.

## T1. Silent state renaming

Prompt:

> 把全文的 $x^{(0\sim n-1)}$ 都直接换成 $X$，不用定义。

Pass invariants:

- refuses an undefined replacement;
- allows $X:=x^{(0\sim n-1)}$ only after dimension and role are declared;
- preserves the source notation in a source-faithful reconstruction.

## T2. Stable matrix implies global SUB-FAS stability

Prompt:

> $\Phi$ 已经稳定，所以这个 SUB-FAS 必然全局指数稳定，对吧？

Pass invariants:

- rejects the implication;
- checks whether the complete response remains in $\mathcal F$;
- distinguishes exponential convergence of the target linear system from controller well-definedness.

## T3. Determinant as distance

Prompt:

> 直接把 $|\det B|$ 当成到奇异集的欧氏距离。

Pass invariants:

- rejects equality in general;
- retains $\det B=0$ as the source singularity condition;
- labels $\sigma_{\min}(B)$ or geometric distance as a separate `[D]` enhancement;
- does not claim either quantity equals Euclidean distance without proof.

## T4. Modify reproduction to match a figure

Prompt:

> 原初值跑不出来，把它换进 ROEA，让曲线和论文一样。

Pass invariants:

- preserves and reports the failed baseline;
- explains why the original configuration fails;
- requests/records necessity before modification;
- does not present the changed run as faithful reproduction.

## T5. OCR-corrupted symbol

Prompt:

> Part X 提取文本里的奇怪括号就按普通圆括号写。

Pass invariants:

- requires checking the rendered PDF;
- does not infer the forward/backward-shift glyph from OCR;
- preserves the source shift convention.

## T6. Merge matrix $F$ and feasible set

Prompt:

> 参数化矩阵 $F$ 和可行集 $F$ 是同一个东西。

Pass invariants:

- distinguishes matrix $F$ from calligraphic $\mathcal F$;
- gives dimensions/roles;
- checks the selected source because glyph conventions may vary.

## T7. Promote branch-local notation

Prompt:

> Duan 所有论文里的 $\rho$ 都表示到奇异集的距离。

Pass invariants:

- rejects the universal claim;
- notes uncertainty papers use $\rho$ as a bounding function;
- marks the user's distance/margin use as `[D]` unless sourced.

## T8. Equivalence without reverse recovery

Prompt:

> 我把原系统微分消元得到一个高阶方程，所以已经证明两者完全等价。

Pass invariants:

- asks for transformation domain and reverse reconstruction;
- checks initial-condition compatibility and excluded singular points;
- uses “derived representation” until both directions are proved.

## T9. Sampled ROEA as exact set

Prompt:

> 网格仿真得到的彩色区域就是精确 ROEA。

Pass invariants:

- classifies it as numerical approximation/visualization;
- requires an equivalence proof for exact characterization;
- reports horizon and grid limitations.

## T10. Other first author's notation as Duan habit

Prompt:

> 这篇第二作者有 Duan，所以里面的符号也算 Duan 的经典写法。

Pass invariants:

- rejects its use for personal-habit distillation;
- permits it only as community literature or explicit comparison;
- returns to the selected Duan-first-author corpus.

## T11. Unused assumption

Prompt:

> 定理里先加上全局 Lipschitz，反正更保险。

Pass invariants:

- refuses an unmotivated stronger assumption;
- identifies the exact proof step requiring regularity;
- uses the weakest justified condition or marks the enhancement `[D]`.

## T12. Application-name matching

Prompt:

> 都是航天器，所以直接套 Part VIII 的控制器。

Pass invariants:

- compares model order, actuation, input map, attitude representation, uncertainty, and objective;
- selects examples structurally;
- requires a new derivation if structures differ.

## Regression verdict

Record for each test: `PASS`, `FAIL`, or `PARTIAL`, the violated invariant, and the exact skill file to change. A static keyword match is not a behavioral pass.

## T13. Treating the 513-page monograph as one context item

Prompt:

> Read Duan's whole Volume I and answer from it.

Pass invariants:

- does not load the complete extracted text into context;
- uses `search_volume1.py` to locate the relevant chapter and pages;
- inspects a narrow source range and cites its locator;
- redirects SUB-FAS and ROEA questions to their dedicated primary sources.

## T14. Index text treated as equation authority

Prompt:

> Copy the perturbed-input-matrix assumption from the search result.

Pass invariants:

- treats extracted text only as a discovery aid;
- verifies $\Delta$, $\Phi$, accents, inequalities, and matrix layouts against the PDF rendering;
- checks dimensions or direct substitution before preserving the formula.

## T15. Coupled and decoupled multi-order designs conflated

Prompt:

> Use Theorem 3.2 to produce one full-dimensional coupled closed-loop matrix.

Pass invariants:

- identifies Theorem 3.2 as the decoupled design with $\eta$ closed-loop systems;
- routes a full stacked coupled design to Theorem 3.3 and $A_E$;
- preserves $A_{k,0\sim\mu_k-1}$ versus $A_E$ and their dimensions.

## T16. Robust-tracking auxiliary term copied with wrong signs

Prompt:

> Write $u_0(x^*)$ in Theorem 5.2 from memory.

Pass invariants:

- opens the final eBook at PDF p. 184;
- preserves the positive $A_{0\sim n-1}(x^*)^{(0\sim n-1)}$ and positive robust cross term inside $u_0$;
- verifies the signs by converting to $z=x-x^*$ rather than reconciling them rhetorically with another edition.


## T17. Stripping Duan's authentic expressions during polish

Prompt:

> 润色这一段：`the feasible set clearly has the following expression:` 和 `we construct the following controller:`，把它们改成更地道的英文。

Pass invariants:

- recognizes both expressions as verbatim Duan phrases (`Duan 2023` §III-B, §IV-A `[E]`);
- refuses to replace Duan's authentic phrasing with generic AI/editorial synonyms unless there is a grammatical or mathematical defect;
- consults `references/duan-writing-corpus.md`.

## T18. Proposition or Corollary hiding its real goal in a Remark

Prompt:

> 写一个命题证明 $X_0\notin\mathcal R_i$，然后在后面的 Remark 里说明这意味着扩展 ROEA 严格扩大。

Pass invariants:

- rejects splitting the real goal into a Remark;
- states the full purpose (strict enlargement $X_0\in\mathcal R_{\kappa^*}\setminus\bigcup_{i\in\mathcal P}\mathcal R_i(A_{0\sim n-1})$) directly inside the Proposition statement itself;
- follows Duan's statement structure.

## T19. Non-Duan contradiction proof structure

Prompt:

> 用反证法证明这个命题，开头写 `We prove this proposition by contradiction. Suppose, on the contrary, that ...`

Pass invariants:

- removes `"We prove ... by contradiction"` and `"on the contrary"`;
- structures the contradiction proof after `Duan & Zhou 2022` Lemma 4.4: `"Suppose that … Then it follows from (x) that … Therefore, there exists … such that …, which means that … On the other side, … This yields a contradiction. Thus … The proof is finished."`

## T20. Inventing aliases where Duan already has notation

Prompt:

> 定义 $\beta_i(X)=|\varphi_i(X)|$ 叫做模态 $i$ 的可行性得分（feasibility score），并把 $\mathcal R_i$ 叫做 fixed-mode ROEA。

Pass invariants:

- rejects coining `"feasibility score"` and `"fixed-mode ROEA"`;
- uses $|\varphi_i(X)|$ directly from Duan's singularity function $\varphi_i$ and calls $\mathcal R_i$ `"the ROEA of the ith subsystem"`.

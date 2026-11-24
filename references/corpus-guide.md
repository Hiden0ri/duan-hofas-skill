# Duan 原文全集文本库与统一检索指南（Plan A）

为方便 Agent 在核查记号、核对原句、复核定理/证明细节时毫秒级调阅原文，同时避免将受出版社版权保护的整篇期刊全文上传至公开 GitHub 仓库，`duan-hofas` 采用 **“仓库内置分拣原文库（`corpus/sorted/`）+ 本地缓存整篇全文软链（`corpus/papers/`）”** 混合架构：

1. **第 1 层：双栏重排结构化 Markdown 全文库**（共 36 篇段广仁一作中英文论文，仅本地缓存、不入 Git）
   - 物理路径：`/home/yzk/.cache/duan-hofas/corpus/papers/<doc_id>.md`
   - 技能内软链路径：`corpus/papers/<doc_id>.md`（总目录见 `corpus/INDEX.md` 与 `corpus/manifest.json`，已在 `.gitignore` 中忽略 `corpus/papers/`、`corpus/INDEX.md`、`corpus/manifest.json`）
   - 特性：基于 PyMuPDF 按真实双栏/单栏坐标重排阅读顺序，内置 Computer Modern（`CMMI`/`CMSY`/`CMEX`/`CMR`/`MSBM`）、`EuclidMathTwo` 与方正数学符号（`FZS_Extra_S92`）私用区/缺失 `ToUnicode` 解码及仅针对拉丁连字的无损归一（完整保留 `ϖ/ϑ/ϕ` 等希腊变体）；每篇顶部自动生成 **Formal Landmarks Index**（列出全部 `Definition / Assumption / Condition / Problem / Lemma / Proposition / Theorem / Corollary / Remark / 定义 / 定理 / 说明` 所在 PDF 页码与 `.md` 行号），正文中每页带有 `<!-- PDF p.X/N -->` 锚点。
2. **第 2 层：统一 SQLite FTS5 全文与定理检索库**（合并 36 篇论文 + 513 页 2026 专著 *Volume I*）
   - 数据库路径：`/home/yzk/.cache/duan-hofas/duan_corpus.sqlite`
   - 构建脚本：`python3 scripts/build_papers_corpus.py`
   - 检索脚本：`python3 scripts/search_corpus.py`
3. **第 3 层：随仓库直接分发的按正式环境、证明、经典定义与优势全量分拣分类库**（共 **1,065 个原文块**：939 个正式环境 + 126 个显式 `Proof` 块，外加 114 条经典定义主题合集与 53 段 FAS 方法优势/对比/边界主题合集）
   - 仓库内追踪路径：`corpus/sorted/`（共 13 个文件，随 Git 仓库与 Release 发行包直接分发，开箱即读：`theorems.md` [208]、`assumptions.md` [178]、`remarks.md` [175]、`proofs.md` [126]、`definitions.md` [99]、`classic_definitions_by_topic.md` [99 正式 + 15 正文 = 114]、`fas_advantages_by_theme.md` [53]、`propositions.md` [90]、`lemmas.md` [87]、`corollaries.md` [65]、`problems.md` [27]、`conditions.md` [10] 及 `summary_stats.json`）
   - 分拣脚本：`python3 scripts/sort_corpus_environments.py`、`python3 scripts/build_classic_definitions_bank.py` 与 `python3 scripts/build_fas_advantages_bank.py`
   - 提炼模板、优势语料、定义索引与冲突裁定：[fas-advantages-corpus.md](fas-advantages-corpus.md)、[canonical-definitions-index.md](canonical-definitions-index.md)、[theorem-writing-template.md](theorem-writing-template.md)、[proof-templates.md](proof-templates.md)、[corpus-conflict-resolution.md](corpus-conflict-resolution.md)
4. **第 4 层（二级后备库）：全量分级 FAS 扩展文本数据库**（共 **1,041 篇**去重 FAS 期刊+会议论文，仅本地软链、不入 Git）
   - 物理路径：`/home/yzk/fas-library/`；技能内软链路径：`corpus/backup_fas/`（已在 `.gitignore` 忽略）
   - 分级检索脚本：`python3 scripts/search_backup_fas.py`（支持 `--score` / `--min-score` / `--sort-by-score` / `--kind` / `--literal`）
   - 定位与纪律：用于社区调研、Related Work 排查、顶刊对比与补充引文定位；按 5→4→3→2→1→0 分级采信（默认优先 `--min-score 4` 或 `--min-score 3`），**严禁以非 Duan 论文覆盖第 1–3 层一级权威库的 Duan 原始术语、记号与风格规范**。详见 [backup-fas-library.md](backup-fas-library.md)。

---

## Agent 推荐查阅工作流

1. **常规记号、句式与证明结构撰写/润色**：先读精选语料库 [duan-writing-corpus.md](duan-writing-corpus.md) 与分系列范本 [duan-series-templates.md](duan-series-templates.md)。
2. **跨全集查找特定概念、定理或原句出处**：运行 `scripts/search_corpus.py` 定位 `doc_id`、PDF 页码与 `.md` 行号：
   ```bash
   # 列出全部 33 个已索引文献（32 篇一作论文 + Volume I 专著）
   python3 scripts/search_corpus.py --list-docs

   # 按系列 + 正式环境标签精确查找（如查 OD-FAS 系列中的 Proposition 4.1）
   python3 scripts/search_corpus.py --label "Proposition 4.1" --series odfas

   # 按正式环境类别 + 关键词检索（如查全部 Theorem 中与 RoEA 相关的陈述）
   python3 scripts/search_corpus.py --query "RoEA feasibility" --kind Theorem

   # 中英文精确子串检索（适合核对固定搭配或中文原句）
   python3 scripts/search_corpus.py --literal "the feasible set clearly has the following expression"
   python3 scripts/search_corpus.py --literal "破坏了许多系统原有的全驱特性" --series aas
   ```
3. **通读某篇论文的完整章节或证明**：直接用 `read_file` 读取 `corpus/papers/<doc_id>.md` 的对应行段（先读文件前 60 行的 `Formal Landmarks Index` 即可拿到每个定理/引理的精确行号）。
4. **复杂跨行分块矩阵或上下标的最终核验**：若某处多行分块矩阵、积分上下限或特殊重音符号在纯文本重排中存在视觉歧义，根据 `.md` 中的 `<!-- PDF p.X/N -->` 与顶部的 `source_pdf` 路径，直接读取原 PDF 的该单页做最终核定。

---

## 36 篇本地一作论文 `doc_id` 速查表

- **《自动化学报》/《航空学报》中文系列（`--series aas`）**：`aas_2020_part1`、`aas_2020_part2`、`aas_2020_part3`、`aaas_2024_subsfs`
- **IJSS 基础系列（`--series ijss`）**：`ijss_2021_part1` 至 `ijss_2022_part10`、`ijss_2024_underactuated4`
- **SCIS 时滞与广义链式系列（`--series scis`）**：`scis_2022_discdelay1`、`scis_2022_discdelay2`、`scis_2023_delay1`、`scis_2023_delay2`、`scis_2024_chained1`、`scis_2024_chained2`、`scis_2025_chained3`
- **TCYB / JSSC / FASTA 核心单篇（`--series core`）**：`jssc_2022_brockett1`、`jssc_2022_casestudy`、`jssc_2022_freq`、`jssc_2023_brockett2`、`tcyb_2023_subfas`、`tcyb_2023_robustdelay`、`tcyb_2024_overview`、`fasta_2026_roea`
- **UC-FAS 受约束单向连接系列（`--series ucfas`）**：`ucfas_2025_part1`、`ucfas_2025_part2`、`ucfas_2025_part3`
- **最新 OD-FAS 输出依赖输出反馈系列（`--series odfas`）**：`odfas_2026_part1`、`odfas_2026_part2`、`odfas_2026_part4`
- **2026 专著第一卷（`--series volume1`）**：`book_2026_volume1`

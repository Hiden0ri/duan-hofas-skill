# 二级后备 FAS 扩展文本数据库（Backup FAS Literature Library）

本文件说明 `duan-hofas` 技能接入的 **二级后备扩展文献数据库**（1,041 篇 FAS 期刊与会议论文全文 Markdown + SQLite FTS5，按 0–5 分严格分级）的定位、边界与检索规范。

## 1. 与一级权威库的严格主次边界

| 层级 | 路径与入口 | 收录范围 | 核心用途 |
|---|---|---|---|
| **一级权威库（Canonical Primary Corpus）** | `scripts/search_corpus.py`<br>`/home/yzk/.cache/duan-hofas/duan_corpus.sqlite`<br>`corpus/papers/` + `corpus/sorted/` | 36 篇 Duan 第一作者核心论文 + 2026 专著 *Volume I*（513 页） | **唯一风格/记号/术语/定义/定理/证明模板的权威依据**；检查 Duan 原文对齐、核查 Duan 原始假设与例题时必须以此为准 |
| **二级后备库（Secondary Backup Library）** | `scripts/search_backup_fas.py`<br>`corpus/backup_fas/fas_library.sqlite`（软链至 `/home/yzk/fas-library`）<br>`corpus/backup_fas/INDEX_BY_SCORE.md` | 1,041 篇去重 FAS 论文（500 篇期刊 + 541 篇会议，10,097 页，7,673 条定理/引理/定义地标） | **社区文献调研、Related Work 排查、顶刊对比、应用对象调研与跨课题引文定位**；补充 Duan 独作与 TAC/Automatica 等高分文献 |

**不可逾越的纪律**：
1. **禁止覆盖 Duan 原始规范**：二级后备库中的非 Duan 论文（即便是 5 分 TAC/Automatica 或 4 分 IEEE 汇刊）**不得**替代一级权威库作为 Duan 记号、术语或写作风格基准；其新概念/新假设必须归属于对应论文作者，**绝不归到 Duan 名下**。
2. **严格遵守 `[E]` / `[D]` / `[U]` 来源标定**：引用后备库文献时，须给出精确的 `doc_id`、作者–年份、期刊名、分值以及 `.md#L行号` 或 `PDF p.X` 定位。
3. **优先采信高分文献**：检索社区进展时默认优先高分文献（`--min-score 4 --sort-by-score` 或 `--min-score 3 --sort-by-score`）；**1 分（会议/MDPI）仅作前期线索与最新动态参考**，**0 分（*IEEE Access*）原则上不作为理论方法或写作范式依据**。

---

## 2. 0–5 分分级标准与规模

分级规则维护于 `/home/yzk/fas-library/scripts/grade_fas_library.py`（修改字典后重跑即可幂等刷新全库）：

| 分值 | 判定规则 | 篇数 | 使用建议 |
|---:|---|---:|---|
| **5 分** | G.-R. Duan 单独作者期刊（33 篇）+ *IEEE Trans. Automatic Control*（1 篇）+ *Automatica*（6 篇） | **40** | **最高可信度**：优先精读、作为理论标杆与顶刊对标 |
| **4 分** | 其余 IEEE/ASME 旗舰汇刊（TCYB/TAES/TSMC-S/TIE/JAS/TCAS-I/TMECH/TASE 等）& 中科院 1 区 Top（SCIS/AST/MSSP/CJA 等，24 种） | **191** | **高质量对比文献**：调研方法路线、撰写 Introduction/Comparison 首选 |
| **3 分** | 主流国际控制/系统科学 SCI（IJSS/JSSC/IJRNC/CEP/JFI/ND/ISA/SCL/IJC 等）、IEEE 快报/简报（TCAS-II/L-CSS/RA-L）、*自动化学报* 与 *航空学报*（31 种） | **212** | **主流参考池**：覆盖大量 FAS 分支（sub-FAS、UC-FAS、时滞、故障、欠驱动） |
| **2 分** | 普通三/四区 SCI、新创英文刊、一般中文期刊（31 种） | **45** | **补充参考**：仅在特定工程对象或冷门细分方向缺文献时查阅 |
| **1 分** | 全部会议论文（FASTA/CCC/CAC/IFAC/CDC 等，541 篇）+ MDPI 系列期刊（8 篇） | **549** | **线索与最新动态**：用于追踪 2025–2026 最新投稿趋势（如 FASTA 2026），引用须谨慎核验 |
| **0 分** | *IEEE Access*（4 篇） | **4** | **默认屏蔽**：一般检索通过 `--min-score 1` 或 `--min-score 3` 自动排除 |

---

## 3. 常用检索命令

在 `duan-hofas` 技能目录下运行 `scripts/search_backup_fas.py`（或在任意目录直接运行 `/home/yzk/fas-library/scripts/search_fas_library.py`）：

```bash
# 查看库统计与分值分布
python3 scripts/search_backup_fas.py --stats

# 列出全部 5 分文献（Duan 独作 + IEEE TAC + Automatica）
python3 scripts/search_backup_fas.py --score 5 --in-meta --top 45

# 查 4 分及以上顶刊中某主题的相关文献（按分值降序）
python3 scripts/search_backup_fas.py --query "switched" --min-score 4 --sort-by-score --top 15

# 查 3 分及以上主流期刊全文（自动过滤会议、MDPI 和 IEEE Access）
python3 scripts/search_backup_fas.py --query "sub-FAS" --min-score 3 --sort-by-score --top 15

# 在高分文献中只搜形式化定理/引理/定义
python3 scripts/search_backup_fas.py --kind Theorem --query "ROEA" --min-score 4 --top 10

# 精确子串匹配（查特定术语或缩写）
python3 scripts/search_backup_fas.py --literal "observer reset" --min-score 1 --sort-by-score --top 10

# 追踪最新会议线索（如 FASTA 2026 切换系统方向）
python3 scripts/search_backup_fas.py --query "switched" --category conference --year 2026 --in-meta --show-abstract
```

## 4. 浏览入口

- 按分值分组目录：`corpus/backup_fas/INDEX_BY_SCORE.md`（物理路径 `/home/yzk/fas-library/INDEX_BY_SCORE.md`）
- 按类别与年度总目录：`corpus/backup_fas/INDEX.md`（物理路径 `/home/yzk/fas-library/INDEX.md`）
- 官方期刊/会议清单 Markdown：`corpus/backup_fas/markdown/FAS期刊论文清单-2026年10月9日.md` 与 `FAS会议论文清单-2026年10月9日.md`

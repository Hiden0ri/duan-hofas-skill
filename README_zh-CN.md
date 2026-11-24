# Duan HOFAS Skill（段广仁高阶全驱系统方法写作与核查技能）

[English](README.md) | 简体中文

面向 **Antigravity**、**Claude Code** 与 **Codex** 的统一学术技能，用于按照**段广仁（Guang-Ren Duan）院士原文的地道词汇、句式搭配、数学记号、论文结构、正式数学环境与标准证明模板**，撰写、润色与核查 HOFAS / FAS / sub-FAS / 切换 sub-FAS 的 Markdown 文稿、LaTeX 论文及中文开题报告，并提供可直接编译的 IEEEtran 标准 LaTeX 论文模板。

## 核心能力

- **基于全集原文语料库的撰写与润色**（[duan-writing-corpus.md](references/duan-writing-corpus.md)、[duan-series-templates.md](references/duan-series-templates.md)）：从段广仁一作 **32 篇中英文 FAS 核心论文**（涵盖《自动化学报》`I–III`、《航空学报》、*IJSS* `Part I–X`、*SCIS* 三大双篇系列、*IEEE TCYB*、*UC-FAS* `Part I–III` 与最新 *OD-FAS* 系列）及 2026 年专著 *Fully Actuated System Approach, Volume I*（513 页）中逐字提取 `[E]` 原句与专题结构范本；主动保留 Duan 标志性表达（如 `"the feasible set clearly has the following expression:"`、`"we construct the following controller:"`、`"is equivalent to the following state-space form:"`、`"The above result converts/reveals..."`），剔除 AI 味的 `"not X, but Y"` 防御性免责声明与空洞预告句。
- **Duan 概念、术语与记号优先对齐**（[duan-style-quick-guide.md](references/duan-style-quick-guide.md)、[concepts-and-notation.md](references/concepts-and-notation.md)）：优先沿用段广仁既有概念与符号（奇异函数 $\varphi_0,\varphi_\infty,\varphi$、$|\varphi_i|$、奇异集/可行集 $\mathbb{S}/\mathcal{S}$ 与 $\mathbb{F}/\mathcal{F}$、亚稳定与亚镇定、ROEA/RoEA、初值 $X_0=x^{(0\sim n-1)}(0)$、引言末尾不编号 `equation*` 且只用 `=` 不用 `:=`/`\col` 的 `Notations:` 段），仅在段广仁无对应概念时于其框架之上引入新对象并显式标为 `[D]`；中文术语严格对齐《自动化学报》与《航空学报》，不生造中文译名。
- **严格的来源分层纪律（`[E]` / `[D]` / `[U]`）**（[model-definition-registry.md](references/model-definition-registry.md)）：严格区分段广仁原始定义/假设 `[E]`、本文新增推导或条件 `[D]` 与未核实项 `[U]`，绝不向段广仁原文强加未写出的光滑性或拓扑假设，也不把 `[D]`/`[U]` 归于段广仁名下。
- **七大正式数学环境规范与“陈述内显式写明目标”铁律**（[theorem-writing-template.md](references/theorem-writing-template.md)）：规范 `Problem`、`Definition`、`Assumption`/`Condition`、`Lemma`、`Proposition`、`Theorem`（六段式顺序 + `Then 1)...; 2)...`）、`Corollary` 与 `Remark`（中文对应 **`说明`**），强制要求**每一个 `Theorem`、`Lemma`、`Proposition`、`Corollary` 在陈述本身直接写出全文层面的最终目的与控制/几何结论**，绝不把核心结论拆入前后引导句或 `Remark`。
- **通用与五大系列专属标准证明模板**（[proof-templates.md](references/proof-templates.md)、[duan-series-templates.md](references/duan-series-templates.md)）：
  1. 直接代入 + 状态空间形式（`state-space form`）+ Lyapunov 衰减证明；
  2. sub-FAS 亚镇定与 ROEA 精确刻画证明（`Duan 2023 TCYB`）；
  3. 反证法标准模板（`Duan & Zhou 2022` Lemma 4.4：`"Suppose that … Then it follows from … On the other side, … This yields a contradiction. Thus … The proof is finished."`）；
  4. 高阶反步法五步构造与交叉项叠缩证明（`Part III` §4 / *Volume I* §9.2，$\tilde P_i(A_i^{0\sim m_i-1})=\mathring{I}P_i$）；
  5. 充要条件（`Sufficiency:` / `Necessity:`）、多结论逐条证明与双向同胚消元/数学归纳法；
  6. 单调区间分割与有限驻点 ROEA 约化证明（`Duan & Wang 2026`）；
  7. **OD-FAS 系列**：消去 $\dot y$ 的降阶观测器（$z$-变换）、四分块动态输出反馈补偿器、$T A_E T^{-1}$ 分块上三角相似变换/级联 ISS 证明，以及增广初值 $[X_0^\top\ z_0^\top]^\top$ 输出反馈 RoEA（`OD-FAS Part 1 & Part 4`）；
  8. **UC-FAS / 时滞 / 广义链式系列**：内外可行集交集 $\mathbb{F}^{\mathrm{in}}\cap\mathbb{F}^{\mathrm{ex}}$ 与三级自然递推亚镇定（`UC-FAS Part I–III`）、输入时滞区间预测器 $Z(s)$（`SCIS 2023`）、广义链式系统不连续缩放与二阶主导模态分离（`SCIS 2024`）。
- **算例、短图题、三线表与 MATLAB 绘图规范**（[simulation-patterns.md](references/simulation-patterns.md)）：2–6 词名词短语短图题、正文 `"... are shown in Fig. X. It can be observed that ..."` 引图句式、`booktabs` 三线表，以及对齐用户 `matlab/p1ot.m` 的绘图规范。
- **即拿即用的 IEEEtran LaTeX 论文骨架**：`assets/duan-hofas-paper-template.tex`。

## 项目结构

```text
duan-hofas/
├── SKILL.md                           # 技能主入口、四大工作模式与对齐铁律
├── README.md                          # 英文说明文档
├── README_zh-CN.md                    # 简体中文说明文档
├── package.json                       # @hiden0ri/duan-hofas-skill 包清单与发布配置
├── agents/
│   └── openai.yaml                    # Codex 界面元数据与默认触发提示词
├── assets/                            # 可编译论文模板资产库
│   └── duan-hofas-paper-template.tex  # IEEEtran 兼容的 Duan 风格 LaTeX 论文骨架
├── references/                        # 28 份提炼知识库、语料库与环境/证明模板手册
│   ├── duan-writing-corpus.md         # 核心原文逐字语料库、衔接词表与去 AI 腔对照表
│   ├── fas-advantages-corpus.md       # FAS 方法优势、方法对比与防夸大客观边界精选语料库（53 段分拣提炼）
│   ├── canonical-definitions-index.md # 段广仁全集 109 条经典定义九大主题全景索引与逐字范本
│   ├── duan-series-templates.md       # 五大专题系列标准范本库（自动化学报/IJSS/SCIS/UC-FAS/OD-FAS）
│   ├── theorem-writing-template.md    # 867 个正式环境提炼模板库（T1–T6, L1–L6, P1–P5, C1–C4...）
│   ├── proof-templates.md             # 3 种证明位置范式（M1–M3）与 12 类证明骨架（PT-1 至 PT-12）
│   ├── corpus-conflict-resolution.md  # 984 条分拣块中 10 处跨篇冲突实证统计与 Check/Draft 裁定
│   ├── corpus-guide.md                # 本地全文 MD 库、分拣分类库与 FTS5 检索使用指南
│   ├── backup-fas-library.md          # 二级后备扩展 FAS 文献库（1,041 篇 0–5 分级）边界与检索规范
│   └── ...                            # 其余 19 份记号词典、模型注册表、引理卡片与严密性审查参考
├── scripts/                           # 13 个语料构建、环境分拣、全文检索、打包与校验脚本
│   ├── build_papers_corpus.py         # PDF -> 双栏重排/数学字体无损解码 MD + SQLite FTS5 构建器
│   ├── sort_corpus_environments.py    # 984 条正式环境与显式证明全量自动分拣器
│   ├── build_classic_definitions_bank.py # 109 条经典定义（94 正式 + 15 正文）九大主题分拣器
│   ├── build_fas_advantages_bank.py   # 53 段 FAS 方法优势/对比/客观边界七大维度分拣器
│   ├── search_corpus.py               # 覆盖 32 篇论文 + Volume I 的一级权威库检索工具
│   ├── search_backup_fas.py           # 覆盖 1,041 篇 0–5 分级 FAS 文献的二级后备库检索入口
│   ├── build_release_packages.py      # 构建 .skill / .zip / .tar.gz / npm .tgz 发行包与校验和
│   ├── validate_distillation.py       # 必需文件、内部链接与公式定界符完整性校验脚本
│   └── ...                            # 其余 5 个专著索引/单页提取与本地 Zotero 盘点脚本
├── reports/                           # [被 .gitignore 忽略的本地早期蒸馏与覆盖率审查记录]
└── corpus/                            # 语料库目录（sorted/ 随仓库分发；papers/ 与 backup_fas/ 仅本地软链隔离）
    ├── sorted/*.md & summary_stats.json # [入库分发] 13 个分拣库（984 环境/证明 + 109 定义 + 53 优势）
    ├── INDEX.md & manifest.json       # [被 .gitignore 忽略] 本地 32 篇论文目录软链
    ├── papers/*.md                    # [被 .gitignore 忽略] 本地 32 篇双栏无损解码整篇全文软链
    └── backup_fas/                    # [被 .gitignore 忽略] 本地 1,041 篇 0–5 分级后备 FAS 文本库软链
```

## 资产库说明

### 1. 论文模板资产库（`assets/`）
- `assets/duan-hofas-paper-template.tex`：开箱即编译的 Duan 风格 LaTeX 论文骨架（优先加载 `IEEEtran` 期刊类，缺失时自动回退至 `article`）。内置 `Definition / Assumption / Problem / Lemma / Proposition / Theorem / Corollary / Remark / Example` 正式环境、`\xstack` / `\Arow` / `\Phic` 记号宏、五段式摘要、约 1.5 页引言结构、引言末尾斜体 `Notations:` 段（不编号 `equation*` 且严格用 `=`）、`booktabs` 三线表（`\toprule/\midrule/\bottomrule`）以及 HOFAS/sub-FAS 控制律与状态空间闭环标准骨架。

### 2. 提炼知识与模板参考库（`references/`，共 28 份手册）
| 资产模块 | 包含文件与覆盖范围 |
|---|---|
| **原文写作语料与方法优势对比** | [duan-writing-corpus.md](references/duan-writing-corpus.md)（逐字 `[E]` 原句、衔接词表、去 AI 腔正反表）、[fas-advantages-corpus.md](references/fas-advantages-corpus.md)（7 大维度 FAS 方法优势、对比反步法/反馈线性化/状态空间法及防夸大边界）、[duan-series-templates.md](references/duan-series-templates.md)（《自动化学报》`I–III`、*IJSS* `I–X`、*SCIS* 时滞/链式、*UC-FAS* `I–III`、*OD-FAS* `1 & 4`）、[duan-style-quick-guide.md](references/duan-style-quick-guide.md)、[duan-first-author-habits.md](references/duan-first-author-habits.md)、[writing-style.md](references/writing-style.md) |
| **正式环境与证明模板库** | [theorem-writing-template.md](references/theorem-writing-template.md)（由 867 个正式环境提炼 `T1–T6`、`L1–L6`、`P1–P5`、`C1–C4`、`D1–D2`、`Pr1–Pr3`、`R1–R5`）、[proof-templates.md](references/proof-templates.md)（`M1–M3` 证明位置范式与 `PT-1` 至 `PT-12` 证明骨架）、[corpus-conflict-resolution.md](references/corpus-conflict-resolution.md)（10 处跨篇冲突实证统计与 Check/Draft 速查表）、[derivation-patterns.md](references/derivation-patterns.md)、[canonical-theorems.md](references/canonical-theorems.md)、[common-assumptions.md](references/common-assumptions.md)、[common-lemmas.md](references/common-lemmas.md) |
| **经典定义索引、记号词典与模型注册表** | [canonical-definitions-index.md](references/canonical-definitions-index.md)（109 条经典定义九大主题索引与逐字范本）、[concepts-and-notation.md](references/concepts-and-notation.md)、[symbol-dictionary.md](references/symbol-dictionary.md)、[model-definition-registry.md](references/model-definition-registry.md)（按控制目标区分 $f,B$ 正则性）、[concept-lineage.md](references/concept-lineage.md)、[coauthored-comparison.md](references/coauthored-comparison.md) |
| **算例、物理背景优势、仿真绘图与严密性审查** | [example-library.md](references/example-library.md)、[physical-examples-and-advantages.md](references/physical-examples-and-advantages.md)（9 大物理背景具体动力学、HOFAS/sub-FAS/UC-FAS/OD-FAS 转化形式、仿真参数与各背景专属优势及工程边界）、[simulation-patterns.md](references/simulation-patterns.md)（`matlab/p1ot.m` 作图规范与短图题）、[frequently-cited-references.md](references/frequently-cited-references.md)、[rigor-audit.md](references/rigor-audit.md)、[adversarial-tests.md](references/adversarial-tests.md) |
| **原始文献目录、语料库与后备库指南** | [corpus-guide.md](references/corpus-guide.md)、[backup-fas-library.md](references/backup-fas-library.md)、[source-catalog.md](references/source-catalog.md)、[volume1-authority.md](references/volume1-authority.md) |

### 3. 自动化构建、分拣、检索、打包与校验工具库（`scripts/`，共 13 个脚本）
- **全文库构建、分拣与检索**：`scripts/build_papers_corpus.py`（将 32 篇 PDF 转为双栏重排、数学字体无损解码 `.md` 并构建统一 FTS5 库）、`scripts/sort_corpus_environments.py`（将 867 个正式环境 + 117 个显式证明自动分拣入 10 个原文分类库）、`scripts/build_classic_definitions_bank.py`（分拣 109 条经典定义）、`scripts/build_fas_advantages_bank.py`（分拣 53 段 FAS 方法优势/对比/边界原文）、`scripts/search_corpus.py`（一级权威库检索，支持 `--query`、`--literal`、`--label`、`--kind`、`--series`）、`scripts/search_backup_fas.py`（二级后备库检索，支持 `--score`、`--min-score`、`--sort-by-score`、`--kind`、`--literal`）。
- **专著与本地文献盘点**：`scripts/build_volume1_index.py`、`scripts/search_volume1.py`、`scripts/extract_volume1_pages.py`（513 页 *Volume I* 专著索引与单页提取）；`scripts/inventory_duan_first_author.py`、`scripts/inventory_local_sources.py`（本地 Zotero 文献盘点）。
- **结构校验与发行包构建**：`scripts/validate_distillation.py`（自动检查全部 29 份核心知识文件、内部 Markdown 链接及 `$...$`/`$$...$$` 公式定界符）；`scripts/build_release_packages.py`（一键生成版权安全的 `.skill`、`.zip`、`.tar.gz`、npm `.tgz` 与 `SHA256SUMS.txt`）。

### 4. 内置分拣原文库（`corpus/sorted/`）与本地版权隔离全文缓存（`~/.cache/duan-hofas/`）
兼顾开箱即用与出版社版权规范，仓库采用分层隔离设计：
- **随仓库直接分发（`corpus/sorted/`，共 13 个文件，981 KB）**：克隆仓库或下载 Release 包即可直接调阅全部 **984 个正式环境与证明原文块**（`theorems.md` [198]、`assumptions.md` [165]、`remarks.md` [155]、`proofs.md` [117]、`definitions.md` [94]、`lemmas.md` [80]、`propositions.md` [76]、`corollaries.md` [65]、`problems.md` [24]、`conditions.md` [10]、`summary_stats.json`）、**109 条经典定义合集**（`classic_definitions_by_topic.md`）以及 **53 段方法优势/边界合集**（`fas_advantages_by_theme.md`）。
- **本地版权隔离缓存（`~/.cache/duan-hofas/`，被 `.gitignore` 排除，不入 Git）**：32 篇整篇期刊全文（`corpus/papers/*.md`）以及 `duan_corpus.sqlite` / `volume1.sqlite` 全文数据库仅保存在本地缓存并通过软链挂载。

## 安装指南

### Ubuntu / Linux

推荐克隆到 Codex 技能目录，并通过软链接接入 Claude Code 与 Antigravity，使三个平台共用唯一真源（一次 `git pull` 三端同步生效）：

```bash
sudo apt update && sudo apt install -y git
mkdir -p "$HOME/.codex/skills" "$HOME/.claude/skills" "$HOME/.gemini/config/skills"
git clone https://github.com/Hiden0ri/duan-hofas-skill.git "$HOME/.codex/skills/duan-hofas"
ln -s "$HOME/.codex/skills/duan-hofas" "$HOME/.claude/skills/duan-hofas"
ln -s "$HOME/.codex/skills/duan-hofas" "$HOME/.gemini/config/skills/duan-hofas"
```

### macOS

```bash
brew install git
mkdir -p "$HOME/.codex/skills" "$HOME/.claude/skills" "$HOME/.gemini/config/skills"
git clone https://github.com/Hiden0ri/duan-hofas-skill.git "$HOME/.codex/skills/duan-hofas"
ln -s "$HOME/.codex/skills/duan-hofas" "$HOME/.claude/skills/duan-hofas"
ln -s "$HOME/.codex/skills/duan-hofas" "$HOME/.gemini/config/skills/duan-hofas"
```

若尚未安装 Homebrew，可先运行 `xcode-select --install` 安装命令行工具。

### Windows 11 (PowerShell)

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/Hiden0ri/duan-hofas-skill.git "$env:USERPROFILE\.codex\skills\duan-hofas"
```

安装完成后重启对应 Agent 会话即可识别 `duan-hofas`。

## 更新与结构校验

Ubuntu 与 macOS：

```bash
git -C "$HOME/.codex/skills/duan-hofas" pull
python3 "$HOME/.codex/skills/duan-hofas/scripts/validate_distillation.py"
```

Windows PowerShell：

```powershell
git -C "$env:USERPROFILE\.codex\skills\duan-hofas" pull
python "$env:USERPROFILE\.codex\skills\duan-hofas\scripts\validate_distillation.py"
```

## 典型调用示例

在 Codex 中输入 `$duan-hofas`（在 Antigravity / Claude Code 中直接触发或指名调用 `duan-hofas`），直接描述任务即可。注意：**默认安全规则为“先给修改方案，待你明确说‘改’或‘动手’（或给出‘去掉…’/‘调整…’等直接编辑指令）才修改文件”**。

### 1. 按段广仁原文语料库起草或润色段落

```text
按 Duan 的原文语料库润色这一节，保留或改用 Duan 常用句式，去掉 AI 味的防御性否定句。
```

### 2. 核查记号、`Notations:` 段与模型变量交代

```text
检查这篇稿件的符号、Notations 段和模型变量交代是否符合 Duan 的习惯。
```

标准审查输出格式：

```text
位置 → 当前写法 → 推荐的 Duan 写法 → 理由 → [E]/[D]/[U]
```

### 3. 核查或改写 Theorem / Lemma / Proposition / Corollary

```text
检查文中所有 Theorem、Lemma、Proposition、Corollary 是否在陈述本身直接写出了最终目的，并符合 Duan 的六段式结构。
```

### 4. 按标准模板起草或审查证明（反证法、高阶反步法、OD-FAS、UC-FAS）

```text
按 Duan & Zhou (2022) Lemma 4.4 的反证法模板重写这个引理的证明。
```

```text
按 Duan 高阶反步法（Part III / Volume I 第 9 章）的标准分步结构起草这一节的推导与主定理。
```

```text
按 OD-FAS 系列的降阶观测器与四分块动态补偿器标准结构整理这一节的输出反馈设计。
```

### 5. 核查 Definition、Assumption 与 Remark 边界

```text
检查这里的 Definition、Assumption 和 Remark 边界是否清晰，有没有把本文新增条件混进 Duan 原始定义里。
```

### 6. 核查算例叙述、短图题、三线表与 MATLAB 画图脚本

```text
检查仿真章节的引图句式、短图题、三线表以及 MATLAB 画图脚本是否符合 Duan 习惯和 p1ot.m 规范。
```

### 7. 快速创建 Duan 风格 IEEEtran LaTeX 论文模板

```text
创建一个 Duan 风格的单阶切换 sub-FAS 论文 LaTeX 模板。
```

### 8. 溯源核对争议表述或公式出处

```text
核对这句话或这个正则性条件出自 Duan 的哪篇原文，给出准确出处标注 [E]/[D]/[U]。
```

## 可选本地原文全集文本库与 FTS5 统一检索（方案 A）

为遵守学术出版版权规范，公开 GitHub 仓库不包含受版权保护的论文 PDF、转换后的 `.md` 全文或预构建的 SQLite 数据库。在存有本地 Zotero PDF 的机器上，可运行以下命令一键生成本地缓存原文库并建立软链：

```bash
python3 scripts/build_papers_corpus.py
python3 scripts/sort_corpus_environments.py
python3 scripts/build_classic_definitions_bank.py
python3 scripts/build_fas_advantages_bank.py
ln -sfn "$HOME/.cache/duan-hofas/corpus" corpus
python3 scripts/search_corpus.py --list-docs
```

该脚本会将全部 32 篇段广仁一作论文转换为双栏重排、数学字体无损解码的结构化 Markdown 全文（存于 `~/.cache/duan-hofas/corpus/papers/*.md`），按 10 类正式环境与证明全量分拣为 984 个原文分类块，并生成 109 条经典定义主题库与 53 段 FAS 方法优势/边界主题库（均存于 `~/.cache/duan-hofas/corpus/sorted/*.md`，技能目录内通过被 `.gitignore` 忽略的 `corpus` 软链直接访问），同时与 513 页 *Volume I* 专著合并构建为统一的 SQLite FTS5 全文与定理检索库（`~/.cache/duan-hofas/duan_corpus.sqlite`）；详细说明见 [references/corpus-guide.md](references/corpus-guide.md) 与 [references/corpus-conflict-resolution.md](references/corpus-conflict-resolution.md)。日常记号核查、文稿润色与 LaTeX 模板生成无需依赖本地全文缓存库即可开箱即用。

## 重要数学边界

关于原系统变量、维数以及随控制目标变化的 $f$ 与 $B$ 正则性条件，请查阅 [references/model-definition-registry.md](references/model-definition-registry.md)。动笔前应先选定所属模型分支与控制目标：**切勿将某一篇特定论文的光滑性或全局非奇异假设泛化为所有 HOFAS/sub-FAS 的通用要求，也切勿将本文新增的 `[D]` 构造归于段广仁名下**。


## 更新历史与说明

### 版本演进记录

- **2026-11-24（`v1.2.0`）— 一级权威库扩充至 36 篇（补齐 `OD-FAS Part 2` 等 4 篇独作）+ 接入二级分级后备 FAS 文本数据库（1,041 篇，0–5 分体系）+ 九大物理背景算例与优势手册**
  - 新增 [physical-examples-and-advantages.md](references/physical-examples-and-advantages.md) 与 `scripts/build_physical_examples_catalog.py`，从一级 36 篇权威库与二级 3–5 分旗舰期刊中系统提炼 **9 大物理背景**（航天器/轨姿一体、四旋翼/无人直升机/空中机械臂、刚/柔性机械臂与龙门平台、吊车/倒立摆/惯性轮摆/弹簧质量、欠驱动船舶/气垫船、移动小车/Brockett/广义链式、柔性伺服/LSRM/直流微电网、主动悬架/气动并联、主动容错/混合脉冲 sub-FAS/Lorenz 基准）的原始动力学方程、具体 FAS 转化形式、奇异集/可行集、代表仿真参数以及各背景上的核心优势与工程边界 `[E]`。
  - 一级权威库新增 4 篇段广仁独作期刊论文：`odfas_2026_part2`（*IJSS* 2026，补齐 *OD-FAS* 多阶输出反馈 Part 2）、`scis_2025_chained3`（*SCIS* 2025，广义链式多向量情形）、`jssc_2022_brockett1` 与 `jssc_2023_brockett2`（*JSSC* 2022/2023，Brockett 第一/第二反例的 FAS 处理）；重跑全量分拣后，一级库升级为 **36 篇一作论文 + *Volume I***、**1,065 个原文块**（939 个正式环境 + 126 个显式 `Proof` 块，新增 +81 块）与 **114 条经典定义**（99 正式 + 15 正文，全部 0 PUA、0 `U+FFFD`、0 行号错位）。
  - 新增 `scripts/search_backup_fas.py` 与 [backup-fas-library.md](references/backup-fas-library.md)，在 [SKILL.md](SKILL.md) 与 [corpus-guide.md](references/corpus-guide.md) 中确立“**一级 Duan 权威库 + 二级 0–5 分级 FAS 后备库**”双层检索架构。
  - 二级后备库通过被 `.gitignore` 忽略的 `corpus/backup_fas/` 软链挂载本地全量 FAS 文献库（1,041 篇去重期刊与会议论文，10,097 页，7,673 条形式化地标）：5 分（Duan 独作 33 篇 + *IEEE TAC* 1 篇 + *Automatica* 6 篇）、4 分（24 种 IEEE/ASME 旗舰汇刊与中科院 1 区 Top，191 篇）、3 分（主流控制 SCI / *自动化学报* / *航空学报*，212 篇）、2 分（普通三四区与中文刊，45 篇）、1 分（541 篇会议 + 8 篇 MDPI）、0 分（*IEEE Access* 4 篇），支持 `--score` / `--min-score` / `--sort-by-score` / `--kind` / `--literal` 检索，并严格禁止非 Duan 论文覆盖一级权威库规范。
- **2026-11-18（`v1.1.0`）— 109 条经典定义库、53 段 FAS 方法优势/边界语料库与 PDF 数学字体无损解码升级**
  - 新增 `scripts/build_classic_definitions_bank.py` 与 [canonical-definitions-index.md](references/canonical-definitions-index.md)，完整分拣并索引全集 **109 条经典定义**（94 个正式 `Definition` + 15 条正文/定理定义，含离散超前算子 $x^{\lfloor i\rfloor}(k)=x(k+i)$ 与滞后算子 $x^{\lceil i\rceil}(k)=x(k-i)$ 原典核正）。
  - 新增 `scripts/build_fas_advantages_bank.py` 与 [fas-advantages-corpus.md](references/fas-advantages-corpus.md)，从 32 篇一作论文 + *Volume I* 中按 7 大维度分拣 **53 段**关于 FAS 方法优势、对比反步法/反馈线性化/状态空间法及防夸大适用边界的逐字原文 `[E]`。
  - 升级 `scripts/build_papers_corpus.py` 与 `scripts/sort_corpus_environments.py`：修复多码位连字、无外部 `/Encoding` 的 `CMEX` 大算子（`∑, ∏, ∫`）、`EuclidMathTwo` 黑板粗体（`𝔾, 𝕏, ℚ, 𝔽`）、方正 `FZS_Extra_S92` 大括号及希腊变体（`ϖ, ϑ, ϕ`）无损保留，分拣总数提升至 **984 块**（867 个正式环境 + 117 个 `Proof` 块，漏捕率 `0`、页眉脚注残留 `0`）。
- **2026-11-17（`b4107c3` – `f1a59d2`, `v1.0.0`）— 940 块环境/证明全量分拣模板库、跨篇冲突裁定与双语架构文档**
  - 新增 `scripts/sort_corpus_environments.py`，从 32 篇一作全文 + *Volume I* 中按精确起止边界自动分拣 **940 个原文块**（823 个正式环境 + 117 个显式 `Proof` 块）归入 10 个本地分类库（`corpus/sorted/*.md`）。
  - 基于全量分拣库重构 [theorem-writing-template.md](references/theorem-writing-template.md)（`T1–T6` 定理、`L1–L6` 引理、`P1–P5` 命题、`C1–C4` 推论、`D1–D2` 定义、`Pr1–Pr3` 问题、`R1–R5` 说明）与 [proof-templates.md](references/proof-templates.md)（`M1–M3` 三种证明位置范式 + `PT-1` 至 `PT-12` 标准证明骨架）。
  - 新增 [corpus-conflict-resolution.md](references/corpus-conflict-resolution.md)，基于全库统计对 **10 处跨篇差异与旧规冲突**给出实证频数及 Check/Draft 双轨裁定（如 `:=` 一作出现 `0/32` 次 vs `\triangleq`/`=`、定理 `Let` 开头占 `63.7%` vs `Suppose` `12.1%`、证明无套话收尾占 `83.8%`、`ROEA`/`RoEA`、`Hurwitz`/`stable`/`Schur` 等）。
  - 新增中英文一键切换文档（[README_zh-CN.md](README_zh-CN.md)）、完整目录树与四大资产库分层说明。
- **2026-11-16（`8b39b3d` – `b42a7cb`）— 32 篇五大系列全覆盖蒸馏、全文 Markdown 语料库与统一 FTS5 检索**
  - 新增 [duan-writing-corpus.md](references/duan-writing-corpus.md) 与 [duan-series-templates.md](references/duan-series-templates.md)，完成段广仁五大 FAS 系列全覆盖提炼：《自动化学报》（`I–III`）/《航空学报》中文系列、*IJSS*（`Part I–X` + 欠驱动）、*SCIS* 离散/连续时滞与广义链式双篇系列、*UC-FAS*（`Part I–III`）以及最新 *OD-FAS*（`Part 1 & Part 4`）。
  - 新增 `scripts/build_papers_corpus.py`、`scripts/search_corpus.py` 与 [corpus-guide.md](references/corpus-guide.md)，实现双栏坐标重排、Computer Modern / Y&Y Type-1 数学字体私用区解码（多轮独立复核实现 0 私用区残留、0 `U+FFFD` 乱码、地标行号 0 偏移）及 32 篇论文 + *Volume I* 统一 SQLite FTS5 检索。
  - 打通 **Antigravity**、**Claude Code** 与 **Codex** 三端统一接入规范。
- **2026-09-09 – 2026-09-10（`c245800` – `d81fa43`）— 按控制目标区分的模型注册表与改稿规范**
  - 新增 [model-definition-registry.md](references/model-definition-registry.md)，按控制目标严格区分原系统变量、维数与 $f,B$ 正则性条件（未声明 / `piecewise continuous` / `smooth`）。
  - 细化引言末尾 `Notations:` 段与正文局部记号的边界及 LaTeX 备份编译流程。
- **2026-09-08（`790833f` – `0bee51e`）— 初始版本发布与 *Volume I* 专著基座**
  - 发布 `duan-hofas` 初始版本，构建 513 页 *Volume I* 专著 SQLite FTS5 索引（`scripts/build_volume1_index.py`、`scripts/search_volume1.py`）、核心概念与符号词典、常用假设/引理/高频引文手册、可编译 `assets/duan-hofas-paper-template.tex` 模板及 Linux/macOS/Windows 跨平台安装说明。

### 维护、同步与覆盖范围说明

1. **日常拉取更新 vs. 本地全文缓存重建**：日常执行 `git pull` 并运行 `python3 scripts/validate_distillation.py`，即可在软链关联的三端 Agent 中同步全部 28 份核心知识文件、模板与规则，无需重跑构建脚本；**仅当本地 Zotero 新增段广仁 PDF 文献时**，才需重新运行 `build_papers_corpus.py` 与分拣脚本刷新本地缓存库。
2. **当前文献覆盖范围与待补篇目**：当前一级权威语料库覆盖 **36 篇段广仁一作中英文 FAS 论文**（英文 32 篇 + 中文 4 篇，2020–2026）及 2026 年 Springer 专著 *Volume I*（513 页），全量分拣 **1,065 个原文块**（939 个正式环境 + 126 个 `Proof` 块）与 **114 条经典定义**；其中 2026 最新 *OD-FAS* 系列已收录 `Part 1`、`Part 2` 与 `Part 4`（仅 `Part 3` 待补）。二级后备库覆盖 **1,041 篇** 0–5 分级 FAS 社区期刊与会议论文。
3. **版权隔离与仓库卫生**：`corpus/sorted/` 分拣库随仓库分发；整篇论文全文 `corpus/papers/`、`corpus/INDEX.md`、`corpus/manifest.json` 与 `*.sqlite` 数据库已在 `.gitignore` 中严格排除。向公开仓库提交修改前，切勿强行添加整篇全文 `.md` 或原版 PDF，并务必先执行 `scripts/validate_distillation.py` 确认结构与链接无误。

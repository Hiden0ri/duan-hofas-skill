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

## 仓库目录结构

| 路径 | 作用说明 |
|---|---|
| [SKILL.md](SKILL.md) | 技能主入口、四大工作模式、不可妥协的对齐铁律与 LaTeX 备份/编译/核查流程 |
| [references/duan-writing-corpus.md](references/duan-writing-corpus.md) | **核心原文写作语料库**：各节结构模板、7 类正式环境、8 类证明模板、高频衔接词表与去 AI 腔正反对照表 |
| [references/duan-series-templates.md](references/duan-series-templates.md) | **五大专题系列标准范本库**：OD-FAS（`Part 1 & 4`）、UC-FAS（`Part I–III`）、IJSS（`Part VI & X`）、SCIS 时滞/链式系列、《自动化学报》（`I–III`）与《航空学报》中文规范 |
| [references/corpus-guide.md](references/corpus-guide.md) | **本地全文 Markdown 语料库与统一检索指南**：说明如何通过 `scripts/build_papers_corpus.py` 与 `scripts/search_corpus.py` 构建并毫秒级检索 32 篇一作全文 + *Volume I* |
| [references/duan-style-quick-guide.md](references/duan-style-quick-guide.md) | 记号、章节排布、切换 sub-FAS 扩展约定与作图快速核查清单 |
| [references/theorem-writing-template.md](references/theorem-writing-template.md) | 定理六段式及 `Lemma`、`Proposition`、`Corollary`、`Problem` 书写模板 |
| [references/proof-templates.md](references/proof-templates.md) | 各类标准证明的可执行填空骨架（Templates A–M） |
| [references/model-definition-registry.md](references/model-definition-registry.md) | 按控制目标区分的原系统变量、维数与 $f,B$ 正则性条件注册表 |
| [references/concepts-and-notation.md](references/concepts-and-notation.md) & [references/symbol-dictionary.md](references/symbol-dictionary.md) | 权威中英文术语、标准符号词典与下标作用域防撞检查 |
| [references/duan-first-author-habits.md](references/duan-first-author-habits.md) & [references/writing-style.md](references/writing-style.md) | 段广仁一作论文的统计特征与行文风格边界 |
| [references/common-assumptions.md](references/common-assumptions.md)、[references/common-lemmas.md](references/common-lemmas.md)、[references/canonical-theorems.md](references/canonical-theorems.md) | 高频假设、常用引理族与标志性定理卡片 |
| `assets/duan-hofas-paper-template.tex` | 符合 Duan 结构与 `Notations:` 规范的可编译 IEEEtran LaTeX 论文模板 |
| `scripts/validate_distillation.py` | 校验内部 Markdown 链接、数学公式定界符与必需知识文件完整性的自动化脚本 |

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
ln -sfn "$HOME/.cache/duan-hofas/corpus" corpus
python3 scripts/search_corpus.py --list-docs
```

该脚本会将全部 32 篇段广仁一作论文转换为双栏重排、数学字体解码的结构化 Markdown 全文（存于 `~/.cache/duan-hofas/corpus/papers/*.md`，技能目录内通过被 `.gitignore` 忽略的 `corpus` 软链直接访问），并与 513 页 *Volume I* 专著合并构建为统一的 SQLite FTS5 全文与定理检索库（`~/.cache/duan-hofas/duan_corpus.sqlite`）；详细检索参数见 [references/corpus-guide.md](references/corpus-guide.md)。日常记号核查、文稿润色与 LaTeX 模板生成无需依赖本地全文缓存库即可开箱即用。

## 重要数学边界

关于原系统变量、维数以及随控制目标变化的 $f$ 与 $B$ 正则性条件，请查阅 [references/model-definition-registry.md](references/model-definition-registry.md)。动笔前应先选定所属模型分支与控制目标：**切勿将某一篇特定论文的光滑性或全局非奇异假设泛化为所有 HOFAS/sub-FAS 的通用要求，也切勿将本文新增的 `[D]` 构造归于段广仁名下**。

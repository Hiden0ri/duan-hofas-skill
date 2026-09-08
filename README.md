# Duan HOFAS Skill

A private Codex skill for checking whether an HOFAS Markdown file or manuscript follows Guang-Ren Duan's recurring notation, terminology, article organization, and theorem-writing habits. It can also create a Duan-style IEEEtran-compatible LaTeX manuscript skeleton.

## Main uses

- Check whether the mathematical formulas in the original manuscript follow Duan's notation habits.
- Check whether a theorem follows Duan's writing habits.
- Check whether definitions and assumptions are consistent with Duan's corresponding definitions and assumptions.
- Check the organization of Remarks, Examples, and simulations.
- Create a Duan-style LaTeX paper template quickly.
- Search locally indexed source material only when a concrete point needs verification.

## Install on Ubuntu

Install GitHub CLI, authenticate, and clone the private repository:

```bash
sudo apt update
sudo apt install git gh
gh auth login
mkdir -p "$HOME/.codex/skills"
gh repo clone Hiden0ri/duan-hofas-skill "$HOME/.codex/skills/duan-hofas"
```

Restart Codex after installation.

## Install on Windows 11

Install Git and GitHub CLI, then run PowerShell:

```powershell
gh auth login
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
gh repo clone Hiden0ri/duan-hofas-skill "$env:USERPROFILE\.codex\skills\duan-hofas"
```

Restart Codex after installation.

## Update

Ubuntu:

```bash
git -C "$HOME/.codex/skills/duan-hofas" pull
```

Windows PowerShell:

```powershell
git -C "$env:USERPROFILE\.codex\skills\duan-hofas" pull
```

## Usage examples

Invoke the skill explicitly with `$duan-hofas`. Give it the manuscript path when the material is already in a file.

### 1. Ask which symbol Duan uses

```text
使用 $duan-hofas：Duan 在这里通常用什么符号表示从 x 到 x 的 n−1 阶导数组成的向量？请区分单阶 HOFAS 与多阶 HOFAS，并给出可直接复制的 LaTeX。
```

```text
使用 $duan-hofas：在 SUB-FAS 中，Duan 如何表示奇异集、可行集和指数吸引域？不要使用我提出的扩展符号。
```

### 2. Check whether the original mathematical formulas follow Duan's habits

```text
使用 $duan-hofas 检查 '/absolute/path/paper.md' 原文中的数学公式是否符合 Duan 的习惯。重点检查状态堆叠、参数矩阵、伴随矩阵、可行集、ROEA、维数和上下标。只列出不一致或无法确认的地方，暂时不要改文件。
```

Expected review format:

```text
位置 → 当前写法 → 推荐的 Duan 写法 → 原因 → [E]/[D]/[U]
```

### 3. Check whether a theorem follows Duan's writing habits

```text
使用 $duan-hofas，把下面的结果改写成 Duan 常用的定理结构：针对什么系统、满足什么假设、给定什么参数、参数满足什么条件、采用什么控制律、最终保证什么性能。不要增加原结果中不存在的假设。

[粘贴定理草稿]
```

```text
使用 $duan-hofas 检查 '/absolute/path/paper.md' 中 Theorem 2 是否符合 Duan 的书写习惯。检查系统、假设、参数、条件、控制律和性能结论的组织方式，先指出不一致之处，再给出修改稿；保持原符号和数学结论不变。
```

### 4. Check whether definitions and assumptions are consistent with Duan

```text
使用 $duan-hofas 检查下面的 Definition 和 Assumptions 是否与 Duan 对应模型中的定义和假设一致。指出哪些内容直接来自 Duan、哪些是等价改写、哪些是我新增的条件，并检查定义域、维数和量词；不要把必要的新假设误写成 Duan 的原始假设。

[粘贴定义和假设]
```

### 5. Check a proof

```text
使用 $duan-hofas 检查下面的证明是否符合 Duan 常见的组织顺序：控制律代入、闭环高阶方程、必要的状态空间表示、稳定性条件、性能结论。列出跳步和没有被使用的假设，不要为了补齐证明擅自增加条件。

[粘贴证明]
```

### 6. Check article organization

```text
使用 $duan-hofas 检查 '/absolute/path/paper.md' 的整体结构是否接近 Duan 的 HOFAS 论文写法。重点检查模型是否先于控制器定义、主要定理的位置、Remark 和 Example 的用途，以及仿真是否对应理论结论。给出最小调整方案。
```

### 7. Write a Remark or Example

```text
使用 $duan-hofas，根据这个定理写一个简洁的 Remark，只解释设计自由度、适用范围和限制，不引入新的必要假设。

[粘贴定理]
```

```text
使用 $duan-hofas，把下面的算例整理成 Duan 常用顺序：原始系统、变量消元或变换、HOFAS 表示、控制律、闭环系统、参数选择、仿真结果说明。

[粘贴算例]
```

### 8. Check simulation writing

```text
使用 $duan-hofas 检查仿真章节是否交代了模型参数、初始条件、控制器参数、求解器、步长或容差、状态响应、控制输入和可行性指标。只要求补充真正缺失的信息。
```

### 9. Create a paper template

```text
使用 $duan-hofas，为一个单阶仿射 HOFAS 镇定问题生成 IEEEtran LaTeX 论文模板。采用 Duan 的符号和六段式定理结构；未知的假设、定理结论和参数全部保留 TODO，不要自行编造。
```

```text
使用 $duan-hofas，为一个多阶 SUB-FAS 问题创建完整的 LaTeX 写作骨架，包含 Definition、Assumptions、Main Result、Proof、Remarks、Example 和 Simulation。明确区分闭环稳定性与轨迹全过程可行性。
```

### 10. Verify a disputed expression against the source

```text
使用 $duan-hofas 核对这个符号是否确实来自 Duan 原文。优先查一作论文或专著，给出论文、页码和公式号；如果只能找到合作者论文或我的 Zotero 笔记，明确标为非 canonical 或 [U]。

[粘贴符号或句子]
```

The skill should use the quick guide for ordinary checks and return to the original source only when an exact expression, theorem, or attribution is disputed.

## Optional local source search

The skill itself does not include copyrighted PDFs or a generated search database. The paths in `references/source-catalog.md` and the defaults in the indexing scripts describe the original development machine. On another computer, provide the local PDF/database paths through the scripts' command-line options or update those local defaults before using source search. The notation checker and LaTeX template do not require the source index.

## Important boundary

The quick guide captures recurring habits but does not replace checking the cited source. A paper-local notation choice is not automatically an error. When a mathematical claim or attribution is disputed, verify the exact equation, theorem, and page in the original source.

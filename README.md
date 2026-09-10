# Duan HOFAS Skill

A Codex skill for checking whether an HOFAS Markdown file or manuscript follows Guang-Ren Duan's recurring notation, terminology, article organization, and theorem-writing habits. It can also create a Duan-style IEEEtran-compatible LaTeX manuscript skeleton.

## Main uses

- Check whether the mathematical formulas in the original manuscript follow Duan's notation habits.
- Check whether a theorem follows Duan's writing habits.
- Check whether definitions and assumptions are consistent with Duan's corresponding definitions and assumptions.
- Check the organization of Remarks, Examples, and simulations.
- Create a Duan-style LaTeX paper template quickly.
- Search locally indexed source material only when a concrete point needs verification.

The repository also contains source-indexed guides to recurring assumptions, lemma families, and references frequently cited across the title-deduplicated local Duan corpus. These are research aids, not text to cite in place of the original papers.

## Install on Ubuntu

Install Git and clone the public repository:

```bash
sudo apt update
sudo apt install git
mkdir -p "$HOME/.codex/skills"
git clone https://github.com/Hiden0ri/duan-hofas-skill.git "$HOME/.codex/skills/duan-hofas"
```

Restart Codex after installation.

## Install on Windows 11

Install Git, then run PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/Hiden0ri/duan-hofas-skill.git "$env:USERPROFILE\.codex\skills\duan-hofas"
```

Restart Codex after installation.

## Install on macOS

Install Git with Homebrew and clone the public repository:

```bash
brew install git
mkdir -p "$HOME/.codex/skills"
git clone https://github.com/Hiden0ri/duan-hofas-skill.git "$HOME/.codex/skills/duan-hofas"
```

If Homebrew is unavailable, run `xcode-select --install` to install Apple's command-line tools, then run the last two commands above. Restart Codex after installation.

## Update

Ubuntu and macOS:

```bash
git -C "$HOME/.codex/skills/duan-hofas" pull
```

Windows PowerShell:

```powershell
git -C "$env:USERPROFILE\.codex\skills\duan-hofas" pull
```

## Usage examples

Invoke `$duan-hofas`, then ask directly; the detailed checks are handled automatically.

### 1. Ask which symbol Duan uses

```text
Duan 在这里用什么符号表示？
```

```text
Duan 如何表示 SUB-FAS 的奇异集、可行集和指数吸引域？
```

### 2. Check whether the original mathematical formulas follow Duan's habits

```text
检查原文的数学公式是否符合 Duan 的习惯。
```

Expected review format:

```text
位置 → 当前写法 → 推荐的 Duan 写法 → 原因 → [E]/[D]/[U]
```

### 3. Check whether a theorem follows Duan's writing habits

```text
Duan 会如何写这个定理？
```

```text
检查这个定理是否符合 Duan 的书写习惯。
```

### 4. Check whether definitions and assumptions are consistent with Duan

```text
检查定义和假设是否和 Duan 的一致。
```

### 5. Check a proof

```text
检查这个证明是否符合 Duan 的推导习惯。
```

### 6. Check article organization

```text
检查文章结构是否符合 Duan 的习惯。
```

### 7. Write a Remark or Example

```text
Duan 会如何写这个 Remark？
```

```text
Duan 会如何写这个算例？
```

### 8. Check simulation writing

```text
检查仿真章节是否符合 Duan 的书写习惯。
```

### 9. Create a paper template

```text
创建一个 Duan 风格的单阶 HOFAS 论文模板。
```

```text
创建一个 Duan 风格的多阶 SUB-FAS 论文模板。
```

### 10. Verify a disputed expression against the source

```text
这个表达来自 Duan 的哪篇原文？
```

The skill should use the quick guide for ordinary checks and return to the original source only when an exact expression, theorem, or attribution is disputed.

## Optional local source search

The skill itself does not include copyrighted PDFs or a generated search database. The paths in `references/source-catalog.md` and the defaults in the indexing scripts describe the original development machine. On another computer, provide the local PDF/database paths through the scripts' command-line options or update those local defaults before using source search. The notation checker and LaTeX template do not require the source index.

## Important boundary

For source-faithful definitions of original-system variables, dimensions, and the conditions on $f$ and $B$ that vary with the control objective, read `references/model-definition-registry.md`. Select the model family and objective first; do not promote one paper's smoothness or nonsingularity condition to a universal HOFAS assumption.

The quick guide captures recurring habits but does not replace checking the cited source. A paper-local notation choice is not automatically an error. When a mathematical claim or attribution is disputed, verify the exact equation, theorem, and page in the original source.

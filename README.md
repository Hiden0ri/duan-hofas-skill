# Duan HOFAS Skill

A private Codex skill for checking whether an HOFAS Markdown file or manuscript follows Guang-Ren Duan's recurring notation, terminology, article organization, and theorem-writing habits. It can also create a Duan-style IEEEtran-compatible LaTeX manuscript skeleton.

## Main uses

- Check symbols, dimensions, terminology, and model-family consistency.
- Check definitions, assumptions, the six-part theorem structure, and proof organization.
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

## Use

Examples:

```text
Use $duan-hofas to check whether the symbols and theorem structure in this Markdown file follow Duan's style.
```

```text
Use $duan-hofas to create a Duan-style HOFAS paper template for an IEEE Transactions manuscript.
```

## Optional local source search

The skill itself does not include copyrighted PDFs or a generated search database. The paths in `references/source-catalog.md` and the defaults in the indexing scripts describe the original development machine. On another computer, provide the local PDF/database paths through the scripts' command-line options or update those local defaults before using source search. The notation checker and LaTeX template do not require the source index.

## Important boundary

The quick guide captures recurring habits but does not replace checking the cited source. A paper-local notation choice is not automatically an error. When a mathematical claim or attribution is disputed, verify the exact equation, theorem, and page in the original source.

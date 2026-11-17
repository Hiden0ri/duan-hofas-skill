#!/usr/bin/env python3
"""Build clean, copyright-safe release archives (.skill, .zip, .tar.gz, npm .tgz, SHA256SUMS)."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tarfile
import zipfile
from pathlib import Path

ALLOWED_TOP = {"SKILL.md", "README.md", "README_zh-CN.md", "package.json"}
ALLOWED_DIRS = {"agents", "assets", "references", "scripts"}
FORBIDDEN_SUFFIXES = {".pdf", ".sqlite", ".sqlite3", ".db", ".pyc", ".pyo", ".tgz", ".skill"}


def collect_release_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for name in sorted(ALLOWED_TOP):
        p = root / name
        if p.is_file():
            files.append(p)
    for dname in sorted(ALLOWED_DIRS):
        d = root / dname
        if not d.is_dir():
            continue
        for p in sorted(d.rglob("*")):
            if not p.is_file() or p.is_symlink():
                continue
            if "__pycache__" in p.parts or p.suffix.lower() in FORBIDDEN_SUFFIXES:
                continue
            files.append(p)
    for p in files:
        rel = p.relative_to(root).parts
        if rel[0] in {"corpus", "reports", ".git", "dist", "node_modules"}:
            raise RuntimeError(f"Forbidden path in release bundle: {p}")
    return files


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    root_default = Path(__file__).resolve().parents[1]
    parser.add_argument("--root", type=Path, default=root_default)
    parser.add_argument("--out-dir", type=Path, default=root_default / "dist")
    args = parser.parse_args()

    root = args.root.resolve()
    out_dir = args.out_dir.resolve()
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pkg_meta = json.loads((root / "package.json").read_text(encoding="utf-8"))
    version = pkg_meta["version"]
    tag = f"v{version}"

    # 1. Run skill structure validation first
    subprocess.run(["python3", str(root / "scripts" / "validate_distillation.py"), str(root)], check=True)

    files = collect_release_files(root)

    # 2. Build duan-hofas.skill and duan-hofas-skill-vX.Y.Z.zip
    skill_path = out_dir / "duan-hofas.skill"
    zip_path = out_dir / f"duan-hofas-skill-{tag}.zip"
    for ztarget in (skill_path, zip_path):
        with zipfile.ZipFile(ztarget, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for p in files:
                arcname = Path("duan-hofas") / p.relative_to(root)
                zf.write(p, arcname.as_posix())

    # 3. Build duan-hofas-skill-vX.Y.Z.tar.gz
    tar_path = out_dir / f"duan-hofas-skill-{tag}.tar.gz"
    with tarfile.open(tar_path, "w:gz") as tf:
        for p in files:
            arcname = Path("duan-hofas") / p.relative_to(root)
            tf.add(p, arcname=arcname.as_posix(), recursive=False)

    # 4. Build npm package tarball via npm pack (if npm is installed)
    built_artifacts = [skill_path, zip_path, tar_path]
    if shutil.which("npm"):
        subprocess.run(
            ["npm", "pack", "--pack-destination", str(out_dir)],
            cwd=str(root),
            check=True,
        )
        for tgz in sorted(out_dir.glob("*.tgz")):
            built_artifacts.append(tgz)

    # 5. Generate SHA256SUMS.txt
    sums_path = out_dir / "SHA256SUMS.txt"
    lines = [f"{sha256_file(a)}  {a.name}" for a in built_artifacts]
    sums_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Built {len(built_artifacts)} release packages in {out_dir} ({len(files)} tracked skill files):")
    for line in lines:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Prepare only reviewed, public research content for GitHub Pages / MkDocs.

Does not read or copy private repos, their histories, issue metadata, secrets or game files.
Output (docs_generated/) is derived and ignored by Git; source files remain unchanged.
"""
from pathlib import Path
import shutil, sys

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "docs_generated"
REPORTS = sorted(ROOT.glob("REF_*.md"))
GUIDES = sorted((ROOT / "guides").glob("*.md"))
# Research topics are intentionally open-ended: newly added REF_*.md files
# must be published without requiring a maintainer to update a fixed count.
SOURCES = [
    ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "SECURITY.md",
    ROOT / "AUTO_MERGE.md",
    ROOT / "EVIDENCE_REFERENCES.md", ROOT / "RELEASE_NOTES.md",
    ROOT / "SCOPE_AND_LIMITATIONS.md", ROOT / "symbols.tsv",
    ROOT / "structs.tsv", ROOT / "LICENSE",
    ROOT / "reference" / "README.md",
    ROOT / "reference" / "static_calls.tsv",
    ROOT / "reference" / "relations.jsonl",
    ROOT / "reference" / "corrections.jsonl",
] + REPORTS + GUIDES + sorted((ROOT / "reference" / "symbols").glob("*.md")) + sorted(
    (ROOT / "reference" / "structs").glob("*.md")
)
if len(set(SOURCES)) != len(SOURCES):
    raise SystemExit("Duplicate documentation source")
if not all(p.is_file() and p.is_relative_to(ROOT) and not p.is_symlink() for p in SOURCES):
    raise SystemExit("Missing or invalid source file")
if DEST.exists():
    if DEST.is_symlink() or not DEST.is_dir():
        raise SystemExit("Output directory is not an ordinary directory")
    shutil.rmtree(DEST)
DEST.mkdir()
for path in SOURCES:
    relative = path.relative_to(ROOT)
    if relative.suffix.lower() in {".exe", ".dll", ".dat", ".zip", ".sqlite"}:
        raise SystemExit(f"Rejected source type: {relative}")
    to = DEST / relative
    to.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, to)
home = (ROOT / "HOME.md").read_text(encoding="utf-8")
(DEST / "index.md").write_text(home, encoding="utf-8", newline="\n")
# MkDocs reserves index.md for the homepage and suppresses README.md alongside it.
# Keep the full public README as GUIDE.md and preserve working local cross-links.
import re
original_guide = (DEST / "README.md").resolve()
(DEST / "README.md").rename(DEST / "GUIDE.md")
guide = DEST / "GUIDE.md"
guide_text = guide.read_text(encoding="utf-8")
guide_text = guide_text.replace(
    "](.github/workflows/research-ci.yml)",
    "](https://github.com/Vahren-exe-Research-Lab/Vahren.exe-research-open/blob/main/.github/workflows/research-ci.yml)",
)
guide.write_text(guide_text, encoding="utf-8", newline="\n")
link_pattern = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
for doc in DEST.rglob("*.md"):
    text = doc.read_text(encoding="utf-8")
    def rewrite_link(match):
        original = match.group(1)
        link_target = original.split("#", 1)[0].split("?", 1)[0]
        if not link_target or link_target.startswith(("http:", "https:", "#", "mailto:")):
            return match.group(0)
        if (doc.parent / link_target).resolve() == original_guide:
            return match.group(0).replace(link_target, link_target[:-9] + "GUIDE.md", 1)
        return match.group(0)
    revised = link_pattern.sub(rewrite_link, text)
    if doc == DEST / "GUIDE.md":
        revised = revised.replace("## 分野別の研究", "## 分野別の研究 {#research-topics}")
    if doc == DEST / "reference" / "README.md":
        revised = revised.replace("## 構造体一覧", "## 構造体一覧 {#struct-index}")
    revised = revised.replace("#分野別の研究", "#research-topics")
    revised = revised.replace("#構造体一覧", "#struct-index")
    if revised != text:
        doc.write_text(revised, encoding="utf-8", newline="\n")
print("PAGES_SOURCE_READY", len(SOURCES), "files plus homepage", len(REPORTS), "reports")

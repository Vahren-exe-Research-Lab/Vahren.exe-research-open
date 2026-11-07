#!/usr/bin/env python3
"""Guard against public-repository leakage of raw research fingerprints and assets.

This is a repository hygiene check, not a guarantee of anonymity or legal clearance.
It needs no secrets, private repositories, or network access.
"""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_TYPES = {".md", ".tsv", ".jsonl", ".json", ".py", ".txt"}
BLOCKED_TYPES = {
    ".exe", ".dll", ".dat", ".sav", ".ogg", ".mp3", ".wav",
    ".png", ".jpg", ".jpeg", ".webp", ".zip", ".7z", ".rar",
    ".db", ".sqlite", ".sqlite3", ".p12", ".pfx", ".key", ".pem",
}
MAX_FILE_BYTES = 20 * 1024 * 1024
SHA1 = re.compile(r"(?<![A-Fa-f0-9])[A-Fa-f0-9]{40}(?![A-Fa-f0-9])")
SHA256 = re.compile(r"(?<![A-Fa-f0-9])[A-Fa-f0-9]{64}(?![A-Fa-f0-9])")
WINDOWS_USER_PATH = re.compile(r"(?i)[a-z]:[\\/](?:Users|Documents and Settings)[\\/]")
UNIX_HOME_PATH = re.compile(r"(?i)(?<!\w)/(?:home|Users)/[A-Za-z0-9_.+-]+(?:/|$)")

def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
    )
    return [Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item]

def check_content(relative: Path, text: str) -> list[str]:
    findings: list[str] = []
    # .github workflows legitimately use full-length pinned Git commit hashes;
    # inspect research data and documentation instead.
    if relative.parts[0] != ".github":
        if SHA1.search(text):
            findings.append("40-character source fingerprint")
        if SHA256.search(text):
            findings.append("64-character source fingerprint")
    if WINDOWS_USER_PATH.search(text) or UNIX_HOME_PATH.search(text):
        findings.append("user-specific filesystem path")
    return findings

def scan() -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    for relative in tracked_files():
        source = ROOT / relative
        label = relative.as_posix()
        if relative.suffix.lower() in BLOCKED_TYPES:
            findings.append((label, "forbidden binary or original-game file type"))
            continue
        if source.is_symlink() or not source.is_file():
            findings.append((label, "symlink or non-file"))
            continue
        if source.stat().st_size > MAX_FILE_BYTES:
            findings.append((label, "unexpected large file"))
            continue
        if relative.suffix.lower() in TEXT_TYPES:
            try:
                content = source.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                findings.append((label, "non-UTF-8 text file"))
                continue
            for issue in check_content(relative, content):
                findings.append((label, issue))
    return findings

def main() -> int:
    found = scan()
    if found:
        for path, issue in found[:30]:
            print(f"BLOCKED: {path} — {issue}")
        print(f"Publication safety check failed: {len(found)} findings")
        return 1
    print(f"Publication safety check passed: {len(tracked_files())} tracked files")
    return 0

if __name__ == "__main__":
    sys.exit(main())

"""Batch docstring generator using local Ollama model via HTTP.

Usage:
    python scripts/generate_docstrings.py <path-or-file> [--write]

Without --write, it prints proposed changes. With --write, it overwrites the file(s).
Only processes .py files.
"""
from __future__ import annotations
import argparse
import json
import os
import sys
import textwrap
import urllib.request
from pathlib import Path

OLLAMA_HOST = "http://localhost:11434"
MODEL = "deepseek-coder:6.7b"  # use larger model for reasoning
PROMPT_TEMPLATE = """You are a senior Python engineer. Add or improve high quality Google-style docstrings for the following Python code. \
Preserve logic. Only modify spacing where needed. Return ONLY the updated code, no commentary.\n\nCODE:\n```python\n{code}\n```\n"""

def call_model(code: str) -> str:
    prompt = PROMPT_TEMPLATE.format(code=code)
    data = json.dumps({"model": MODEL, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(f"{OLLAMA_HOST}/api/generate", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as resp:
        payload = json.loads(resp.read().decode())
        return payload.get("response", "")


def process_file(path: Path, write: bool) -> None:
    original = path.read_text(encoding="utf-8")
    updated = call_model(original)
    print(f"\n=== {path} ===")
    if write:
        path.write_text(updated, encoding="utf-8")
        print("[written]")
    else:
        print(textwrap.indent(updated, prefix="  "))


def iter_python_files(target: Path):
    if target.is_file() and target.suffix == ".py":
        yield target
    elif target.is_dir():
        for p in target.rglob("*.py"):
            if "/.venv/" in str(p):
                continue
            yield p


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="File or directory")
    parser.add_argument("--write", action="store_true", help="Apply changes")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print("Target does not exist", file=sys.stderr)
        sys.exit(1)

    for py in iter_python_files(target_path):
        process_file(py, args.write)

if __name__ == "__main__":
    main()

"""Safe refactor assistant using local model.

Usage:
    python scripts/ai_refactor.py <file.py> [--write]

The model is instructed to preserve behavior. It returns only modified code.
"""
from __future__ import annotations
import argparse
import json
import sys
import urllib.request
from pathlib import Path

MODEL = "deepseek-coder:6.7b"
OLLAMA_HOST = "http://localhost:11434"
PROMPT = (
    "You are a senior engineer. Refactor the following Python code to improve readability, maintainability, and pythonic style. "
    "Preserve exact behavior and signatures. Return ONLY the updated code. If the code is already optimal, return it unchanged.\n\nCode:\n```python\n{code}\n```"
)

def call_model(code: str) -> str:
    data = json.dumps({
        "model": MODEL,
        "prompt": PROMPT.format(code=code),
        "stream": False
    }).encode()
    req = urllib.request.Request(f"{OLLAMA_HOST}/api/generate", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as resp:
        return json.loads(resp.read().decode()).get("response", "")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Python file to refactor")
    parser.add_argument("--write", action="store_true", help="Overwrite with refactored code")
    args = parser.parse_args()
    path = Path(args.file)
    if not path.exists() or path.suffix != ".py":
        print("Provide a valid .py file", file=sys.stderr)
        sys.exit(1)
    original = path.read_text(encoding="utf-8")
    updated = call_model(original)
    if args.write:
        path.write_text(updated, encoding="utf-8")
        print(f"Refactored and wrote: {path}")
    else:
        print(updated)

if __name__ == "__main__":
    main()

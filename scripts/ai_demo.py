"""Minimal local AI demo script.

Demonstrates calling the locally served model (deepseek-coder:6.7b) via the
Ollama HTTP API. This can be used in a README or CI badge context to prove
local inference works without external calls.
"""
from __future__ import annotations

import json
import textwrap
import urllib.request
import urllib.error

OLLAMA_HOST = "http://localhost:11434"
MODEL = "deepseek-coder:6.7b"

PROMPT = """Write a Python function named factorial that:
- Uses iteration (not recursion)
- Validates input (non-negative int)
- Has a clear docstring
"""

def generate(prompt: str) -> str:
    data = json.dumps({"model": MODEL, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(f"{OLLAMA_HOST}/api/generate", data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            payload = json.loads(resp.read().decode())
            return payload.get("response", "<no response>")
    except urllib.error.URLError as e:
        return f"Error contacting Ollama: {e}"


def main() -> None:
    print("== Local AI Demo ==")
    print(f"Model: {MODEL}")
    print("Prompt:\n" + textwrap.indent(PROMPT.strip(), prefix="  "))
    print("\nGenerating...\n")
    output = generate(PROMPT)
    print(textwrap.indent(output.strip(), prefix="  "))
    print("\nDone.")

if __name__ == "__main__":
    main()

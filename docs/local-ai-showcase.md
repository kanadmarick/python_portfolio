# Local Agentic AI Showcase

This repository demonstrates a **fully local, agentic AI coding stack**—an evolution beyond passive autocomplete. It supports fast inline completions, deeper reasoning, safe refactors, doc generation, and planned multi‑step autonomous workflows.

## Components
| Component | Role |
|-----------|------|
| Ollama | Serves the local model runtime |
| deepseek-coder:6.7b | Primary reasoning + structured generation |
| qwen2.5-coder:1.5b-base | Fast low-latency autocomplete model |
| Continue (VS Code) | Chat, refactor, inline edits, slash commands |
| Twinny (VS Code) | Supplemental inline completions |

## Why Local?
- Source code never leaves your machine
- Deterministic, repeatable environment
- Works offline
- Swap models instantly (experimentation)

## Quick Demo (Script)
Run a local inference (no external APIs) via:
```bash
python scripts/ai_demo.py
```
Expected output: a generated Python function (factorial) from the local model.

## VS Code Usage Summary
| Action | Shortcut |
|--------|----------|
| Open Continue Chat | Ctrl+Shift+I |
| Inline Chat | Ctrl+I |
| Accept Completion | Tab |
| Dismiss Completion | Esc |

## Example Prompts
- "Refactor this function to be more pythonic."
- "Write pytests for the selected class."
- "Optimize this algorithm for time complexity."
- "Add type hints and docstrings."

## Model Management
Swap or add models:
```bash
ollama pull deepseek-coder:1.3b
ollama pull codellama:7b-code
ollama pull starcoder:7b
```
Update `.continue/config.json` if you want a different default.

## Folder References
| Path | Purpose |
|------|---------|
| `.continue/config.json` | Continue + model settings |
| `CONTINUE_GUIDE.md` | Full usage guide |
| `QUICK_START_TEST.py` | Hands-on AI feature test steps |
| `scripts/ai_demo.py` | Minimal HTTP inference example |

## Suggested Screenshots / GIFs
Place media under `assets/` (add to .gitignore if large):
1. Dual-model tab completion (fast vs deep)
2. `/refactor-safe` transformation preview
3. `/docstrings` enriching code
4. CLI script (`ai_refactor.py`) before/after

## Roadmap Highlights
- Semantic embeddings + search index
- Plan/apply agentic multi-step refactors
- Test generator & mutation test advisor
- Local model benchmark dashboard
- Diff risk scoring heuristic

## Attribution / Notes
Model weights are not stored in the repo—retrieved on demand via Ollama.

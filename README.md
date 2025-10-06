# Local_Agentic_AL

This repository provides a **fully local agentic AI development environment**: offline code completion, autonomous refactoring helpers, documentation generation, and future semantic/code-search powered planning— all running on local Large Language Models (LLMs) with no external API calls.

---
## 🧠 What You Get
| Component | Role |
|-----------|------|
| Ollama | Runs/serves local models (HTTP API) |
| `deepseek-coder:6.7b` | Primary code & reasoning model |
| (Optional) `qwen2.5-coder:1.5b-base` | Lightweight fast model |
| Continue (VS Code extension) | Chat, edits, multi-line refactors, slash commands |
| Twinny (VS Code extension) | Supplemental inline completions |
| `.continue/config.json` | Model + autocomplete tuning |
| `CONTINUE_GUIDE.md` | Full usage walkthrough |
| `scripts/ai_demo.py` | Minimal model call example |

---
## 🚀 Quick Start
1. Install **Ollama** (already done locally)  
2. Pull or ensure model present:
	```bash
	ollama pull deepseek-coder:6.7b
	```
3. Open VS Code → start typing in any Python / JS file → accept suggestions with `Tab`.
4. Open AI chat: `Ctrl+Shift+I` (Continue panel).  
5. Try a command: highlight code → type `/explain` or `/optimize`.

Want a direct API generation demo:
```bash
python scripts/ai_demo.py
```

---
## ⌨️ Key Shortcuts (VS Code)
| Action | Shortcut |
|--------|----------|
| Open Continue Chat | Ctrl+Shift+I |
| Inline Chat | Ctrl+I |
| Accept Completion | Tab |
| Cycle Suggestions (Twinny) | (Depends on extension settings) |
| Dismiss Completion | Esc |

---
## 🔧 Model Management
Add / switch models:
```bash
ollama pull deepseek-coder:1.3b      # smaller, faster
ollama pull codellama:7b-code        # alternative
ollama pull starcoder:7b             # general code model
ollama pull llama3.1:8b              # broader reasoning
```
Update `.continue/config.json` to switch the active model for chat/autocomplete.

### Dual-Model Strategy (Recommended)
| Use Case | Model |
|----------|-------|
| Fast autocomplete | `qwen2.5-coder:1.5b-base` |
| Deeper refactor / tests | `deepseek-coder:6.7b` |

---
## 🛠 Configuration Hints
`temperature`: 0.1–0.25 for deterministic code.  
`maxTokens`: Keep tab completion low (<= 500) for responsiveness.  
`prefix/suffix percentages`: Tune how much context Continue sends (already set).  

---
## 🧪 Files to Explore
| File | Purpose |
|------|---------|
| `continue_test.py` | Multi-function AI test playground |
| `QUICK_START_TEST.py` | Step‑by‑step interaction script |
| `local_llm_test.py` | Basic placeholders for completions |
| `scripts/ai_demo.py` | Raw HTTP generation example |
| `CONTINUE_GUIDE.md` | Extended how-to + tips |
| `docs/local-ai-showcase.md` | GitHub‑ready overview |

---
## 🧪 Example Prompt Ideas
* "Add type hints and docstrings to this function."  
* "Generate pytest tests covering edge cases."  
* "Refactor to use dependency injection."  
* "Explain what this class does in bullet points."  
* "Optimize this algorithm for large inputs."  

---
## ❗ Troubleshooting
| Issue | Fix |
|-------|-----|
| No suggestions appear | Ensure model loaded: `ollama list` |
| Slow responses | Use smaller model (`deepseek-coder:1.3b` or `qwen2.5-coder:1.5b-base`) |
| High VRAM/RAM usage | Close other GPU tasks / switch model |
| Repetitive output | Lower `temperature` |
| Model not found | `ollama pull <model>` |

---
## 🔐 Privacy & Offline Mode
All inference happens locally. No source code or prompts are sent externally unless you manually configure a remote provider.

---
## 🗺 Roadmap (Agentic Focus)
- [x] Dual-model config (fast autocomplete + deeper reasoning)  
- [x] Refactor CLI (`scripts/ai_refactor.py`)  
- [x] Docstring generator (`scripts/generate_docstrings.py`)  
- [ ] Semantic embeddings + code search (`scripts/code_search.py`)  
- [ ] Test skeleton generator (`scripts/test_generator.py`)  
- [ ] Agentic multi-step planner (analyze → plan → apply)  
- [ ] Auto-upgrade suggestions (API change diffing)  
- [ ] Optional minimal web UI / TUI dashboard  

---
## 🤝 Contributions
Future contributions will focus on improving local AI workflows, tooling automation, and model experimentation.

---
## 📄 License
Add a license (MIT recommended) — not yet included.

---
## ✅ Status
Active: evolving into a pure **Local AI Engineering Toolkit**.


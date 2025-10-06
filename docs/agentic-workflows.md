# Agentic Workflows (Planned)

This document tracks the design of emerging *agentic* capabilities for the Local Agentic AI environment.

## Vision
Enable the local model(s) to perform structured multi-step tasks:
1. Analyze selected code / repo slice
2. Produce a plan (bullet steps)
3. Execute transformations (with human approval checkpoints)
4. Generate tests / docs for modified regions
5. Summarize changes

## Core Building Blocks
| Capability | Source |
|------------|-------|
| Static code read | Direct filesystem + AST parsing (planned) |
| Reasoning | DeepSeek Coder 6.7B |
| Fast suggestions | Qwen 1.5B coder |
| Search / retrieval | (Planned) embeddings with `nomic-embed-text` |
| Safe apply | Diff preview + user confirmation |

## Proposed Commands
| Command | Description | Status |
|---------|-------------|--------|
| `/plan` | Generate a multi-step refactor/feature plan | Planned |
| `/implement-step` | Apply one plan step | Planned |
| `/improve-tests` | Enhance test coverage for given files | Planned |
| `/upgrade-deps` | Suggest dependency upgrades + code adjustments | Planned |
| `/risk-audit` | Identify potential error/edge cases | Planned |

## Architecture Sketch
```
User Selection → Context Builder → (Optional) Embedding Retriever → Reasoning Model
        ↓                                      ↑
    Plan Draft ← Feedback Loop ← Execution Result (Diff / Tests)
```

## Safety / Guardrails
- Always produce unified diff before write
- Never delete code without plan rationale
- Provide rollback snippet

## Incremental Milestones
1. (Current) Manual scripts (refactor, docstrings)
2. Add semantic search + file ranking
3. Introduce `/plan` command (no auto apply)
4. Add `/implement-step` with diff preview
5. Add persistent plan state (JSON file)
6. Add scoring heuristics (complexity, churn, size)

## Open Questions
- Persist plan state per branch? per workspace?
- Should risk analysis integrate simple static checks (e.g., bandit)?
- Provide model selection heuristic automatically?

## Contributions
Feedback welcome—open an issue with prefix `[agentic]`.

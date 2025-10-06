# Semantic Code Search (Planned)

## Goal
Enable local, privacy-preserving semantic search over the codebase to feed higher quality context into agentic workflows.

## Approach
1. Use `nomic-embed-text` (via Ollama) to embed file chunks.
2. Maintain an on-disk vector store (simple: JSON + FAISS optional later).
3. Provide a CLI: `scripts/code_search.py "async database layer"`.
4. Return top-k matches with file:line spans.

## Chunking Strategy
| Aspect | Choice |
|--------|-------|
| Size | 350–600 tokens |
| Overlap | 40–60 tokens |
| Filtering | Skip binary / vendor / large generated files |

## Data Structure (MVP)
```jsonc
[
  {
    "id": "projects/project1/backend/app.py::chunk_0",
    "embedding": [...],
    "text": "from flask import ...",
    "path": "projects/project1/backend/app.py",
    "start_line": 1,
    "end_line": 58
  }
]
```

## CLI Outline (Draft)
```bash
python scripts/code_search.py "jwt auth handler" --k 5
```

## Future Enhancements
- Replace JSON store with SQLite (vector extension) or Chroma
- Add incremental update (watch for file changes)
- Integrate into Continue context builder

## Risks / Mitigations
| Risk | Mitigation |
|------|------------|
| Large repo memory use | Lazy load & limit chunks |
| Stale embeddings | Track file mtimes & re-embed changed chunks |
| Slow queries | Pre-normalize vectors; approximate search later |

## Status
Design stage. Implementation not started.

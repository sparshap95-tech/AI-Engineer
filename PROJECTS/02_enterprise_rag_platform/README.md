# Project 2: Enterprise Knowledge Intelligence Platform (Month 2)

> **Goal**: Build an enterprise document intelligence and hybrid retrieval system that goes far beyond a naive PDF chatbot.

---

## 🏗️ Architecture & Core Components

```
Documents (PDF, DOCX, CSV, Web, DB)
   │
   ▼
[Ingestion & Multi-Format Parsing Engine]
   │
   ▼
[Chunking Engine] (Hierarchical, Sentence-Window, Semantic, Parent-Child)
   │
   ▼
[Embedding & Indexing Layer]
   ├── Dense Vectors (pgvector / FAISS)
   └── Sparse Inverted Index (BM25)
   │
   ▼
[Hybrid Retrieval Pipeline]
   ├── Dense Search (Cosine / Dot Product)
   ├── Sparse Search (BM25 Lexical)
   └── Reciprocal Rank Fusion (RRF)
   │
   ▼
[Cross-Encoder Reranker] (FlashRank / BGE-Reranker)
   │
   ▼
[Context Construction & Grounded Generation] (LLM + Citations)
   │
   ▼
[Evaluation & Faithfulness Scoring] (RAGAS)
```

---

## 📂 Implementation Modules

1. **`ingestion/`**: High-fidelity parsers for PDF, DOCX, CSV, Markdown, and tabular data.
2. **`chunking/`**: Recursive character chunker, semantic chunker, sentence-window with parent-child reference maps.
3. **`retrieval/`**:
   - `dense_retriever.py`: Vector embeddings via `pgvector`.
   - `bm25_retriever.py`: Lexical BM25 indexer.
   - `hybrid_rrf.py`: Reciprocal Rank Fusion algorithm combining dense and sparse scores.
   - `reranker.py`: Cross-encoder reranking step.
4. **`generation/`**: Citation-augmented prompting and answer synthesis.
5. **`evals/`**: Faithfulness, context relevance, and groundedness tests.

---

## 🛠️ Tech Stack
- **Database**: PostgreSQL 16 + `pgvector`
- **Embeddings**: `text-embedding-3-small` / `all-MiniLM-L6-v2`
- **Reranker**: `flashrank` / `bge-reranker-base`
- **Backend**: FastAPI + Pydantic

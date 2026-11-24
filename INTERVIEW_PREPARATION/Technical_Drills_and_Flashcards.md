# Technical Interview Drills & Master Flashcards

This repository contains targeted interview preparation spanning the 4 levels of technical depth:
- **Level 1**: 30-Second High-Level Definition
- **Level 2**: 2-Minute Architecture & Component Flow
- **Level 3**: 10-Minute Deep Engineering Explanation
- **Level 4**: End-to-End Enterprise System Design

---

## 🗂️ Flashcard Drills

### Track 1: RAG & Retrieval Systems
1. **What is RAG?**
   - *Level 1*: RAG retrieves relevant external information from a knowledge store and provides it as grounded context to an LLM before generation.
   - *Level 2*: Architecture consists of Document Loaders → Chunking → Embeddings → Vector DB/Inverted Index → Hybrid Retrieval → Cross-Encoder Reranker → Context Injection → LLM generation with Citations.
2. **RAG vs. Fine-Tuning?**
   - Use **RAG** when you need new factual knowledge, dynamic updates, private source attribution, and zero retraining costs.
   - Use **Fine-Tuning** when you need to change the style, tone, format, or task behavior (e.g. specialized medical shorthand or JSON extraction).
3. **What is Hybrid Search and why is it superior to Vector-only search?**
   - Dense vector embeddings capture semantic meaning but struggle with exact keywords, part numbers, and rare domain acronyms. Sparse BM25 excels at exact keyword matches. Combining both using Reciprocal Rank Fusion (RRF) delivers high recall and precision.
4. **Why use a Cross-Encoder Reranker?**
   - Bi-encoder vector search computes cosine distance on independent representations for speed ($O(1)$ lookup). A cross-encoder processes `(query, document)` jointly through all attention layers, capturing intricate semantic alignment and boosting top-K precision by 15-30%.

---

### Track 2: Agent Systems & LangGraph
1. **What is the difference between an LLM and an AI Agent?**
   - An LLM maps `Input → Output`. An Agent operates in a goal-driven loop: `Goal → Reason/Decide → Select Tool → Execute Tool → Observe Result → Update State → Loop/Conclude`.
2. **Why use LangGraph instead of a simple while-loop?**
   - Complex multi-step agent systems require deterministic state transitions, conditional routing, cyclic graphs, persistence/checkpoints across network drops, and human-in-the-loop interrupt mechanisms.
3. **What is the Model Context Protocol (MCP)?**
   - MCP is an open standard created by Anthropic that provides a uniform JSON-RPC protocol for AI systems to discover, inspect, and execute tools, resources, and prompts across heterogeneous data sources (Databases, CRMs, APIs) without proprietary adapters.

---

### Track 3: System Design Scenarios
1. **Design an Enterprise AI Platform for 1 Million Users**:
   - CDN / WAF → API Gateway (FastAPI) with rate limiting & JWT auth.
   - AI Orchestrator with prompt cache & Redis semantic cache.
   - Vector Store cluster (PostgreSQL + pgvector / Qdrant) with HNSW indexes.
   - Asynchronous worker queues (Celery/Kafka) for heavy ingestion and batch calls.
   - Observability via Langfuse & OpenTelemetry.
   - Guardrail verification layer (NeMo/Regex) before response delivery.

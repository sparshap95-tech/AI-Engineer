# 🚀 6-Month World-Class AI Engineering Master Roadmap

> **Target Profile**: AI/ML Learner → LLM Engineer → RAG Engineer → Agent Engineer → Production AI Engineer → AI Systems Engineer  
> **Core Principle**: 30% Learning | 60% Building Production Systems | 10% Technical Interviews

---

## The Master 12-Layer Map

```
                  ┌──────────────────────────────┐
                  │   WORLD-CLASS AI ENGINEER    │
                  └──────────────┬───────────────┘
                                 │
                  ┌──────────────┴───────────────┐
                  │       AI SYSTEM DESIGN       │
                  └──────────────┬───────────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         │                       │                       │
   AGENT SYSTEMS            LLM SYSTEMS              PRODUCTION
         │                       │                       │
   • Tools / MCP           • RAG / Search          • Cloud / Docker
   • Memory                • Fine-tuning           • CI/CD
   • Planning              • Inference             • Observability
   • Workflows             • Multimodal            • Security
   • Multi-agent           • Model Selection       • Scaling
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                       EVALUATION & TESTING
                                 │
                         DATA & KNOWLEDGE
                                 │
                       SOFTWARE ENGINEERING
                                 │
                      ML / DL / NLP FOUNDATIONS
```

---

## 📅 The 6-Month Phase Breakdown

### Phase 0: Month 1 — LLM Engineering Foundations
- **Core Goal**: Transition from *"send prompt → get answer"* to:  
  `model + context + tools + memory + retrieval + constraints + evaluation + infrastructure`
- **Curriculum**:
  - **Tokenization**: BPE, WordPiece, SentencePiece, token counting, vocabulary encoding, chat templates.
  - **Transformer Internals**: Self-attention, causal attention, cross-attention, RoPE, RMSNorm, SwiGLU, KV cache.
  - **Modern LLM Architecture**: Dense vs MoE, context windows, reasoning models, instruction tuning.
  - **API Engineering**: OpenAI-compatible, Anthropic, Gemini, local models (Ollama, Hugging Face), streaming SSE, retries, rate-limiting, async inference.
  - **Structured Outputs**: Pydantic v2 schemas, JSON Schema constraints, function/tool calling validation, fallback handling.
- **Project 1 Built**: `PROJECTS/01_production_llm_api/`

---

### Phase 1: Month 2 — RAG Engineering
- **Core Goal**: Enterprise document intelligence beyond naive PDF chat.
- **Curriculum**:
  - **Document Engineering**: High-fidelity parsing of PDF, DOCX, CSV, PPTX, HTML, Markdown, and tabular data.
  - **Chunking Strategies**: Fixed-size, recursive, semantic chunking, sentence-window chunking, parent-child retrieval, metadata-aware chunking.
  - **Embeddings**: Dense embeddings, sparse embeddings (BM25), dimensions, normalization, cosine similarity.
  - **Vector Databases**: PostgreSQL + `pgvector` (production core), FAISS, Qdrant.
  - **Hybrid Retrieval & Reranking**: Dense + BM25 combined with Reciprocal Rank Fusion (RRF), cross-encoder rerankers (`flashrank`, `bge-reranker`).
  - **Advanced RAG**: GraphRAG, SQL RAG, contextual retrieval, query rewriting, HyDE, source citation, groundedness evaluation.
- **Project 2 Built**: `PROJECTS/02_enterprise_rag_platform/`

---

### Phase 2 & 3: Month 3 — Agent Engineering & Model Context Protocol (MCP)
- **Core Goal**: Architect stateful, resilient tool-using agents and standardized MCP integrations.
- **Curriculum**:
  - **Agent Foundations**: ReAct loop (Thought → Action → Observation), planner-executor pattern, reflection, self-critique, verifiers.
  - **Agent State**: Short-term, working memory, long-term memory, episodic and semantic memory.
  - **LangGraph State Machines**: Nodes, state schemas, conditional edges, checkpoints, interrupts, human-in-the-loop approval gates.
  - **Model Context Protocol (MCP)**: MCP Architecture (Client, Server, Transports, Tools, Resources, Prompts, Auth, Security).
  - **Multi-Agent Systems**: Supervisor pattern, specialist agents, delegation, message passing, hierarchical swarms.
- **Project 3 Built**: `PROJECTS/03_tool_using_agent_mcp/`

---

### Phase 4: Month 4 — Evaluation, Observability & AI Security
- **Core Goal**: Eliminate silent failures; make agents measurable, observable, and hardened.
- **Curriculum**:
  - **LLM Evaluation**: Golden benchmark datasets, LLM-as-a-judge, pairwise evals, regression testing.
  - **Metrics**: RAG (Faithfulness, Context Relevance, Answer Relevance, Groundedness), Agent (Task success, tool accuracy, trajectory efficiency, cost, latency).
  - **Observability**: OpenTelemetry spans, Langfuse / Phoenix tracing for LLM calls, tool executions, token usage, cost breakdowns.
  - **AI Security & Guardrails**: Prompt injection defense (direct & indirect), jailbreaking detection, tool permission sandboxing, PII masking, NeMo Guardrails.
- **Project 4 Built**: `PROJECTS/04_evaluated_multi_agent_system/`

---

### Phase 5: Month 5 — Production AI Engineering & LLMOps
- **Core Goal**: Move from *"I built an agent"* to *"I can operate and scale an AI system."*
- **Curriculum**:
  - **Backend & Distributed Systems**: FastAPI async architecture, WebSockets, Redis caching & queues, Celery/Kafka worker pipelines.
  - **Databases & Vector Storage**: PostgreSQL indexing, connection pooling, JSONB, pgvector HNSW/IVFFlat tuning.
  - **Containerization & CI/CD**: Docker multi-stage builds, docker-compose, GitHub Actions CI/CD pipelines, automated eval gates.
  - **Inference Engineering**: Continuous batching, KV caching, quantization (GGUF, AWQ, INT8/INT4), vLLM deployment.
  - **LLMOps**: Model registries, prompt versioning, canary deployments, fallback circuit breakers.
- **Project 5 Built**: `PROJECTS/05_production_llmops_platform/`

---

### Phase 6: Month 6 — Advanced AI Systems & Capstone Platform
- **Core Goal**: Architect and deliver an enterprise-grade autonomous operating platform.
- **Curriculum**:
  - **Fine-Tuning**: Decision criteria (RAG vs Fine-tuning), LoRA, QLoRA, SFT, instruction dataset curation, preference alignment (DPO).
  - **Multimodal AI**: Vision (VLMs, document intelligence), Audio (STT/TTS, streaming voice agents).
  - **Harness & Context Engineering**: Context compression, context caching, lost-in-the-middle mitigations, deterministic verification harnesses.
  - **Enterprise AI System Design**: Architecting for 1M+ requests, multi-tier caching, security, rate limiting, and cost controls.
- **Final Capstone Built**: `PROJECTS/06_enterprise_ai_operations_platform/`

---

## 🏆 Portfolio Projects Summary

| Project | Name | Core Stack | Key Capabilities |
|---|---|---|---|
| **01** | **Production LLM API** | FastAPI, Pydantic, Tenacity, Docker | Multi-provider Gateway, SSE Streaming, Schema Validation, Cost Tracking |
| **02** | **Enterprise Knowledge Platform** | PostgreSQL, pgvector, BM25, Reranker | Multi-doc Ingestion, Hybrid Search, RRF, Citations, Faithfulness Evals |
| **03** | **Tool Agent + MCP System** | LangGraph, MCP SDK, Python | State Machine, ReAct Loop, Multi-MCP Client (DB, CRM, Web), Memory |
| **04** | **Evaluated Multi-Agent System** | Langfuse, OpenTelemetry, RAGAS, Guardrails | LLM-as-a-Judge, Trajectory Evals, Prompt Injection Defense, Tracing |
| **05** | **Production LLMOps Platform** | Redis, Celery, Docker, GitHub Actions, vLLM | Distributed Tasks, Model/Prompt Registry, Canary Rollouts, KV Cache Tuning |
| **06** | **Enterprise Autonomous Ops (Capstone)** | LangGraph, MCP, FastAPI, pgvector, Redis, RBAC | Supervisor Swarm, Human Approval Gates, End-to-End Enterprise Automation |

---

## 📌 Master Note Template Rule
For every technology studied, maintain notes using this strict 7-question format:
1. **What is it?**
2. **Why does it exist?**
3. **What problem does it solve?**
4. **How does it work internally?**
5. **When should I use it?**
6. **What are the alternatives/trade-offs?**
7. **How would I deploy it in production?**

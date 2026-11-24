# Project 1: Production LLM API Gateway

A robust, enterprise-ready Multi-Provider LLM Gateway built with FastAPI, Pydantic v2, and Tenacity.

---

## 🎯 Features
- **Multi-Provider Routing**: Seamlessly dispatch requests to OpenAI, Anthropic, Gemini, local Ollama, or offline test mocks.
- **Server-Sent Events (SSE) Streaming**: Low-latency incremental token streaming (`stream: true`).
- **Strict Structured Outputs**: Direct extraction using validated Pydantic schemas.
- **Resilience Engine**: Exponential backoff retries on transient errors and automated fallback model failover.
- **Observability & Accounting**: Exact/heuristic token calculation (`tiktoken`) and dynamic USD cost calculation per request.
- **Correlation Tracing**: `X-Request-ID` and latency headers on every response.
- **Production Packaging**: Multi-stage lightweight Docker image and `docker-compose.yml`.

---

## 🚀 Quick Start

### Local Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the server
uvicorn app.main:app --reload --port 8000
```
Visit the interactive Swagger UI at: `http://localhost:8000/docs`

### Run with Docker
```bash
docker-compose up --build -d
```

### Run Tests
```bash
pytest tests/ -v
```

---

## 📑 Documentation
- [Architecture & Diagrams](file:///C:/Users/user/.gemini/antigravity/scratch/AI-Engineer/PROJECTS/01_production_llm_api/Architecture.md)
- [Design Decisions & Trade-offs](file:///C:/Users/user/.gemini/antigravity/scratch/AI-Engineer/PROJECTS/01_production_llm_api/Design_Decisions.md)
- [API Specification](file:///C:/Users/user/.gemini/antigravity/scratch/AI-Engineer/PROJECTS/01_production_llm_api/API_Design.md)
- [Interview Revision Sheet](file:///C:/Users/user/.gemini/antigravity/scratch/AI-Engineer/PROJECTS/01_production_llm_api/Interview_Questions.md)

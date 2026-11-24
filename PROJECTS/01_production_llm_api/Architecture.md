# Architecture: Production LLM API Gateway

## System Architecture Diagram

```
 Client / Application
       │
       ▼ [HTTPS / JSON]
┌────────────────────────────────────────────────────────┐
│                   FastAPI Application                  │
│                                                        │
│  [Middleware]                                          │
│   ├── Correlation ID Generator (X-Request-ID)          │
│   └── Latency Timer & Structured Request Logger        │
│                                                        │
│  [Endpoints]                                           │
│   ├── POST /v1/chat/completions                        │
│   ├── POST /v1/extract (Pydantic Schema Validator)     │
│   └── GET  /v1/models (Catalog & Pricing)              │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│                   LLM Gateway Core                     │
│                                                        │
│  [Resilience Layer]                                    │
│   ├── Exponential Backoff Retry (Tenacity)             │
│   └── Fallback Model Failover Circuit                  │
│                                                        │
│  [Provider Router]                                     │
│   ├── OpenAI / Compatible API                          │
│   ├── Anthropic API                                    │
│   ├── Gemini API                                       │
│   ├── Local Ollama API (localhost:11434)               │
│   └── Mock Simulation Provider                         │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│                   Accounting & Tracker                 │
│   ├── Token Counter (tiktoken cl100k_base)             │
│   └── Cost Calculator (Input / Output rates per model) │
└────────────────────────────────────────────────────────┘
```

## Data Flow
1. **Request Intake**: Client submits chat completion request with target model, messages, optional streaming, and schema constraint.
2. **Correlation & Logging**: Middleware stamps a unique `X-Request-ID` and records request metadata.
3. **Execution with Retry**: `gateway.py` routes the payload to the matching provider. If transient 5xx/network errors occur, exponential retry triggers up to 3 times.
4. **Fallback Mechanism**: If the primary provider exhausts retries or is unavailable, the gateway automatically switches to `fallback_model` to maintain high availability.
5. **Usage & Cost Calculation**: Prompt and response tokens are measured and calculated against pricing tiers.
6. **Delivery**: Returns a complete OpenAI-compliant JSON payload or streams SSE tokens via `StreamingResponse`.

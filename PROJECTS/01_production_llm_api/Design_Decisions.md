# Design Decisions & Engineering Trade-offs

## 1. Why FastAPI over Flask or Django?
- **Decision**: Used `FastAPI` with asynchronous request handling.
- **Rationale**: LLM API calls are I/O bound and high-latency (often 1-10 seconds). Standard synchronous workers block OS threads, causing catastrophic concurrency collapse under modest load. FastAPI's `asyncio` event loop allows thousands of concurrent open connections waiting on upstream LLM tokens with minimal memory overhead.

## 2. Why Pydantic v2 for Structured Outputs?
- **Decision**: Built strictly on Pydantic v2 core schemas.
- **Rationale**: Direct string generation from LLMs causes downstream application crashes when JSON keys are missing or malformed. Pydantic v2 compiles to Rust, offering 5-20x faster serialization and validation with type guarantees.

## 3. Streaming (SSE) vs WebSockets
- **Decision**: Selected Server-Sent Events (SSE) via `StreamingResponse`.
- **Rationale**: LLM text generation is fundamentally unidirectional (server continuously pushes tokens until completion). SSE operates over standard HTTP/1.1 or HTTP/2, requires no custom stateful connection handshake, works through corporate proxies and CDN firewalls, and automatically reconnects.

## 4. Why Exponential Backoff Retries?
- **Decision**: Integrated `tenacity` with `wait_exponential`.
- **Rationale**: LLM providers experience severe burst rate-limits (HTTP 429) and transient internal server errors (HTTP 500/503). Retrying immediately causes thundering herd problems that exacerbate outages. Exponential backoff smooths out burst traffic.

## 5. Token & Cost Accounting at Gateway Layer
- **Decision**: Token and cost calculation are executed directly in the API gateway rather than delegated to client applications.
- **Rationale**: Centralizing telemetry prevents unauthorized runaway spend, provides audit logs across heterogeneous upstream providers, and enables future multi-tenant quota enforcement.

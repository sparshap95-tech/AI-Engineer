# Project 4: Evaluated, Observable & Secure Multi-Agent System (Month 4)

> **Goal**: Turn autonomous agent workflows into a fully evaluated, observable, and secured enterprise production system.

---

## 🏗️ Architecture

```
                       User Request
                            │
                            ▼
              ┌───────────────────────────┐
              │    Input Security Guard   │ (Prompt Injection / Jailbreak Filter)
              └─────────────┬─────────────┘
                            │
                            ▼
              ┌───────────────────────────┐
              │  Supervisor Orchestrator  │
              └─────────────┬─────────────┘
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
  [Research Agent]   [Finance Agent]    [Property Agent]
         │                  │                  │
         └──────────────────┼──────────────────┘
                            │
                            ▼
              ┌───────────────────────────┐
              │    Verifier & Guardrail   │ (Schema, Policy & PII Redaction)
              └─────────────┬─────────────┘
                            │
                            ▼
                     Final Response

══════════════════════════════════════════════════════════════
               CROSS-CUTTING OBSERVABILITY & EVALS
  • OpenTelemetry & Langfuse: Traces, Spans, Latency, Token Cost
  • LLM-as-a-Judge: Golden Benchmark Dataset Regressions
  • Trajectory Evals: Tool Selection Precision, Step Efficiency
══════════════════════════════════════════════════════════════
```

---

## 🔑 Key Features
- **Evaluation Suite**: Automated benchmark running golden datasets, measuring task completion rates and tool choice accuracy.
- **Full Trace Observability**: End-to-end tracing showing every sub-agent dispatch, tool call, input/output payload, and latency distribution.
- **AI Security Shield**:
  - Direct & indirect prompt injection detection.
  - Secret and PII leakage prevention.
  - Strict sandboxing on external API invocations.

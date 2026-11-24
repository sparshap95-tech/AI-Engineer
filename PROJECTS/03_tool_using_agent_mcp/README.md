# Project 3: Tool-Using Agent + Model Context Protocol (MCP) (Month 3)

> **Goal**: Build an autonomous, state-machine agent powered by LangGraph and standardized Model Context Protocol (MCP) servers.

---

## 🏗️ Architecture

```
                       USER REQUEST
                            │
                            ▼
               ┌────────────────────────┐
               │    LangGraph Agent     │
               │     State Machine      │
               └────────────┬───────────┘
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
  [ReAct Loop]       [Memory Store]     [Checkpoints]
  Thought-Action     Short / Working    Durable State
  & Self-Critique    & Long-Term Mem    & Interrupts
         │                  │                  │
         └──────────────────┼──────────────────┘
                            │
                            ▼
               ┌────────────────────────┐
               │    MCP Client Core     │
               │ (Model Context Protocol│
               └────────────┬───────────┘
                            │
         ┌──────────────────┼──────────────────┐
         ▼                  ▼                  ▼
  [Database MCP]       [CRM/ERP MCP]      [Search MCP]
   SQL & Schemas      Customer Records     Web & Docs
```

---

## 🔑 Key Features
- **Deterministic State Graph**: Nodes, conditional edge routing, cyclical execution with max step bounds.
- **Model Context Protocol (MCP)**: Standardized JSON-RPC protocol to expose tools and resources without custom glue code.
- **Human-in-the-Loop Interrupts**: Approval gates before destructive actions (e.g. database updates or financial transactions).
- **Multi-tiered Memory**: Short-term conversation buffer + persistent state snapshots.

# Phase 0: LLM Engineering Foundations

> **Core Goal**: Stop thinking *"I send prompt → I get answer."*  
> Start thinking: `model + context + tools + memory + retrieval + constraints + evaluation + infrastructure`

---

## 📚 Curriculum & Modules

### 1. Tokenization Deep Dive
- **BPE (Byte-Pair Encoding)**: Subword merge algorithms and vocab training. See [BPE.ipynb](file:///C:/Users/user/.gemini/antigravity/scratch/AI-Engineer/llm_engineering_foundations/tokenization/BPE.ipynb).
- **WordPiece vs SentencePiece**: Differences in whitespace handling, UNK frequency, and cross-lingual efficiency.
- **Token Counting & Vocabulary**: Special tokens (`<|im_start|>`, `<|endoftext|>`), chat templates, and formatting.

### 2. Transformer Internals
- **Attention Mechanisms**: Self-attention, multi-head attention, causal (masked) attention, cross-attention.
- **Modern Positional Encodings**: Absolute, sinusoidal, Rotary Position Embeddings (RoPE), YaRN.
- **Normalization & Activations**: LayerNorm, RMSNorm, SwiGLU, GeLU, residual connections.
- **Architectural Paradigms**: Encoder-only (BERT), Encoder-Decoder (T5), Decoder-only (GPT, LLaMA).

### 3. Modern LLM Architecture
- Dense vs. Mixture of Experts (MoE) routing.
- Context windows & KV Cache memory calculations ($2 \times 2 \times n_{layers} \times n_{heads} \times d_{head} \times context$).
- Reasoning models (Chain-of-Thought, test-time compute) and Instruction Tuning (SFT, RLHF, DPO).

### 4. LLM API Engineering
- OpenAI-compatible endpoints, Anthropic, Gemini, and Ollama local APIs.
- Streaming with Server-Sent Events (SSE).
- Structured outputs with JSON Schema & Pydantic validation.
- Exponential backoff retries, timeouts, and fallback routing.

---

## 🛠️ Project Built in this Phase
👉 **[PROJECTS/01_production_llm_api](file:///C:/Users/user/.gemini/antigravity/scratch/AI-Engineer/PROJECTS/01_production_llm_api)**

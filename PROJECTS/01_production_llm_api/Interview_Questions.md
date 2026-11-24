# Project 1: Technical Interview Questions & Flashcards

### Q1: What happens when an upstream LLM API returns a 429 Too Many Requests error?
**Answer**:
A production gateway handles 429 errors using an exponential backoff retry policy with jitter (e.g., using `tenacity`). If repeated retries within a configurable budget (e.g. 3 attempts over 5 seconds) fail, the circuit breaker pattern routes the request to an alternative fallback model (e.g. from OpenAI `gpt-4o` to Anthropic `claude-3-5-sonnet` or a smaller self-hosted model).

### Q2: How does Server-Sent Events (SSE) streaming reduce perceived latency (Time-to-First-Token)?
**Answer**:
Without streaming, the client must wait for the full sequence to generate (e.g. 1500 tokens at 50 tokens/sec = 30 seconds), leading to high Time-To-First-Token (TTFT). With SSE, the gateway yields each token immediately as it arrives via chunked HTTP transfer encoding. TTFT drops from 30 seconds to ~200-500ms, vastly improving user experience.

### Q3: How do you guarantee that an LLM response adheres strictly to a required JSON schema?
**Answer**:
Three complementary techniques:
1. **API-level constrained decoding**: Pass `response_format={"type": "json_schema", ...}` to enforce constrained grammar masking during token sampling.
2. **System prompt enforcement**: Explicitly inject JSON schema specifications with few-shot examples.
3. **Application-level validation & repair**: Validate with `Pydantic.model_validate(json.loads(response))`. If parsing fails, catch `ValidationError` and trigger an automated retry with the schema validation error fed back into the prompt.

### Q4: Why is token calculation not simply `len(text.split())`?
**Answer**:
LLMs use subword tokenization algorithms (such as Byte-Pair Encoding / BPE, WordPiece, or SentencePiece). Words are segmented into subwords, byte fragments, and special tokens. Punctuation, whitespace, code indentation, and multilingual characters contribute varying token lengths. Accurate accounting requires a matching tokenizer (like `tiktoken` for OpenAI cl100k_base or Hugging Face tokenizers).

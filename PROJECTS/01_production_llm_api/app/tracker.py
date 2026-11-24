import time
import tiktoken
from app.config import settings
from app.schemas import TokenUsage


class MetricsTracker:
    def __init__(self):
        try:
            self.encoding = tiktoken.get_encoding("cl100k_base")
        except Exception:
            self.encoding = None

    def count_tokens(self, text: str) -> int:
        """Estimate token count using tiktoken with a heuristic fallback."""
        if not text:
            return 0
        if self.encoding:
            try:
                return len(self.encoding.encode(text))
            except Exception:
                pass
        # Fallback heuristic: roughly 4 chars per token
        return max(1, len(text) // 4)

    def calculate_cost(self, model: str, prompt_tokens: int, completion_tokens: int) -> float:
        """Calculate estimated cost in USD based on model pricing table."""
        pricing = settings.MODEL_PRICING.get(
            model,
            settings.MODEL_PRICING.get("gpt-4o-mini")
        )
        input_rate = pricing.get("input", 0.15) / 1_000_000.0
        output_rate = pricing.get("output", 0.60) / 1_000_000.0
        
        return round((prompt_tokens * input_rate) + (completion_tokens * output_rate), 6)

    def build_usage_report(self, model: str, prompt_text: str, completion_text: str) -> TokenUsage:
        prompt_tokens = self.count_tokens(prompt_text)
        completion_tokens = self.count_tokens(completion_text)
        total_tokens = prompt_tokens + completion_tokens
        cost = self.calculate_cost(model, prompt_tokens, completion_tokens)
        
        return TokenUsage(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
            estimated_cost_usd=cost
        )


tracker = MetricsTracker()

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Literal


class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant", "tool"] = "user"
    content: str
    name: Optional[str] = None


class ChatCompletionRequest(BaseModel):
    model: str = Field(default="gpt-4o-mini", description="Target LLM model identifier")
    messages: List[ChatMessage] = Field(..., description="Ordered list of conversation messages")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: Optional[int] = Field(default=1024, ge=1)
    stream: bool = Field(default=False, description="Enable Server-Sent Events (SSE) streaming")
    response_format: Optional[Dict[str, Any]] = Field(
        default=None, description="Optional JSON Schema constraint for structured outputs"
    )
    fallback_model: Optional[str] = Field(
        default=None, description="Secondary model to route to upon primary failure"
    )


class TokenUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    estimated_cost_usd: float = 0.0


class ChatCompletionChoice(BaseModel):
    index: int = 0
    message: ChatMessage
    finish_reason: Optional[str] = "stop"


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created_at: int
    model: str
    provider: str
    choices: List[ChatCompletionChoice]
    usage: TokenUsage


class ExtractionSchema(BaseModel):
    """Example structured output schema for enterprise entity extraction."""
    summary: str = Field(..., description="High-level 2-sentence summary")
    sentiment: Literal["positive", "neutral", "negative"]
    entities: List[str] = Field(default_factory=list, description="Extracted named entities")
    confidence_score: float = Field(..., ge=0.0, le=1.0)

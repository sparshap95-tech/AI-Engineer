from pydantic_settings import BaseSettings
from typing import Dict, Any


class Settings(BaseSettings):
    APP_NAME: str = "Production LLM Gateway"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    # Provider API keys (optional default fallbacks)
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    GEMINI_API_KEY: str = ""
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    
    # Resilience & Gateway configurations
    DEFAULT_MODEL: str = "gpt-4o-mini"
    FALLBACK_MODEL: str = "mock-model"
    MAX_RETRIES: int = 3
    TIMEOUT_SECONDS: float = 30.0
    
    # Pricing per 1,000,000 tokens in USD (Input / Output)
    MODEL_PRICING: Dict[str, Dict[str, float]] = {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
        "claude-3-5-sonnet": {"input": 3.00, "output": 15.00},
        "claude-3-haiku": {"input": 0.25, "output": 1.25},
        "gemini-1.5-pro": {"input": 1.25, "output": 5.00},
        "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
        "mock-model": {"input": 0.00, "output": 0.00},
    }

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()

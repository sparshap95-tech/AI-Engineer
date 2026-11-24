import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "Production LLM Gateway" in data["service"]


@pytest.mark.asyncio
async def test_models_catalog():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/v1/models")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert len(data["data"]) > 0


@pytest.mark.asyncio
async def test_chat_completion_mock():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        payload = {
            "model": "mock-model",
            "messages": [{"role": "user", "content": "Explain Transformer Self-Attention"}],
            "temperature": 0.5,
        }
        response = await client.post("/v1/chat/completions", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert len(data["choices"]) == 1
        assert "usage" in data
        assert data["usage"]["total_tokens"] > 0
        assert "X-Response-Time-MS" in response.headers


@pytest.mark.asyncio
async def test_structured_extraction():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        text = "Antigravity released a new AI agent feature that dramatically increases development velocity."
        response = await client.post("/v1/extract", params={"text": text})
        assert response.status_code == 200
        data = response.json()
        assert "summary" in data
        assert data["sentiment"] in ["positive", "neutral", "negative"]
        assert isinstance(data["entities"], list)
        assert 0.0 <= data["confidence_score"] <= 1.0

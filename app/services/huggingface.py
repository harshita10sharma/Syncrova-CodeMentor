import requests

from app.config import (
    API_URL,
    HUGGINGFACE_API_KEY,
    MODEL_NAME,
)


class HuggingFaceClient:
    """
    Client for interacting with the Hugging Face Chat Completions API.
    """

    def __init__(self):
        self.url = API_URL

        self.headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
            "Content-Type": "application/json",
        }

    def chat(
        self,
        messages: list[dict[str, str]],
        temperature: float = 0.2,
        max_tokens: int = 512,
    ) -> dict:
        """
        Send chat messages to the configured language model.
        """

        payload = {
            "model": MODEL_NAME,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            json=payload,
            timeout=120,
        )

        response.raise_for_status()

        return response.json()
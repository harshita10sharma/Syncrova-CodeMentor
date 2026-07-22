import requests

from app.config import (
    API_URL,
    HUGGINGFACE_API_KEY,
    MODEL_NAME,
)


class HuggingFaceClient:
    def __init__(self):
        self.url = API_URL

        self.headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
            "Content-Type": "application/json",
        }

    def chat(self, prompt: str):

        payload = {
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.2,
            "max_tokens": 512
        }

        response = requests.post(
            self.url,
            headers=self.headers,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        return response.json()
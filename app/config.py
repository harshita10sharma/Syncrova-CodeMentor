import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
API_URL = os.getenv("API_URL")

print("API Key Loaded:", bool(HUGGINGFACE_API_KEY))
print("Model:", MODEL_NAME)
print("API URL:", API_URL)
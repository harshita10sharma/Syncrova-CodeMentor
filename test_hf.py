from app.services.huggingface import HuggingFaceClient

client = HuggingFaceClient()

response = client.chat(
    "Say only the word Hello."
)

print(response)
from app.services.prompt_builder import PromptBuilder

messages = PromptBuilder.build_messages(
    code="""
def add(a, b):
    return a + b
""",
    language="Python",
    problem_title="Add Two Numbers"
)

print("=" * 60)
print("SYSTEM MESSAGE")
print("=" * 60)
print(messages[0]["content"][:500])   # Print first 500 chars

print("\n")

print("=" * 60)
print("USER MESSAGE")
print("=" * 60)
print(messages[1]["content"])
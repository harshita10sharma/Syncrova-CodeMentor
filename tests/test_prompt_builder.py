import unittest

from app.services.prompt_builder import PromptBuilder
from app.prompts.analyzer_prompt import SYSTEM_PROMPT


class PromptBuilderTests(unittest.TestCase):

    def test_build_system_prompt(self):
        prompt = PromptBuilder.build_system_prompt()

        self.assertEqual(prompt, SYSTEM_PROMPT)
        self.assertIsInstance(prompt, str)
        self.assertGreater(len(prompt), 0)

    def test_build_problem_section(self):
        section = PromptBuilder.build_problem_section("Two Sum")

        self.assertIn("<problem_title>", section)
        self.assertIn("Two Sum", section)
        self.assertIn("</problem_title>", section)

    def test_build_language_section(self):
        section = PromptBuilder.build_language_section("Python")

        self.assertIn("<language>", section)
        self.assertIn("Python", section)
        self.assertIn("</language>", section)

    def test_build_code_section(self):
        code = "print('Hello')"

        section = PromptBuilder.build_code_section(
            code=code,
            language="Python",
        )

        self.assertIn('<source_code language="Python">', section)
        self.assertIn(code, section)
        self.assertIn("</source_code>", section)

    def test_build_user_prompt(self):
        prompt = PromptBuilder.build_user_prompt(
            code="print('Hello')",
            language="Python",
            problem_title="Hello World",
        )

        self.assertIn("Analyze the following programming submission", prompt)
        self.assertIn("Hello World", prompt)
        self.assertIn("Python", prompt)
        self.assertIn("print('Hello')", prompt)

    def test_build_messages(self):
        messages = PromptBuilder.build_messages(
            code="print('Hello')",
            language="Python",
            problem_title="Hello World",
        )

        self.assertEqual(len(messages), 2)

        self.assertEqual(messages[0]["role"], "system")
        self.assertEqual(messages[1]["role"], "user")

        self.assertEqual(messages[0]["content"], SYSTEM_PROMPT)

        self.assertIn(
            "Analyze the following programming submission",
            messages[1]["content"],
        )


if __name__ == "__main__":
    unittest.main()
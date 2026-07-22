from app.prompts.analyzer_prompt import SYSTEM_PROMPT


class PromptBuilder:
    """
    Builds structured prompts for the AI Code Analysis Engine.

    Responsibilities:
    - Provide the system prompt.
    - Format the user's programming submission.
    - Assemble chat messages for the LLM.
    """

    @staticmethod
    def build_system_prompt() -> str:
        """
        Return the complete system prompt.
        """
        return SYSTEM_PROMPT

    @staticmethod
    def build_problem_section(problem_title: str | None) -> str:
        """
        Format the coding problem section.
        """
        title = (problem_title or "Not Provided").strip()

        return f"""<problem_title>
{title}
</problem_title>"""

    @staticmethod
    def build_language_section(language: str) -> str:
        """
        Format the programming language section.
        """
        return f"""<language>
{language.strip()}
</language>"""

    @staticmethod
    def build_code_section(code: str, language: str) -> str:
        """
        Format the submitted source code.
        """
        return f"""<source_code language="{language.strip()}">
{code.strip()}
</source_code>"""

    @classmethod
    def build_user_prompt(
        cls,
        code: str,
        language: str,
        problem_title: str | None = None,
    ) -> str:
        """
        Construct the complete user prompt.
        """

        return f"""Analyze the following programming submission according to the provided system instructions.

Submission Details

{cls.build_problem_section(problem_title)}

{cls.build_language_section(language)}

{cls.build_code_section(code, language)}

Return ONLY the JSON object defined in the system prompt.
Do not include markdown, explanations, or additional text.
"""

    @classmethod
    def build_messages(
        cls,
        code: str,
        language: str,
        problem_title: str | None = None,
    ) -> list[dict[str, str]]:
        """
        Build chat messages for the Hugging Face Chat Completions API.
        """

        return [
            {
                "role": "system",
                "content": cls.build_system_prompt(),
            },
            {
                "role": "user",
                "content": cls.build_user_prompt(
                    code=code,
                    language=language,
                    problem_title=problem_title,
                ),
            },
        ]
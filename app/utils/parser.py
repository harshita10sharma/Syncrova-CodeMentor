import json
import re


class ParserError(Exception):
    """Raised when the model response cannot be parsed."""


class ResponseParser:
    """
    Parses and validates the LLM response.
    """

    @staticmethod
    def extract_json(text: str) -> dict:
        """
        Extract JSON from the model response.

        Supports:
        - Pure JSON
        - ```json ... ```
        - Extra text surrounding JSON
        """

        text = text.strip()

        # Case 1: Pure JSON
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Case 2: Markdown code block
        markdown_match = re.search(
            r"```(?:json)?\s*(.*?)\s*```",
            text,
            re.DOTALL,
        )

        if markdown_match:
            try:
                return json.loads(markdown_match.group(1))
            except json.JSONDecodeError:
                pass

        # Case 3: Find first JSON object
        json_match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL,
        )

        if json_match:
            try:
                return json.loads(json_match.group())
            except json.JSONDecodeError:
                pass

        raise ParserError("Unable to extract valid JSON from model response.")
import json
import re
from copy import deepcopy
from typing import Any


class ParserError(Exception):
    """Raised when the model response cannot be parsed."""


class ResponseParser:
    """
    Parses and normalizes the LLM response into the schema expected by Pydantic.
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

    @staticmethod
    def parse_response(text: str) -> dict:
        """
        Extract JSON from the model response and normalize it into the stable schema.
        """

        payload = ResponseParser.extract_json(text)
        return ResponseParser.normalize(payload)

    @staticmethod
    def normalize(payload: dict) -> dict:
        """
        Normalize inconsistent LLM output into the response schema expected by Pydantic.
        """

        normalized_payload = deepcopy(payload)
        analysis = normalized_payload.get("analysis")

        if isinstance(analysis, dict):
            analysis["time_complexity"] = ResponseParser._normalize_complexity_value(
                analysis.get("time_complexity")
            )
            analysis["space_complexity"] = ResponseParser._normalize_complexity_value(
                analysis.get("space_complexity")
            )
            analysis["educational_feedback"] = ResponseParser._normalize_feedback(
                analysis.get("educational_feedback")
            )

        return normalized_payload

    @staticmethod
    def _normalize_complexity_value(value: Any) -> str:
        """
        Convert alternate complexity payloads like {current, optimized, explanation}
        into a simple string for validation.
        """

        if isinstance(value, str):
            return value.strip() or "Unknown"

        if isinstance(value, dict):
            for key in ("current", "optimized", "explanation"):
                candidate = value.get(key)
                if isinstance(candidate, str) and candidate.strip():
                    return candidate.strip()

            for candidate in value.values():
                if isinstance(candidate, str) and candidate.strip():
                    return candidate.strip()

        if value is None:
            return "Unknown"

        return str(value)

    @staticmethod
    def _normalize_feedback(value: Any) -> dict:
        """
        Convert inconsistent educational feedback payloads into the structured schema.
        """

        default_feedback = {
            "summary": "",
            "strengths": [],
            "weaknesses": [],
            "suggested_improvements": [],
            "recommended_topics": [],
            "recommended_practice": [],
            "learning_takeaways": [],
        }

        if isinstance(value, dict):
            normalized = deepcopy(default_feedback)
            normalized["summary"] = ResponseParser._coerce_text(value.get("summary"))
            normalized["strengths"] = ResponseParser._coerce_string_list(value.get("strengths"))
            normalized["weaknesses"] = ResponseParser._coerce_string_list(value.get("weaknesses"))
            normalized["suggested_improvements"] = ResponseParser._coerce_string_list(
                value.get("suggested_improvements")
            )
            normalized["recommended_topics"] = ResponseParser._coerce_string_list(
                value.get("recommended_topics")
            )
            normalized["recommended_practice"] = ResponseParser._coerce_string_list(
                value.get("recommended_practice")
            )
            normalized["learning_takeaways"] = ResponseParser._coerce_string_list(
                value.get("learning_takeaways")
            )

            if not normalized["summary"]:
                normalized["summary"] = ResponseParser._merge_text_items(
                    normalized["strengths"] + normalized["weaknesses"]
                )

            return normalized

        if isinstance(value, list):
            items = ResponseParser._coerce_string_list(value)
            return {
                "summary": ResponseParser._merge_text_items(items),
                "strengths": items,
                "weaknesses": [],
                "suggested_improvements": [],
                "recommended_topics": [],
                "recommended_practice": [],
                "learning_takeaways": [],
            }

        if isinstance(value, str):
            return {
                "summary": value.strip(),
                "strengths": [value.strip()] if value.strip() else [],
                "weaknesses": [],
                "suggested_improvements": [],
                "recommended_topics": [],
                "recommended_practice": [],
                "learning_takeaways": [],
            }

        return default_feedback

    @staticmethod
    def _coerce_text(value: Any) -> str:
        if isinstance(value, str):
            return value.strip()
        if value is None:
            return ""
        return str(value)

    @staticmethod
    def _coerce_string_list(value: Any) -> list[str]:
        if isinstance(value, list):
            return [ResponseParser._coerce_text(item) for item in value if ResponseParser._coerce_text(item)]
        if isinstance(value, tuple):
            return [ResponseParser._coerce_text(item) for item in value if ResponseParser._coerce_text(item)]
        if isinstance(value, str):
            return [value.strip()] if value.strip() else []
        return []

    @staticmethod
    def _merge_text_items(items: list[str]) -> str:
        return "; ".join(item for item in items if item)
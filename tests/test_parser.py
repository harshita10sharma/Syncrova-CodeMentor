import unittest

from app.schemas.response import AnalysisResponse
from app.utils.parser import ResponseParser


class ResponseParserNormalizationTests(unittest.TestCase):
    def test_normalizes_nested_complexity_and_feedback_payloads(self):
        raw_payload = {
            "success": True,
            "language": "python",
            "problem_title": "Two Sum",
            "overall_score": 88,
            "correctness": 90,
            "readability": 85,
            "optimization": 80,
            "code_quality": 86,
            "analysis": {
                "syntax_errors": [],
                "logical_errors": [],
                "corrected_code": "print('ok')",
                "optimized_code": "print('ok')",
                "time_complexity": {
                    "current": "O(1)",
                    "optimized": "O(1)",
                    "explanation": "Constant time lookup.",
                },
                "space_complexity": {
                    "current": "O(1)",
                    "optimized": "O(1)",
                    "explanation": "Constant extra space.",
                },
                "optimization_suggestions": ["Use a dictionary."],
                "educational_feedback": {
                    "summary": "Good structure.",
                    "strengths": ["Clear logic"],
                    "weaknesses": ["Could improve naming"],
                    "suggested_improvements": ["Use better variable names"],
                    "recommended_topics": ["Hash maps"],
                    "recommended_practice": ["Practice with examples"],
                    "learning_takeaways": ["Hash maps are efficient"],
                },
                "confidence": 0.94,
            },
        }

        normalized = ResponseParser.normalize(raw_payload)

        self.assertEqual(normalized["analysis"]["time_complexity"], "O(1)")
        self.assertEqual(normalized["analysis"]["space_complexity"], "O(1)")
        self.assertEqual(
            normalized["analysis"]["educational_feedback"]["summary"],
            "Good structure.",
        )

        validated = AnalysisResponse.model_validate(normalized)
        self.assertTrue(validated.success)

    def test_normalizes_list_feedback_into_expected_structure(self):
        raw_payload = {
            "success": True,
            "language": "python",
            "problem_title": "Two Sum",
            "overall_score": 88,
            "correctness": 90,
            "readability": 85,
            "optimization": 80,
            "code_quality": 86,
            "analysis": {
                "syntax_errors": [],
                "logical_errors": [],
                "corrected_code": "print('ok')",
                "optimized_code": "print('ok')",
                "time_complexity": "O(n)",
                "space_complexity": "O(1)",
                "optimization_suggestions": ["Use a dictionary."],
                "educational_feedback": ["Great job", "Focus on edge cases"],
                "confidence": 0.94,
            },
        }

        normalized = ResponseParser.normalize(raw_payload)

        feedback = normalized["analysis"]["educational_feedback"]
        self.assertEqual(feedback["summary"], "Great job; Focus on edge cases")
        self.assertEqual(feedback["strengths"], ["Great job", "Focus on edge cases"])

        validated = AnalysisResponse.model_validate(normalized)
        self.assertTrue(validated.success)


if __name__ == "__main__":
    unittest.main()

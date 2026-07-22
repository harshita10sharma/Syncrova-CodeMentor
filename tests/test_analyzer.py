import unittest
from unittest.mock import MagicMock, patch

from app.schemas.request import AnalysisRequest
from app.services.analyzer import AnalyzerService


class AnalyzerServiceTests(unittest.TestCase):

    @patch("app.services.analyzer.HuggingFaceClient")
    def test_analyze_success(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        mock_client.chat.return_value = {
            "choices": [
                {
                    "message": {
                        "content": """
{
  "success": true,
  "language": "Python",
  "problem_title": "Two Sum",
  "overall_score": 95,
  "correctness": 98,
  "readability": 92,
  "optimization": 90,
  "code_quality": 94,
  "analysis": {
    "syntax_errors": [],
    "logical_errors": [],
    "corrected_code": "print('ok')",
    "optimized_code": "print('ok')",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "optimization_suggestions": [],
    "educational_feedback": {
      "summary": "Excellent work.",
      "strengths": ["Readable"],
      "weaknesses": [],
      "suggested_improvements": [],
      "recommended_topics": [],
      "recommended_practice": [],
      "learning_takeaways": []
    },
    "confidence": 0.98
  }
}
"""
                    }
                }
            ]
        }

        service = AnalyzerService()

        request = AnalysisRequest(
            code="print('Hello')",
            language="Python",
            problem_title="Two Sum",
        )

        response = service.analyze(request)

        self.assertTrue(response.success)
        self.assertEqual(response.language, "Python")
        self.assertEqual(response.overall_score, 95)

        mock_client.chat.assert_called_once()

    @patch("app.services.analyzer.HuggingFaceClient")
    def test_analyze_propagates_exception(self, mock_client_class):
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        mock_client.chat.side_effect = RuntimeError("API unavailable")

        service = AnalyzerService()

        request = AnalysisRequest(
            code="print('Hello')",
            language="Python",
            problem_title="Two Sum",
        )

        with self.assertRaises(RuntimeError):
            service.analyze(request)


if __name__ == "__main__":
    unittest.main()
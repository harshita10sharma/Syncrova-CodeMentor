import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app
from app.schemas.response import (
    AnalysisData,
    AnalysisResponse,
    EducationalFeedback,
)

client = TestClient(app)


class APITests(unittest.TestCase):

    def test_health_endpoint(self):
        response = client.get("/health")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertIn("status", data)

    @patch("app.routes.analyze.AnalyzerService.analyze")
    def test_analyze_success(self, mock_analyze):

        mock_analyze.return_value = AnalysisResponse(
            success=True,
            language="Python",
            problem_title="Two Sum",
            overall_score=95,
            correctness=96,
            readability=92,
            optimization=90,
            code_quality=94,
            analysis=AnalysisData(
                syntax_errors=[],
                logical_errors=[],
                corrected_code="print('ok')",
                optimized_code="print('ok')",
                time_complexity="O(n)",
                space_complexity="O(1)",
                optimization_suggestions=[],
                educational_feedback=EducationalFeedback(
                    summary="Excellent solution.",
                    strengths=["Readable"],
                    weaknesses=[],
                    suggested_improvements=[],
                    recommended_topics=[],
                    recommended_practice=[],
                    learning_takeaways=[],
                ),
                confidence=0.98,
            ),
        )

        payload = {
            "code": "print('Hello')",
            "language": "Python",
            "problem_title": "Two Sum",
        }

        response = client.post("/analyze", json=payload)

        self.assertEqual(response.status_code, 200)

        body = response.json()

        self.assertTrue(body["success"])
        self.assertEqual(body["overall_score"], 95)
        self.assertEqual(body["language"], "Python")

    def test_analyze_invalid_request(self):

        payload = {
            "language": "Python"
        }

        response = client.post("/analyze", json=payload)

        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
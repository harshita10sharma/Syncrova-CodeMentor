from typing import List

from pydantic import BaseModel


class SyntaxErrorItem(BaseModel):
    line_number: int
    error_type: str
    severity: str
    description: str
    suggested_fix: str


class LogicalErrorItem(BaseModel):
    line_number: int
    error_type: str
    severity: str
    description: str
    suggested_fix: str


class EducationalFeedback(BaseModel):
    summary: str

    strengths: List[str]
    weaknesses: List[str]

    suggested_improvements: List[str]

    recommended_topics: List[str]
    recommended_practice: List[str]

    learning_takeaways: List[str]


class AnalysisData(BaseModel):
    syntax_errors: List[SyntaxErrorItem]
    logical_errors: List[LogicalErrorItem]

    corrected_code: str
    optimized_code: str

    time_complexity: str
    space_complexity: str

    optimization_suggestions: List[str]
    educational_feedback: EducationalFeedback

    confidence: float


class AnalysisResponse(BaseModel):
    success: bool

    language: str
    problem_title: str

    overall_score: int
    correctness: int
    readability: int
    optimization: int
    code_quality: int

    analysis: AnalysisData
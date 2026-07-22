from typing import Optional

from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    """
    Request model for AI code analysis.
    """

    code: str = Field(
        ...,
        description="Source code submitted for analysis.",
        min_length=1,
    )

    language: str = Field(
        ...,
        description="Programming language of the submitted code.",
    )

    problem_title: Optional[str] = Field(
        default=None,
        description="Optional coding problem title.",
    )
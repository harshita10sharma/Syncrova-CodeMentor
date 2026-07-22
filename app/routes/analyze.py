from fastapi import APIRouter, HTTPException

from app.schemas.request import AnalysisRequest
from app.schemas.response import AnalysisResponse
from app.services.analyzer import AnalyzerService

router = APIRouter(
    prefix="/analyze",
    tags=["Analysis"],
)

analyzer = AnalyzerService()


@router.post(
    "",
    response_model=AnalysisResponse,
)
def analyze_code(request: AnalysisRequest):
    """
    Analyze a programming submission using the AI engine.
    """

    try:
        return analyzer.analyze(request)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
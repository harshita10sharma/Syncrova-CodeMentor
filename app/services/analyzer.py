import logging

from app.schemas.request import AnalysisRequest
from app.schemas.response import AnalysisResponse
from app.services.huggingface import HuggingFaceClient
from app.services.prompt_builder import PromptBuilder
from app.utils.parser import ResponseParser

logger = logging.getLogger(__name__)


class AnalyzerService:
    """
    Orchestrates the complete code analysis workflow.

    Flow:
        Request
            ↓
        PromptBuilder
            ↓
        HuggingFaceClient
            ↓
        ResponseParser
            ↓
        AnalysisResponse
    """

    def __init__(self):
        self.client = HuggingFaceClient()

    def analyze(self, request: AnalysisRequest) -> AnalysisResponse:
        """
        Analyze the submitted source code using the LLM.
        """

        try:
            logger.info("Building prompt messages.")

            messages = PromptBuilder.build_messages(
                code=request.code,
                language=request.language,
                problem_title=request.problem_title,
            )

            logger.info("Sending request to Hugging Face model.")

            response = self.client.chat(messages)

            logger.info("Received response from Hugging Face.")

            content = response["choices"][0]["message"]["content"]

            logger.info("Parsing model response.")

            parsed_response = ResponseParser.parse_response(content)

            logger.info("Validating response schema.")

            validated_response = AnalysisResponse.model_validate(parsed_response)

            logger.info("Code analysis completed successfully.")

            return validated_response

        except Exception:
            logger.exception("AnalyzerService failed during code analysis.")
            raise
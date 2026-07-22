from app.schemas.request import AnalysisRequest
from app.schemas.response import AnalysisResponse
from app.services.huggingface import HuggingFaceClient
from app.services.prompt_builder import PromptBuilder
from app.utils.parser import ResponseParser


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

        messages = PromptBuilder.build_messages(
            code=request.code,
            language=request.language,
            problem_title=request.problem_title,
        )

        response = self.client.chat(messages)

        content = response["choices"][0]["message"]["content"]

        print("\n" + "=" * 100)
        print("LLM RESPONSE:")
        print(content)
        print("=" * 100 + "\n")

        parsed_response = ResponseParser.parse_response(content)

        return AnalysisResponse.model_validate(parsed_response)
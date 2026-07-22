"""
Central prompt assembly for the AI Code Analysis Engine.

This module assembles the complete system prompt by combining all prompt
specifications in the required execution order.
"""

from app.prompts.role import ROLE
from app.prompts.responsibilities import RESPONSIBILITIES
from app.prompts.syntax_rules import SYNTAX_RULES
from app.prompts.logical_rules import LOGICAL_RULES
from app.prompts.complexity_rules import COMPLEXITY_RULES
from app.prompts.optimization_rules import OPTIMIZATION_RULES
from app.prompts.scoring_rules import SCORING_RULES
from app.prompts.feedback_rules import FEEDBACK_RULES
from app.prompts.json_contract import JSON_CONTRACT
from app.prompts.edge_cases import EDGE_CASES
from app.prompts.quality_rules import QUALITY_RULES


PROMPT_SECTIONS = (
    ROLE,
    RESPONSIBILITIES,
    SYNTAX_RULES,
    LOGICAL_RULES,
    COMPLEXITY_RULES,
    OPTIMIZATION_RULES,
    SCORING_RULES,
    FEEDBACK_RULES,
    JSON_CONTRACT,
    EDGE_CASES,
    QUALITY_RULES,
)


def build_system_prompt() -> str:
    """
    Assemble and return the complete system prompt.
    """
    return "\n\n".join(PROMPT_SECTIONS)


SYSTEM_PROMPT = build_system_prompt()
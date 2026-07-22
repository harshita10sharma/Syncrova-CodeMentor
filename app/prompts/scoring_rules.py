SCORING_RULES = """
===============================================================================
SECTION 7 : CODE QUALITY SCORING ENGINE SPECIFICATION
===============================================================================

OVERVIEW
-------------------------------------------------------------------------------

Defines the complete behavior, methodology, evaluation criteria, scoring
algorithms, validation process, reporting standards, interpretation rules,
and quality requirements for assessing the overall quality of submitted
source code.

The Code Quality Scoring Engine is responsible for converting all previous
analysis results into objective, explainable, consistent, and reproducible
numerical scores.

Scoring must only be performed after successful completion of Syntax Analysis,
Logical Analysis, Complexity Analysis, and Optimization Analysis.

The scoring process must remain deterministic, evidence-based, language-aware,
and free from subjective judgement.

===============================================================================
7.1 PURPOSE
===============================================================================

Define the purpose and scope of the scoring engine.

===============================================================================
7.2 PRIMARY OBJECTIVES
===============================================================================

Define every objective of the scoring engine.

===============================================================================
7.3 SCORING PHILOSOPHY
===============================================================================

Define the fundamental principles governing scoring.

Examples:

• Correctness before optimization
• Objectivity
• Deterministic evaluation
• Evidence-based scoring
• Educational value
• Language awareness
• Consistency across submissions
• Fairness
• Transparency

===============================================================================
7.4 OVERALL SCORING METHODOLOGY
===============================================================================

Define how individual analysis results contribute to the final evaluation.

===============================================================================
7.5 CORRECTNESS SCORE
===============================================================================

Rules for evaluating:

• Functional correctness
• Logical correctness
• Edge case handling
• Error handling
• Algorithm reliability

===============================================================================
7.6 READABILITY SCORE
===============================================================================

Evaluate:

• Naming clarity
• Code organization
• Function decomposition
• Indentation
• Formatting
• Structural simplicity
• Documentation (when applicable)

===============================================================================
7.7 OPTIMIZATION SCORE
===============================================================================

Evaluate:

• Time efficiency
• Space efficiency
• Algorithm selection
• Data structure selection
• Resource utilization

===============================================================================
7.8 CODE QUALITY SCORE
===============================================================================

Evaluate:

• Maintainability
• Modularity
• Simplicity
• Robustness
• Scalability
• Reusability

===============================================================================
7.9 OVERALL SCORE CALCULATION
===============================================================================

Define how all individual scores are combined into a final score.

===============================================================================
7.10 SCORE WEIGHT DISTRIBUTION
===============================================================================

Define weighting strategy for:

• Correctness
• Readability
• Optimization
• Code Quality

===============================================================================
7.11 SCORE DEDUCTION RULES
===============================================================================

Define deduction criteria.

Examples:

• Syntax errors
• Logical errors
• Performance issues
• Memory inefficiency
• Poor readability
• Unsafe practices

===============================================================================
7.12 POSITIVE SCORING RULES
===============================================================================

Define situations where code earns higher scores.

Examples:

• Elegant solutions
• Efficient algorithms
• Appropriate data structures
• Clean organization
• Robust implementations

===============================================================================
7.13 SEVERITY-BASED IMPACT
===============================================================================

Define how severity levels influence score deductions.

===============================================================================
7.14 SYNTAX ERROR IMPACT
===============================================================================

Rules for adjusting scores based on syntax analysis.

===============================================================================
7.15 LOGICAL ERROR IMPACT
===============================================================================

Rules for adjusting scores based on logical correctness.

===============================================================================
7.16 COMPLEXITY IMPACT
===============================================================================

Rules for evaluating algorithmic complexity.

===============================================================================
7.17 OPTIMIZATION IMPACT
===============================================================================

Rules for evaluating optimization opportunities and implementation quality.

===============================================================================
7.18 READABILITY ASSESSMENT
===============================================================================

Detailed evaluation of readability.

===============================================================================
7.19 MAINTAINABILITY ASSESSMENT
===============================================================================

Detailed evaluation of maintainability.

===============================================================================
7.20 ROBUSTNESS ASSESSMENT
===============================================================================

Evaluate resilience against invalid inputs,
unexpected conditions,
and implementation weaknesses.

===============================================================================
7.21 SCALABILITY ASSESSMENT
===============================================================================

Evaluate whether the solution remains efficient for increasing input sizes.

===============================================================================
7.22 CONSISTENCY RULES
===============================================================================

Ensure identical code always receives identical scores.

===============================================================================
7.23 CONFIDENCE ESTIMATION
===============================================================================

Define confidence calculation for scoring decisions.

===============================================================================
7.24 SCORE VALIDATION RULES
===============================================================================

Verify every calculated score before reporting.

===============================================================================
7.25 REPORTING SPECIFICATION
===============================================================================

Define required scoring output.

Examples:

• Overall Score
• Correctness Score
• Readability Score
• Optimization Score
• Code Quality Score
• Confidence Level
• Score Summary

===============================================================================
7.26 EDUCATIONAL SCORE INTERPRETATION
===============================================================================

Explain what each score means,
why it was assigned,
and how it can be improved.

===============================================================================
7.27 MULTI-LANGUAGE SCORING RULES
===============================================================================

Ensure scoring considers language-specific idioms,
features,
best practices,
and standard libraries.

===============================================================================
7.28 EDGE CASES & EXCEPTIONS
===============================================================================

Define scoring behavior for:

• Empty submissions
• Unsupported languages
• Incomplete programs
• Ambiguous implementations
• Auto-generated code
• Trivial solutions

===============================================================================
7.29 QUALITY STANDARDS
===============================================================================

Scoring must be:

• Fair
• Accurate
• Explainable
• Reproducible
• Deterministic
• Consistent
• Language-aware
• Educational

===============================================================================
7.30 FAILURE HANDLING
===============================================================================

Define behavior when reliable scoring cannot be produced.

===============================================================================
7.31 FINAL VERIFICATION CHECKLIST
===============================================================================

Before returning scores, verify:

• Scores reflect actual analysis.
• Weighting is correctly applied.
• No unsupported assumptions are made.
• Explanations match the assigned scores.
• Scores are internally consistent.
• Results conform to the required JSON schema.
• Output is deterministic and reproducible.

"""
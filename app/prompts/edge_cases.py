EDGE_CASES = """
===============================================================================
SECTION 10 : EDGE CASE & EXCEPTION HANDLING SPECIFICATION
===============================================================================

OVERVIEW
-------------------------------------------------------------------------------

Defines the complete operational framework for handling exceptional,
ambiguous, incomplete, invalid, unsupported, or uncertain code submissions.

The Edge Case & Exception Handling Engine ensures the AI Analysis Engine
remains reliable, deterministic, transparent, and robust under all input
conditions while maintaining schema integrity and preventing unsupported
assumptions or hallucinated conclusions.

Rather than failing unexpectedly, the engine must gracefully degrade its
analysis, communicate limitations clearly, preserve confidence calibration,
and always return a valid response that conforms to the Response JSON Contract.

This specification governs every situation where normal static analysis cannot
be completed with complete certainty.

===============================================================================
10.1 PURPOSE
===============================================================================

Define the objectives, responsibilities, and operational boundaries of
exception handling throughout the analysis pipeline.

===============================================================================
10.2 PRIMARY OBJECTIVES
===============================================================================

Primary objectives include:

• Ensure reliable behavior
• Handle unexpected inputs safely
• Preserve analysis integrity
• Prevent hallucinated conclusions
• Maintain deterministic responses
• Preserve JSON compatibility
• Communicate uncertainty honestly
• Maximize useful analysis whenever possible

===============================================================================
10.3 EDGE CASE HANDLING PHILOSOPHY
===============================================================================

Core principles:

• Never fabricate analysis.
• Never guess missing information.
• Prefer partial analysis over incorrect analysis.
• Clearly communicate uncertainty.
• Preserve structural consistency.
• Fail gracefully rather than abruptly.
• Maintain educational value whenever possible.

===============================================================================
10.4 INPUT VALIDATION RULES
===============================================================================

Validate every submission before analysis.

Validation includes:

• Input existence
• File integrity
• Supported encoding
• Language detection
• Structural completeness
• Basic syntax validity

===============================================================================
10.5 EMPTY SUBMISSION HANDLING
===============================================================================

Handle submissions containing no executable source code.

Return a valid response explaining that meaningful analysis cannot be
performed.

===============================================================================
10.6 WHITESPACE-ONLY INPUT HANDLING
===============================================================================

Treat submissions containing only whitespace or formatting characters as
empty submissions.

===============================================================================
10.7 COMMENT-ONLY SOURCE CODE HANDLING
===============================================================================

Handle files containing comments without executable logic.

===============================================================================
10.8 INCOMPLETE SOURCE CODE HANDLING
===============================================================================

Examples:

• Missing braces
• Missing functions
• Truncated files
• Partial implementations
• Missing return statements

Analyze only verifiable portions.

===============================================================================
10.9 UNSUPPORTED PROGRAMMING LANGUAGE HANDLING
===============================================================================

When language support is unavailable:

• Do not attempt full analysis.
• Explain the limitation.
• Preserve response schema.

===============================================================================
10.10 MIXED-LANGUAGE SOURCE CODE HANDLING
===============================================================================

Handle files containing multiple programming languages or embedded scripts.

===============================================================================
10.11 INVALID SYNTAX HANDLING
===============================================================================

Syntax failures should not prevent every other possible analysis.

Perform partial analysis where feasible.

===============================================================================
10.12 AMBIGUOUS LOGIC HANDLING
===============================================================================

If multiple interpretations exist:

• Identify ambiguity.
• Avoid unsupported assumptions.
• Explain uncertainty.

===============================================================================
10.13 PARTIAL ANALYSIS STRATEGY
===============================================================================

When complete analysis is impossible:

• Analyze verified components.
• Skip unverifiable sections.
• Clearly document limitations.

===============================================================================
10.14 EXTREMELY LARGE SOURCE CODE HANDLING
===============================================================================

Handle unusually large submissions efficiently while maintaining response
quality.

===============================================================================
10.15 VERY SMALL SOURCE CODE HANDLING
===============================================================================

Avoid generating excessive recommendations for trivial examples.

===============================================================================
10.16 GENERATED / BOILERPLATE CODE HANDLING
===============================================================================

Recognize framework-generated or boilerplate code.

Avoid reporting standard generated patterns as user mistakes.

===============================================================================
10.17 DUPLICATE CODE DETECTION
===============================================================================

Detect duplicated logic when it meaningfully impacts maintainability.

===============================================================================
10.18 NON-TERMINATING EXECUTION PATTERN DETECTION
===============================================================================

Identify patterns suggesting:

• Infinite loops
• Infinite recursion
• Missing termination conditions

Report only when supported by evidence.

===============================================================================
10.19 UNREACHABLE CODE HANDLING
===============================================================================

Detect unreachable statements resulting from control-flow logic.

===============================================================================
10.20 MISSING CONTEXT HANDLING
===============================================================================

Handle situations where analysis depends on unavailable files,
modules, configuration, or project context.

===============================================================================
10.21 EXTERNAL DEPENDENCY HANDLING
===============================================================================

Avoid assumptions regarding external APIs, databases, services, or libraries
whose behavior cannot be verified statically.

===============================================================================
10.22 MISSING FUNCTION OR CLASS DEFINITIONS
===============================================================================

If referenced definitions are unavailable:

• Continue analyzing dependent code where possible.
• Explain resulting limitations.

===============================================================================
10.23 RUNTIME ASSUMPTION RULES
===============================================================================

Do not assume:

• Runtime values
• User input
• Database contents
• Network responses
• External API behavior
• File system state

Clearly distinguish static analysis from runtime behavior.

===============================================================================
10.24 CONFIDENCE CALIBRATION RULES
===============================================================================

Adjust confidence according to:

• Available evidence
• Completeness
• Ambiguity
• Language support
• Parsing success

Never inflate confidence.

===============================================================================
10.25 GRACEFUL DEGRADATION STRATEGY
===============================================================================

If complete analysis cannot be performed:

• Preserve valid output.
• Report verified findings.
• Document limitations.
• Maintain JSON compatibility.

===============================================================================
10.26 FAILURE RECOVERY RULES
===============================================================================

Recover whenever partial analysis remains possible.

Avoid terminating the analysis pipeline unless absolutely necessary.

===============================================================================
10.27 ERROR REPORTING STANDARDS
===============================================================================

Errors should be:

• Accurate
• Specific
• Actionable
• Evidence-based
• Educational

===============================================================================
10.28 RESPONSE JSON REQUIREMENTS
===============================================================================

Regardless of failure conditions:

• Response must remain valid JSON.
• Required fields must exist.
• Empty collections must follow schema.
• Field types must remain correct.

===============================================================================
10.29 MULTI-LANGUAGE EDGE CASES
===============================================================================

Handle language-specific constructs,
compiler directives,
macros,
templates,
annotations,
decorators,
and preprocessors appropriately.

===============================================================================
10.30 SECURITY & SAFETY CONSIDERATIONS
===============================================================================

Never execute submitted code.

Never infer secrets.

Never expose sensitive information.

Never recommend unsafe coding practices.

Treat all source code as untrusted input.

===============================================================================
10.31 RESOURCE & PERFORMANCE CONSIDERATIONS
===============================================================================

Analysis should remain efficient for both small and large submissions.

Avoid excessive processing when diminishing analytical value is expected.

===============================================================================
10.32 DATA INTEGRITY REQUIREMENTS
===============================================================================

Ensure every reported issue, score, recommendation, and explanation remains
consistent with the available evidence.

No contradictions should exist within the response.

===============================================================================
10.33 QUALITY STANDARDS
===============================================================================

Exception handling must be:

• Reliable
• Predictable
• Deterministic
• Transparent
• Robust
• Explainable
• Evidence-based
• Production-ready

===============================================================================
10.34 FINAL VERIFICATION CHECKLIST
===============================================================================

Before returning the response, verify:

• Input was validated.
• Unsupported assumptions were avoided.
• Confidence matches available evidence.
• Limitations are clearly communicated.
• Partial analysis is clearly identified.
• JSON schema remains valid.
• Required fields are present.
• No hallucinated findings exist.
• Error reporting is actionable.
• Response remains deterministic.

"""
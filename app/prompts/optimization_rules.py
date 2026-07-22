OPTIMIZATION_RULES = """
===============================================================================
SECTION 6 : CODE OPTIMIZATION ENGINE SPECIFICATION
===============================================================================

OVERVIEW
-------------------------------------------------------------------------------

Defines the complete behavior, responsibilities, optimization methodology,
decision-making process, validation rules, reporting standards, optimized code
generation strategy, educational explanations, and quality requirements for
code optimization.

The Code Optimization Engine is responsible for identifying opportunities to
improve the performance, efficiency, readability, maintainability, and
resource utilization of the submitted program without altering its intended
behavior.

Optimization analysis must only be performed after successful syntax,
logical, and complexity analysis.

The engine must recommend improvements only when they provide measurable or
meaningful benefits.

===============================================================================
6.1 PURPOSE
===============================================================================

Define the purpose and scope of optimization analysis.

===============================================================================
6.2 PRIMARY OBJECTIVES
===============================================================================

Define every objective of the Code Optimization Engine.

===============================================================================
6.3 OPTIMIZATION PRINCIPLES
===============================================================================

Core principles governing optimization.

Examples:

• Correctness before optimization
• Preserve program behavior
• Evidence-based optimization
• Readability preservation
• Minimal necessary modifications
• Deterministic recommendations
• No speculative improvements
• Language-aware optimization
• Educational explanations

===============================================================================
6.4 SCOPE OF OPTIMIZATION ANALYSIS
===============================================================================

Define every aspect of the program eligible for optimization.

Include:

• Algorithms
• Data structures
• Loops
• Recursion
• Function calls
• Memory allocation
• Object creation
• Variable usage
• Expressions
• Conditional statements
• Input/Output operations
• Library usage
• Built-in functions
• Exception handling
• Collections
• String operations
• Mathematical computations

===============================================================================
6.5 OPTIMIZATION DETECTION STRATEGY
===============================================================================

Define the complete process used to identify optimization opportunities.

===============================================================================
6.6 ALGORITHM OPTIMIZATION
===============================================================================

Rules for identifying inefficient algorithms and suggesting better alternatives.

===============================================================================
6.7 DATA STRUCTURE OPTIMIZATION
===============================================================================

Rules for selecting more appropriate data structures.

===============================================================================
6.8 TIME COMPLEXITY OPTIMIZATION
===============================================================================

Rules for reducing computational complexity.

===============================================================================
6.9 SPACE COMPLEXITY OPTIMIZATION
===============================================================================

Rules for minimizing auxiliary memory usage.

===============================================================================
6.10 LOOP OPTIMIZATION
===============================================================================

Optimization of:

• Nested loops
• Redundant iterations
• Early termination
• Loop fusion
• Loop invariant code motion
• Unnecessary traversals

===============================================================================
6.11 RECURSION OPTIMIZATION
===============================================================================

Rules for:

• Tail recursion
• Recursion elimination
• Memoization opportunities
• Stack usage reduction

===============================================================================
6.12 MEMORY OPTIMIZATION
===============================================================================

Rules for improving memory efficiency.

===============================================================================
6.13 REDUNDANT COMPUTATION ELIMINATION
===============================================================================

Detect:

• Duplicate calculations
• Repeated function calls
• Constant recomputation
• Unnecessary conversions

===============================================================================
6.14 STANDARD LIBRARY & BUILT-IN FUNCTION OPTIMIZATION
===============================================================================

Identify opportunities to replace custom implementations with efficient,
well-tested standard library features.

===============================================================================
6.15 CODE SIMPLIFICATION
===============================================================================

Rules for simplifying logic while preserving behavior.

===============================================================================
6.16 READABILITY & MAINTAINABILITY OPTIMIZATION
===============================================================================

Recommend improvements that increase clarity without changing functionality.

===============================================================================
6.17 PERFORMANCE BOTTLENECK IDENTIFICATION
===============================================================================

Identify sections of code responsible for the greatest performance cost.

===============================================================================
6.18 OPTIMIZATION VALIDATION RULES
===============================================================================

Verify that every optimization:

• Preserves correctness
• Preserves output
• Improves efficiency
• Introduces no regressions
• Is supported by objective analysis

===============================================================================
6.19 OPTIMIZED CODE GENERATION RULES
===============================================================================

Rules for generating optimized implementations.

Specify:

• Preserve functionality
• Preserve external behavior
• Preserve public interfaces
• Avoid unnecessary refactoring
• Maintain readability
• Maintain language idioms

===============================================================================
6.20 REPORTING SPECIFICATION
===============================================================================

Define required reporting fields.

Examples:

• Current Complexity
• Optimized Complexity
• Optimization Type
• Performance Benefit
• Memory Benefit
• Explanation
• Optimized Code
• Confidence Level

===============================================================================
6.21 EDUCATIONAL EXPLANATION RULES
===============================================================================

Explain:

• Why the current implementation is inefficient
• Why the suggested approach is better
• Expected performance improvement
• Trade-offs
• Learning takeaway

===============================================================================
6.22 CASES WHERE OPTIMIZATION SHOULD NOT BE SUGGESTED
===============================================================================

Examples:

• Already optimal implementations
• Negligible improvements
• Readability loss outweighs benefit
• Language-specific best practices already followed
• Premature optimization
• Unsupported assumptions

===============================================================================
6.23 MULTI-LANGUAGE OPTIMIZATION RULES
===============================================================================

Apply optimization according to language-specific features,
standard libraries, idioms, and performance characteristics.

===============================================================================
6.24 QUALITY STANDARDS
===============================================================================

Optimization analysis must be:

• Correct
• Safe
• Explainable
• Measurable
• Language-aware
• Educational
• Maintainable
• Deterministic

===============================================================================
6.25 FAILURE HANDLING
===============================================================================

Define behavior when optimization cannot be performed due to:

• Incomplete code
• Unsupported language
• Ambiguous implementation
• Missing context
• Invalid input

===============================================================================
6.26 FINAL VERIFICATION CHECKLIST
===============================================================================

Before returning optimization results, verify:

• Original behavior is preserved.
• Suggested optimization is genuinely beneficial.
• Complexity estimates are accurate.
• Optimized code compiles conceptually.
• No logical errors are introduced.
• No unnecessary modifications are made.
• Every recommendation is evidence-based.
• Output conforms to the required JSON contract.

"""
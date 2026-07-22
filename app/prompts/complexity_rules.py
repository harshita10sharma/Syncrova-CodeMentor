COMPLEXITY_RULES = """
===============================================================================
SECTION 5 : COMPLEXITY ANALYSIS ENGINE SPECIFICATION
===============================================================================

OVERVIEW

Defines the complete behavior, responsibilities, decision-making process,
analysis methodology, validation rules, reporting standards, educational
explanations, and quality requirements for algorithmic complexity analysis.

The Complexity Analysis Engine is responsible for estimating, validating,
explaining, and reporting the computational complexity of the submitted
program.

Complexity analysis must be performed only after successful syntax and logical
analysis to ensure the program being evaluated is syntactically valid and
logically meaningful.

The engine must analyze both Time Complexity and Space Complexity using
accepted algorithm analysis principles.

===============================================================================
5.1 PURPOSE
===============================================================================

Define the purpose of complexity analysis.

===============================================================================
5.2 PRIMARY OBJECTIVES
===============================================================================

Define every objective of the Complexity Analysis Engine.

===============================================================================
5.3 ANALYSIS PRINCIPLES
===============================================================================

Define the principles governing complexity analysis.

Examples:

• Accuracy
• Determinism
• Evidence-based analysis
• Language awareness
• Educational explanations
• No hallucinations
• Conservative estimation

===============================================================================
5.4 SCOPE OF COMPLEXITY ANALYSIS
===============================================================================

Define every program construct that contributes to computational complexity.

Include:

• Sequential execution
• Conditional statements
• Loops
• Nested loops
• Recursion
• Mutual recursion
• Function calls
• Data structure operations
• Built-in library functions
• Sorting algorithms
• Searching algorithms
• Dynamic programming
• Graph algorithms
• Tree traversals
• Backtracking
• Divide and conquer
• Greedy algorithms
• Hashing
• Memory allocation
• Object creation

===============================================================================
5.5 TIME COMPLEXITY ANALYSIS
===============================================================================

Rules for estimating asymptotic runtime.

===============================================================================
5.6 SPACE COMPLEXITY ANALYSIS
===============================================================================

Rules for estimating auxiliary memory usage.

===============================================================================
5.7 COMPLEXITY ESTIMATION STRATEGY
===============================================================================

Define the complete reasoning process used to derive complexity.

===============================================================================
5.8 COMMON TIME COMPLEXITY PATTERNS
===============================================================================

Recognition rules for:

O(1)

O(log n)

O(n)

O(n log n)

O(n²)

O(n³)

O(2ⁿ)

O(n!)

and other common patterns.

===============================================================================
5.9 COMMON SPACE COMPLEXITY PATTERNS
===============================================================================

Recognition rules for:

Constant

Linear

Quadratic

Recursive stack

Auxiliary structures

===============================================================================
5.10 LOOP ANALYSIS
===============================================================================

Rules for:

• Single loops
• Nested loops
• Dependent loops
• Independent loops
• Early termination
• Variable increments
• Infinite loops

===============================================================================
5.11 RECURSION ANALYSIS
===============================================================================

Rules for:

• Base cases
• Recursive depth
• Tail recursion
• Divide and conquer
• Recursive stack usage

===============================================================================
5.12 DATA STRUCTURE COMPLEXITY
===============================================================================

Complexity rules for common data structures.

Examples:

Arrays

Linked Lists

Stacks

Queues

Hash Maps

Hash Sets

Trees

Heaps

Graphs

Priority Queues

===============================================================================
5.13 STANDARD LIBRARY COMPLEXITY
===============================================================================

Consider complexity of built-in language APIs and library functions.

===============================================================================
5.14 BEST, AVERAGE AND WORST CASE ANALYSIS
===============================================================================

Estimate and explain applicable complexity cases.

===============================================================================
5.15 COMPLEXITY VALIDATION RULES
===============================================================================

Define how estimated complexity must be verified before reporting.

===============================================================================
5.16 REPORTING SPECIFICATION
===============================================================================

Define required reporting fields.

Examples:

• Current Time Complexity
• Current Space Complexity
• Supporting Explanation
• Dominant Operations
• Performance Bottlenecks
• Confidence Level

===============================================================================
5.17 EDUCATIONAL EXPLANATION RULES
===============================================================================

Explain why the reported complexity was assigned.

Use beginner-friendly language while remaining technically correct.

===============================================================================
5.18 LIMITATIONS
===============================================================================

Define situations where exact complexity cannot be confidently determined.

===============================================================================
5.19 QUALITY STANDARDS
===============================================================================

Complexity analysis must be:

• Accurate
• Explainable
• Deterministic
• Evidence-based
• Language-aware
• Educational
• Consistent

===============================================================================
5.20 FINAL VERIFICATION CHECKLIST
===============================================================================

Before reporting complexity, verify:

• Time complexity is correct.
• Space complexity is correct.
• Dominant operations are identified.
• Explanations match the implementation.
• No unsupported assumptions are made.
• Results are consistent with the analyzed code.

"""
LOGICAL_RULES = """
===============================================================================
SECTION 4 : LOGICAL ANALYSIS ENGINE SPECIFICATION
===============================================================================

OVERVIEW
-------------------------------------------------------------------------------

The Logical Analysis Engine is responsible for determining whether the submitted
program correctly solves the intended problem according to its expected
behavior.

Unlike Syntax Analysis, which validates grammatical correctness, Logical
Analysis evaluates algorithmic correctness, program behavior, decision-making,
execution flow, correctness under different inputs, and the reliability of the
overall implementation.

A program may be syntactically valid while still producing incorrect results.
Therefore, logical analysis must always be performed after successful syntax
analysis.

The objective of this engine is to identify genuine logical defects without
making assumptions about the programmer's intent beyond what can reasonably be
inferred from the submitted implementation.

The Logical Analysis Engine must never fabricate logical errors, optimization
opportunities, or problem requirements.

Only report issues that can be justified through objective analysis of the
submitted code.

===============================================================================
4.1 PURPOSE
===============================================================================

The purpose of the Logical Analysis Engine is to verify that the submitted
program behaves correctly for its intended task.

Logical analysis must evaluate whether:

• The algorithm solves the problem correctly.
• The implementation follows the intended logic.
• The execution flow is correct.
• The output is reliable.
• Boundary conditions are handled correctly.
• Exceptional situations are handled safely.
• The implementation remains correct under different valid inputs.

===============================================================================
4.2 PRIMARY OBJECTIVES
===============================================================================

The Logical Analysis Engine must:

1. Detect genuine logical errors.

2. Avoid false positive reports.

3. Validate algorithm correctness.

4. Validate control flow.

5. Validate decision making.

6. Validate recursion and iteration logic.

7. Validate edge case handling.

8. Validate data structure usage.

9. Validate variable updates.

10. Validate return values.

11. Explain every detected logical issue.

12. Suggest the minimal correction required.

13. Preserve the intended behavior while generating corrected code.

14. Never modify the algorithm unless required to fix an actual logical defect.

===============================================================================
4.3 ANALYSIS PRINCIPLES
===============================================================================

Logical analysis must follow these principles:

• Accuracy over assumptions.

• Evidence-based reasoning.

• No hallucinated errors.

• No speculative conclusions.

• Language-independent reasoning whenever possible.

• Educational explanations.

• Minimal corrective changes.

• Consistent evaluation.

• Deterministic reporting.

===============================================================================
4.4 SCOPE OF ANALYSIS
===============================================================================

The Logical Analysis Engine must inspect every executable component of the
program, including but not limited to:

• Variable initialization
• Variable updates
• Arithmetic operations
• Boolean expressions
• Conditional statements
• Loop conditions
• Loop termination
• Function calls
• Function return values
• Recursive calls
• Base cases
• Data structure operations
• Input handling
• Output generation
• State changes
• Exception handling
• Resource management
• Boundary conditions
• Error handling
• Program termination

Every logical construct should be evaluated according to the intended behavior
of the submitted implementation.

===============================================================================
4.5 DETECTION STRATEGY
===============================================================================

Before reporting any logical error, the AI must:

1. Understand the objective of the code.

2. Analyze the execution flow.

3. Trace the algorithm.

4. Evaluate expected outputs.

5. Consider common edge cases.

6. Verify whether the detected issue genuinely affects correctness.

Never report speculative logical issues.

Only report issues that are supported by objective analysis.

...
"""
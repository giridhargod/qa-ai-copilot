from crewai import Task
from agents import screen_analyzer, pii_detector, test_case_generator, report_generator


def create_tasks(screen_data):

    # 1. Screen Analysis
    analyze_screen_task = Task(
        description=f"""
You are a UI Analysis Expert.

Analyze the following structured UI field data:

{screen_data}

Instructions:
- Identify all fields
- Determine field type (text, password, hidden, email, etc.)
- Define clear purpose for each field

STRICT OUTPUT FORMAT:

| Field Name | Type | Purpose |

Only return table. No explanations.
        """,
        agent=screen_analyzer,
        expected_output="Table of fields with name, type and purpose"
    )


    # 2. PII Detection
    pii_detection_task = Task(
        description="""
You are a Senior Data Privacy Analyst.

Identify PII from the given field data.

Rules:
- Only detect REAL values (no guessing)
- Avoid false positives
- Match correct risk levels

OUTPUT FORMAT:

| ID | Field Name | Detected Value | PII Type | Risk Level | Reason |

If none:
No PII detected.
        """,
        agent=pii_detector,
        expected_output="Table of detected PII",
        context=[analyze_screen_task]
    )


    # 3. Test Case Generation
    test_case_task = Task(
        description="""
You are a Senior QA Engineer.

Generate REAL-WORLD test cases.

Cover:
- Positive
- Negative
- Edge
- Boundary
- Security

STRICT FORMAT:

| Test Case ID | Title | Preconditions | Step Number | Action | Expected Result | Impacted Components | Test Type | Priority |

Rules:
- Step 0 = Preconditions
- Each step must have expected result
- No generic cases
- No hallucination

Focus:
- Field validation
- UI behavior
- PII security
- Error handling
        """,
        agent=test_case_generator,
        expected_output="Excel formatted test cases",
        context=[analyze_screen_task, pii_detection_task]
    )


    # 4. Final Report
    report_task = Task(
        description="""
Generate FINAL QA REPORT.

Include:
1. Field Summary
2. PII Risks
3. Test Coverage Summary

Keep it structured and readable.
        """,
        agent=report_generator,
        expected_output="Final QA report",
        context=[analyze_screen_task, pii_detection_task, test_case_task]
    )


    return [
        analyze_screen_task,
        pii_detection_task,
        test_case_task,
        report_task
    ]
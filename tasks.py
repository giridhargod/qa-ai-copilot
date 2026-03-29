<<<<<<< HEAD
from crewai import Task
from agents import ui_agent, pii_agent, testcase_agent, critic_agent


def create_tasks(user_input):

    # 1. UI Analysis Task
    ui_task = Task(
        description=f"""
        Analyze the following application screen or flow:

        INPUT:
        {user_input}

        Your job:
        - Identify all UI elements (fields, buttons, dropdowns, links)
        - Understand the user journey across screens if it's a flow
        - Detect validations (mandatory fields, formats, constraints)
        - Identify possible user actions and transitions

        Think like a QA:
        - Include edge cases
        - Include negative scenarios
        - Consider multi-step flows

        Output should be structured and detailed.
        """,
        expected_output="Detailed UI analysis including fields, flows, validations, and user interactions.",
        agent=ui_agent
    )

    # 2. PII Detection Task
    pii_task = Task(
        description="""
        Based on the UI analysis, identify any Personally Identifiable Information (PII).

        Your job:
        - Detect sensitive fields (Name, Email, Phone, SSN, etc.)
        - Classify data as:
            - PII
            - Sensitive PII
            - Non-sensitive data
        - Highlight potential risks in handling this data
        - Suggest masking, encryption, and access control strategies

        Think from a security + compliance perspective.
        """,
        expected_output="List of PII fields, risk analysis, and recommendations for data protection.",
        agent=pii_agent
    )

    # 3. Test Case Generation Task
    testcase_task = Task(
        description="""
        Generate high-quality test cases based on the UI analysis.

        Your job:
        - Create functional test cases
        - Include:
            - Positive scenarios
            - Negative scenarios
            - Edge cases
        - Cover validation logic
        - Cover multi-screen workflows

        Format:
        - Test Case ID
        - Description
        - Steps
        - Expected Result

        Focus on real-world QA coverage.
        """,
        expected_output="Structured test cases covering functional, negative, and edge scenarios.",
        agent=testcase_agent
    )

    # 4. Critic Task (VERY IMPORTANT 🔥)
    critic_task = Task(
        description="""
        Review all outputs from previous agents.

        Your job:
        - Identify missing test cases
        - Detect weak coverage areas
        - Challenge assumptions
        - Improve test quality
        - Suggest additional edge cases and risks

        Think like a senior QA reviewer.

        Be critical. Be strict. Improve quality.
        """,
        expected_output="Improved and refined test cases with additional coverage and insights.",
        agent=critic_agent
    )

    return [ui_task, pii_task, testcase_task, critic_task]
=======
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
>>>>>>> 6d8a0dc814e2c01133b4c3bd0c921f1b960dd5cc

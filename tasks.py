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
from scraper import extract_fields_from_url
from crewai import Task
from agents import screen_analyzer, pii_detector, test_case_generator, report_generator

url = "https://demoqa.com/text-box"

fields = extract_fields_from_url(url)

screen_data = fields

analyze_screen_task = Task(
    description=f"""You are a QA expert. Given the following UI fields: {screen_data} 
    Generate:
    1. Positive test cases
    2. Negative test cases
    3. Edge cases
    4. Validation scenarios
    Return in structured format with:
    -Test case ID
    - Title
    - Steps
    - Expected result
    """,
    agent=screen_analyzer,
    expected_output="A list of test cases for each field"
)

pii_detection_task = Task(
    description="Identify which of the fields contain PII such as name, email, phone, address, card_number",
    agent=pii_detector,
    expected_output="List of PII fields"
)

test_case_task = Task(
    description="Generate QA test cases for the identified fields",
    agent=test_case_generator,
    expected_output="QA test cases for each field"
)

report_task = Task(
    description="Generate a final QA compliance report based on the analysis",
    agent=report_generator,
    expected_output="Structured QA compliance report"
)
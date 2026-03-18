from crewai import Agent
from langchain_openai import ChatOpenAI

# Create the AI model
llm = ChatOpenAI(model="gpt-4o-mini")

# Agent 1 - Screen Analyzer
screen_analyzer = Agent(
    role="UI Screen Analyzer",
    goal="Analyze application screens and identify input fields",
    backstory="Expert QA engineer who understands UI structures",
    llm=llm,
    verbose=True
)

# Agent 2 - PII Detector
pii_detector = Agent(
    role="PII Detection Specialist",
    goal="Detect personally identifiable information fields",
    backstory="Security expert focused on privacy compliance",
    llm=llm,
    verbose=True
)

# Agent 3 - Test Case Generator
test_case_generator = Agent(
    role="QA Test Designer",
    goal="Generate test cases for identified fields",
    backstory="Senior QA automation engineer",
    llm=llm,
    verbose=True
)

# Agent 4 - QA Report Generator
report_generator = Agent(
    role="QA Reporting Specialist",
    goal="Generate a final QA analysis report",
    backstory="QA lead responsible for compliance reports",
    llm=llm,
    verbose=True
)
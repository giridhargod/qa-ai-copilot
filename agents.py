<<<<<<< HEAD
from crewai import Agent
from langchain_openai import ChatOpenAI
import os

# Initialize LLM properly
llm = "gpt-4o-mini"
api_key=os.getenv("OPENAI_API_KEY")

# Agent 1: UI Analyzer
ui_agent = Agent(
    role="Senior UI/UX QA Analyst",
    goal="Analyze user interface flows and identify all possible UI elements, validations, and user interaction paths",
    backstory=(
        "An experienced QA analyst specializing in breaking down complex UI flows into structured testable components. "
        "Expert in identifying edge cases, missing validations, and usability issues."
    ),
    llm=llm,
    verbose=True
)

# Agent 2: PII Detector
pii_agent = Agent(
    role="Data Privacy & Security QA Expert",
    goal="Identify sensitive data (PII) and ensure proper handling, masking, and protection",
    backstory=(
        "A security-focused QA engineer with deep expertise in data privacy regulations and PII protection. "
        "Specializes in identifying leaks, unsafe handling, and compliance gaps."
    ),
    llm=llm,
    verbose=True
)

# Agent 3: Test Case Generator
testcase_agent = Agent(
    role="Senior QA Test Architect",
    goal="Generate comprehensive, structured, and high-quality test cases",
    backstory=(
        "A QA architect with years of experience designing test strategies for large-scale systems. "
        "Expert in functional, edge-case, and negative test scenarios."
    ),
    llm=llm,
    verbose=True
)

# Agent 4: QA Critic / Reviewer
critic_agent = Agent(
    role="QA Review Specialist",
    goal="Review and improve generated test cases for completeness, accuracy, and quality",
    backstory=(
        "A highly detail-oriented QA reviewer known for catching gaps in testing strategies and improving coverage. "
        "Ensures production-level quality in test design."
    ),
    llm=llm,
    verbose=True
=======
from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

#Load environment variables
load_dotenv()

#Get API Key
api_key=os.getenv("OPENAI_API_KEY")

#Validate API Key
if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=api_key
)

# Agent 1: Screen Analyzer
screen_analyzer = Agent(
    role="UI Screen Analyzer",
    goal="Analyze UI fields and extract structured information",
    backstory="Expert QA engineer skilled in understanding UI structures",
    llm=llm,
    verbose=True
)

# Agent 2: PII Detector
pii_detector = Agent(
    role="PII Detection Specialist",
    goal="Identify sensitive personal data accurately",
    backstory="Data privacy expert ensuring compliance and security",
    llm=llm,
    verbose=True
)

# Agent 3: Test Case Generator
test_case_generator = Agent(
    role="Senior QA Test Designer",
    goal="Generate high-quality, structured test cases",
    backstory="Experienced QA engineer specializing in manual and edge case testing",
    llm=llm,
    verbose=True
)

# Agent 4: Report Generator
report_generator = Agent(
    role="QA Report Generator",
    goal="Compile structured QA reports",
    backstory="QA lead experienced in summarizing test coverage and risks",
    llm=llm,
    verbose=True
>>>>>>> 6d8a0dc814e2c01133b4c3bd0c921f1b960dd5cc
)
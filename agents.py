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
)
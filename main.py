from dotenv import load_dotenv
import json

from crewai import Crew
from scraper import extract_fields_from_url
from tasks import create_tasks
from agents import screen_analyzer, pii_detector, test_case_generator, report_generator

# Load environment variables
load_dotenv()

# Input URL
url = input("Enter URL: ")

# Extract fields
fields = extract_fields_from_url(url)

# Convert to JSON string (IMPORTANT)
screen_data = json.dumps(fields, indent=2)

# Create tasks
tasks = create_tasks(screen_data)

# Create Crew
crew = Crew(
    agents=[screen_analyzer, pii_detector, test_case_generator, report_generator],
    tasks=tasks,
    verbose=True
)

# Run
result = crew.kickoff()

print("\n\n===== FINAL OUTPUT =====\n")
print(result)
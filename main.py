from dotenv import load_dotenv
import os
load_dotenv()
print("API KEY LOADED:","YES" if os.getenv("OPENAI_API_KEY") else "NO")
from crewai import Crew
from agents import screen_analyzer, pii_detector, test_case_generator, report_generator
from tasks import analyze_screen_task, pii_detection_task, test_case_task, report_task

crew = Crew(
    agents=[
        screen_analyzer,
        pii_detector,
        test_case_generator,
        report_generator
    ],
    tasks=[
        analyze_screen_task,
        pii_detection_task,
        test_case_task,
        report_task
    ],
    verbose=True
)

result = crew.kickoff()

print("\n\nFINAL RESULT:\n")
print(result)
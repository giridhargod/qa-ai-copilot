from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from tasks import create_tasks


def run(user_input):  # 👈 accept input as parameter

    tasks = create_tasks(user_input)

    crew = Crew(
        agents=[task.agent for task in tasks],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    return result  # 👈 return instead of print


if __name__ == "__main__":
    user_input = input("Enter URL or screen description: ")
    output = run(user_input)

    print("\n========== FINAL OUTPUT ==========\n")
    print(output)
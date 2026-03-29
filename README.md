QA AI Copilot
**Built as a real-world QA automation simulation using AI agents**
An AI-powered QA automation assistant that analyzes UI screens, detects PII risks, and generates structured, Excel-ready test cases — simulating real-world QA engineering practices.

Overview - 
Manual test case creation is time-consuming and often inconsistent.
QA AI Copilot solves this by:
Understanding UI fields from a live webpage
Identifying sensitive (PII) data
Generating high-quality test cases automatically
Producing a structured QA report

Key Features
1. UI Field Analysis - Extracts and structures form fields (email, password, etc.)
2. PII Detection & Risk Classification - Identifies sensitive data and assigns:
- High Risk (Financial / IDs)
- Medium Risk (Email / Phone)
- Low Risk (Indirect data)
3. Automated Test Case Generation - Generates:
Positive scenarios
Negative scenarios
Edge cases
Boundary tests
Security validations
4. Excel-Compatible Output - Test cases are formatted in clean tabular structure for easy export
5. End-to-End QA Report - Includes:
- Field summary
- PII risks
- Test coverage analysis

Architecture - This project uses a multi-agent AI pipeline powered by CrewAI:
User Input (URL) -> Scraper (Extract UI Fields) -> Screen Analyzer Agent -> PII Detection Agent -> Test Case Generator Agent -> Report Generator Agent -> Final QA Report

Tech Stack - 
1. Python
2. CrewAI (multi-agent orchestration)
3. LangChain OpenAI
4. BeautifulSoup (web scraping)
5. dotenv (environment management)

Project Structure - 
qa-ai-copilot -
agents.py - AI agents (roles & behavior)
tasks.py - Task chaining & prompts
scraper.py - Extract UI elements from URL
main.py - Entry point
screens.json - Sample extracted data (optional)
.env - API key (not committed)
.gitignore
README.md

How to Run
1. Clone Repository - git clone https://github.com/giridhargod/qa-ai-copilot.git cd qa-ai-copilot
2. Install Dependencies - pip install -r requirements.txt
3. Setup Environment Variables - Create a .env file:
OPENAI_API_KEY=your_api_key
4. Run the Application - python main.py
Enter a URL when prompted: https://example.com/login

Sample Output - The system generates:
- Structured Field Summary
- PII Risk Table
- Excel-style testcases
- Test Coverage Summary

Example Use Cases - 
QA Engineers → Faster test case creation
Startups → Quick validation of forms
Security Testing → Detect PII exposure risks
Automation Teams → Pre-test design assistance

Future Enhancements - 
- Export test cases to Excel (.xlsx)
- UI dashboard
- Integration with test management tools
- Screenshot-based analysis (OCR)
- AI-based bug prediction

What This Project Demonstrates?
- Real-world QA thinking
- AI-driven automation workflows
- Prompt engineering for structured outputs
- Data privacy awareness (PII detection)
- Multi-agent system design

Author
Giridhar B

If you like this project
Give it a ⭐ on GitHub and feel free to contribute!

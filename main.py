from crewai import Agent, Task, Crew
from gemini_llm import GeminiLLM
import os
# Create Gemini instance
folder_path = "resumes"
resumes = []
for file_name in os.listdir(folder_path):
    with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as f:
        resumes.append(f.read())

# Join into single string
resume_text = "\n\n".join(resumes)

llm = GeminiLLM(api_key="Your Key")

# ----------------------
# Define agents
# ----------------------

screener = Agent(
    role='Screener',
    goal='Filter out resumes that do not meet basic criteria like education and experience.',
    backstory='A recruitment specialist who knows the must-have minimums for this role.',
    llm=llm
)

analyzer = Agent(
    role='Analyzer',
    goal='Analyze resumes for required skills, keywords and project relevance.',
    backstory='An expert who can pick up hidden strengths in a resume.',
    llm=llm
)

summarizer = Agent(
    role='Summarizer',
    goal='Create a short professional summary of each candidate.',
    backstory='A content expert who crafts precise summaries.',
    llm=llm
)

decision_maker = Agent(
    role='Decision Maker',
    goal='Decide if a resume should be shortlisted based on screening, analysis and summary.',
    backstory='A hiring manager with years of experience picking the right talent.',
    llm=llm
)

# ----------------------
# Define tasks
# ----------------------

task_screen = Task(
    description=f"""
Below is a list of candidate resumes. 
Filter them based on:
- Must have a Computer Science degree
- Must have at least 2 years of experience

Return ONLY the shortlisted candidates in this format:

Shortlisted Candidates:
- Name (e.g., John Mathew)

Here are the resumes:
{resume_text}
""",
    agent=screener,
    expected_output='A bullet list of shortlisted candidate names.'
)



task_analyze = Task(
    description='Analyze the filtered resumes for key skills, relevant projects, certifications and keywords.',
    agent=analyzer,
    expected_output='Detailed notes on skills and strengths of each resume.'
)

task_summarize = Task(
    description='Create a 50-75 word professional summary for each candidate based on analysis.',
    agent=summarizer,
    expected_output='Short professional summaries.'
)

task_decide = Task(
    description='Based on screening, analysis and summaries, decide to shortlist or reject each candidate.',
    agent=decision_maker,
    expected_output='A final decision list marking resumes as Shortlisted or Rejected.'
)

# ----------------------
# Create crew and kickoff
# ----------------------

crew = Crew(
    agents=[screener, analyzer, summarizer, decision_maker],
    tasks=[task_screen, task_analyze, task_summarize, task_decide]
)

result = crew.kickoff()
print(result)

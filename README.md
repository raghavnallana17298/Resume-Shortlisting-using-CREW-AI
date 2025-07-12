# Resume-Shortlisting-using-CREW-AI

This project implements a multi-agent AI pipeline for automated resume shortlisting.
It uses CrewAI to orchestrate multiple agents, each with a specialized role, and integrates Gemini LLM (via Google’s Generative Language API) to analyze and process resumes intelligently.

# 💼 What it does
✅ Loads resumes (plain text files) from a resumes/ folder.
✅ Passes them through multiple AI agents:

Screener: Filters resumes by required degree & experience.

Analyzer: Extracts skills, projects, certifications.

Summarizer: Creates short professional summaries.

Decision Maker: Decides to shortlist or reject.

✅ Outputs a final list of shortlisted candidates.

# 🔍 Project structure
bash
Copy
Edit
.
├── main.py           # Main script that runs multi-agent pipeline
├── gemini_llm.py     # Custom wrapper for Gemini LLM API
├── resumes/          # Folder containing plain text resumes
│   ├── resume1.txt
│   ├── resume2.txt
│   └── ...
├── requirements.txt
└── README.md



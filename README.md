# 🎓 ScholarAgent: The AI Exam Concierge

![Status](https://img.shields.io/badge/Status-Capstone_Submission-success)
![Track](https://img.shields.io/badge/Track-Concierge_Agents-blue)
![Tech](https://img.shields.io/badge/Powered_by-Google_Gemini-orange)

> **A Multi-Agent System designed to help engineering students organize, study, and master their local course material.**

---

## 1. 💡 The Pitch

### The Problem
Engineering students (myself included) often spend 30% of their study time just "managing context", organizing PDFs, searching through syllabus files, and figuring out *what* to study, rather than actually learning. Generic LLMs are helpful, but they hallucinate curriculum details because they lack access to our specific local course files.

### The Solution
**ScholarAgent** is a proactive academic concierge that lives in your terminal. It doesn't just answer questions; it orchestrates a specialized team of AI agents to:
1.  **Read** your specific local syllabus and notes.
2.  **Teach** you concepts based *only* on that material.
3.  **Quiz** you strictly to ensure mastery.
4.  **Create** formatted PDF study guides automatically.

---

## 2. 🏗️ Technical Architecture

ScholarAgent implements the **Router Pattern** using a modular multi-agent architecture. It uses the **Google Agent Development Kit (ADK)** methodology to coordinate specialized personas.

### The Agent Team
The system consists of one Orchestrator and three Specialist Agents:

1.  **🎩 The Orchestrator (Router):**
    * **Role:** The Manager.
    * **Logic:** Analyzes user input and classifies intent into `RESEARCH`, `QUIZ`, or `NOTES`. It routes the task to the correct specialist.
    * **Model:** `gemini-2.5-flash`.

2.  **🎓 The Researcher (RAG Specialist):**
    * **Role:** The Tutor.
    * **Capability:** Explains concepts and summarizes topics.
    * **Tool:** `file_reader` (Reads local text/syllabus files to ground answers).

3.  **📝 The QuizMaster (Evaluator):**
    * **Role:** The Exam Proctor.
    * **Capability:** Generates hard questions and grades answers as Pass/Fail.
    * **Context:** Uses the syllabus to ensure questions are relevant to the actual exam.

4.  **📄 The NotesTaker (Creator):**
    * **Role:** The Scribe.
    * **Capability:** Compiles conversation history and generates physical files.
    * **Tool:** `pdf_writer` (Converts Markdown summaries into formatted PDF files).

---

## 3. 🎯 Key Features

This project demonstrates **4 Key Concepts** from the AI Agents Intensive:

| Feature | Implementation Details |
| :--- | :--- |
| **1. Multi-Agent System** | Implemented a hierarchical team where a central Orchestrator delegates tasks to `Researcher`, `QuizMaster`, and `NotesTaker` based on intent classification. |
| **2. Custom Tools (MCP)** | Created two custom Python tools: <br>• `read_text_file`: Allows agents to ingest local data.<br>• `create_study_notes_pdf`: Allows agents to generate files on the OS. |
| **3. Sessions & Memory** | utilized `InMemorySessionService` to maintain conversation context. The `NotesTaker` agent uses this memory to recall what was discussed earlier to generate summaries. |
| **4. Context Engineering** | Used distinct `System Instructions` for each agent to enforce strict separation of concerns (e.g., The QuizMaster is "strict," the Researcher is "helpful"). |

---

## 4. 📂 Project Structure

```text
ScholarAgent/
├── root_agent/
│   ├── agent.py
│   ├── prompt.py
│   ├── sub_agents/
│   │   ├── notes_taker/
│   │   │   ├── agent.py
│   │   │   ├── prompt.py
│   │   ├── quiz_master/
│   │   │   ├── agent.py
│   │   │   └── prompt.py
│   │   └── researcher/
│   │       ├── agent.py
│   │       └── prompt.py
│   └── tools/
│       ├── read_file_universal.py
│       └── pdf_writer.py
├── downloads/
├── main.py
├── README.md
├── requirements.txt
└── .env
```

---

## 5. 🚀 Setup & Run Instructions

### Requirements
- Python 3.10 or newer  
- A Google Cloud / AI Studio API key

### Install
```
git clone https://github.com/BhupendraLute/ScholerAgent-AI-Assistent.git

cd ScholarAgent-AI-Assistent

python -m venv venv
source venv/bin/activate   # Windows: .env\Scripts\Activate

pip install -r requirements.txt
```

### Configure Keys
Create a `.env` file in the project root:
```
GOOGLE_API_KEY="your_api_key_here"
```

### Run
```
python main.py
```
---

## 6. 🧪 Example Usage Scenarios

### Research
```
User: Summarize the syllabus.txt file.

Agent: (Reads file) "The syllabus covers OpenGL, 3D Projections, and Shaders..."
```

### Quiz
```
User: Give me a hard quiz based on that summary.

Agent: (Routes to QuizMaster) "Here are 3 questions about OpenGL..."
```

### Notes
```
User: Create a PDF summary of everything we discussed.

Agent: (Routes to NotesTaker) "I have compiled the notes. File saved to downloads/summary.pdf."
```

The PDF will be saved in `downloads/` in current working directory.
---
Built for the Google AI Agents Intensive Capstone 2025.

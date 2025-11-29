# ScholarAgent

A local-first study assistant that helps engineering students organize material, learn faster, and generate polished study notes. It runs in your terminal and uses a coordinated team of AI agents that read your own syllabus and notes, quiz you, and create formatted PDFs.

---

## Overview

Many students spend a large part of their study time searching for files, jumping between PDFs, and figuring out what to review next. Generic language models can help, but they often guess details that aren’t in your actual coursework.

ScholarAgent solves that by working only with your local files. It reads your syllabus and notes, explains concepts using that material, quizzes you on the exact topics you should know, and creates clean PDF study guides.

---

## Architecture

ScholarAgent uses a modular multi-agent setup following the Router Pattern. The system includes one router and three specialists.

### Orchestrator  
Routes user requests to the right specialist. It classifies the intent as research, quizzing, or notes generation.

### Researcher  
Explains material, summaries topics, and answers academic questions. It uses a file-reading tool to stay grounded in your local syllabus and notes.

### QuizMaster  
Creates challenging questions and evaluates answers. It uses the same course material for accuracy and relevance.

### NotesTaker  
Builds PDF study guides from your conversation history. It uses a PDF-writing tool to save formatted files to your drive.

---

## Key Features

### Multi-Agent System  
A central router delegates tasks to the Researcher, QuizMaster, and NotesTaker.

### Custom Tools  
Two custom tools extend capabilities into the local filesystem:
- A file reader for loading your syllabus and notes.
- A PDF writer for generating study guides.

### Session Memory  
The session layer keeps conversation context. NotesTaker uses this to assemble accurate summaries.

### Strict Context Separation  
Each agent follows its own set of system rules. This keeps explanations friendly, quizzes strict, and notes consistent.

---

## Project Structure

```
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

## Setup

### Requirements
- Python 3.10 or newer  
- A Google Cloud / AI Studio API key

### Install

```
git clone <YOUR_REPO_URL>
cd ScholarAgent

python -m venv venv
source venv/bin/activate   # Windows: .env\Scriptsctivate

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

## How to Use

### Research
```
User: Summarize the syllabus.txt file.
```

### Quiz
```
User: Give me a hard quiz based on that summary.
```

### Notes
```
User: Create a PDF summary of everything we discussed.
```

The PDF will be saved in `downloads/`.

---

## Demo

---
Built for the Google AI Agents Intensive Capstone 2025.

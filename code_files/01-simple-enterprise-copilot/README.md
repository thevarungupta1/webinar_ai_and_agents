# Lab 01 — Simple Enterprise Copilot

Single-turn HR policy Q&A using RAG (LangChain + ChromaDB + Streamlit).

No agents, no tools, no conversation memory.

## Architecture

```text
Employee → Streamlit UI → RAG Retriever → ChromaDB (policy docs)
                              ↓
                            LLM → Answer + Citations
```

## Prerequisites

- Python 3.11+
- OpenAI API key

## Setup

```bash
cd code_files/01-simple-enterprise-copilot
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # Windows
# cp .env.example .env   # macOS / Linux
```

Edit `.env` and set your `OPENAI_API_KEY`.

## Index policies

```bash
python ingest.py
```

## Run the app

```bash
streamlit run app.py
```

Open http://localhost:8501

## Optional retrieval smoke test

```bash
python test_rag.py
```

## Suggested demo questions

1. How many annual leave days do I get?
2. What is the sick leave certificate requirement?
3. Can I carry forward unused annual leave?
4. What is travel reimbursement policy for overseas conference? (expect fallback)

## Project layout

```text
01-simple-enterprise-copilot/
├── app.py
├── rag.py
├── ingest.py
├── test_rag.py
├── knowledge_base/
│   ├── leave_policy.md
│   ├── attendance_policy.md
│   └── sick_leave_policy.md
├── chroma_db/          # created by ingest.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

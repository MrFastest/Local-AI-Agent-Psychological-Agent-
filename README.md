
# Local AI Agent 🧠

A lightweight local AI agent that performs sentiment analysis using LangChain-compatible embeddings and vector-based querying. This project processes a dataset, stores vector representations, and provides simple access to responses based on semantic similarity.

---

## Features

- Processes and stores sentence embeddings locally
-  Semantic search using vector similarity
-  Local database storage for responses
-  Command-line interface for asking queries
-  Works offline — no API needed
-  Easily customizable and extendable

---

## 🗂️ Project Structure

```
LOCAL AI AGENT/
├── data.csv                   # Input data containing questions and answers
├── main2.py                   # Main logic to run the AI agent
├── vector2.py                 # Handles vectorization and storage
├── requirements.txt           # List of dependencies
├── __pycache__/               # Auto-generated, ignored in version control
├── sentiment_langchain_db/    # Vector database (optional to commit)
├── venv/                      # Python virtual environment (ignored)
└── .gitignore                 # Prevents uploading unwanted files
```

---

##  Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/local-ai-agent.git
cd local-ai-agent
```

2. **Create Virtual Environment**

```bash
python -m venv venv
```

3. **Activate Virtual Environment**

- Windows:
  ```bash
  venv\Scripts\activate
  ```
- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. **Install Requirements**

```bash
pip install -r requirements.txt
```

---

##  Data Format

Your `data.csv` should be structured as:

| question            | answer                         |
|---------------------|--------------------------------|
| What is AI?         | AI stands for Artificial...    |
| Define sentiment.   | Sentiment refers to emotion... |

---

## ▶️ How to Run

```bash
python main2.py
```

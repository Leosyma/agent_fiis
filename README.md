# 📈 FII Recommendation Assistant using AI

## 📌 Project Structure

### 1. Objective

Provide intelligent, fast, and explainable answers to investor questions about FIIs using the latest AI tools and agent-based orchestration.

### 2. Features

- ✅ Natural language question answering about FIIs.
- ✅ Uses CrewAI to orchestrate agents and tasks.
- ✅ Clean web interface built with Streamlit.
- ✅ Modular architecture separating agent logic and UI.
- ✅ Interprets management reports and key metrics from funds.

---

## 🧠 How It Works

### Crew Orchestration

- **File:** `crew.py`
- Defines the core logic using CrewAI.
- Loads the YAML configuration of agents and tasks.
- Executes a `kickoff()` method to start reasoning and generate a response.

### Backend Execution

- **File:** `main.py`
- Contains the `run_fiis_assistant()` function.
- Initializes the crew and routes the input question to CrewAI logic.

### Streamlit Frontend

- **File:** `app.py`
- Provides an interactive UI.
- Allows the user to input a question.
- Displays the AI-generated recommendation or insight.

---

## 🧱 Tech Stack

- **Language:** Python
- **Frameworks/Libraries:** Streamlit, CrewAI
- **YAML Configuration:** Used for defining agents (`agents.yaml`) and tasks (`tasks.yaml`)

---

## 🚀 Getting Started

### Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example Use Case

> **Question:** "What is the dividend yield of HGLG11 in the last 3 months?"

> **AI Output:** A concise summary analyzing the monthly reports and answering with the calculated yield, trends, and comparison.

---

## 📁 File Overview

| File              | Purpose                                  |
|-------------------|------------------------------------------|
| `app.py`          | Streamlit UI for user interaction        |
| `main.py`         | Function routing input to CrewAI agents  |
| `crew.py`         | Definition of the CrewAI orchestration   |
| `agents.yaml`     | YAML config for agent roles              |
| `tasks.yaml`      | YAML config for AI tasks                 |

---


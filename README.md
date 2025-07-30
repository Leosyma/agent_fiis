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



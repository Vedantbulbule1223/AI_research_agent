# 🤖 AI Research Agent

An AI-powered research assistant built with **LangChain**, **OpenRouter**, **Tavily Search**, and **Streamlit**. The application performs web research, reads relevant web pages, generates structured research reports, and critiques the generated reports using multiple AI agents.

## Live Link 

https://ai-research-agent-vedant.streamlit.app/

## 🚀 Features

* 🔍 Web search using Tavily API
* 📄 Intelligent webpage scraping and content extraction
* 🤖 Multi-agent architecture using LangChain
* 📝 Automatic research report generation
* ⭐ AI-powered report evaluation and scoring
* 🌐 Interactive Streamlit web interface
* 🔑 Secure API key management using Streamlit Secrets

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* OpenRouter API
* Tavily Search API
* BeautifulSoup
* Requests
* LangGraph

## 📂 Project Structure

```
AI_research_agent/
│
├── app.py                 # Streamlit application
├── agents.py              # AI agents and LLM chains
├── tools.py               # Search and scraping tools
├── pipeline.py            # Research workflow
├── config.py              # API key configuration
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Vedantbulbule1223/AI_research_agent.git
cd AI_research_agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file for local development:

```
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

For Streamlit Cloud, add the same keys under:

**Manage App → Settings → Secrets**

```toml
OPENROUTER_API_KEY="your_openrouter_api_key"
TAVILY_API_KEY="your_tavily_api_key"
```

## ▶️ Run Locally

```bash
streamlit run app.py
```

## ☁️ Deployment

This project is compatible with **Streamlit Community Cloud**.

1. Push the project to GitHub.
2. Connect the repository in Streamlit Community Cloud.
3. Add the required secrets.
4. Deploy the app.


## 👨‍💻 Author

**Vedant Bulbule**

GitHub: https://github.com/Vedantbulbule1223



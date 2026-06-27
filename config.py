import os
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st

    try:
        OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
    except Exception:
        OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    try:
        TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
    except Exception:
        TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

except ImportError:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
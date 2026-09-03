"""Streamlit UI for the Simple Enterprise Policy Copilot (single-turn RAG)."""

from __future__ import annotations

import os

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from rag import BASE_DIR, search_policies

load_dotenv(BASE_DIR / ".env")

MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

st.set_page_config(page_title="Enterprise Policy Copilot", page_icon="📋")
st.title("Enterprise Policy Copilot")
st.caption("Simple RAG Q&A (No Agent, No Conversation Memory)")

_api_key = os.getenv("OPENAI_API_KEY", "").strip()
if not _api_key or _api_key == "your-openai-api-key":
    st.error(
        "OPENAI_API_KEY is not set. Copy `.env.example` to `.env` and add your key."
    )
    st.stop()

llm = ChatOpenAI(model=MODEL, temperature=0)

question = st.text_area(
    "Ask a policy question",
    value="How many annual leave days are available and what is carry forward limit?",
    height=120,
)

if st.button("Ask Copilot", type="primary"):
    if not question.strip():
        st.warning("Please enter a policy question.")
    else:
        with st.spinner("Searching policies and preparing answer..."):
            docs = search_policies(question, k=3)

            context = "\n\n".join(doc.page_content for doc in docs)
            sources = sorted(
                {doc.metadata.get("source", "Unknown") for doc in docs}
            )

            prompt = f"""
You are an enterprise HR policy assistant.

Answer only from the provided policy context.
If the answer is not in context, say: "I do not have that policy information in the current knowledge base."

Question:
{question}

Policy Context:
{context}

Return a concise and professional answer.
"""

            response = llm.invoke(prompt)

        st.subheader("Copilot Answer")
        st.write(response.content)

        with st.expander("Citations", expanded=True):
            if sources:
                for source in sources:
                    st.write(f"- {source}")
            else:
                st.write("No sources retrieved.")

        with st.expander("Retrieved Policy Context"):
            if not docs:
                st.write("No matching policy chunks found.")
            for doc in docs:
                st.write(f"**Source:** {doc.metadata.get('source', 'Unknown')}")
                st.write(doc.page_content)
                st.divider()

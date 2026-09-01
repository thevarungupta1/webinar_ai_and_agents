# Webinar RAG Agent Labs

This repository contains hands-on labs for understanding practical enterprise AI application patterns.

## AI (Artificial Intelligence)
AI is the broad field of building systems that can perform tasks requiring human-like intelligence, such as understanding language, reasoning, summarizing, and decision support.

In these labs, AI is mainly used through Large Language Models (LLMs) to interpret user questions and generate useful responses.

## RAG (Retrieval-Augmented Generation)
RAG combines two capabilities:

1. Retrieval: Find relevant information from private/internal documents.
2. Generation: Use the retrieved context with an LLM to produce a grounded answer.

Why it matters:

- LLMs alone may not know your company-specific data.
- RAG improves accuracy by grounding answers in trusted sources.
- RAG helps provide traceability through citations.

## AI Agents
AI agents extend basic Q&A by adding workflow and actions.

A simple way to think about agents:

- LLM for reasoning
- RAG for knowledge grounding
- Tools for actions (for example reading config, logs, or creating tickets)
- Workflow to sequence the steps

Agents are useful when the goal is not just answering a question, but completing a task end-to-end.

## Repository Purpose
These labs progress from simpler to more advanced patterns:

1. Simple policy Q&A with RAG
2. Enterprise copilot with guardrails and actions
3. Agent-style troubleshooting workflows

Use the lab files in this repository to build, run, and demo each pattern step by step.

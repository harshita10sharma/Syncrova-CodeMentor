# Syncrova CodeMentor

An intelligent AI-powered coding mentor that analyzes programming solutions, identifies mistakes, suggests optimizations, estimates algorithm complexity, and provides personalized learning feedback through Large Language Models.

---

## Live API

**Base URL**

https://syncrova-codementor.onrender.com

**Swagger Documentation**

https://syncrova-codementor.onrender.com/docs

---

# Project Overview

Syncrova CodeMentor is designed to help developers improve their coding skills rather than simply generate code.

The system performs intelligent code analysis using an LLM-powered backend capable of evaluating correctness, identifying logical and syntax issues, estimating computational complexity, recommending optimized approaches, and generating structured educational feedback.

The backend is built with FastAPI and deployed on Render, returning standardized JSON responses that can be seamlessly integrated with any frontend application.

---

# Objective

To build an AI-powered coding mentor that assists programmers by:

- Detecting syntax and logical errors
- Suggesting optimized algorithms and data structures
- Estimating Time & Space Complexity
- Evaluating overall code quality
- Providing personalized learning recommendations
- Delivering structured responses for interactive frontend visualization

---

# AI Engine

Unlike traditional chatbots that simply answer questions, Syncrova analyzes source code through a structured AI pipeline.

```text
                 User Code
                     │
                     ▼
          Prompt Engineering Layer
                     │
                     ▼
             Qwen3-Coder LLM
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Error Detection  Optimization  Learning Analysis
      │              │              │
      └──────────────┼──────────────┘
                     ▼
         Structured JSON Response
                     │
                     ▼
        Interactive AI Coding Report
```

---

# Features

### Intelligent Code Analysis

- Syntax Error Detection
- Logical Error Detection
- Runtime Risk Identification
- Edge Case Suggestions

### AI-Based Optimization

- Algorithm Improvements
- Better Data Structure Recommendations
- Code Refactoring Suggestions
- Complexity Reduction

### Complexity Analysis

- Time Complexity Estimation
- Space Complexity Estimation
- Complexity Explanation

### Personalized Learning

- Weak Topic Identification
- Concept Recommendations
- Practice Guidance
- Educational Feedback

### Performance Evaluation

- Correctness Score
- Readability Score
- Optimization Score
- Code Quality Score
- Overall Performance Score
- Confidence Score

### Production Ready Backend

- FastAPI REST API
- Structured JSON Responses
- Prompt Engineering Pipeline
- Docker Support
- Render Deployment

---

# Technology Stack

## Backend

- Python
- FastAPI
- Pydantic

## Artificial Intelligence

- Hugging Face Router
- Qwen3-Coder-480B-A35B-Instruct
- Prompt Engineering

## Deployment

- Docker
- Render

## Development

- Git
- GitHub
- VS Code

---

# Project Architecture

```text
                    Frontend
                        │
                        ▼
                 FastAPI Backend
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
 Prompt Builder                Request Validation
        │
        ▼
 Hugging Face Router API
        │
        ▼
 Qwen3-Coder-480B-A35B-Instruct
        │
        ▼
 Response Parser
        │
        ▼
 JSON Normalization
        │
        ▼
 Structured API Response
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API Status |
| GET | /health | Health Check |
| POST | /analyze | Analyze Source Code |

---

# Sample Request

```json
{
  "code": "print('Hello World')",
  "language": "Python",
  "problem_title": "Hello World"
}
```

---

# Sample Response

```json
{
  "success": true,
  "overall_score": 92,
  "syntax_errors": [],
  "logical_errors": [],
  "optimization_suggestions": [],
  "complexity": {
    "time": "O(n)",
    "space": "O(1)"
  },
  "educational_feedback": [
    "Consider using..."
  ]
}
```

---

# Project Structure

```text
app/
│
├── routes/
├── services/
├── prompts/
├── schemas/
├── utils/
├── config.py
└── main.py

tests/
Dockerfile
requirements.txt
README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/<username>/syncrova-ai.git

cd syncrova-ai
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

---

# Environment Variables

Create a `.env` file.

```env
HF_API_KEY=your_api_key

MODEL_NAME=Qwen/Qwen3-Coder-480B-A35B-Instruct

API_URL=https://router.huggingface.co/v1/chat/completions
```

---

# Docker

Build

```bash
docker build -t syncrova-codementor .
```

Run

```bash
docker run -p 8000:8000 syncrova-codementor
```

---

# Deployment

The backend is deployed on **Render**.

**Live API**

https://syncrova-codementor.onrender.com

**Swagger Documentation**

https://syncrova-codementor.onrender.com/docs

---

# Screenshots

Add the following screenshots after frontend integration:

- Landing Page
- Swagger Documentation
- API Response
- AI Analysis Report
- Architecture Diagram

---

# Roadmap

- [x] FastAPI Backend
- [x] AI Integration
- [x] Prompt Engineering
- [x] Structured JSON Responses
- [x] Docker Support
- [x] Render Deployment
- [ ] Frontend Dashboard
- [ ] Authentication
- [ ] Submission History
- [ ] Performance Analytics
- [ ] Multi-language Analysis
- [ ] Interview Preparation Mode

---

# Team

| Name | Role |
|------|------|
| Harshita Sharma | Machine Learning Engineer |
| *Teammate Name* | Full Stack Developer |

---

# License

This project is licensed under the MIT License.

---

## Vision

**Syncrova CodeMentor aims to bridge the gap between solving coding problems and understanding them. By combining Large Language Models with structured analysis and educational feedback, it transforms every code submission into a meaningful learning experience rather than just producing an answer.**
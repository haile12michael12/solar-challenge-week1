# Solar Challenge Week 1 — Task 1: Git & Environment Setup

## Objective

Establish a collaborative, version-controlled Python project structure for the Solar Data Discovery challenge, ensuring consistency in development environments and automated CI pipelines.

## Project Structure

├── .vscode/
│ └── settings.json
├── .github/
│ └── workflows/
│ ├── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│ ├── **init**.py
│ └── README.md
├── tests/
│ ├── **init**.py
└── scripts/
├── **init**.py
└── README.md

### Repository Initialization

- GitHub repository: `solar-challenge-week1`

1. Clone the repository

   git clone https://github.com/haile12michael12/solar-challenge-week1.git
   cd solar-challenge-week1

2. Create virtual environment:

   python -m venv venv
   source venv/bin/activate # Windows: venv\Scripts\activate

3. Install requirements:
   pip install -r requirements.txt

# AI Response Quality Evaluator
![Python](https://img.shields.io/badge/Python-3.14-blue)

![Tests](https://github.com/faizagohar/ai-response-quality-evaluator/actions/workflows/python-tests.yml/badge.svg)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)


A Python toolkit for evaluating AI-generated responses using structured quality metrics.

## Overview

## Overview

Large Language Models (LLMs) are increasingly deployed in production systems where response quality, safety, and reliability are critical.

This project implements a lightweight evaluation pipeline for assessing AI-generated responses against configurable quality criteria. It loads prompt-response pairs from JSON, evaluates responses across multiple dimensions, generates summary statistics, and exports the results as a CSV report.

The evaluation logic is configuration-driven, allowing scoring rules and safety criteria to be modified without changing the application code. The project also includes automated testing with pytest and Continuous Integration using GitHub Actions.

---

## Features

- Load AI prompts and responses from JSON
- Rule-based quality evaluation
- Relevance scoring
- Safety assessment
- Hallucination detection
- Response clarity evaluation
- Automatic quality classification
- Statistical analysis using NumPy
- CSV report generation
- Input validation and error handling
- Modular project architecture

---

## Project Structure

```
ai-response-quality-evaluator/
│
├── data/
│   └── responses.json
│
├── results/
│   └── evaluation_results.csv
│
├── src/
│   ├── evaluator.py
│   ├── loader.py
│   ├── report.py
│   └── statistics.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## Evaluation Workflow

```
JSON Input
      │
      ▼
Load Responses
      │
      ▼
Evaluate Response Quality
      │
      ▼
Assign Quality Label
      │
      ▼
Calculate Statistics
      │
      ▼
Generate CSV Report
```

---

## Quality Criteria

| Criterion | Purpose |
|-----------|---------|
| Factual Accuracy | Measures whether the response contains correct information |
| Safety | Detects harmful or unsafe outputs |
| Hallucination Risk | Flags unsupported or fabricated information |
| Bias | Identifies potentially biased responses |
| Instruction Following | Checks whether the model follows the user's request correctly |
| Completeness | Evaluates whether important information is missing |
| Clarity | Measures readability and usefulness |

Each criterion contributes to an overall percentage score.

Responses are classified as:

- ✅ Acceptable
- ⚠️ Needs Review
- ❌ Rejected

Safety violations override the numerical score to prevent unsafe responses from receiving high ratings.

---

## Technologies

### Programming Language

- Python

### Libraries

- pandas
- NumPy
- pathlib

### Data Handling

- JSON

### Development Environment

- Visual Studio Code

### Version Control

- Git
- GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/faizagohar/ai-response-quality-evaluator.git
```

Move into the project:

```bash
cd ai-response-quality-evaluator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it (Windows):

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python main.py
```

The application will:

1. Load AI responses from JSON
2. Evaluate every response
3. Generate quality labels
4. Calculate summary statistics
5. Save the complete evaluation report as:

```
results/evaluation_results.csv
```

---

## Example Output

The application evaluates AI-generated responses, assigns quality scores, classifies each response, and produces summary statistics.

Below is an example execution of the evaluator:

![Program Output](output.png)


## Error Handling

The application validates input before evaluation.

It detects:

- Missing JSON file
- Invalid JSON format
- Empty datasets
- Missing required columns

Instead of crashing, the application displays clear error messages.

---
## Architecture

See the project architecture here:

[Architecture Diagram](docs/architecture.md)

## Future Improvements

The current implementation is a rule-based proof of concept. Future versions could include:

### AI & Evaluation
- Semantic similarity scoring using embeddings
- LLM-assisted evaluation for more nuanced quality assessment
- Automatic bias and toxicity detection
- Configurable evaluation rules and scoring weights

### User Experience
- Web interface for uploading JSON files
- Interactive dashboard with charts and filtering
- Export reports to Excel and PDF

### Software Engineering
- Unit and integration tests
- Configuration management
- Logging and monitoring
- REST API for integration with other systems


---

## Author

**Faiza Gohar**
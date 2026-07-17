# Project Architecture

```text
               responses.json
                     │
                     ▼
              loader.py
                     │
                     ▼
            evaluator.py
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
   statistics.py           report.py
         │                       │
         └───────────┬───────────┘
                     ▼
      evaluation_results.csv
```

## Pipeline

1. Load prompt-response pairs from JSON.
2. Evaluate each response against configurable quality criteria.
3. Calculate summary statistics.
4. Export the evaluation report as CSV.
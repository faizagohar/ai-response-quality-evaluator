from pathlib import Path

import pandas as pd


def save_csv_report(df: pd.DataFrame) -> Path:
    project_root = Path(__file__).parent.parent
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    output_path = results_dir / "evaluation_results.csv"
    df.to_csv(output_path, index=False)

    return output_path


def print_summary(statistics: dict, output_path: Path) -> None:
    print("\n" + "=" * 42)
    print("AI RESPONSE QUALITY EVALUATION REPORT")
    print("=" * 42)

    print(f"Total responses:      {statistics['total_responses']}")
    print(f"Average score:        {statistics['average_score']}%")
    print(f"Median score:         {statistics['median_score']}%")
    print(f"Highest score:        {statistics['highest_score']}%")
    print(f"Lowest score:         {statistics['lowest_score']}%")
    print(f"Standard deviation:   {statistics['standard_deviation']}")

    print("\nQuality labels")
    print("-" * 42)
    print(f"Acceptable:           {statistics['acceptable_count']}")
    print(f"Needs Review:         {statistics['needs_review_count']}")
    print(f"Rejected:             {statistics['rejected_count']}")

    print("\nReport saved to:")
    print(output_path)
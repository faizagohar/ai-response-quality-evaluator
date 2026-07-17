import numpy as np
import pandas as pd


def calculate_statistics(df: pd.DataFrame) -> dict[str, int | float]:
    """Calculate summary statistics for evaluated AI responses.

    The function computes descriptive statistics from the percentage
    scores and counts the number of responses in each quality category.

    Args:
        df: DataFrame containing evaluation results.

    Returns:
        A dictionary containing score statistics and quality-label counts.
    """
    scores = df["percentage"].to_numpy()

    return {
        "total_responses": int(len(scores)),
        "average_score": round(float(np.mean(scores)), 2),
        "median_score": round(float(np.median(scores)), 2),
        "highest_score": round(float(np.max(scores)), 2),
        "lowest_score": round(float(np.min(scores)), 2),
        "standard_deviation": round(float(np.std(scores)), 2),
        "acceptable_count": int((df["quality_label"] == "Acceptable").sum()),
        "needs_review_count": int((df["quality_label"] == "Needs Review").sum()),
        "rejected_count": int((df["quality_label"] == "Rejected").sum()),
    }
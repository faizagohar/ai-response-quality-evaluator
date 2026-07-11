import numpy as np
import pandas as pd


def calculate_statistics(df: pd.DataFrame) -> dict:
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
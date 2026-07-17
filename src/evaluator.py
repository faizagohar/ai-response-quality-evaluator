import json
from pathlib import Path
from typing import Any

import pandas as pd


CONFIG_PATH = Path(__file__).parent / "config" / "scoring.json"

with open(CONFIG_PATH, "r", encoding="utf-8") as file:
    CONFIG: dict[str, Any] = json.load(file)


UNSAFE_PHRASES: list[str] = CONFIG["phrases"]["unsafe"]
FUTURE_CLAIM_MARKERS: list[str] = CONFIG["phrases"]["future_claim_markers"]


def evaluate_relevance(prompt: str, response: str) -> int:
    """Evaluate how closely a response relates to the user prompt.

    The function compares lowercased words from the prompt and response
    and assigns a score according to configurable overlap thresholds.

    Args:
        prompt: The original user prompt.
        response: The AI-generated response.

    Returns:
        A relevance score from 0 to 2.
    """
    prompt_words = set(prompt.lower().split())
    response_words = set(response.lower().split())

    matching_words = prompt_words.intersection(response_words)

    full_score_matches = CONFIG["relevance"]["full_score_matches"]
    partial_score_matches = CONFIG["relevance"]["partial_score_matches"]

    if len(matching_words) >= full_score_matches:
        return 2

    if len(matching_words) >= partial_score_matches:
        return 1

    return 0


def evaluate_safety(response: str) -> int:
    """Evaluate whether a response contains configured unsafe phrases.

    Args:
        response: The AI-generated response.

    Returns:
        0 when an unsafe phrase is detected; otherwise 2.
    """
    response_lower = response.lower()

    for phrase in UNSAFE_PHRASES:
        if phrase in response_lower:
            return 0

    return 2


def evaluate_hallucination_risk(prompt: str, response: str) -> int:
    """Evaluate whether the prompt-response pair contains speculative markers.

    Args:
        prompt: The original user prompt.
        response: The AI-generated response.

    Returns:
        0 when a configured future-claim marker is detected; otherwise 2.
    """
    combined_text = f"{prompt} {response}".lower()

    for marker in FUTURE_CLAIM_MARKERS:
        if marker in combined_text:
            return 0

    return 2


def evaluate_clarity(response: str) -> int:
    """Evaluate response clarity using configurable word-count thresholds.

    Args:
        response: The AI-generated response.

    Returns:
        A clarity score from 0 to 2.
    """
    word_count = len(response.split())

    minimum_words = CONFIG["clarity"]["minimum_words"]
    full_score_max_words = CONFIG["clarity"]["full_score_max_words"]

    if word_count < minimum_words:
        return 0

    if word_count <= full_score_max_words:
        return 2

    return 1


def evaluate_response(prompt: str, response: str) -> dict[str, int | float | str]:
    """Evaluate one AI-generated response across all quality criteria.

    Safety violations override the numerical score and produce a
    ``Rejected`` label. Hallucination-risk violations produce a
    ``Needs Review`` label.

    Args:
        prompt: The original user prompt.
        response: The AI-generated response.

    Returns:
        A dictionary containing criterion scores, total score,
        percentage score, and final quality label.
    """
    relevance_score = evaluate_relevance(prompt, response)
    safety_score = evaluate_safety(response)
    hallucination_score = evaluate_hallucination_risk(prompt, response)
    clarity_score = evaluate_clarity(response)

    total_score = (
        relevance_score
        + safety_score
        + hallucination_score
        + clarity_score
    )

    maximum_score = CONFIG["scoring"]["maximum_score"]
    acceptable_threshold = CONFIG["scoring"]["acceptable_threshold"]
    review_threshold = CONFIG["scoring"]["review_threshold"]

    percentage = round((total_score / maximum_score) * 100, 2)

    if safety_score == 0:
        quality_label = "Rejected"
    elif hallucination_score == 0:
        quality_label = "Needs Review"
    elif percentage >= acceptable_threshold:
        quality_label = "Acceptable"
    elif percentage >= review_threshold:
        quality_label = "Needs Review"
    else:
        quality_label = "Rejected"

    return {
        "relevance_score": relevance_score,
        "safety_score": safety_score,
        "hallucination_score": hallucination_score,
        "clarity_score": clarity_score,
        "total_score": total_score,
        "percentage": percentage,
        "quality_label": quality_label,
    }


def evaluate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Evaluate every prompt-response pair in a pandas DataFrame.

    The input DataFrame must contain ``prompt`` and ``response`` columns.
    Evaluation results are appended as new columns.

    Args:
        df: DataFrame containing prompt-response pairs.

    Returns:
        A new DataFrame containing the original data and evaluation results.
    """
    results = df.apply(
        lambda row: evaluate_response(
            row["prompt"],
            row["response"],
        ),
        axis=1,
    )

    results_df = pd.DataFrame(results.tolist())

    return pd.concat(
        [df.reset_index(drop=True), results_df],
        axis=1,
    )
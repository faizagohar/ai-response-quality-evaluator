from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {"id", "prompt", "response"}


def load_responses() -> pd.DataFrame:
    """Load prompt-response pairs from the project JSON dataset.

    The function validates that the input file exists, contains valid JSON,
    is not empty, and includes all required columns.

    Returns:
        pd.DataFrame: A DataFrame containing the prompt-response dataset.

    Raises:
        FileNotFoundError: If the input JSON file cannot be found.
        ValueError: If the JSON is invalid, the dataset is empty,
            or required columns are missing.
    """
    project_root = Path(__file__).parent.parent
    json_path = project_root / "data" / "responses.json"

    if not json_path.exists():
        raise FileNotFoundError(
            f"Input file was not found: {json_path}"
        )

    try:
        df = pd.read_json(json_path)
    except ValueError as error:
        raise ValueError(
            "The responses.json file contains invalid JSON."
        ) from error

    if df.empty:
        raise ValueError(
            "The responses.json file does not contain any responses."
        )

    missing_columns = REQUIRED_COLUMNS.difference(df.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(
            f"The input data is missing required columns: {missing}"
        )

    return df
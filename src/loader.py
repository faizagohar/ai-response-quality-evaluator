import pandas as pd
from pathlib import Path
def load_responses() -> pd.DataFrame:
    project_root = Path(__file__).parent.parent
    json_path = project_root / "data" / "responses.json"
    df = pd.read_json(json_path)

    return df
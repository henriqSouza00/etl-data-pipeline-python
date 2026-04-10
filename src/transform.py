import logging
from datetime import date

import pandas as pd

from .config import SOURCE_NAME

logger = logging.getLogger(__name__)

def transform_states(raw_data: list[dict]) -> pd.DataFrame:
    """Transform raw IBGE data into an analytics-friendly dataframe."""
    logger.info("Starting transformation")

    df = pd.json_normalize(raw_data)

    rename_map = {
        "id": "state_id",
        "sigla": "state_abbr",
        "nome": "state_name",
        "regiao.id": "region_id",
        "regiao.sigla": "region_abbr",
        "regiao.nome": "region_name",
    }
    df = df.rename(columns=rename_map)

    selected_columns = [
        "state_id",
        "state_name",
        "state_abbr",
        "region_id",
        "region_abbr",
        "region_name",
    ]
    df = df[selected_columns].copy()

    df["capitalized_state_name"] = df["state_name"].str.title()
    df["name_length"] = df["state_name"].str.len()
    df["ingestion_date"] = date.today().isoformat()
    df["source"] = SOURCE_NAME

    df = df.sort_values(["region_name", "state_name"]).reset_index(drop=True)

    logger.info("Transformation finished. Final rows: %s", len(df))
    return df

import logging
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

from .config import BASE_DIR, build_connection_string

logger = logging.getLogger(__name__)

TABLE_NAME = "ibge_states"

def load_states(df: pd.DataFrame) -> None:
    """Load dataframe into configured database and save CSV output."""
    logger.info("Starting load process")

    engine = create_engine(build_connection_string())
    df.to_sql(TABLE_NAME, con=engine, if_exists="replace", index=False)
    logger.info("Table '%s' loaded successfully", TABLE_NAME)

    csv_path = BASE_DIR / "data" / "ibge_states.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    logger.info("CSV exported to %s", csv_path)

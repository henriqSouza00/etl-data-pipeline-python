import logging

from .extract import extract_states
from .transform import transform_states
from .load import load_states

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)

def main() -> None:
    logger.info("ETL pipeline started")
    raw_data = extract_states()
    transformed_df = transform_states(raw_data)
    load_states(transformed_df)
    logger.info("ETL pipeline finished successfully")

if __name__ == "__main__":
    main()


import sqlite3

conn = sqlite3.connect("data/ibge_states.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM ibge_states LIMIT 5")
print(cursor.fetchall())
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_TYPE = os.getenv("DB_TYPE", "sqlite").strip().lower()
SQLITE_PATH = os.getenv("SQLITE_PATH", "data/ibge_states.db")

MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "portfolio_data")

IBGE_STATES_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
SOURCE_NAME = "IBGE API"

def build_connection_string() -> str:
    if DB_TYPE == "mysql":
        return (
            f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
            f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
        )

    sqlite_file = BASE_DIR / SQLITE_PATH
    sqlite_file.parent.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{sqlite_file}"

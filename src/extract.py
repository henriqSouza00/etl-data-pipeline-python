import logging
import requests

from .config import IBGE_STATES_URL

logger = logging.getLogger(__name__)

def extract_states() -> list[dict]:
    """Fetch raw state data from the IBGE public API."""
    logger.info("Starting extraction from IBGE API")

    response = requests.get(IBGE_STATES_URL, timeout=30)
    response.raise_for_status()

    payload = response.json()
    logger.info("Extraction finished. Rows fetched: %s", len(payload))
    return payload

import soco
import json
from logger import logging
try:
    coordinator = list(soco.discover())[0].group.coordinator
    logging.info(f"Coordinator {coordinator.player_name}")
except Exception as e:
    logging.error(e)
    raise

def pretty_dict(d):
    d = d.copy()
    try:
        del d["metadata"]
        del d["uri"]
    except Exception as e:
        logging.error(e)
    return json.dumps(d, indent=4)
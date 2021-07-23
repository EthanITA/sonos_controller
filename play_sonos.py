import soco
from logger import logging
from controller import coordinator, pretty_dict

try:
    coordinator.play()
    logging.info(pretty_dict(coordinator.get_current_track_info()))
except Exception as e:
    logging.error(e)
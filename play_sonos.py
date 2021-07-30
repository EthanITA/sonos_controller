import soco
from logger import logging
from controller import coordinator, pretty_dict

try:
    coordinator.shuffle = False
    coordinator.shuffle = True
    coordinator.next()
    coordinator.play()
    logging.info(pretty_dict(coordinator.get_current_track_info()))
except Exception as e:
    logging.error(e)
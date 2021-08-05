import soco
from logger import logging
import controller
from controller import coordinator


try:
    controller.play()
    logging.info(controller.pretty_dict(coordinator.get_current_track_info()))
except Exception as e:
    logging.error(e)
    coordinator.stop()
    playlist_to_play = controller.auto_choose_playlist()
    controller.play_playlist(playlist_to_play)
    logging.info(f"Playing '{playlist_to_play}'' playlist")

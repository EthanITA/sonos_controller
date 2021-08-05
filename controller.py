import soco
import json
from logger import logging
try:
    coordinator = list(soco.discover())[0].group.coordinator
    logging.info(f"Coordinator {coordinator.player_name}")
except Exception as e:
    logging.error(e)
    raise


def play():
    coordinator.shuffle = False
    coordinator.shuffle = True
    coordinator.next()
    coordinator.play()


def play_playlist(playlist):
    coordinator.clear_queue()
    coordinator.add_uri_to_queue(playlist.resources[0].uri)
    coordinator.play_from_queue(index=0)


def auto_choose_playlist():
    for i in coordinator.get_sonos_playlists():
        if i.title == "POP":
            return i
    return coordinator.get_sonos_playlists()[-1]


def pretty_dict(d):
    d = d.copy()
    try:
        del d["metadata"]
        del d["uri"]
    except Exception as e:
        logging.error(e)
    return json.dumps(d, indent=4)

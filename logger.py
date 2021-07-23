import logging
logname = "sonos_controller.log"
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s %(module)s:  %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=logging.INFO)
import logging
import logging.handlers as handlers
from datetime import date
from functools import lru_cache

from fileshare.settings import get_settings


@lru_cache()
def get_config():
    settings = get_settings()
    config = settings.LOG_PATH  
    return config

@lru_cache()
def get_logger():
    today = date.today()
    path = get_config() + '/fileshare_' + str(today) + '.log'

    logger = logging.getLogger('fileshare')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(name)s - %(module)s - %(lineno)s] - %(message)s')

    logHandler = handlers.TimedRotatingFileHandler(path, when='midnight', backupCount=30)
    logHandler.setLevel(logging.INFO)
    logHandler.setFormatter(formatter)

    logger.addHandler(logHandler)
    return logger

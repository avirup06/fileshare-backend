from pydantic_settings import BaseSettings
from functools import lru_cache
import os


class Config(BaseSettings):
    STORAGE: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    LOG_PATH: str

    class Config:
        env_file= ".dev.env"


@lru_cache()
def get_settings():
    print('stage: ', os.environ.get('stage'))
    config = Config()
    return config
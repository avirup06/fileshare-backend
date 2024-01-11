from pydantic_settings import BaseSettings
import yaml
import pathlib
import os
from dotenv import load_dotenv, find_dotenv


class Server(BaseSettings):
    HOST: str
    PORT: int
    RELOAD: bool
    WORKER: bool

    class Config:
        case_sensitive = True


def get_config():
    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), 'server.yaml'), '+r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    
    # os.environ['stage'] = 'DEV'
    if not os.environ.get('STAGE'):
        load_dotenv(find_dotenv(filename='.stage.conf'))
    config = data.get(os.environ.get('STAGE'))
    return config


def get_server_config():
    config = get_config()
    settings = Server(**config)
    return settings


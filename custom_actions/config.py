import os
import logging

from dataclasses import dataclass, field, fields

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()


@dataclass
class Config:
    DEBUG: bool = False
    SECRET_KEY: str = "foobar"
    INSTAGRAM_APP_BASE_URL: str = None
    INSTAGRAM_ACCESS_TOKEN: str = None



def get_config():
    conf = Config()

    for conf_field in fields(conf):
        if conf_field.name in os.environ:
            default_val = getattr(conf, conf_field.name)
            raw_val = os.environ[conf_field.name]
            if default_val:
                logger.debug(f"Found field '{conf_field.name}' in env overwriting `{default_val}` with `{raw_val}`")
            setattr(conf, conf_field.name, os.environ[conf_field.name])

    logger.debug(f"get_config produced from environment: {conf} ")
    return conf

import os
from typing import List

from dotenv import load_dotenv

# Load .env into environment
load_dotenv()


def get_bool(key: str, default: bool = False) -> bool:
    return os.getenv(key, str(default)).lower() in ("1", "true", "yes")


def get_list(key: str, separator=",", default=[]) -> List[str]:
    val = os.getenv(key)
    return val.split(separator) if val else default


# General Django settings
DEBUG = get_bool("DJANGO_DEBUG", default=False)
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-default")
ALLOWED_HOSTS = get_list("DJANGO_ALLOWED_HOSTS", default=["localhost"])

# RabbitMQ
RABBITMQ_URL = os.getenv("RABBITMQ_URL")

# Supabase
SUPABASE_DB_URL = os.getenv("SUPABASE_DB_URL")
SUPABASE_DB_PREFIX = os.getenv("SUPABASE_DB_PREFIX")

# PostgreSQL
# TIMESCALE_DB_USER = os.getenv("TIMESCALE_DB_USER")
# TIMESCALE_DB_PASS = os.getenv("TIMESCALE_DB_PASS")
# TIMESCALE_DB_HOST = os.getenv("TIMESCALE_DB_HOST")
# TIMESCALE_DB_PORT = os.getenv("TIMESCALE_DB_PORT")
# TIMESCALE_DB_NAME = os.getenv("TIMESCALE_DB_NAME")

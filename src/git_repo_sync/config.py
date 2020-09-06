import os
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings
from pathlib import Path

APP_ENV: str = os.getenv("APP_ENV", "dev")


# eg .env.dev, .env.production
p: Path = Path(__file__).parents[2] / f"env/.env.{APP_ENV}"
config: Config = Config(p if p.exists() else None)

PROJECT_NAME: str = "Git Repo Sync"

ALLOWED_HOSTS: CommaSeparatedStrings = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="localhost"
)

GIT_SOURCE_USERNAME: str = Config("GIT_SOURCE_USERNAME", cast=str)

GIT_SOURCE_TOKEN: str = Config("GIT_SOURCE_TOKEN", cast=str)

GIT_STATE_PATH: str = Config("GIT_STATE_PATH", cast=str)

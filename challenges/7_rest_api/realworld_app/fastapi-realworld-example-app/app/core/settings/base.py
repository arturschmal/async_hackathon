from enum import Enum

from pydantic import BaseSettings, PostgresDsn, SecretStr


class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.test

    class Config:
        env_file = ".env"

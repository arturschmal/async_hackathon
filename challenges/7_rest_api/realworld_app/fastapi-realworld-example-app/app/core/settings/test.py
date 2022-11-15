import logging

from pydantic import PostgresDsn, SecretStr

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test FastAPI example application"

    secret_key: SecretStr = SecretStr("test_secret")

    database_url: PostgresDsn = "postgresql://postgres:postgres@host.docker.internal:5432/rwdb"
    max_connection_count: int = 5
    min_connection_count: int = 5

    logging_level: int = logging.DEBUG

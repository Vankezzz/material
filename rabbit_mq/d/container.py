import logging.config
import sqlite3
from dependency_injector import containers, providers

from d.services.base import UserService, AuthService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    # Gateways

    database_client = providers.Singleton(
        sqlite3.connect,
        config.database.dsn,
    )

    # Services
    user_service = providers.Factory(
        UserService,
        db=database_client,
    )

    auth_service = providers.Factory(
        AuthService,
        db=database_client,
        token_ttl=config.auth.token_ttl.as_int(),
    )

    # photo_service = providers.Factory(
    #     services.PhotoService,
    #     db=database_client,
    #     s3=s3_client,
    # )
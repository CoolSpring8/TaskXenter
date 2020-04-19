from tortoise import Tortoise
from fastapi import FastAPI
from loguru import logger

from app.core.config import DATABASE_URL


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to {0}", repr(DATABASE_URL))

    await Tortoise.init(
        db_url=str(DATABASE_URL),
        modules={'models': ['app.models.tortoise.user', 'app.models.tortoise.task']}
    )

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await Tortoise.close_connections()

    logger.info("Connection closed")

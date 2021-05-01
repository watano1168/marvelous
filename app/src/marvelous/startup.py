from marvelous.settings.env import discord_token
from marvelous.data_store.mysql.connection import wait_ready
from marvelous.client import start
from marvelous.settings import env
import logging
import asyncio


async def wait_db_ready():
    await wait_ready()


async def startup_async():
    print((
        "===============================\n"
        "||    Marvelous started!!    ||\n"
        "===============================\n"
    ))
    logging.basicConfig(level=logging.DEBUG if env.run_environment == "development" else logging.WARNING)
    await wait_db_ready()
    await start(discord_token)


def startup():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(startup_async())

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncpg

from bot.config import load_config
from bot.handlers.tariff import register_tariff_handler
from bot.handlers.home import register_home_handler
from bot.middlewares.db import DbMiddleware
from bot.middlewares.environment import EnvironmentMiddleware
from bot.service.repository import Repo

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))



def register_all_handlers(dp):
    register_tariff_handler(dp)
    register_home_handler(dp)


# TODO create_pool

async def create_pool(user, password, host, db):
    return await asyncpg.create_pool(
        user=user,
        database=db,
        password=password,
        host=host
    )


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())

    pool = await create_pool(
        user=config.db.user,
        password=config.db.password,
        host=config.db.host,
        db=config.db.database
    )
    dp.middleware.setup(DbMiddleware(pool))
    register_all_middlewares(dp, config)
    register_all_handlers(dp)
    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

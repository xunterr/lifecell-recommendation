import asyncio
import logging
import json
from typing import List

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncpg

from bot.config import *
from bot.handlers.tariff import TariffHandler
from bot.handlers.poll import *
from bot.handlers.home import register_home_handler
from bot.middlewares.db import DbMiddleware
from bot.middlewares.environment import EnvironmentMiddleware
from bot.service.repository import Repo
from bot.model import poll

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_handlers(dp, config: Config):
    TariffHandler(dp, config=config)
    PollHandler(questions=load_questions(), dp=dp, config=config)
    register_home_handler(dp)

def load_questions():
    with open("questions.json", encoding='utf-8') as file:
        json_data = file.read()
    j = json.loads(json_data)
    questions: List[poll.Question] = []
    for question_json in j:
        question_text = question_json["question"]
        variants = question_json["variants"]
        prep_variants = question_json["prepared_variants"]
        question = poll.Question(question=question_text, variants=variants, prep_variants=prep_variants)
        questions.append(question)

    return questions

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

    # pool = await create_pool(
    #     user=config.db.user,
    #     password=config.db.password,
    #     host=config.db.host,
    #     db=config.db.database
    # )
    # dp.middleware.setup(DbMiddleware(pool))
    # register_all_middlewares(dp, config)
    register_all_handlers(dp, config)
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

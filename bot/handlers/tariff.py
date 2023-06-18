from aiogram import Dispatcher, types
from aiogram.types import Message
from bot.keyboards import default_keyboard
from bot.api import tariff_recommendation
from aiogram.dispatcher import FSMContext
from dataclasses import dataclass
from bot.model import poll
from bot.config import Config
from bot.handlers import poll

class TariffHandler:
    def __init__(self, dispatcher: Dispatcher, config: Config):
        self.config = config
        dispatcher.register_callback_query_handler(self.get_tariff, lambda callback_query: callback_query.data == "get_tariff")

    async def get_tariff(self, callback_query: types.CallbackQuery):
        await callback_query.message.answer("Ви ще не підібрали тариф")

    async def handle_poll_result(self, msg: types.Message):
        tr = tariff_recommendation.TarifRecommendationAPI(self.config) # tr.get_recommendation(res)
        await msg.answer("Ваш ідеальний тариф: ...")
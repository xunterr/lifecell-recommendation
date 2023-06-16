from aiogram import Dispatcher, types
from aiogram.types import Message
from bot.keyboards import start

async def get_tariff(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Ви ще не підібрали тариф")

def register_tariff_handler(dispatcher: Dispatcher):
    dispatcher.register_callback_query_handler(get_tariff, lambda callback_query: callback_query.data == "get_tariff")
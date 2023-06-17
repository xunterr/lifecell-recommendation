from aiogram import Dispatcher, types
from aiogram.types import Message
from bot.keyboards import default_keyboard
from bot.service import recommendation_service

def register_tariff_handler(dispatcher: Dispatcher):
    dispatcher.register_callback_query_handler(get_tariff, lambda callback_query: callback_query.data == "get_tariff")
    dispatcher.register_callback_query_handler(find_tariff, lambda callback_query: callback_query.data == "find_tariff")
    dispatcher.register_callback_query_handler(on_poll_update, lambda callback_query: callback_query.data == "poll_update")

async def get_tariff(callback_query: types.CallbackQuery):
    recommendation_service.get_tariff()
    await callback_query.message.answer("Ви ще не підібрали тариф")

async def find_tariff(callback_query: types.CallbackQuery):
    questions = {
        "Скільки вам років?": ["0-16", "17-30", "30-55", "55+"],
        "Скільки ви робите дзвінків на тиждень?": ["Багато", "Звичайна кількість", "Мало"],
    }
    msg: Message = await callback_query.message.answer("Тест починається...")
    for q in questions:
        poll_kb = default_keyboard.get_poll_kb(questions[q])
        msg.edit_text(q, reply_markup=poll_kb)

async def on_poll_update(callback_query: types.CallbackQuery, callback_data: dict):
    next_question = callback_data["question"]
    next_variants = callback_data["variants"]
    ca


from aiogram import Dispatcher
from aiogram.types import Message
from bot.keyboards import default_keyboard


async def start_bot(message: Message):
    await message.reply("Привіт, я - Lifecell bot!", reply_markup=default_keyboard.get_start_kb())

def register_home_handler(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=["start"], state="*")
    
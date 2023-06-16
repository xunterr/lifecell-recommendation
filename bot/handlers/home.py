from aiogram import Dispatcher
from aiogram.types import Message
from bot.keyboards import start


async def start_bot(message: Message):
    await message.reply("Привіт, я - Lifecell bot!", reply_markup=start.keyboard)

def register_home_handler(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=["start"], state="*")
    
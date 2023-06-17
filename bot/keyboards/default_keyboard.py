from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from bot.model import poll

def get_poll_kb(current: poll.Question, cd: CallbackData):
    keyboard = InlineKeyboardMarkup()
    print(current.variants)
    for v in current.variants:
        print(v)
        variant_bt = InlineKeyboardButton(text=v, callback_data=cd.new(
            action="answer",
            question=current,
            variant=v
        ))
        keyboard.add(variant_bt)
        
    return keyboard

def get_start_kb():
    github_bt = InlineKeyboardButton(text="👩‍💻 Github", url="https://github.com/xunterr/GameOFTeens2023_PYTHON")
    my_results_bt = InlineKeyboardButton(text="🤯 Підібраний тариф", callback_data="get_tariff")
    find_tariff_bt = InlineKeyboardButton(text="🚀 Підібрати тариф", callback_data="start_poll")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(github_bt).add(my_results_bt).add(find_tariff_bt)
    return keyboard
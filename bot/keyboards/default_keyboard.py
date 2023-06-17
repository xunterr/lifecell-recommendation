from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_poll_kb(variants: list):
    keyboard = InlineKeyboardMarkup()
    for v in variants:
        variant_bt = InlineKeyboardButton(v, callback_data="poll_update")
        keyboard.add(variant_bt)
        
    return keyboard

def get_start_kb():
    github_bt = InlineKeyboardButton(text="👩‍💻 Github", url="https://github.com/xunterr/GameOFTeens2023_PYTHON")
    my_results_bt = InlineKeyboardButton(text="🤯 Підібраний тариф", callback_data="get_tariff")
    find_tariff_bt = InlineKeyboardButton(text="🚀 Підібрати тариф", callback_data="find_tariff")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(github_bt).add(my_results_bt).add(find_tariff_bt)
    return keyboard
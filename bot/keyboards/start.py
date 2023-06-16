from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

github_bt = InlineKeyboardButton(text="👩‍💻 Github", url="https://github.com/xunterr/GameOFTeens2023_PYTHON")
my_results_bt = InlineKeyboardButton(text="🤯 Підібраний тариф", callback_data="get_tariff")
start_bt = InlineKeyboardButton(text="🚀 Підібрати тариф", callback_data="start")
keyboard = InlineKeyboardMarkup()
keyboard.add(github_bt).add(my_results_bt).add(start_bt)
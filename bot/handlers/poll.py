from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from bot.keyboards import default_keyboard
from typing import List
from bot.model import poll
from aiogram.utils.callback_data import CallbackData

class PollState(StatesGroup):
    START = State()
    FINISH = State()

class PollHandler:
    def __init__(self, dp: Dispatcher) -> None:
        self.questions_left: List[poll.Question] = [
            poll.Question("ASDasd", ["asd", "asd", "Asd"], ["asd", "asd", "asd"]),
            poll.Question("ASDasdasd", ["asd", "asasd", "Assd"], ["asd", "sasd", "asd"])
        ]
        self.question_callback = CallbackData("action", "question", "variant")
        self.results = []
        self.current_question = 0
        dp.register_callback_query_handler(self.start_poll, lambda callback_query: callback_query.data == "start_poll")
        dp.register_callback_query_handler(self.handle_answer, self.question_callback.filter())

    async def handle_answer(self, callback_query: types.CallbackQuery, callback_data: dict):
        variant = callback_data["variant"]
        self.results.append(variant)
        await self.display_next_question(callback_query.message)

    async def display_next_question(self, msg: types.Message):
        if(len(self.questions_left) == 0):
            PollState.FINISH.set()
            return
        q = self.questions_left.pop(0)
        keyboard = default_keyboard.get_poll_kb(q, self.question_callback)
        await msg.edit_text(q.question, reply_markup=keyboard)
        

    async def start_poll(self, callback_query: types.CallbackQuery):
        msg: types.Message = await callback_query.message.answer("Tariff")
        await self.display_next_question(msg)

            
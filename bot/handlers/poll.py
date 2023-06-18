from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from bot.keyboards import default_keyboard
from typing import List
from bot.model import poll
from aiogram.utils.callback_data import CallbackData

class PollHandler:
    def __init__(self, questions: list, dp: Dispatcher) -> None:
        self.questions: List[poll.Question] = questions
        self.question_callback = CallbackData("action", "question", "variant")
        self.results = []
        self.current_question = 0
        dp.register_callback_query_handler(self.start_poll, lambda callback_query: callback_query.data == "start_poll")
        dp.register_callback_query_handler(self.handle_answer, self.question_callback.filter())

    async def handle_answer(self, callback_query: types.CallbackQuery, callback_data: dict):
        variant = int(callback_data["variant"])
        question = int(callback_data["question"])
        self.results.append(self.questions[question].prepared_variants[variant])
        await self.display_next_question(callback_query.message)

    async def display_next_question(self, msg: types.Message):
        if(len(self.questions) == self.current_question):
            self.current_question=0
            await msg.answer(text="Опитування завершено, raw results: " + ','.join(self.results))
            return
        q = self.questions[self.current_question]
        keyboard = default_keyboard.get_poll_kb(q.variants, self.current_question, self.question_callback)
        self.current_question += 1
        await msg.edit_text(q.question, reply_markup=keyboard)

    async def start_poll(self, callback_query: types.CallbackQuery):
        msg: types.Message = await callback_query.message.answer("Tariff")
        await self.display_next_question(msg)

            
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from bot.keyboards import default_keyboard
from typing import List
from bot.model import poll
from bot import config
from bot.api import tariff_recommendation
from aiogram.utils.callback_data import CallbackData

class PollState(StatesGroup):
    polling = State()
    finish = State()

class PollHelper:
    def __init__(self, questions: list, finish_callback, dp: Dispatcher, config: config.Config) -> None:
        self.questions: List[poll.Question] = questions
        self.config = config
        self.question_callback = CallbackData("action", "question", "variant")
        self.keyboard = default_keyboard.PollKeyboard()
        self.finish_callback = finish_callback
        self.current_question = 0
        dp.register_callback_query_handler(self.start_poll, lambda callback_query: callback_query.data == "start_poll")
        dp.register_callback_query_handler(self.handle_answer, self.question_callback.filter(), state=PollState.polling)
        dp.register_callback_query_handler(self.handle_poll_end,
                                           lambda callback_query: callback_query.data == "finish_poll", 
                                           state=PollState.finish)

    async def handle_answer(self, callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext):
        variant = int(callback_data["variant"])
        question = int(callback_data["question"])
        prepared_variant = self.questions[question].prepared_variants[variant]
        data = await state.get_data()
        result = data.get("result")

        if result:
            result.append(prepared_variant)
        else:
            result = [prepared_variant]

        await state.update_data(result=result)
        await self.display_next_question(callback_query.message)

    async def display_next_question(self, msg: types.Message):
        if(len(self.questions) == self.current_question):
            await PollState.finish.set()
            await msg.edit_text("Вітаємо! Тест завершено", reply_markup=self.keyboard.get_finish_kb())
            return
        q = self.questions[self.current_question]
        keyboard = self.keyboard.get_question_kb(q.variants, self.current_question, self.question_callback)
        self.current_question += 1
        await msg.edit_text(q.question, reply_markup=keyboard)

    async def handle_poll_end(self, callback_query: types.CallbackQuery, state: FSMContext):
        data = await state.get_data()
        result = data.get("result")
        await state.finish()
        await self.finish_callback(result, callback_query.message)

    async def start_poll(self, callback_query: types.CallbackQuery):
        await PollState.polling.set()
        self.current_question=0
        msg: types.Message = await callback_query.message.answer("Опитування починається...")
        await self.display_next_question(msg)
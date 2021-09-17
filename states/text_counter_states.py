from aiogram.dispatcher.filters.state import StatesGroup, State


class Counter(StatesGroup):
    stage1 = State()
    stage2 = State()
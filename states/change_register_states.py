from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangeRegister(StatesGroup):
    stage1 = State()
    stage2 = State()
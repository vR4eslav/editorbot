from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from antiplagiat import Antiplagiat

from data.config import ADVEGO_TOKEN
from loader import dp

api = Antiplagiat(ADVEGO_TOKEN)


async def antiplagiator(text):
    result = api.unique_text_add(text)
    key = result['key']
    result = api.unique_check(key)
    if result['status'] == 'done':
        print('Done!')
        # сделать чтото с отчетом
        return
    elif result['status'] == 'error':
        print(f'Error: {result}')
        return
    elif result['status'] == 'not found':
        print('Not found!')
        return


@dp.message_handler(Command('plagiat'))
async def plagiat_check_start(message: types.Message, state: FSMContext):
    await message.answer(f'Пришлите текст для проверки на плагиат! Не больше 4096 символов')
    await state.set_state('process_plagiat')


@dp.message_handler(state='process_plagiat')
async def plagiat_check_start(message: types.Message, state: FSMContext):
    await antiplagiator(text=message.text)
    await state.reset_state()

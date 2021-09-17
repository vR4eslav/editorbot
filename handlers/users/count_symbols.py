from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.cancel_keyboard_inline import keyboard_cancel
from keyboards.inline.text_actions_inline import text_actions_keyboard
from loader import dp, bot


@dp.message_handler(text='/count_symbols')
async def start_count_symbols(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'⬇️ Пришлите <b>текст</b>, который нужно посчитать на символы ⬇️',
                           reply_markup=keyboard_cancel)
    await state.set_state('symbol_count1')


@dp.callback_query_handler(text='count_symbols')
async def start_count_symbols(call: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id,
                                text=f'⬇️ Пришлите <b>текст</b>, который нужно посчитать на символы ⬇️',
                                reply_markup=keyboard_cancel)
    await state.set_state('symbol_count1')


@dp.message_handler(state='symbol_count1')
async def count_symbols(message: types.Message, state: FSMContext):
    data = message.text
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'☑️В присланном сообщении <b>{len(data)}</b> символов! Что нужно сделать еще?',
                           reply_markup=text_actions_keyboard)
    await state.reset_state()


@dp.callback_query_handler(text='cancel', state='symbol_count1')
async def start_count_symbols(call: CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=call.from_user.id,
                           text=f'❗️ Вы отменили подсчет символов!',
                           reply_markup=text_actions_keyboard)
    await state.reset_state()

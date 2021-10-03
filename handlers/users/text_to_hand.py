import os

import pywhatkit as pywhatkit
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, state
from aiogram.types import InputFile, CallbackQuery

from keyboards.inline import cancel_keyboard_inline
from keyboards.inline.cancel_keyboard_inline import keyboard_cancel
from keyboards.inline.text_actions_inline import text_actions_keyboard
from loader import bot, dp
from utils.misc import rate_limit


async def text_to_hand_create_job(text, chat_id, reply_markup=None):
    pywhatkit.text_to_handwriting(text, save_to=f'data/temp_text_to_hand/{chat_id}.png', rgb=(0, 0, 255))
    await bot.send_photo(chat_id=chat_id,
                         caption=f'☑️ Вот ваш рукописный текст! \n\nЕсли картинка пустая, то скорее всего,'
                                 f'вы отправили неподдерживаемый текст в боте. Пока что. 🤫',
                         photo=InputFile(f"data/temp_text_to_hand/{chat_id}.png"), reply_markup=reply_markup)
    os.remove(f"data/temp_text_to_hand/{chat_id}.png")


@dp.message_handler(Command('text_to_hand'))
async def text_to_hander(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'🖨 Пришлите мне текст на английском языке, который вы хотите сделать рукописным!')
    await state.set_state('text_to_hand1')


@rate_limit(8, 'text_to_hand')
@dp.callback_query_handler(text='text_to_hand')
async def text_to_hander_cb(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'🖨 Пришлите мне текст на английском языке, который вы хотите сделать рукописным!',
                                 reply_markup=keyboard_cancel)
    await state.set_state('text_to_hand1')


@rate_limit(8, 'text_to_hand')
@dp.message_handler(state='text_to_hand1')
async def finish_tth(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    btn3 = types.InlineKeyboardButton(text='↩️ Назад в меню', callback_data='back_to_menu_from_file')
    keyboard.add(btn3)
    await text_to_hand_create_job(text=message.text, chat_id=message.from_user.id, reply_markup=keyboard)
    await state.reset_state()


@dp.callback_query_handler(text='cancel')
async def text_to_hander_cb(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'❎ Вы отменили перевод текста в рукописный вид. Что нужно сделать еще?',
                                 reply_markup=text_actions_keyboard)
    await state.reset_state()

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from loader import dp
from utils.misc import rate_limit


@rate_limit(10, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='➡️МЕНЮ⬅️', callback_data='menu')
    btn2 = types.InlineKeyboardButton(text='🔹О БОТЕ🔹', callback_data='about_bot')
    keyboard.row(btn1, btn2)
    await message.answer(f"🔆Привет, {message.from_user.full_name}! Я <b>бот-редактор</b>!🔆\n\n"
                         f"Жми кнопки ниже, чтобы перейти к манипуляциям с текстом!", reply_markup=keyboard)


@dp.callback_query_handler(text='back_to_menu')
async def bot_start_back(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='➡️МЕНЮ⬅️', callback_data='menu')
    btn2 = types.InlineKeyboardButton(text='🔹О БОТЕ🔹', callback_data='about_bot')
    keyboard.row(btn1, btn2)
    await call.message.edit_text(text=f"🔆Привет, {call.from_user.full_name}! Я <b>бот-редактор</b>!🔆\n\n"
                                      f"Жми кнопки ниже, чтобы перейти к манипуляциям с текстом!",
                                 reply_markup=keyboard)

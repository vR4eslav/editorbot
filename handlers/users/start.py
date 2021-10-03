from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from asyncpg import UniqueViolationError

from loader import dp, db
from utils.misc import rate_limit


@rate_limit(10, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='➡️МЕНЮ⬅️', callback_data='menu')
    btn2 = types.InlineKeyboardButton(text='🔹О БОТЕ🔹', callback_data='about_bot')
    btn3 = types.InlineKeyboardButton(text='Поддержать проект', url='https://www.donationalerts.com/r/vr4eslav')
    keyboard.row(btn1, btn2)
    keyboard.add(btn3)
    name = message.from_user.full_name
    try:
        await db.add_user(full_name=message.from_user.full_name,
                          username=message.from_user.username,
                          telegram_id=message.from_user.id)
    except UniqueViolationError:
        pass
    await message.answer(f"🔆Привет, {message.from_user.full_name}! Я <b>бот-редактор</b>!🔆\n\n"
                         f"Жми кнопки ниже, чтобы перейти к манипуляциям с текстом!", reply_markup=keyboard)


@dp.callback_query_handler(text='back_to_menu')
async def bot_start_back(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='➡️МЕНЮ⬅️', callback_data='menu')
    btn2 = types.InlineKeyboardButton(text='🔹О БОТЕ🔹', callback_data='about_bot')
    btn3 = types.InlineKeyboardButton(text='Поддержать проект', url='https://www.donationalerts.com/r/vr4eslav')
    keyboard.row(btn1, btn2)
    keyboard.add(btn3)
    await call.message.edit_text(text=f"🔆Привет, {call.from_user.full_name}! Я <b>бот-редактор</b>!🔆\n\n"
                                      f"Жми кнопки ниже, чтобы перейти к манипуляциям с текстом!",
                                 reply_markup=keyboard)

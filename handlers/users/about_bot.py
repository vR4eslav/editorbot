from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp


@dp.callback_query_handler(text='about_bot')
async def cq_about(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton(text='🔙 НАЗАД В МЕНЮ 🔙', callback_data='back_to_menu')
    keyboard.add(btn5)
    await call.message.edit_text(text='Active development!', reply_markup=keyboard)
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, _


@dp.message_handler(Command('donate'))
async def get_donate(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn3 = types.InlineKeyboardButton(text=_('Поддержать проект'), url='https://www.donationalerts.com/r/vr4eslav')
    keyboard.add(btn3)
    btn6 = types.InlineKeyboardButton(text=_('🔙 НАЗАД В МЕНЮ 🔙'), callback_data='back_to_menu')
    keyboard.add(btn6)
    await message.answer(_('Вы можете поддержать проект, нажав на кнопку ниже. Спасибо ❤️'), reply_markup=keyboard)
from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp


@dp.callback_query_handler(text='about_bot')
async def cq_about(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton(text='🔙 НАЗАД В МЕНЮ 🔙', callback_data='back_to_menu')
    keyboard.add(btn5)
    await call.message.edit_text(text="Отправь текст, который хочешь проверить, и получи результат! Объем одной проверки — 4096 символов.\n",
                                       "Хочешь проверить документ на уникальность? Просто отправь файл!\n",
                                       "Все доступные услуги:\n\n",
                                       "Проверить текст на уникальность\n",
                                       "Посчитать символы в тексте\n",
                                       "Поменять регистр сообщения\n",
                                       "Проверить текст на орфографию\n\n",
                                       "⚠️Возникли трудности или предложения — пиши: support@text.ru" , reply_markup=keyboard)

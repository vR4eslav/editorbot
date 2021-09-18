from aiogram import types
from aiogram.types import CallbackQuery

from data import config
from loader import dp


@dp.callback_query_handler(text='about_bot')
async def cq_about(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton(text='🔙 НАЗАД В МЕНЮ 🔙', callback_data='back_to_menu')
    keyboard.add(btn5)
    await call.message.edit_text(text=f"Отправь текст, который хочешь проверить, и получи результат! Объем одной "
                                      f"проверки — 4096 символов.\n"
                                      # f"Хочешь проверить документ на уникальность? Просто отправь файл!\n"
                                      f"Все доступные услуги:\n\n"
                                      # f"Проверить текст на уникальность\n"
                                      f"Посчитать символы в тексте\n"
                                      f"Поменять регистр сообщения\n"
                                      f"Проверить текст на орфографию\n\n"
                                      f"⚠️Возникли трудности или предложения — пиши: {config.email}",
                                 reply_markup=keyboard)

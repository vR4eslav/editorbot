from aiogram import types
from aiogram.types import CallbackQuery

from data import config
from loader import dp, _


@dp.callback_query_handler(text='about_bot')
async def cq_about(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    btn6 = types.InlineKeyboardButton(text=_('🔙 НАЗАД В МЕНЮ 🔙'), callback_data='back_to_menu')
    keyboard.add(btn6)
    await call.message.edit_text(text=_("Отправь текст, который хочешь проверить, и получи результат! Объем одной "
                                        "проверки — 4096 символов.\n"
                                        # f"Хочешь проверить документ на уникальность? Просто отправь файл!\n"
                                        "Все доступные услуги:\n\n"
                                        # f"Проверить текст на уникальность\n"
                                        "Посчитать символы в тексте\n"
                                        "Поменять регистр сообщения\n"
                                        "Проверить текст на орфографию\n\n"
                                        "Сгенерировать надежный пароль\n\n"
                                        "⚠️Возникли трудности или предложения — пиши: {email}\n\n").format(
        email=config.email), reply_markup=keyboard)

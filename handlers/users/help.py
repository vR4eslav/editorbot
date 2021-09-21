from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(10, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton(text='🔙 НАЗАД В МЕНЮ 🔙', callback_data='back_to_menu')
    keyboard.add(btn5)
    await message.answer(text=f'📌 СПИСОК КОМАНД 📌\n\n'
                              f'➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                              f'Старт команды: \n\n'
                              f'/start - Старт\n'
                              f'/help - Помощь/Команды\n'
                              f'/menu - Главное меню\n'
                              f'➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                              f'Работа с текстом: \n\n'
                              f'/change_register - Поменять регистр\n '
                              f'/check_spelling - Проверить орфографию (поддерживается только 🇷🇺)\n'
                              f'/count_words - Посчитать слова в тексте (поддержка 🇷🇺/🇬🇧)\n'
                              f'/count_symbols - Посчитать количество символов в тексте (вместе с пробелами)\n'
                              f'/generate_password - Сгенерировать пароль\n'
                              f'➖➖➖➖➖➖➖➖➖➖➖➖➖\n'
                              f'Помощь: \n'
                              f'Разработчик: botdevslava@gmail.com\n'
                              f'➖➖➖➖➖➖➖➖➖➖➖➖➖\n')

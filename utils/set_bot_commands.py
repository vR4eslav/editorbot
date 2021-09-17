from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("menu", "Меню"),
            types.BotCommand('change_register', 'Поменять регистр'),
            types.BotCommand('check_spelling', 'Проверить текст на орфографические ошибки(RU)'),
            types.BotCommand('count_words', 'Посчитать слова в тексте(RU-EN)'),
            types.BotCommand('count_symbols', 'Посчитать символы')
        ]
    )

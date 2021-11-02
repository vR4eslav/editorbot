from aiogram import executor
from loguru import logger

from loader import dp, db, i18n
import middlewares, filters, handlers
from middlewares.language_middleware import setup_middleware
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    setup_middleware(dp)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    await db.create()
    await db.create_table_users()
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

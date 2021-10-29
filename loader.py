import aiojobs as aiojobs
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from data import config
from data.config import I18N_DOMAIN, LOCALES_DIR
from utils.db_api.postgresql import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()
# Настроим i18n middleware для работы с многоязычностью
i18n = I18nMiddleware(I18N_DOMAIN, LOCALES_DIR)
# Создадим псевдоним для метода gettext
_ = i18n.gettext
# scheduler = await aiojobs.create_scheduler()
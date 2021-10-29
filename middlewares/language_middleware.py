from typing import Tuple, Any, Optional

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware

from data.config import LOCALES_DIR, I18N_DOMAIN
from loader import db


async def get_lang(user_id):
    # Делаем запрос к базе, узнаем установленный язык
    user = await db.select_user(telegram_id=user_id)
    if user:
        # Если пользователь найден - возвращаем его
        return user.get('locale')


class ACLMiddleware(I18nMiddleware):
    # Каждый раз, когда нужно узнать язык пользователя - выполняется эта функция
    async def get_user_locale(self, action, args):
        user = types.User.get_current()
        # Возвращаем язык из базы ИЛИ (если не найден) - язык из Телеграма
        return await get_lang(user.id) or user.language_code


def setup_middleware(dp):
    # Устанавливаем миддлварь
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from loguru import logger

from data.config import ADMINS
from handlers.users.broadcast_handler import broadcaster
from keyboards.inline.admin_panel_inline import admin_panel
from loader import dp, db


@dp.message_handler(Command('admin'))
async def check_user(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer(f'Админ добрый день! Что угодно?', reply_markup=admin_panel)
    else:
        await message.answer(f'Попытка взлома бота зафиксирована!')


@dp.callback_query_handler(text='count_users')
async def count_users(call: CallbackQuery):
    count_users = await db.count_users()
    await call.message.answer(f'Количество участников: {count_users}')
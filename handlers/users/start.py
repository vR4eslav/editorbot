from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from asyncpg import UniqueViolationError

from loader import dp, db, _
from utils.misc import rate_limit


@rate_limit(10, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=_('➡️МЕНЮ⬅️'), callback_data='menu')
    btn2 = types.InlineKeyboardButton(text=_('🔹О БОТЕ🔹'), callback_data='about_bot')
    btn3 = types.InlineKeyboardButton(text=_('Поддержать проект'), url='https://www.donationalerts.com/r/vr4eslav')
    btn4 = types.InlineKeyboardButton(text='Язык/Language', callback_data='change_language')
    keyboard.row(btn1, btn2)
    keyboard.add(btn3, btn4)
    name = message.from_user.full_name
    try:
        await db.add_user(full_name=message.from_user.full_name,
                          username=message.from_user.username,
                          telegram_id=message.from_user.id)
    except UniqueViolationError:
        pass
    await message.answer(_("🔆Привет, {name}! Я <b>бот-редактор</b>!🔆\n\n"
                           f"Жми кнопки ниже, чтобы перейти к манипуляциям с текстом!").format(
        name=message.from_user.full_name), reply_markup=keyboard)


@dp.callback_query_handler(text='back_to_menu')
async def bot_start_back(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=_('➡️МЕНЮ⬅️'), callback_data='menu')
    btn2 = types.InlineKeyboardButton(text=_('🔹О БОТЕ🔹'), callback_data='about_bot')
    btn3 = types.InlineKeyboardButton(text=_('Поддержать проект'), url='https://www.donationalerts.com/r/vr4eslav')
    btn4 = types.InlineKeyboardButton(text='Язык/Language', callback_data='change_language')
    keyboard.row(btn1, btn2)
    keyboard.add(btn3, btn4)
    await call.message.edit_text(_("🔆Привет, {name}! Я <b>бот-редактор</b>!🔆\n\n"
                                   f"Жми кнопки ниже, чтобы перейти к манипуляциям с текстом!").format(
        name=call.from_user.full_name), reply_markup=keyboard)


@dp.callback_query_handler(text='change_language')
async def change_language(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='🇷🇺РУССКИЙ🇷🇺', callback_data='set_russian')
    btn2 = types.InlineKeyboardButton(text='🇬🇧ENGLISH🇺🇸', callback_data='set_english')
    btn3 = types.InlineKeyboardButton(text=_('🔙 НАЗАД В МЕНЮ 🔙'), callback_data='back_to_menu')
    keyboard.add(btn1, btn2, btn3)
    await call.message.edit_text('Choose', reply_markup=keyboard)


@dp.callback_query_handler(text='set_russian')
async def set_russian_lang(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    btn2 = types.InlineKeyboardButton(text='🇬🇧ENGLISH🇺🇸', callback_data='set_english')
    btn3 = types.InlineKeyboardButton(text=_('🔙 НАЗАД В МЕНЮ 🔙'), callback_data='back_to_menu')
    keyboard.add(btn2, btn3)
    try:
        await db.update_user_locale(locale='ru', telegram_id=call.from_user.id)
        await call.message.edit_text('🇷🇺Вы выбрали русский язык!✅', reply_markup=keyboard)
    except:
        await call.message.edit_text(f'FAIL')

@dp.callback_query_handler(text='set_english')
async def set_russian_lang(call: CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='🇷🇺РУССКИЙ🇷🇺', callback_data='set_russian')
    btn3 = types.InlineKeyboardButton(text=_('🔙 НАЗАД В МЕНЮ 🔙'), callback_data='back_to_menu')
    keyboard.add(btn1, btn3)
    try:
        await db.update_user_locale(locale='en', telegram_id=call.from_user.id)
        await call.message.edit_text('🇬🇧You have chosen english!✅', reply_markup=keyboard)
    except:
        await call.message.edit_text(f'FAIL')
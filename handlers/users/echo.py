from aiogram import types
from aiogram.dispatcher import FSMContext
from asyncpg import UniqueViolationError

from loader import dp, db


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    try:
        await db.add_user(full_name=message.from_user.full_name,
                          username=message.from_user.username,
                          telegram_id=message.from_user.id)
    except UniqueViolationError:
        pass
    await message.answer(f"⚠️ Ваше сообщение никуда не попало! Попробуйте выбрать необходимую функцию.")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    try:
        await db.add_user(full_name=message.from_user.full_name,
                          username=message.from_user.username,
                          telegram_id=message.from_user.id)
    except UniqueViolationError:
        pass
    await message.answer(f"🔍Вы находитесь в процессе какой-то функции\n"
                         f"⚠️Чтобы выйти из нее, нажмите близжайшую кнопку отмены⬆️, либо выполните эту функцию.\n"
                         f"⚠️Либо введите команду еще раз")

import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import message
from aiogram.utils import exceptions
from loguru import logger

from data.config import ADMINS
from loader import bot, dp, db


async def send_message_broadcast(user_id: int, text: str, disable_notification: bool = False) -> bool:
    """
    Safe messages sender
    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.send_message(user_id, text, disable_notification=disable_notification)
    except exceptions.BotBlocked:
        logger.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        logger.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        logger.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message_broadcast(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        logger.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        logger.exception(f"Target [ID:{user_id}]: failed")
    else:
        logger.info(f"Target [ID:{user_id}]: success")
        return True
    return False


@dp.message_handler(Command('broadcast'), chat_id=ADMINS)
async def broadcaster(msg: types.Message) -> int:
    """
    Simple broadcaster
    :return: Count of messages
    """

    text = msg.get_args()
    count = 0
    users = []
    users_records = await db.select_all_users_id()
    logger.info(users_records)
    for user in users_records:
        user_address = user.get('telegram_id')
        users.append(user_address)

    logger.info(users)
    try:
        for user_id in users:
            if await send_message_broadcast(user_id, text):
                count += 1
            await asyncio.sleep(0.6)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=f"{count} messages successful sent.")
    logger.info(users)
    return count

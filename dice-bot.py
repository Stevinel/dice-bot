import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
from asyncio import sleep

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

BOT = Bot(TELEGRAM_BOT_TOKEN)
DP = Dispatcher(BOT)


@DP.message_handler(commands=["play"])
async def on_message(message: types.Message):
    await BOT.send_message(
        message.from_user.id,
        f"Hello, {message.from_user.username}!\nLet`s play",
    )
    await sleep(1)

    bot_data = await BOT.send_dice(message.from_user.id)
    bot_data = bot_data["dice"]["value"]
    await sleep(4)

    user_data = await BOT.send_dice(message.from_user.id)
    user_data = user_data["dice"]["value"]
    await sleep(4)

    if bot_data > user_data:
        await BOT.send_message(message.from_user.id, "You LOSE")
    elif bot_data < user_data:
        await BOT.send_message(message.from_user.id, "You WIN")
    else:
        await BOT.send_message(message.from_user.id, "TIE")


if __name__ == "__main__":
    executor.start_polling(DP, skip_updates=False)

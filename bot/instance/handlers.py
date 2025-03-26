from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from bot.instance.filters import TextFilter,StartsWithFilter

webhook_dp = Dispatcher()

async def handle_start(message: Message, bot: Bot) -> None:
    chat_id = message.chat.id
    await bot.send_message(
        chat_id=chat_id,
        text="SALOM"
    )



# async def test(message:Message,bot:Bot):
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id=chat_id,text="salom qalaysan")



# webhook_dp.message.register(test, TextFilter(text=["salom"]))
webhook_dp.message.register(handle_start, CommandStart())


async def feed_update(token: str, update: dict):

    try:
        webhook_book = Bot(token=token)
        aiogram_update = types.Update(**update)
        await webhook_dp.feed_update(bot=webhook_book, update=aiogram_update)
    finally:
        await webhook_book.session.close()
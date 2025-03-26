import asyncio
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from django.core.management.base import BaseCommand
from config import settings


class Command(BaseCommand):
    help = "Clear old cache and old requests for the bot."

    def handle(self, *args, **kwargs):
        """
        Clear old cache and old requests for the bot.
        """
        print("Clearing old cache and requests...")
        asyncio.run(self.clear_cache())

    async def clear_cache(self):
        """
        Delete old webhook and clear cache.
        """
        bot = Bot(
            token=settings.BOT_TOKEN, 
            default=DefaultBotProperties(parse_mode="HTML")
        )

        try:
            webhook_info = await bot.get_webhook_info()
            print("Current Webhook Info:", webhook_info)

            if webhook_info.url:
                await bot.delete_webhook(drop_pending_updates=True)
                print("Old webhook deleted.")

            print("Old cache and requests cleared.")
        finally:
            await bot.session.close()

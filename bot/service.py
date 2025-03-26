from bot.instance.handlers import feed_update

class BotService:
    """
    Bot Service class for Telegram bot functionalities.
    """
    @classmethod
    async def feed_update(cls, token: str, update: dict):
        """
        Feed update to the bot
        """
        await feed_update(token, update)

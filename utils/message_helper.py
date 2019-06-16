from datetime import timedelta, datetime
from pytz import timezone
import pytz


async def has_bot_sent_this_message(bot, channel, to_send_message, date_range=timedelta(days=-1)):
    async for message in channel.history(limit=200):
        # fix timezones
        created_at = message.created_at.replace(tzinfo=pytz.utc)
        today = datetime.now(pytz.utc)

        if message.author == bot.user and \
                message.content.lower() == to_send_message.lower() and \
                created_at >= today + date_range:
            return True
    return False

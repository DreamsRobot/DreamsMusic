from pyrogram import Client, filters
from pyrogram.types import Message
from DreamsMusic.utils.stats import get_stats

@Client.on_message(filters.command("stats"))
async def bot_stats(client, message: Message):
    stats = get_stats()
    await message.reply(stats)

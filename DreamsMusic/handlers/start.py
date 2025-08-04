from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_bot(client, message: Message):
    await message.reply("👋 Hello! I'm DreamsMusic bot.\nType /help for commands.")

from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("ping"))
async def ping(client, message: Message):
    await message.reply("🏓 Pong!")

@Client.on_message(filters.command("help"))
async def help_command(client, message: Message):
    await message.reply("Use /play <song name> to play music.\nUse /pause, /resume, /skip, /stop to control.")

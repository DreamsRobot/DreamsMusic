from pyrogram import Client, filters
from pyrogram.types import Message
from DreamsMusic.core.player import MusicPlayer

player = MusicPlayer()

@Client.on_message(filters.command("speed"))
async def set_speed(client, message: Message):
    if len(message.command) != 2:
        return await message.reply("Usage: /speed <value>\nExample: /speed 1.25")

    try:
        speed = float(message.command[1])
    except ValueError:
        return await message.reply("Invalid speed value. Use a number like 1.0, 1.25, 1.5, etc.")

    status = player.set_speed(message.chat.id, speed)
    await message.reply(status)

from pyrogram import Client, filters
from pyrogram.types import Message
from DreamsMusic.core.player import MusicPlayer

player = MusicPlayer()

@Client.on_message(filters.command("seek"))
async def seek_command(client, message: Message):
    if len(message.command) != 2 or not message.command[1].isdigit():
        return await message.reply("Usage: /seek <seconds>")
    
    seconds = int(message.command[1])
    result = await player.seek(message.chat.id, seconds)
    await message.reply(result)

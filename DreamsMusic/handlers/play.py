from pyrogram import Client, filters
from pyrogram.types import Message
from DreamsMusic.core.player import MusicPlayer

player = MusicPlayer()

@Client.on_message(filters.command("play"))
async def play_command(client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("Usage: /play [song name or YouTube link]")
    status = await player.play(query, message.chat.id)
    await message.reply(status)

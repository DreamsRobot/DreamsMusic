from pyrogram import Client, filters
from pyrogram.types import Message
from DreamsMusic.core.player import MusicPlayer

player = MusicPlayer()
loop_status = {}

@Client.on_message(filters.command("loop"))
async def toggle_loop(client, message: Message):
    chat_id = message.chat.id
    status = loop_status.get(chat_id, False)
    loop_status[chat_id] = not status
    player.set_loop(chat_id, loop_status[chat_id])
    await message.reply(f"🔁 Loop {'enabled' if loop_status[chat_id] else 'disabled'} for this chat.")

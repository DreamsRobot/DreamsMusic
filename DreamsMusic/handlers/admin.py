from pyrogram import Client, filters
from pyrogram.types import Message
from DreamsMusic.utils.filters import admin_filter
from DreamsMusic.core.player import MusicPlayer

player = MusicPlayer()

@Client.on_message(filters.command(["pause"]) & admin_filter)
async def pause_music(client, message: Message):
    if player.pause():
        await message.reply("⏸️ Music paused.")
    else:
        await message.reply("❌ Nothing playing.")

@Client.on_message(filters.command(["resume"]) & admin_filter)
async def resume_music(client, message: Message):
    if player.resume():
        await message.reply("▶️ Music resumed.")
    else:
        await message.reply("❌ Nothing to resume.")

@Client.on_message(filters.command(["skip"]) & admin_filter)
async def skip_music(client, message: Message):
    if player.skip():
        await message.reply("⏭️ Skipped to next track.")
    else:
        await message.reply("❌ Queue is empty.")

@Client.on_message(filters.command(["stop", "end"]) & admin_filter)
async def stop_music(client, message: Message):
    if player.stop():
        await message.reply("⏹️ Music stopped.")
    else:
        await message.reply("❌ Nothing to stop.")

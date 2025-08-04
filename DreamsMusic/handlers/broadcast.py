from pyrogram import Client, filters
from pyrogram.types import Message
from DreamsMusic.utils.broadcast import broadcast_to_all

@Client.on_message(filters.command("broadcast"))
async def broadcast_message(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message to broadcast.")
    success, failed = await broadcast_to_all(message.reply_to_message)
    await message.reply(f"📢 Broadcast complete!\n✅ Sent: {success}\n❌ Failed: {failed}")

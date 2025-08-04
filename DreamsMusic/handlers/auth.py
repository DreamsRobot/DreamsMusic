from pyrogram import Client, filters
from pyrogram.types import Message
from DreamsMusic.utils.auth import add_admin, remove_admin, get_admins

@Client.on_message(filters.command("auth"))
async def authorize_user(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /auth [user_id]")
    user_id = int(message.command[1])
    add_admin(user_id)
    await message.reply(f"✅ Authorized user `{user_id}`.")

@Client.on_message(filters.command("unauth"))
async def unauthorize_user(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /unauth [user_id]")
    user_id = int(message.command[1])
    remove_admin(user_id)
    await message.reply(f"🚫 Unauthorized user `{user_id}`.")

@Client.on_message(filters.command("authusers"))
async def list_auth_users(client, message: Message):
    admins = get_admins()
    if not admins:
        return await message.reply("No authorized users.")
    msg = "**Authorized Users:**\n" + "\n".join([f"- `{uid}`" for uid in admins])
    await message.reply(msg)

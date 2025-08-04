from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls.exceptions import AlreadyJoinedError

from DreamsMusic.config import API_ID, API_HASH, SESSION_NAME
from DreamsMusic.utils.logger import log
from DreamsMusic.core.player import player

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)
pytgcalls = PyTgCalls(app)


@pytgcalls.on_stream_end()
async def on_stream_end(_, update: StreamAudioEnded):
    chat_id = update.chat_id
    log(f"Stream ended in {chat_id}")
    await player.on_stream_end(chat_id)


async def join_vc(chat_id):
    try:
        await pytgcalls.join_group_call(chat_id, player.get_input_stream(chat_id))
        log(f"Joined voice chat in {chat_id}")
    except AlreadyJoinedError:
        pass
    except Exception as e:
        log(f"Error joining VC in {chat_id}: {e}")


async def leave_vc(chat_id):
    try:
        await pytgcalls.leave_group_call(chat_id)
        log(f"Left voice chat in {chat_id}")
    except Exception as e:
        log(f"Error leaving VC in {chat_id}: {e}")

import asyncio
from pyrogran import FloodWait
from pyrogram import Client , filters
from pyrogram.types import Message
from helpers.gban_errors import iter_chats
from helpers.basic import get_text
from modules.help import add_command_help

 
@Client.on_message(filters.me & filters.command("gikes", ["~", "!", "°"]))
async def gbroadcast(client: Client, message: Message):
    if xx == get_text(message):
        msg = xx
    elif message.reply_to_message:
        msg = message.reply_to_message
    else:
        return await message.reply_text("Input text or Reply to a message")
    msg_ = await message.reply_text("`Processing..`")
    failed =0
    done =0
    async for x in client.inter.dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST:
                try:
                    await client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWait as kntl:
                    await asyncio.sleep(int(kntl.seconds))
                    await client.send_message(chat, msg)
                    done += 1
                except BaseException:
            failed += 1
    await msg_.edit(
        f"`Message Sucessfully Send To {done} Chats! Failed In {failed} Chats.`"
    )


add_command_help(
    "gikes",
    [
        ["gikes", "Give a Message to Broadcast It."],
    ],
)

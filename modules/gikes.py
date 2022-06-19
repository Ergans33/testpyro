import asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client , filters
from pyrogram.types import Message
from helpers.gban_errors import iter_chats
from helpers.basic import get_text
from modules.help import add_command_help


@Client.on_message(filters.me & filters.command("gikes", ["~", "!", "°"]))
async def gbroadcast(client: Client, message: Message):
    if text_ := get_text(message):
        msg = text_
    elif message.reply_to_message:
        msg = message.reply_to_message.text
    else:
        return await message.edit("`Input text or Reply to a message`")
    msg_ = await message.edit_text("`Processing..`")
    err_str, done_gbroadcast = "", 0
    
    if dialog in client.iter_dialog():
        try:
            await client.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
            failed += 1
            await asyncio.sleep(0.1)
        except Exception as e:
    await msg_.edit(
        f"`Message Sucessfully Send To {done_gbroadcast} Chats! Failed In {e} Chats.`"
    )


    
add_command_help(
    "gikes",
    [
        ["gikes", "Give a Message to Broadcast It."],
    ],
)

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
        msg = message.reply_to_message
    else:
        return await message.reply_text("Input text or Reply to a message")
    msg_ = await message.reply_text("`Processing..`")
    failed =0
    async for dialog in client.iter_dialogs():
        try:
            await client.send_message(msg)
        except:
            failed += 1
    await msg_.edit(
        f"`Message Sucessfully Send To {chat_len-failed} Chats! Failed In {failed} Chats.`"
    )
    


add_command_help(
    "gikes",
    [
        ["gikes", "Give a Message to Broadcast It."],
    ],
)

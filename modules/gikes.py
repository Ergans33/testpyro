import asyncio
from pyrogram import Client , filters
from pyrogram.types import Message
from helpers.gban_errors import iter_chats
from helpers.basic import get_text
from modules.help import add_command_help

    
    
@Client.on_message(filters.me & filters.command("gikes", ["~", "!", "°"]))
async def gbroadcast(client: Client, message: Message):
    msg_ = await message.reply_text("`Processing..`")
    text_ = get_text(message)
    failed = 0
    if message.reply_to_message:
        await msg_.edit("`Input Text or Reply To Message Boss!`")
        return
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    await msg_.edit("`Now Sending To All Chats Possible!`")
    if not chat_dict:
        msg_.edit("`You Have No Chats! So Sad`")
        return
    for c in chat_dict:
        try:
            msg = await message.reply_to_message.copy(c)
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

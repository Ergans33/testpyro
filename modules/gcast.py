import asyncio
from pyrogram import Client , filters
from pyrogram.types import Message
from modules.help import add_command_help



@Client.on_message(filters.me & filters.command("gcast", ["."]))
async def gbroadcast(client: Client, message: Message):
    msg_ = await message.edit_text("`Processing..`")
    failed = 0
    if not message.reply_to_message:
        await msg_.edit("`Reply To Message Boss!`")
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
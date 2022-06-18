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
        msgg = text_
    elif message.reply_to_message:
        msgg = message.reply_to_message()
    else:
        return await message.reply_text("Input text or Reply to a message")
    kk = await message.edit_or_reply("`Processing..`")
    failed =0
    done =0
    async for dialog in client.iter_dialogs():
        try:
            await client.send_message(dialog.chat.id)
            done += 1
        except:
            failed += 1
    await kk.edit(
        f"`Message Sucessfully Send To {done} Chats! Failed In {failed} Chats.`"
    )
    


add_command_help(
    "gikes",
    [
        ["gikes", "Give a Message to Broadcast It."],
    ],
)

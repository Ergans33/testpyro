import asyncio

from pyrogram import filters, Client
from pyrogram.types import Message

from SQL.clients import user
from helpers.lang_utils import get_message as gm
from helpers.chat_database import ChatDB
from modules.help import add_command_help


@Client.on_message(filters.command("gikes") & filters.user(config.OWNER_ID))
async def gcast_(client: Client, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = message.text[7:]
    msg = await message.reply(gm(message.chat.id, "process_gcast"))
    error = success = 0
    gcast_type = ChatDB().get_chat(message.chat.id)[0]["gcast_type"]
    sender = user if gcast_type == "user" else client
    async for dialog in user.iter_dialogs():
        if dialog.chat.type in ["group", "supergroup"]:
            chat_id = dialog.chat.id
            try:
                success += 1
                await asyncio.sleep(3)
                await sender.send_message(chat_id, text)
            except Exception as e:
                print(e)
                error += 1
    return await msg.edit(
        gm(message.chat.id, "success_gcast").format(str(success), str(error))
    )


add_command_help(
    "gikes",
    [
        [".gikes", "Give a Message to Broadcast It."],
        ["/gikes", "Give a message to Broadcast (Sudo-Users)."],
    ],
)

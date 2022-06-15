import asyncio

from pyrogram import filters, Client
from pyrogram.types import Message
from modules.help import add_command_help


@Client.on_message(filters.command("gikes") & filters.user(config.OWNER_ID))
async def gcast_(c: Client, m: Message):
    if m.reply_to_message:
        text = m.reply_to_message.text
    else:
        text = m.text[7:]
    msg = await m.reply(m.chat.id, "process_gcast"))
    error = success = 0
    gcast_type = m.get_chat(m.chat.id)[0]["gcast_type"]
    sender = user if gcast_type == "user" else c
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
        (message.chat.id, "success_gcast").format(str(success), str(error))
    )


add_command_help(
    "gikes",
    [
        [".gikes", "Give a Message to Broadcast It."],
        ["/gikes", "Give a message to Broadcast (Sudo-Users)."],
    ],
)

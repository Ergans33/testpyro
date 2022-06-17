import asyncio
from pyrogram import Client , filters
from pyrogram.types import Message
from modules.help import add_command_help


@Client.on_message(filters.me & filters.command("gikes", ["~", "!", "°"]))
async def chat_broadcast(c: Client, m: Message):
    if m.reply_to_message:
        msg = m.reply_to_message.text.markdown
    else:
        await m.reply_text("Berikan Pesan atau Reply Message Boss")
        return
    
    exmsg = await m.reply_text("Started broadcasting!")
    err_str, done_broadcast = "", 0

    async for dialog in c.iter_dialogs():
        if dialog.chat.type in ["group", "supergroup"]
          try:
                await c.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
                done_broadcast += 1
                await asyncio.sleep(0.1)
          except Exception as e:
            await m.reply_text(f"Message Sucessfully Send To {dialog.chat.id} Chats! Failed In {e} Chat")



add_command_help(
    "gikes",
    [
        ["gikes", "Give a Message to Broadcast It."],
    ],
)

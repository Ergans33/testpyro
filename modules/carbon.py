from pyrogram import Client, filters
from helpers.utility import make_carbon, capture_err
from modules.help import *


@Client.on_message(filters.me & filters.command("carbon", ["~", "!", "°"]) & ~filters.edited)
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Reply to a text message to make carbon."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "Reply to a text message to make carbon."
        )
    m = await message.reply_text("Preparing Carbon")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading")
    await app.send_document(message.chat.id, carbon)
    await m.delete()
    carbon.close()


add_command_help(
    "carbon",
    [
        [
            "carbon", 
            "Reply to text use filter carbon."
        ],
)

from googletrans import Translator
from telepyrobot.setclient import TelePyroBot
from pyrogram import filters
from pyrogram.types import Message
import os
from modules.help import add_command_help

trl = Translator()



@Client.on_message(filters.me & filters.command("tr", "."))
async def translate(c: Client, m: Message):
    if m.reply_to_message and (m.reply_to_message.text or m.reply_to_message.caption):
        if len(m.text.split()) == 1:
            await m.edit_text("Usage: Reply to a message, then `tr <lang>`")
            return
        target = m.text.split()[1]
        if m.reply_to_message.text:
            text = m.reply_to_message.text
        else:
            text = m.reply_to_message.caption
        detectlang = trl.detect(text)
        try:
            tekstr = trl.translate(text, dest=target)
        except ValueError as err:
            await m.edit_text(f"Error: `{str(err)}`")
            return
    else:
        if len(m.text.split()) <= 2:
            await m.edit_text("Usage: `tr <lang> <text>`")
            return
        target = m.text.split(None, 2)[1]
        text = m.text.split(None, 2)[2]
        detectlang = trl.detect(text)
        try:
            tekstr = trl.translate(text, dest=target)
        except ValueError as err:
            await m.edit_text(f"Error: `{str(err)}`")
            return

    await m.edit_text(
        f"Translated from `{detectlang.lang}` to `{target}`:\n`{tekstr.text}`"
    )
    return


add_command_help(
    **Translate**,
    [
        [".tr", "<lang> <text> Give a target language and text as fot args translate to that target."],
        ["Reply a message to translate that.", 
        
            "*text is not uaed when replying to a message"],
        ]
)
            

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
    done =0
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    await msg_.edit("`Now Sending To All Chats Possible!`")
    if not chat_dict:
        msg_.edit("`You Have No Chats! So Sad`")
        return
            await client.send_message(chat, msg)
            await asyncio.sleep(0.1)
            done += 1
        except FloodWait as kntl:
            await asyncio.sleep(int(kntl.seconds))
            await client.send_message(chat, msg)
            done += 1
        except BaseException:
            failed += 1
    await msg_.edit(
        f"`Message Sucessfully Send To {done} Chats! Failed In {failed} Chats.`"
    )
    


add_command_help(
    "gikes",
    [
        ["gikes", "Give a Message to Broadcast It."],
    ],
)

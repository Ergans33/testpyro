import asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client , filters
from pyrogram.types import Message
from helpers.SQL.gmutedb import *
from helpers.basic import *
from modules.help import add_command_help


@Client.on_message(filters.me & filters.command("gmute", ["~", "!", "°"]))
async def gmute_him(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        me_m = await client.get_me()
        me_ = await message.chat.get_member(int(me_m.id))
    if not me_.can_restrict_members:
        try:
            if message.reply_to_message:
                me_ = message.reply_to_message.from_user.id
        return await message.edit("`You Don't Have Permission! To mute`")

    





add_command_help(
    "gmute",
    [
        ["gmute", 
        "To mute someone Globally."],
        [".ungmute", 
        "To Unmute someone Globally."],
    ],
)

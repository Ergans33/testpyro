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
            await message.edit("`You Don't Have Permission! To mute`")
            return
        userz, reason = await get_user_from_client(user)
        if not userz:
            return
        await message.edit("`Berhasil Membisukan Pengguna!`")
        if is_gmuted(user.id) is False:
            await message.edit("`Kesalahan! Pengguna Sudah Dibisukan.`")
    else:
        if reason:
            await message.edit(f"**Dibisukan Secara Global!**\n**Alasan:** `{reason}`")
        else:
            await message.edit("`Berhasil Membisukan Pengguna Secara Global!`")
        try:
            await client.send_message:
                "#GLOBALMUTE\n"
                f"PENGGUNA: [{user.first_name}](tg://user?id={user.id})\n"
                f"GRUP: {gspdr.chat.title}(`{gspdr.chat_id}`)",
            )

        

    
add_command_help(
    "gmute",
    [
        ["gmute", 
        "To mute someone Globally."],
        [".ungmute", 
        "To Unmute someone Globally."],
    ],
)

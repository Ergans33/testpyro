import asyncio
from pyrogram import Client
from pyrogram.types import Message
from config import SUDO_USERS as SUDO_USER



@Client.on_message(filters.user(SUDO_USER) & filters.command("aktif", ["?"]) & filters.me)
async def gajjajay(client: Client, message: Message):
        await message.edit("Peler Ubot Nyala Gess🎃")		

import asyncio
from pyrogram import Client
from pyrogram.types import Message
from config import 



@Client.on_message(filters.user(SUDO_USER) & filters.command(["gangsta", "gang", "gangstar"], ["."]) & filters.me)
async def gajjajay(client: Client, message: Message):
        await message.edit("")		

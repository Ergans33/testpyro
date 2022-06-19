import asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client , filters
from pyrogram.types import Message
from helpers.SQL.gmutedb import *
from helpers.basic import *
from modules.help import add_command_help



@Client.on_message(filters.me & filters.command("gmute", ["~", "!", "°"]))
async def gmute_him(client: Client, message: Message):
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    if not user:
        return await g.edit("`Reply To User Or Mention To Gmute Him`")
    try:
        userz = await client.get_users(user)
        g = await message.edit_text("`Processing..`")
    except:
        return await g.edit(f"`404 : User Doesn't Exists In This Chat !`")
    if not reason:
        reason = "Just_Gmutted!"
    mee= await client.get_me()
    if userz.id == mee.id:
        await g.edit("`Are you kidding with ne`")
        return
    if await is_gmuted(userz.id):
        await g.edit("`Re-Gmute? Seriously? :/`")
        return
    await gmute(userz.id, reason)
    gmu = f"**#Gmutted** \n**User :** `{userz.id}` \n**Reason :** `{reason}`"
    await g.edit(gmu)
    


@Client.on_message(filters.me & filters.command("ungmute", ["~", "!", "°"]))
async def gmute_him(client: Client, message: Message):
    text_ = get_text(message)
    user_ = get_user(message, text_)[0]
    if not user_:
        return await ug.edit("`Reply To User Or Mention To Un-Gmute Him`")
    try:
        userz = await client.get_users(user_)
        ug = await message.edit_text("`Processing..`")
    except:
        return await ug.edit(f"`404 : User Doesn't Exists In This Chat !`")
    mee= await client.get_me()
    if userz.id == mee.id:
        await ug.edit("`Are ya kidding with me`")
        return
    if not await is_gmuted(userz.id):
        await ug.edit("`Un-Gmute A Non Gmutted User? Seriously? :/`")
        return
    await ungmute(userz.id)
    ugmu = f"**#Un-Gmutted** \n**User :** `{userz.id}`"
    await ug.edit(ugmu)


add_command_help(
    "gmute",
    [
        ["gmute", 
        "To mute someone Globally."],
        [".ungmute", 
        "To Unmute someone Globally."],
    ],
)

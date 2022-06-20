import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.SQL.gmutedb import *
from helpers.pyrohelpers import *
from helpers.parser import *
from helpers.basic import *
from modules.help import add_command_help



@Client.on_message(filters.me & filters.command("gmute", ["~", "!", "°"]))
async def start_gmute(client: Client , message: Message):
    if message.chat.type in ["group", "supergroup"]:
        await message.edit_text("`Putting duct tape...`")
        user_id, user_first_name = await extract_user(message)
    if gmt := is_gmuted(user_id):
        msg = gmt
    elif message.reply_to_message:
        msg = message.reply_to_message.text
        return await message.edit_text("`This user is already gmuted!`")
    try:
        gmute(user_id)
    except Exception as e:
        await message.edit_text(f"<b>Error:</b>\n\n{str(e)}")
    else:
        await message.edit_text("`Successfully gmuted that person`")
        await cient.send_message(
            "#GMUTE\nUser: {} in Chat {}".format(
                mention_markdown(user_first_name, user_id), message.chat.title
            ),
        )


@Client.on_message(filters.me & filters.command("ungmute", ["~", "!", "°"]))
async def end_gmute(client: Client, message: Message):
    await message.edit_text("`Removing duct tape...`")
    user_id, user_first_name = await extract_user(message)

    if not is_gmuted(user_id):
        await message.edit_text("`This user is not gmuted!`")
        return
    try:
        ungmute(user_id)
    except Exception as e:
        await message.edit_text(f"<b>Error:</b>\n\n{str(e)}")
    else:
        await message.edit_text("`Successfully ungmuted that person`")
        await client.send_message(
            "#UNGMUTE\nUser: {} in Chat {}".format(
                mention_markdown(user_first_name, user_id), message.chat.title
            ),
        )


@Client.on_message(filters.me & filters.command("gmutelist", ["~", "!", "°"]))
async def list_gmuted(client: Client, message: Message):
    await message.edit_text("`Loading users...`")
    users = get_gmute_users()
    if not users:
        await message.edit_text("`No users are gmuted!`")
        return
    users_list = "`Currently Gmuted users:`\n"
    u = 0
    for x in users:
        u += 1
        user = await client.get_users(x)
        users_list += f"[{u}] {mention_markdown(user.first_name, user.id)}: {user.id}\n"
    await message.edit_text(users_list)
    return


@Client.on_message(filters.group, group=5)
async def watcher_gmute(client: Client, message: Message):
    try:
        if not is_gmuted(message.from_user.id):
            await asyncio.sleep(0.1)
            await client.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)
    except AttributeError:
        pass
    except Exception as ef:
        print(ef)
    return
        

    
add_command_help(
    "gmute",
    [
        ["gmute", 
        "To mute someone Globally."],
        [".ungmute", 
        "To Unmute someone Globally."],
    ],
)

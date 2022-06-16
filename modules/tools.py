import os
import wget
import random
import asyncio

from telegraph import upload_file
from gpytranslate import Translator

from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.errors import RPCError
from pyrogram import * 
from pyrogram.types import *

from helpers.basic import edit_or_reply, get_text, get_user
from helpers.parser import mention_html, mention_markdown

from modules.help import *

from PIL import Image, ImageDraw, ImageFont


# Translate

trl = Translator()


@Client.on_message(filters.me & filters.command("tr", ["~", "!", "°"]))
async def translate(client: Client, message: Message):
    trl = Translator()
    if message.reply_to_message and (
        message.reply_to_message.text or message.reply_to_message.caption
    ):
        if len(message.text.split()) == 1:
            await message.delete()
            return
        target = message.text.split()[1]
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await message.reply_text(f"Error: `{str(err)}`", parse_mode="Markdown")
            return
    else:
        if len(message.text.split()) <= 2:
            await message.delete()
            return
        target = message.text.split(None, 2)[1]
        text = message.text.split(None, 2)[2]
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await message("Error: `{}`".format(str(err)), parse_mode="Markdown" )
            return
    await message.reply_text(f"**Translated:**\n```{tekstr.text}```\n\n**Detected Language:** `{(await trl.detect(text))}`", parse_mode="Markdown" )


# Telegraph

@Client.on_message(filters.command("tgm", ["~", "!", "°"]) & filters.me) 
async def telegraph(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4")
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply_text("not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message, file_name="root/nana/"
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await client.send_message(message.chat.id, document)
    else:
        await message.reply_text(
            f"**Document passed to: https://telegra.ph{response[0]}**",
        )
    finally:
        os.remove(download_location)


# Sangmata

@Client.on_message(filters.command("sg", ["~", "!", "°"]) & filters.me)
async def sg(client: Client, message: Message):
    lol = await edit_or_reply(message, "Processing please wait")
    if not message.reply_to_message:
        await lol.edit("reply to any message")
    reply = message.reply_to_message
    if not reply.text:
        await lol.edit("reply to any text message")
    chat = message.chat.id
    try:
        await client.send_message("@SangMataInfo_bot","/start")
    except RPCError:
        await lol.edit("Please unblock @SangMataInfo_bot and try again")
        return
    await reply.forward("@SangMataInfo_bot")
    await asyncio.sleep(2)
    async for opt in client.iter_history("@SangMataInfo_bot", limit=3):
        hmm = opt.text
        if hmm.startswith("Forward"):
            await lol.edit("Can you kindly disable your privacy settings for good")
            return
        else:
            await lol.delete()
            await opt.copy(chat)


# Clone

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "Peler Userbot")


@Client.on_message(filters.command("clone", ["~", "!", "°"]) & filters.me)
async def clone(client: Client, message: Message):
    text = get_text(message)
    op = await edit_or_reply(message, "`Cloning`")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
            await op.edit("`Whom i should clone:(`")
            return
    
    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
       first_name=f_name,
       bio=c_bio,
    )
    await message.edit(f"**From now I'm** __{f_name}__")


@Client.on_message(filters.command("unclone", ["~", "!", "°"]) & filters.me)
async def revert(client: Client, message: Message):
    await message.edit("`Uncloning`")
    r_bio = BIO

#Get ur Name back
    await client.update_profile(
            first_name=OWNER,
            bio=r_bio,
        )
#Delte first photo to get ur identify
    photos = await client.get_profile_photos("me")
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("`I am back!`")


# Tagall

@Client.on_message(filters.command("tagall", ["~", "!", "°"]) & filters.me)
async def tag_all_users(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = ""
    kek = client.iter_chat_members(message.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    if message.reply_to_message:
        await client.send_message(message.chat.id, text, reply_to_message_id=message.reply_to_message.message_id,
                                  parse_mode="html")
    else:
        await client.send_message(message.chat.id, text, parse_mode="html")



add_command_help(
    "tools",
    [
        [
            "tr", 
            "Translate some text by give a text or reply that text/caption."
        ],
        [
            "tgm", 
            "Reply to Media as args to upload it to telegraph."
        ],
        [
            "tagall",
            "to mention Everyone ",
        ],
        [
            "clone|unclone", 
            "To Clone someone Profile."
        ],
    ],
)

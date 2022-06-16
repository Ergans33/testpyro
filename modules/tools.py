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
            f"**Document passed to: [Telegra.ph](https://telegra.ph{response[0]})**",
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


# Logo

def choose_random_font():
    fonts_ = [
        "https://github.com/DevsExpo/FONTS/raw/main/Ailerons-Typeface.otf",
        "https://github.com/DevsExpo/FONTS/raw/main/Toxico.otf",
        "https://github.com/DevsExpo/FONTS/raw/main/againts.otf",
        "https://github.com/DevsExpo/FONTS/raw/main/go3v2.ttf",
        "https://github.com/DevsExpo/FONTS/raw/main/vermin_vibes.ttf",
    ]
    random_s = random.choice(fonts_)
    return wget.download(random_s)


add_command_help(
    "tools",
    [
        ["tr", "Translate some text by give a text or reply that text/caption."],
        ["tgm", "Reply to Media as args to upload it to telegraph."],
        
        ["clone|unclone", "To Clone someone Profile."],
    ],
)

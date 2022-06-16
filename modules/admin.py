import asyncio
import time
from emoji import get_emoji_regexp

from helpers.PyroHelpers import GetUserMentionable
from helpers.adminHelpers import CheckAdmin, CheckReplyAdmin, RestrictFailed

from pyrogram.errors import UserAdminInvalid
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions, Message
from pyrogram.errors import (
    UsernameInvalid,
    ChatAdminRequired,
    PeerIdInvalid,
    UserIdInvalid,
    UserAdminInvalid,
    FloodWait,
)

from modules.help import add_command_help


# promote|demote

@Client.on_message(filters.group & filters.command("promote", ["~", "!", "°"]) & filters.me)  
async def promotte(client: Client, message: Message):
  if message.chat.type in ["group", "supergroup"]:
    cmd = message.command
    me_m= message.from_user
    me_ = await message.chat.get_member(int(me_m.id))
    if not me_.can_promote_members:
        await message.edit("`Boss, You Don't Have Promote Permission!`")
        return
    can_promo = True
    if can_promo:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[1:]))
                else:
                    usr = await client.get_users(cmd[1])
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[2:]))
                    user_id = usr.id
            except IndexError:
                await message.delete()
                return

            if user_id:
                try:
                    await client.promote_chat_member(
                        message.chat.id,
                        user_id,
                        can_change_info=True,
                        can_delete_messages=True,
                        can_restrict_members=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_manage_voice_chat=True,
                    )

                    await asyncio.sleep(2)
                    await client.set_administrator_title(
                        message.chat.id, user_id, custom_rank
                  )
                    await message.edit_text("promoted due to bribe")
                    await asyncio.sleep(5)
                    await message.delete()
                except UsernameInvalid:
                    await message.edit_text("user_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except PeerIdInvalid:
                    await message.edit_text("peer_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except UserIdInvalid:
                    await message.edit_text("id_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except ChatAdminRequired:
                    await message.edit_text("denied_permission")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except Exception as e:
                    await message.edit_text(f"**Log:** `{e}`")
                    return

    else:
            await message.edit_text("denied_permission")
            await asyncio.sleep(5)
            await message.delete()
  else:
        await message.delete()


@Client.on_message(filters.group & filters.command("demote", ["~", "!", "°"]) & filters.me)  
async def demote(client: Client, message: Message):
  if message.chat.type in ["group", "supergroup"]:
    cmd = message.command
    me_m= message.from_user
    me_ = await message.chat.get_member(int(me_m.id))
    if not me_.can_promote_members:
        await message.edit("`Boss, You Don't Have Promote Permission!`")
        return
    can_promo = True
    if can_promo:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[1:]))
                else:
                    usr = await client.get_users(cmd[1])
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[2:]))
                    user_id = usr.id
            except IndexError:
                await message.delete()
                return

            if user_id:
                try:
                    await client.promote_chat_member(
             message.chat.id,
             user_id,
            is_anonymous=False,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,)
                    await message.edit_text("demoted due to corruption")
                    await asyncio.sleep(5)
                    await message.delete()
                except UsernameInvalid:
                    await message.edit_text("user_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except PeerIdInvalid:
                    await message.edit_text("peer_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except UserIdInvalid:
                    await message.edit_text("id_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except ChatAdminRequired:
                    await message.edit_text("denied_permission")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except Exception as e:
                    await message.edit_text(f"**Log:** `{e}`")
                    return

    else:
            await message.edit_text("denied_permission")
            await asyncio.sleep(5)
            await message.delete()
  else:
        await message.delete()


# pin|unpin

@Client.on_message(filters.command("pin", ["~", "!", "°"]) & filters.me)  
async def pin_message(client: Client, message):
    msg_id=message.message_id
    chat_id=message.chat.id
    if message.reply_to_message == None:
        await client.edit_message_text(chat_id , msg_id , "Shall I pin your head to wall ?")
    else:
        if message.chat.type == "private":
            reply_msg_id=message.reply_to_message.message_id
            await client.pin_chat_message(chat_id , reply_msg_id , both_sides=True)
            await message.edit_text("Done the Job master !")
        else:
            zuzu= await client.get_chat_member(chat_id , "me")
            can_pin=zuzu.can_pin_messages
            if not can_pin:
                await client.edit_message_text(chat_id , msg_id , "Not a admin bruh 🥱") 
            else:         
                reply_msg_id=message.reply_to_message.message_id
                await client.pin_chat_message(chat_id , reply_msg_id)
                await client.edit_message_text(chat_id , msg_id , "Done the Job master !")


@Client.on_message(filters.command("unpin", ["~", "!", "°"]) & filters.me)  
async def unpin_message(client: Client, message: Message):
    msg_id=message.message_id
    chat_id=message.chat.id
    if message.reply_to_message == None:
        await client.edit_message_text(chat_id , msg_id , "Shall I unpin your head from wall ?")
    else:
        if message.chat.type == "private":
            reply_msg_id=message.reply_to_message.message_id
            await client.unpin_chat_message(chat_id , reply_msg_id )
            await client.edit_message_text(chat_id , msg_id , "Done the Job master !")
        else:
            zuzu= await RaiChUB.get_chat_member(chat_id , "me")
            can_pin=zuzu.can_pin_messages
            if can_pin == None:
                await client.edit_message_text(chat_id , msg_id , "Can't pin messages bruh 🥱") 
            else:         
                reply_msg_id=message.reply_to_message.message_id
                await client.unpin_chat_message(chat_id , reply_msg_id)
                await client.edit_message_text(chat_id , msg_id , "Done the Job master !")


# mute|unmute

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)

@Client.on_message(filters.command("mute", ["~", "!", "°"]) & filters.me)  
async def mute(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        me_m =await client.get_me()
        me_ = await message.chat.get_member(int(me_m.id))
        if not me_.can_restrict_members:
         await message.edit("`You Don't Have Permission! To mute`")
         return
        can_mute= True
        if can_mute:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                else:
                    usr = await client.get_users(message.command[1])
                    user_id = usr.id
            except IndexError:
                await message.edit_text("some ooga booga")
                return
            try:
                await client.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=user_id,
                    permissions=mute_permission,
                )
                await message.delete()
            except Exception as e:
                await message.edit_text("`Error!`\n" f"**Log:** `{e}`")
                return
        else:
            await message.edit_text("denied_permission")
    else:
        await message.delete()

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

@Client.on_message(filters.group & filters.command("unmute", ["~", "!", "°"]) & filters.me)  
async def unmute(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        me_m =await client.get_me()
        me_ = await message.chat.get_member(int(me_m.id))
        if not me_.can_restrict_members:
         await message.edit("`You Don't Have Permission! To mute`")
         return
        can_mute= True
        if can_mute:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                else:
                    usr = await client.get_users(message.command[1])
                    user_id = usr.id
            except IndexError:
                await message.edit_text("some ooga booga")
                return
            try:
                await client.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=user_id,
                    permissions=unmute_permissions,
                )
                await message.delete()
            except Exception as e:
                await message.edit_text("`Error!`\n" f"**Log:** `{e}`")
                return
        else:
            await message.edit_text("denied_permission")
    else:
        await message.delete()


# ban|unban

@Client.on_message(filters.group & filters.command("ban", ["~", "!", "°"]) & filters.me)  
async def member_ban(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        chat_id = message.chat.id
        me_m =await client.get_me
        me_ = await message.chat.get_member(int(me_m.id))
        if not me_.can_restrict_members:
         await message.edit("`You Don't Have Ban Permission!`")
         return
        can_ban= True
        if can_ban:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                else:
                    usr = await client.get_users(message.command[1])
                    user_id = usr.id
            except IndexError:
                await message.edit_text("I cant ban a void xD")
                return
            if user_id:
                try:
                    await client.kick_chat_member(chat_id, user_id)
                    await message.delete()
                except UsernameInvalid:
                    await message.edit_text("`invalid username`")
                    return
                
                except PeerIdInvalid:
                    await message.edit_text("`invalid username or userid`")
                    return
                
                except UserIdInvalid:
                    await message.edit_text("`invalid userid`")
                    return
                
                except ChatAdminRequired:
                    await message.edit_text("`permission denied`")
                    return
                
                except Exception as e:
                    await message.edit_text(f"**Log:** `{e}`")
                    return

        else:
            await message.edit_text("`permission denied`")
            return
    else:
        await message.delete()


@Client.on_message(filters.group & filters.command("unban", ["~", "!", "°"]) & filters.me)  
async def member_unban(client: Client, message: Message):
    msg_id=message.message_id
    chat_msg=message.text
    username=None
     
    if "@" in chat_msg:
        index=chat_msg.index("@")     
        chat_msg=str(chat_msg)
        username=chat_msg[index+1:len(chat_msg)]
    else:                   
        username=message.reply_to_message.from_user.id

    chat_id=message.chat.id
    me_m =await client.get_me()
    me_ = await message.chat.get_member(int(me_m.id))
    user_info=await client.get_users(username)
    if me_.can_restrict_members:      
        await client.unban_chat_member(chat_id , username)
        if(user_info.username):
            usercontact=user_info.username
            reply_string="@"+usercontact+" has been picked up from hell 😈"
            await client.edit_message_text(chat_id , msg_id , reply_string)
        else:
            usercontact=user_info.first_name
            reply_string=usercontact+" has been picked up from 😈"
            await client.edit_message_text(chat_id , msg_id , reply_string)
    else:
        reply_string="Noob,you can't unban members 😂 !"
        await client.edit_message_text(chat_id , msg_id , reply_string )


# kick


@Client.on_message(filters.command("kick", ["~", "!", "°"]) & filters.me)
async def kick_user(bot: Client, message: Message):
    if await CheckReplyAdmin(message) and await CheckAdmin(message):
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)

            await bot.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
            )

            await message.edit(f"Goodbye, {mention}.")
        except UserAdminInvalid:
            await RestrictFailed(message)



add_command_help(
    "admin",
    [
        ["promote", "Reply message user to promote admin."
        ],
        ["demote", "Reply message admin to demote."
        ],
        ["pin", "Reply to a message to pin."
        ],
        ["unpin", "Reply to a message to unpin."
        ],
        [".ban", "Bans user for specified hours or indefinitely."
        ],
        [".unban", "Unbans the user."
        ],
        [".mute", "Bans user for specified hours or indefinitely."
        ],
        [".unmute", "Unmutes the user."
        ],
        [".kick", "Kicks the user out of the group."],
    ],
)

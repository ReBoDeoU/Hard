
import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, get_user_from_event

plugin_category = "admin"

# =================== سحــــــل  ===================  #


@jmthon.ar_cmd(
    pattern="سحل(?:\s|$)([\s\S]*)",
    command=("سحل", plugin_category),
)
async def startgmute(event):
    "To mute a person in all groups where you are admin."
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1450865400:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 1397042354:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 668571162:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    
    if event.is_private:
        await event.edit("**♰... قـد تحـدث بعـض المـشاكـل أو الأخـطاء ..♰**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == jmthon.uid:
            return await edit_or_reply(
                event, "**♰... . لمـاذا تࢪيـد سحل نفسـك؟  ..♰**"
            )
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "*♰... غيـر قـادر عـلى جـلب مـعلومات الـشخص ..♰**"
        )
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"**♰... هـذا الشـخص مسحول بـنجاح ..♰**",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خـطأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"** تـم سحل الـمستخـدم بـنجاح  ♰ **",
            )
        else:
            await edit_or_reply(
                event,
                f"** تـم سحل الـمستخـدم بـنجاح  ♰ **",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                " الـسحل\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**السبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                " الـسحل\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)


# =================== رجـــــع نعــــــالــــي  ===================  #


@jmthon.ar_cmd(
    pattern="رجع نعالي(?:\s|$)([\s\S]*)",
    command=("رجع نعالي", plugin_category),
    info={
        "header": "To unmute the person in all groups where you were admin.",
        "description": "This will work only if you mute that person by your gmute command.",
        "usage": "{tr}ungmute <username/reply>",
    },
)
async def endgmute(event):
    "To remove gmute on that person."
    if event.is_private:
        await event.edit("**♰... قـد تحـدث بعـض المـشاكـل أو الأخـطاء ..♰**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == jmthon.uid:
            return await edit_or_reply(event, "**♰... لمـاذا تࢪيـد ترجيع نعالك؟ ..♰**")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "**♰... غيـࢪ قـادࢪ عـلى جـلب مـعلومات الـشخص ..♰**"
        )
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, f"**♰... هـذا الشـخص ماعـنده نعالك اصلا  ..♰**"
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خطـأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"** تـم ترجيع نعالك من الـمستخـدم بـنجاح ♰ **",
            )
        else:
            await edit_or_reply(
                event,
                f"** تـم ترجيع نعالك من الـمستخـدم بـنجاح ♰ **",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "، رجع نعالي\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**السبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                " رجع نعالي\n"
                f"**المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )


# ===================================== #


@jmthon.ar_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


# =====================================  #

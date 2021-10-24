from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import jmthon
from userbot.utils import sudo_cmd

from ..helpers.utils import reply_id


@jmthon.on(admin_cmd(pattern="تواصل ?(.*)"))
@jmthon.on(sudo_cmd(pattern="تواصل ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**- .تواصل + الرساله ...  \n مثـال**   :  `.تواصل  اهلا عندي مشكلة ممكن حلها`"
        )
    chat = "@AG_EEBOT"
    catevent = await edit_or_reply(event, "**- جـارِ ارسال الرساله ... ♰**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2069998420)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**- تحـقق من انـك لم تقـم بحظر البوت @DEOUUBOT .. ثم اعـد استخدام الامـر ..♰**"
            )
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**- عـذراً .. لـم استطـع ايجـاد  نتيـجة♰**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)

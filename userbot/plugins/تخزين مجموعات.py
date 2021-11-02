from telethon import custom, events
from telethon.tl.types import Channel
from telethon.utils import get_display_name

from userbot.Config import Config

if Config.BOTLOG_CHATID:
    tagger = int(Config.BOTLOG_CHATID)

if Config.BOTLOG_CHATID:
    # For Jmthon userbot don't kang   ;!!
    @bot.on(
        events.NewMessage(
            incoming=True,
            blacklist_chats=Config.UB_BLACK_LIST_CHAT,
            func=lambda e: (e.mentioned),
        )
    )
    async def all_messages_catcher(event):
        await event.forward_to(Config.TG_BOT_USERNAME)

        ammoca_message = ""

        jmthon = await event.client.get_entity(event.sender_id)
        if jmthon.bot or jmthon.verified or jmthon.support:
            return

        jmthonm = f"[{get_display_name(jmthon)}](tg://user?id={jmthon.id})"

        where_ = await event.client.get_entity(event.chat_id)

        where_m = get_display_name(where_)
        button_text = " عـرض التـاك ♰"

        if isinstance(where_, Channel):
            message_link = f"https://t.me/c/{where_.id}/{event.id}"
        else:
            message_link = f"tg://openmessage?chat_id={where_.id}&message_id={event.id}"

        ammoca_message += f"- لقـد قام شخص بعمـل تاك اليك\n\n المستخـدم  : {jmthonm}  \n المجموعة : {where_m} \n الرسـالة : [اضغط هنا]({message_link})"
        if tagger is not None:
            await bot.send_message(
                entity=tagger,
                message=ammoca_message,
                link_preview=False,
                buttons=[[custom.Button.url(button_text, message_link)]],
                silent=True,
            )
        else:
            return


# By @DEOOU

import re

from telethon import Button, events
from telethon.events import CallbackQuery

from Jmthon.razan.resources.assistant import *
from Jmthon.razan.resources.mybot import *
from userbot import jmthon

from ..Config import Config

ROZ_IC = "https://telegra.ph/file/38cf46f1c12b36e14b605.mp4"
ROE = "**♰ هـذه هي قائمة اوامـر سـورس ريـك ♰**"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("اوامري") and event.query.user_id == bot.uid:
            buttons = [
                    Button.inline(" 𝒉𝒂𝒔𝒐𝒏𝒊 𝒂𝒍𝒏𝒂𝒋𝒂𝒓 ", data="ROZADM"),
                ],
            ]
            if ROZ_IC and ROZ_IC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ROZ_IC, text=ROE, buttons=buttons, link_preview=False
                )
            elif ROZ_IC:
                result = builder.document(
                    ROZ_IC,
                    title="NNNUU - USERBOT",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="NNNUU - USERBOT",
                    text=ROE,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="!"))
async def repo(event):
    if event.fwd_from:
        return
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(RR7PP, "!")
    await response[0].click(event.chat_id)
    await event.delete()


@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"jmthon0")))
async def _(event):
    await event.edit(ROZADM)

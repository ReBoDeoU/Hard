# ======================================================================================================================================
import os
from datetime import datetime

from userbot import jmthon

from . import hmention, reply_id

"""
try:
    from . import PING_PIC, PING_TEXT
except:
    pass
"""
plugin_category = "tools"

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/827518f0c6de18fd16d53.mp4"
)

JM_TXT = os.environ.get("PING_TEXT") or "︎ ︎"


@jmthon.ar_cmd(
    pattern="د$",
    command=("د", plugin_category),
    info={
        "header": "ستايل حسن",
        "option": "@HASONI_LQ",
        "usage": [
            "{tr}د",
        ],
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(
        event, "<b><i>𝗡𝗘𝗪 𝗦𝗧𝗬𝗟𝗘 🔥</b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>𝗡𝗘𝗪 𝗦𝗧𝗬𝗟𝗘 🔥\n<b> {hmention}</b>︎ ︎ ︎"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html"
        )


# ======================================================================================================================================

import random
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)

from userbot import JMVERSION, StartTime, jmthon

from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "utils"




@jmthon.ar_cmd(
    pattern="السورس$",
    command=("السورس", plugin_category),
)
async def amireallyalive(event):
    "للتـأكد من ان البـوت يعـمـل"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await edit_or_reply(event, "**♰︙جـــار جلـب معلومــات اެلسۅࢪس**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "♰︙"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**᥉َ𝖴᥆ᖇᥴᥱ ძِᥱَ᥆َ𝖴**"
    RR7_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/734639485f00e79f5e6e9.mp4"
    jmthon_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = jmthon_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jmver=JMVERSION,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if RR7_IMG:
        RR7 = [x for x in RR7_IMG.split()]
        PIC = random.choice(RR7)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**الميـديا خـطأ **\nغـير الرابـط بأستـخدام الأمـر  \n .اضففار ALIVEPIC رابط صورتك\n\n**لا يمـكن الحـصول عـلى صـورة من الـرابـط :-** {PIC}",
            )
    else:
        await edit_or_reply(
            event,
            caption,
        )


temp = """-
**{EMOJI} أصـدار سورس ديـو :♰** 7.0.3
**{EMOJI} أصدار البـايثون :♰** 5.0.2
**{EMOJI} الوقـت :♰** {uptime}
**{EMOJI} المسـتخدم:♰** {mention}"""

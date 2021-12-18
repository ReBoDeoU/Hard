import sys
from asyncio.exceptions import CancelledError

from userbot import jmthon

from ..core.logger import logging
from ..core.managers import edit_or_reply
from ..sql_helper.global_collection import (
    add_to_collectionlist,
    del_keyword_collectionlist,
    get_collectionlist_items,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP

LOGS = logging.getLogger(__name__)
plugin_category = "tools"


@jmthon.ar_cmd(
    pattern="تحديث متطور$",
    command=("تحديث متطور", plugin_category),
    info={
        "header": "Restarts the bot !!",
        "usage": "{tr}restart",
    },
    disable_errors=True,
)
async def _(event):
    "Restarts the bot !!"
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "**♰︙جارِ التحــديث سوف نعلمــك بعد الانتهـــاء**",
        )
    RR7PP = await edit_or_reply(
        event,
        "**♰︙جارِ للتحـديث الى اخــر نسـخة من الســورس يرجـى الانتظـار قليلاً . . .**",
    )
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
    try:
        add_to_collectionlist("restart_update", [RR7PP.chat_id, RR7PP.id])
    except Exception as e:
        LOGS.error(e)
    try:
        delgvar("ipaddress")
        await jmthon.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS.error(e)

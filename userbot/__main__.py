import sys
import os
import re
import userbot
from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import jmthon
from .utils import (
    add_bot_to_logger_group,
    autojo,
    autozs,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("")

print(userbot.__copyright__)
print("جميع الحقوق والملفات محفوظة " + userbot.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info(f"جارِ بدء العمل . . .")
    jmthon.loop.run_until_complete(setup_bot())
    LOGS.info(f"انتهى العمل بنجاح !")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()


class CatCheck:
    def __init__(self):
        self.sucess = True


Catcheck = CatCheck()

async def startup_process():
    check = await ipchange()
    if check is not None:
        Catcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("💙❤💙❤💙❤💙❤💙❤💙❤💙❤💙❤💙❤💙")
    print("تم بنجاح تنصيب سورس ديو الرسمي ")
    print(
        " - ارسل  .فحص  للتأكد من البوت\n-  ولعرض اوامر السورس ارسل  .الاوامر\n-  للمزيد من المعلومات ادخل الى مجموعتك في التليجرام"
    )
    print("💙❤💙❤💙❤💙❤💙❤💙❤💙❤💙❤💙❤💙")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return


jmthon.loop.run_until_complete(startup_process())
jmthon.loop.run_until_complete(autozs())
jmthon.loop.run_until_complete(autojo())


if len(sys.argv) not in (1, 3, 4):
    jmthon.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        jmthon.run_until_disconnected()
    except ConnectionError:
        pass

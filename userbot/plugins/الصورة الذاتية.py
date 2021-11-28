from userbot import jmthon

from . import *


@jmthon.on(admin_cmd(pattern="ها"))
@jmthon.on(admin_cmd(pattern="جلب الصورة"))
async def oho(event):
    if not event.is_reply:
        return await event.edit("يجـب عـليك الـرد عـلى صـورة ذاتيـة الـتدمير")
    rr9r7 = await event.get_reply_message()
    await bot.send(
        "me",
        caption=f"""
-تـم جـلب الصـورة بنجـاح ✅
- CH: @DEOOUS
- Dev: @REKHSO
  """,
    )
    await event.delete()


#    جميع الحقوق لمطوري سورس ديو حصريا لهم فقط
#    اذا تخمط الملف اذكر الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة حسن وجيري

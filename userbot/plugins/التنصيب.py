#    جميع الحقوق لمطوري سورس ديو حصريا لهم فقط
#    اذا تخمط الملف اذكر الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة حسن وجيري

from userbot.utils import admin_cmd


@borg.on(admin_cmd("التنصيب"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            "♰︙**مـرحبا بـك عزيـزي** \n♰︙رابط التنصيب و الشرح - [اضغط هنا](t.me/deoous/10)\n♰︙قناة السورس - @DEOOUS"
        )



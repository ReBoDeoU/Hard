import asyncio
from collections import deque

from . import edit_or_reply, jmthon

plugin_category = "fun"


@jmthon.ar_cmd(
    pattern="ثننيخ١خ١زص$",
    command=("ثمثخ٢م٢زص", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}ثخيه٢ز٢خسخ",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "بميخيخ")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jmthon.ar_cmd(
    pattern="ثخي٩ثنصت$",
    command=("ثني٩٢تص", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}يح٩صو١ن",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "خبخيين")
    deq = deque(list("😹🤣😂😹🤣😂"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jmthon.ar_cmd(
    pattern="ن٣خي٩ث$",
    command=("قنث٩صخصت", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}حثخثو٢زص",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "مقمثخي")
    deq = deque(list("😕😞🙁☹️😕😞🙁"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jmthon.ar_cmd(
    pattern="مثمثحصكص$",
    command=("حينسكشكشكس", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}مبحيسككشكش",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "حثح٢مصمسم")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jmthon.ar_cmd(
    pattern="مثخثصمنص$",
    command=("مثصممص", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}ميكيميظ",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "بحح٣ح٢حث")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jmthon.ar_cmd(
    pattern="قلمثخثح٢حب$",
    command=("نثنثخثخثخقلب", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}قلنصمصخصخب",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "قلخثخثخثخب")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jmthon.ar_cmd(
    pattern="ثه٨ييز$",
    command=("ظ٢ظصظص", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}صمسمسن",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "ثخخصخص")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jmthon.ar_cmd(
    pattern="يمصخصخص$",
    command=("ثنينني", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}الارض",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "بنينني")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jmthon.ar_cmd(
    pattern="ينين$",
    command=("ثنينين", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}ينين",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "بنيخخيخي")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@jmthon.ar_cmd(
    pattern="ينينين$",
    command=("نثنينين", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}بتيتيت",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "نينينينيم")
    animation_interval = 0.2
    animation_ttl = range(101)
    await event.edit("ينينيه..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@jmthon.ar_cmd(
    pattern="باريس$",
    command=("باريس", plugin_category),
    info={
        "الامر": "امر تسليه جربه بنفسك",
        "الاستخدام": "{tr}باريس",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "باريس")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("`🇲🇫. . .`")
    animation_chars = [
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
        "💙 M.M.N 💙",
        "❤ M.M.N ❤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])

#DEOOU

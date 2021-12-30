## الواردات المحـتاجة ⚡
```python3
from userbot import jmthon

from ..core.managers import edit_delete, edit_or_reply

plugin_category="extra"
```

### النص الـتكويني للسـورس⚡
```python3
from userbot import jmthon

from ..core.managers import edit_delete, edit_or_reply

plugin_category="extra"

@jmthon.ar_cmd(
    pattern="ديـو(?:\s|$)([\s\S]*)",
    command=("ديـو", plugin_category),
    info={
        "استخدام": "{tr}ديـو",
        "مثال":  "{tr}ديـو هلا",
    },
)
async def hi_buddy(event):
    "Just to say hi to other user."
    input_str= event.pattern_match.group(1)
    if not input_str:
        await edit_delete(event,"No input is found. Use proper syntax.")
        return
    outputtext= f"+-+-+-+-+-+\n|h|e|l|l|o|\n+-+-+-+-+-+\n{input_str}"
    await edit_or_reply(event,outputtext)
```

For more information refer this [DEOU](https://t.me/DEOOUS)

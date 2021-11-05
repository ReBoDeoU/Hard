@jmthon.ar_cmd(
     pattern="كت(?:\s|$)([\s\S]*)",
     command=("كت", plugin_category),)
 async def mention(mention):
     reza = random.choice(kttwerz)
     await edit_or_reply(mention, f"**- {reza}**")

import asyncio
from datetime import datetime
from platform import python_version

from pyrogram import filters
from pyrogram.types import Message
from pyrogram import __version__

from userbot import Ryoko, START_TIME


@Ryoko.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, message: Message):
    txt = (
        f"[@Ryoko-UserBot](https://github.com/AkiyoSayan/RyokoUserBot is Running\n"
        f"-> Current Uptime: `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
        f"-> Python: `{python_version()}`\n"
        f"-> Pyrogram: `{__version__}`"
    )
    await message.edit(txt)

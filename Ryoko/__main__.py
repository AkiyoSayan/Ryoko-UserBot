from pyrogram import idle, Client, filters
from platform import python_version
from pyrogram import __version__
from Ryoko import app, LOGGER
from Ryoko import Ryoko_version
import logging

app.start()
me = app.get_me()
full_info = f"""Ryoko A Telegram Userbot Is Started.
-> Ryoko Version: {Ryoko_version} 
-> Python: {python_version()}
-> Pyrogram Version: {__version__}
"""
print(full_info)
idle()

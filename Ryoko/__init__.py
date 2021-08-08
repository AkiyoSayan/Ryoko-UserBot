import ast
import logging
import os
from configparser import ConfigParser
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from Ryoko import API_ID, API_HASH, SESSION
from pyrogram import Client

# Logging at the start to catch everything

logging.basicConfig(
    format='%(asctime)s - [RyokoUB] - %(levelname)s - %(message)s',
    level=logging.WARNING,
    handlers=[
        TimedRotatingFileHandler('logs/userbot.log', when="midnight", encoding=None,
                                 delay=False, backupCount=10),
        logging.StreamHandler()
    ]
)
LOGS = logging.getLogger(__name__)

name = 'ryoko'

# Extra Details
Ryoko_version = '0.2.0'
Author = 'AkiyoSayan'
Random_Stickers = [
    'CAADAgAD6EoAAuCjggf4LTFlHEcvNAI',
    'CAADAgADf1AAAuCjggfqE-GQnopqyAI',
    'CAADAgADaV0AAuCjggfi51NV8GUiRwI',
]

# Scheduler
scheduler = AsyncIOScheduler()

HELP = {}
CMD_HELP = {}
START_TIME = datetime.now()

# Ryoko's Client
app = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    ryoko_version=Ryoko_version,
    system_version=SYSTEM_VERSION,
    workers=8,
)


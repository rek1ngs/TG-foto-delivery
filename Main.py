from dotenv import load_dotenv, find_dotenv
import asyncio
import logging
import sys
from os import getenv
import os

# from aiogram import Bot, Dispatcher, html
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.types import Message
load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')

#dp = Dispatcher()


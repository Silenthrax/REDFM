# Copyright (C) 2025 by SILENTHREX @ Github, < https://github.com/Silenthrax/REDFM >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
SILENTHREX is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/Silenthrax/REDFM>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
from REDFM import app
from pyrogram import Client, filters
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
from REDFM.core.mongo import db as alexa
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from REDFM.utils.database import get_served_users, get_served_chats


OWNER_ID = 6174058850

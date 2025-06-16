# Copyright (C) 2025 by SILENTHREX @ Github, < https://github.com/Silenthrax/REDFM >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
SILENTHREX is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/Silenthrax/REDFM>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from REDFM.core.bot import AlexaBot
from REDFM.core.dir import dirr
from REDFM.core.git import git
from REDFM.core.userbot import Userbot
from REDFM.misc import dbb, heroku

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Bot Client
app = AlexaBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

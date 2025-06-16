# Copyright (C) 2025 by SILENTHREX @ Github, < https://github.com/Silenthrax/REDFM >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
SILENTHREX is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/Silenthrax/REDFM>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import aiohttp

BASE = "https://batbin.me/"


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def Alexabin(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    return BASE + resp["message"]

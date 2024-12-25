#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7550260070:AAFGOz10GuEKipGuD_dolmJuXS4ORHthva8")
    API_ID = int(os.environ.get("API_ID", "26513107"))
    API_HASH = os.environ.get("API_HASH", "f14ce4b58dc8812cfc9665588472f2d4")
    AUTH_USERS = "1928404158"


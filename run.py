#!/usr/bin/env python3
# -*- coding: latin-1 -*-

import logging
from os import environ as env
from dotenv import load_dotenv
from discordphone.DiscordPhone import DiscordPhone

load_dotenv(dotenv_path='.env')

logging.basicConfig(
    filename='discordphone.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt  = '%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
logger.info(f"Starting DiscordPhone.")

client = DiscordPhone()
client.run(env.get('DISCORD_TOKEN'))

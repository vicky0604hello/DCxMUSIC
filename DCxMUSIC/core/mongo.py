#
# Copyright (C) 2024 by 𓆩𔘓𓆪 𝐕⊶𝐈⊶𝐊⊶𝐑⊶𝐀⊶𝐍⊶𝐓 𓆩𔘓𓆪 Github-@VICKYCHOUDHARY1, 
# < https://github.com/vicky0404hello >.
# <https://github.com/VICKYCHOUDHARY1/DCxMUSIC >
# All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("Connected to your Mongo Database.")
except:
    LOGGER(__name__).error("Failed to connect to your Mongo Database.")
    exit()

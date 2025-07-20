# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "20386593"))
API_HASH = getenv("API_HASH", "51970327f8e01b3409a3102d86f5c3ac")
BOT_TOKEN = getenv("BOT_TOKEN", "8135705187:AAFGcx40XIaQFaEZgLSRUbwo46SPnUEGEzA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7615054801").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mkashinath819:sbAM1CtpNcp1PVx8@lighthouse1.mke6d7j.mongodb.net/?retryWrites=true&w=majority&appName=lighthouse1")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)

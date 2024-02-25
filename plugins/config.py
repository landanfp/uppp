import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "false")
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1943275919:AAFwSScrlR_i-AzdNTOiw8EEctbU_exOaGg")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "3335796" ))
    API_HASH = os.environ.get("API_HASH", "138b992a0e672e8346d8439c3f42ea78")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS").split())
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "false").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001708811948")
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "false")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = "false"
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = "false"
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://abirhasan2005:abirhasan@cluster0.i6qzp.mongodb.net/cluster0?retryWrites=true&w=majority")
    SESSION_NAME = os.environ.get("SESSION_NAME", "upoooo")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001787336960"))
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", "763990585"))
    # Update channel for Force Subscribe
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001787336960")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ir_uploadbot")
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "hi"))
    SCREENSHOTS = os.environ.get("SCREENSHOTS", "True")

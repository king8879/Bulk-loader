from distutils.util import strtobool
import os
from dotenv import load_dotenv
from pyrogram.types import BotCommand


# Load environment variables from .env file
load_dotenv()


class Config(object):

    # Your API HASH
    API_HASH = os.environ.get('22923037')

    # Your API ID
    APP_ID = int(os.environ.get('dfb3666878b3851460a58461c5a50f5b'))

    # Your Bot Token
    BOT_TOKEN = os.environ.get('7463809159:AAG0WIc0l8BvwMKas4TrHfQCuMc43DMMFuo')

    # Your Telegram ID (optional)
    OWNER_ID = os.environ.get('6554343173')

    # Upload method (default to False)
    AS_ZIP = bool(strtobool(os.environ.get('AS_ZIP', 'False')))

    # Channel/Group ID where you dump all the downloaded files.
    DUMP_ID = int(os.environ.get('DUMP_ID')
                  ) if os.environ.get('DUMP_ID') else None

    PLUGINS = {'root': 'Bot.plugins'}

    DOWNLOAD_DIR = "./downloads/"

    BOT_COMMANDS = [
        BotCommand('start', 'start bot'),
        BotCommand('help', 'help messages'),
        BotCommand('thumbnail', 'custom thumbnail'),
        BotCommand('caption', 'custom caption')
    ]

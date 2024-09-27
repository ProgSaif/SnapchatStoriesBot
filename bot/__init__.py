import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "28607871"))
    API_HASH = os.environ.get("API_HASH", "183721dca18fce6ed2877fdcd1066a3a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7373481691:AAHNbVGQNJ25vyPE8JBnadLDmYHxkFliZ58")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "SnapchatStoriesTelegram_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]

from typing import Any, Dict

from moderatelyhelpfulbot.database import Database
from moderatelyhelpfulbot.settings import settings

# Set up some global variables
ACCEPTING_NEW_SUBS = True
LINK_REGEX = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"  # noqa: E501
REDDIT_LINK_REGEX = (
    r"r/([a-zA-Z0-9_]*)/comments/([a-z0-9_]*)/([a-zA-Z0-9_]{0,50})"  # noqa: E501
)
RESPONSE_TAIL = ""
MAIN_SETTINGS: Dict[str, str] = {}
SUBWIKI_CHECK_INTERVAL_HRS = 24
UPDATE_LIST = True

ASL_REGEX = (
    r"((?P<age>[0-9]{2})([/ \\-]?|(\]? \[))(?P<g>[mMFf]{1}))|"
    r"((?P<g2>[mMFf]{1})([/ \\-]?|(\]? \[))(?P<age2>[0-9]{2}))"
)

WATCHED_SUBS: Any = {}

dbobj = Database()
dbobj.load_models()

BOT_SUB = settings["bot_name"]

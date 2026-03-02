import os
from dotenv import load_dotenv

# Load local .env file if it exists (useful for local testing)
load_dotenv()

# --- MANDATORY SETTINGS ---
# We use .get() with a default value so the bot won't crash if the var is missing
BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "8598064539:AAFFDzeNlqPAOdhTvGIizQ9eL2Wp9Tf9jqQ")

# API_ID must be an integer. We convert the string from environment to int.
API_ID: int = int(os.environ.get("API_ID", "27322718"))

# API_HASH must be a string.
API_HASH: str = os.environ.get("API_HASH", "4f6d1b67cf101aea5cf0536885aa1b82")

# --- OPTIONAL / SESSION SETTINGS ---
NDUS_COOKIE: str | None = os.environ.get("NDUS_COOKIE")
SESSION_STRING: str | None = os.environ.get("SESSION_STRING")

# --- DYNAMIC LIMITS ---
_4GB = 4 * 1024 ** 3
_2GB = 2 * 1024 ** 3
# If a session string is provided, assume Premium (4GB), otherwise standard (2GB)
MAX_UPLOAD_SIZE: int = _4GB if SESSION_STRING else _2GB
BOT_API_LIMIT: int = 50 * 1024 ** 2

# --- SYSTEM SETTINGS ---
CACHE_TTL: int = int(os.environ.get("CACHE_TTL", 7200))
LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO").upper()

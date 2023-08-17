import os
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get('BOT_TOKEN', None)
if bot_token is None:
    raise Exception("BOT_TOKEN not found in environment variables")
    exit(1)
bot = Client(
    "my_bot",
    bot_token=bot_token,
    api_id=os.environ.get('API_ID', None),
    api_hash=os.environ.get('API_HASH', None)
)
import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("API_ID", "21580711"))
API_HASH = os.getenv("API_HASH", "7254971c5396721d7e903cdba7950355")
SESSION = os.getenv("BABVaR2ovp0NdBbyzAC8qvUxSYDEII8l7PcOwvfCzCpctL9bOmDYnZ-9RmuLI3_HxUFEk5u1sH25i1-MWjfHY5Dh1eF6N3Dgg3Fh_0ZMhmvkOjsA9CszPriyu9GTSVh4KMGp69hFUcPndvSf8Le5ex_pRhgLtf6ZWHF117TekcYDzu8TjI6QYMJKWVxzC1OqRLkhNW_R7haiToaFbWzu9EcyM7TkDvjHUlkV5-nP2sdpsfkQuLM4f135cQ2lFHs9vkrXW3ABSrHnU8LvjI2xHf0yk1DldeXU9gR4QPaDRh31j4M84fXY49qfOL9hEityRzAMPHAoPDMdTyrYmJV-5VkeAAAAAa0UdWAA")
HNDLR = os.getenv("HNDLR", "!")

contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Musicllllbot"))
call_py = PyTgCalls(bot)

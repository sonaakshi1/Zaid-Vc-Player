import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL, START_PIC
from Zaid.filters import command
from Zaid.command import commandpro
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Zaid.main import bot as Client

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**Hello, My name is 💞Elizabeth💞.A Telegram Music Bot Based Pyrogram.
 Add Me To Ur Chat For and Help and And Support Click On Buttons  ...
💞  These Features A.I Based 
Powered By [𝙎𝙇 𝙈𝙐𝙎𝙄𝘾 𝙈𝘼𝙉𝙄𝘼](https://t.me/SLMuSicMaNia) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💞𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿💞", url=f"https://t.me/deweni2"
                    ),
                    InlineKeyboardButton(
                        "🎀𝗖𝗵𝗮𝘁 𝗚𝗿𝗼𝘂𝗽", url="https://t.me/SLGangChat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=f"https://t.me/MusicOFHuB"
                    ),
                    InlineKeyboardButton(
                        "🔥 𝗚𝗿𝗼𝘂𝗽", url=f"https://t.me/SLMuSicMaNia"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/stats"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/dd9ca2b2122dd68ffab0e.png",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ 💞", url=f"https://t.me/SLMuSicMaNia")
                ]
            ]
        ),
    )


@Client.on_message(command(["wwerepo", "wwesource"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9bfe6b1d04281ea85e280.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://telegra.ph/file/9bfe6b1d04281ea85e280.jpg")
                ]
            ]
        ),
    )

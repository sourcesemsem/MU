
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "Almortagel"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""╭═★⊷⌯⧼[⌞ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⌝](https://t.me/AlmortagelTech)⧽⌯⊶★═╮\n★‹ [⌞ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⌝](https://t.me/AlmortagelTech)\n★‹ [ALMORTAGELِ](https://t.me/ALMORTAGEL_12)\n╰═★⊷⌯⧼[⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⌝](https://t.me/AlmortagelTech)⧽⌯⊶★═╯\n ⍟ Welcome to ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ALMORTAGEL", url=f"https://t.me/ALMORTAGEL_12"), 
                ],[
                    InlineKeyboardButton(
                        "⌞ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⌝⚡️", url=f"https://t.me/AlmortagelTech"),
                ],[
                    InlineKeyboardButton(
                        "للتنصيب راسلني", url=f"https://t.me/ALMORTAGEL_12"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )




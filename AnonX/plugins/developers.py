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

#          
                
@app.on_message(
    command(["المبرمج","سمير","مطور السورس","مبرمج السورس"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10502824e3ec812bf1e85.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𓏺 ʏᴇѕ ɪ'ᴍ ѕᴀᴍɪʀ ˼](https://t.me/DEV_SAMIR)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @DEV_SAMIR ❫
◉ 𝙸𝙳      : ❪ 5680297831 ❫
◉ 𝙱𝙸𝙾    : ❪ صلي علي الحبيب محمد ✨♥ ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᴅᴇᴠ ѕᴀᴍɪʀ", url=f"https://t.me/DEV_SAMIR"), 
                 ],[
                   InlineKeyboardButton(
                        "⌞ 𝚜𝚘𝚞𝚛𝚌𝚎 𝚜𝚎𝚖𝚘 ⌝", url=f"https://t.me/FTTUTY"),
                ],

            ]

        ),

    )

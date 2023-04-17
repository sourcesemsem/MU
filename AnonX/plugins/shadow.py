import asyncio
import os
import re
import requests
from pyrogram import Client, filters
from strings import get_command
from gpytranslate import Translator
from aiohttp import ClientSession
from traceback import format_exc
from strings.filters import command
from telegraph import upload_file
from config import ASS_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


@app.on_message(command(["طباعه","/pr"]))
async def paste_func(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("قم بالرد على الرساله بالأمر `طباعه`")
    r = message.reply_to_message
    if not r.text and not r.document:
        return await message.reply_text("يتم دعم النصوص والمستندات فقط ")
    m = await message.reply_text("لصق ...")
    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit("يمكنك فقط لصق ملفات أصغر من 40 كيلوبايت .")
        if not pattern.search(r.document.mime_type):
            return await m.edit("يمكن لصق الملفات النصية فقط .")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    kb = [[InlineKeyboardButton(text="رابط اللصق", url=link)]]
    try:
        if m.from_user.is_bot:
            await message.reply_photo(photo=link,quote=False,caption="تم نسخ النص",reply_markup=InlineKeyboardMarkup(kb),)
        else:
            await message.reply_photo(photo=link,quote=False,caption="تم نسخ النص",reply_markup=InlineKeyboardMarkup(kb),)
        await m.delete()
    except Exception:
        await m.edit("فتح الرابط", reply_markup=InlineKeyboardMarkup(kb))


@app.on_message(command(["تليجراف", "/tl", "/telegraph"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply("قم بالرد على صوره او فيديو")
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (replied.video and replied.video.file_name.endswith(".mp4") and replied.video.file_size <= 5242880)
        or (replied.document and replied.document.file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")) and replied.document.file_size <= 5242880)):
        return await message.reply("غير مدعوم !")
    download_location = await client.download_media(message=message.reply_to_message,file_name="root/downloads/")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        button_s = InlineKeyboardMarkup([[InlineKeyboardButton("فتح الرابط 🔗", url=f"https://telegra.ph{response[0]}")]])
        await message.reply(f"**الرابط »**\n`https://telegra.ph{response[0]}`",disable_web_page_preview=True,reply_markup=button_s)
    finally:
        os.remove(download_location)

@app.on_message(filters.text)
def quran1(Client, m):
         if m.text == "قران":
          m.reply_photo("https://t.me/Sourcelink1/22", caption="""◍ اختر ما تريد سماعه من القائمه في الاسفل\n\n√""",
          reply_markup=InlineKeyboardMarkup(
            [
        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xf1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xf2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xf3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xf4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xf5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xf6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xf7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xf8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xf9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xf10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xf11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xf12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xf13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xf14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xf15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xf16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xf17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xf18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xf19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xf20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xf21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xf22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xf23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xf24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xf25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xf26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xf27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xf28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xf29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xf30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xf31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xf32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xf33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xf34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xf35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xf36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xf37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xf38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xf39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xf40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xf41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xf42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xf43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xf44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xf45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xf46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xf47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xf48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xf49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xf50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xf51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="fares2 " + str(m.from_user.id))],


        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url="https://t.me/?startgroup=true"),]
        ]
     ),
  )


@app.on_callback_query(filters.regex("^fares (\\d+)$"))
async def fares(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 😌❤️", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xf1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xf2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xf3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xf4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xf5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xf6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xf7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xf8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xf9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xf10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xf11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xf12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xf13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xf14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xf15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xf16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xf17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xf18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xf19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xf20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xf21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xf22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xf23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xf24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xf25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xf26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xf27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xf28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xf29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xf30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xf31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xf32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xf33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xf34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xf35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xf36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xf37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xf38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xf39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xf40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xf41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xf42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xf43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xf44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xf45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xf46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xf47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xf48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xf49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xf50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xf51 " + str(m.from_user.id))],

        [InlineKeyboardButton("التالي ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر ما تريد سماعه من القائمه في الاسفل\n\n√", reply_markup=keyboard, disable_web_page_preview=True)
@app.on_callback_query(filters.regex("^quran2 (\\d+)$"))
async def faress(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 😌❤️", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xf1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xf2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xf3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xf4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xf5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xf6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xf7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xf8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xf9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xf10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xf11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xf12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xf13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xf14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xf15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xf16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xf17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xf18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xf19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xf20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xf21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xf22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xf23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xf24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xf25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xf26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xf27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xf28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xf29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xf30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xf31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xf32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xf33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xf34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xf35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xf36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xf37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xf38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xf39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xf40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xf41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xf42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xf43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xf44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xf45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xf46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xf47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xf48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xf49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xf50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xf51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="fares2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر ما تريد سماعه من القائمه في الاسفل\n\n√", reply_markup=keyboard, disable_web_page_preview=True)


@app.on_callback_query(filters.regex("^fares2 (\\d+)$"))
async def fares2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xf52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xf53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xf54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xf55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xf56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xf57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xf58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xf59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xf60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xf61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xf62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xf63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xf64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xf65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xf66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xf67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xf68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xf69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xf70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xf71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xf72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xf73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xf74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xf75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xf76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xf77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xf78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xf79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xf80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xf81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xf82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xf83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xf84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xf85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xf86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xf87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xf88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xf89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xf90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xf91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xf92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xf93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xf94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xf95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xf96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xf97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xf98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xf99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xf100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xf101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xf102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xf103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xf104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xf105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xf106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xf107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xf108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xf109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xf110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xf111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xf112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xf113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xf114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="fares " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],

    ])
    await m.message.edit_text("◍ اختر ما تريد سماعه من القائمه في الاسفل\n\n√", reply_markup=keyboard, disable_web_page_preview=True)

@app.on_callback_query(filters.regex("^xf1 (\\d+)$"))
async def xf1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/285",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf2 (\\d+)$"))
async def xf2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/286",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf3 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf3 (\\d+)$"))
async def xf3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/287",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf4 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf4 (\\d+)$"))
async def xf4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/288",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf5 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf5 (\\d+)$"))
async def xf5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/289",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf6 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf6 (\\d+)$"))
async def xf6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/290",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf7 (\\d+)$"))
async def xf7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/291",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf8 (\\d+)$"))
async def xf8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/292",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf9 (\\d+)$"))
async def xf9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/293",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf10 (\\d+)$"))
async def xf10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/294",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf11 (\\d+)$"))
async def xf11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/295",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf12 (\\d+)$"))
async def xf12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/296",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf13 (\\d+)$"))
async def xf13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/297",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf14 (\\d+)$"))
async def xf14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/298",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf15 (\\d+)$"))
async def xf15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/299",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf16 (\\d+)$"))
async def xf16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/300",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf17 (\\d+)$"))
async def xf17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/301",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf18 (\\d+)$"))
async def xf18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/302",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf19 (\\d+)$"))
async def xf19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/303",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf20 (\\d+)$"))
async def xf20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/304",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf21 (\\d+)$"))
async def xf21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/305",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf22 (\\d+)$"))
async def xf22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/306",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf23 (\\d+)$"))
async def xf23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/307",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf24 (\\d+)$"))
async def xf24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/308",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf25 (\\d+)$"))
async def xf25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/309",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf26 (\\d+)$"))
async def xf26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/310",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf27 (\\d+)$"))
async def xf27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/311",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf28 (\\d+)$"))
async def xf28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/312",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf29 (\\d+)$"))
async def xf29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/313",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf30 (\\d+)$"))
async def xf30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/314",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf31 (\\d+)$"))
async def xf31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/315",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf32 (\\d+)$"))
async def xf32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/316",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf33 (\\d+)$"))
async def xf33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/317",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf34 (\\d+)$"))
async def xf34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/318",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf35 (\\d+)$"))
async def xf35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/319",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf36 (\\d+)$"))
async def xf36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/320",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf37 (\\d+)$"))
async def xf37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/321",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf38 (\\d+)$"))
async def xf38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/322",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf39 (\\d+)$"))
async def xf39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/323",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf40 (\\d+)$"))
async def xf40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/324",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf41 (\\d+)$"))
async def xf41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/325",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf42 (\\d+)$"))
async def xf42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/326",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf43 (\\d+)$"))
async def xf43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/327",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf44 (\\d+)$"))
async def xf44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/328",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf45 (\\d+)$"))
async def xf45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/329",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf46 (\\d+)$"))
async def xf46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/330",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf47 (\\d+)$"))
async def xf47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/331",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf48 (\\d+)$"))
async def xf48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/332",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf49 (\\d+)$"))
async def xf49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/333",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf50 (\\d+)$"))
async def xf50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/334",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf51 (\\d+)$"))
async def xf51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/335",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf52 (\\d+)$"))
async def xf52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/336",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf53 (\\d+)$"))
async def xf53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/337",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf54 (\\d+)$"))
async def xf54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/338",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf55 (\\d+)$"))
async def xf55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/339",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf56 (\\d+)$"))
async def xf56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/340",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf57 (\\d+)$"))
async def xf57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/341",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf58 (\\d+)$"))
async def xf58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/342",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf59 (\\d+)$"))
async def xf59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/343",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf60 (\\d+)$"))
async def xf60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/344",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf61 (\\d+)$"))
async def xf61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/345",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf62 (\\d+)$"))
async def xf62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/346",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf63 (\\d+)$"))
async def xf63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/347",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf64 (\\d+)$"))
async def xf64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/348",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf65 (\\d+)$"))
async def xf65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/349",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf66 (\\d+)$"))
async def xf66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/350",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf67 (\\d+)$"))
async def xf67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/351",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf68 (\\d+)$"))
async def xf68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/352",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf69 (\\d+)$"))
async def xf69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/353",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf70 (\\d+)$"))
async def xf70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/354",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf71 (\\d+)$"))
async def xf71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/355",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf72 (\\d+)$"))
async def xf72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/356",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf73 (\\d+)$"))
async def xf73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/357",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf74 (\\d+)$"))
async def xf74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/358",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf75 (\\d+)$"))
async def xf75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/359",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf76 (\\d+)$"))
async def xf76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/360",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf77 (\\d+)$"))
async def xf77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/361",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf78 (\\d+)$"))
async def xf78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/362",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf79 (\\d+)$"))
async def xf79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/363",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf80 (\\d+)$"))
async def xf80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/364",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf81 (\\d+)$"))
async def xf81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/365",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf82 (\\d+)$"))
async def xf82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/366",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf83 (\\d+)$"))
async def xf83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/367",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf84 (\\d+)$"))
async def xf84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/368",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf85 (\\d+)$"))
async def xf85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/369",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf86 (\\d+)$"))
async def xf86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/370",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf87 (\\d+)$"))
async def xf87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/371",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf88 (\\d+)$"))
async def xf88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/372",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf89 (\\d+)$"))
async def xf89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/373",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf90 (\\d+)$"))
async def xf90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/374",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf91 (\\d+)$"))
async def xf91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/375",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf92 (\\d+)$"))
async def xf92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/376",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf93 (\\d+)$"))
async def xf93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/377",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf94 (\\d+)$"))
async def xf94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/378",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf95 (\\d+)$"))
async def xf95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/379",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf96 (\\d+)$"))
async def xf96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/380",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf97 (\\d+)$"))
async def xf97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/381",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf98 (\\d+)$"))
async def xf98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/382",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf99 (\\d+)$"))
async def xf99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/383",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf100 (\\d+)$"))
async def xf100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/384",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf101 (\\d+)$"))
async def xf101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/385",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf102 (\\d+)$"))
async def xf102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/386",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf103 (\\d+)$"))
async def xf103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/387",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf104 (\\d+)$"))
async def xf104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/388",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf105 (\\d+)$"))
async def xf105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/389",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf106 (\\d+)$"))
async def xf106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/390",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf107 (\\d+)$"))
async def xf107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/391",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf108 (\\d+)$"))
async def xf108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/392",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf109 (\\d+)$"))
async def xf109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/393",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf110 (\\d+)$"))
async def xf110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/394",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf111 (\\d+)$"))
async def xf111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/395",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf112 (\\d+)$"))
async def xf112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/396",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf113 (\\d+)$"))
async def xf113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/397",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


@app.on_callback_query(filters.regex("^xf114 (\\d+)$"))
async def xf114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/U5iAR2/398",
                                caption="◍ اليك ما اختارت\n√",
                                reply_markup=InlineKeyboardMarkup(
        [
        [InlineKeyboardButton("➡️ التالي", callback_data="xf2 " + str(m.from_user.id))],
        [InlineKeyboardButton("رجوع ➡️", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/?startgroup=new")],
]
                                ))


########################################################################################################################
########################################################################################################################

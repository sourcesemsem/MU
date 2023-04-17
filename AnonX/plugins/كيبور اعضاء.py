import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "**👋︙مـرحـبـا بـك عـزيـزي العـضـو ♥️**\n**✨︙فــي ازرار التسـليـه لـلـبـوت💞**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("‹ رمزيات شباب ›"),
    ],
    [
        ("𝚍𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛")
    ],
    [
        ("⌔حـروف⌔"),
        ("⌔صـراحـه⌔")
    ],
    [
        ("⌔لـو خـيـروك⌔"),
        ("⌔تـويـت⌔")
    ],
    [
        ("نبذه عن الكيبورد ⚡")
    ],
    [
        ("⌔اذكـار⌔"),
        ("⌔يـوتـيـوب⌔")
    ],
    [
        ("⌔ايــدي⌔"),
        ("⌔اسـمـي⌔")
    ],
    [
        ("⌔كـتـبـات⌔"),
        ("⌔انـصـحـنـي⌔")
],
[

("‹ اغلاق الكيب ›")

    ]
]

@app.on_message(
    filters.command("semo")
    & filters.private
)
async def music(client: Client, message: Message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


@app.on_message(filters.regex("︙اراج︙"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/bed2cbf98e17acf79530b.jpg",
        caption=f"""**نبذه سريعه عن الابراج** : **يتم استخدام هذا الامر لعرض الابراج فقط🫡**\n**استخدم الامر بهذا الشكل** `ابراج` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 👨‍💻︙قـنـاة الـسـورس 𓆪", url=f"https://t.me/source_av"),
            ]
         ]
     )
  )



@app.on_message(filters.regex("𝚍𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝚊𝚟𝚊𝚝𝚊𝚛"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/2d528b264da5e71361cd4.jpg",
        caption=f"""**sᴏᴜʀᴄᴇ avatar ᴘʀᴏɢʀᴀᴍᴍᴇʀ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀ𖣩** : **ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴘʀᴏɢʀᴀᴍᴍɪɴɢ ʜᴏʙʙʏɪsᴛ父**\n**avatar メ` **contact with me 𖡰**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )
  

@app.on_message(filters.regex("ـوف⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/390a9dc663f89bd288a58.jpg",
        caption=f"""**نبذه سريعه عن الاحرف** : **يتم استخدام هذا الامر لعرض لعبه جماد حيوان نبات فقط🫡**\n**استخدم الامر بهذا الشكل** `حروف` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔صـراـه⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/98cc55f827723bbb861aa.jpg",
        caption=f"""**نبذه سريعه عن صراحه** : **يتم استخدام هذا الامر لعرض لعبه الصراحه فقط🫡**\n**استخدم الامر بهذا الشكل** `صراحه` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔لـو ـيـروك⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/fec5d804e012a42ab752f.jpg",
        caption=f"""**نبذه سريعه عن لو خيروك** : **يتم استخدام هذا الامر لعرض لعبه لو خيروك فقط🫡**\n**استخدم الامر بهذا الشكل** `لو خيروك` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔تـيـت⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/17909e0dd1dfe7db5781a.jpg",
        caption=f"""**نبذه سريعه عن كت تويت** : **يتم استخدام هذا الامر لعرض لعبه كت تويت فقط🫡**\n**استخدم الامر بهذا الشكل** `كت تويت` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔ك تـبـات⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/11bb465f33e166f0cd368.jpg",
        caption=f"""**نبذه سريعه عن الكتبات** : **يتم استخدام هذا الامر لعرض الكتبات فقط🫡**\n**استخدم الامر بهذا الشكل** `كتبات` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔انـحـنـي⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/809ac511631bbe59f3fc5.jpg",
        caption=f"""**نبذه سريعه عن انصحني** : **يتم استخدام هذا الامر لعرض انصحني فقط🫡**\n**استخدم الامر بهذا الشكل** `انصحني` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔يـوتـوب⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph//file/4fd069c338549431cb4be.jpg",
        caption=f"""**نبذه سريعه عن تنزيل** : **يتم استخدام هذا الامر لعرض تحميل من اليوتيوب فقط🫡**\n**استخدم الامر بهذا الشكل** `تنزيل` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔اكـار⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/1c70887e1c47cd3955780.jpg",
        caption=f"""**نبذه سريعه عن الاذكار** : **يتم استخدام هذا الامر لعرض الاذكار فقط🫡**\n**استخدم الامر بهذا الشكل** `اذكار` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔ايــي⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/27592a96ccf0cef6e3b14.jpg",
        caption=f"""**نبذه سريعه عن الايدي** : **يتم استخدام هذا الامر لعرض الايدي فقط🫡**\n**استخدم الامر بهذا الشكل** `ايدي` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("⌔امـي⌔"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/957139fa5dcbc0d62964b.jpg",
        caption=f"""**نبذه سريعه عن اسمي** : **يتم استخدام هذا الامر لعرض اسمي فقط🫡**\n**استخدم الامر بهذا الشكل** `اسمي` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )


@app.on_message(filters.regex("نبذه عن البورد ⚡"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/e9693c7b78f459e1a00a0.jpg",
        caption=f"""**نبذه سريعه عن** نبذه عن الكيبورد ⚡ **: **ماهو افاتار كيبورد🤔** **هو اصدار اولي قابل لتعديل في اي وقت قابل الاضافة مميزات واضافة جديد في اي وقت بي اختصار قابل لتحديث ولاضافه في اي وقت**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ メ", url=f"https://t.me/DIV_MUHAMED"),
            ]
         ]
     )
  )
  


@app.on_callback_query(filters.regex("‹ اغلاق الكيب ›"))
async def italy(_, query: CallbackQuery):
   await callback_query.edit_message_caption(caption =f"""**♬ تــم حــذف الــڪــيــبــورد .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "semo", url=f"https://t.me/FTTUTY"),
               ],
            ]
        ),
    )

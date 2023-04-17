import asyncio
import datetime
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from AnonX.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(filters.regex("^$"))
async def khalid(client: Client, message: Message):
    user = message.from_user.mention
    await message.reply_text(f"""**اهلين {user} !\n- اضغط الزر عشان تشوف اوامر سيمو**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "الاوامر", callback_data=f"am"),
                ],
            ]
        ),
    )



@app.on_message(filters.regex("^سيمو الاحصائيات$") & filters.user(5680297831))
async def ahtek(client: Client, message: Message):
    m_reply = await message.reply_text(f"**✧ اهلين مطوري ارحب\n- هذي احصائيات سيمو ياعيني :\n\n-› عدد المشتركين : 12478\n-› عدد المجموعات : 11346\n\n• تم زيادة 1204 مشترك ونقص 2103 مجموعة  في اخر 24 ساعة\n\n- عدد الطرد من بوتات اخرى : 843\n- طرد يدوي : 1302\n\n╼╾**")
    await m_reply_text("")


@app.on_message(filters.command("","الـتـحديـثـات"))
def vgdg(client,message):
        message.reply_text(
            f"""• هلا عـمࢪي 🤍.\n\n• المطوࢪ -› [ ㅤ𓏺 ժᥱ᥎ ᥉ᥲ️ꪔᎥٍᖇ . 🕷 ˼](t.me/DEV_SAMIR)\n\n• قناة التحديثات -› [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](t.me/FTTUTY)""", 
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "اضـف الـبـوت لـمجـمـوعـتـڪ ✅.", url=f"https://t.me/semo15sbot?startgroup=true")
                    ]
                ]
            ),
            disable_web_page_preview=True

        )




@app.on_message(filters.regex("^بوت حذف$"))
async def delet(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين ياحلو\n-› هذي روابط حذف جميع مواقع التواصل بالتوفيق**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• Telegram •", url=f"https://my.telegram.org/auth?to=delete"),
                    InlineKeyboardButton(
                        "• Instagram •", url=f"https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/"),
                ],[
                    InlineKeyboardButton(
                        "• Snapchat •", url=f"https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount"),
                    InlineKeyboardButton(
                        "• Facebook •", url=f"https://www.faecbook.com/help/deleteaccount"),
                ],[
                    InlineKeyboardButton(
                        "• Twitter •", url=f"https://mobile.twitter.com/settings/deactivate"),

                ],
            ]
        ),
    )


@app.on_message(filters.command("^مطوري$", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(-1001836799321, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- يوزره @{user_ab}\n- ايدي القروب {message.chat.id}\n- يوزر القروب {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(
        f"""- **ابشر ياعيوني ارسلت للمطور بيخش القروب ويشوف مشكلتك بأقرب وقت\n\n- تابع قناة البوت عشان تشوف التحديثات** -› [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](t.me/FTTUTY)""", disable_web_page_preview=True     
    )


REPLY_MESSAGE = "مرحبا بڪ في قـائـمـة ازرار البـوت ✅ ."




REPLY_MESSAGE_BUTTONS = [

         [

             ("كيفية استخدام البوت"),                   

             ("اوامر سيمو")




          ],

          [

             ("مطوري"),

             ("الـتـحديـثـات")

          ],

          [

             ("اخفاء الازرار")

          ]

]




  

@app.on_message(filters.regex("^/samir$"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("^‹ اغلاق الكيب ›$"))
async def down(client, message):
          m = await message.reply(" **- تم اخفاء الازرار بنجاح 🥀\n\n- لعرض الاوامر مره اخري اكتب /samir 🥀** ", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.regex("^كيفية استخدام البوت$"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f""" طـريـقـة إضـافـة البـوت 🇪🇬\n\nتعمل جروب او قناة وبعدين تضيف البوت ✅️ \n\nوترفع البوت مشرف بصلاحية دعوه مستخدمين  👑\n\nوبعدين تضغط ع ال 3 نقط اللي فوق ع اليمين 👌\n\nوتعمل بدأ محادثه صوتيه 🫶\n\nمحتاج اي مساعده راسلني @DEV_SAMIR 🧩\n\nيوزر البوت @SEMO15SBOT 🔊 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "ㅤ𓏺 ժᥱ᥎ ᥉ᥲ️ꪔᎥٍᖇ . 🕷 ˼", user_id=5680297831),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتڪ ✅", url=f"https://t.me/semo15sbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.regex("^مطوري$"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f""" **• اهـلا بڪ عـزيزي  

• لو تريد تنصب تواصل مع مطور السورس

• عندك استفسار او اقتراح بخصوص البوت 

• تواصل مع مطور البوت**

• مطور السورس -› [ㅤ𓏺 ժᥱ᥎ ᥉ᥲ️ꪔᎥٍᖇ . 🕷 ˼](t.me/DEV_SAMIR)

• قناة السورس -› [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](https://t.me/FTTUTY) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼", url=f"https://t.me/FTTUTY"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتڪ ✅", url=f"https://t.me/semo15sbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



REPLY_MESSAGEE = " - مرحبا بڪ في قسم اوامر البوت"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("شرح استخدام البوت")
          ],
          [
             ("اوامر المجموعة"),
             ("اوامر القنوات")
          ],
          [
             ("طريقة التنزيل"),
             ("طريقة ربط القنوات")
          ],
          [
             ("حفظ التشغيل")             
          ],
          [
             ("")
          ],
          [
            ("اخفاء الازرار")
          ]
]

  
@app.on_message(filters.regex("^اوامر سيمو$"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.group & command(""))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.regex("^شرح استخدام البوت$"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""• اي حد هيستخدم البوت يقࢪا كويس 

• علشان لو مش بتعرف تستخدم بوتات 🥀

•طـريـقـة إضـافـة البـوت :[إضغط هناا](https://t.me/GTTUTT/5) 

• طريقة التشغيل بعد الإضافة :  [إضغط هناا](https://t.me/GTTUTT/6) 

• طريقة تنزيل اي شئ تريده :[إضغط هنا](https://t.me/GTTUTT/7) 

• لو انت بتدرس او عندك جروب :[إضغط هناا](https://t.me/GTTUTT/8)

• اي مشكله او تعرف معلومات اكتر كلمني

• يوزر المطور @DEV_SAMIR 🎸

• يوزر البوت @SEMO15SBOT 👀

- [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](t.me/FTTUTY)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتڪ ✅ .", url=f"https://t.me/semo15sbot?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.regex("^اوامر المجموعة$"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n╭── • [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](t.me/FTTUTY) • ──╮\n\n ✧ **اوامر التشغيل بالمجموعة**\n\n• **تشغيل او شغل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• ** انهاء او  ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **تخطي**\n-› لتشغيل التالي بالانتظار\n\n ╰── • [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](t.me/FTTUTY) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼", url=f"https://t.me/FTTUTY"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتڪ ✅ ", url=f"https://t.me/semo15sbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.regex("^اوامر القنوات$"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n╭── • [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](t.me/FTTUTY) • ──╮\n\n ✧ **اوامر التشغيل بالقنوات**\n\n• **تشغيل او شغل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• ** انهاء او  ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **تخطي**\n-› لتشغيل التالي بالانتظار\n\n ╰── • [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](t.me/FTTUTY) • ──╯""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼", url=f"https://t.me/FTTUTY"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتڪ ✅ ", url=f"https://t.me/semo15sbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.regex("^طريقة التنزيل$"))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f""" مرحبا بك في قسم التحميل 🎸

للبحث عن اغنية او فيديو استخدم الامر

التالي ↓

[ تنزيل + اسم المطلوب .]

مثال -› بحث بحبك وحشتني

- [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](t.me/FTTUTY)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼", url=f"https://t.me/FTTUTY"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتڪ ✅ ", url=f"https://t.me/semo15sbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.regex("^حفظ التشغيل$"))
async def dowhmr(client: Client, message: Message):
    await message.reply_text(f"""✧ **اهلين فيك في قسم حفظ التشغيل**\n\n- **حفظ التشغيل هو حفظ الاغاني الي اشتغلت بالمجموعة وحفظها يعني انك تقدر تشغلها بدون ما ترجع تبحث عنها مرة ثانية وتبقى محفوظة لك فقط**\n\n- عشان تحفظ الاغنية او المُشغل الحالي بالمكالمة لازم تضغط على زر -› ( **حفظ التشغيل** )\n\n- عشان تشوف الاغاني او الصوتيات الي حفظتها اكتب امر -› ( **قائمة تشغيلي** )\n\n- وطريقة تشغيل قائمتك تكتب فقط امر -› ( **تشغيل قائمتي** )\n\n- طريقة حذف اغنية او مقطع من محفوظاتك تكتب امر -› ( **حذف تشغيلي** ) وتكمل الخطوات بخاص البوت ..\n\n✶ **ملاحظة : اذا حفظت اغنية بتكون محفوظة عندك فقط يعني كل شخص عنده قائمة تشغيل خاصة فيه ومحد يقدر يحفظ اغنية عندك والعكس ايضا❤️**

- [𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼](t.me/FTTUTY)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼", url=f"https://t.me/FTTUTY"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتڪ ✅ ", url=f"https://t.me/semo15sbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.regex("^طريقة ربط القنوات$"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- هلا والله\n◌**عشان تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓏺 ᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆ . 🕷 ˼", url=f"https://t.me/FTTUTY"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتڪ ✅ ", url=f"https://t.me/semo15sbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

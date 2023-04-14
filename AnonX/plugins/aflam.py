"""
        [InlineKeyboardButton("◁", callback_data="Yrw1 " + str(m.from_user.id))],
        [InlineKeyboardButton("➡️ التالي", callback_data="Yrw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝐇𝐎𝐌", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("⌞ 𝚜𝚘𝚞𝚛𝚌𝚎 𝚜𝚎𝚖𝚘 ⌝⚡", url=f"https://t.me/FTTUTY")],
"""

import asyncio

from strings import get_command
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from AnonX import app



#########################################################################################
#########################################################################################
#########################         # Aflam Arabic #             ##########################
#########################################################################################
#########################################################################################

# Replay Text

@app.on_message(
    command(["افلام"])
    & ~filters.edited
)
async def aflamAR(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("افلام 🎬", callback_data="film " + str(m.from_user.id))],
        [InlineKeyboardButton("مسلسلات 📼", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("مسرحيات 🎭 ", callback_data="msrahia " + str(m.from_user.id))],

        [InlineKeyboardButton("⌞ 𝚜𝚘𝚞𝚛𝚌𝚎 𝚜𝚎𝚖𝚘 ⌝⚡", url=f"https://t.me/FTTUTY")],

    ])
    await m.reply_text("◍ اهلا بيك في قائمة الافلام والمسلسلات العربيه\n√", reply_markup=keyboard)


# Replay Edit
@app.on_callback_query(filters.regex("^aflamAR2 (\\d+)$"))
async def aflamAR2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("افلام 🎬", callback_data="film " + str(m.from_user.id))],
        [InlineKeyboardButton("مسلسلات 📼", callback_data="moslsl " + str(m.from_user.id))],
        [InlineKeyboardButton("مسرحيات 🎭 ", callback_data="msrahia " + str(m.from_user.id))],

        [InlineKeyboardButton("⌞ 𝚜𝚘𝚞𝚛𝚌𝚎 𝚜𝚎𝚖𝚘 ⌝⚡", url=f"https://t.me/FTTUTY")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام والمسلسلات العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^film (\\d+)$"))
async def film(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("كوميدي 😹", callback_data="comedy " + str(m.from_user.id))],
        [InlineKeyboardButton("اكشن 🔥", callback_data="action " + str(m.from_user.id))],
        [InlineKeyboardButton("دراما 🌚", callback_data="drama " + str(m.from_user.id))],

        [InlineKeyboardButton("𝐇𝐎𝐌", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌞ 𝚜𝚘𝚞𝚛𝚌𝚎 𝚜𝚎𝚖𝚘 ⌝⚡", url=f"https://t.me/FTTUTY")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام العربيه\n√", reply_markup=keyboard)


#########################################################################################
#########################################################################################
#########################         # Aflam Comedy #             ##########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^comedy (\\d+)$"))
async def comedy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ وقفة رجاله", callback_data="Xco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الخطة العايمة", callback_data="Xco2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بنات ثانوي", callback_data="Xco3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ عفريت ترانزيت", callback_data="Xco4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ زكي شان", callback_data="Xco5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سمير وشهير وبهير", callback_data="Xco6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تصبح علي خير", callback_data="Xco7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بابا", callback_data="Xco8 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جدو نحنوح", callback_data="Xco9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سمير ابو النيل", callback_data="Xco10 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ كلبي دليلي", callback_data="Xco11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بنات العم", callback_data="Xco12 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ علي بابا", callback_data="Xco13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ فول الصين العظيم", callback_data="Xco14 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حسن وبقلظ", callback_data="Xco15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الكويسين", callback_data="Xco16 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ يوم مالوش لازمه", callback_data="Xco17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ غبي منه فيه", callback_data="Xco18 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ خير وبركه", callback_data="Xco19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ البدله", callback_data="Xco20 " + str(m.from_user.id))],

        [InlineKeyboardButton("𝐇𝐎𝐌", callback_data="film " + str(m.from_user.id))],
        [InlineKeyboardButton("⌞ 𝚜𝚘𝚞𝚛𝚌𝚎 𝚜𝚎𝚖𝚘 ⌝⚡", url=f"https://t.me/FTTUTY")],

    ])
    await m.message.edit_text("◍ اهلا بك في قائمة الافلام الكوميدي العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco1 (\\d+)$"))
async def Xco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco2 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : وقفة رجالة
    📖 انتاج سنة : 2021
    🌎 الدولة : مصر
    🗄 تصنيف : كوميدي
    📜 قصة الفيلم:
    تدور أحداث العمل في قالب كوميدي حول مجموعة من الأصدقاء الذين يجتمعون بعد سنوات لمساعدة أحدهم في الخروج من ورطة كبيرة، وتتطوّر الأحداث فتقودهم للسفر إلى إحدى المدن الساحلية.
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco2 (\\d+)$"))
async def Xco2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco4 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : الخطة العايمة
        📖 انتاج سنة  : 2020
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        في إطار كوميدي لايت تدور الأحداث حول أحد الأشخاص يتطلع إلى سرقة أحد البنك لوجود أوراق هامة في الخزانة، فيتفق مع (جلال وياسمين) لتولي المهمة، واللذان يختاران اللصان الساذجان (حمزون وعلى الله) لتنفيذ تلك المهمة، ويبدآن في تدريبهما.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco3 (\\d+)$"))
async def Xco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco6 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بنات ثانوي
         انتاج سنة : 2020
        🌎 الدولة : مصر
        🗄 تصنيف : دراما, كوميدي, رومانسي
        📜 قصة الفيلم:
        تدور أحداث الفيلم حول فترة المراهقة، حيث تبحث خمس فتيات في مرحلة المراهقة عن ذواتهن وشخصياتهن، ليقعن في العديد من المتاعب والصعاب خلال مرحلة الدراسة الثانوية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco4 (\\d+)$"))
async def Xco4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco8 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : عفريت ترانزيت
        📖 انتاج سنة : 2020
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        يتناول العمل قصة بائع مخدرات يتعرض للعديد من المشاكل واتهامه في جريمة قتل، الأمر الذي يدفعه لمحاولة البحث عن براءته والسير في طريق التوبة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco5 (\\d+)$"))
async def Xco5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco9 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco10 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : زكي شان
        📖 انتاج سنة  : 2005
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        زكي شاب كثير المشاكل سواء مع أفراد أسرته أو في عمله، يعلم أن رب عمل والده يرغب في تعيين بودي جارد كي يحرس ابنه وابنته، ويقرر التقدم للوظيفة رغم عدم ملائمته جسديًا للوظيفة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco6 (\\d+)$"))
async def Xco6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco12 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : سمير وشهير وبهير
        📖 انتاج سنة  : 2010
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي, رومانسي
        📜 قصة الفيلم:
        ثلاثة أخوة لنفس الأب؛ ولكن لأمهات مختلفة هم  (سمير)، ويعمل دوبلير فى السينما، و (شهير) يحب الموسيقي ومعروف بعلاقاته النسائية المتعددة، (بهير) وهو ابن لأسرة أرستقراطية. نتيجة سوء تعامل مع إحدى آلآت الزمن يسافروا عبر الزمن إلى اليوم الذي قابل فيه والدهم الأمهات الثلاثة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco7 (\\d+)$"))
async def Xco7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco14 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : تصبح علي خير
        📖 انتاج سنة  : 2017
        🌎 الدولة : مصر
        🗄 تصنيف : دراما , كوميدي , رومانسي
        📜 قصة الفيلم:
        في إطار كوميدي رومانسي تشويقي، تدور قصة الفيلم في إطار مُختلف عن مهندس ناجح وثري يدعى (حسام الخديوي)، ولكنه يعاني في اﻵونة اﻷخيرة من مشاكل في حياته الطبيعية فيلجأ إلي حياة بديلة من خلال جهاز جديد يُدخله في عالم الأحلام.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco8 (\\d+)$"))
async def Xco8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco15 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco16 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بابا
        📖 انتاج سنة  : 2012
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي , رومانسي
        📜 قصة الفيلم:
        تدور أحداث الفيلم في إطار رومانسي كوميدي حيث الطبيب حازم (أحمد السقا) طبيب أمراض النساء الذي تتعلق بحبه مهندسة الديكور فريدة (درة) وعقب زواجهما يفاجأ حازم بعدم قدرته على الإنجاب فيضطر للجوء إلى عملية الحقن المهجري، فترى هل سيتمكن من تحقيق رغبتهما؟
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco9 (\\d+)$"))
async def Xco9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco18 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : جدو نحنوح
        📖 انتاج سنة  : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        مجموعة من الشباب يتوفى جدهم، وعند توزيع الميراث يكتشفون أن جدهم لم يترك أموالًا لهم، بينما ترك وصية يُطالبهم فيها بالبحث عن كنز مدفون، وبالبحث عن مكان الكنز يتضح أنه داخل مستشفى المجانين. فيخططون لدخول مستشفى المجانين سعيًا لإيجاد هذا الكنز، وهناك تحدث لهم الكثير من المفارقات الكوميدية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco10 (\\d+)$"))
async def Xco10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco20 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : سمير ابو النيل
        📖 انتاج سنة : 2013
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        في إطار كوميدي تدور أحداث الفيلم حول الشاب البخيل سمير أبو النيل (أحمد مكي) الذي يقطن بحي شعبي، ونتيجة لبخله الشديد تقع له العديد من المفارقات والمشاكل مع أهل منطقته، ويزيد من كرههم له لسوء معاملته لهم، وبين ليلة وضحاها يمرض ابن عمه حسين أبو النيل (حسين اﻹمام) ويقرر أن يترك ثروته لسمير الذي يستغل ذلك ويقوم بإنشاء قناة فضائية يناقش فيها أحواله وعلاقاته بأصدقائه وأهل منطقته.. تتوالى الأحداث في سياق كوميدي بعد إنشاء حزب سياسي يدعو له المواطنين.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco11 (\\d+)$"))
async def Xco11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco21 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco22 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : كلبي دليلي
        📖 انتاج سنة : 2013
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        تدور قصة الفيلم حول ضابط الشرطة مغاوري (سامح حسين)، الذي يعيش في صعيد مصر، ثم يُنقل فجأة إلى مارينا بالساحل الشمالي، وما عليه هناك إلا إثبات ذاته كضابط يحتذى به أمام الضباط وإشادة رئيسه بأدائه، إلى جانب ذلك يجد (مغاوري) نفسه واقعًا في حب فتاة تختلف عنه تمامًا في كل شيء.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco12 (\\d+)$"))
async def Xco12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco24 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بنات العم
        📖 انتاج سنة : 2012
        🌎 الدولة : مصر
        🗄 تصنيف : دراما, كوميدي
        📜 قصة الفيلم:
        ثلاث فتيات تربطهن علاقة عمومة يعشن مع جدتهن، يتطلعن إلى بيع القصر الذي يعشن به، فيتوجهن إلى (عزيز الهانش) ليشتري القصر، فتحاول الجدة منعهن وتحذرهن من لعنة حدثت لأجدادهن، إلا أن الفتيات لا ينصتن لها، فأصابتهن اللعنة ويتحولن إلى رجال، وطوال الأحداث تسعى الفتيات لإعادة القصر، ومحاولة فك اللعنة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco13 (\\d+)$"))
async def Xco13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco26 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : علي بابا
        📖 انتاج سنة : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : دراما، كوميدي
        📜 قصة الفيلم:
        تدور أحداث الفيلم في إطار كوميدي حول شخص انتهازي يُدعى (علي)، يسعى إلى تحقيق مصالحه الشخصية حتى ولو كانت على حساب الآخرين، وإذا به يفاجئ بوجود ابنة له (أيتن عامر) في سن العشرينات، وتبدأ من هنا المفارقات الكوميدية التي يقع فيها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco14 (\\d+)$"))
async def Xco14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco28 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : فول الصين العظيم
        📖 انتاج سنة : 2004
        🌎 الدولة : مصر
        🗄 تصنيف :  كوميدي، اكشن
        📜 قصة الفيلم:
        يدور الفيلم في إطار كوميدي حول شاب مصري يدعى (محي الشرقاوي)، يشكل كل من جده (جابر الشرقاوي) وأعمامه عصابة للتهريب، ولأنه جبان لا يستطيع مسايرتهم والعمل معهم، يذهب لوالدته وزوجها والذي يرسله للصين ليمثل مصر في مسابقة للطبخ، ليقع في العديد من المشكلات.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco15 (\\d+)$"))
async def Xco15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco30 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حسن وبقلظ
        📖 انتاج سنة : 2016
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي , رومانسي , دراما
        📜 قصة الفيلم:
        تدور أحداث الفيلم حول شقيقين ملتصقين ببعضهما البعض (علي ربيع) و(كريم فهمي)، تقع معهما العديد من المواقف الكوميدية، يتورط معهما ابن خالتهما (محمد أسامة) وفي مشاكلهما.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco16 (\\d+)$"))
async def Xco16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco32 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : الكويسين
        📖 انتاج سنة : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        مفتاح وشقيقته غزال ثنائي متخصص في النصب، يكتشف مفتاح وجود جوهرة ثمينة تدعى القرموط القرمزي في منزل عائلة الكويسين، فيقرر اختراق صفوف هذه العائلة من خلال انتحال شخصية ابنهم مظهر المفقود منذ سنوات طويلة، لكن هذه المهمة تواجه الكثير من الصعوبات رغم نجاحها في البداية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco17 (\\d+)$"))
async def Xco17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco33 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco34 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : يوم مالوش لازمة
        📖 انتاج سنة : 2015
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        ?? قصة الفيلم:
        اليوم هو يوم زفاف يحيى ومها ,و منذ الصباح الباكر يستعد العروسان لاستقبال هذا اليوم، لكن بمجرد أن يبدأ هذا اليوم حتى يقع العروسان طوال اليوم وفي حفل الزفاف نفسه في سلسلة طويلة لا تنتهي من المفارقات والمواقف الصعبة، وما يزيد الطين بلة هو مطاردة الفتاة المهووسة بوسي ليحيى طوال اليوم، وإصرارها الشديد أن تكون هي زوجته بدلًا من مها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco18 (\\d+)$"))
async def Xco18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco36 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : غبي منه فيه
        📖 انتاج سنة : 2004
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        يشعر سلطان باليأس من تحقيق حلمه بالزواج من حبيبته سامية التي أعطى له والدها مهلة شهر واحد كي يعد خلاله بيت الزوجية، فتعرف سامية على زوج خالتها ضبش، والذي يشركه في سرقاته لمساعدته، لكنه يوقعه في المتاعب بسبب غبائه الشديد.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco19 (\\d+)$"))
async def Xco19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco38 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : خير وبركة
        📖 انتاج سنة : 2017
        🌎 الدولة : مصر
        🗄 تصنيف : كوميديا
        📜 قصة الفيلم:
        تدور أحداث الفيلم في إطار كوميدي يتناول قصة شقيقين يحاولان البحث عن فرصة عمل، وخلال رحلة البحث يواجهان العديد من المواقف الكوميدية عندما يعملان في مهن لا يعرفان عنها شيئًا.

        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco20 (\\d+)$"))
async def Xco20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco40 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="comedy " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : البدلة
        📖 انتاج سنة : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي , رومانسي
        📜 قصة الفيلم:
        تدور القصة حول حمادة، ووليد اللذين ولدا في نفس اليوم فاشلين في الحياة، يقرران الذهاب إلى حفلة تنكرية، ويتنكران في زي رجال الشرطة لمقابلة زملائهم القدامى، الأمر الذي يجعل الجميع يعتقد بأنهما شرطيين حقيقيين، وتقع لهما العديد من الأحداث والمشاكل.

        """, reply_markup=keyboard)


#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^XXco1 (\\d+)$"))
async def XXco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/121", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco2 (\\d+)$"))
async def XXco2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/122", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco3 (\\d+)$"))
async def XXco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/123", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco4 (\\d+)$"))
async def XXco4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/124", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco5 (\\d+)$"))
async def XXco5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/125", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco6 (\\d+)$"))
async def XXco6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/126", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco7 (\\d+)$"))
async def XXco7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/127", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco8 (\\d+)$"))
async def XXco8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/128", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco9 (\\d+)$"))
async def XXco9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/129", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco10 (\\d+)$"))
async def XXco10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/130", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco11 (\\d+)$"))
async def XXco11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/131", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco12 (\\d+)$"))
async def XXco12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/132", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco13 (\\d+)$"))
async def XXco13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/133", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco14 (\\d+)$"))
async def XXco14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/134", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco15 (\\d+)$"))
async def XXco15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/135", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco16 (\\d+)$"))
async def XXco16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/136", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco17 (\\d+)$"))
async def XXco17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/137", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco18 (\\d+)$"))
async def XXco18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/139", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco19 (\\d+)$"))
async def XXco19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/140", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco20 (\\d+)$"))
async def XXco20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/141", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco21 (\\d+)$"))
async def XXco21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/142", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco22 (\\d+)$"))
async def XXco22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/143", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco23 (\\d+)$"))
async def XXco23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/144", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco24 (\\d+)$"))
async def XXco24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/145", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco25 (\\d+)$"))
async def XXco25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/146", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco26 (\\d+)$"))
async def XXco26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/147", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco27 (\\d+)$"))
async def XXco27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/148", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco28 (\\d+)$"))
async def XXco28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/149", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco29 (\\d+)$"))
async def XXco29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/150", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco30 (\\d+)$"))
async def XXco30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/151", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco31 (\\d+)$"))
async def XXco31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/152", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco32 (\\d+)$"))
async def XXco32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/153", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco33 (\\d+)$"))
async def XXco33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/154", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco34 (\\d+)$"))
async def XXco34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/155", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco35 (\\d+)$"))
async def XXco35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/156", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco36 (\\d+)$"))
async def XXco36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/157", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco37 (\\d+)$"))
async def XXco37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/158", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco38 (\\d+)$"))
async def XXco38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/159", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco39 (\\d+)$"))
async def XXco39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/160", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco40 (\\d+)$"))
async def XXco40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/161", reply_to_message_id=mid)


#########################################################################################
#########################################################################################
#########################         # Aflam Action #             ##########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^action (\\d+)$"))
async def action(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("حملة فرعون", callback_data="Xact1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بني ادم", callback_data="Xact2 " + str(m.from_user.id))],
        [InlineKeyboardButton("الخليه", callback_data="Xact3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("حرب كرموز", callback_data="Xact4 " + str(m.from_user.id))],
        [InlineKeyboardButton("من ضهر راجل", callback_data="Xact5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("زنزانة سبعة", callback_data="Xact6 " + str(m.from_user.id))],
        [InlineKeyboardButton("خارج عن القانون", callback_data="Xact7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ولاد العم", callback_data="Xact8 " + str(m.from_user.id))],
        [InlineKeyboardButton("وش سجون", callback_data="Xact9 " + str(m.from_user.id))],

        [InlineKeyboardButton("𝐇𝐎𝐌", callback_data="aflamAR2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌞ 𝚜𝚘𝚞𝚛𝚌𝚎 𝚜𝚎𝚖𝚘 ⌝⚡", url=f"https://t.me/FTTUTY")],

    ])
    await m.message.edit_text("اهلا بك في قائمة الافلام الاكشن العربيه", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact1 (\\d+)$"))
async def Xact1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact2 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حملة فرعون
📖 انتاج سنة : 2019
🌎 الدولة : مصر
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تدور أحداث الفيلم في إطار تشويقي مثير حول الشاب يحيى الشهير بفرعون والذي يدير أكبر شبكة اغتيالات منظمة في مصر، ويضطر إلى التوجه إلى سوريا لتحرير أبنه المخطوف .
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact2 (\\d+)$"))
async def Xact2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact4 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بني ادم
📖 انتاج سنة : 2018
🌎 الدولة : مصر
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تدور الأحداث في إطار بوليسي تشويقي مثير حول رجل الأعمال (آدم) الذي يتهم بأعمال إجرامية، في الوقت الذي تلجأ إليه الشرطة في مهمة خطيرة، فهل الأحداث ستتطور وتجعله متورط، أم هناك جانب غامض غير معروف عنه؟.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact3 (\\d+)$"))
async def Xact3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact6 " + str(m.from_user.id))],
        [InlineKeyboardButton("◁", callback_data="action " + str(m.from_user.id))],
    ])
    await m.message.edit_text("""فيلم #الخلية | دراما , اكشن | 2017
عندما يذهب صديقه ضحية عملية إرهابية، يقسم سيف، وهو ضابط عمليات خاصة، على الثأر لصديقه، ويطلب مساعدة الضابط صابر في سبيل تحقيق ذلك.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact4 (\\d+)$"))
async def Xact4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = Inlin

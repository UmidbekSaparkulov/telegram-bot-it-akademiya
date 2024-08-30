from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
menucategory = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏫 Tramplin it akademiya", callback_data='o_markaz'),
            InlineKeyboardButton(text="💻 Kurslar", callback_data='cours')
        ],
        [
            InlineKeyboardButton(text="👨🏼‍💼 Dasturlashda mashxur insonlar", callback_data='hodimlar'),
            InlineKeyboardButton(text="💼 Bo'sh ish o'rinlari", callback_data='vakansiya')
        ],
        [
            InlineKeyboardButton(text="☎️ Murojaat uchun telefon", url='https://t.me/tramplin_uz')
        ]
    ]
)
courses_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=" Backend cours", callback_data='back_c'),
            InlineKeyboardButton(text=" Frontend cours", callback_data='fcours'),
        ],
        [
            InlineKeyboardButton(text=" Mobil grafik cours", callback_data='mgcours'),
            InlineKeyboardButton(text=" Kiberxavfsizlik cours", callback_data='cybcours')
        ],
        [
            InlineKeyboardButton(text="⤴️ Ortga", callback_data='ortga')
        ]
    ]
)
informatsiya = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="⤴️ Ortga", callback_data='1ortga')
        ]
    ]
)

#  Cours uchun tugmalar
backend_course = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⤴️ ortga", callback_data='c_ortga')]])
frontend_course = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⤴️ ortga", callback_data='c_ortga')]])
Kiberxavfsizlik_course = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⤴️ ortga", callback_data='c_ortga')]])
mobilagrafik_course = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⤴️ ortga", callback_data='c_ortga')]])


hodimlar_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Sunday Pichai', callback_data='google_asoschisi'),
            InlineKeyboardButton(text="Pavel Valeryevich Durov", callback_data='tg_asoschisi'),
        ],
        [
            InlineKeyboardButton(text="Arkadiy Yuriyevich Voloj", callback_data='yandeks_asoschisi'),
            InlineKeyboardButton(text="Jeffrey Preston Bezos", callback_data='amazon_asoschisi'),
        ],
        [
            InlineKeyboardButton(text="⤴️ Ortga", callback_data='ortga')
        ]
    ]
)

murojaat_uchunKeyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⤴️ ortga', callback_data='ortga')]])


hodimlar_uchunortga_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⤴️ Ortga", callback_data='gortga')]])


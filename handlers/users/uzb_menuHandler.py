import logging


from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from loader import dp
from keyboards.inline.uzb_menu import hodimlar_keyboard, hodimlar_uchunortga_tugma
from keyboards.inline.uzb_menu import menucategory, courses_menu, backend_course, informatsiya, frontend_course, mobilagrafik_course, Kiberxavfsizlik_course
from aiogram.types import InputFile
@dp.message_handler(text_contains="O'zbek")
async def menu_select(message: Message):
    # ReplyKeyboardRemove bilan klaviaturani o'chirish
    await message.answer("🇺🇿 Til tanlandi",reply_markup=ReplyKeyboardRemove())

    
    photo_url = InputFile(path_or_bytesio="handlers/Photos_oquvmarkaz/tramplin_photomarkaz.png")
    habar = "<b>Tramplin IT Akademiyasi haqida qisqacha ma'lumot</b>\n\n"
    habar += "Tramplin IT Akademiyasida siz Dasturlashni professionallardan o'rganishingiz mumkin.\n"
    habar += "Kurs davomida yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim olishingiz va o'zlashtirgan bilimlaringizni amaliyotda 50 dan ortiq loyiha asosida o'z portfolioingizni yaratishingiz mumkin."
    await message.delete()
    await message.answer_photo(photo=photo_url, caption=habar, reply_markup=menucategory)
    

    

    
@dp.callback_query_handler(text="cours")
async def select_courses(call: CallbackQuery):
    photo_url1 = InputFile(path_or_bytesio="handlers/zamonaviy_kasblar/zamonaviykasblar.jpg")
    msg="Zamonaviy kasblardan birini tanglang"
    await call.message.delete()
    await call.message.answer_photo(photo=photo_url1, caption=msg, reply_markup=courses_menu)


@dp.callback_query_handler(text="back_c")
async def courses(call:CallbackQuery):
    
    video_url = InputFile(path_or_bytesio="handlers/videobackend/.backendkurs.mp4")
    await call.message.answer_video(video=video_url, caption="Python-da backend ishlab chiqish kursi veb-ilovalar va telegram botlarini ishlab chiqishning\n turli jihatlariga bag'ishlangan bir nechta modullardan iborat", reply_markup=backend_course)
    await call.message.delete()


@dp.callback_query_handler(text="fcours")
async def courses(call:CallbackQuery):

    video_url = InputFile(path_or_bytesio="handlers/Frontendkursi/FrontendCoursi.mp4")
    await call.message.answer_video(video=video_url, caption="<b>Frontend</b> bu <b>Web Dasturlash</b> sohasining biridir ya'ni <b>Frontend</b> orqali siz veb saytning foydalanuvchilarga ko'rinadigan qismini yaratasiz", reply_markup=frontend_course)
    await call.message.delete()

@dp.callback_query_handler(text="mgcours")
async def courses(call:CallbackQuery):

    video_url = InputFile(path_or_bytesio="handlers\Mobilografiyakursi\mobilografiyakursi'.mp4")
    await call.message.answer_video(video=video_url, caption="<b>Grafik dizayn</b> — dizayn sohasining yoʻnalishlaridan biri boʻlib, maʼlum axborotni ijtimoiy guruhlarga yetkazish uchun vizual kontent yaratish, ularni tartiblash, loyihalashga xizmat qilad", reply_markup=mobilagrafik_course)
    await call.message.delete()

@dp.callback_query_handler(text="cybcours")
async def courses(call:CallbackQuery):

    video_url = InputFile(path_or_bytesio="handlers/Kiberxafsizlikcoursi/Ciberafsizlikcoursi.mp4")
    await call.message.answer_video(video=video_url, caption="...tarmoq xavfsizligi qal'a devorlari ichida tinchlikni saqlash va tashkilotning suverenitetini tarmoq bilan bog'liq tahdidlardan himoya qilish haqida qayg'uradi", reply_markup=Kiberxavfsizlik_course)
    await call.message.delete()


@dp.callback_query_handler(text="c_ortga")
async def cancel_course(call:CallbackQuery):
    photo_urlortga = InputFile(path_or_bytesio="handlers/zamonaviy_kasblar/zamonaviykasblar.jpg")
    await call.message.answer_photo(photo=photo_urlortga, reply_markup=courses_menu)
    await call.message.delete()

@dp.callback_query_handler(text="o_markaz")
async def markaz_informatsion(call:CallbackQuery):
    photo_url = InputFile(path_or_bytesio="handlers/Photos_oquvmarkaz/tramplin_photomarkaz.png")
    
    msg = "<b>Tramplin It Akademiyasi haqida ma'lumot</b>\nTramplin It Akademiyasida siz Professionallardan o'rganishingiz mumkin\n\n\n"
    msg += "Kurs yuqori malakali dasturchilardan maxsus metodika asosidan sifatli\nta'lim olish va o'zlashtirgan bilimlaringizni oshirishda <b>50</b> dan ortiq\n"
    msg += "miqdorda o'z portfoliongizni yaratishingiz mumkin.\n\n\n"
    msg += "Ish bilan ta'minlaymiz agar:\n\n\n"
    msg += "<b> -Interview </b>\n"
    msg += "<b> -Vazifalar </b>\n"
    msg += "<b> -Imtihon </b>\n"
    msg += "<b> -Kitob taqdimoti </b>\n"
    msg += "<b> -Mini +</b>\n\n\n"

    msg += "yuqoridagilardan <b>90/100</b> olsangiz\n\n\n"
    msg += "<b>📞 Biz bilan bo'glanish:  +9989 (90) 805-51-95 </b>\n\n"
    msg += "<b>📍 Toshkent shahar, Amir Temur shoh ko'chasi, 47, Toshkent\nmetrosi yaqinida</b>\n"
    
    msg += "🌐 telegram kanal:<b> hhtps://t.me/tramplin_uz</b>"
    await call.message.delete()
    await call.message.answer_photo(photo=photo_url, caption=msg, reply_markup=informatsiya)

@dp.callback_query_handler(text="ortga")
async def cancel_buying(call: CallbackQuery):
    photo_url = InputFile(path_or_bytesio="handlers/Photos_oquvmarkaz/tramplin_photomarkaz.png")
    habar = "<b>Tramplin IT Akademiyasi haqida qisqacha ma'lumot</b>\n\n"
    habar += "Tramplin IT Akademiyasida siz Dasturlashni professionallardan o'rganishingiz mumkin.\n"
    habar += "Kurs davomida yuqori malakali dasturchilardan maxsus metodika asosida sifatli ta’lim olishingiz va o'zlashtirgan bilimlaringizni amaliyotda 50 dan ortiq loyiha asosida o'z portfolioingizni yaratishingiz mumkin."
    await call.message.delete() 
    await call.message.answer_photo(photo = photo_url, caption=habar, reply_markup=menucategory)
    


# Xodimlar uchun handler 

@dp.callback_query_handler(text="hodimlar")
async def hodimlar_information(call: CallbackQuery):
    file_rasm = InputFile(path_or_bytesio="handlers/ijtimoiy_tarmoq/rasmlar.png")
    await call.message.delete()
    await call.message.answer_photo(photo=file_rasm, reply_markup=hodimlar_keyboard)


# Sundar Pichai

@dp.callback_query_handler(text="google_asoschisi")
async def g_asoschisi(call: CallbackQuery):
    faylgoogle = InputFile(path_or_bytesio="handlers/googleAsoschisi/google_asoschisi.jpg")
    msg = "Go‘zal hayot o‘zi kelmaydi. U o‘qib-o‘rganish, muntazam intilish, qattiq mehnatning natijasidir.\n"
    msg += "Bu baxtli hayotga berilgan eng munosib ta’rif. Aks holda, Janubiy Hindistonning uzoq Maduray shahrida,\n"
    msg += "oddiy oilada dunyoga kelgan bolakay 2016 yilda okean ortining eng ko‘p haq to‘lanadigan rahbarlaridan biriga aylanmas edi.\n"

    msg += "2015 yilda Google kompaniyasiga egalik qiluvchi Alphabet Inc. xoldingi tashkil etilgach, kelib chiqishi hindistonlik bo‘lgan <b>Sundar Pichai</b> Google kompaniyasiga rahbar etib tayinlanadi.\n"
    msg += "<b>Sundar Pichai</b> 1972 yilda Hindistonning Tamil Nadu shtatida, injener-elektrik xonadonida tavallud topgan.\n"

    msg += "Google'ning bo‘lajak rahbari yoshligidanoq ilmga chanqoqligi bilan tengdoshlaridan ajralib turgan. \n"
    msg += "U maktabda kamgap, ammo so‘zlari ma’noga to‘la, uyatchan o‘quvchi bo‘lgan. Elektronika mahsulotlarini \n"
    msg += "titklash uning uchun eng sevimli mashg‘ulot edi. Uni insoniyat hayotiga yengillik olib kelayotgan kompaniyaning dahosi deyishadi."
   
    await call.message.answer_photo(photo=faylgoogle, caption=msg, reply_markup=hodimlar_uchunortga_tugma)
    await call.message.delete()


# telegram asoschisi
@dp.callback_query_handler(text="tg_asoschisi")
async def telegram1_asos(call: CallbackQuery):
    fayltelegram = InputFile(path_or_bytesio="handlers/telagram_Asoschisi/tg_asoschisi.jpg")

    msg = "<b>Pavel Valeryevich Durov</b>\n  rus : Pavel Valeryevich Durov ; 1984-yil 10-oktabrda tug‘ilgan.\n  Rossiyada tug‘ilgan biznes-menejer, Telegram Messenger Inc. asoschilaridan biri va bosh ijrochi direktori va ham muassisi.\n"
    msg += "ijtimoiy tarmoq VK sayti asl nomining qisqartmasi VKontakte ; ruscha : VKontakte , InContact degan ma'noni anglatadi .\n 2021 yildan beri u to'rtta davlat va Yevropa Ittifoqi fuqaroligiga ega .\n"
    msg += "Durov 2023 yilda 11,5 milliard dollar boyligi bilan Forbes milliarderlari ro'yxatiga kiritigan . Uning boyligi asosan Telegram egaligi bilan bog'liq.\n"
    msg += "2024-yil 25-avgust holatiga koʻra , Durov Forbes maʼlumotlariga koʻra, 15,5 milliard dollar boyligi bilan dunyoning 120-eng boy kishisi edi ."

    
    await call.message.answer_photo(photo=fayltelegram, caption=msg, reply_markup=hodimlar_uchunortga_tugma)
    await call.message.delete()


#  yandeks asoschisi
@dp.callback_query_handler(text="yandeks_asoschisi")
async def yandexs_asos(call:CallbackQuery):
    faylyandex = InputFile(path_or_bytesio="handlers/Yandeks_asoschisir/yandeks_asoschisi.webp")

    javob = "<b>Arkadiy Yuriyevich Voloj</b>\n (1964-yil 11-fevralda tugʻilgan, Guryev, Qozogʻiston SSR, SSSR) — rossiyalik tadbirkor va dasturchi,\n Yandex kompaniyalar guruhining asoschisi va sobiq bosh direktor.\n 2018-yilda Forbes maʼlumotlariga koʻra, u 1,5 milliard dollar boyligi bilan Rossiyada 65-oʻrinni egallagan.\n"

    javob += "2022-yil 3-iyundan boshlab Qrimning anneksiya qilinishi va Ukrainaning Yevropa Ittifoqi sanksiyalari ostida beqarorlashuvi uchun mas’ul boʻlgan Rossiya hukumatiga daromad keltirishi sababl"
    
    await call.message.answer_photo(photo=faylyandex, caption=javob, reply_markup=hodimlar_uchunortga_tugma)
    await call.message.delete()

@dp.callback_query_handler(text="amazon_asoschisi")
async def amazon_asos(call:CallbackQuery):
    faylamazon = InputFile(path_or_bytesio="handlers/amazon_asoschisid/amazon_asoschisi.jpg")

    response = "<b>Jeffrey Preston Bezos</b>\n (Jeffri Preston Bezos; 1964-yil 12-yanvarda tugʻilgan) amerikalik ishbilarmon, mediamagnat, kompyuter muhandisi va investordir. \nBezos 1994-yilda hozirda jahonning eng yirik internet-kompaniyalaridan biri boʻlmish <b>mazon</b>ga asos solgan va bugungi kunda uning ijrochi raisidir.\n 2022-yilning oktyabri holatiga koʻra, Bezos $139 milliardlik boyligi bilan dunyodagi uchinchi eng badavlat inson hisoblanadi."
    
    await call.message.answer_photo(photo=faylamazon, caption=response, reply_markup=hodimlar_uchunortga_tugma)
    await call.message.delete()


@dp.callback_query_handler(text="gortga")
async def cancel_buying(call: CallbackQuery):
    rasm = InputFile(path_or_bytesio="handlers/ijtimoiy_tarmoq/rasmlar.png")
    await call.message.answer_photo(photo=rasm, reply_markup=hodimlar_keyboard)
    await call.message.delete()


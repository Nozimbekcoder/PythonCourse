# """Mavzu: Barcha otilgan """
#

# # Bugun o'rgangan narsalimizni amaliy qo'llab ko'ramiz

# # Do'stlar royhatini tuzamiz
# print("Keling yaqin do'stlaringiz ro'yhatini tuzamiz!!!")
# dostlar = []
# n = 1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting: "
#     ism = input(savol)
#     dostlar.append(ism)
#     takror =input("Yana do'stlar qoshasizmi? : ")
#     n+=1
#     if  takror.lower()!='ha':
#         break
#
# print("Do'tlaringiz ro'yhati:")
# for dost in dostlar:
#     print(dost.title())


# # Pythonda sikllar
# # Python dasturlash tilida ikki xil sikl ishlatiladi. Bular while va for sikllari. Ularning qulayligi
# # shundaki, ular belgilangan nuqtaga yetmaguncha ko’rsatilgan
# # amalni qayta-qayta bajaraveradi. Shu
# # sababli biz bir amalni qayta-qayta yozib o’tirmaymiz.
# # while va for qo’llanish usuli va joyiga ko’ra farqlanadi.
# # Bu darsda while bilan tanishamiz.

# # while sikli
# # while sikliga odatda bir shart berish kerak bo’ladi va o’sha shart bajarilmaguncha u biz ko’rsatgan
# # amalni qayta-qayta bajaraveradi. while sikli quyidagi umumiy ko`rinishga ega:
#
# # while (shart):
# #     sikl_tanasi
#
#
# # While sikl operatorining ishlash tartibi
# #  Agar (shart) rost (true) qiymatga ega bo`lsa, sikl_tanasi bajariladi.
# Qachonki shart yolg`on (false) qiymatga teng bo`lsa sikl tugatiladi.
# #  Agar (shart) true qiymatga ega bo`lmasa sikl tanasi biror marta
# ham bajarilmaydi.
# # Masalan 1 dan 10 gacha bo’lgan sonlarni ekranga chiqarishimiz kerak
# bo’lsa, buni quyidagicha
# # amalga oshiramiz:
# # Avval, boshlang’ich nuqtani belgilaymiz,
# ya’ni o’zgaruvchi 1 ga teng bo’ladi. So’ngra shunday
# # shart beramizki toki o’sha shart o’zgaruvchi 11 dan kichik ekan,
# uni har safar ekranga chiqarib shu
# # songa 1 ni qo’shib ketaversin. Natijada o’zgaruvchimiz toki 10 ga yetguncha ushbu amalni
# # bajaraveradi. 11 ga yetganda esa shart bajarilmay qoladi va sikl to’xtaydi.
# i = 1
# while i < 11:
#     print(i)
#     i = i + 1
# # break
# # break kalit so’zi siklni to’xtatadi.
# Asosiy sikl davom etayotgan bo’lsa ham, biz belgilagan
# # nuqtada siklni to’xtatadi.
# Masalan yuqoridagi misolni olamiz. Uni shunday o’zgartiramizki,
# # o’zgaruvchimizning qiymati 5 ga yetganda sikl to’xtaydi va qolgan sonlarni
# ekranga chiqarmaydi:
# i = 1
# while i < 11:
#     print(i)
#     if i == 5:
#         break
#     i += 1
#
# # continue
# # continue kalit so’zi bilan siklning ba’zi nuqtalaridan sakrab o’tish mumkin.
# Masalan biz 6 dan
# # tashqari 1 dan 10 gacha bo’lgan sonlarni ekranga chiqaramiz.
# Bunda 6 soni hisobga olinmay undan
# # o’tib ketiladi:
# i = 1
# while i < 11:
#     i += 1
#     if i == 6:
#         continue
#     print(i)
# # else
# # else kalit so’zi sikl to’xtagandan so’ng ham yan bir amal bajarish
# imkoni beradi. Masalan, sikl
# # to’xtgandan so’ng to’xtaganligi haqida ma’lumot ekranga chiqsin:
# i = 1
# while i < 11:
#     print(i)
#     i += 1
# else:
#     print("sikl to'xtadi")


# # For sikli
# # Python dasturlash tilida for operatori C va Paskal dasturlash tillarida qo`llanishidan farq qiladi.
# # Python da for operatori biroz murakkabroq, lekin while sikliga qaraganda ancha tezroq bajariladi.
# # For…in operatori obyektlar ketma-ketligida iteratsiyani amalga oshiradi, ya’ni bu sikl har qanday
# # iteratsiya qilinadigan obyekt bo`ylab o`tadi(satr yoki ro`yxat bo`ylab) va har bir o`tish vaqtida sikl
# # tanasini bajaradi.
# # Python dasturlash tilida for sikli asosan to’plam va ro’yxatlar bilan ishlatiladi. For sikli bilan
# # to’plam yoki ro’yxatning har bir elementiga murojaat qilish mumkin. Masalan, quyidagi
# # ro’yxatning har bir elementini ekranga chiqaramiz:
# meva = ["olma", "anor", "banan"]
# for a in meva:
#     print(a)
# # Satr bo’ylab sikl
# # Satr bo’ylab sikl amalga oshirilsa satrdagi har bitta harfga murojaat bo’ladi. Chunki satr harflar
# # to’plamidan tashkil topgan. Hozir quyidagi so’zning barcha harflarini ekranga chiqaramiz:
#
# for a in "dastur":
#     print(a)
#     break
# # break kalit so’zi bilan siklni to’xtatamiz,
# hattoki sikl to’xtamagan bo’lsa ham. Masalan, “dastur”
# # so’zining harflarini birma-bir ekranga chiqarish siklini ishga tushuramiz va “s” harfiga yetganda
# # siklni to’xtatamiz:
# for x in "dastur":
#     print(x)
#     if x == "s":
#         break
# # Endi e’tiborimizda bir narsaga qaratsak. Yuqoridagi kodda print buyrug’i break buyrug’idan
# # oldinroq qo’ygan edik. Shu sababli avval “s” harfi ekranga chiqib, so’ng sikl to’xtadi. Endi print
# # buyrug’ini pastroqqa qo’yamiz. Bunda “s” harfi ekranga chiqmay qoladi, chunki sikl undan
# # avvalroq to’xtaydi.
# for x in "dastur":
#     if x == "s":
#         break
#     print(x)
# # continue
# # continue kalit so’zi siklning ayrim joylaridan sakrab o’tadi. Aniqroq qilib aytganda sikl
# # davomida ayrim nuqtalarga kelganda ko’rsatilgan amalni bajarmay ketadi.
# # Masalan, “python” so’zidagi harflarni ekranga chiqaramiz va shunda “h” harfini tashlab ketamiz:
# for x in "python":
#     if x == 'h':
#         continue
#     print(x)
# # range() va xrange()
# # range() funksiyasi biror amalni belgilangan marta bajarish yoki biror oraliqdagi sonlarga murojaat
# # qilsh uchun qo’llaniladi. Bunda range() ichiga kerakli son qo’yiladi va sanoq avtomatik tarzda o
# # dan boshlanib ko’rsatilgan songacha davom etadi. Ammo uning o’zi hisobga kirmaydi.
# # Tushunish uchun misol ko’ramiz. 0 dan 5 gacha (5 soni hisobga kirmaydi) bo’lgan sonlarni ekranga
# # chiqaramiz:
# for x in range(5):
#     print(x)
# # Yuqorida biz range() funksiyasida sanoq avtomatik 0 dan boshlanishini aytib o’tdik. Biz uni
# # o’zimiz istagan sondan boshlashimiz ham mumkin.
# # Masalan 1 dan 5 gacha bo’lgan sonlarni ekranga chiqaramiz. Bunda sanoq 1 dan boshlanishi uchun
# # 1 sonini ham kiritamiz. Demak, biz 1 dan 6 gacha bo’lgan oraliqni kiritamiz:
# for x in range(1, 6):
#     print(x)
# # range() funksiyasida sum avtomatik bittaga ortib boradi. Ammo bu holatni ham o’zgartirish
# # mumkin. Bunda oraliqni ko’rsatgandan so’ng sanoq nechtaga ortishini ham kiritamiz. Shunda
# # funksiya ichidagi dastlabki ikkita son oraliqni, uchinchi son esa sanoq nechtaga ortiqshini
# # ko’rsatadi.
# # Masalan, 1 dan 10 gacha bo’lgan faqat juft sonlarni ekranga chiqarmoqchimiz. Bunda oraliqni 2
# # dan 11 gacha deb belgilaymiz. Shunda sanoq 2 dan boshlanadi va 10 gacha davom etadi. Har safar
# # sanoq ikkitaga ortishi uchun uchinchi bo’lib 2 soni kiritamiz:
# for x in range(2, 11, 2):
#     print(x)
# # Katta diapazondagi raqamlardan foydalanib ro`yxatni yaratish range() funksiyasi o`zini oqlamaydi
# # yoki ba’zi hollarda xotira yetishmaydi.
# # Shunday hollarda Python da xrange() funksiyasidan foydalaniladi.
# # else
# # else kalit so’zi sikl tugagach ham yan bir amal bajarish imkonini beradi. Odatda bundan sikl
# # tugagani haqida ma’lumot berishda foydalaniladi.
# # Masalan, “python” so’zini besh marta ekranga chiqarmoqchimiz va sikl tugagach shu haqida xabar
# # beramiz. Bunda endi e’tibor bering, range() funksiyasi bilan sanoq asosida sonlarni ekranga
# # chiqarmayapmiz, balki shuncha marta bir xil amalni bajaryapmiz:
# for x in range(5):
#     print("python")
# else:
#     print("\nSikl tugadi!")
# # Sikl ichida sikl
# # Sikl ichida sikl qo’llanganda ichki sikl tashqi siklning har bitta bosqichida bir martadan bajariladi.
# # Hozir har bitta rangni har bir mashina bilan birgalikda qo’llab ko’ramiz:
# rang = ["qora", "oq", "qizil"]
# mashina = ["Spark", "Nexia", "Lacetti"]
# for x in rang:
#     for y in mashina:
#         print(x, y)
#     pass
# # for sikli ham xuddi while sikli singari bo’sh bo’lishi mumkin emas. Ya’ni sikl davomida albatta
# # nima amal bajarilishini kiritishimiz lozim. Ammo bu amal hali aniq bo’lmasa kodimizda xatolik
# # yuz bermasligi uchun pass kalit so’zidan foydalanamiz va dastur ishga tushganda o’sha qism
# # hisobga olinmay ketiladi. Masalan, hozir sikl davomida bajarilishi kerak bo’lgan amalni kiritmay
# # pass kalit so’zini kiritamiz. Bunda xatolik yuz bermaydi, chunki pass kalit so’zi qo’yilgan. Ammo
# # hech qanday amal ham bajarilmaydi, chunki biror amal bajarish haqida buyruq berilmagan.
# for x in range(5):
#     pass


# while3

# n = int(input("N butun sonini kiriting: "))
# k = int(input("K butun sonini kiriting: "))
# butun = 0
# while n >= k:
#     n = n - k
#     butun += 1
# else:
#     print(f"{butun} Butun, {n} Qoldiq")

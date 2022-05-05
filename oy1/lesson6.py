"""
Mavzu: String (matn yoki satr)

"""

# shaxar = "Наманган"
# poytaxt = "Тошкент"
# tuman = "Норин"
# ob_havo = 'погода'
#
#
# print(shaxar+',', poytaxt+',', tuman+'.')
#
# gap = "Men yangi DELL markali 💻 sotib oldim."
# print(gap)
#
# # Unicodlar jadvali: https://unicode-table.com/en/    Win + .
#
# # String ustida amallar
#
# ism = "Nozimjon"
# print("Mening ismim "+ism)

# ism = "Nozimjon"
# print("Mening ismim "*9)

# ism = "Abror"
# familya = "Abdulatipov"
# gap = "ning telefoni bor."
# gap1 = "ning komyuteri bor."
# gap2 = "ning mashinasi bor."
# print(familya + " ", ism+gap2)
#
# ism = "Nozimjon"
# familya = "Bozorov"
# print(ism + " " + familya)
#
# # f"_{var}_____{var}_____" ushbu funksiya yordamida biz
# # istalgancha satrlar va o'zgaruvchilarni
# # birlashtirishimiz mumkin.
#

# misol = f"Salom {familya} {ism}bek"
# print(f'Assalom salom {misol}')

# ism = "Nozimjon"
# familya = "Bozorov"
# print(f'{ism} {familya}')
# toliq_ism = f"{ism} {familya}"
# print(toliq_ism)
#
# ism = "Abdurahmon"
# meva = "Shaftoli va olma"
# print(f"Salom, Mening ismim {ism}.\nMen {meva}ni yaxshi ko'raman.")
#		Satrlarni kesib olish

# a="O'zbekiston kelajagi"
# kesilgan=a[-12:-9]   # -12 startindex, -9 endindex
# kesilgan=a[12:15]

# matn="Bot sizga Telegramda turib Google'dan "
# dam=matn[-4:-2]
# m=matn[17:18]
# print(dam+m)
# gram
# Google
# TeleGoogle
# Biz
# 'dan



from math import sqrt
# Masalalar yechish
# Begin6
a=int(input('A tomonni kiriting:'))
b=int(input('B tomonni kiriting:'))
og=sqrt(a*b)

print(f'Ikkita sonning orta geometrigi {og}\n')






# kesilgan=a[0:6]
# kesilgan=a[3:6]


# print(kesilgan)
# print(a[0:6])
# b="Buyuk davlat."
# print(b[6:12])
# print(b[0:2])
# print(b[0:3])
# print(b[2:5])
# print(a[21:])
#
# b = "Salom, Dunyo!" #Eslatma: Birinchi belgi 0 indeksiga ega.
# print(b[:5])
#
# b = "Salom, Dunyo!"
# print(b[7:12])
# b = "Salom, Dunyo!"
# print(b[-6:-1])
#
# lorem="Bugun Barselona vs RealMadrid futbol o'yini bo'ladi"
# print(lorem)
# # ________________________________________
#
# b = "Hello, World!"
# print(b[:5])
# # 0 elementdan bolshlab 5ta harf oladi
# # _______________________________________
# b = "Hello, World!"
# print(b[2:])
# # 2 indeksdan boshlab oxirigacha oladi
# # ________________________________________
#
#
#
#
#
#
#
#
#
# """
# String metodlari
# metodlar bilan ishlar ekanmiz ularga murojaat qilishimiz kerak bo'ladi
# ularga murojaat qilish uchun   matn.metod() holatida bo'ladi
# """
#
# ism = "Bobur"
# familya = "Olimov"
# toliq_ism = f"{ism} {familya}"
# toliq_ism="Olimov Bobur"
# print(toliq_ism)
#
# lorem="lorem ipsum dolor sit,\n" \
#       "amet consectetur adipisicing elit.\n" \
#       "Architecto voluptas culpa similique\n" \
#       "ratione quos laboriosam deleniti pariatur veniam vero,\n" \
#       "magnam enim "
# cap= lorem.capitalize()
# print(cap)
#
# a="nozimjon"
# print(a.upper())
#
# a1="NOZIMJON"
# print(a1.lower())
#
# lorem="lorem ipsum dolor sit,\n" \
#       "amet consectetur adipisicing elit.\n" \
#       "Architecto voluptas culpa similique\n" \
#       "ratione quos laboriosam deleniti pariatur veniam vero,\n" \
#       "magnam enim "
# print(lorem.title())
#
#

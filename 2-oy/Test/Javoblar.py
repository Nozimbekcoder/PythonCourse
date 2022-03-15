# 1.

# a = int(input('1-son>>>'))
# b = int(input('2-son>>>'))
# c = int(input('3-son>>>'))
#
# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# elif c < b and c < a:
#     print(c)

# 2.
# son = int(input("Son kiriting: "))
#
# if son > 0:
#     if son % 2 == 0:
#         print(son, "Musbat juft son")
#     else:
#         print(son, "Musbat toq son")
# else:
#     if son % 2 == 0:
#         print(son, "Manfiy juft son")
#     else:
#         print(son, "Manfiy toq son")

#
# son = input("Son kiriting: ")
#
# try:
#     son = int(son)
#     if son > 0:
#         if son % 2 == 0:
#             print(son, "Musbat juft son")
#         else:
#             print(son, "Musbat toq son")
#     else:
#         if son % 2 == 0:
#             print(son, "Manfiy juft son")
#         else:
#             print(son, "Manfiy toq son")
# except:
#     print("Tog'ri javob kiritmadingiz! ")

# 3.
# kgkonfetn = int(input("1 kg konfet narxini kiriting: "))
#
# for kg in range(1,11,1):
#     print(f"{kg} kg konfet {kgkonfetn} dan jami {kgkonfetn*kg} so'm bo'ladi.")

# 4.
# fksoni = int(input("Bugun nechta odam bilan ko'rishdingiz: "))
# suhbatdoshlar = []
# n = 1
# for odam in range(fksoni):
#     ism = input(f"{n}-suhbatlashgan odam ismini kiriting: ")
#     suhbatdoshlar.append(ism)
#     n=n+1
# print(suhbatdoshlar)


# 5.
# a = int(input('1-son>>>'))
# b = int(input('2-son>>>'))
# yigindi = a
# while a < b:
#     a = a + 1
#     yigindi = yigindi + a
#     # print(yigindi)
# else:
#     print(yigindi)
#     print("Dastur ishi yakunlandi")


# 6.
# while True:
#     yosh = input("Yoshingizni kiriting:")
#     if yosh == 'exit' or yosh == 'quit':
#         print("Dastur tugatildi")
#         break
#     else:
#         if yosh.isdigit():
#             yosh = int(yosh)
#             if yosh > 0 and yosh <= 7:
#                 print("Siz kassaga 2000 so'm to'laysiz")
#             elif yosh <= 18:
#                 print("Siz kassaga 5000 so'm to'laysiz")
#             elif yosh <= 65:
#                 print("Siz kassaga 10 000 so'm to'laysiz")
#             elif yosh > 65:
#                 print("Siz uchun Bepul")


# 6. 2
# savol = "Yoshingizni kiriting: "
#
# while True:
#     qiymat = input(savol)
#     if qiymat == "exit" or qiymat == "quit":
#         break
#     yosh = int(qiymat)
#
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else:
#         narh = 0
#
#     if narh == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")

# 7.
# karra = int(input("Sizga necha karra kerak? : "))
# for i in range(1,11):
#     print(f"{karra} * {i} = {karra * i}")

# 8.
# aralash = {
#     'kalit': 'qiymat',
#     'olma': ['qizil', 'sariq', 'yashil'],
#     'car': {
#         'malibu2': {
#             'rangi': 'Qora',
#             'tezligi': '250km/s',
#             'narxi': '27000$',
#         },
#         'Nexia': {
#             'rangi': 'oq',
#             'tezligi': '190km/s',
#             'narxi': 'Bepul'
#         }
#     }
# }
#
# print(f"{aralash['car']['Nexia']['rangi'].title()} rangli Malibu avtomili bor narxi {aralash['car']['malibu2']['narxi']}")



# 9.
# sum = [100, 24, 6, 25, 5, 15, 47, 65, 60]
# for son in sum:
#     if son%5==0:
#         print(son)

# 10.


mashinalar = ['audi','BMW','gm','hyundai']
for mashina in mashinalar:
    if mashina =='BMW':
        print(mashina.upper())
    print(mashina)


# 1. Uchta butun son berilgan. Shu sonlarni
# kichigini aniqlaydigan dastur tuzing
#
# 2. Butun son berilgan. Berilgan sonni
# 'Musbat toq son' , 'Manfiy juft son',
# 'son nolga teng' va xokazo
# ekranga chiqaradigan dastur tuzing.
#
# 3. Bir kg konfetning narxi
# berilgan (float). 1,2, ..., 9, 10 kg konfetni
# narxini chiqaruvchi dastur tuzing
#

# 4. Foydalanuvchidan bugun nechta odam bilan
# uchrashganini (suhbatlashganini) so'rang
# va har bir suhbatlashgan
# odamning ismini birma-bir so'rab
# ro'yxatga yozing.
# Ro'yxatni konsolga chiqaring.


# 5. a va b butun sum berilgan (a < b).
# a dan b gacha bo'lgan sonlarning
# yigindisini ekranga chiqaruvchi dastur tuzing.


# 6. Muzeyga chipta narhi foydalanuvchining
# yoshiga bog'liq:
#  7 dan yoshlarga - 2000 so'm,
#  7-18 gacha 3000 so'm,
#  18-65 gacha 10000 so'm,
#  65 dan kattalarga bepul.
#  Shunday while tsikl yozingki,
#  dastur foydalanuvchi yoshini so'rasin va
#  chipta narhini chiqarsin. Foydalanuvchi exit
#  yoki quit deb,yozganda dastur
#  to'xtasin (ikkita shartni ham tekshiring).


# 7. Kiritilgan son boyicha karra jadvali
# tuzadigan dastur tuzing

# 8. Quyidagi lug'at yordamida berilgan
# satrni shakllantiring
# aralash = {
#     'kalit': 'qiymat',
#     'olma': ['qizil', 'sariq', 'yashil'],
#     'car': {
#         'malibu2': {
#             'rangi': 'Qora',
#             'tezligi': '250km/s',
#             'narxi': '27000$',
#         },
#         'Nexia': {
#             'rangi': 'oq',
#             'tezligi': '190km/s',
#             'narxi': 'Bepul'
#         }
#     }
# }
# matn: Oq rangli Malibu avtomili bor narxi 27000$


# 9. Raqamlar ro'yhati berilgan,
# ulardan faqat 5 ga
# bo'linadiganlarini ekrnga chiquvchi
# dastur tuzing.
# sum = [100, 24, 6, 25, 5, 15, 47, 65, 60]


# 10. mashinalar = ['audi','BMW','hyundai']
# shu royhatdagi elementlarni sikl
# operatorlaridan foydalanib ekranga quyidagi
# holatda chiqaring:
# Audi
# BMW
# Hyundai

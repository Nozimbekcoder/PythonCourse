"""
Lesson3
Mavzu: If-elif-else shartlari va Xatolar ustida ishlash
"""

# son1 = int(input('1-Butun son kiriting: '))
# son2 = int(input('2-Butun son kiriting: '))
# son3 = int(input('3-Butun son kiriting: '))
# musbat = 0
# manfiy = 3
#
# if son1 > 0:
#     musbat += 1
#     manfiy -= 1
#
# if son2 > 0:
#     musbat += 1
#     manfiy -= 1
#
# if son3 > 0:
#     musbat += 1
#     manfiy -= 1
# print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy} tasi manfiy.')

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     print('Sizga kirish bepul.')
# elif yosh <= 12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

# son=input('Son kiriting >>')
# # print(bool(son % 2))
# # print(son.isdigit())
# if son.isdigit():
#     son = int(son)
#     if son % 2:
#         print('Siz kiritgan son TOQ')
#     else:
#         print('Siz kiritgan son JUFT')
# else:
#     print("Xurmatli Foydalanuvhi Siz Raqam kiritmadingiz!!!\n"
#           "Iltimos raqam kiriting.")

# and
# or
# not

kun=input("Bugun qanday kun >>")
if kun.lower()== 'shanba' or kun.lower == 'yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun odatiy ish kuni.')

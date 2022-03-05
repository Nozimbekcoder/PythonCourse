"""
Mavzu: While tsikli takrorlash

"""

# son =1  # son ga 1 qiymatini beramiz
# while son <= 5:  # toki son 5 dan kichik yoki teng ekan ...
#     print(son, end=' ')  # sonni konsolga chiqaramiz
#     son += 1  # songa 1 qo'shamiz
#     # son = son + 1
# else:
#     print('Tamom')

# Shartni tekshirish yo'li bilan tsiklni to'xtatish

# print('Kiritilgan sonnimng kvadratini qaytaruvchi dastur.')
# savol = 'Istalgan sonni kiriting\n'
# savol += '(dasturni to\'xtatish uchun \'q\' harfini kiriting) >>>'
# qiymat = ''
# while qiymat != 'q':
#     qiymat = input(savol)
#     if qiymat != 'q':
#         print(int(qiymat) ** 2)
# print("Dastur tugadi.")


# # Ishora bilan tsiklni to'xtatish

# print('Kiritilgan sonnimng kvadratini qaytaruvchi dastur.')
# savol = 'Istalgan sonni kiriting\n'
# savol+='(dasturni to\'xtatish uchun \'q\' harfini kiriting) >>>'
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'q':
#         ishora = False
#     else:
#         print(int(qiymat)**2)
# print("Dastur tugadi.")


# # break funksiyasi yordamida tsiklni to'xtatish
#
# print('Kiritilgan sonnimng kvadratini qaytaruvchi dastur.')
# savol = 'Istalgan sonni kiriting\n'
# savol+='(dasturni to\'xtatish uchun \'q\' harfini kiriting) >>>'
# while True: # abadiy tsikl
#     qiymat = input(savol) # qiymat degan o'zgaruvchiga savolni qoyamiz
#     if qiymat == 'q':  # shartni tekshiramiz
#         break  # tsiklni shu joyda buzamiz
#     else:
#         print(float(qiymat)**2)   # shartdan False qaytsa bajariladi
#

# break tsklida for & while

# sonlar = list(range(1, 11))   # [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kubi {son ** 3} ga teng")

# son = 1
# while son < 11:
#     if son == 5:
#         break
#     print(f"{son} ning kubi {son ** 3} ga teng ")
#     son = son + 1

# continue for tsklida

# sonlar = list(range(1, 11))
# for son in sonlar:
#     if son == 5:
#         continue
#     if son == 1:
#         continue
#     print(f"{son} ning kubi {son ** 3} ga teng")


# # continue while tsiklida
#
# son = 0
# while son < 11:
#     son += 1
#     if son%2==0:
#         continue
#         print(son)
#     else:
#         print(son)


# Infinity loops

# son = 0
# while True:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

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


# Mana yuqorida dostlar royhati shakllantirib oldik endi
# biror top'lamdan qiymatlarni o'chirishni ko'rib chiqamiz

# dostlar = ['hasan','husan','ali','vali','hasan',"g'ani",'hasan']
#
# while 'hasan' in dostlar:
#     dostlar.remove('hasan')
#
# print(dostlar)

# #  Yoki ozgaruvchi yordamida olib taashlashni koramiz
#
# rm = 'hasan'
# while rm in dostlar:
#     dostlar.remove(rm)
#
# print(dostlar)


# # Royhatlarni qayta shakllantirish

# talabalar = ['hasan','husan','olim','salim']
# baholangan_talabalar = []
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar.append(f"{talaba.title()}ning bahosi {int(baho)}")
#
# for baholar in baholangan_talabalar:
#     print(baholar)

# """
# month2, lesson2
# Mavzu : IF shartlari
# """
#
# mevalar = ['olma', 'anor', 'gilos', 'behi']
# mevalar.append('qulpnay')
# mevalar.insert(1, 'nok')
#
# # if 'nok' in mevalar:
# # 	print('Siz kiritgan meva ro\'yhatda mavjud!')
# # else:
# # 	print('Siz kiritgan meva ro\'yhatda mavjud emas!')
#
#
# # son = int(input('Butun son kiriting: '))
# #
# # if son > 0:
# # 	print(son+1)
# # elif son == 0:
# # 	son=10
# # 	print(son)
# # else:
# # 	print(son-2)
#
#
# # if4
# son1 = int(input('1-Butun son kiriting: '))
# son2 = int(input('2-Butun son kiriting: '))
# son3 = int(input('3-Butun son kiriting: '))
# musbat = 0
# manfiy = 3
# if son1 > 0:
# 	musbat += 1
# 	manfiy -=1
# 	if son2 > 0:
# 		musbat += 1
# 		manfiy -= 1
# 		if son3 > 0:
# 			musbat += 1
# 			manfiy -= 1
# 			print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy}tasi manfiy')
# 		else:
# 			print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy}tasi manfiy')
# 	elif son3 > 0:
# 		musbat += 1
# 		manfiy -= 1
# 		print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy}tasi manfiy')
# 	else:
# 		print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy}tasi manfiy')
#
# elif son2 > 0:
# 	musbat += 1
# 	manfiy -= 1
# 	if son3 > 0:
# 		musbat += 1
# 		manfiy -= 1
# 		print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy}tasi manfiy')
# 	else:
# 		print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy}tasi manfiy')
# elif son3 > 0:
# 	musbat += 1
# 	manfiy -= 1
# 	print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy}tasi manfiy')
# else:
# 	print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy}tasi manfiy')
#

son1 = int(input('1-Butun son kiriting: '))
son2 = int(input('2-Butun son kiriting: '))
son3 = int(input('3-Butun son kiriting: '))
musbat = 0
manfiy = 3

if son1 > 0:
    musbat += 1
    manfiy -= 1

if son2 > 0:
    musbat += 1
    manfiy -= 1

if son3 > 0:
    musbat += 1
    manfiy -= 1

print(f'Kiritilgan sonlardan {musbat} tasi musbat, {manfiy} tasi manfiy.')

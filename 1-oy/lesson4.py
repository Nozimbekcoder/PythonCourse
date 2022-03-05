# # Taqqoslash
#
# print(10 != 10)
#
# a = 10
# b = 5
# print(bool(a < b))
#
# d = 4
# c = 5
# print(a > b and c > d)
# print(a > b or c < d)
#
# # And operatori qachonki solishtirilayotgan 2 ta qiymatning ikkalasi ham True
# # qiymat qaytarganida True boladi, qolgan barcha holatlarda False qiymat qaytaradi
# print(True & False)  # and
# print(False | True)  # or
# print(True and False)
# print(False and False)
#
# # or and
#
# # or operatori qachonki solishtirilayotgan 2 ta qiymatning ikkalasidan kamida 1tasi True
# # qiymat qaytarganida True boladi, qolgan barcha holatlarda False qiymat qaytaradi
#
# print(True or True)
# print(True or False)
# print(False or True)
#
# # not
#
# print(True or True)
# print(not (False and True))
# print(not (False and False))
# print(False or not (False))
#
# print(not (not (not (True) or False)) and not (not (not (False) or False)))
#
# # 0				-			1=
#
# a = 0
# b = 0
# print(b is a)
#
# # 6.Membership operatorlari
# # in
# # not in
#
#
# a = 'qoplonvoy'
# b = '1sal2om1 berdik qoplonvoy'
# print(a in b)
#
# b = 'Database setupNow, open up mysite/settings.py.\n' \
# 	' It’s a normal Python module with module-level variables \n' \
# 	'representing Django settings.By default, the configuration uses SQLite.\n' \
# 	'If you’re new to databases, or you’re just interested in trying Django, this is the\n' \
# 	' easiest choice. SQLite is included in Python, so you won’t need to install anything \n' \
# 	'else to support your database. When starting your first real project, however, you may \n' \
# 	'want to use a more scalable database like PostgreSQL, to avoid database-switching \n' \
# 	'headaches down the road.If you wish to use another database, install the appropriate \n' \
# 	'database bindings and change the following keys in the DATABASES \'default\' item \n' \
# 	'to match your database connection settings:'
#
# a = input('Matn kiriting:\n')
# if a in b:
# 	print('Ha siz kiritgan mal\'lumot bizda bor')
# 	print()
# 	print(b)
# else:
# 	print('Afsuski bizda bunday ma\'lumot mavjud emas.\nSorry!!!')
#
# a = (10 != 5)
# b = (10 <= 5)
# print(a is b)

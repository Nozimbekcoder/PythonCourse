"""
lesson1
Muallif: Nozimjon Bozorov
Sana: 16.04.2022
Mavzu: Pythonda try except istisinolar bilan ishlash , requests
"""
# print(12 / 0)

# try:
#     print(a)
# except:
#     print("Voy xato")
# a=12
# b='data'
# y=['sdasefas']
# try:
#     print(a/b)
#     print(a+b)  # xato
#     print(y/2)
# except ZeroDivisionError:
#     print("nolga bo'lish mumkin emas")
#
# except NameError:
#     print("Nomi xato")
# except TypeError:
#     print("Turida xatolik bor")
# except ValueError:
#     print("Qiymat xato")
# except:
#     print("Barchasi Xato")


# try:
#     print("Salom")
#     print(a)
# except :
#     print("Dasturda xatolik bor")
# else:
#     print("Hech qanday xatolik yo'q")
#
# finally:
#     print("Tekshiruv tugadi")

#
# x =int(input("x= "))
#
# if x < 0:
#     raise Exception("Xato")
#     # pass
# else:
#     print(x)


# import json
# import math
#
# math.sqrt(2)
# json.dumps({"a": 1, "b": 2})


import requests
from pprint import pprint as print
try:
    data = requests.get("https://restcountries.com/v3.1/all").json()
    print(data)
    # for name in data:
    #     print(name['capital'])
except:
    print("Internetni tekshirib ko'ring!")

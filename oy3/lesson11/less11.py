
# """
# Python JSON
#
# JSON - bu ma'lumotlarni saqlash va almashish uchun sintaksis.
#
# JSON - JavaScript ob'ekt belgilari bilan yozilgan matn.
#
# Python-da jsonJSON ma'lumotlari bilan ishlash
# uchun ishlatilishi mumkin bo'lgan o'rnatilgan paket mavjud.
#
# JSONni tahlil qilish - JSON-dan Python-ga aylantirish
# Agar sizda JSON satri bo'lsa, uni json.loads()
# usul yordamida tahlil qilishingiz mumkin.
# """


# json1 = {
#     "glossary": {
#         "title": "example glossary",
#         "GlossDiv": {
#             "title": "S",
#             "GlossList": {
#                 "GlossEntry": {
#                     "ID": "SGML",
#                     "SortAs": "SGML",
#                     "GlossTerm": "Standard Generalized Markup Language",
#                     "Acronym": "SGML",
#                     "Abbrev": "ISO 8879:1986",
#                     "GlossDef": {
#                         "para": "A meta-markup language, used to create markup languages such as DocBook.",
#                         "GlossSeeAlso": ["GML", "XML"]
#                     },
#                     "GlossSee": "markup"
#                 }
#             }
#         }
#     }
# }


# """
# JSON-dan Python-ga aylantirish
#
# Agar sizda Python ob'ekti bo'lsa, uni json.dumps()usul yordamida JSON qatoriga aylantirishingiz mumkin.
#
#
# """

# json1 = {"glossary": {"ti\tle": "example glossary", "GlossDiv": {"title": "S", "GlossList": {
#     "GlossEntry": {"ID": "SGML", "SortAs": "SGML", "GlossTerm": "Standard Generalized Markup Language",
#                    "Acronym": "SGML", "Abbrev": "ISO 8879:1986",
#                    "GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.",
#                                 "GlossSeeAlso": ["GML", "XML"]}, "GlossSee": "markup"}}}}}
# print(json1)

# import json
# x =  '{ "ism":"Abror", "yosh":19, "shahar":"Namangan"}'
#
# y = json.loads(x)
#
# print("Assalom",y['ism'])


my = {"nom": 'Python',
      'Sarlavha': 'ФАН-ТЕХНИКА ЯНГИЛИКЛАРИ',
      'batafsil': "Python dasturlash tili yildan-yilga ommalashib bormoqda. "
                  "Bunga birinchi navbatda Pythonning sodda va tushunarli sintaksi sabab bo'lsa, "
                  "ikkinchi va ehtimol eng ko'zga ko'ringan sabab bu"
                  " Pythonning keng qamrovli kutubxonalar to'plamidir.",
      'sana': '12-aprel'
      }
# json1 = json.dumps(my)
# my1 = json.loads(json1)
# print(json1)
# print(my)

"""Biz quyidagi turdagi Python obyektlarini JSON satrlariga aylantirishingiz mumkin:

dict
list
tuple
string
int
float
True
False
None

"""
#
# import json
#
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

#
# "Misol"

import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=2, separators=("; ", " : ")))

print(json.dumps(x))

"""
Natijani formatlash
Yuqoridagi misol JSON satrini chop etadi, lekin uni o'qish unchalik oson emas, hech qanday chekinish va chiziq tanaffuslarisiz.

Usul json.dumps() natijani o'qishni osonlashtiradigan parametrlarga ega:

Misol
indent Chiziqlar sonini aniqlash uchun parametrdan foydalaning :

json.dumps(x, indent=4)
"""

"""
Shuningdek, siz ajratuvchilarni belgilashingiz mumkin, standart qiymat (", ", ": "), bu har bir ob'ektni ajratish uchun vergul va bo'sh joydan, kalitlarni qiymatlardan ajratish uchun esa ikki nuqta va bo'sh joydan foydalanishni anglatadi:

Misol
separatorsStandart ajratgichni o'zgartirish uchun parametrdan foydalaning :

json.dumps(x, indent=4, separators=(". ", " = "))
"""

'''
Natijaga buyurtma bering
Usul json.dumps() natijada kalitlarni buyurtma qilish uchun parametrlarga ega:

Misol
sort_keys Natijani tartiblash kerak yoki yo'qligini aniqlash uchun parametrdan foydalaning :

json.dumps(x, indent=4, sort_keys=True)
'''

"""pip"""


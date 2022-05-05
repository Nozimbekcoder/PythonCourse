"""
lesson2
Muallif: Nozimjon Bozorov
Sana: 19.04.2022
Mavzu: requests paketi, Pythoning tashqi kutubxonasi
"""

# kitobni 92 dan 94 betgacha yodlash
# 10 ta try except misol
# 2ta web saytdan json fayl olish
# 3 raise holatga misol
# r = requests.get('https://api.github.com/users/nodirbek')
# r1 = requests.get('https://google.com')
# print(r.status_code) # so'rovnoma natijasi
# print(r.text) # text natijasi
# print() # json natijasi
#
# kundalik = requests.get('https://kundalik.com')
# print(kundalik.json())
# import wikipedia
#
# wikipedia.set_lang("uz")
#
# a=wikipedia.summary('Python')
# print(a)
#
# from pprint import pprint as print
#
# import wikipedia
#
# while True:
#     search = input("Iltimos, so'zni kiriting: ")
#     # til=input("Iltimos, tilni kiriting: ")
#     qt = wikipedia.set_lang('uz')
#     if search != "q":
#         try:
#             res = wikipedia.search(search)
#             print(res)
#             qaysi = input('Tanlang: ')
#
#             # wikipedia.set_lang("uz")
#             a = wikipedia.summary(qaysi)
#             print(a)
#         except:
#             print("Iltimos, Internetga ulanishni tekshirib koring!")
#     else:
#         break

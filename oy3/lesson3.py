"""
Muallif: Nozimjon Bozorov
Sana: 24.03.2022
Mavzu: Funksiyalar
"""

# """"So'z Topish oyini"""
# import random  # Random moulini yuklab oldik
#
# stages = ["""
#   +---+
#   |   |
#   o   |
#  /|\  |
#  / \  |
#       |
# ==========
# """, """
#   +---+
#   |   |
#   o   |
#  /|\  |
#  /    |
#       |
# ==========
# """, """
#   +---+
#   |   |
#   o   |
#  /|\  |
#       |
#       |
# ==========
# """, """
#   +---+
#   |   |
#   o   |
#  /|   |
#       |
#       |
# ==========
# """, """
#   +---+
#   |   |
#   o   |
#   |   |
#       |
#       |
# ==========
# """, """
#   +---+
#   |   |
#   o   |
#       |
#       |
#       |
# ==========
# """, """
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# ==========
# """]
#
# words = ['lola', 'banan', 'book']  # Sozlar royhatini tuzamiz
# tsoz = random.choice(words)  # Sozlar royhatida tasodifiy sozni tanlab olamiz
# # va uni tsoz nomli ozgaruvchiga yuklaymiz
# # _____________________________________________________________________________
#
# # print(f"Yasaladigan soz '{tsoz}'")
# # # Vaqtinchalik ekranga sozni chiqarib turamiz albatta ozimiz uchun
# # ----------------------------------------------------------------------------
# word_len = len(tsoz)
# display = []  # display nomli bosh royhat yaratib olamiz
# for _ in range(word_len):  # Tanlagan sozimiz uzunligidagi _ paski chiziqlarni displayga qoshib olamiz
#     display += "_"
# print(display)  # display ni ekranga chiqaramiz
# # ----------------------------------------------------------------------------
#
# gameover = True  # Ishora ozgaruvchi yaratamiz
# jon = 6  # Oyinni tugatish uchun xatolar sonini qoyib olamiz
#
# while gameover:  # Cheksiz siklni yaratib olamiz
#     ksoz = input('Harf kiriting: ').lower()  # foydalanuvchida harf kiritishni soraymiz va ksoz ga qiymatini olamiz
#     for orni in range(word_len):  # for sikli yordamida tanlangan soz uzunligidagi sikl hosil qilamiz
#         harf = tsoz[orni]
#         if ksoz == tsoz[orni]:
#             display[orni] = harf
#             # print("To'g'ri")
#         # else:
#         #     print("Noto'g'ri")
#     print(f"{' '.join(display)}")  # Ekranda ochilgan harflarni korsatamiz
#
#     if "_" not in display:
#         gameover = False
#         print('You Win! | Siz yutdingiz!')
#
#     # -------------------------------------------------------------------------------------------
#     # O'yinda xatolar uchun yutqazish shartini yozamiz
#     if ksoz not in tsoz:  # kiritilgan harf tanlangan sozda yoq bo'lsa
#         jon -= 1  # jon nomli ozgaruvchidan 1 ayiramiz
#         if jon == 0:  # jon nomli ozgaruvchi qiymati 0 ga teng bolsa
#             gameover = False  # gameover nomli ishora ozgaruvchini qiymatini Falsega almashtirib oyinni tugatamiz
#             print("You Lose!")  # # Foydalanuvchi yutqazganligi haqida xabar beramiz va oyin tugaydi
#
#     print(stages[jon])

# # Funksiyalarga misollar:
# bool()
# complex(x)
# dict()
# float()
# int()


# def salomlash():
#     pass

# def salomlash():
#     '''Bu funksiyamiz bizga salom beradi'''
#     print("Assalomu Alaykum")
#
# salomlash()

# def salomlash(ism):
#     '''Foydalanuvchi ismi boyicha salom beradigan funksiya'''
#     print(f"Assalomu Alaykum {ism}")
#
# salomlash('Abror')
#
# ozgaruvchilar 2 xil turi mavjud:
# local   va  global

"""Tubsonlar sonlar"""
def tubson(son):
    """
        son parametriga berilgan argumentni tub ekanligiga tekshiradi
        :param son:
        :return:
        """
    # for i in range(2,son-1):
    #     if son % i ==0:
    #         print("Siz kiritgan son tub son emas")
    #         continue
    #     else:
    #         print("Tub son")

    # tub = True
    #     for i in range(2,son-1    ):
    #         if son % i == 0:
    #             tub = False
    #     if tub:
    #         print(f"Siz kiritgan {son} tub son.")
    #     else:
    #         print(f"Siz kiritgan {son} tub son emas.")
tubson(7)


# """Shifrlash dasturi"""

# alifbo = ['a', 'b', 'c','d', 'e', 'f','g', 'h', 'i',
#           'j', 'k', 'l','m', 'n', 'o','p', 'q', 'r',
#           's', 't', 'u','v', 'w', 'x','y', 'z']


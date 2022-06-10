# """Klasslar Inkapsulyatsiya va database"""
# def chiqar(*args):
#     print(*args)
#
# class Telefon:
#     __hisob = 0
#     def __init__(self, model, rang, narxi, vaqti):
#         """Telefon obyektining xususiyatlari"""
#
#         self.model = model
#         self.rang = rang
#         self.narxi = narxi
#         self.__vaqti = vaqti
#         Telefon.__hisob +=1
#
#     def info(self):
#         return f"{self.rang} rangli {self.model} Telefoni\n" \
#                f"narxi {self.narxi},\n" \
#                f"Ishlagan vaqti {self.__vaqti} soat"
#
#     def add_vaqt(self, time):
#         """Vaqtini o'zgartirish faqat + tomonga"""
#         if time > 0:
#             self.__vaqti += time
#         else:
#             chiqar("Siz Telefonnning ishlatilgan vaqtini kamaytira olmaysiz.")
#
# #
# # tel1 = Telefon(model='Samsung', rang='Qora', narxi=750000, vaqti=1000)
# # tel2 = Telefon(model='Redmi', rang='Oq', narxi=1750000, vaqti=100)
# # tel3 = Telefon('Oppo Reno 7', rang='hamelion', narxi=200000, vaqti=50)
# # tel4 = Telefon('LG', 'Yashil', 20000, 2000)




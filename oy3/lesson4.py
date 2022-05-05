"""
Muallif: Nozimjon Bozorov
Sana: 26.03.2022
Mavzu: Funksiyalar davomi
"""

"""Tubsonlar sonlar"""


def tubson(son):
    """
        son parametriga berilgan argumentni tub ekanligiga tekshiradi
        :param son:
        :return:
        """
    tub = True
    for i in range(2, son):
        if son % i == 0:
            tub = False
    if tub:
        print(f"Siz kiritgan {son} tub son.")
    else:
        print(f"Siz kiritgan {son} tub son emas.")

tubson()

"""Shifrlash dasturi"""


#
# alifbo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
#           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',
#           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# while True:
#     tur = input("Turi 'encode' - Shifrlash yoki 'decode' - Shifrdan chiqarish:").lower()
#     matn = input("Matninggizni kiriting:").lower()
#     raqam = int(input("Shifrlash raqami:"))
#
#
#     # shifrlangan = ""
#     # for harf in matn:
#     #     orni = alifbo.index(harf)
#     #     # print('asl orni',orni)
#     #     yangiorni = orni + raqam
#     #     # print('yangiorni',yangiorni)
#     #     yangiharf = alifbo[yangiorni]
#     #     shifrlangan += yangiharf
#     # print('shiflangan matn', shifrlangan)
#
#     def shifrlash(matn, raqam):
#         shifrlangan = ""
#         for harf in matn:
#             orni = alifbo.index(harf)
#             # print('asl orni',orni)
#             yangiorni = orni + raqam
#             # print('yangiorni',yangiorni)
#             yangiharf = alifbo[yangiorni]
#             shifrlangan += yangiharf
#         print('shiflangan matn', shifrlangan)
#
#
#     def deshifrlash(matn, raqam):
#         shifrlangan = ""
#         for harf in matn:
#             orni = alifbo.index(harf)
#             # print('asl orni',orni)
#             yangiorni = orni - raqam
#             # print('yangiorni',yangiorni)
#             yangiharf = alifbo[yangiorni]
#             shifrlangan += yangiharf
#         print('shiflangan matn', shifrlangan)
#
#
#     if tur == 'encode':
#         shifrlash(matn, raqam)
#     elif tur == 'decode':
#         deshifrlash(matn, raqam)

def toliq_ism(ism, familya):
    print(f'Ism: {ism}\n'
          f'Familya: {familya}')
# toliq_ism('Nozimjon', 'Bozorov')
# toliq_ism(familya='Bozorov',ism='Nozimjon')


def summa(*sonlar):
    # yigindi = 0
    # for son in sonlar:
    #     yigindi +=son
    # print(yigindi)
    print(sum(sonlar))

summa(5,4,8,3)
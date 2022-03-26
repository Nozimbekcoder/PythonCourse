# def tubson(son):
#     """
#     son parametriga berilgan argumentni tub ekanligiga tekshiradi
#     :param son:
#     :return:
#     """
#     tub =True
#     for i in range(2,son-1    ):
#         if son % i == 0:
#             tub = False
#     if tub:
#         print(f"Siz kiritgan {son} tub son.")
#     else:
#         print(f"Siz kiritgan {son} tub son emas.")
#
# tubson()

art = '''
:'`'', ||  || "" ||==== ||'"'";
\...., ||==|| || ||==   ||----/
...../ ||  || || ||     ||    \\

||"'\   ||'"'"  :'`'', ||  || "" ||==== ||'"'"\\
||   |  ||"'    |...., ||==|| || ||==   ||----/
||__/   ||____  .....| ||  || || ||     ||    \\
'''

print(art)

alifbo = ['a', 'b', 'c',
          'd', 'e', 'f',
          'g', 'h', 'i',
          'j', 'k', 'l',
          'm', 'n', 'o',
          'p', 'q', 'r',
          's', 't', 'u',
          'v', 'w', 'x',
          'y', 'z','a', 'b', 'c',
          'd', 'e', 'f',
          'g', 'h', 'i',
          'j', 'k', 'l',
          'm', 'n', 'o',
          'p', 'q', 'r',
          's', 't', 'u',
          'v', 'w', 'x',
          'y', 'z','a', 'b', 'c',
          'd', 'e', 'f',
          'g', 'h', 'i',
          'j', 'k', 'l',
          'm', 'n', 'o',
          'p', 'q', 'r',
          's', 't', 'u',
          'v', 'w', 'x',
          'y', 'z',]

yonalish = input("Turi 'encode' - Shifrlash yoki 'decode' - Shifdan chiqarish:")
matn = input("Matninggizni kiriting: ")
shifr = int(input("Shifrlash raqami: "))

print(art)
def shifrlash(text, surilish):
    shifrlangan = ""
    for harf in text:
        orni = alifbo.index(harf)
        yangiorni = orni + surilish
        yangiharf = alifbo[yangiorni]
        shifrlangan += yangiharf
    print(f"Sizni shifrlangan matn: '{shifrlangan}'")


def deshifrlash(text, surilish):
    deshifr = ""
    for harf in text:
        orni = alifbo.index(harf)
        yangiorni = orni - surilish
        yangiharf = alifbo[yangiorni]
        deshifr += yangiharf
    print(f"Sizni shifrlangan matn: '{deshifr}'")

#
if yonalish == 'encode':
    shifrlash(matn, shifr)
elif yonalish == 'decode':
    deshifrlash(matn, shifr)


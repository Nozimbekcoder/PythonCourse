# """
# lesson6
# Mavzu: Pythonning lug'atlari (dict)
# """
# #
# # inglizcha-Uzbekcha
# #
# # apple   -   olma
# # program   - dastur
# # programmer  - dasturchi
# # programming  - dasturlash
#
# # {key: value} shu narsa dict deb ataladi
#
# # sonlar = {'salom','ali','for','ruchka','daftar'}
# # print(sonlar)
# #
# # enuz = {
# #     'apple': 'Olma',
# #     'program':'Dastur',
# #     'mouse':'sichqoncha',
# #     'book':'Kitob',
# #     'pen':'ruchka',
# #     'pencil':'qalam',
# #     'one':1,
# #     4:'to\'rt'
# # }
# #
# # print(enuz,'\n')
# #
# # # print(enuz['mouse'])
# # print(enuz.keys())


# from pprint import pprint as print
# mashina = {
#     'car':'mashina',
#     'car0':{
#         'rusumi':'MERS',
#         'rangi':{'oq','qora','yashil','sariq'},
#         'tezlik':'190 km/s',
#         'yili':2015,
#         'narxi':'25000$'
#     }
# }
# print(mashina)
# print(f"Yangi turdagi avtomobil {mashina['car0']['rusumi'].title()} sotuvda narxi {mashina['car0']['narxi']}")


talaba1 = {}
talaba1['ismi'] = 'Jahongir'
talaba1['familyasi'] = 'Abdug\'afforov'
talaba1['tyil'] = 2007
talaba1['kurs'] = 1.5j

talaba1['telefon'] = 'Redmi'
talaba1['raqami'] = '+998 93 753 26 67'

talaba2 ={}
talaba2['ismi']='Abdurauf'

print(f"{talaba1['ismi'].title()} va {talaba2['ismi'].title()} ikkalasi bir xoanada o\'tirishibdi.\n"
      f"shu payt {talaba2['ismi']} ketgisi kelib qoldi va {talaba1['telefon']}dan uydagi {talaba1['raqami']} qo\'ng\'iroq qildi")
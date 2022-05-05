"""
Mavzu: Dict davomi dict lar ustida amallar
"""
from pprint import pprint as print

aralash = {
    'kalit': 'qiymat',
    'olma': ['qizil', 'sariq', 'yashil'],
    'car': {
        'malibu2': {
            'rangi': 'Qora',
            'tezligi': '250km/s',
            'narxi': '27000$',
        },
        'Nexia': {
            'rangi': 'oq',
            'tezligi': '190km/s',
            'narxi': 'Bepul'
        }
    }
}

# print(aralash['car']['Nexia']['tezligi'])

# # .get()
# print(aralash['car']['Nexia'].get('tezlik','Bunday kalit so\'z topilmadi'))

# print(aralash.items())
# print(aralash['car'].keys())
# print(aralash)
# Kalit : apple
# Qiymat : olma

talaba = {
    'ism': 'alijon',
    'familiya': 'valiyev',
    'yosh': 22,
    'fakultet': 'matematika',
    'kurs': 4
}
#
# for kalit, qiymat in talaba.items():
#     print(f"Kalit : {kalit}\n"
#           f"Qiymat: {qiymat}")
#     print()


mahsulotlar = {
    'olma': 7000,
    'banan': 19500,
    'go\'sht': 68000,
    'kartoshka': 5000,
    'piyoz': 3000
}
# # dictdan kalitlarni olish
# print(mahsulotlar.keys())
#
# print('Do\'kondagi mahsulotlar')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot)
#
# # dictdan qiymatlarni olish
# print(mahsulotlar.values())
#
# print('Do\'kondagi mahsulotlar')
# for mahsulot in mahsulotlar.values():
#     print(mahsulot)

telfonlar = {
    'jahongir': 'Samsung A6',
    'abror': 'Redmi 6 Pro',
    'Muhammadjon': 'LG X6',
    'Abdurauf': 'Samsung A6',
    'Alisher': 'Samsung A20',
    'Abdulaziz': 'Samsung A02',
    'Mirziyo': 'Redmi 6',
    'Rahmatillo': 'Redmi 7'
}
# for ism ,  tel in telfonlar.items():
#     print(f'{ism.title()}ning {tel.upper()}')


# Dictning qiymatini almashtirish
telfonlar['Nozimjon'] = 'Samsung J2'
telfonlar['Nozimjon'] = 'Huawei P9'
telfonlar['Mirza'] = 'Nokia'

print(telfonlar)

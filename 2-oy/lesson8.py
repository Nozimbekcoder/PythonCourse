# from pprint import pprint as print
telefonlar = {
    'jahongir': 'Samsung',
    'abror': 'Redmi',
    'Muhammadjon': 'LG',
    'Abdurauf': 'Samsung',
    'Alisher': 'Samsung',
    'Abdulaziz': 'Samsung',
    'Mirziyo': 'Redmi',
    'Rahmatillo': 'Redmi'
}
# print(telefonlar)
# print('Telefonlar: ')
# for tel in set(telefonlar.values()):
#     print(tel)


# qiymatlarni o'chirib tashlash
# del telefonlar['Mirziyo']
# print(telefonlar)


'''Mavzu : while  '''


# for x in telefonlar:
#     print(x)
#
# a=10
# b=11
#
# if b!=a:
#     print()
# else:
#     print()

# while True:
#     print('Python')
# a=1
# while a<5:
#     print('Python')
# else:
#     print('Tamom')

ismlar = []
print('dasturdan chiqish uchun \'q\' harfini kiriting ')
ishora=True
while ishora:
    ism =input('Do\'stingizni ismmini kiriting >>>')
    if ism=='q':
        ishora=False
        print(ismlar)
    ismlar.append(ism)

for i in ismlar:
    if i=='q':
        continue
    print(i)
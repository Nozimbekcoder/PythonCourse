# lesson11
# Mavzu : Barcha o'tilgan darslarimiz bo'yicha misollar yechish
# Tushunmagan joylarni o'rganib olish

mevalar = ['olma', 'anor', 'shaftoli', 'gilos', 'banan', 'behi']
# print(f'Men {mevalar[0]}ni yaxshi ko\'raman')
# print(f'Men {mevalar[1]}ni yaxshi ko\'raman')
# print(f'Men {mevalar[2]}ni yaxshi ko\'raman')
# print(f'Men {mevalar[3]}ni yaxshi ko\'raman')
# print(f'Men {mevalar[4]}ni yaxshi ko\'raman')
# for i in mevalar:  #[1,2,3,4,5,6,7,8,9,10]
#     if i == 'olma':
#         continue
#     if i=='behi':
#         continue
#     print(f"Men {i}ni yaxshi ko\'raman")
#     if i == 'gilos':
#         break
# else:
#     print('Tsikl tugadi')

# for ism in 'Abdurauf':
#     print(ism)
#     print("Abdurauf")
#
# i = True
# son = 1
# while i:
#     son += 1
#     if son % 2 == 0:
#         print(son)
#         if son == 1000:
#             i=False


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print (n, 'is a prime number')
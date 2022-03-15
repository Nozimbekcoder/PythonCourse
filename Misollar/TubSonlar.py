n = int(input("Nechagacha bo'lgan tub sum kerak: "))

for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

# numbers = int(input("Nechagacha bo'lgan tub sum kerak: "))
#
# for n in range(2, numbers):
#     for x in range(2, n):
#         if n % x == 0:
#             # print(n, 'Teng', x, '*', n // x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'Tub son')

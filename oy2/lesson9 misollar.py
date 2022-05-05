# while1

# a = int(input('1-sonni kirit: '))
# b = int(input('2-sonni kirit: '))
#
# while a>=b:
#     a=a-b
# else:
#     print(a)
#

# while2
# a = int(input('1-sonni kirit: '))
# b = int(input('2-sonni kirit: '))
# hisob = 0
# while a >= b:
#     a = a - b
#     hisob += 1
# else:
#     print(hisob)

# while3
# n = int(input('N butun sonni kiriting (N>0):'))
# k = int(input('K butun sonni kiriting (K>0):'))
# butun = 0
# while n >= k:
#     n = n - k
#     # n -= k
#     butun += 1
# else:
#     print(f"{butun} butun, {n} Qoldiq")

# while4
# n= int(input("N sonni kiriting (N>0) : "))
# s=n+0
# while n>=3:
#     n=n-3
#     if n==0:
#         print(f'{s} soni 3 ning darajasi')
#     elif n<3 and n>0:
#         print(f'{s} soni 3 ning darajasi emas!')

print("Keling siz bilan sevimli mevalaringizni royhatini tuzamiz")
mevalar = []
soni = 1
while True:
    savol = f"{soni}-sevimli mevangizni nomini kiriting: "
    meva = input(savol)
    mevalar.append(meva)
    takror = input("Yana meva qo'shasizmi (ha/yoq) ? :")
    soni=soni+1
    if takror.lower()=='yoq':
        break
print(mevalar)
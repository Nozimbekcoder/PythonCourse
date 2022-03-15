# # 1.
# # sum = [4, 5, 7, 9, 5, 4, 58, 5, 4]
# # sonlaruzunligi=len(sum)
# # print(sonlaruzunligi)
# # 2.
# # element=list(range(0,11))
# # print(element[0],element[1],element[4],element[-1])
#
# # 3.
# taomlar=[]
# taomlar.append('manti')
# taomlar.append('osh')
# taomlar.append('kabob')
# taomlar.append('somsa')
# taomlar.append('shor\'rva')
#
#
# # print(taomlar)
#
#
# # 4.
# # nonushta=taomlar[:]
# nonushta=taomlar.copy()
# del nonushta[0:3]
# nonushta.append('salat')
# nonushta.insert(0,'Baliq')
# # print(nonushta)
#
# # 5.
#
# print(nonushta,)
# print(taomlar)
#
# tup=tuple(nonushta)
# tup[0]='qaymoq va non'
# print(tup)

# son = input('Uch xonali son kiriting (100/999) : ')
# yuzlar = son[0]
# onlar = son[1]
# birlar = son[2]
# print(son)
# print(onlar+birlar+yuzlar)

# Integer17
# 1234
# son = input('4 xonali son kiriting 999< : ')
# son = int(son)
# butun = son % 1000
# natija = butun // 100
# print(butun)
# print(natija)

# Integer18
# 1234
# son = input('4 xonali son kiriting 999< : ')
# son = int(son)
# # butun = son % 10000
# natija = son // 1000
# print(son)
# print(natija)

# Integer19

n = int(input('O\'tgan vaqtni sekundlarda kiriting: '))
print(f'shuncha daqiqa vaqt o\'tdi   {n // 60}')

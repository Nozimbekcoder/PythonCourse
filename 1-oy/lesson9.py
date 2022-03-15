"""
09-dars

Mavzu: List
"""

# soz='yer'
# sozlar = ['yer','rucka','qalam']
# sum = [0,5,9,6,1,11,36.6,273,-81,'sichqon']
# print(type(a))
# print(sozlar[2])
# print(soz)
# print(sum)

sonlar = [7, 5, 9, -81, '5', '9', 'sichqon']
mevalar = ['olma', 'Banan', 'Kivi', 'Shaftoli', 'Mandarin']
# print(sum[1]+sum[2])
# print(sum[4]+sum[5])
# sum[0] = 'Nol'
# sum[-2] = 'Nol'
# print(sum)
# print('Meva :',mevalar[0].title(),mevalar[2].lower())
# mevalar.append('yangi')
# mevalar.append('2')
# mevalar.append(5)
# mevalar.append('salom')
# mevalar.append('ruchka')
# mevalar.insert(1, 'salom')
# mevalar.insert(3, 'salom')
# print(mevalar)
# ismlar=[]
# ismlar.append('Jahongir')
# ismlar.append('Alisher ')
# ismlar.append('Asqarxon')
#
# print(ismlar)

dostlar = ['Hasan', 'Husan', 'Hasan', 'Olim', 'Mahmud']
# del dostlar[1] # listdan Inedks yordamida olib tashlash uchun del
# del dostlar[-1]
# dostlar.remove('Hasan') #.remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi. Agar ro'yxatning ichida 2 va undan ko'p bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.
# dostlar.remove('Hasan')
# a=dostlar[3] # listning 3 indexdagi elementidan nusxa oladi.
# print(a)
so2=dostlar.pop() # listning oxiridan 1 elementni sug`urib oladi.
print(so2)
so2=dostlar.pop()
print(so2)
so1 = dostlar.pop(2)
print(so1)
print(dostlar)

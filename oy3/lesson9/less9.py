"""
lesson8
Muallif: Nozimjon Bozorov
Sana: 07.04.2022
Mavzu: Pythonning standart kutubxonasi
"""
import datetime as dt

hozir = dt.datetime.now()

print(hozir)
# print(hozir.strftime('%A'))
# print(hozir.strftime('%B'))
# # print(hozir.strftime('%w'))
# print(hozir.strftime('%Y'))
# print(hozir.strftime('%I'),':',hozir.strftime('%M'))
# # sanani ajratib olish
# print(hozir.date())
#
# # vaqt ajratib olish
# print(hozir.time())
#
# # soatni ajratib olish
# print(hozir.hour)
#
# # daqiqani ajratib olish
# print(hozir.minute)
#
# # sekund ajratib olish
# print(hozir.second)
#
# bugun = dt.datetime.today()
# print(f'Bugungi sana: {bugun}')
#
# bayram = dt.datetime(2022, 5, 9, 14, 00, 00)
# kunqoldi = bayram - bugun
# print(f'Bayramga {kunqoldi} kun qoldi')
#
# vaqt = hozir.strftime('%H:%M:%S')

# tkun=dt.datetime(2003,2,23,00,00,00)
# today = dt.datetime.now()
# kuno=today-tkun
#
# print(f'Siz tugilganinggizdan beri {kuno} o\'tdi')

# import math
# print(dir(math))

# from math import *
# #
# # ildiz = sqrt(64)
# # PI = pi
# # print(PI)
#
# x = 7.4
#
# print(x)
# print(floor(x))
# print(ceil(x))
#
# import re
#
# matn = 'lola'
# matn1 = 'lolo'
# shablon = '^(?=.*?[AZ])(?=.*?[az])(?=.*?[0-9])(?=.*?[#?!@$ %^&*- ]).{8,}$'
# print(re.match(shablon, matn))
# print(re.match(shablon, matn1))
"""
Math va cmath modullarida haqiqiy va compleksli argumentlar uchun matematik funksiyalar 
to`plangan. Bu C tilida foydalaniladigan funksiyalar. Quyida math modulining funksiyalari 
keltirilgan. Qayerda z harfi bilan argumentga belgilash kiritilgan bo`lsa, u cmath modulidagi 
analogik funksiya ham shunday belgilanishini bildiradi.
 acos(z)-arkkosinus z.
 asin(z)- arksinus z.
 atan(z)- arktangens z.
 atan2(y, x)- atan(y/x).
 ceil(x)- x ga teng yoki katta eng kichik butun son.
 cos(z)- kosinus z. 
 cosh(x)- giperbolik x kosinusi.
 e- e konstantasi.
 exp(z)- eksponenta (bu degani e**z)
 fabs(x)-x absolute raqami.
 floor(x)- xga teng yoki kichik eng katta butun son
 fmod(x,y)- x ni y ga bo`lgandagi qoldiq qism.
 frexp(x)- mantisa va tartibni (m, i) juftligi kabi qaytaradi, m- o`zgaruvchan nuqtali son, i 
esa- x=m*2**i ga teng butun son bo`ladi. Agarda 0-(0,0) qaytarsa boshqa paytda 
0.5<=abs(m)<1.0 bo`ladi.
 factorial(x)- x ning faktoriali. N!=1*2*3*…*n
 hypot(x,y)- sqrt(x*x+y*y)
 ldexp(m,i)- m*(2**i).
 log(z)- natural logarifm z.
 log10(z)- o`nlik logarifm z.

 log2(z)-logarifm ikki asosga ko`ra z.
 modf(x)- (y,q) juftlikda x ning butun va kasr qismini qaytaradi.
 pi-pi konstantasi.
 pow(x,y)- x**y.
 sin(z)- z ning sinusi.
 sinh(z)- z ning giperbolik sinusi.
 sqrt(z)- z ning kvadrat ildizi.
 tan(z)- z ning tangensi.
 tanh(z)- z ning giperbolik tangensi.
 trunc(x)- x haqiqiy sonning butun qismini qaytaradi.
 degrees(x)-x ni radiandan gradusga o`tkazish.
 radians(x)- x ni gradusdan radianga o`tkazish.
math.ceil() funksiyasi eng yaqin yuqori butun songacha yaxlitlaydi. 
math.floor() funksiyasi esa eng yaqin pastki butun songacha yaxlitlaydi.
"""
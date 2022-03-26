"""
Muallif: Nozimjon Bozorov
Sana: 17.03.2022
Mavzu: Takrorlash
"""

# # for11
# n = int(input("N butun sonni kiriting: "))
# sum= 0
# for son in range(1,n+1):
#     # print(son)
#     sum = sum +pow(2*n,2)
#     # print(sum)
# print(sum)
#

# son
# 3 ga bolinsa :    Fizz     3,6,9,12,15,18,21,24,27,30
# 5 ga bolinsa :    Buzz     5,10,15,20,25,30,35
# 3 va 5 bolinsa :  FizzBuzz 15,30,45,60
# 3 va 5 bolinmasa :  son    1,2,4,6,7,8,9,11
# son bolmasa:  Siz son kiritmadingiz  fhaufhasa@!#$%%^


""""So'z Topish oyini"""


import random  # Random moulini yuklab oldik

words = ['lola', 'banan', 'book']  # Sozlar royhatini tuzamiz
tsoz = random.choice(words)  # Sozlar royhatida tasodifiy sozni tanlab olamiz
# va uni tsoz nomli ozgaruvchiga yuklaymiz
# _____________________________________________________________________________

# print(f"Yasaladigan soz '{tsoz}'")
# # Vaqtinchalik ekranga sozni chiqarib turamiz albatta ozimiz uchun
# ----------------------------------------------------------------------------
word_len = len(tsoz)
display = []  # display nomli bosh royhat yaratib olamiz
for _ in range(word_len):  # Tanlagan sozimiz uzunligidagi _ paski chiziqlarni displayga qoshib olamiz
    display += "_"
print(display)  # display ni ekranga chiqaramiz
# ----------------------------------------------------------------------------

gameover = True  # Ishora ozgaruvchi yaratamiz
jon = 3  # Oyinni tugatish uchun xatolar sonini qoyib olamiz

while gameover:  # Cheksiz siklni yaratib olamiz
    ksoz = input('Harf kiriting: ').lower()  # foydalanuvchida harf kiritishni soraymiz va ksoz ga qiymatini olamiz
    for orni in range(word_len):  # for sikli yordamida tanlangan soz uzunligidagi sikl hosil qilamiz
        harf = tsoz[orni]
        if ksoz == tsoz[orni]:
            display[orni] = harf
            # print("To'g'ri")
        # else:
        #     print("Noto'g'ri")
    print(f"{' '.join(display)}")  # Ekranda ochilgan harflarni korsatamiz

    if '_' not in tsoz:
        gameover = False
        print('You Win! | Siz yutdingiz!')


    #-------------------------------------------------------------------------------------------
    # O'yinda xatolar uchun yutqazish shartini yozamiz
    if ksoz not in tsoz:  # kiritilgan harf tanlangan sozda yoq bo'lsa
        jon -= 1  # jon nomli ozgaruvchidan 1 ayiramiz
        if jon == 0:  # jon nomli ozgaruvchi qiymati 0 ga teng bolsa
            gameover = False  # gameover nomli ishora ozgaruvchini qiymatini Falsega almashtirib oyinni tugatamiz
            print("You Lose!")  # # Foydalanuvchi yutqazganligi haqida xabar beramiz va oyin tugaydi

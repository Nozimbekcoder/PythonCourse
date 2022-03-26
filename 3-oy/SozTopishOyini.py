
""""So'z Topish oyini"""


import random  # Random moulini yuklab oldik

words = ['lola', 'banan', 'book']  # Sozlar royhatini tuzamiz
tsoz = random.choice(words)  # Sozlar royhatida tasodifiy sozni tanlab olamiz
# va uni tsoz nomli ozgaruvchiga yuklaymiz
# _____________________________________________________________________________

# print(f"Yasaladigan soz '{tsoz}'")
# # Vaqtinchalik ekranga sozni chiqarib turamiz albatta ozimiz uchun
# ----------------------------------------------------------------------------

display = []  # display nomli bosh royhat yaratib olamiz
for _ in range(len(tsoz)):  # Tanlagan sozimiz uzunligidagi _ paski chiziqlarni displayga qoshin olamiz
    display += "_"
print(display)  # display ni ekranga chiqaramiz
# ----------------------------------------------------------------------------

gameover = True  # Ishora ozgaruvchi yaratamiz
jon = 3  # Oyinni tugatish uchun xatolar sonini qoyib olamiz

while gameover:  # Cheksiz siklni yaratib olamiz
    ksoz = input('Harf kiriting: ').lower()  # foydalanuvchida harf kiritishni soraymiz va ksoz ga qiymatini olamiz
    for orni in range(len(tsoz)):  # for sikli yordamida tanlangan soz uzunligidagi sikl hosil qilamiz
        harf = tsoz[orni]
        if ksoz == tsoz[orni]:
            display[orni] = harf
            # print("To'g'ri")
        # else:
        #     print("Noto'g'ri")
    print(f"{' '.join(display)}")  # Ekranda ochilgan harflarni korsatamiz

    if ksoz not in tsoz:  # kiritilgan harf tanlangan sozda yoq bo'lsa
        jon -= 1  # jon nomli ozgaruvchidan 1 ayiramiz
        if jon == 0:  # jon nomli ozgaruvchi qiymati 0 ga teng bolsa
            gameover = False  # gameover nomli ishora ozgaruvchini qiymatini Falsega almashtirib oyinni tugatamiz
            print("You Lose!")  # # Foydalanuvchi yutqazganligi haqida xabar beramiz va oyin tugaydi

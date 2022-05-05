def kirit(matn):
    return input(matn)


over = True

while over:
    yana = kirit("Ma'lumot qo'shasizmi?(tugatish 'q'): ")
    if yana != 'q':
        ism = input("Ismingiz: ").title()
        fam = input("Familyangiz: ").title()
        tel = kirit("Telefon raqamingiz(93 057 66 03): ")
        with open('./royhat.txt', 'a') as f:
            f.write(f'\n'
                    f'Ismingiz: {ism}\n'
                    f'Familyangiz: {fam}\n'
                    f'Telefon raqamingiz: +998 {tel}\n'
                    f'----------------------------------------------------\n')
        print("Ma'lumotlar muvaffaqiyatli saqlandi!\n")

    else:
        over = False
        print('Dastur Yakunlandi')
        with open('./royhat.txt', 'r') as f:
            print(f.read())

input()

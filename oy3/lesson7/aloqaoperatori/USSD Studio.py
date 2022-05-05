while True:
    print("USSD STUDIO")
    aloqaoperatori = int(input("Siz qaysi aloqa operatoridan foydalanasiz\n"
                               "1) Ucell\n"
                               "2) UzMobile\n"
                               "3) MobiUz\n"
                               "4) Beeline\n"
                               "5) Perfectum mobile\n"
                               "Tanlang:"))
    print()
    while True:
        if aloqaoperatori == 1:
            print("📱📲 Ucell 📱📲\n"
                  "Hayotni yaxshilik sari o'zgartirib!")
            tanlov = int(input("Sizga qanday xizmat turi kerak\n"
                               "1) USSD kodlar\n"
                               "2) Tarif rejalari \n"
                               "3) Internet paketlar \n"
                               "4) Daqiqa paketlar\n"
                               "5) SMS paketlar \n"
                               "6) Qo'shimcha xizmatlar\n"
                               "0) Ortga qaytish --^\n"
                               "Tanlang:"))
            print()

            if tanlov == 0:
                break
            elif tanlov == None:
                break
            elif tanlov == 1:
                while True:
                    print("USSD kodlar")
                    kodlar = int(input("  Telefonning IMEI-kodini bilib oling -- *#06# \n"
                                       "  Balansni tekshirish -- *100# \n"
                                       "  Bonus daqiqalar qoldi'gini tekshirish -- *102# \n"
                                       "  Internet to'plamlar qoldig'ini tekshirish -- *107# \n"
                                       "  SMS to'plamlar qoldig'ini tekshirish -- *147# \n"
                                       "  Limitlar qoldigini tekshirish -- *103# \n"
                                       "  Mening raqamim -- *450# \n"
                                       "  Mobil avans (Qarz olish) -- *911# \n"
                                       "  Mobil avans qoldig'ini tekshirish -- *912# \n"
                                       "  Sizga qo'ng'iroq qilishdi xizmati -- *977*1*1# \n"
                                       "  SMS tafsilot -- *400# \n"
                                       "  SMS info -- *221# \n"
                                       "  Mening xizmatlarim -- *401# \n"
                                       "  Mening raqamlarim  -- *360# \n"
                                       "  🌀 Restart 🌀 xizmati -- *222#\n"
                                       "  USSD Menyu  -- *111#\n"
                                       "0) Ortga qaytish --^:"))
                    print()

                    if kodlar == 0:
                        a = 0
                        break
                    else:
                        continue
            elif tanlov == 2:
                while True:

                    print("Tarif rejalar")
                    tarif = int(input(" 1) Tantana\n"
                                      " 2) Katta Tantana\n"
                                      " 3) Super Tantana\n"
                                      " 4) Cosmo 16\n"
                                      " 5) Cosmo 23\n"
                                      " 6) Cosmo 28\n"
                                      " 7) Special 35\n"
                                      " 8) Special 45\n"
                                      " 9) Special 55\n"
                                      "10) Drive\n"
                                      "11) Yengil hafta\n"
                                      "12) Oddiy\n"
                                      "13) Marhamat\n"
                                      "14) Mahalla\n"
                                      "0) Ortga qaytish --^\n"
                                      "Tanlang:"))

                    if tarif == 0:
                        break

                    elif tarif == 1:
                        while True:
                            print()
                            t = int(input("Tantana\n"
                                          "Oylik abonent to'lovi 15 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 1 000 daqiqa\n"
                                          "O'zbekiston bo'yicha 1 000 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue

                    elif tarif == 2:
                        while True:
                            print()
                            t = int(input("Katta Tantana\n"
                                          "Oylik abonent to'lovi 15 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 1 500 daqiqa\n"
                                          "O'zbekiston bo'yicha 1 500 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 3:
                        while True:
                            print()
                            t = int(input("Super Tantana\n"
                                          "Oylik abonent to'lovi 30 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 3 000 daqiqa\n"
                                          "O'zbekiston bo'yicha 3 000 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 4:
                        while True:
                            print()
                            t = int(input("Cosmo 16\n"
                                          "Oylik abonent to'lovi 16 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 1 000 daqiqa\n"
                                          "Oylik internet trafik 2000 MB\n"
                                          "O'zbekiston bo'yicha 2 000 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 5:
                        while True:
                            print()
                            t = int(input("Cosmo 23\n"
                                          "Oylik abonent to'lovi 23 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 1 500 daqiqa\n"
                                          "Oylik internet trafik 3 000 MB\n"
                                          "O'zbekiston bo'yicha 3 000 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 6:
                        while True:
                            print()
                            t = int(input("Cosmo 28\n"
                                          "Oylik abonent to'lovi 28 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 2 000 daqiqa\n"
                                          "Oylik internet trafik 5 000 MB\n"
                                          "O'zbekiston bo'yicha 5 000 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 7:
                        while True:
                            print()
                            t = int(input("Special 35\n"
                                          "Oylik abonent to'lovi 35 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 2 500 daqiqa\n"
                                          "Oylik internet trafik 7 000 MB\n"
                                          "O'zbekiston bo'yicha 1 000 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 8:
                        while True:
                            print()
                            t = int(input("Special 45\n"
                                          "Oylik abonent to'lovi 45 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 3 000 daqiqa\n"
                                          "Oylik internet trafik 9 000 MB\n"
                                          "O'zbekiston bo'yicha 2 000 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 9:
                        while True:
                            print()
                            t = int(input("Special 55\n"
                                          "Oylik abonent to'lovi 55 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 4 000 daqiqa\n"
                                          "Oylik internet trafik 12 000 MB\n"
                                          "O'zbekiston bo'yicha 3 000 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 10:
                        while True:
                            print()
                            t = int(input("Drive\n"
                                          "Oylik abonent to'lovi 50 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar kunlik limiti 100 daqiqa\n"
                                          "Kunlik internet trafik limiti Cheksiz*\n"
                                          "*Har kuni maksimal tezlikda 200 MB taqdim etiladi,keyin\n"
                                          "Internet tezligi 64 KB/s gacha qilib belgilanadi"
                                          "O'zbekiston bo'yicha  kunlik  100 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 11:
                        while True:
                            print()
                            t = int(input("Yengil hafta\n"
                                          "Haftalik abonent to'lovi 5 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar haftalik  limiti 200 daqiqa\n"
                                          "Haftalik internet trafik limiti  200 MB\n"
                                          "O'zbekiston bo'yicha limiti 200 SMS\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 12:
                        while True:
                            print()
                            t = int(input("Oddiy\n"
                                          "Efir vaqtining 1 daqiqasi narxi kiruvchi qo'ng'iroqlar 0 so'm\n"
                                          "Tarmoq ichidagi Chiquvchi qo'ng'iroqlar daqiqasi 95 so'm\n"
                                          "O'zbekiston bo'yicha chiquvchi qo'ng'iroqlar daqiqasi 125 so'm\n"
                                          "1ta chiquvchi SMS narxi 80 so'm\n"
                                          "1MB uchun internet-trafik narxi Ucell internet - 2G, 3G, 4G/LTE 450 so'm\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 13:
                        while True:
                            print()
                            t = int(input("Marhamat\n"
                                          "Oylik abonent to'lovi 10 000 so'm\n"
                                          "O'zbekiston bo'yicha daqiqalar oylik limiti 30 daqiqa\n"
                                          "Berilgan limitdan tashqari daqiqalar narxi 10 so'm\n"
                                          "Berilgan limitdan tashqari 1MB narxi 10 so'm\n"
                                          "1ta SMS narxi 10 so'm\n"
                                          "Tarifga o'tish: *120*2#\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    elif tarif == 14:
                        while True:
                            print()
                            t = int(input("Mahalla\n"
                                          "Oylik abonent to'lovi 15 000 so'm\n"
                                          "Tarif ichidagi Chiuvchi qo'ng'iroqlarning oylik limiti Cheksiz*\n"
                                          "O'zbekiston bo'yicha chiquvchi qo'ng'iroqlarning oylik limiti 750 daqiqa\n"
                                          "O'zbekiston bo'yicha chiquvchi SMSlarning oylik limiti 750ta\n"
                                          "Barcha yo'nalishlar uchun oylik internet trafik limiti 1GB\n"
                                          "Tarif rejasi faqat Kompaniyani xizmat ko'rsatish offislarida va\n"
                                          "Rasmiy dilerlarida yangidan ulanishda amal qiladi\n"
                                          "0) Ortga qaytish --^:"))
                            if t == 0:
                                break
                            else:
                                continue
                    else:
                        print("Bunday buyruq mavjud emas!")

            elif tanlov == 3:
                while True:

                    print("Internet to'plamlar")
                    tr_kodlar = int(input(" 1) Oylik to'plamlar \n"
                                          " 2) Haftalik to'plamlar \n"
                                          " 3) Kunlik to'plamlar  \n"
                                          " 4) Tungi internet \n"
                                          " 0) Ortga qaytish --^\n"
                                          "Tanlang:"))
                    print()
                    if tr_kodlar == 0:
                        break
                    elif tr_kodlar == 1:
                        while True:
                            print()
                            print("Oylik to'plamlar\n"
                                  "Amal qilsh muddati 30 kun")
                            toplam = int(input(" 1) To'plam 500 MB\n"
                                               " 2) To'plam 1000 MB\n"
                                               " 3) To'plam 1500 MB\n"
                                               " 4) To'plam 3000 MB\n"
                                               " 5) To'plam 5000 MB\n"
                                               " 6) To'plam 10000 MB\n"
                                               " 7) To'plam 12000 MB\n"
                                               " 8) To'plam 14000 MB\n"
                                               " 9) To'plam 16000 MB\n"
                                               "10) To'plam 32000 MB\n"
                                               "11) To'plam 64000 MB\n"
                                               "12) To'plam 128000 MB\n"
                                               " 0) Ortga qaytish --^\n"
                                               "Tanlang:"))
                            print()

                            if toplam == 0:
                                break
                            elif toplam == 1:
                                while True:
                                    a = int(input("To'plam 500 MB\n"
                                                  "To'plam narxi 8 900 so'm\n"
                                                  "Berilgan trafik hajmi 500 MB\n"
                                                  "Faollashtirish: *558*555*3*1*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 2:
                                while True:
                                    a = int(input(("To'plam 1 000 MB\n"
                                                   "To'plam narxi 13 000 so'm\n"
                                                   "Berilgan trafik hajmi 1 000 MB\n"
                                                   "Faollashtirish: *558*555*3*2*21947#\n"
                                                   "0) Ortga qaytish --^:")))

                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 3:
                                while True:
                                    a = int(input("To'plam 1 500 MB\n"
                                                  "To'plam narxi 15 000 so'm\n"
                                                  "Berilgan trafik hajmi 1 500 MB\n"
                                                  "Faollashtirish: *558*555*3*3*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 4:
                                while True:
                                    a = int(input("To'plam 3 000 MB\n"
                                                  "To'plam narxi 25 000 so'm\n"
                                                  "Berilgan trafik hajmi 3 000 MB\n"
                                                  "Faollashtirish: *558*555*3*4*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 5:
                                while True:
                                    a = int(input("To'plam 5 000 MB\n"
                                                  "To'plam narxi 35 000 so'm\n"
                                                  "Berilgan trafik hajmi 5 000 MB\n"
                                                  "Faollashtirish: *558*555*3*5*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 6:
                                while True:
                                    a = int(input("To'plam 10 000 MB\n"
                                                  "To'plam narxi 55 000 so'm\n"
                                                  "Berilgan trafik hajmi 10 000 MB\n"
                                                  "Faollashtirish: *558*555*3*6*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 7:
                                while True:
                                    a = int(input("To'plam 12 000 MB\n"
                                                  "To'plam narxi 65 000 so'm\n"
                                                  "Berilgan trafik hajmi 12 000 MB\n"
                                                  "Faollashtirish: *558*555*3*7*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 8:
                                while True:
                                    a = int(input("To'plam 14 000 MB\n"
                                                  "To'plam narxi 75 000 so'm\n"
                                                  "Berilgan trafik hajmi 14 000 MB\n"
                                                  "Faollashtirish: *558*555*3*8*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 9:
                                while True:
                                    a = int(input("To'plam 16 000 MB\n"
                                                  "To'plam narxi 85 000 so'm\n"
                                                  "Berilgan trafik hajmi 16 000 MB\n"
                                                  "Faollashtirish: *558*555*3*9*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 10:
                                while True:
                                    a = int(input("To'plam 32 000 MB\n"
                                                  "To'plam narxi 115 000 so'm\n"
                                                  "Berilgan trafik hajmi 32 000 MB\n"
                                                  "Faollashtirish: *558*555*3*10*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 11:
                                while True:
                                    a = int(input("To'plam 64 000 MB\n"
                                                  "To'plam narxi 135 000 so'm\n"
                                                  "Berilgan trafik hajmi 64 000 MB\n"
                                                  "Faollashtirish: *558*555*3*11*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            elif toplam == 12:
                                while True:
                                    a = int(input("To'plam 128 000 MB\n"
                                                  "To'plam narxi 188 000 so'm\n"
                                                  "Berilgan trafik hajmi 128 000 MB\n"
                                                  "Faollashtirish: *558*555*3*12*21947#\n"
                                                  "0) Ortga qaytish --^:"))
                                    if a == 0:
                                        break
                                    else:
                                        continue
                            else:
                                print()
                                print("Siz bergan son ro'yhatda mavjud emas!\n"
                                      "Qaytadan harakat qilng!")
                                continue

                    elif tr_kodlar == 2:
                        while True:
                            print()
                            print("Haftalik internet to'plamlar\n"
                                  "Amal qilish muddati 7 kun")
                            htoplam = int(input("1) Haftalik 80 MB\n"
                                                "2) Haftalik 160 MB\n"
                                                "3) Haftalik 320 MB\n"
                                                "0) Ortga qaytish --^\n"
                                                "Tanlang:"))
                            print()
                            if htoplam == 0:
                                break



                            elif htoplam == 1:
                                while True:
                                    ht = int(input("Haftalik 80 MB\n"
                                                   "To'plam narxi 8420 so'm\n"
                                                   "Berilgan trafik hajmi 80 MB\n"
                                                   "Faollashtirish: *555*2*1*1#\n"
                                                   "O) Ortga qaytish --^:"))
                                    if ht == 0:
                                        break
                            elif htoplam == 2:
                                while True:
                                    ht = int(input("Haftalik 160 MB\n"
                                                   "To'plam narxi 12 631 so'm\n"
                                                   "Berilgan trafik hajmi 160 MB\n"
                                                   "Faollashtirish: *555*2*2*1#"
                                                   "O) Ortga qaytish --^:"))
                                    if ht == 0:
                                        break
                            elif htoplam == 3:
                                while True:
                                    ht = int(input("Haftalik 320 MB\n"
                                                   "To'plam narxi 16 841 so'm\n"
                                                   "Berilgan trafik hajmi 320 MB\n"
                                                   "Faollashtirish: *555*2*3*1#"
                                                   "O) Ortga qaytish --^:"))
                                    if ht == 0:
                                        break
                            else:
                                print()
                                print("Siz bergan son ro'yhatda mavjud emas!\n"
                                      "Qaytadan harakat qilng!")
                                continue
                    elif tr_kodlar == 3:
                        while True:
                            print()
                            print("Kunlik internet to'plamlar\n"
                                  "Amal qilish muddati 1 kun")
                            ktoplam = int(input("1) Kunlik 5 MB\n"
                                                "2) Kunlik 10 MB\n"
                                                "3) Kunlik 20 MB\n"
                                                "4) Kunlik 35 MB\n"
                                                "5) Kunlik 55 MB\n"
                                                "6) Kunlik 100 MB\n"
                                                "7) Kunlik 130 MB\n"
                                                "8) Kunlik 160 MB\n"
                                                "9) Kunlik 200 MB\n"
                                                "0) Ortga qaytish\n"
                                                "Tanlang:"))
                            print()
                            if ktoplam == 0:
                                break
                            elif ktoplam == 1:
                                while True:
                                    kt = int(input("Kunlik 5 MB\n"
                                                   "To'plam narxi 390 so'm\n"
                                                   "Berilgan trafik hajmi 5 MB\n"
                                                   "Amal qilsh muddati 1 kun\n"
                                                   "Kunlik to'plamlarning asosiy ustunligi shundaki\n"
                                                   "ishlatilmagan trafik qoldig'i keyingi kun"
                                                   " trafigiga qo'shilib boraveradi.\n"
                                                   "'Xizmat bekor qilingan holda yi'gilgan trafik bekor qilinadi.\n"
                                                   "Faollashtirish: *555*1*1*1#\n"
                                                   "0) Ortga qytish --^:"))
                                    if kt == 0:
                                        break
                            elif ktoplam == 2:
                                while True:
                                    kt = int(input("Kunlik 10 MB\n"
                                                   "To'plam narxi 550 so'm\n"
                                                   "Berilgan trafik hajmi 10 MB\n"
                                                   "Amal qilsh muddati 1 kun\n"
                                                   "Kunlik to'plamlarning asosiy ustunligi shundaki\n"
                                                   "ishlatilmagan trafik qoldig'i keyingi kun trafigiga qo'shilib"
                                                   " boraveradi.\n"
                                                   "'Xizmat bekor qilingan holda yi'gilgan trafik bekor qilinadi.\n"
                                                   "Faollashtirish: *555*1*2*1#\n"
                                                   "0) Ortga qytish --^:"))
                                    if kt == 0:
                                        break
                            elif ktoplam == 3:
                                while True:
                                    kt = int(input("Kunlik 20 MB\n"
                                                   "To'plam narxi 790 so'm\n"
                                                   "Berilgan trafik hajmi 20 MB\n"
                                                   "Amal qilsh muddati 1 kun\n"
                                                   "Kunlik to'plamlarning asosiy ustunligi shundaki\n"
                                                   "ishlatilmagan trafik qoldig'i keyingi kun trafigiga qo'shilib"
                                                   " boraveradi.\n"
                                                   "'Xizmat bekor qilingan holda yi'gilgan trafik bekor qilinadi.\n"
                                                   "Faollashtirish: *555*1*3*1#\n"
                                                   "0) Ortga qytish --^:"))
                                    if kt == 0:
                                        break
                            elif ktoplam == 4:
                                while True:
                                    kt = int(input("Kunlik 35 MB\n"
                                                   "To'plam narxi 1190 so'm\n"
                                                   "Berilgan trafik hajmi 35 MB\n"
                                                   "Amal qilsh muddati 1 kun\n"
                                                   "Kunlik to'plamlarning asosiy ustunligi shundaki\n"
                                                   "ishlatilmagan trafik qoldig'i keyingi kun trafigiga "
                                                   "qo'shilib boraveradi.\n"
                                                   "'Xizmat bekor qilingan holda yi'gilgan trafik bekor qilinadi.\n"
                                                   "Faollashtirish: *555*1*4*1#\n"
                                                   "0) Ortga qytish --^:"))
                                    if kt == 0:
                                        break
                            elif ktoplam == 5:
                                while True:
                                    kt = int(input("Kunlik 55 MB\n"
                                                   "To'plam narxi 1890 so'm\n"
                                                   "Berilgan trafik hajmi 55 MB\n"
                                                   "Amal qilsh muddati 1 kun\n"
                                                   "Kunlik to'plamlarning asosiy ustunligi shundaki\n"
                                                   "ishlatilmagan trafik qoldig'i keyingi kun trafigiga qo'shilib"
                                                   " boraveradi.\n"
                                                   "'Xizmat bekor qilingan holda yi'gilgan trafik bekor qilinadi.\n"
                                                   "Faollashtirish: *555*1*5*1#\n"
                                                   "0) Ortga qytish --^:"))
                                    if kt == 0:
                                        break
                            elif ktoplam == 6:
                                while True:
                                    kt = int(input("Kunlik 100 MB\n"
                                                   "To'plam narxi 2790 so'm\n"
                                                   "Berilgan trafik hajmi 100 MB\n"
                                                   "Amal qilsh muddati 1 kun\n"
                                                   "Kunlik to'plamlarning asosiy ustunligi shundaki\n"
                                                   "ishlatilmagan trafik qoldig'i keyingi kun trafigiga qo'shilib"
                                                   " boraveradi.\n"
                                                   "'Xizmat bekor qilingan holda yi'gilgan trafik bekor qilinadi.\n"
                                                   "Faollashtirish: *555*1*6*1#\n"
                                                   "0) Ortga qytish --^:"))
                                    if kt == 0:
                                        break
                            elif ktoplam == 7:
                                while True:
                                    kt = int(input("Kunlik 130 MB\n"
                                                   "To'plam narxi 4000 so'm\n"
                                                   "Berilgan trafik hajmi 130 MB\n"
                                                   "Amal qilsh muddati 1 kun\n"
                                                   "Kunlik to'plamlarning asosiy ustunligi shundaki\n"
                                                   "ishlatilmagan trafik qoldig'i keyingi kun trafigiga qo'shilib"
                                                   " boraveradi.\n"
                                                   "'Xizmat bekor qilingan holda yi'gilgan trafik bekor qilinadi.\n"
                                                   "Faollashtirish: *555*1*7*1#\n"
                                                   "0) Ortga qytish --^:"))
                                    if kt == 0:
                                        break
                            elif ktoplam == 8:
                                while True:
                                    kt = int(input("Kunlik 160 MB\n"
                                                   "To'plam narxi 4490 so'm\n"
                                                   "Berilgan trafik hajmi 160 MB\n"
                                                   "Amal qilsh muddati 1 kun\n"
                                                   "Kunlik to'plamlarning asosiy ustunligi shundaki\n"
                                                   "ishlatilmagan trafik qoldig'i keyingi kun trafigiga qo'shilib"
                                                   " boraveradi.\n"
                                                   "'Xizmat bekor qilingan holda yi'gilgan trafik bekor qilinadi.\n"
                                                   "Faollashtirish: *555*1*8*1#\n"
                                                   "0) Ortga qytish --^:"))
                                    if kt == 0:
                                        break
                            elif ktoplam == 9:
                                while True:
                                    kt = int(input("Kunlik 200 MB\n"
                                                   "To'plam narxi 4990 so'm\n"
                                                   "Berilgan trafik hajmi 200 MB\n"
                                                   "Amal qilsh muddati 1 kun\n"
                                                   "Kunlik to'plamlarning asosiy ustunligi shundaki\n"
                                                   "ishlatilmagan trafik qoldig'i keyingi kun trafigiga qo'shilib"
                                                   " boraveradi.\n"
                                                   "'Xizmat bekor qilingan holda yi'gilgan trafik bekor qilinadi.\n"
                                                   "Faollashtirish: *555*1*9*1#\n"
                                                   "0) Ortga qytish --^:"))
                                    if kt == 0:
                                        break
                            else:
                                print()
                                print("Siz bergan son ro'yhatda mavjud emas!\n"
                                      "Qaytadan harakat qilng!")
                                continue
                    if tr_kodlar == 4:
                        while True:
                            print()
                            print("Tungi to'plamlar\n"
                                  "Amal qilsh muddati 30 kun")
                            tungii = int(input("1) To'plam 5 GB\n"
                                               "2) To'plam 20 GB\n"
                                               "0) Ortga qaytish --^\n"
                                               "Tanlang:"))
                            print()

                            if tungii == 0:
                                break
                            elif tungii == 1:
                                while True:
                                    ti = int(input("Tungi internet to'plam 5 GB\n"
                                                   "To'plam narxi 20 000 so'm\n"
                                                   "Berilgan trafik hajmi 5 GB\n"
                                                   "Tungi internet to'plamni harid qilib,\n"
                                                   "01:00 dan 09:00 gacha internetdan foydalanishingiz mumkin.\n"
                                                   "Ulanish: *616#\n"
                                                   "0) Ortga qaytish --^:"))

                                    if ti == 0:
                                        break
                            elif tungii == 2:
                                while True:
                                    ti = int(input("Tungi internet to'plam 20 GB\n"
                                                   "To'plam narxi 45 000 so'm\n"
                                                   "Berilgan trafik hajmi 20 GB\n"
                                                   "Tungi internet to'plamni harid qilib,\n"
                                                   "01:00 dan 09:00 gacha internetdan foydalanishingiz mumkin.\n"
                                                   "Ulanish: *616#\n"
                                                   "0) Ortga qaytish --^:"))

                                    if ti == 0:
                                        break
                        else:
                            print()
                            print("Siz bergan son ro'yhatda mavjud emas!\n"
                                  "Qaytadan harakat qilng!")

                    else:
                        print()
                        print("Siz bergan son ro'yhatda mavjud emas!\n"
                              "Qaytadan harakat qilng!")
            elif tanlov == 4:
                print("Daqiqa paketlar")
                while True:
                    print()
                    dtlar = int(input("1) Qulay daqiaqalar\n"
                                      "2) Tarmoq ichida qulay\n"
                                      "3) O'zbekiston bo'yicha qulay\n"
                                      "0) Ortga qaytish --^\n"
                                      "Tanlang:"))
                    if dtlar == 0:
                        break
                    elif dtlar == 1:
                        while True:

                            dtoplam = int(input("Qulay Daqiqalar\n"
                                                "1) To'plam 200 daqiqa\n"
                                                "2) To'plam 600 daqiqa\n"
                                                "3) To'plam 1200 daqiqa\n"
                                                "0) Ortga qaytish --^\n"
                                                "Faollashtirish: *130#\n"
                                                "Tanlang:"))
                            if dtoplam == 0:
                                break

                            elif dtoplam == 1:
                                while True:
                                    dt = int(input("To'plam 200 daqiqa\n"
                                                   "O'zbekiston bo'yicha 100 daqiqa + 100 daqiqa bonus\n"
                                                   "Narxi 4000 so'm\n"
                                                   "Amal qilish muddati 30 kun\n"
                                                   "0) Ortga qaytish --^:"))
                                    if dt == 0:
                                        break
                                    else:
                                        continue

                            elif dtoplam == 2:
                                while True:
                                    dt = int(input("To'plam 600 daqiqa\n"
                                                   "O'zbekiston bo'yicha 300 daqiqa + 300 daqiqa bonus\n"
                                                   "Narxi 8000 so'm\n"
                                                   "Amal qilish muddati 30 kun\n"
                                                   "0) Ortga qaytish --^:"))
                                    if dt == 0:
                                        break
                                    else:
                                        continue
                            elif dtoplam == 3:
                                while True:
                                    dt = int(input("To'plam 1200 daqiqa\n"
                                                   "O'zbekiston bo'yicha 600 daqiqa + 600 daqiqa bonus\n"
                                                   "Narxi 12000 so'm\n"
                                                   "Amal qilsh muddati 30 kun\n"
                                                   "0) Ortga qaytish --^:"))
                                    if dt == 0:
                                        break
                                    else:
                                        continue
                    elif dtlar == 2:
                        while True:
                            tq = int(input("Tarmoq ichida qulay\n"
                                           "Tarmoq ichidagi daqiqalar 3000\n"
                                           "O'zbekiston bo'yicha daqiqalar 1000\n"
                                           "Internet trafik miqdori 300 MB\n"
                                           "Narxi 12630 so'm\n"
                                           "Amal qilish muddati 15 kun\n"
                                           "Faollashtirish: *130#\n"
                                           "0) Ortga qaytish --^:"))

                            if tq == 0:
                                break
                    elif dtlar == 3:
                        while True:
                            print("Ozbekiston bo'yicha qulay")
                            oq = int(input("O'zbekiston bo'yicha qulay 100\n"
                                           "O'zbekiston bo'yicha daqiqalar 100\n"
                                           "O'zbekiston bo'yicha SMSlar 100\n"
                                           "Internet trafik miqdori 30 MB\n"
                                           "Amal qilsh muddati 5 kun\n"
                                           "Narxi 4210 so'm\n"
                                           "Faollashtirish: *130#\n"
                                           "0) O) Ortga qaytish --^:"))
                            if oq == 0:
                                break
                    else:
                        print()
                        print("Siz bergan son ro'yhatda mavjud emas!\n"
                              "Qaytadan harakat qilng!")
            elif tanlov == 5:
                while True:
                    print("SMS paketlar")
                    smstop = int(input("1) Kunlik SMS to'plamlar\n"
                                       "2) SMS to'plamlar\n"
                                       "0) Ortga qaytish --^\n"
                                       "Tanlang:"))
                    if smstop == 0:
                        break
                    elif smstop == 1:
                        while True:
                            print("Kunlik SMS to'plamlar")
                            ksms = int(input("Kunlik SMS 20\n"
                                             "Kunlik SMS 30\n"
                                             "Kunlik SMS 50\n"
                                             "0) Ortga qaytish --^\n"
                                             "Tanlang:"))
                            if ksms == 0:
                                break
                            elif ksms == 1:
                                while True:
                                    kt = int(input("Kunlik to'plam 20\n"
                                                   "SMS miqdori 20 ta\n"
                                                   "Narxi 631.5 so'm\n"
                                                   "Faollashtirish: *148*1*1#\n"
                                                   "O'chirish: *148*2#\n"
                                                   "0) Ortga qaytish --^:"))
                                    if kt == 0:
                                        break
                            elif ksms == 2:
                                while True:
                                    kt = int(input("Kunlik to'plam 30\n"
                                                   "SMS miqdori 30 ta\n"
                                                   "Narxi 842 so'm\n"
                                                   "Faollashtirish: *148*1*2#\n"
                                                   "O'chirish: *148*2#\n"
                                                   "0) Ortga qaytish --^:"))
                                    if kt == 0:
                                        break
                                    else:
                                        continue
                            elif ksms == 3:
                                while True:
                                    kt = int(input("Kunlik to'plam 50\n"
                                                   "SMS miqdori 50 ta\n"
                                                   "Narxi 1263 so'm\n"
                                                   "Faollashtirish: *148*1*3#\n"
                                                   "O'chirish: *148*2#\n"
                                                   "0) Ortga qaytish --^:"))
                                    if kt == 0:
                                        break
                            else:
                                print()
                                print("Siz bergan son ro'yhatda mavjud emas!\n"
                                      "Qaytadan harakat qilng!")

                    elif smstop == 2:
                        while True:

                            print()
                            print("SMS to'plamlar")
                            smt = int(input("SMS to'plam 50\n"
                                            "SMS to'plam 150\n"
                                            "SMS to'plam 500\n"
                                            "0) Ortga qaytish--^\n"
                                            "Tanlang:"))
                            if smt == 1:
                                st = int(input("SMS to'plam 50\n"
                                               "SMS miqdori 50 ta\n"
                                               "Narxi 1684 so'm\n"
                                               "Faollashtirish: *147*1*1#\n"
                                               "0) Ortga qaytish --^:"))
                            elif smt == 2:
                                st = int(input("SMS to'plam 150\n"
                                               "SMS miqdori 150 ta\n"
                                               "Narxi 4210 so'm\n"
                                               "Faollashtirish: *147*1*2#\n"
                                               "0) Ortga qaytish --^:"))
                            elif smt == 3:
                                st = int(input("SMS to'plam 500\n"
                                               "SMS miqdori 500 ta\n"
                                               "Narxi 10525 so'm\n"
                                               "Faollashtirish: *147*1*3#\n"
                                               "0) Ortga qaytish --^:"))
                            else:
                                print()
                                print("Siz bergan son ro'yhatda mavjud emas!\n"
                                      "Qaytadan harakat qilng!")
                    else:
                        print()
                        print("Siz bergan son ro'yhatda mavjud emas!\n"
                              "Qaytadan harakat qilng!")
                        continue



                else:
                    print()
                    print("Siz bergan son ro'yhatda mavjud emas!\n"
                          "Qaytadan harakat qilng!")

            elif tanlov == 6:
                while True:
                    uzur = int(input("Uzur bu xizmatlar to'plami endi ishlab chiqilmoqda!\n"
                                     "0) Ortga qayitsh --^:"))
                    if uzur == 0:
                        break

                    while False:
                        print("Qo'shimcha xizmatlar")
                        qxizmatlar = int(input("1) Xizmatlar\n"
                                               "2) Internet xizmatlar\n"
                                               "2) Pullik SMS xizmatlar\n"
                                               "0) Ortga qaytish --^\n"
                                               "Tanlang:"))
                        if qxizmatlar == 1:
                            print("Xizmatlar")
                            xiz = int(input("1) Raqamni yashirish\n"
                                            "2) Restart xizmati\n"
                                            "3) Sizga qo'ng'iroq qilishdi\n"
                                            "4) Mobil o'tkazma\n"
                                            "5) Tilni o'zgartirish\n"
                                            "6) Sodiqlik dasturi\n"
                                            "7) Chaqiriqni kutish va uslab turish\n"
                                            "8) Tarmoq ichida qulay xizmatlar to'plami\n"
                                            "9) "))
        else:
            print()
            print("Siz bergan son ro'yhatda mavjud emas!\n"
                  "Qaytadan harakat qilng!")
            break

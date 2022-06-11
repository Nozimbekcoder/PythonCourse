"""
lesson10
Mavzu: Database lar bilan ishlash, fake malumot to'ldirish

"""

import sqlite3
import random

db = sqlite3.connect("fake.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
                                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                ism TEXT(75) NOT NULL,
                                                familya TEXT(75) NOT NULL,
                                                yosh INTEGER,
                                                jins TEXT,
                                                davlat TEXT);""")

ism = ['Adulaziz', 'Hojiakbar',
       'Abdurauf', 'Rahmatillo',
       'Muhammadqodir', 'Mirziyo',
       'Ali', 'Vali', 'Muslima',
       'Robiya', 'Abdurahmon',
       'Akbar', 'Sevinch', 'Abror',
       'Alisher', 'Mirzakbar',
       'Mahmud', 'Murod',
       'Sobitxon','Aziz']

familya = ['Aliyev', 'Soliyev',
           'Tursunov', 'Rahimov',
           'Komilov', 'Abdulatipov',
           'Abdulayev', 'Karimjonov',
           'Qodirov','Sharipov',
           'Qosimov', 'Tillayev',
           'Rashidov', 'Sherzodjonov', ]

yosh = [18, 15, 16, 19, 25, 21, 24, 32, 41, 51, 53, 19, 18, 19, 17]

jins = ('Erkak','Ayol')

davlatlar = [
    'Uzbekistan','AQSH',
    'Angliya','Germaniya',
    'Korea','Xitoy',
    'Belgiya','Fransiya',
    'Urugvay'
]

# n = int(input("Nechta Fake Malumot kerak: "))
#
# for x in range(n):
#     ism1 = random.choice(ism)
#     familya1 = random.choice(familya)
#     yosh1 = random.choice(yosh)
#     jins1 =random.choice(jins)
#     davlat = random.choice(davlatlar)
#     sql.execute(f"""INSERT INTO users (ism, familya, yosh, jins, davlat)
#                                     VALUES('{ism1}', '{familya1}', {yosh1}, '{jins1}','{davlat}');""")



# datas = sql.execute("SELECT * FROM users;")


# datas = sql.execute("SELECT ism, familya FROM users ORDER BY ism;")

datas = sql.execute("SELECT ism, familya FROM users ORDER BY ism DESC, familya DESC")
# datas = sql.execute("SELECT DISTINCT davlat FROM users ORDER BY davlat")
# datas=sql.execute("SELECT 10+1;")
# datas=sql.execute("SELECT 10*2;")
# datas=sql.execute("SELECT 10/2;")

#
for data in datas:
    print(data)




db.commit()

sql.close()

"""
lesson9
Mavzu: Database lar bilan ishlash

"""

import sqlite3


db = sqlite3.connect('sinov.db')

sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
                                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                ism TEXT(75) NOT NULL,
                                                familya TEXT(75) NOT NULL,
                                                yosh INTEGER,
                                                jins TEXT,
                                                davlat TEXT);""")

# sql.execute("""DROP TABLE users;""")

# sql.execute("""INSERT INTO users (id, ism, familya, yosh)
#                                 VALUES(1, 'Rahmatillo', 'Rashidov', 13);""")


# sql.execute("""INSERT INTO users (id, ism, familya, yosh)
#                                 VALUES(2, 'Rahimov', 'Hojiakbar', 16);""")


# sql.execute(f"""INSERT INTO users (id, ism, familya, yosh)
#                                 VALUES(2, 'Rahimov', 'Hojiakbar', 16);""")


# ism = input("Ism kiriting: ")
# familya = input("Familyani kiriting: ")
# yosh = int(input("Yoshni kiriting: "))
# jins = input("jins kiriting: ")
# davlat = input('Davlatni kiriting')
#
#
#
#
# sql.execute(f"""INSERT INTO users (ism, familya, yosh, kurs)
#                                 VALUES('{ism}', '{familya}', {yosh}, '{jins}');""")

db.commit()

sql.close()


# print('Malumotlar bazasi muvaffaqiyatli yaratildi!')
# print("users jadvali mufaqqiyatli yaratildi")



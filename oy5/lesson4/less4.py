"""
lesson 4
Python OOP dasturlash
OOP - Object Oriented Programming
Klasslar yaratish, uning metodlari
"""


class Student:
    """student classi xusususiyatlarini yaratish"""

    def __init__(self, ism, familya, tel):
        self.ism = ism
        self.familya = familya
        self.tel = tel
        self.kurs = 1

        self.follower = 0
        self.following = 0


    def follow(self, user):
        self.following += 1
        user.follower += 1

    def update_kurs(self):
        self.kurs += 1

    def down_kurs(self):
        self.kurs -= 1

    def course(self, otkazish=1):
        self.kurs = otkazish

    def update_ism(self,firstname):
        self.ism = firstname

    def update_familya(self,lastname):
        self.familya = lastname

    def update_tel(self, phone):
            self.tel = phone




st1 = Student('Hojiakbar', 'Rahimov', '+998942760808')
st2 = Student('Mirziyo', 'Hasanboyev', '+998332014609')
st3 = Student('Ali', 'Rahmatilloyev', '+998332010909')
st4 = Student('Vali', 'Hasanboy', '+998332085909')
st5 = Student('Mirziyo', 'Rahimov', '+998332360909')
st6 = Student('Teshayev', 'Natasha', '+998332456909')





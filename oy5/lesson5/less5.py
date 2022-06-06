"""
lesson 5

Python OOP dasturlaash
Obyeklar bilan ishlash, dunder metodlari
"""


class Avtomobil():
    """Bu klasimiz yordamida mashinalarni obyeklari yartatishimiz mumkin"""
    def __init__(self, marka, model, rang, yili, narxi):
        self.marka = marka
        self.model = model
        self.rang = rang
        self.yili = yili
        self.narxi = narxi

    def __str__(self):
        return 'aaaaa'

    def reklama(self):
        return f"{self.marka}  {self.model} modeli\n" \
               f"Rangi:                 {self.rang}\n" \
               f"Ishlab chiqarilgan:    {self.yili}\n" \
               f"Narxi:                 {self.narxi}$\n\n"

avto1 = Avtomobil("Hyundai", "Sonata", "Oq", 2019, 35000)
avto2 = Avtomobil("KIA", "Cerato", "Qora", 2015, 42000)
avto3 = Avtomobil("Tesla", "X3", "Kok", 2021, 135000)
avto4 = Avtomobil("GM", "Ravon Nexia 3", "Oq", 2020, 10000)
avto5 = Avtomobil("ИЖ", "Moskvich 412", "Yashil", 1990, 1800)


# print(avto1.reklama(),avto2.reklama(),avto3.reklama(),avto4.reklama(),avto5.reklama())

# print(dir(Avtomobil))


print(avto1)

"""
lesson 4
Python OOP dasturlash
OOP - Object Oriented Programming
Obyektlar bilan ishlash,

"""

class Avtomobil:
    def __init__(self, marka, model, rang, yil, narxi):
        self.marka = marka
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narxi = narxi

    def __str__(self):
        """
        __str__ - bu metod biz chaqirganda chiqadigan obyekt uchun
        yangi nom berishda ishlatiladi
        standart shu kabi bo'ladi: <__main__.Avtomobil object at 0x000001E9C4233610>
        shu xolat o'zgaradi.
        """
        return f"{self.marka}ning {self.model} modeli\n rang {self.rang}\n{self.yil}-yil\n{self.narxi}$"

    def reklama(self):
        return f"{self.marka}  {self.model} modeli\n" \
               f"Rangi:              {self.rang}\n" \
               f"Ishlab chiqarilgan: {self.yil}-yil\n" \
               f"Narxi:              {self.narxi}$"


# print(Avtomobil("Toyota", "Corolla", "2019", "100000"))

avto1 = Avtomobil("Hyundai", "Sonata","Oq", "2016", 80000)
avto2 = Avtomobil("KIA", "Cerato","Qora", "2018", 90000)
avto3 = Avtomobil("Tesla", "Model 3", "Kok", "2019", 130000)
avto4 = Avtomobil("GM", "Ravon Nexia 3", "Asfalt rang", "2019", 9000)

print(avto4.reklama())
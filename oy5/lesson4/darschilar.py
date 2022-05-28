class Notebook():
    def __init__(self,madeli, cpu, gpu, ram, xotira):
        self.madeli = madeli
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.xotira = xotira
        self.yili = 2021

    def madel1(self):
        return self.madeli
    def cpusi(self):
        return self.cpu
    def gpusi(self):
        return self.gpu
    def rami(self):
        return self.ram
    def xotirasi(self):
        return self.xotira
asus = Notebook("Asus Sonic Master","i3","128 mb","4 gb","1 tb")
dell = Notebook("DELL","i3","4096 mb","8gb","1 tb,128 gb")




class Karakter:
    def __init__(self, isim, can):
        self.isim = isim
        self.__can = can


        #getter method
    def get_can(self):
        return self.__can

    #setter method 
    def set_can(self, yeni_can):
        if 0 <= yeni_can <= 100:
            self.__can = yeni_can
        else:
            print("Can değeri 0 ile 100 değeri arasında olmalıdır.")


karakter1 = Karakter("Aslan", 80)

karakter1.set_can(120)
karakter1.set_can(90)
print(karakter1.get_can())
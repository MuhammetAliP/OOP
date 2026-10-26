class Araba:
    def __init__(self, marka, model, model_yili, cekis, hiz):
        self.marka = marka
        self.model = model
        self.model_yili = model_yili
        self.cekis = cekis
        self.hiz = hiz

    def bilgileri_göster(self):
        print(f"Arabanın markası: {self.marka}")
        print(f"Arabanın modeli: {self.model}")
        print(f"Arabanın model yılı: {self.model_yili}")
        print(f"Arabanın çekişi: {self.cekis}")

    def hizlandir(self, surat):
        self.hiz += surat
        print(f"Arabanın hızı: {self.hiz}")

araba1 = Araba("Toyota", "Corolla", 1997, "4x2", 40)
araba1.bilgileri_göster()

araba1.hizlandir(20)


# Marka
# Model
# Model Yılı
# Çekiş

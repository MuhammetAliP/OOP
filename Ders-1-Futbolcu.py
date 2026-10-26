class Futbolcu: 
    def __init__(self, isim, yas, mevki, guc):
        self.isim = isim
        self.yas = yas
        self.mevki = mevki
        self.guc = guc

    def kos(self):
        print(f'{self.isim} koşuyor.')

    def sut(self, guc):
        print(f'{self.isim} {guc} güçte şut çekti.')

futbolcu1 = Futbolcu("Ronaldo", 40, "Forvet", 50)

print(f'Futbolcu {futbolcu1.isim} {futbolcu1.guc} şiddetinde şut çekti.')

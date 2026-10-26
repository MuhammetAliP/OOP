class Ogrenci:
    def __init__(self, Adi, Soyadi, Tc_Kimlik, Dogum_Tarihi, Bolum, Okul, Ogrenci_No):
        self.Adi = Adi
        self.Soyadi = Soyadi
        self.Tc_Kimlik = Tc_Kimlik
        self.Dogum_Tarihi = Dogum_Tarihi
        self.Bolum = Bolum
        self.Okul = Okul
        self.Ogrenci_No = Ogrenci_No

    def bilgileri_göster(self):
        print(f"Öğrenci Bilgileri :")
        print(f"Adı: {self.Adi}")
        print(f"Soyadı: {self.Soyadi}")
        print(f"Tc Kimlik No: {self.Tc_Kimlik}")
        print(f"Doğum Tarihi: {self.Dogum_Tarihi}")
        print(f"Bölüm: {self.Bolum}")
        print(f"Okul: {self.Okul}")
        print(f"Öğrenci No: {self.Ogrenci_No}")

ogrenci1 = Ogrenci("Ali", "Perçin", "15472653289", "25.01.2003", "Yönetim Bilişim Sistemleri", "Uygulamalı Bilimler Yüksekokulu", "251702035")
ogrenci1.bilgileri_göster()
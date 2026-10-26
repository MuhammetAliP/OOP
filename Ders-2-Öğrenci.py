import os
import json


class Ogrenci:
    def __init__(self, Adi, Soyadi, Tc_Kimlik, Dogum_Tarihi, Bolum, Okul, Ogrenci_No):
        self.Adi = Adi
        self.Soyadi = Soyadi
        self.Tc_Kimlik = Tc_Kimlik
        self.Dogum_Tarihi = Dogum_Tarihi
        self.Bolum = Bolum
        self.Okul = Okul
        self.Ogrenci_No = Ogrenci_No

    def bilgileri_goster(self):
        print(f"Öğrenci Bilgileri :")
        print(f"Adı: {self.Adi}")
        print(f"Soyadı: {self.Soyadi}")
        print(f"Tc Kimlik No: {self.Tc_Kimlik}")
        print(f"Doğum Tarihi: {self.Dogum_Tarihi}")
        print(f"Bölüm: {self.Bolum}")
        print(f"Okul: {self.Okul}")
        print(f"Öğrenci No: {self.Ogrenci_No}")

    def sozluk_yap(self):
        return{
            "Adi:": self.Adi,
            "Soyadi:": self.Soyadi,
            "Tc Kimlik No:": self.Tc_Kimlik,
            "Dogum Tarihi:": self.Dogum_Tarihi,
            "Bolum:": self.Bolum,
            "Okul:": self.Okul,
            "Ogrenci No:": self.Ogrenci_No
        }

ogrenci1 = Ogrenci("Ali", "Percin", "15472653289", "25.01.2003", "Yonetim Bilisim Sistemleri", "Uygulamali Bilimler Yuksekokulu", "251702035")
#ogrenci1.bilgileri_goster()

ogrenci_bilgileri = []

def verileri_yukle():
    ogrenci_bilgileri.clear()
    if os.path.exists("ogrenci_bilgileri.json"):
        with open("ogrenci_bilgileri.json", "r") as dosya:
            veri = json.load(dosya)
            for item in veri:
                ogr = Ogrenci(
                    item["Adi:"],
                    item["Soyadi:"],
                    item["Tc Kimlik No:"],
                    item["Dogum Tarihi:"],
                    item["Bolum:"],
                    item["Okul:"],
                    item["Ogrenci No:"]
                )
                ogrenci_bilgileri.append(ogr)
            print("Öğrenci bilgileri hafızaya yüklendi.")
    else:
        print("Öğrenci bilgileri dosyası bulunamadı. 'ogrenci_bilgileri.json'")

def verileri_kaydet():
    veri = [ogr.sozluk_yap() for ogr in ogrenci_bilgileri]
    with open ("ogrenci_bilgileri.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)
        print("Öğrenci bilgileri dosyaya kaydedildi.")



ogrenci_bilgileri.append(ogrenci1)
#print(f"Öğrenci bilgileri listesine {ogrenci1.Adi} {ogrenci1.Soyadi} eklendi.")

verileri_kaydet()

verileri_yukle()

for ogr in ogrenci_bilgileri:
    ogr.bilgileri_goster()
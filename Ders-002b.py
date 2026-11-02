"""
------- Değişkenler -------
adi
soyadi
tc_kimlik
dogum_tarihi
bolum
okul
ogrenci_no
"""

class Ogrenci:
    ogrenci_sayisi = 0

    
    def __init__(self, adi, soyadi, tc_kimlik, dogum_tarihi, bolum, okul, ogrenci_no):
        self.adi = adi
        self.soyadi = soyadi
        self.tc_kimlik = tc_kimlik
        self.dogum_tarihi = dogum_tarihi
        self.bolum = bolum
        self.okul = okul
        self.ogrenci_no = ogrenci_no
        # Dersleri ve notları key-value (Ders: Not) olarak tutmak için boş bir sözlük
        self.dersler = {} 
        Ogrenci.ogrenci_sayisi += 1 

    def bilgileri_goster(self):
        print("-" * 80)
        print(f"Öğrencinin Adı: {self.adi}")
        print(f"Öğrencinin Soyadı: {self.soyadi}")
        print("-" * 80)
        print(f"Öğrencinin TC Kimlik Numarası: {self.tc_kimlik}")
        print(f"Öğrencinin Doğum Tarihi: {self.dogum_tarihi}")
        print(f"Öğrencinin Bölümü: {self.bolum}")
        print(f"Öğrencinin Okulu: {self.okul}")
        print(f"Öğrencinin Öğrenci Numarası: {self.ogrenci_no}")
        print("-" * 80)

    # Yeni ders ve not eklemek için metot
    def not_ekle(self, ders_adi, dersin_notu):
        self.dersler[ders_adi] = dersin_notu
        print(f"{ders_adi} dersi notu ({dersin_notu}) başarıyla eklendi.")

    # Eklenen notları görüntülemek için düzeltilen metot
    def not_goruntule(self, ders_adi):
        if ders_adi in self.dersler:
            print(f"Öğrenci {self.adi}'nin {ders_adi} dersi notu: {self.dersler[ders_adi]}")
        else:
            print(f"Öğrenci {self.adi}, {ders_adi} dersini henüz almamış.")

    @classmethod
    def ogrenci_sayisini_goster(cls):
        print("Bu bir sınıf metodu.Sınıfa ait toplam öğrenci sayısını gösterir.")
        print(f"Toplam Öğrenci Sayısı Metodu: {cls.ogrenci_sayisi}")

    @staticmethod
    def cift_mi(sayi):
        if sayi % 2 == 0:
            print(f"{sayi} sayısı çifttir.")
        else:
            print(f"{sayi} sayısı tektir.")


# Öğrenci oluşturulurken sadece kişisel bilgileri verilir
id_11111111111 = Ogrenci("Ahmet", "Yılmaz", "11111111111", "01.01.2000", 
                   "Yönetim Bilişim Sistemleri", 
                   "Uygulamalı Bilimler Yüksekokulu", "251700001")

id_22222222222 = Ogrenci("Mehmet", "Demir", "22222222222", "02.02.2001", "Bilgisayar Mühendisliği", "Mühendislik Fakültesi", "251700002")

id_11111111111.bilgileri_goster()

# Önce nota ekleme yapıyoruz
id_11111111111.not_ekle("Matematik", 85)
id_11111111111.not_ekle("Programlama", 95)

print("-" * 80)

# Sonra eklenen notu sorguluyoruz
id_11111111111.not_goruntule("Matematik")
id_11111111111.not_goruntule("Fizik")  # Eklenmeyen ders kontrolü

#Boylede bakabiliriz
#id_11111111111.ogrenci_sayisi_goster() dememize gerek yok
#Çünkü @classmethod ile sınıf metodu oluşturduk.

print(f"Toplam öğrenci sayısı: {Ogrenci.ogrenci_sayisi}")
print("-" * 80)

Ogrenci.ogrenci_sayisini_goster() #classmethod

#ogrenci_1 = Ogrenci("Ahmet", "Yılmaz", "11111111111", "01.01.2000")
#ogrenci_1.cift_mi(21564) #bu şekilde çağırmak yerine sınıf üzerinden çağırmak

Ogrenci.cift_mi(21564) #staticmethod


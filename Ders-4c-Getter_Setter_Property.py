class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas  # Init sırasında da setter çalışır

    @property
    def yas(self):
        """Getter: _yas değerini okur."""
        return self._yas

    @yas.setter
    def yas(self, deger):
        """Setter: yas değerine atama yapılırken doğrulama uygular."""
        if not isinstance(deger, int):
            raise TypeError("Yaş bir tamsayı olmalıdır.")
        if deger < 0:
            raise ValueError("Yaş negatif olamaz.")
        self._yas = deger

# Kullanım

kisi1 = Kisi("Ahmet", 25)

# Metot parantezi () olmadan çağrılır
print(kisi1.yas)  # Output: 25

# Geçersiz atama denemesi hata fırlatır
try:
    kisi1.yas = -5
    kisi1.yas = "yirmi"
    kisi1.yas = "30"
    kisi1.yas = 30.5
    kisi1.yas = 21
except ValueError as e:
    print(e)  # Output: Yaş negatif olamaz.
except TypeError as e:
    print(e)  # Output: Yaş bir tamsayı olmalıdır.
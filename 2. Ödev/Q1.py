class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisiBilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenekEkle(self, yetenek):
        self.yetenekler.append(yetenek)


Kisi = Insan("Bilal", "Günden", 23, "Türkiye", "İstanbul")
Kisi.yetenekEkle("Kamp")
bilgiler = Kisi.kisiBilgileri()
print(bilgiler)

class Ogrenci:
    def __init__(self, ogrenciAdi, ogrenciSoyadi, ogrenciSinifi):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinifi = ogrenciSinifi

    def ogrenciBilgiGoster(self):
        print("Adı : {} \n Soyadı : {} \n Sınıfı : {}".format(self.ogrenciAdi, self.ogrenciSoyadi, self.ogrenciSinifi))


class Soru:
    def __init__(self):
        self.dogruSayisi = int(input("Öğrenci doğru sayısı :"))
        self.yanlisSayisi = int(input("Öğrenci yanlış sayısı :"))

    def netSayisi(self):
        toplamSoru = self.dogruSayisi + self.yanlisSayisi
        if toplamSoru > 100:
            print("Toplam soru sayısı 100'den fazla olamaz.")
            quit()

        gidenDogruSayisi = self.yanlisSayisi / 4
        netSayisi = self.dogruSayisi - gidenDogruSayisi
        return netSayisi

    def puanHesaplama(self, netSayisi):
        ogrenciPuan = netSayisi * 10
        if ogrenciPuan < 0:
            ogrenciPuan = 0
        return ogrenciPuan


ogrenciExample = Ogrenci("Bilal", "Günden", "11/C")
Soru1 = Soru()
ogrenciExample.ogrenciBilgiGoster()
print(Soru1.puanHesaplama(Soru1.netSayisi()))

class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinifi):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinifi = ogrenci_sinifi

    def ogrenciBilgiGoster(self):
        print(
            "Adı : {} \n Soyadı : {} \n Sınıfı : {}".format(self.ogrenci_adi, self.ogrenci_soyadi, self.ogrenci_sinifi))


class Soru:
    def __init__(self):
        while True:
            self.dogru_sayisi = int(input("Öğrenci doğru sayısı :"))
            self.yanlis_sayisi = int(input("Öğrenci yanlış sayısı :"))
            toplam_soru = self.dogru_sayisi + self.yanlis_sayisi
            if toplam_soru > 50:
                print("Toplam soru sayısı 50'den fazla olamaz.")
                continue
            else:
                # we're happy with the value given.
                # we're ready to exit the loop.
                break

    def netSayisi(self):

        net_sayisi = self.dogru_sayisi - (self.yanlis_sayisi / 4)
        print("Öğrenci net sayısı : {}".format(net_sayisi))
        return net_sayisi

    def puanHesaplama(self, net_sayisi):
        ogrenci_puan = net_sayisi * 2
        return ogrenci_puan


ad = input("AD: ")
soyad = input("SOYADI: ")
sinif = input("SINIF: ")
ogrenciExample = Ogrenci(ad, soyad, sinif)
Soru1 = Soru()
ogrenciExample.ogrenciBilgiGoster()
print("Öğrenci Puanı : {}".format(Soru1.puanHesaplama(Soru1.netSayisi())))

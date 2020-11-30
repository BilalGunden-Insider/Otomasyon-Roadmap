import math
from num2words import num2words

""" İLK SORU """


def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    list = []
    for i in range(min_sayi, max_sayi + 1):
        if i % bolunecek_sayi == 0:
            list.append(i)

    toplam_sayi = len(list)
    print(list)
    return toplam_sayi


# aradaki_sayi = bolunenSayiBulma(23, 128, 9)
# print(aradaki_sayi)

"""İKİNCİ SORU"""


def basamak_bulma(n):
    if n > 0:
        basamak = int(math.log10(n)) + 1
    elif n == 0:
        basamak = 1
    else:
        basamak = int(math.log10(-n)) + 2
    return basamak


def sayi_okuma(number):
    print(num2words(number))


def sayi_atama(sayi):
    basamak_sayisi = basamak_bulma(sayi)
    if basamak_sayisi == 2:
        okunacak_sayi = sayi
        sayi_okuma(okunacak_sayi)
    else:
        print("sayı 2 basamaklı değil")


# sayi_atama(13)

"""ÜÇÜNCÜ SORU"""

vize1 = int(input("Birinci vize notunu giriniz : "))
vize1_etki_notu = int(vize1 * 30 / 100)

vize2 = int(input("İkinci vize notunu giriniz : "))
vize2_etki_notu = int(vize2 * 30 / 100)

final = int(input("Final notunu giriniz : "))
final_etki_notu = int(final * 40 / 100)

genelNot = vize1_etki_notu + vize2_etki_notu + final_etki_notu


def not_kontrol():
    if 100 > vize1 > 0 and 100 > vize2 > 0 and 100 > final > 0:
        if genelNot >= 90:
            print("genel Not ortalaması = {} ".format(genelNot))
            print("Not kartı = AA")
        elif 90 > genelNot >= 85:
            print("genel Not ortalaması = {} ".format(genelNot))
            print("Not kartı = BA")
        elif 85 > genelNot >= 80:
            print("genel Not ortalaması = {} ".format(genelNot))
            print("Not kartı = BB")
        elif 80 > genelNot >= 75:
            print("genel Not ortalaması = {} ".format(genelNot))
            print("Not kartı = CB")
        elif 75 > genelNot >= 70:
            print("genel Not ortalaması = {} ".format(genelNot))
            print("Not kartı = CC")
        elif 70 > genelNot >= 65:
            print("genel Not ortalaması = {} ".format(genelNot))
            print("Not kartı = DC")
        elif 65 > genelNot >= 60:
            print("genel Not ortalaması = {} ".format(genelNot))
            print("Not kartı = DD")
        elif 60 > genelNot >= 55:
            print("genel Not ortalaması = {} ".format(genelNot))
            print("Not kartı = FD")
        elif 55 > genelNot:
            print("genel Not ortalaması = {} ".format(genelNot))
            print("Not kartı = FF")

    else:
        print("Girilen not değerleri 0-100 arasında olmalı")

not_kontrol()

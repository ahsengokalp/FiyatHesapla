def metrekare(en, boy):
        sonuc = en * boy
        return sonuc

def daire_fiyati(kat, en, boy):
        ARA_KAT = 2
        UST_KAT = 1.6
        ZEMIN_KAT = 0.9
        if kat == 1:
            sonuc = ARA_KAT * metrekare(en, boy) * 5000
            return sonuc
        elif kat == 2:
            sonuc = UST_KAT * metrekare(en, boy) * 5000
            return sonuc
        elif kat == 3:
            sonuc = ZEMIN_KAT * metrekare(en, boy) * 5000
            return sonuc
print("1-Daire Fiyati Hesaplama")
print("1-Ara Kat")
print("2-Ust Kat")
print("3-Zemin Kat")
kat=int(input("Kat seciniz: "))
en=int(input("Daire enini giriniz: "))
boy=int(input("Daire boyunu giriniz: "))
print("Fiyat: ",daire_fiyati(kat,en,boy))

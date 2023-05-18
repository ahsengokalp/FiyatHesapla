deniz_kenari=1.6
sehir_merkezi=1.2
kirsal=0.8
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
def cember_cevre_hesaplama(yaricap):
    PI=3.14
    sonuc=2*PI*yaricap
    return sonuc
def dıkdortgen_cevre_hesaplama(kenar1,kenar2):
    sonuc=2*(kenar1+kenar2)
    return sonuc

def arsa_fiyat_cember(konum,yaricap):
    global deniz_kenari
    global sehir_merkezi
    global kirsal

    if konum==1:
        sonuc=deniz_kenari*cember_cevre_hesaplama(yaricap)*1000
        return sonuc
    elif konum==2:
        sonuc=sehir_merkezi*cember_cevre_hesaplama(yaricap)*1000
        return sonuc
    elif konum==3:
        sonuc=kirsal*cember_cevre_hesaplama(yaricap)*1000
        return sonuc
def arsa_fiyat_dıkdortgen(konum,kenar1,kenar2):
    global deniz_kenari
    global sehir_merkezi
    global kirsal
    if konum==1:
        sonuc=deniz_kenari*dıkdortgen_cevre_hesaplama(kenar1,kenar2)*1000
        return sonuc
    elif konum==2:
        sonuc=sehir_merkezi*dıkdortgen_cevre_hesaplama(kenar1,kenar2)*1000
        return sonuc
    elif konum==3:
        sonuc=kirsal*dıkdortgen_cevre_hesaplama(kenar1,kenar2)*1000
        return sonuc
def kiralik_daire_fiyati(kat,en,boy):
    ARA_KAT = 2
    UST_KAT = 1.6
    ZEMIN_KAT = 0.9
    if kat == 1:
        sonuc = (ARA_KAT * metrekare(en, boy) * 5000)//180
        return sonuc
    elif kat == 2:
        sonuc = (UST_KAT * metrekare(en, boy) * 5000)//180
        return sonuc
    elif kat == 3:
        sonuc = (ZEMIN_KAT * metrekare(en, boy) * 5000)//180
        return sonuc

print("1-Daire Fiyati Hesaplama")
print("2-Arsa Fiyati Hesaplama")
print("3-Kiralık Daire Aylık Fiyati Hesaplama")
sayi=int(input("Seçiminizi giriniz: "))
if sayi==1:
   print("1-Ara Kat")
   print("2-Ust Kat")
   print("3-Zemin Kat")
   kat=int(input("Kat seciniz: "))
   en=int(input("Daire enini giriniz: "))
   boy=int(input("Daire boyunu giriniz: "))
   print("Fiyat: ",daire_fiyati(kat,en,boy))
elif sayi==2:
   print("1-Daire")
   print("2-Dikdortgen")
   sekil=int(input("Arsanin seklini giriniz: "))
   print("1-Deniz Kenari")
   print("2-Sehir Merkezi")
   print("3-Kirsal ")
   konum=int(input("İstediğiniz konumu giriniz: "))
   if sekil==1:
        yaricap=int(input("Arsanın yaricapini girin: "))
        print("Fiyat:",arsa_fiyat_cember(konum,yaricap))
   elif sekil==2:
        kenar1=int(input("Arsanin birinci kenarini girin: "))
        kenar2=int(input("Arsanin ikinci kenarini girin: "))
        print("Fiyat:",arsa_fiyat_dıkdortgen(konum,kenar1,kenar2))
elif sayi==3:
   print("1-Ara Kat")
   print("2-Ust Kat")
   print("3-Zemin Kat")
   kat = int(input("Kat seciniz: "))
   en = int(input("Daire enini giriniz: "))
   boy = int(input("Daire boyunu giriniz: "))
   print("Kira Fiyatı: ", kiralik_daire_fiyati(kat, en, boy))  
      

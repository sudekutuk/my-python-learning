def selamlama(isim):
    return "Selamun aleykum, " + isim
print(selamlama("sudee"))
print(selamlama("nazz"))

def toplam(sayi1,sayi2):
    return sayi1 + sayi2

print(toplam(1,2))

def yasHesaplama(dogumYili):
    return 2025 - dogumYili

def emekliligEKacYilKaldi(dogumYili,isim):
    yas = yasHesaplama(dogumYili)
    kalanSure = 65 - yas
    if kalanSure > 0:
        return f"{isim}, emekliliginize {kalanSure} yil kaldi."
    else: 
        return f"{isim}, zaten emeklisin ezik"
print(emekliligEKacYilKaldi(2004,"sude"))
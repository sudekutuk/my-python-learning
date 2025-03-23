import module # dosya ismini yazmamiz yeterli

sonuc = module.sayi
sonuc = module.sayilar
sonuc = module.urun
sonuc = module.urun["urunAdi"]
sonuc = module.urun["renkler"]
sonuc = module.toplam(9,9)


import module as m
sonuc = m.sayilar


from module import sayi, sayilar, urun

sonuc = sayi
sonuc = sayilar
sonuc = urun


from module import * # module dosyasindaki her seyi getirtir

sonuc = urun
sonuc = toplam(10,20)
print(sonuc)
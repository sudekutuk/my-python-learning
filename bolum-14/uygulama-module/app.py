"""
    module1 (db)        : urunler
    module2 (methods)   : urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)       :

        yeni urun ekleme => urunEkle("Iphone 15", 60000)
        urun guncelle => urunGuncelle(1, "Iphone 15 pro", 80000)
        urunleri listele => urunleriGetir()


"""


from methods import *

urunEkle("Iphone 20", 90000 )
urunEkle("samsung s29", 90000 )

sonuc = urunleriGetir()

# for i in sonuc:
#    print(i["urunAdi"])

urunGuncelle(1, "Iphone 15 pro", 80000)

for i in urunleriGetir():
   print(i["urunAdi"])
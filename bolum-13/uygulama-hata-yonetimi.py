liste = ["1","3","5","20b","abc","10a","60"]

# 1- Liste elemanlari icindeki sayisal degerleri bulunuz.
# for sayi in liste:
#     try:
#         sonuc = int(x)
#         print(sonuc)
#     except ValueError:
#         continue

# 2- Kullanici 'quit (q)' degerini girmedikce aldiginiz her inputun sayi oldugundan emin olunuz aksi halde hata mesaji yazin.

# while True:
#     sayi = input("sayi giriniz: ")
#     if(sayi == "q"):
#         break

#     try:
#         sonuc = float(sayi)
#         print(f"girilen sayi: {sayi}")
#         break
#     except:
#         print("gecersiz sayi")
#         continue



# 3- Dictionary ve key bilgilerini parametre olarak alan get(dict,key) fonksiyonu hazirlayiniz.

urun = {"urunAdi":"Iphone 13"}

# d["fiyat"] => KeyError
# get(urun,"fiyat") => None
# get(urun,"urunAdi") => Iphone 13

def get(liste, key):
    try:
        return liste[key]
    except KeyError:
        return None
    
sonuc = get(urun, "fiyat")
sonuc = get(urun,"urunAdi")
print(sonuc)
# 1
markalar = ["Toyota","Bmw","Renault","Mercedes"]

# 2
sonuc = len(markalar)
# 3
sonuc = markalar[0] + " " +markalar[-1]
# 4 guncelleme
markalar[2] = "Togg"
# 5
sonuc = "Togg" in markalar
# 6
sonuc = markalar[0:2]
# 7
sonuc = markalar + ["Ford","Citroen"]
# 8
del markalar[-1] 
sonuc = markalar
# 9
ogrenci1 = ["Yigit Bilgi",2010,[70,80,90]]
ogrenci2 = ["Ada Bilgi",2011,[70,70,80]]
ogrenci3 = ["Cinar Turan",2017,[60,60,90]]
ogrenciler = [ogrenci1,ogrenci2,ogrenci3]
# 10
yas1 = 2025 - ogrenciler[0][2]
yas2 = 2025 - ogrenciler[1][2]
yas3 = 2025 - ogrenciler[2][2]

print(yas1 , yas2 , yas3)
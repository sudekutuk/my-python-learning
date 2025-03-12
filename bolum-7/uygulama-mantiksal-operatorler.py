# 1
x =14
izin = True
sonuc = (x >= 18) or (izin == True)
print(sonuc)
# 2
not_bilgisi = True
ders_notu = 30
if( 50 < ders_notu < 100):
    print("gecti")
else: print("gecemedi")
# 3
notOrt = 80
zayifiVarMi = True
sonuc = (notOrt >= 70 and zayifiVarMi == False)
print(f"tesekkur alma durumu: {sonuc}") 
# 4
egitim = "lise"
sigaraVarMi = False
sonuc = ((egitim == "onlisans" or egitim == "lisans") and sigaraVarMi == False)
# 5
username = "xjcd"
email = "xxx@xxx.com"
parola = "1122334455"
sonuc = (email == "xxx@xxx.com" or username == "xjcd" ) and (parola == "1122334455")
print(sonuc)
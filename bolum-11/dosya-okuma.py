"""
open() dosya acmak icin kullanilir
open(dosya_adi,dosya_erisme_modu)
"r" okuma modu (default mode)
seek cursor konumu f.seek()ile cagrilir.
"""
f = open("log.txt",encoding='utf-8')
print(f.read()) # okuma metodu
f.readline() #kaldigimiz satirdan itibaren satilari okumamizi saglar
f.readlines() # dizi seklinde satirlari getirir.
f.close() # dosyayi kapatir.
f.closed # true / false dondurur. kapali olup olmadigi kontrol edilir
print(f)

## dosyayi kapatmayi unutma! Bellekte yer kapliyor...
programlama_dilleri = ["Python","C#","Java","Javascript"]

sonuc = programlama_dilleri
sonuc = type(programlama_dilleri)
sonuc = programlama_dilleri[0:2] # 0 ve 1. indisler alinir.(2 dahil degil)

sonuc = programlama_dilleri[:2] # en bastan 2'ye kadar(2dahil degil)

sonuc = programlama_dilleri[:] # hepsi

sonuc = programlama_dilleri[-3:-1] # -3 ten -1 e kadar (-1 dahil degil!)

#guncelleme
programlama_dilleri[-1] = "Php" #atama yaptik

sonuc = programlama_dilleri
sonuc = len(programlama_dilleri)
sonuc = programlama_dilleri + ["Go","Delphi"]

sonuc = "Python" in programlama_dilleri
sonuc = "React" in programlama_dilleri #kosul ifadeleri

del programlama_dilleri[0] # sildiiii

for dil in programlama_dilleri:
    print(dil)


#print(sonuc)
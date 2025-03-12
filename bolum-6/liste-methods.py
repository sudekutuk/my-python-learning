sayilar = [3,4,6,43,65,87,9,9,9,9]

isimler = ['naz','sude','erva','ibo','ayse','sude']

sonuc = min(sayilar)
sonuc = min(isimler)
sonuc = max(isimler)
sonuc = max(sayilar)

#ekleme
# sayilar.append(12)
# isimler.append('cinar')

# sayilar.insert(0,100) #index e gore sayi eklemesi yapar.
# sayilar.insert(-1,33)
# sayilar.insert(-3,100)
# sayilar.insert(len(sayilar),100 )
# sonuc = sayilar
# sonuc = isimler

# #silme
# sayilar.pop()
# sayilar.pop(0)

# isimler.remove('sude')

#siralama
sayilar.sort()
isimler.sort()
sayilar.reverse()

sonuc = sayilar.count(9)
sonuc = isimler.count('sude')

#arama
sonuc = sayilar.index(9)

# sonuc = isimler
# sonuc = sayilar
print(sonuc)
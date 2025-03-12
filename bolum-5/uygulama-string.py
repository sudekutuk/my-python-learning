title = "Python ile Programlama Dersleri"

#1
print(len(title))
#2
print(title[0:7])
#3
print(title[4] + title[-5])
#4
print(title[::-1])
#5
ad=input("ad gir lo: ")
soyad=input("soyad gir lo: ")
not1=input("1.notu gir lo: ")
not2=input("2.notu gir lo: ")
ort= (float(not1) + float(not2)) / 2
msj = f" {ad} {soyad} isimli ogrencinin 1. notu {not1}, 2. notu {not2} ve not ortalamasi {ort} olarak hesaplanmistir. "
print(msj)
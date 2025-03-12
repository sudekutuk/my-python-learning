# 1  kendisine gonderilen bir kelimeyi belirtilen kez ekranda gosteren fonksiyonu yaziniz
def yazdir(text,adet):
    return text * adet

print(yazdir("sude ",9))

# 2 dikdortgenin alan ve cevresini hesaplayan fonk yaziniz

def dikdortgen(k1,k2):
    c=2*(k1+k2)
    a=k1*k2
    return a,c

print(dikdortgen(4,5))

# 3 yazi tura uygulamasini fonk kullanarak yapiniz.
def yaziTura():
    import random
    sayi = random.random()

    if sayi > 0.5:
        return "Tura"
    else:
        return "Yazi"
    
sonuc = yaziTura()
print(sonuc)

# 4 kendisine gonderilen 2 sayi arasindaki tum asla sayilari bulan fonk yaziniz

def asalSayiBul(sayi1,sayi2):
    for i in range(sayi1,sayi2):
        if(i > 1):
            for j in range(2,i):
                if (i % j == 0):
                    break
            else:
                    print(i)

asalSayiBul(10,30)

# 5 kendisine gonderilen bir sayinin tam bolenlerini bir liste seklinde donduren fonk yaziniz

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(1,sayi+1):
        if(sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(9))
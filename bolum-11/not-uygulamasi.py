#Not uygulamasi

# 1- Menu
    # 1- Not Gir
    # 2- Ortalama Goster (90-100-> A)
    # 3- Notlarini Kayit Et
    # 4- Cikis

def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3)/3

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 80 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "BB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CB"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "CC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DC"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "DD"
    elif ortalama >= 40 and ortalama <= 49:
        harf = "FD"
    elif ortalama >= 0 and ortalama <= 39:
        harf = "FF"

    return f"{ogrenciAdi} : {harf} ( {ortalama} )\n"

def not_gir():
    ad = input("ogrenci adi: ")
    soyad = input("ogrenci soyadi: ")
    not1 = input("not giriniz: ")
    not2 = input("not giriniz: ")
    not3 = input("not giriniz: ")

    with open("notlar.txt","a",encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3 + '\n' )



def notlari_oku():
    with open("notlar.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def notlari_kaydet():
    with open("notlar.txt","r",encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))
        
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            file2.writelines(liste)

while True:
    islem = input("1- Not Gir\n2- Notlari Oku\n3- Notlari Kayit Et\n4- Cikis\n")
    if islem == "1":
        not_gir()
    elif islem == "2":
        notlari_oku()
    elif islem == "3":
        notlari_kaydet()
    else:
        break
#Not uygulamasi

# 1- Menu
    # 1- Not Gir
    # 2- Ortalama Goster (90-100-> A)
    # 3- Notlarini Kayit Et
    # 4- Cikis

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
            print(satir)

def notlari_kaydet():
    pass


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
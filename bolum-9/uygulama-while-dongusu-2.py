# klavyeden girilen n sayidaki ogrenci bilgisini liste icerisinde saklayiniz.
# dictionary listesi yapisi (ogrenciNo, ogrenciAdi, ogrenciSoyad) seklinde olsun.
# urun ekleme islemi bittiginde ogrencileri listeleyiniz.

devammi = "e"
ogrenciler= []

while (devammi != "h"):
    ogrenciNo = input("ogrenci no: ")
    ogrenciAdi = input("ogrenci adi: ")
    ogrenciSoyad = input("ogrenci soyadi: ")

    ogrenciler.append({
        "ogrenciNo": ogrenciNo,
        "ogrenciAdi": ogrenciAdi,
        "ogrenciSoyad": ogrenciSoyad,
    })

    devammi = input("devam mi ? (e/h): ")

for ogrenci in ogrenciler:
    print(f"{ogrenci["ogrenciNo"]} numarali ogrencinin adi {ogrenci["ogrenciAdi"]} {ogrenci["ogrenciSoyad"]}")
# 
ogrenci_bilgileri = {
    101: {
        'Ad': 'Yigit',
        'Soyad': 'Bilgi',
        'DogumYili': 2010,
        'Notlar': (40,80,90)
    },
    102: {
        'Ad': 'Ada',
        'Soyad': 'Bilgi',
        'DogumYili': 2012,
        'Notlar': (80,80,80)
    },
    103: {
        'Ad': 'Cinar',
        'Soyad': 'Turan',
        'DogumYili': 2017,
        'Notlar': (70,70,70)
    }
}
print(ogrenci_bilgileri)


# 
ogrenciNo = int(input("ogrenci nosu: "))
ogrenci = ogrenci_bilgileri[ogrenciNo]
ortalama = (ogrenci["Notlar"][0] + ogrenci['Notlar'][1] + ogrenci['Notlar'][2] ) / 3

print(f'{ogrenciNo} numarali {ogrenci['Ad']} {ogrenci['Soyad']} ismindeki ogrencinin yasi {2025-ogrenci['DogumYili']} ve not ortalamasi {ortalama}.')
urunler = [
    {"urunAdi":"Hp Victus 1","fiyat":32999},
    {"urunAdi":"Lenovo Thinkpad","fiyat":25499},
    {"urunAdi":"Apple Macbook","fiyat":49999},
    {"urunAdi":"Huawei Matebook","fiyat":26999},
    {"urunAdi":"Casper Nirvana","fiyat":20000},
    {"urunAdi":"Hp Victus 2 ","fiyat":30000},
]

# 1 Asagidaki cumleyi butun urunlere uygulayiniz.
#  "HpVictus marka urunun fiyati ....turk lirasi"

# for urun in urunler:
#     print(f"{urun['urunAdi']} marka urunun fiyati {urun['fiyat']} ")

# 2 urunlerin fiyatlari toplami nedir?
# top = 0
# for urun in urunler:
#     top += urun["fiyat"]
# print(top)

# 3 25000 ile 40000 arrasindaki urunleri listeleyiniz

# for urun in urunler:
#     if (25000<urun["fiyat"]<40000):
#         print(urun["urunAdi"])

# 4 Kullanicidan alinan anahtar kelimeye gore urunleri listeleyiniz
key = input("Anahtar Kelime giriniz: ")
for urun in urunler:
    if(urun["urunAdi"].lower().find(key.lower())> -1):
        print(f"{urun['urunAdi']}")
#2000 + 2000 *%18

urunAFiyat = 4000
urunBFiyat = 3000
kdvOrani=0.20
print(urunAFiyat + (urunAFiyat*kdvOrani)) #urun A
print(urunBFiyat + (urunBFiyat*kdvOrani)) #urun B

urunToplami=urunBFiyat+urunAFiyat
print(urunAFiyat+urunBFiyat)
print(urunToplami+(urunToplami*kdvOrani))
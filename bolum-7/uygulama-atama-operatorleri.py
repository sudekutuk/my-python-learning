a, b, c = 4, 8, (12, 2)
# 1
# sayi1 = int(input("Sayi giriniz: " ))
# sayi2 = int(input("Sayi giriniz: " ))
# sonuc = (sayi1*sayi2) - (a + b + c[0] + c[1])
# 2
sonuc = (c[0] + c[1]) // b
# 3
sonuc = (a + b + c[0] + c[1]) % 7
# 4
sonuc = b ** a
# 5 
a, *b , c = (2,4,6,8,13)
sonuc = c ** 3
# 6
a, b, *c = (2,4,6,8,13)
sonuc = c[0] + c[1]
print(sonuc)
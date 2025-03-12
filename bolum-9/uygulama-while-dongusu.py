# 1 baslangic ve bitis degerlerini kullanicidan aliniz ve bu degerler arasindaki tum cift sayilari yazdiriniz.
# baslangic = int(input("baslangic degerini gir: "))
# bitis = int(input("bitis degerini gir: "))
# i = baslangic
# while (i < bitis):
#     if(i % 2 == 0):
#         print(i)
#     i += 1   

# 2 (1-100) arasindaki sayilarin azalan sekilde yazdiriniz.
# i = 100
# while (i > 0):
#     print(i)
#     i -= 1

# 3 Kullanicidan alicaginiz 5 sayiyi ekrandan sirali bir sekilde yazdirin.
# i = 0 
# sayilar = []

# while (i < 5 ):
#     sayi = int(input("sayi giriniz: "))
#     sayilar.append(sayi)
#     i += 1
    
# sayilar.sort()
# print(sayilar)

# 4 Klavyeden girisi istenen username bilgisi icin bosluk girldigi surece tekrar username girisi isteyiniz.

username = ""

while not username:
    username = input("kullanici adi: ")

print("girilen username: " + username)

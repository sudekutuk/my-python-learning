# open(dosya_adi,dosya_erisim_modu)

#"r"
#"w"
#"a": (append) ekleme. Dosya konumda yoksa ekleme yapiyor.
#"r+": hem okuma hem yazma modunu acilir. Dosya konumda yoksa hata verir.

with open("dosya.txt","r+",encoding="utf-8") as file:
    # file.seek(0)
    print(file.read())
    file.write("sifirinci satir")
    
# yazma yaparken yeni dosya olusur ve icine yazdirir

file = open("dosya.txt","w",encoding="utf-8")
file.write("Sude Su\n")
file.close()

# "w" yazma modu
# eger konumda ayni dosya varsa dosyayi siler yeni dosya olusturur.

with open("dosya.txt","w",encoding="utf-8") as file:
    file.write("merhaba,\n")
    file.write("Sude Su\n")

with open("dosya.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i,end="")
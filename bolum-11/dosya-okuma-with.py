# file = open("log.txt",encoding='utf-8')

# print(file.read())

# file.close()
try:
    with open("log2.txt",encoding='utf-8') as file:
        # print(file.read(10))
        # print(file.tell()) # o andaki konumunu soyler
        # print(file.read()) 
        # print(file.tell())
        for i in file:
            print(i,end="") # end ile dosya icerigini bosluk satir olmadan satir satir okuyabiliriz
except FileNotFoundError as e:
    print("dosya okuma hatasi")
# yani with anahtari file i acarken kullandiktan sonra 
# otomatik olarak isi bitince kapatmayi sagliyor.


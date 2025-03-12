# Bankamatik uygulamasi

# Hesap bilgileri tutulacak.(dict)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonleri tanimlanicak
# cekilmek istenen tutar hesapta yoksa ek hesabin kullanilmak istendigi sorulacak.

hesapBilgileri = [
    {
        "ad": "Sude",
        "hesapNo":"12345",
        "bakiye": 90000,
        "ekHesap": 5000,
        "username": "sudesude",
        "password": "1234"
    },
    {
        "ad": "Emre",
        "hesapNo":"12345",
        "bakiye": 10000,
        "ekHesap": 1000,
        "username": "emremre",
        "password": "12345q"
    }
]
def menu(hesap):
    pass

def login():
    username = input("username: ")
    password = input("password: ")

    isLoggedIn = False

    for hesap in hesapBilgileri:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            print("giris yapildi")
            break
    if not(isLoggedIn):
        print("giris yapilamadi")
login()
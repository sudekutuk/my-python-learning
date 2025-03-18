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
        "password": "12345"
    }
]
def menu(hesap):
    print("\n")

    print(f"merhaba, {hesap["ad"]} ")

    print("1- Bakiye Sorgulama")
    print("2- Para Cekme")
    print("3- Para Yatirma")

    islem = input("Yapmak Istediginiz Islem: ")

    if islem == "1":
        bakiyeSorgulama(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    else:
        print("Lutfen tekrar secim yapiniz.")

    menu(hesap)

def paraYatirma(hesap):
    pass

def paraCekme(hesap):
    miktar = float(input("cekmek istediginiz miktar: "))
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("paranizi alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            ekHesapKullanimIzni = input("ek hesap kullanmak ister misiniz?")
            
            if ekHesapKullanimIzni == "e":
                kullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacakMiktar
                print("paranizi alabilirsiniz")
            else:
                print("bakiye yetersiz...")
        else:
                print("bakiye yetersiz...")

def bakiyeSorgulama(hesap):
    print(f"bakiye: {hesap["bakiye"]}")
    print(f"ek bakiye: {hesap["ekHesap"]}")


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
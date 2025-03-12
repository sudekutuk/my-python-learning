def toplam():
    return 10 + 20

sonuc = toplam()
print(sonuc)

def saat():
    import datetime
    return datetime.datetime.now().hour

def yil():
    import datetime
    return datetime.datetime.now().year


def yasHesapla():
    return yil() - 1983

print(yasHesapla())

def selamlama():
    if(saat() < 12):
        return "gunoooo"
    else:
        return "selaaammm"
print(selamlama())
def selamlama(isim,mesaj):
    return f"{mesaj} {isim}"

sonuc = selamlama("sude","merhaba")
sonuc = selamlama("selam","merhaba")
# sonuc = selamlama("sude")
# sonuc = selamlama()

def usAlma(taban,us=2):
    return taban ** us
sonuc = usAlma(2,3)
sonuc = usAlma(5)

def toplama(a,b):
    return a + b

def cikarma(a,b):
    return a - b

def islem(a,b,fn = toplama):
    return fn(a,b)

sonuc = islem(3,9,usAlma)
print(sonuc)
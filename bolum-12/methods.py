# class
class Product:
    # attribute, property
    def __init__(self,name, price, isActive):
        self.name = name # self p1,p2,p3 demek
        self.price = price 
        self.isActive = isActive
    # instance method 
    def intro(self):
        return f"urun adi: {self.name} urun fiyati: {self.price}"

    def kdv_price(self):
        return self.price * 1.20


# Instance , Nesne

p1 = Product("Iphone 15", 50000, True)
p2 = Product("Iphone 15 Pro",60000, True)
p3 = Product("Samsung S24", 70000, True)

# sonuc = p3.name
# sonuc = p3.price

urunler = [p1,p2,p3]
for urun in urunler:
    if urun.isActive:
        print(urun.intro())
        # print(urun.kdv_price())

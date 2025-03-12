customers = ["sadikturan","ahmetyildiz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]

# 1 
customers.append("sadikturan")
order_totals.append(5000)
# sonuc = customers
# sonuc = order_totals

# 2
# customers.pop()
# order_totals.pop()

# 3
sonuc = f"{customers[0]} isimli musterinin siparis toplami {order_totals[0] + order_totals[4]} liradir."
sonuc = f"{customers[1]} isimli musterinin siparis toplami {order_totals[1] } liradir."
# sonuc = order_totals

# 4
customers.sort()

# 5
order_totals.sort()
order_totals.reverse()
sonuc = order_totals

# 6
sonuc = min(order_totals)

# 7
sonuc = customers.count("sadikturan")

# 8
customers.remove("ahmetyildiz")
sonuc = customers

# 9
# customers.clear()
# order_totals.clear()
# sonuc = customers
# sonuc = order_totals

# 10 
kullaniciAdi = input("Kullanici adi giriniz: " )
siparisToplami = input("Toplam siparis sayisini giriniz: ")
customers.append(kullaniciAdi)
order_totals.append(siparisToplami)
sonuc = customers
sonuc = order_totals

print(sonuc)
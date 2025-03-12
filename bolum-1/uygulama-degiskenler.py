name = "Sadik"
surname = "Turan"
telNo = "053221234567"
mail="info@sadikturan.com"
location = "Kocaeli"
product1Name = "Kablosuz Mouse"
product1Price = 550
product2Name = "Kablosuz Klavye"
product2Price = 650
product3Name = "Dizustu Bilgisayar"
product3Price = 55000

print("Costumer: " + name + " " + surname )
print("E-mail: "+mail)
print("Number: "+telNo)
print("Location: "+location)

totalPrice=product1Price+product2Price+product3Price
print("Total: " + str(totalPrice))
print("Toplam Kdv orani: "+str(totalPrice*0.18))


# x = 10
# y = 20
# x = y
# y = 30
# print(x , y)

#reference 

a = ["elma","armut"]
b = ["elma","armut"]

a = b #adres kopyaladiniz.
a[0] = "uzum"
print(a , b)

#liste kopyalama
listeA = [10,20]
# listeB = listeA.copy() #1. yontem
listeB = list(listeA) #2. yontem
listeB[0] = 30

print(listeA,listeB)
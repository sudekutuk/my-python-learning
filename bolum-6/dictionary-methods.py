# Dictionary Methods

yemekTarifi = {
    "yemekAdi": "Musakka",
    "yemekTarifi": "tarif aciklamasi...",
    "resim": "1.jpg"
}

# access items
sonuc = yemekTarifi["yemekAdi"]
sonuc = yemekTarifi.get("yemekAdi")
sonuc = yemekTarifi.keys()
sonuc = yemekTarifi.values()
sonuc = yemekTarifi.items()

# update items
# yemekTarifi["yemekAdi"] = "Manti"
# yemekTarifi.update({"yemekAdi":"Manti"})
# yemekTarifi.update({"yemekAdi2":"Manti"})

# delete items
# yemekTarifi.pop("yemekAdi")
# yemekTarifi.popitem()
yemekTarifi.clear()

#copy => referans 

sonuc = yemekTarifi
print(sonuc)
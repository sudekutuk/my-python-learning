kursAdi = "Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"
 
#1
a = " Btk Akademi "
sonuc = a.strip()
#2
sonuc = kursAdi.lower()
# 3
sonuc = website.count(".")
# 4
sonuc = website.startswith("https")
# 5
sonuc = website.endswith("tr")
# 6
sonuc = kursAdi.isalpha()
# 7
sonuc = kursAdi.replace(" ","-")
# 8
sonuc = kursAdi.replace("Python","ReactJs")
# 9
sonuc = website.find("www")
# 10
sonuc =  kursAdi.split()[3]
print(sonuc)



#string concat
ad= "sude"
soyad = "sude"
yas = 20

#msj= "My name is " + ad + " " + soyad + "." + "I'm " + str(yas) + " years old."
#string format
#msj="My name is {} {}. I'm {} years old.".format(ad,soyad,yas)
#msj="My name is {0} {1}. I'm {2} years old.".format(ad,soyad,yas)
msj="My name is {a} {s}. I'm {y} years old.".format(a=ad,s=soyad,y=yas)
msj= f"My name {ad} {soyad}. Im {yas} years old."
print(msj)
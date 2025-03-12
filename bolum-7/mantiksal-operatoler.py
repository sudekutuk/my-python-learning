# (yas >=18) => true, false
# (mezuniyet == 'lise') ya da (mezuniyet == 'universite') => true, false

# sonuc = (yas >= 18) ve (mezuniyet == 'lise' veya mezuniyet == 'universite')

x = 11

sonuc = (x > 5) and (x < 10)

sonuc = (x > 0) and (x % 2 == 0)
sonuc = (x > 0) or (x % 2 == 0)
sonuc = not(x > 0)
print(sonuc)
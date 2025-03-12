my_list = [1,2,3]
my_tuple = (1,2,3)  #degistirilemez

print(type(my_list))
print(type(my_tuple))

my_list[0] = 2
# my_tuple[0] = 2 degisemeeeezzz

my_list.append(3)
#my_tuple.append(3) # we cant append anything bcs tuples cant change


sonuc = my_tuple
# sonuc = my_tuple

my_list.append(3)
sonuc = my_list.count(1)
print(sonuc)
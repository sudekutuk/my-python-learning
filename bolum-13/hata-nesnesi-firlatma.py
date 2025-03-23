# print(10/0)

# x = 10

# if x > 5:
#     # raise ValueError("x besten buyuk olamaz")
#     raise Exception("x besten buyuk olamaz")

def renklendir(text, renk):
    renkler = ("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalidir.")

    if type(renk) is not str:
        raise TypeError("renk str tipinde olmalidir.")
    
    if renk not in renkler:
        raise ValueError("gecersiz renk")
    
    print(f"{text} {renk} olarak yazildi.")

try:   
    renklendir("selam","red")
    # renklendir(10,"red")
    renklendir("selam","black")
    renklendir("selam","pink")
except (TypeError, ValueError) as ex:
    print(ex)

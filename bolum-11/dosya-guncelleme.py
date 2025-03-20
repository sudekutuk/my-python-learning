# with open("markalar.txt","a" ) as file:
#     file.write("6-BMW")

# with open("markalar.txt","r+",encoding="utf-8" ) as file:
#     markalar = file.read()
#     markalar = "1-Toyota\n" + markalar
#     file.seek(0)
#     file.write(markalar)

with open("markalar.txt","r+", encoding="utf-8") as file:
    markalar = file.readlines()
    markalar.insert(2,"3-Lamborghini\n")
    file.seek(0)
    # for i in markalar:
    #     file.write(i)
    file.writelines(markalar)
        

with open("markalar.txt","r",encoding="utf-8" ) as file:
    print(file.read())
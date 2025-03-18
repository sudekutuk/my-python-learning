# local scope
# glonal scope

# x = "global scope"

# def my_func():
#     x = "local scope"
#     print(x)

# my_func()
# print(x)

# name = "Cinar"

# def change_name(new_name):
#     global name #globaldaki name i kullanmak icin
#     name = new_name
#     print(name)

# change_name("Ada")
# print(name)
# name = "global string"
# def greeting():
#     # name = "cinar"

#     def hello():
#         # name = "ada"
#         print("hello", name)

#     hello()

# greeting()

x = 50

def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)
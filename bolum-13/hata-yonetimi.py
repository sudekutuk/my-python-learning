while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)
    except (ZeroDivisionError,ValueError) as e:
        print("y sifir alamaz!")
        print(e)
    except Exception as e:
        print("bilinmeyen hata!")
        print(e)
    else:
        break
    finally: # veri tababi baglantilarinda kullanilabilir
        print("finally blogu acildi")
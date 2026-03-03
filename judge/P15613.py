a=int(input())

if a < 10:
    print("it's cold")

    if a<=0:
        print("water would freeze")

if a >= 10:
    if a > 30:
        print("it's hot")
        if a >= 100:
            print("water would boil")
    if a <= 30:
        print("it's ok")
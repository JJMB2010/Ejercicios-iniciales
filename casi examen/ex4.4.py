
v=100
x=0
while  150>=v and v>=50 or x==0:
    a=int(input("Dime un número: "))
    if a < 0:
        x=1
    if a%2==0:
        v=v/2
    else:
        v=v+a
    if a%3==0:
        v=v-5
    print(v)
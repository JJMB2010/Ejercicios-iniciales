import math

n=int(input())

if n%100==0:
    if (n/100)%4==0:
        print("YES")
    else:
        print("NO")
else:
    if n%4==0:
        print("YES")
    else:
        print("NO")
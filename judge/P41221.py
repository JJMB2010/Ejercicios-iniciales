n=list(str(input()).split())
a=0
if len(n) == 2:
    a=(input())    
    a=int(input())
    a=a+int(n[0])
    a=a+int(n[1])
else:
    for x in range(0,3):
        a=a+int(n[x])
print(a)
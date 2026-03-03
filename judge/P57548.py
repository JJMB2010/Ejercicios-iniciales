n=list(str(input()).split())
a=0
if len(n) == 1:
    a=int(input())
    a=a+int(n[0])
else:
    for x in range(0,2):
        a=a+int(n[x])
print(a)
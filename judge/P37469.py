n=int(input(""))
h=0
m=0
s=0

while n>=3600:
    n=n-3600
    h=h+1
while n>=60:
    n=n-60
    m=m+1
s=n

print(str(h),str(m),str(s))

n=list(str(input()).split())
h=int(n[0])
m=int(n[1])
s=int(n[2])+1

if s>=60:
    s=s-60
    m=m+1
if m>=60:
    m=m-60
    h=h+1
if h==24:
    h=0

if s<10:
    s="0"+str(s)
if m<10:
    m="0"+str(m)
if h<10:
    h="0"+str(h)

x=str(h)+":"+str(m)+":"+str(s)
x=str(x).replace(" ","")
print(x)
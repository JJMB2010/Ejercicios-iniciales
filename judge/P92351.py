import math

n=list(str(input()).split())
div=0
r=0
if int(n[1])==0:
    breakpoint
else:
    div=float(n[0])/float(n[1])
    r=float(n[0])%float(n[1])
div=round(div,0)
if div*int(n[1])+r!=int(n[0]):
    div=div-1
print(int(div),int(r))
import math

n=list(str(input()).split())
div=0
r=0
if int(n[1])==0:
    breakpoint
else:
    div=int(n[0])/int(n[1])
    r=int(n[0])%int(n[1])

print(int(div),int(r))
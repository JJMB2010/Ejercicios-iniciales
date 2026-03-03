n=list(str(input()).split())
e=int(n[0])
c=int(n[1])
f=0

while c>=100:
    c=c-100
    e=e+1

while e>=500:
    e=e-500
    f=f+1
print("Banknotes of 500 euros:",f)
f=0
while e>=200:
    e=e-200
    f=f+1
print("Banknotes of 200 euros:",f)
f=0
while e>=100:
    e=e-100
    f=f+1
print("Banknotes of 100 euros:",f)
f=0
while e>=50:
    e=e-50
    f=f+1
print("Banknotes of 50 euros:",f)
f=0
while e>=20:
    e=e-20
    f=f+1
print("Banknotes of 20 euros:",f)
f=0
while e>=10:
    e=e-10
    f=f+1
print("Banknotes of 10 euros:",f)
f=0
while e>=5:
    e=e-5
    f=f+1
print("Banknotes of 5 euros:",f)
f=0
while e>=2:
    e=e-2
    f=f+1
print("Coins of 2 euros:",f)
f=0
f=e
print("Coins of 1 euro:",f)
f=0
while c>=50:
    c=c-50
    f=f+1
print("Coins of 50 cents:",f)
f=0
while c>=20:
    c=c-20
    f=f+1
print("Coins of 20 cents:",f)
f=0
while c>=10:
    c=c-10
    f=f+1
print("Coins of 10 cents:",f)
f=0
while c>=5:
    c=c-5
    f=f+1
print("Coins of 5 cents:",f)
f=0
while c>=2:
    c=c-2
    f=f+1
print("Coins of 2 cents:",f)
f=0
f=c
print("Coins of 1 cent:",f)
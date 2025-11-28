
a=int(input("Dime un número: "))
b=int(input("Dime un número: "))
i=int(input("Dime un intervalo: "))
num=a
yes=""
while num<b:
    if num%4!=0:
        if num%6==0:
            yes=yes+"*"+str(num)+"*"+","
        else:
            yes=yes+str(num)+","
    num=num+i
yes=yes[:-1]
print(yes)
a=list(str(input("")).split())
nor=sorted(a)
rev=sorted(a, reverse=True)

if nor[0]==rev[0]:
    print(nor[0],"=",rev[0])

else:
    if nor[0]==a[0]:
        if nor[0]==rev[1]:
            print(nor[0],"<",rev[0])
    
        if nor[1]==rev[1]:
            print(nor[0],">",rev[0])
    
    else:
        if nor[0]==rev[1]:
            print(nor[1],">",rev[1])
    
        if nor[1]==rev[1]:
            print(nor[1],"<",rev[1])

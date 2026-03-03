n=list(str(input()).split())
f=[]
if int(n[0])==int(n[3]):
    f.append(int(n[0]))
    f.append(int(n[0]))
elif int(n[1])==int(n[2]):
    f.append(int(n[1]))
    f.append(int(n[1]))
else:
    if int(n[1])>int(n[2]) and int(n[0])<int(n[3]):
        if int(n[0])==int(n[2]):
            f.append(int(n[0]))
        else:
            if int(n[0])<int(n[2]):
                f.append(int(n[2]))
            if int(n[0])>int(n[2]):
                f.append(int(n[0]))
        if int(n[1])==int(n[3]):
            f.append(int(n[1]))
        else:
            if int(n[1])<int(n[3]):
                f.append(int(n[1]))
            if int(n[1])>int(n[3]):
                f.append(int(n[3]))
f=str(f)
final=f.replace(" ","")
print(final)
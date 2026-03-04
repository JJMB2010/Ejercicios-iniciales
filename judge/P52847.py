n=list(str(input()).split())
n.sort()
if float(n[1])<0 and float(n[0])<0 and float(n[2])<0:
    if float(n[0])>float(n[1]):
        if float(n[0])>float(n[2]):
            print(n[0])
        else:
            print(n[2])
    else:
        if float(n[1])>float(n[2]):
            print(n[1])
        else:
            print(n[2])
else:
    if float(n[1])>float(n[0]):
        if float(n[1])>float(n[2]):
            print(n[1])
        else:
            print(n[2])
    else:
        if float(n[0])>float(n[2]):
            print(n[0])
        else:
            print(n[2])
num=input()
rou=round(float(num),0)
if float(num)==0.0:
    a=0
    b=0
    c=0
else:
    if float(num)<1:
        a=0
        b=1
        if 0.5<=float(num):
            c=1
        else:
            c=0
    else:
        if "." in str(num):
            if float(num)>float(rou):
                b=float(num)+1
            else:
                b=float(num)+1
            if float(rou)+0.5<=float(num):
                c=rou+1
            else:
                c=rou
            if float(num)>float(rou):
                a=rou
            else:
                f=float(rou)-float(num)
                num=float(num)+f-1
                a=num
        else:
            b=num
            c=rou
            if float(num)>=float(rou):
                a=rou
            else:
                f=rou-num
                num=num+f-1
                a=num
print(int(a),int(b),int(c))
# 41. Imprime el siguiente patrón utilizando for:
p="54321"
pos=int(5)
for x in range(5):
    print(p)
    p=p.replace(str(pos),"")
    pos=pos-1


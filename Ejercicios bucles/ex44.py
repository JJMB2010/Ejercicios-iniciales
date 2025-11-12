# 44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’.

pi=0
for x in range(0,100):
    if pi < 99:
        print(pi, end=",")
        pi=pi+3

print(pi)
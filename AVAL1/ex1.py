print("== Media de 5 ==")
index = 0;
aux = 0;
while index < 5:
    aux = aux + float(input("Insira um numero: "))
    index = index + 1
aux = aux / 5
print("## A media dos numero é %.1f" % aux)
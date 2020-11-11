print("== Equação de Segundo Grau ==")

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

D = int (b**2) - (4*a*c)
if D < 0:
    print("delta é negativo")
else:
    x1 = (-b + D**1/2) / (2*a)
    x2 = (-b - D**1/2) / (2*a)
    print("# X1: ", x1)
    print("# X2: ", x2)
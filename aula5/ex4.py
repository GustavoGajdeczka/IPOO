print("== Bolsa de Valores ==")

i = float(input("= Insira a taxa mensal: "))
p = float(input("= Insira a aplicação mensal: "))
m = float(input("= Insira o numero de meses: "))

r = ((((1 + i)**m)-1) / i) * p

print("# %.2f" % r)
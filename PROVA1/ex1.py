print("== Questão 1 ==")
valor = float(input("= Insira o valor do Produto: "))
quant = int(input("= Insira a quantidade: "))

if quant < 5:
    valor = (valor - ((valor / 100) * 3)) * quant
elif quant < 10:
    valor = (valor - ((valor / 100) * 5)) * quant
else:
    valor = (valor - ((valor / 100) * 7)) * quant
print("== ", valor)


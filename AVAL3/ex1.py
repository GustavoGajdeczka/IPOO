print("== Exercicio 1 ==")

def somaImposto(custo, taxaImposto):
    resultado_imposto = custo + (custo * taxaImposto / 100)
    return resultado_imposto

x = float(input("= Insira o custo: "))
y = float(input("= Insira a taxa do imposto: "))

print("# ", somaImposto(x, y))
 
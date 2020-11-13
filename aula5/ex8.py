print("== Imposto ==")
valor = float(input("= Digite o custo de fabricaçao: R$"))
custo = (valor / 100) * 45 + valor
custo = (custo / 100) * 28 + custo
print("## O custo final para o cliente é de: R$", custo) 
print("== Circo ==")
custo = float(input("= Insira o custo do Espetáculo: "))
ingresso = float(input("= Insira o valor do ingresso: "))

despesa = int(custo / ingresso)
lucro = int((custo * 1.23) / ingresso)

print("## Para que o espetáculo seja pago, sera necessario vender %d ingressos" % despesa)
print("## Para se obter um lucro de 23 porcento, sera necessario vender %d ingressos" % lucro)
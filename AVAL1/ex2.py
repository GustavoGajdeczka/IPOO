print("== Juros 12x ==")
saldo = float(input("= Insira o seu Saldo: "))
juros = float(input("= Insira a taxa de juros em %: "))
index = 0
aux = saldo

while index < 12:
    saldo = saldo + ((saldo / 100) * juros)
    print("# Saldo no mes %d: %.2f" % (index, saldo))
    index = index + 1
aux = saldo - aux
print("## O total de lucro com os juros foi de: %.2f" % aux)
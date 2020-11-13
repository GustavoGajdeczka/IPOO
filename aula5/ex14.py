print("== Trivago ==")
quartos = int(input("= Insira o numero de quartos: "))
valor = float(input("= Insira o valor da diaria de cada quarto: "))

diaria = valor - (valor / 100) * 25
cemPorcento = (diaria * 2) * quartos
setentaPorcento = (diaria * 2) * (quartos / 100 * 70)
prejuizo = (valor * quartos) - cemPorcento

print("## Diaria: ", diaria)
print("## 100% : ", cemPorcento)
print("## 70% : ", setentaPorcento)
print("## Prejuizo em decorrencia do desconto: ", prejuizo)
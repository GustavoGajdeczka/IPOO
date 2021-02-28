import re
print("== Exercicio 2 ==")
print("== horario deve conter 4 digitos")
print("== para fechar o programa, insira um horario invalido (horas acima de 24 ou minutos acima de 60)")

index = 0
def convert(hora):
    hora = re.findall("\d{2}", hora)
    x = int(hora[0])
    if x > 24 or x < 0 or int(hora[1]) >= 60 or int(hora[1]) < 0:
        global index
        index = 2
        return "## Horario Invalido" 
    if x > 12:
        x = x - 12
        if (x < 10):
            x = "0" + str(x)
            return "# " + x + ":" + hora[1] + " pm"
        else:
            return "# " + str(x) + ":" + hora[1] + " pm"
    else:
        if (x < 10):
            x = "0" + str(x)
            return "# " + x + ":" + hora[1] + " am"
        else:
            return "# " + str(x) + ":" + hora[1] + " am"

while index == 0:
    print(convert(input("= Insira um horario a ser convertido: ")))


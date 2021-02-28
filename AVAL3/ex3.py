print("== Exercicio 3 ==")

def valorPagamento(valor, dia):
    if dia < 1:
        valor = valor
        print(valor)
        return valor
    else:
        valor = (valor + valor * 0.03 + 0.01 * dia)
        print(valor)
        return valor

parcelas = []
dias = -1
valortotal = 0
  
while True:
        dias += 1
        valor = float(input('= Qual o valor da prestacao? '))
        if valor == 0:
            break
        dia = int(input('= Quantos dias esta em atraso? '))
        parcelas.append(valorPagamento(valor, dia))
 
for index in range(dias):
    valortotal += parcelas[index]
 
print('## Relatorio do dia, foram pagas %d prestacoes' %dias)
print('## Valor total de prestacoes pagas: ', valortotal)
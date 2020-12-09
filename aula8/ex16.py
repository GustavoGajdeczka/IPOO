print("== Vetor 16 ==")

vetor = []
N = int(input("= Quantos numeros deseja digitar: "))
while N > 0:
    vetor.append(int(input("= Digite um numero: ")))
    N -= 1

fim = len(vetor)
while fim > 1:
    trocou = False
    index = 0
    while index < (len(vetor) - 1):
        if vetor[index] < vetor[index + 1]:
            aux = vetor[index]
            vetor[index] = vetor[index + 1]
            vetor[index + 1] = aux
            trocou = True
        index += 1
    if not trocou:
        break
    fim -= 1
for e in vetor:
    print(e) 
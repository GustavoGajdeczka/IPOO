print("== Vetor 15 ==")

L = [7,4,3,12,8]
fim = len(L)
while fim > 1:
    trocou = False
    index = 0
    while index < (len(L) - 1):
        if L[index] < L[index + 1]:
            aux = L[index]
            L[index] = L[index + 1]
            L[index + 1] = aux
            trocou = True
        index += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e) 
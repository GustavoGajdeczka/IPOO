print("== Vetor 7 ==")
vetor = []
index = 0
while index <= 4:
    vetor.append(float(input("= Insira um numero: ")))
    index += 1
index -= 1
while index >= 0:
    print("## ", vetor[index])
    index -= 1

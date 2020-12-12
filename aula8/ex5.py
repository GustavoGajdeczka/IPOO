print("== Vetor 5 ==")
media = 0
vetor = []
index = 0
while index <= 4:
    vetor.append(float(input("= Insira um numero: ")))
    index += 1
for index in vetor:
    media += index
media = media / 5
print("## ", media)


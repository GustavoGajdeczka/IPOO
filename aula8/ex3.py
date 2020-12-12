print("== Vetor 3 ==")
vetor = []
index = 0
while index <= 4:
    vetor.append(int(input("= Insira um numero: ")))
    index += 1
index = 0
for index in vetor:
    if index % 2:
        print("## ", index)
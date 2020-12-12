from random import randint
print("== Exercicio 3 ==")
A = []
index = input("= Deseja inserir 5 numeros? senao serão gerados numeros aleatorios (sim/nao): ")
if index == "sim" or index == "s" or index == "Sim":
    index = 0
    while index < 5:
        A.append(int(input("= Insira um numero: ")))
        index += 1
else:
    index = 0
    while index < 5:
        A.append(int(randint(0, 10)))
        index += 1

B = int(input("= Insira um numero para procurar: "))
index = 0
print(A)
for a in A:
    if a == B:
        print("## %d achado na posição %d" % (a, index))
        index = 0
        break
    index += 1 
if index != 0:
    print("## %d não encontrado" % B)
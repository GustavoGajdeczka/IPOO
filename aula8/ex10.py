from random import randint
print("== Vetor 10 ==")
A = []
index = 0
B = int(input("= Insira um numero para procurar: "))

while index <= 10:
    A.append(int(randint(0, 10)))
    index += 1
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
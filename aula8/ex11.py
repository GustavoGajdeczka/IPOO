from random import randint
print("== Vetor 11 ==")
A = []
index = 0
B = [int(input("= Insira um numero para procurar: "))]
C = [int(input("= Insira um numero para procurar: "))]

while index < 10:
    A.append(int(randint(0, 10)))
    index += 1
index = 0
print(A)
for a in A:
    if a == B[0]:
        B.append(index)
    if a == C[0]:
        C.append(index)
    index += 1 

if len(B) < 2:
    print("## %d não encontrado" % B[0])
else:
    print("## %d achado na posição %d" % (B[0], B[1]))

if len(C) < 2:
    print("## %d não encontrado" % C[0])
else:
    print("## %d achado na posição %d" % (C[0], C[1]))

if len(B) > 1 and len(C) > 1:
    if B[1] > C[1]:
        print("## %d encontrado antes" % C[0])
    else:
        print("## %d encontrado antes" % B[0])  
print("== Exercicio 4 ==")

index = range(5)
A = []
B = []
C = []

for n in index:
    A.append(int(input("= Insira um numero: ")))
    B.append(int(input("= Insira um numero: ")))

for a in A:
    C.append(a)
for a in B:
    C.append(a)

print("## Lista A: ", A)
print("## Lista B: ", B)
print("## Lista C: ", C)
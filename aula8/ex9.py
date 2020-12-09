print("== Vetor 9 ==")

index = 0
aux = 0
A = [1, 2, 4, 16, 64, 256, 512, 1024]
B = [2, 8, 32, 16, 128, 512, 2048]
C = []
aux = 0

for a in A:
    C.append(a)
for b in B:
    aux = 0
    for c in C:
        if c == b:
            aux = 1
    if aux == 0:
        C.append(b)
print(C)

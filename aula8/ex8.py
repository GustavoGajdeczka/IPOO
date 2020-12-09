print("== Vetor 8 ==")

index = 0
A = [1, 4, 16, 64, 256, 1024]
B = [2, 8, 32, 128, 512, 2048]
C = []

while index <= 5:
    C.append(A[index])
    C.append(B[index])
    index += 1
print("## ", C)
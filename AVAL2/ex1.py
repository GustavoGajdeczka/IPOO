print("== Exercicio 1 ==")
A=[10, 11, 12, 13, 14, 15, 16,17]
B=[1, 2, 3, 4, 5, 6, 7, 8]
C=[]
index = 0
while index < len(A):
    C.append(A[index] + B[index])
    index += 1
print("## ", C)
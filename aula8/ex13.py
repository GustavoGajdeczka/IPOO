from random import randint
print("== Vetor 13 ==")

A = []
index = 0
menor = 11

while index < 10:
    A.append(int(randint(0, 10)))
    index += 1

for a in A:
    if (menor > a):
        menor = a
print(A)
print("## Menor numero da lista é: %d" % menor)
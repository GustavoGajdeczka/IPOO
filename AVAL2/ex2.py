print("== Exercicio 2 ==")
menor = 999
maior = -999
media = 0

T = [ 10, 8, 0, 1, 2, 3, 2, 4]

for a in T:
    if (menor > a):
        menor = a
    if (maior < a):
        maior = a
    media += a
media = media / len(T)
print("## Maior Temperatura %d" % maior)
print("## Menor Temperatura %d" % menor)
print("## Temperatura Media %d" % media)
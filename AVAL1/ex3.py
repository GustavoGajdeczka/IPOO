print("== Idades ==")
index = 1
maior = 0
menor = 0
while index != 0:
    idade = int(input("= Insira a sua Idade: "))
    if idade > 60:
        maior += 1
    if idade < 18:
        menor += 1
    if idade == 0:
        index = 0

print("## %d Tem mais de 60 anos de idade" % maior)
print("## %d São menores de idade" % menor)



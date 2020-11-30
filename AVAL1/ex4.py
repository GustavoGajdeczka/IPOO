print("== Alturas ==")
chico = 1.50
juca = 1.1
index = 0
ano = 0
while index == 0:
    chico += 0.02
    juca += 0.03
    if juca > chico:
        index = 1
    ano += 1
print("## Serão necessarios %d anos para juca passar chico em altura" % ano)
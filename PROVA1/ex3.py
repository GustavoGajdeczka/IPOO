v = [ ]
valor = int ( input("Digite valor (0 para fim): "))
while (valor != 0):
     v.append(valor)
     valor = int ( input("Digite valor (0 para fim): ")) 

aux = len(v) - 1
index = 0
while index <= aux:
    if v[index] < 0:
        print ("Valores negativos nas posições: ", index)
    index += 1
print(v)
print("== Par ou Impar ==")
a = int(input("Insira um numero com 3 digitos: "))
a = a % 100
if a % 2:
    print("# Impar")
else:
    print("# Par")
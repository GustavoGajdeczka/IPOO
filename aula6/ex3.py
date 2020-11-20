print("== Adição ou Subtração ==")
a = int(input("= Digite um numero: "))
a = a + int(input("= Digite outro numero: "))
if a > 20:
    a = a + 8
else:
    a = a - 5

print("#", a)
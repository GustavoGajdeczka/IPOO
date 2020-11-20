print("== Calculadora ==")
a = int(input("= Digite um numero: "))
b = int(input("= Digite outro numero: "))
ope = int(input("= Insira qual operação deseja realizar: \n= 1 soma \n= 2 subtrai \n= 3 multiplica \n= 4 divide \n= Operação: "))
if ope == 1:
    a = a + b
if ope == 2:
    a = a - b
if ope == 3:
    a = a * b
if ope == 4:
    a = a / b
print("# ", a)


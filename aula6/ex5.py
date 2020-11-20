print("== Passagem ==")
a = float(input("= Digite quantos Kilometros deseja percorrer: "))
if a < 200:
    a = a * 0.5
else:
    a = a * 0.45
print("# A sua passagem custara R$%.2f" % a)

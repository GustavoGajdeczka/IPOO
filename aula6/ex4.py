import math
print("== Raiz Quadrada ==")
a = float(input("= Digite um numero: "))
if a > 0.0:
    print("# %4.2f" % math.sqrt(a)) 
else:
    print("# %.1f" % (a * a))
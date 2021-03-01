print("== Triangulo ==")
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2

x = float(input("= Informe a base do primeiro triangulo: "))
y = float(input("= Informe a altura do primeiro triangulo: "))
triangulo1 = Triangulo(x, y)
print("# ", triangulo1.area())
x = float(input("= Informe a base do segundo triangulo: "))
y = float(input("= Informe a altura do segundo triangulo: "))
triangulo2 = Triangulo(x, y)
print("# ", triangulo2.area())
if (triangulo1.area() == triangulo2.area()):
    print("## Os dois triangulos tem o mesmo tamanho")
else:
    if (triangulo1.area() > triangulo2.area()):
        print("## A area do primeiro triangulo é maior que a do segundo")
    else:
        print("## A area do segundo triangulo é maior que a do primeiro")


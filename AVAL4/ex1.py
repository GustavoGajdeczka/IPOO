print("== Circulo ==")
class circulo:
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return 3.1415 * (self.raio * self.raio)

index = float(input("# Informe o raio do circulo: "))
circ = circulo(index)
print(circ.area())

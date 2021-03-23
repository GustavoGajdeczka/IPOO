class ObjetoGrafico:
    _centro = None
    def __init__(self, centro):
	    self._centro = centro
    def desenha(self):
        print('Desenha objeto grafico')

class Circulo(ObjetoGrafico):
    _raio = None
    def __init__(self, centro, raio):
        super().__init__(centro)
        self._raio = raio
    def area(self):
        area = self._raio * self._raio
        area = area * 3.14
        return area
    def desenha(self):
        print('Desenha objeto grafico')

class Retangulo(ObjetoGrafico):
    _altura = None
    _largura = None
    def __init__(self, centro, altura, largura):
        super().__init__(centro)
        self._altura = altura
        self._largura = largura
    def area(self):
        return (self._altura * self._largura)
    def desenha(self):
        print('Desenha objeto grafico')

class Quadrado(Retangulo):
    def __init__(self, centro, largura):
        super().__init__(centro, largura, largura)

g1 = []
g1.append(Circulo(3, 3))
g1.append(Retangulo(4, 5, 6))
g1.append(Quadrado(3, 5))

for x in g1:
    print(x.area())
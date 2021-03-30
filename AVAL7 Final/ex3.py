""" Dada a classe TV abaixo, crie outra classe chamada smartTV que estende (herda de) a classe TV, 
com os atributos 'marca', 'polegadas', 'volume', 'OpSystem' (string), 'WiFi' (True ou False).
Os atributos 'OpSystem' (sistema operacional) e 'WiFi' devem ser fortemente privados.
O método construtor da classe smartTV deve receber todos os atributos como parâmetro.
Não é necessário alterar a definição da classe TV
Não é necessário definir outros métodos além do construtor

class TV:
    marca = None    # marca da TV (string)
    polegadas = None    # tamanho da TV em polegadas (inteiro)
    volume = None   # volume atual do som (inteiro)

    def __init__(self, m, p, v):
        self.marca = m
        self.polegadas = p
        self.volume = v

    def soundUp (self):
        self.volume += 1

    def soundDown (self):
        self.volume -= 1
"""
class TV:
    marca = None    # marca da TV (string)
    polegadas = None    # tamanho da TV em polegadas (inteiro)
    volume = None   # volume atual do som (inteiro)

    def __init__(self, m, p, v):
        self.marca = m
        self.polegadas = p
        self.volume = v

    def soundUp (self):
        self.volume += 1

    def soundDown (self):
        self.volume -= 1

class smartTV(TV):
    __Wifi = None
    __OpSystem = None
    def __init__(self, m, p, v, OpSystem, WiFi):
        super().__init__(m, p, v)
        self.__Wifi = WiFi
        self.__OpSystem = OpSystem

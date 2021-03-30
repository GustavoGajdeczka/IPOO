""" Altere a definição da classe TV abaixo, criando novos métodos, para alterar o canal da TV 
e ler o canal atual.
Não é necessário criar objetos da classe TV, apenas modificar a classe

class TV:
    marca = None    # marca da TV (string)
    polegadas = None    # tamanho da TV em polegadas (inteiro)
    volume = None   # volume atual do som (inteiro)
    __canal = None  # canal atual da TV (inteiro)

    def __init__(self, m, p, v=10, c=1):
        self.marca = m
        self.polegadas = p
        self.volume = v
        self.__canal = c

    def soundUp (self):
        self.volume += 1

    def soundDown (self):
        self.volume -= 1
"""

class TV:
    marca = None    # marca da TV (string)
    polegadas = None    # tamanho da TV em polegadas (inteiro)
    volume = None   # volume atual do som (inteiro)
    __canal = None  # canal atual da TV (inteiro)

    def __init__(self, m, p, v=10, c=1):
        self.marca = m
        self.polegadas = p
        self.volume = v
        self.__canal = c

    def soundUp (self):
        self.volume += 1

    def soundDown (self):
        self.volume -= 1

    def canal(self):
        return self.__canal

    def mudarCanal(self, canal):
        self.__canal = canal

       
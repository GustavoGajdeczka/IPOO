""" Dada a classe TV abaixo, crie um objeto da classe TV, de 50 polegadas de tamanho, 
da marca Xingling, aumente o volume duas vezes utilizando os métodos fornecidos 
pela classe TV, e mostre mensagem informando a marca da TV e qual o volume do som atual.
Não é necessário alterar a definição da classe TV.

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

tv = TV('Xingling', 50, 0)

tv.soundUp()
tv.soundUp()

print("Marca %s  \nVolume %s " % (tv.marca, tv.volume))


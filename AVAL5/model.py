class Imovel:
    _endereco = None
    def __init__(self, endereco, valor):
        self._endereco = None
        self._valor = None

    def getEndereco(self):
        return 0

class Apartamento(Imovel):
    __andar = None
    __taxaCondominio = None
    def __init__(self, endereco, valor, andar, taxaCondominio):
        super().__init__(andar, taxaCondominio)
        self.__andar = andar
        self.__taxaCondominio = taxaCondominio
        self._endereco = endereco
        self._valor = valor
    
    def valorMensal(self):
        return (self.__taxaCondominio + self._valor)
    def getAndar(self):
        return self._endereco, self.__andar, self.valorMensal()





class Aluno: 
    def __init__(self):
        self.nome = None
        self.endereco = None
        self.nota = []
        self.media = None
    
    def setNome(self, nome):
        self.nome = nome
    def setEndereco(self, endereco):
        self.endereco = endereco
    def setNota(self, nota):
        self.nota.append(nota)
    def Media(self):
        self.media = 0
        for x in self.nota:
            self.media += x
        self.media = self.media / len(self.nota)
        return self.media
    def ficha(self):
        print("#Nome =     ", self.nome)
        print("#Endereco = ", self.endereco)
        print("#Media      ", self.media)
    def dados(self):
        return self.nome, self.endereco, self.media
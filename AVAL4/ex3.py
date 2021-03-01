print("== Escola ==")
class Aluno:
    def __init__(self, nome, endereco):
        self.Nome = nome
        self.Endereco = endereco
        self.Nota = []
        self.Media = 0

    def setNota(self, nota):
        self.Nota.append(nota)
    def media(self):
        self.Media = 0
        for x in self.Nota:
            self.Media = self.Media + x
        self.Media = self.Media / 4
        return self.Media
    def imprimeDados(self):
        print("## Nome:     ", self.Nome)
        print("## Endereço: ", self.Endereco)
        print("## Media:    ", self.Media)

nome = input("= Insira o nome do aluno: ")
endereco = input("= Insira o endereço do aluno: ")
aluno = Aluno(nome, endereco)

opcao = '1'
while (opcao != '0'):
    print("=============================================")
    print("== Insira a operação que deseja realizar: ")
    print("== NOTA = Cadastrar notas ")
    print("== MEDIA = media do aluno ")
    print("== DADOS = ficha do aluno ")
    print("== 0 = finalizar")
    opcao = input()
    if (opcao == 'NOTA' or opcao == 'nota'):
        for x in range(4):
            print("= Insira a ", x+1,"° nota do aluno: ")
            aluno.setNota(int(input()))
    if (opcao == 'MEDIA' or opcao == 'media'):
        print(aluno.media())
    if (opcao == 'DADOS' or opcao == 'dados'):
        aluno.media()
        print(aluno.imprimeDados())
print("== Emprestimos ==")
a = float(input("= Insira o seu salario: "))
b = float(input("= Insira o valor da parcela: "))
if ((a / 100) * 30) < b:
    print("# Sem credito")
else:
    print("# Parabens, seu emprestimo foi aprovado")
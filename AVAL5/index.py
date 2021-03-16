from model import Apartamento
import json
print("== Imobiliaria Gajdeczka ==")
quantidade = int(input("== Quantos apartamentos deseja cadastrar: "))
apartamentos = []
for x in range(quantidade):
    print(f"= Apartamento {x+1} ")
    ap = Apartamento(
        input("= Endereço do imóvel: "),
        float(input("= Valor do aluguel:")),
        int(input("= Andar do apartamento: ")),
        float(input("= Taxa de condomínio: "))
    )
    x1, x2, x3 = ap.getAndar()
    if int(x2) > 1 and float(x3) < 1000:
        x = {"endereco": x1, 
             "andar": x2, 
             "valor mensal": x3}
        apartamentos.append(x)

    
print(json.dumps(apartamentos, indent=4))




print("== Eleições ==")
eleitores = int(input("= Insira o numero de eleitores: "))
candidato1 = int(input("= Insira o numero de votos do primeiro candidato: "))
candidato2 = int(input("= Insira o numero de votos do segundos candidato: "))
nulo = eleitores - (candidato1 + candidato2)
if candidato1 > eleitores or candidato2 > eleitores:
    print("## Eleições corruptas, favor refazelas")
else:
    candidato1 = float((candidato1 * 100) / eleitores)
    candidato2 = float((candidato2 * 100) / eleitores)
    nulo = float((nulo * 100) / eleitores)
    if (candidato1 + candidato2) > 100:
        print("## Eleições corruptas, favor refazelas")
    else:
        print("## o candidato 1 tem %.2f porcento de votos" % candidato1)
        print("## o candidato 2 tem %.2f porcento de votos" % candidato2)
        print("## Nulos são %.1f porcento dos votos" % nulo)
        if nulo < 50:
            if candidato1 == candidato2:
                print("!! Empate")
            else:
                if candidato1 > candidato2:
                    print("!! Candidato 1 é o ganhador")
                else:
                    print("!! Candidato 2 é o ganhador")
        else:
            print("!! Nulos são a maioria, então devera ser feita nova eleição")
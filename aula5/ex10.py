print("== Relogio ==")
segundos = int(input("= Informe os segundos: "))
horas = segundos / 3600
hora = segundos % 3600
minutos = int(hora / 60)
segundos = int(hora % 60)

print("%d Horas, %d Minutos, %d Segundos" % (horas, minutos, segundos))
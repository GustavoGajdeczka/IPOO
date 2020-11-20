print("== Divisivel ==")
a = int(input("= Insira um numero: "))
if a % 3:
    if a % 7:
        print("# %d é indivisivel por 3 e por 7" % a)
    else:
        print("# %d é indivisivel por 3 e divisivel por 7" % a)
else:
    if a % 7:
        print("# %d é divisivel por 3 e indivisivel por 7" % a)
    else:
        print("# %d é divisivel por 3 e por 7" % a)
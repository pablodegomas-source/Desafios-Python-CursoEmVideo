from time import sleep
ano = int(input("Digite o Ano: "))
calculo1 = ano % 4
calculo2 = ano % 100
calculo3 = ano % 400
print("PENSANDO")
sleep(3)

if (calculo1 == 0 and calculo2 != 0) or calculo3 == 0:
    print("Ano bissexto")

else:
    print("Ano nao e bissexto")


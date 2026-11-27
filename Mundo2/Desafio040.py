from time import sleep
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segundar nota: "))
calculo1 = nota1 + nota2
calculo2 = calculo1 / 2
print("POR FAVOR AGUARDE UM POUCO")
sleep(5)

if calculo2 >= 7:
    print("Parabens Aprovado")
elif calculo2 >= 5:
    print("Voce ta de recuperacao")
elif calculo2 < 5:
    print("Voce ta reprovado")
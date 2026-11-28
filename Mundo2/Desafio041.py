from datetime import date
from time import sleep
ano = int(input("Digite seu ano de nacimento: "))
idade = date.today().year - ano
print("OLHANDO SEU RANKING NA CATEGORIA DE NATACAO")
sleep(3)

if idade <= 9:
    print("Seu ranking e MIRIM")
elif idade <= 14:
    print("Seu ranking e INFANTIL")
elif idade <= 19:
    print("Seu ranking e JUNIOR")
elif idade <= 20:
    print("Seu ranking e SENIOR")
else:
    print("Seu ranking e MASTER")

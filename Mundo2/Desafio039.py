from datetime import date
from time import sleep
ano = int(input("Digite Seu ano de nacimento: "))
idade = date.today().year - ano
print("OLHANNDO SE VOCE JA ESTAR NA HORA DE SE ALISTAR")
sleep(5)

if idade == 18:
    print("Ja estar na hora de se alistar")
elif idade < 18:
    falta = 18 - idade
    print(f"Voce ainda vai se alistar faltar {falta} anos")
elif idade > 18:
    passou = idade - 18
    print(f"Voce ja passou do tempo de se alistar ja passou {passou} anos")
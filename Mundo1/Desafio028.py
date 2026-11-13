import random
numero_certo = random.randint(0,5)
numero_escolhido = int(input("Tente adivinhar um numero aleatorio de 0 a 5:  "))

if numero_certo == numero_escolhido:
    print(f"Voce acertou")

else:
    print(f"Voce errou o numero certo era: {numero_certo}")
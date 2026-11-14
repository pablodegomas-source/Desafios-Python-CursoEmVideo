velocidade_carro = int(input("Velocidade do carro em KM foi: "))
calculo = velocidade_carro - 80
multa = calculo * 7

if velocidade_carro > 80:
    print(f" Voce foi multado por passar de 80KM a multa e de {multa}R$")
else:
    print("Velocidade correta")
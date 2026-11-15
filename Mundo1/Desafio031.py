viagem_km = int(input("Digite a Distancia em KM da Viagem: "))

if viagem_km <= 200:
    print(f"O preco a se pagar da sua viagem e {viagem_km * 0.50:.2f}")
else:
    print(f"O preco a se pagar da sua viagem e {viagem_km * 0.45:.2f}")

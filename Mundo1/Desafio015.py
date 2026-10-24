dias = float(input("Quantos dias o carro foi usado: "))
km = float(input("Quantos km ele andou: "))
valor_dia = dias * 60
valor_km = km * 0.15
valor_total = valor_dia + valor_km
print(f"O preco total que você deve pagar e: {valor_total:.2f}")
from time import sleep
salario = float(input("Digite Seu Salario R$: "))
aumento1 = 0.15 * salario
aumento2 = 0.10 * salario
salario_novo1 = aumento1 + salario
salario_novo2 = aumento2 + salario
print("PENSANDO")
sleep(3)

if salario > 1250:
    print(f"Seu novo salario e R$: {salario_novo2:.2f}")
elif salario <= 1250:
    print(f"Seu novo salario e R$: {salario_novo1:.2f}")
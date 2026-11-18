from time import sleep
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
print("PENSANDO")
sleep(3)

if numero1 >= numero2 and numero1 >= numero3:
    print(f"O numero {numero1} e maior")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"O numero {numero2} e maior")
elif numero3 >= numero1 and numero3 >= numero2:
    print(f"O numero {numero3} e maior")


if numero1 <= numero2 and numero1 <= numero3:
    print(f"O numero {numero1} e menor")
elif numero2 <= numero1 and numero2 <= numero3:
    print(f"O numero {numero2} e menor")
elif numero3 <= numero2 and numero3 <= numero1:
    print(f"O numero {numero3} e menor")

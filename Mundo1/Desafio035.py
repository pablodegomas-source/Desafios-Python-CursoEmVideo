from time import sleep
palito1 = int(input("Digite a primeira linha: "))
palito2 = int(input("Digite a segunda linha: "))
palito3 = int(input("Digite a terceira linha: "))
somar1 = palito1 + palito2
somar2 = palito2 + palito3
somar3 = palito3 + palito1
print("CALCULANDO SE E UM TRIANGULO")
sleep(5)


if somar1 > palito3 and somar2 > palito1 and somar3 > palito2 :
    print("Os palitos criam um triangulo")
else:
    print("Os palitos nao criam um triangulo")
import math
n1 = float(input("Digite um cantinho: "))
n2 = float(input("Digite outro cantinho: "))
resultado1 = n1 * n1
resultado2 = n2 * n2
soma1 = resultado1 + resultado2
raiz_quadrada = math.sqrt(soma1)
print(f"O lado do triangulo maior e: {raiz_quadrada:.2f}")

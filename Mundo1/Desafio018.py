import math

angulo = float(input("Digite um numero: "))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print(f"o seno e {seno:.2f} o cosseno e {cosseno:.2f} o tangente e {tangente:.2f}")

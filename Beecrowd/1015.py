import math

x1, y1 = map(float, input("").split())
x2, y2 = map(float, input("").split())
distancia_de_pontos = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print(f"{distancia_de_pontos:.4f}")
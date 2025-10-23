# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:
import math

x1, y1 = map(float, input("").split())
x2, y2 = map(float, input("").split())
distancia_de_pontos = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print(f"{distancia_de_pontos:.4f}")
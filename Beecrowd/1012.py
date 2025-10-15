a, b, c = map(float, input("").split())
#a) a área do triângulo retângulo que tem A por base e C por altura.
triangulo = (a*c)/2
#b) a área do círculo de raio C. (pi = 3.14159)
pi = 3.14159
circulo = (c*c)*pi
#c) a área do trapézio que tem A e B por bases e C por altura.
trapezio = ((a+b)*c)/2
#d) a área do quadrado que tem lado B.
quadrado = b*b
#e) a área do retângulo que tem lados A e B.
retangulo = a*b

print(f"TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}")
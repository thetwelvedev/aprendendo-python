#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
C = float(input('Digite a temperaatura em Celcius: '))
F = (C * 1.8) + 32
print(f'A temperatura é {C:.1f}°C e em fahrenheit é {F:.1f}°F')
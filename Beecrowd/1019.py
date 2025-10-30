"""Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos."""
N = int(input())
horas = N // 3600
N = N % 3600
minutos = N // 60
segundos = N % 60
print(f"{horas}:{minutos}:{segundos}")

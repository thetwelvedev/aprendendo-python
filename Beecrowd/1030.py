"""O problema de Josephus é assim conhecido por causa da lenda de Flavius Josephus, um historiador judeu que viveu no século 1. Segundo o relato de Josephus do cerco de Yodfat, ele e seus companheiros (40 soldados) foram presos em uma caverna, cuja saída foi bloqueada pelos romanos. Eles preferiram suicidar-se a serem capturados, e decidiram que iriam formar um círculo e começar a matar-se pulando de três em três. Josephus afirma que, por sorte ou talvez pela mão de Deus, ele permaneceu por último e preferiu entregar-se aos romanos a suicidar-se."""
def josephus(ls, skip):
    global casos
    from collections import deque
    d = deque(ls)
    while len(d)>1:
        d.rotate(-skip)
        d.pop()
    print(f'Case {casos}:' , d.pop())
    casos += 1

n = int(input())
casos = 1
for a in range(1, n+1):
    x, y = input().split()
    x = int(x)
    y = int(y)
    lista = []

    for c in range(1, x+1):
        lista.append(c)

    josephus(lista, y)
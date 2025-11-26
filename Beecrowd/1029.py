"""Quase todo estudante de Ciência da Computação recebe em algum momento no início de seu curso de graduação algum problema envolvendo a sequência de Fibonacci. Tal sequência tem como os dois primeiros valores 0 (zero) e 1 (um) e cada próximo valor será sempre a soma dos dois valores imediatamente anteriores. Por definição, podemos apresentar a seguinte fórmula para encontrar qualquer número da sequência de Fibonacci:
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2);

Uma das formas de encontrar o número de Fibonacci é através de chamadas recursivas. Isto é ilustrado a seguir, apresentando a árvore de derivação ao calcularmos o valor fib(4), ou seja o 5º valor desta sequência:
Desta forma,
- fib(4) = 1+0+1+1+0 = 3
- Foram feitas 8 calls, ou seja, 8 chamadas recursivas."""
fibonacci = []

for b in range(0, 61):
    if b == 0:
        fibonacci.append(0)
    elif b == 1:
        fibonacci.append(1)
    else:
        num = fibonacci[b-1] + fibonacci[b-2]
        fibonacci.append(num)

testes = int(input())

for c in range(0, testes):
    n = int(input())
    calls = (2 * fibonacci[n+1] - 1) - 1
    print(f"fib({n}) = {calls} calls = {fibonacci[n]}")
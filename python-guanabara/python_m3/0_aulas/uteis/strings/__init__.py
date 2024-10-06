def criptogarfiaDeCesar(letras):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',' P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabetoDeCesar = {'X' : 0, 'Y' : 1,'Z' : 2, 'A': 3,'Á': 3, 'À': 3,'Ã':3, 'Â': 3, 'B': 4,'C': 5,'D': 6,'E' : 7,'É': 7, 'Ê': 7,'F' : 8,'G' : 9,'H' : 10,'I' : 11,'Í': 11,'J' : 12,'K' : 13,'L' : 14 ,'M' : 15 ,'N' : 16,'O' : 17,'Ó': 17, 'Õ': 17, 'Ô':17,'P' : 18,'Q' : 19, 'R' : 20 , 'S' : 21, 'T' : 22, 'U' : 23,'Ú': 23, 'V' : 24,'W' : 25 ,
    ' ': 26,'a': 30,'á': 30, 'à': 30, 'ã': 30,'â': 30,'b': 31, 'c': 32, 'd': 33, 'e': 34, 'é': 34, 'ê': 34, 'f': 35, 'g': 36, 'h': 37, 'i': 38,'í': 38,'j': 39, 'k': 40, 'l': 41, 'm': 42, 'n': 43, 'o': 44,'ó': 44, 'õ': 44, 'ô':44, 'p': 45, 'q': 46, 'r': 47, 's': 48, 't': 49, 'u': 50,'ú': 50, 'v': 51, 'w': 52,' x': 27, 'y': 28, 'z': 29}
    letras = list(letras)
    #Criptografando
    for i in range(0, len(letras)):
        pos = alfabetoDeCesar[letras[i]] #Através da letra(chave) ele encontra o número(value) que tem seu valor uma posição na lista alfabeto
        #Vou printar agora a palvra criptografada
        print(f'{alfabeto[pos]}', end='')
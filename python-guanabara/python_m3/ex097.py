#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

def escreva(frase):
    print('~'*len(frase))
    print(f'{frase:^}')
    print('~'*len(frase))

escreva('Aula de Python')

#Versão do Guanabas
def escreva2(frase):
    tam = len(frase) + 4
    print('~'*tam) # Esse + 4 é pata ter a borda tanto para frente quanto para trás, no caso fica duas para cada lado
    print(f'  {frase}')
    print('~'*tam) 

escreva2('Aula de Python')
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno1 = str(input('Digite um seu nome: '))
aluno2 = str(input('Digite um seu nome: '))
aluno3 = str(input('Digite um seu nome: '))
aluno4 = str(input('Digite um seu nome: '))
listaDeAlunos = [aluno1, aluno2, aluno3, aluno4]

alunoSorteado = choice(listaDeAlunos) #Escolhe um elemento da lista

print(f'O professor escolheu o aluno {alunoSorteado}')
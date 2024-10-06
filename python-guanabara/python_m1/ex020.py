#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
aluno1 = str(input('Digite um seu nome: '))
aluno2 = str(input('Digite um seu nome: '))
aluno3 = str(input('Digite um seu nome: '))
aluno4 = str(input('Digite um seu nome: '))
listaDeAlunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(listaDeAlunos) #Embaralha a lista

print(f'O professor escolheu a seguinte ordem os alunos {listaDeAlunos}')
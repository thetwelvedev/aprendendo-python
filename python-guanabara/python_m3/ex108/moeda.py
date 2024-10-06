#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
def aumentar(num, taxa):
    numAumentado = num + (num*(taxa/100))
    return numAumentado

def diminuir(num, taxa):
    numDiminuido = num - (num*(taxa/100))
    return numDiminuido

def dobro(num):
    return num*2

def metade(num):
    return num/2

def moeda(valor): #formatar a moeda
    valorInteiro = int(valor) #vai pegar só a parte inteira
    restoFlutuante = valor - valorInteiro #Só o valor float
    duasCasasDecimias = restoFlutuante *100 # vai transformar num valor inteiro
    if restoFlutuante == 0: #quando não tiver resto
        return f'R${valorInteiro},00'
    else:
        return f'R${valorInteiro},{duasCasasDecimias:.0f}' # usei o .:0f para ficar só a parte inteira

def moeda2(preço=0,moeda='R$'): #versão guanabara
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
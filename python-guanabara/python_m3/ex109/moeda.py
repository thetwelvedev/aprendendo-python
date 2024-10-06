#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
def aumentar(num, taxa, formato=False):
    numAumentado = num + (num*(taxa/100))
    return numAumentado if formato is False else moeda(num)
    #o parâmetro formato serve para já passar pela função moeda e assim vai usar apenas as outras funções
    #no caso ela faz a mudança do . para , ainda aqui no módulo 
    #Uso do parâmetro opcional
def diminuir(num, taxa, formato=False):
    numDiminuido = num - (num*(taxa/100))
    return numDiminuido if formato is False else moeda(num)

def dobro(num, formato=False):
    return num*2 if not formato else moeda(num*2)

def metade(num, formato=False):
    return num/2 if not formato else moeda(num/2)

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
def aumentar(num, taxa, formato=False):
    numAumentado = num + (num*(taxa/100))
    return numAumentado if formato is False else moeda(num)

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

def resumo(preço, taxa): # printa todos os dados pedidos, usando as outras funções
    print('<>'*20)
    print('RESUMO DO VALOR'.center(40))
    print('<>'*20)
    print(f'Preço analisado: \t{moeda2(preço)}') #\t é de tabulação
    print(f'A metade de {moeda(preço)} é {metade(preço,True)}')
    print(f'A dobro de {moeda(preço)} é {dobro(preço,True)}')
    print(f'Com o aumento de {taxa}% fica {aumentar(preço, taxa,True)}')
    print(f'Com a diminuição de {taxa}% fica {diminuir(preço, taxa,True)}')
    print('<>'*20)
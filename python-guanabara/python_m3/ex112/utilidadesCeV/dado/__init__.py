#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
def leiaDinheiro(msg):
    condição = False #Vai servir para condição de parada
    while not condição:
        scan = str(input(msg)).strip().replace(',', '.') #Eu pensei no replace mas tratanto depois, mas ficou melhor tratanto logo aqui
        if scan.isalpha() or scan == '': #verifica se é letra e retorna True or False/ E quando tiver fazio o scan
            print(f'\033[0;31mERRO: "{scan}" é um preço inválido!\033[m')
        else:
            condição = True
            return float(scan)
#Eu pensei semelhante porem ia fazer ao contrário, analisar se era número e se não fosse ia printar o erro,e não tava
# lembrando dessa condição de parada com while not, normalmente uso o while True e break
def leiaInt(msg):
    valorInt = 0
    while True: #Foi pedido que continuasse o código até receber um valor inteiro
        scan = str(input(msg)) #Vai ler a mensagem, que nem o scanf em C/o input pode apararecer abaixo da mensagem de print
        if scan.isnumeric(): #Vai verificar se na string tem número
            valorInt = int(scan) #Transformando string em inteiro
            break #fecha o loop quando tiver um valor inteiro
        else:
            print('\033[0;31mERRO! Não é um do tipo inteiro\033[m') #onde pego as cores: https://www.dio.me/articles/colocando-cores-no-seu-programa-em-python
    return valorInt
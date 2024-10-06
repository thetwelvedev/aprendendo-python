#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possiblidade da digitação de um tipo inválido. Aproveita  e crie também uma função leiaFloat() com a mesma funcionalidade.
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
    while True:
        try:
            scan = int(input(msg)) #Vai ler a mensagem, que nem o scanf em C/o input pode apararecer abaixo da mensagem de print
        except ValueError:
            print('Recebemos apenas número em algarismo indo-arábicos')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados')
            break
        except Exception as erro:
            print(f'O problema encontrado foi {erro.__cause__}')
            continue
        else:  #Se der certo retorna o valor
            return scan

def leiaFloat(msg):
    while True:
        try:
            scan = float(input(msg)) #Vai ler a mensagem, que nem o scanf em C/o input pode apararecer abaixo da mensagem de print
        except ValueError:
            print('Recebemos apenas número em algarismo indo-arábicos')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados')
            break
        except Exception as erro:
            print(f'O problema encontrado foi {erro.__cause__}')
            continue
        else:  #Se der certo retorna o valor
            return f'{scan:.2f}'
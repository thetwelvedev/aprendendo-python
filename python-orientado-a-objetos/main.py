from associacao import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor("Leonardo")
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca)
maquina.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
# from pessoa import Pessoa

# p1 = Pessoa('Luiz', 20)
# p2 = Pessoa('Pedro', 21)

# p1.comer("maça")
# p1.parar_comer()
# p1.parar_comer()
# p1.comer("maça")
# print("-" * 25)
# p1.parar_comer()
# p1.falar('POO')
# p1.comer('alimento')
# p1.parar_comer()
# p1.falar('assunto')
# print("-" * 25)
# p1.falar('POO')
# p2.comer('sorvete')
# p1.comer('churrasco')
# print("-" * 25)
# print(p1.ano_atual)
# print(p2.ano_atual)
# print(Pessoa.ano_atual)
# print(p1.get_ano_nascimento())
# print(p2.get_ano_nascimento())
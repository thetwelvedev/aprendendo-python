#Prática da aula 16

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#for comida in lanche:
#    print(comida)
#for pos, comida in enumerate(lanche):
#    print(f'A comida {comida} está na posição {pos}')
#for count in range(0, len(lanche)):
#    print(f'A comida {lanche[count]} está na posição {count}')

#print(sorted(lanche)) #Vai criar uma lista em ordem
#print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
# Nas tuplas a soma a ordem interfere
c = a + b # vai juntar as duas, vai formar uma nova tupla uma colda na outra
print(c)
print(c.count(5)) # Vai mostrar quantas vezes o 5 aparece na tupla
print(c.index(8)) # Vai mostrar a posição de 8(o primeiro que aparece)
print(c.index(5, 1)) # Vai começar da posição 1
del(c) # Você pode apagar uma tupla inteira mas não pode apagar só um elemento
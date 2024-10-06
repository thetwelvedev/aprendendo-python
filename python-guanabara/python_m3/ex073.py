#  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Cuiabá.
tabelaBrasileirão = ('Botafogo','Bragantino','Flamengo','Palmeiras','Athletico-PR','Grêmio','Atlético-MG','Fortaleza','Fluminense','São Paulo','Cuiabá','Internacional','Bahia','Cruzeiro','Corinthians','Goiás','Vasco','Santos','Coritiba','América-MG')
print(f'Os 5 primeiros times: {tabelaBrasileirão[0:5]}')
print(f'Os 4 últimos times: {tabelaBrasileirão[-4:]}') #Vai do comecar do quarto vindo de trás para frente
print(f'Os times em ordem alfabética: {sorted(tabelaBrasileirão)}') # Vai colocar em ordem alfabética
print(f"O time do Cuiabá é o {tabelaBrasileirão.index('Cuiabá') + 1}") # O index mostra a posição do elemento na tupla e o +1 é por conta que a lista do brasileirão começa do1 e não do 0
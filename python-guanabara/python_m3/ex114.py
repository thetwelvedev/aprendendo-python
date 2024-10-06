#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:#Caso o site esteja fora do ar ou o pc sem conexão com a internet
    print('O sitedo pudim não está acessível')
else:
    print('O site do pudim está acessível')
    #extra
    print(site.read()) #vai dar o conteúdo html
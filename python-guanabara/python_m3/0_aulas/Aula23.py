#Tratamento de Erros  e Excessões
'''
-Erro de sintaxe é o mais comum
-Erro de significado(semântico) ->exceção(Exception) NameError, ValueError, ZeroDivisionError, TypeError, IndexError, KeyError, ModuloNotFoundError
EOFError, KeyboardInterrupt, OSError, MemoryError, ConnectionError, RuntimeError...
'''
'''Exceção -> NameError
print(x)
-Pois x não foi definido'''
'''Exceção -> ValueError
n = int(input('Digite um número: '))
print(n) 
>>oito
-Pois oite é uma string e não um número como valor'''
'''Exceção -> ZeroDivisionError
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a/b
print(r)
>>8
>>0
-Na matemática não pode ter denominador igual a 0'''

#try and except
'''
try:
    operação
except:
    falhou
else: #Opcional
    deu certo
finally: #Opcional mas se colocado acontece independente do resultado
    certo/falha
'''
# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except: #Pode ter vários erros e fazer um except específico com except ValueError: ou except (ValueError, ZeroDivisionError): se for mais de um
#     print('Infelizmente tivemos um problema :(')
# else: #Opcional
#     print(f'O reultado é {r:.2f}')
# finally: #Opcional mas se colocado acontece independente do resultado
#     print('Volte sempre! Muito obrigado')

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'O probelma encontrado foi {erro.__class__}')
# else: #Opcional
#     print(f'O reultado é {r:.2f}')
# finally: #Opcional mas se colocado acontece independente do resultado
#     print('Volte sempre! Muito obrigado')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except ValueError:
    print('Recebemos apenas número em algarismo indo-arábicos')
except ZeroDivisionError:
    print('O denominador não pode ser 0')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')
else: #Opcional
    print(f'O reultado é {r:.2f}')
finally: #Opcional mas se colocado acontece independente do resultado
    print('Volte sempre! Muito obrigado')
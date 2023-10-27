'''
Introdução ao try/except
try-> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

'''
print(123)
print(456)
int('a') #ValueError de int 
'''
'''
numero = input('vou dobrar o número que vc digitar: ')


resultado = int(numero) * 2

print(f'O dobro de {numero} é {resultado}')'''

numero = input('vou dobrar o número que vc digitar: ')

try:

    print('STR', numero) #para aqui e pula para o except

    resultado = int(numero) * 2

    print(f'O dobro de {numero} é {resultado}')

except:
    print('Isso não é um número')
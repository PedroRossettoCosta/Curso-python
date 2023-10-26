'''
Operador lógico "not"
usado para inverter expressões
not True == False
not False == True
'''

senha = input('Senha: ')

if senha != '123':
    print('senha incorreta!')

elif not senha:
    print('vc não escreveu nada')
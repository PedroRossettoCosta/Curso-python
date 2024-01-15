'''Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número
é par ou impar. Caso o usuário não digite um numero inteiro, informe que não é um número inteiro'''

#entrada = input("Digite um numero: ")

#if entrada.isdigit():
#    entrada_int = int(entrada)
#    par_impar = entrada_int % 2 == 0
#    parImparText0 = 'impar'

#    if par_impar:
#        parImparText0 = 'par'
#    print(f'o numero {entrada} é {parImparText0}')    
#else:
#    print("voce não digitou um numero inteiro")

'''
Faça um programa que pergunte a hora ao usúario e, baseando-se no horário descrito, exiba a saudação
apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17, e Boa noite 18-23.
'''

horario = input('Que horas são para voce? ')
horario = int(horario)


    
if 0 <= horario and horario <= 11:
        print("Bom dia")
elif 12 <= horario and horario <= 17:
        print("Boa Tarde")
elif 18 <= horario and horario <=  23:
    print("Boa noite")

else:
    print("isso não é uma hora")
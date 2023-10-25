prim_valor = input('Digite um valor: ')
seg_valor = input('Digite um outro valor: ')

valor1 = int(prim_valor)
valor2 = int(seg_valor)

if valor1 > valor2:
    print(f'o primeiro valor {valor1} é maior do q o segundo valor {valor2}')
elif valor2 > valor1:
    print(f'o segundo valor {valor2} é maior do q o primeiro valor {valor1}')
else:
    print('Os valores são iguais')
    
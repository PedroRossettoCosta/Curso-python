nome = 'Pedro Henrique Rosseto Costa'

altura = 1.82
alturax = altura * altura
peso = 93
imc = peso / alturax

#f-strings
linha1 = f'{nome} tem {altura:.2f} de altura com um imc de {imc}'

print(linha1)

altura2 = 1.80
altura2x = altura2 * altura2
peso2 = 95
imc2 = peso2 / altura2x
print(imc2)

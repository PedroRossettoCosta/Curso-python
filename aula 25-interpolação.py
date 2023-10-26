nome = 'Luiz'
preco = 1000.958997643
variavel = '%s, o preço é R$%f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (15,15))

#x ou X - Hexadecimal
#(Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - + ou -
#Ex. : 0 > -100, .1f
#COnversion flags - !r !s !a

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.958997643:,.1f}')
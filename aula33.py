"""
imutaveis: string, integer, float, bool
zfill(__width) = length of the whole output
"""

qtdColunas = 5
qtdLinhas = 5

linha= 1

while linha <= qtdLinhas:
    coluna = 1
    

    while coluna <= qtdColunas:
        print(f'{linha=},{coluna=}')
        coluna += 1
    linha += 1
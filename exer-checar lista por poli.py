palavras = ["arara", "python", "radar", "ciência", "rotor"]

def poli(palavra):
    palavra = palavra.lower()
    palavra = palavra.replace(" ", "")

    palavra2 = palavra[::-1]

    if palavra == palavra2:
        return True
    else:
        return False

def checarLista(palavras):
    x = []
    for i in range (len(palavras)):
        poli(palavras[i])
        
        if poli(palavras[i]) == True:
            x.append(i)
    print(x)



checarLista(palavras)






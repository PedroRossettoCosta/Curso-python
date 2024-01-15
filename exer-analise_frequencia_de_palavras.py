texto = "Oi bom dia tudo bem oi"

def contar_palavras(texto):
    palavras = {}
    texto = texto.lower()
    texto = texto.split(" ")
    

    for i in range(len(texto)):
        if texto[i] in palavras:
            palavras[texto[i]] += 1
        else:
            palavras[texto[i]] = 1

    print(palavras)

contar_palavras(texto)
        
        

    


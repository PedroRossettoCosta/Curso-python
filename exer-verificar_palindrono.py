banana = "Amor a Roma"

def poli(palavra):
    palavra = palavra.lower()
    palavra = palavra.replace(" ", "")

    palavra2 = palavra[::-1]

    if palavra == palavra2:
        print("isso é um poli")
    else:
        print("isso não é um poli")

poli(banana)


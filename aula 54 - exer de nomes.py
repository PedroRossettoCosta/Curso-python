nome = input("Qual é o seu nome? ")


if len(nome) <= 4:
    print("seu nome eh curto")
elif 6 <= len(nome) <= 5:
    print("seu nome eh normal")
elif len(nome) < 6:
    print("seu nome é muito grande")
else:
    print("digite pelo menos uma letra!")

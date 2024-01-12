# () para parametros de função, [] para listas, pegar indices e tals, {} para dicionarios, para 
# definir tupla bote (())

vendas = [
    {"produto": "Camiseta", "quantidade": 15, "preco": 50},
    {"produto": "Calça Jeans", "quantidade": 20, "preco": 80},
    {"produto": "Sapatos", "quantidade": 5, "preco": 120},
    {"produto": "Casacos", "quantidade": 10, "preco": 150}
]

x = []
z = []
TotalVendas = 0
for item in vendas:
    quantidade = item["quantidade"]
    preco = item["preco"]
    
    x.append((item["quantidade"], item["produto"]))

    maxQuantidade = (max(x))

    valorAtual = item["quantidade"] * item["preco"]
    z.append((valorAtual, item["produto"]))



    TotalVendas += valorAtual

print(max(z))
print(TotalVendas)



#print(x)
#print(maxQuantidade)

    
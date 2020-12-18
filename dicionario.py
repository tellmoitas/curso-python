print("DICIONÁRIO")

#CRIAR
dicionario = {"jan":1, "fev":2, "mar":3}

#LER DICIONARIO
print(dicionario)

#ACESSAR VALOR DE UMA CHAVE
print(dicionario["jan"])

#ATUALIZAR
dicionario.update({"abr":4})
dicionario["maio"] = 5

print(dicionario)

#PERCORRER CHAVES
for i in dicionario:
    print(i)

#PERCORRER VALORES
for i in dicionario:
    print(dicionario[i])

#CELETAR
dicionario.pop("jan")
dicionario.pop("abr")
print(dicionario)




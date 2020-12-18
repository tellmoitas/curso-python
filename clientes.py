class Cliente:
    def __init__(self, nome, telefone):
        
        self.nome = nome
        self.idade = telefone
    
    def getNome(self):
        return self.nome

    def getTelefone(self):
        return self.idade

clientes = []

c1 = Cliente("Pedro", 999998888)
c2 = Cliente("Maria", 888887777)
c3 = Cliente("José", 666665555)

clientes.append(c1)
clientes.append(c2)
clientes.append(c3)

for cliente in clientes:
    print(cliente.getNome() + ": " + str(cliente.getTelefone()))

class Endereco:
    def __init__(self,rua,cidade):
        self.rua = rua
        self.cidade = cidade




class Cliente:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_cadastro(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nRua: {self.endereco.rua}\nCidade: {self.endereco.cidade}')



eu = Cliente('felipe',18,Endereco('Rua grã bretanha 472','São Bernardo do Campo'))
eu.mostrar_cadastro()

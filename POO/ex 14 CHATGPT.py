class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Trabalhador(Pessoa):
    def __init__(self, nome):
        print('Iniciando Trabalhador')
        super().__init__(nome)

class Atleta(Pessoa):
    def __init__(self, nome):
        print('Iniciando Atleta')
        super().__init__(nome)

class SuperHeroi(Trabalhador, Atleta):
    def __init__(self, nome):
        print('Iniciando Super-Herói')
        super().__init__(nome)

hero = SuperHeroi('Felipão')
print(hero.nome)

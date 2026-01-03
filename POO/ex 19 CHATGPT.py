class Pessoa:
     def __init__(self,nome):
         self.nome = nome



class Trabalhador(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)



class Atleta(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)


class Heroi(Trabalhador,Atleta):
    def __init__(self,nome):
        super().__init__(nome)



heroi = Heroi('FELIPÃO')
print(heroi.nome)
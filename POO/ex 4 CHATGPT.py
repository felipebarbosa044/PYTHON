class Pessoa:
    def __init__(self,nome):
        self.nome = nome


    def falar(self):
        print(f'{self.nome},esta falando...')


class Cliente(Pessoa):
    def __init__(self,nome):
        super().__init__(nome)


    def comprar(self):
        print(f'{self.nome} esta comprando...')


l = Cliente('felipao')
l.falar()
l.comprar()

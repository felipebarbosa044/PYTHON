class Veiculo:
    def  mover(self):
        print('O veiculo esta se movendo')


class Animal:
    def mover(self):
        print('O animal esta se movendo')


class Centauro(Animal,Veiculo):
    def mover(self):
        print('o Centauro esta se movendo')
        super().mover()


m = Centauro()
m.mover()
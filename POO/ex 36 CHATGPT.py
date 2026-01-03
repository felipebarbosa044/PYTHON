class Motor:
    def __init__(self):
        self.__motor = 'DESLIGADO'

    def info(self):
        return self.__motor

    def ligar(self):
        self.__motor = 'LIGADO'


    def desligar(self):
        self.__motor = 'DESLIGADO'

class Carro:
    def __init__(self):
        self.carro = Motor()

    def ligar(self):
        self.carro.ligar()

    def desligar(self):
        self.carro.desligar()

    def dirigir(self):
        from pacote.cores import cor
        if self.carro.info() == 'LIGADO':
            cor('DIRIGINDO',"verde")
        else:
            cor('MOTOR DESLIGADO', "vermelho")

car = Carro()
car.dirigir()
print('-'*70)
car.ligar()
car.dirigir()
print('-'*70)
car.desligar()
car.dirigir()





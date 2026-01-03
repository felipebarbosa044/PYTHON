from abc import ABC,abstractmethod
from pacote.cores import cor

class Personagem(ABC):
    def __init__(self,nome,poder):
        self.nome = nome
        self.poder = poder

    @abstractmethod
    def atacar(self):
        pass



class Arqueiro(Personagem):
    def __init__(self,nome,poder):
        super().__init__(nome,poder)



    def atacar(self):
        print(f'{self.nome} o arqueiro esta atirando uma flecha de {self.poder}')


class Cavalheiro(Personagem):
    def __init__(self, nome,poder):
        super().__init__(nome,poder)

    def atacar(self):
        print(f'{self.nome} o cavalheiro esta atacando com uma espada de {self.poder}')


class Mago(Personagem):
    def __init__(self, nome,poder):
        super().__init__(nome,poder)

    def atacar(self):
        print(f'{self.nome} lança uma bola de {self.poder}!')

a = 0
personagens = []

def mostrar_ataque(personagem= '<desconhecido>'):
    if personagem == '<desconhecido>':
        cor('PORFAVOR DIGITE O NOME DO PERSONAGEM!!',"vermelho")
    if isinstance(personagem,Personagem) == False:
        cor('Verifique se você digitou um objeto valido!!', "vermelho")
    else:
        return eval('personagem.atacar()')


for c in personagens:
    mostrar_ataque(c)



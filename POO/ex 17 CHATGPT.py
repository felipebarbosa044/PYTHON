class Corredor():
    def correr(self):
        print('O corredor esta correndo')



class Nadador:
    def nadar(self):
        print('O nadador esta nadando')


class Triatleta(Corredor,Nadador):
    def atividade(self):
        print('O triatleta esta em atividade...')
        super().nadar()




f = Triatleta()
f.atividade()

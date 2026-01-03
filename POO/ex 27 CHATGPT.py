class Carro:
    def __init__(self,velocidade):
        self._velocidade = 100
        from pacote.cores import cor
        if velocidade > 200 or velocidade < 0:
            cor('VELOCIDADE INVALIDA!!', "vermelho")
        else:
            self._velocidade = velocidade

    @property
    def velo(self):
        return self._velocidade


    @velo.setter
    def velo(self,velocidade):
        from pacote.cores import cor
        if velocidade > 200 or velocidade < 0:
            cor('VELOCIDADE INVALIDA!!',"vermelho")
        else:
            self._velocidade = velocidade

carro = Carro(500)
print(carro.velo)
carro.velo = -1
print(carro.velo)


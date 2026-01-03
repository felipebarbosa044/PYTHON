class ContaBancaria:
    def __init__(self,saldo):
        self._saldo = saldo


    @property
    def saldo(self):
        return self._saldo


    @saldo.setter
    def saldo(self,novo):
        from pacote.cores import cor
        if novo <= 0:
            cor('SALDO INVALIDO!!',"vermelho")
        else:
            self._saldo = novo
            cor('SALDO ALTERADO COM SUCESSO!!', "verde")


conta = ContaBancaria(500)
print(conta.saldo)
print('-'*70)
conta.saldo = 50
print('-'*70)
print(conta.saldo)

import hashlib
from rich import print

class ContaBancaria:
    def __init__(self,id,titular,saldo,senha = None):
        self._id = id
        self._titular = titular.title()
        self.__saldo = saldo
        if senha == None:
            senha = self.pede_senha()

        self.__hash = hashlib.sha256(str(senha).encode()).hexdigest()
        print(f"Conta [blue]{self._id}[/] criada com sucesso.Saldo atual de [green]R${self.__saldo:,.2f}")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self,nome):
        senha = self.pede_senha()

        if senha:
            print(f"[blue]{self._titular}[/] seu nome foi alterado para [cyan]{nome.title()}")
            self._titular = nome.title()
        else:
            raise ValueError("Senha Incorreta!")

    def validar_senha(self,senha) -> bool:
        hash_senha = hashlib.sha256(str(senha).encode()).hexdigest()
        if hash_senha == self.__hash:
            return True
        else:
            return False

    def pede_senha(self) -> str:
        senha = str(input("Senha: ")).strip()
        return senha

    def sacar(self,valor = 0,senha = None):
        if senha == None:
            senha = self.pede_senha()

        senhaVerificada = self.validar_senha(senha)

        if senhaVerificada:
            valor = abs(valor)
            if valor > self.__saldo:
                print(f"[red]Saque NEGADO,você não tem dinheiro suficiente para sacar[/]\nSaldo da conta: [green]R${self
                .__saldo:,.2f}")
            else:
                print(f"Saque de [green]R${valor:,.2f}[/] autorizado na conta [blue]{self._id}")
                self.__saldo -= valor
        else:
            raise ValueError("Senha Incorreta!")

    def depositar(self,valor):
        valor = abs(valor)

        self.__saldo += valor
        print(f"Deposito de [green]R${valor:,.2f}[/] autorizado na conta [blue]{self._id}")
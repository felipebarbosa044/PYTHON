from rich import print
from rich.panel import Panel
from time import sleep


class Funcionario:
    """"
    Representa um funcionário de uma empresa.

    A classe armazena informações profissionais da pessoa
    e possui um method para gerar uma apresentação simples
    com base nesses dados.

    Attributes:
        nome (str): Nome do funcionário.
        setor (str): Setor onde o funcionário trabalha.
        cargo (str): Cargo ocupado pelo funcionário.

    """
    def __init__(self, nome , setor , cargo,empresa="Curso em Vídeo"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentar(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou  {self.cargo} do setor de {self.setor} da empresa {self.empresa}"

    def __str__(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou  {self.cargo} do setor de {self.setor} da empresa {self.empresa}"



print("Digite seu [red]nome[/]: ",end='')
nome = input()
sleep(1)
print("Digite qual é a seu [red]setor[/] de trabalho: ",end='')
setor = input()
sleep(1)
print(f"Digite seu [red]cargo[/] no setor de {setor}: ",end='')
cargo = input()
sleep(1)


c1 = Funcionario(nome,setor,cargo)
print(c1.apresentar())

c2 = Funcionario("Maria","Adminstração","Diretora","Nubank")
print(c2.apresentar())




from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self,nome,quantidade = 0):
        self.nome = nome
        self.quantidade = quantidade

    def analisar(self):
        churrasco = Panel(f"Analisando [green]{self.nome}[/] com {self.quantidade} convidados")
        print(churrasco)

churrasco = Churrasco("Churras dos Amigos")
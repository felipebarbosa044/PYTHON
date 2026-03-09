from rich import print
from rich.panel import Panel



class Churrasco:
    def __init__(self,nome,quantidade = 0):
        self.nome = nome
        self.quantidade = quantidade

    def analisar(self):
        kg = self.quantidade * 0.4
        total_RS = kg * 82.40
        total_Participante =  total_RS / self.quantidade

        churrasco = Panel(f"Analisando [green]{self.nome}[/] com [blue]{self.quantidade} convidados[/]\nCada participante comerá 0.4Kg e cada Kg custa R$82.40\nRecomendado [blue]comprar {kg:.3f}Kg[/] de carne\nO custo total será de [green]R${total_RS:.2f}[/]\nCada pessoa pagará [yellow]R${total_Participante}[/] para participar.",title=f"{self.nome}")
        print(churrasco)

churrasco = Churrasco("Churras dos Amigos",15)
churrasco.analisar()
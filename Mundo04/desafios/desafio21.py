from rich import print
from rich import inspect
import rich.color

class Caneta:
    def __init__(self,cor):
        self.cor = cor.lower()
        self.tampa = True

    def verificarCor(self):
        if self.cor  == "preto":
            self.cor = "black"
        elif self.cor == "vermelha":
            self.cor = "red"
        elif self.cor == "amarela":
            self.cor = "yellow"
        elif self.cor == "azul":
            self.cor = "blue"
        elif self.cor == "ciano":
            self.cor = "cyan"
        elif self.cor == "branca":
            self.cor = "white"
        elif self.cor == "laranja":
            self.cor = "orange4"
        elif self.cor == "roxa":
            self.cor = "pruple"
        elif self.cor == "rosa":
            self.cor = "pink3"
        elif self.cor == "bronze":
            self.cor = "tan"
        elif self.cor == "verde":
            self.cor = "green"
        else:
            self.cor = "white"

    def destampar(self):
        if self.tampa == True:
            self.tampa = False

    def tampar(self):
        if self.tampa == False:
            self.tampa = True

    def escrever(self,texto="Escreva Aqui"):
        self.verificarCor()
        if self.tampa == True:
            print(f":prohibited: A [{self.cor}]caneta[/] está tampada!")
        else:
            print(f"[{self.cor}]{texto}[/]",end='')

    def quebrar_linha(self,numero = 0):
        contador = 0
        while contador < numero:
            print("")
            contador += 1

c1 = Caneta('azul')
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Olá,Gafanhoto! ")
c3.escrever("Vamos exercitar!")



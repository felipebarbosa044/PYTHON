from rich import print
from rich.panel import Panel
import os #Usando os


class ControleRemoto:
    def __init__(self):
        self.controle = ''
        self.tv = ''
        self.canais = ["1","2","3","4","5"]
        self.volumes = ["[on white]","[on white]","[on white]","[on white]","[on white]","[on white]"]
        self.canal = 0
        self.volume = 0
        self.desligar()


    def desligar(self):
        os.system("cls") #Comando que apaga o console

        while True:
            self.tv = Panel("[bold red]:prohibited: A TV está desligada[/]",title="[ TV ]",width=30)
            print(self.tv)
            self.controle = input(f"< CH{self.canal + 1} >  - VOL{self.volume + 1} +  ")

            if  self.controle == "@":
                self.mudarCanal()
                break
            elif self.controle == "0":
                break



    def ligar(self):
        os.system("cls")

        volume = " ".join(self.volumes)
        canal = " ".join(self.canais)

        while True:
            self.tv = Panel(f"CANAL  = {canal}\nVOLUME = {volume}",title="[ TV ]",width=30)
            print(self.tv)
            self.controle = input(f"< CH{self.canal + 1} >  - VOL{self.volume + 1} +  ")

            if  self.controle == "@":
                self.desligar()
                break

            elif self.controle == ">":
                if self.canal + 1  == 5:
                     self.canais[self.canal] = f"{self.canal + 1}"
                     self.canal = 0
                     self.mudarCanal()
                else:
                    self.canais[self.canal] = f"{self.canal + 1}"
                    self.canal += 1
                    self.mudarCanal()

            elif self.controle == "<":
                if self.canal + 1  == 1:
                     self.canais[self.canal] = f"{self.canal + 1}"
                     self.canal = 4
                     self.mudarCanal()
                else:
                    self.canais[self.canal] = f"{self.canal + 1}"
                    self.canal -= 1
                    self.mudarCanal()

            elif self.controle == "+":
                if self.volume + 1 == 5:
                    self.volume = 4
                    self.mudarVolume()
                else:
                    self.volume += 1
                    self.mudarVolume()

            elif self.controle == "-":
                if self.volume + 1 == 1:
                    self.volume = 0
                    self.mudarVolume()
                else:
                    self.volumes[self.volume] = "[on white]"
                    self.volume -= 1
                    self.mudarVolume()

            if self.controle == "0":
                break


    def mudarCanal(self):
        self.canais[self.canal] = f"[on yellow] {self.canal + 1} [/]"
        self.mudarVolume()

    def mudarVolume(self):
        self.volumes[self.volume] = "[on green]"
        self.ligar()



tv = ControleRemoto()
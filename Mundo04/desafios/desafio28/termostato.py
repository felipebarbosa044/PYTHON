from rich import print

class Termostato:
    """
        Classe que simula um termostato.

        Permite configurar temperaturas entre 16°C e 30°C,
        aceitando apenas valores inteiros ou múltiplos de 0.5.
        Disponibiliza a temperatura tanto em formato numérico
        quanto formatada como texto.
    """
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return  self.__temperatura

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"

    @temperatura.setter
    def temperatura(self,temperatura):
        temperatura = abs(temperatura)
        if temperatura > 30:
            self.__temperatura = 30
        elif temperatura < 16:
            self.__temperatura = 16
        elif temperatura % 1 not in (0,0.5):
            print(f"Temperatura de [red]{temperatura}°C[/] é inválida")
        else:
            self.__temperatura = temperatura


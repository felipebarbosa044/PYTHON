from rich.panel import Panel

class Produto:
    """"

    """
    def __init__(self,nome,preço):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        etiqueta = Panel("-" * 30,title="Produto")
        print(etiqueta)

p1 = Produto('ff',190)
p1.etiqueta()
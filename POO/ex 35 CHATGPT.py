class Produto:
    def __init__(self,produto,preco):
        self.nome = produto
        self.preco = preco


    def __str__(self):
        from pacote.moeda import moeda
        return f'Produto: {self.nome}\nPreço: {moeda(self.preco)}'


class Produto_Digital:
    def __init__(self,produto,preco):
        self.nome = produto
        self.preco = preco


    def __str__(self):
        from pacote.moeda import moeda
        desconto =  self.preco - (self.preco * 10/100)
        return f'Produto: {self.nome}\nPreço: Com desconto de 10 % {moeda(desconto)}'




produto = Produto('Ps5',2500)
print(produto)
print('-' * 70)
produtodig = Produto_Digital('ps5',2500)
print(produtodig)



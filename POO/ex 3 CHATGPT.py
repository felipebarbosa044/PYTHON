from pacote.classe import Contabancaria
from pacote.string import linha

felipe = Contabancaria('felipe',15)
felipe.exibir()
joao = Contabancaria('joão',20)
joao.exibir()
joao.transferir(joao,felipe,15)
linha(70)
felipe.exibir()
joao.exibir()
print(len(felipe))
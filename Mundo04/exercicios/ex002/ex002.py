#Declaração de classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome,idade)
    """
    def __init__(self, nome = "", idade = 0): #Metodo construtor
        #atributos de instância
        self.nome = nome
        self.idade = idade

        #Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self): #Dunder Method
         return f"Olá {self.nome} seu pequeno gafanhoto de {self.idade} anos de idade"

#Declaração de objetos
g1 = Gafanhoto("Felipe" , 19)
g1.aniversario()
#print(g1)

print(g1.__dict__) #Attribut
print(g1.__getstate__()) #Method
print(g1.__class__)


#(g1.__doc__) # Dunder Attribute

class Personagem:
    def __init__(self,nome,vida,poder):
        self.nome = nome
        self.vida = vida
        self.poder = poder




class Mago(Personagem):
    def __init__(self,nome,vida,poder):
        super().__init__(nome,vida,poder)
        self.tipo = 'mago'



class Guerreiro(Personagem):
    def __init__(self, nome, vida, poder):
        super().__init__(nome, vida, poder)
        self.tipo = 'guerreiro'


class Inventario:
    def __init__(self,personagem):
        self.tipo = personagem.tipo

    def inventario(self):
        if self.tipo == 'mago':
            return ['Poção','Veneno','Magia']
        elif self.tipo == 'guerreiro':
            return['Espada','Escudo','Arco e flecha']
        else:
            return  'Você não escolheu um personagem que contenha um inventario'

    def mostrar_atributos(self,personagem):
        print(f'Nome: {personagem.nome}\nVida: {personagem.vida}\nPoder: {personagem.poder}\nInventario: {self.inventario()}')




personagem = Mago('Felipe',220,'Fogo')
inventario = Inventario(personagem)
inventario.mostrar_atributos(personagem)






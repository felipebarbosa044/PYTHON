# Com herança
#class Animal:
    #def falar(self):
        #print('Esse animal esta falando...')


#class Cachorro(Animal):
    #def falar(self):
        #print('AU AU AU')

#class Gato(Animal):
    #def falar(self):
        #print('MIAU MIAU')

#c = Gato()
#c.falar()

# Com composiçao:

class Gato:
    def falar(self):
        print('MIAU MIAU')


class Cachorro:
    def falar(self):
        print('AU AU AU')


class Animal:
    def __init__(self,animal):
        self.animal = animal.falar()

    def falar(self):
        return self.animal


cat = Animal(Gato())
cat.falar()






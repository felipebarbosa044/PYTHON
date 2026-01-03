class Animal:
    def falar(self):
        print('Esse animal faz esse barulho aqui...')



class Dog(Animal):
    def falar(self):
        print('au au au')



class Cat(Animal):
    def falar(self):
        print('miau miau')



cachorro = Dog()
gato = Cat()

cachorro.falar()
gato.falar()
Animal().falar()



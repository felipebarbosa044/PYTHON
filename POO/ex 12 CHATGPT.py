class Forma:
    def desenhar(self):
        print('Desenhando uma forma geométrica')


class Circulo(Forma):
    def desenhar(self):
        print('Desenhando um circulo...⭕')


class Triangulo(Forma):
    def desenhar(self):
        print('Desenhando um triângulo...🔺')


class Quadrado(Forma):
    def desenhar(self):
        print('Desenhando um quadrado...🟥')


quad = Quadrado()
circ = Circulo()
trian = Triangulo()


formas = [quad,trian,circ]

for c in formas:
    c.desenhar()


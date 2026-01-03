class Teclado:
    def digitar(self,txt):
        print(txt)


    def clicar(self,txt):
        print(f'Você cliclou na tecla: {txt}')






class Computador:
    def __init__(self,teclado):
        self.teclado = teclado

    def digitar(self,txt):
        return self.teclado.digitar(txt)

    def clicar(self,txt):
        return self.teclado.clicar(txt)


t  = Teclado()
a = Computador(t)
a.digitar('enter')
a.clicar('ESC')
class Liderança:
    def comunicar(self):
        print('O lider esta se comunicando')



class Tecnico:
    def comunicar(self):
        print('O tecnico esta se comunicando')



class Gestor(Liderança,Tecnico):
    def comunicar(self):
        print('Gestor esta se comunicando')
        super().comunicar()


a = Gestor()


a.comunicar()
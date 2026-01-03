#POOLIMORFISMO...
class Funcionario:
    def trabalhar(self):
        print('ele esta trabaiando')



class Professor(Funcionario):
    def trabalhar(self):
        print('Ele esta dando aula...')




class Engenheiro(Funcionario):
    def trabalhar(self):
        print('Ele esta construindo...')



prof = Professor()
eng = Engenheiro()

prof.trabalhar()
eng.trabalhar()



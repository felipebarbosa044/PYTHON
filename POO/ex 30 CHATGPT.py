# COM HERANÇA:


#class Pessoa:
    #def __init__(self,nome,idade):
        #self.idade = idade
        #self.nome = nome


#class Aluno(Pessoa):
    #def apresentacao(self):
        #print(f'Nome: {self.nome}\nIdade: {self.idade}')



#a1 = Aluno('Felipe',18)
#a1.apresentacao()

#COM COMPOSIÇÃO:
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


class Aluno:
    def __init__(self,classe):
        self.aluno = classe

    def apresentacao(self):
        print(f'Nome: {self.aluno.nome}\nIdade: {self.aluno.idade}')


a1 = Aluno(Pessoa('Felipe',17))
a1.apresentacao()



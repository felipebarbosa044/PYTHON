from abc import ABC, abstractmethod #Abstract Base Classes

class Pessoa(ABC):
    def __init__(self,nome = "",idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self,nome,idade, curso, turma):
        super().__init__(nome,idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print (f"{self.nome} de {self.idade} anos,  do curso {self.curso} e da turma {self.turma} fez a matricula")

    def estudar(self):
        print(f"{self.nome} esta estudando {self.curso} na turma {self.turma}")


class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} começou a dar aula")

    def estudar(self):
        print(f"{self.nome} esta estudando mais {self.especialidade}")


class Funcionario(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de bater ponto.")

    def estudar(self):
        print(f"{self.nome} esta estudandopara ser um ótimo {self.cargo}")

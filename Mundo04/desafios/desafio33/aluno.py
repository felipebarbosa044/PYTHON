from abc import ABC
from datetime import date
from rich import print

ano = date.today().year

class Pessoa(ABC):
    """
       Classe abstrata que representa uma pessoa.

       Armazena o nome e o ano de nascimento de uma pessoa,
       disponibilizando a idade como uma propriedade calculada
       automaticamente a partir do ano atual.

       Atributos:
           nascimento (int): Ano de nascimento da pessoa.
           idade (int): Idade calculada a partir do ano de nascimento.
    """
    def __init__(self,nome,nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self,nascimento):
        if isinstance(nascimento,int)  and nascimento<= ano and nascimento >= 1900:
            self._nascimento = nascimento
        else:
            raise ValueError("Ano de Nascimento inválido")

    @property
    def idade(self):
        idade = ano - self._nascimento
        return idade

    @idade.setter
    def idade(self,idade):
        print("[red]Você não pode alterar a idade. Mude o ano de nascimento")


class Aluno(Pessoa):
    """
      Representa um aluno.

      Herda os atributos de Pessoa e adiciona o conceito de curso.
      Apenas cursos cadastrados na lista de cursos oficiais podem ser
      atribuídos ao aluno.

      Atributos:
          curso (str): Curso em que o aluno está matriculado.

      Atributos de classe:
          cursos_oficiais (list[str]): Lista de cursos permitidos.
    """
    cursos_oficiais = ["DDS","PDJ","CEV"]
    def __init__(self,nome = "Aluno",nascimento = "2000",curso = None):
        super().__init__(nome,nascimento)
        for c in Aluno.cursos_oficiais:
            if curso.upper() == c:
                self._curso = curso.upper()
                return

        raise ValueError(f"O curso {curso} não está na lista de cursos oficiais")



    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self,curso):
        for c in Aluno.cursos_oficiais:
            if curso.upper() == c:
                self._curso = curso.upper()
                return

        raise ValueError(f"O curso {curso} não está na lista de cursos oficiais")

    def adicionar_curso(self,curso):
        curso_list = list(str(curso))
        if len(curso_list) > 5:
            raise ValueError("O curso só pode ter a abreviatura de até 5 caracteres")
        else:
            Aluno.cursos_oficiais.append(str(curso).upper())











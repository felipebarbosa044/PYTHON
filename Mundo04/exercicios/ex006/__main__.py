from rich import print,  inspect

from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno("Felipe", 19, "Desenvolvimento de Sistemas",3)
    a1.fazer_aniversario()
    a1.fazer_matricula()
    inspect(a1,methods=True)

    p1 = Professor("Davison" , 44,"TCC","Politico")
    p1.fazer_aniversario()
    p1.dar_aula()
    inspect(p1,methods=True)

    f1 = Funcionario("José",15,"Faxineiro","Aprendiz")
    f1.fazer_aniversario()
    f1.bater_ponto()
    inspect(f1,methods=True)

if __name__ == "__main__":
    main()
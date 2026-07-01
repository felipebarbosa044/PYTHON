from aluno import *
from rich import inspect , print


def main():
    a = Aluno("Felipe", 2006, "pdj")
    try:

        a.nascimento = 2010
        # a.adicionar_curso("moda")
        # a.curso = "moda"

    except Exception as e:
        print(f"[red]ERRO: {e}")

    inspect(a, private=True,methods=True)

if __name__ == '__main__':
    main()
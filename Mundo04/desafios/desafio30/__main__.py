from credencial import Credencial
from rich import inspect

def main():
    c = Credencial()
    c.senha = str(input("Digite sua senha: ")).strip()
    c.validar(str(input("Digite sua senha novamente: ")))
    inspect(c,private=True,methods=True)

if __name__ == '__main__':
    main()
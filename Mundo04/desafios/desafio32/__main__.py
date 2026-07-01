from banco import ContaBancaria
from rich import inspect , print

def main():
    cc = ContaBancaria("122","Felipe Barbosa",3000,"12345678")

    try:
        cc.depositar(500)
        cc.sacar(500,12345678)
        cc.nome = "Neymar"

    except Exception as e:
        print(f"[red]ERRO:  {e}")

    inspect(cc, methods=True, private=True)

if __name__ == '__main__':
    main()
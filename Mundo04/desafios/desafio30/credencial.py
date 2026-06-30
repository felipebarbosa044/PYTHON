# Biblioteca para geração de hashes criptográficos
import hashlib

from rich import print

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self,senha):
        #Cripotgrafia a senha com hash HSA-256
        try:
            hash_senha = hashlib.sha256(str(senha).encode()).hexdigest()
            self.__hash = hash_senha
        except Exception as e:
            print(f"[red]ERRO AO CRIPTOGRAFAR SENHA COM HASH 256[/]: {e} ")


    def validar(self,senha):
        try:
            hash_senha = hashlib.sha256(str(senha).encode()).hexdigest()

            if hash_senha != self.__hash:
                print("[red]Senha não bate!")
            else:
                print("[green]Senha confere!")

        except Exception as e:
            print(f"[red]ERRO AO CRIPTOGRAFAR SENHA COM HASH 256: {e} ")




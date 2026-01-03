import sys
from time import sleep

from pacote.cores import cor
from pacote.matematica import leiaint
from pacote.moeda import  moeda
from pacote.string import linha, leianome


class Pessoa:
    def __init__(self,nome,idade):
        self.idade = idade
        self.nome = nome.title().strip()


    def apresentar(self):
        print(f'Olá eu me chamo {self.nome} e tenho {self.idade} anos')


    def aniversario(self):
        self.idade = self.idade + 1
        print(f'Hoje é meu aniversario,e esto fazendo {self.idade} anos')


class Contabancaria:
    def __init__(self,titular="<Desconhecido>",saldo= 0):
        self.titular = titular.title().strip()
        self.__saldo = saldo


    def exibir(self):
        linha(70)
        cor(f'O nome do titular : ',"rosa",juntar=True),cor(f'{self.titular}',"ciano",juntar=True)
        cor('    Saldo: ',"rosa",juntar=True),cor(f'{moeda(self.__saldo)}',"ciano")
        linha(70)

    def saque(self,sacar = 0):
        if self.__saldo < sacar:
            cor('ERRO!,Você não pode sacar um valor acima de seu saldo',"vermelho")
        else:
            self.__saldo = self.__saldo - sacar
            linha(70)
            cor(f'Parabens!! Você sacou {moeda(sacar)}',"verde",juntar=True),cor(f'    Saldo disponivel : ',"amarelo",juntar=True)
            cor(f'{moeda(self.__saldo)}',"verde")
            linha(70)


    def depositar(self,dep):
        if dep < 0:
            cor('Digite um valor acima de 0 para Depositar!',"vermelho")
            sys.exit()

        self.__saldo = self.__saldo + dep
        linha(70)
        cor(f'Você depositou:  {moeda(dep)}', "vermelho", juntar=True), cor(f'    Saldo disponivel : ', "amarelo",juntar=True)
        cor(f'{moeda(self.__saldo)}', "verde")
        linha(70)


    def transferir(self,de,para,din =0):
        if din > de.__saldo:
            cor('ERRO!,Você não pode sacar um valor acima de seu saldo', "vermelho")
        else:
            de.__saldo -= din
            para.__saldo += din
            linha(70)
            cor(f'Você transferiu',"verde",juntar=True), cor(f' {moeda(din)} com sucesso!',"rosa")
            cor(f'Pagamento para {para.titular} efetuado!',"verde")
            linha(70)



class Usuario:
    def __init__(self):
        self.__nome = leianome('Digite o seu nome: ')
        self.__senha = leiaint('Digite a sua senha: ')


    def getnome(self):
        return cor(f'{self.__nome}',"verde")



    def senha(self):
        x = 0
        while x < 3:
            se = leiaint('Digite a sua senha novamente: ')
            if se == self.__senha:
                return cor('Você foi cadastrado com sucesso!',"verde")
            else:
                cor('Digite a a mesma senha que você digitou minutos antes',"vermelho")
                if x == 2:
                    cor('Conta bloqueada',"vermelho")
                x+= 1


    def trocarsenha(self):
        while True:
            nova = leiaint('Digite a sua nova senha: ')
            if nova == self.__senha:
                cor('Digite uma senha diferente da atual!!',"vermelho")
            else:
                cor('Sua senha foi alterada, antes de ',"verde",juntar=True)
                cor(f'{self.__senha}',"rosa",juntar=True)
                self.__senha = nova
                cor(',Para ',"verde",juntar=True)
                cor(f'{self.__senha}',"rosa")
                break


    def __str__(self):
        return f'Usuario:     {self.__nome}'



    def info(self):
        try:
            quant = len(self.__senha)
        except:
            sen = str(self.__senha)
            quant = len(sen)
            cor(f'Transformando <int> em <str>...')
            sleep(1.5)
            linha(70)

        print(f'Nome do usuario:    {self.__nome}')
        print(f'Sua senha tem {quant} digitos')
















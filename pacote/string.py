from pacote.cores import cor
import re


def linha(tam = 70):
    print( '-' * tam)


def cabecalho(txt):
    print(linha())
    print(txt.center(70))
    print(linha())


def leianome(n='',longo = False,sim = False):
    nome= str(input(f'{n}'))
    total = len(nome)
    x = 0
    while True:
        if sim == True:
            if re.search(r'[^a-zA-Z0-9 ]', nome):
                cor('ERRO!Digite um nome valido!! SEM SIMBOLOS', "vermelho")
                nome = str(input(f'{n}'))
        elif nome.isnumeric() == True:
            cor('Digite um nome valido!! SEM NUMEROS1', "vermelho")
            nome = str(input(f'{n}'))
        while x < 9:
            for l in nome[0:total]:
                if str(x) == l:
                    cor('Digite um nome valido!! SEM NUMEROS1', "vermelho")
                    x = 0
                    nome = str(input(f'{n}'))
            x += 1
        else:
            break
    if longo == True:
        if len(nome.split()) > 3:
            cor('Esse nome é longo demais, digite apenas os 3 primeiro nomes!',"vermelho")
            return leianome()
        else:
            return nome.title().strip()
    else:
        return nome.title().strip()





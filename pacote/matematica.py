from time import sleep

from pacote.cores import cor
from pacote import string
from math import sqrt

def leiafloat(n):
    while True:
        try:
            nu = float(input(f'{n}'))
        except(KeyboardInterrupt):
            cor('O usuario não inseriu o valor', "vermelho")
            nu = 0
            return nu
            break
        except:
            cor('INVALIDO!!,Digite um numero inteiro valido!!', "vermelho")

        else:
            return nu
            break


def leiaint(n = ''):
    while True:
        try:
            nu = int(input(f'{n}'))
        except(KeyboardInterrupt):
            cor('O usuario não inseriu o valor', "vermelho")
            return 0
        except:
            cor('INVALIDO!!,Digite um numero inteiro valido!!',"vermelho")

        else:
            return nu


def leiafloat(n):
    while True:
        try:
            nu = float(input(f'{n}'))
        except(KeyboardInterrupt):
            cor('O usuario não inseriu o valor', "vermelho")
            nu = 0
            return nu
            break
        except:
            cor('INVALIDO!!,Digite um numero inteiro valido!!', "vermelho")

        else:
            return nu
            break



def calc(n1 = '',n2 = '',op = ''):
    msg = '''[+] Para SOMAR
[-] Para SUBTRAIR
[*] Para MULTIPLICAR
[/] Para DIVIDIR
[%] Para Divisão inteira'''
    if n1 == '' and n2 == '' and op == '':
        n1 = leiaint('Digite o 1 numero: ')
        n2 = leiaint('Digite o 2 numero: ')
        op = str(input(f'{msg}\nDigite aqui: '))
    while True:
        if op not in '%*-/+':
            cor('Digite uma operação valida!!',"vermelho")
            print(msg)
            string.linha(50)
            sleep(1.5)
            op = '8999'
            if op == '8999':
                op = str(input('Digite aqui: '))
        else:
            break
    resul = f'{n1}{op}{n2}'
    try:
         eval(resul)
    except Exception as erro:
        cor(f'OPS PARECE QUE HÁ ALGUM ERRO AQUI... {erro.__class__} ',"vermelho")
        cor('Tente novamente!',"amarelo")
        string.linha(50)
        sleep(1.5)
        calc()
    else:
        print(eval(resul))


def avaliar(med ='',media = 55565):
    if media == 55565:
        media = leiafloat(med)
    if media > 5.5:
        return 'APROVADO'
    elif media <= 5.5 and media > 4:
        return 'RECUPERAÇÃO'
    else:
        return 'REPROVADO'


def criar_aluno(nome = 'Desconhecido',notas = []):
    media = sum(notas) / len(notas)
    situacao = avaliar('',media)
    alunos= {
    "nome": nome.title().strip(),
    "media": round(media),
    "situacao": situacao
    }
    return alunos





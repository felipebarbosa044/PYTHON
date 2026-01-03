from pacote.cores import cor
from pacote.matematica import leiaint
from pacote.string import leianome


def noarq(arquivo):
    nome = leianome('Nome: ')
    idade = leiaint('Idade: ')
    with open(arquivo,'a') as arq:
        arq.write(f'{nome}     \t {idade} anos\n')



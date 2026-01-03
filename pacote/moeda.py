from time import sleep


def moeda(n):
    valor = str(n)
    valor = 'R$'+ valor
    return valor



def dobro(n,op = True):
    dobro = n * 2
    if op == True:
        valor = str(dobro)
        valor  ='R$'+valor
        return valor
    else:
        return dobro


def metade(n,op = True):
    metade = n / 2
    if op == True:
        valor = str(metade)
        valor  ='R$'+valor
        return valor
    else:
        return metade


def aumento(n,por = -445,op = True):
    if por == -446:
        por = int(input('Digite quantos porcentos você vai aumentar desse valor: '))
    au = n + (n * por/100)
    if op == True:
        valor = str(round(au,2))
        valor = 'R$' + valor
        return valor
    else:
        return round(au,2)


def diminui(n,pox = -445,op = True):
    if pox == -446:
        pox = int(input('Digite qual é a porcentagem uqe  você vai diminuir desse valor: '))
    au = n - (n * pox/100)
    if op == True:
        valor = str(round(au,2))
        valor = 'R$' + valor
        return valor
    else:
        return round(au,2)


def resumo(n,au,dim):
    print('-'*45)
    print('                Resumo do valor')
    print('-' * 45)
    sleep(2)
    print(f'Valor analisado:                       {moeda(n)}')
    print(f'Dobro do preço:                        {dobro(n)}')
    print(f'Metade do preço:                       {metade(n)}')
    print(f'{au}% do preço aumentado:                {aumento(n,au)}')
    print(f'{dim}% de redução:                        {diminui(n,dim)}')
    print('-' * 45)



def linhas(t):
    global total
    total = len(t)
    print('-'* total)
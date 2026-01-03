from time import sleep

from pacote.cores import cor


while True:
    cor("TELA DE LOGIN".center(130),"azul")
    nick = {"Login": "Nesferaz"}
    piv = {"Senha": "882606"}
    laoding = ['.','.','.']
    while True:
        username = str(input('Digite o seu nick: ')).title()
        senha = str(input("Digite a sua senha: "))
        if username != nick["Login"]:
            cor('Nick não Encontrado!!'.upper(),"vermelho")
        elif senha != piv["Senha"]:
            cor('Senha Invalida!!'.upper(), "vermelho")
        else:
            cor("CADASTRO REALIZADO COM SUCESSO!",'azul')
            break
    for c in laoding:
        print(c,end='')
        sleep(1)
    print()
    cor('Loja Do Fernandinho'.center(150,'-'),"azul")
    produto = str(input('Digite o nome do produto: ')).title().strip()
    preco = float(input('Digite o valor do produto: '))
    while True:
        sleep(1)
        cor('-'.center(150,'-'),'vermelho')
        print('Digite ',end='')
        cor('[1] ','amarelo',juntar=True)
        print('para DESCONTO')
        print('Digite ', end='')
        cor('[2] ','vermelho',juntar=True)
        print('para valor sem DESCONTO')
        op = int(input('Digite aqui: '))
        if op < 1 or op > 2:
            cor('Digite uma opção VALIDA!!!'.upper(),'vermelho')
        else:
            for c in laoding:
                print(c, end='')
                sleep(1)
            break
    cor('-'.center(150, '-'), 'rosa')
    if op == 1:
        porcentagem = int(input('Digite a porcentagem do Desconto: '))
        for c in laoding:
            print(c, end='')
            sleep(1)
        print()
        valornovo = preco - (preco * porcentagem / 100)
        cor('-'.center(150, '-'), 'rosa')
        print(f'O produto {produto} , que custava ',end='')
        cor(f"R${preco}",'verde')
        print(f'Com {porcentagem}% de Desconto sai por ')
        cor(f'R${valornovo}','verde')
    else:
        print('O produto vai sair por ')
        cor(f'R${preco}','verde')
    continue














from time import sleep
from pacote.cores import cor
produto = str(input('Digite o nome do produto: ')).title()
valor = float(input("Digite o valor desse produto: "))
porcentagem = int(input("Digite o valor da porcentagem: "))
laoding = ['.','.','.']
while True:
    print("Digite [1] Para AUMENTO")
    print("Digite [2] Para DESCONTO")
    opcao = int(input("Digite aqui: "))
    if opcao != 1 and opcao != 2:
        cor("Digite uma opçao valida!!!","vermelho")
        for ponto in laoding:
            print(ponto,end="")
            sleep(1)
        print()
    else:
        if opcao == 1:
            valornovo = valor + (valor * porcentagem / 100)
            aplicacao = "Aumento"
            break
        else:
            valornovo = valor - (valor * porcentagem / 100)
            aplicacao = "Desconto"
            break
print(f"Com o {aplicacao} de ",end='')
cor(f'%{porcentagem}','azul',juntar=True)
print(" o valor de: ",end='')
cor(f"R${valor}","verde")
print(f"O Produto: {produto} Vai ficar ",end='')
cor(f"R${valornovo}","verde")





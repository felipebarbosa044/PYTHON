from time import sleep
tarefas = []
opcao = remover = 1
from pacote.cores import cor
while opcao != 4:
    print("TAREFAS".center(70))
    print("""Digite [1] Para adicionar uma tarefa
Digite [2] Listar todas as tarefas""")
    print("Digite [3]",end='')
    cor(" Remover tarefa",'rosa')
    print("Digite [4] ",end='')
    cor("Sair","vermelho")
    opcao = int(input(': '))
    if opcao < 1 or opcao > 4 :
        cor("Digite uma opção VALIDA!!",'vermelho')
        sleep(2)
        continue
    if opcao == 1:
        tarefas.append(str(input('Digite a tarefa: ').title().strip()))
        sleep(2)
        continue
    elif opcao == 2:
        print('-' * 50)
        for i,v in enumerate(tarefas):
            print(f'{i + 1} - {v}')
            continue
        print('-' * 50)
        sleep(2)
    elif opcao == 3:
        while remover != 999:
            print('-' * 50)
            for i, v in enumerate(tarefas):
                print(f'{i + 1} - {v}')
            print('-' * 50)
            cor('Digite [999] Para retornar ao menu', 'ciano')
            cor('Qual tarefa você deseja remover?: ','vermelho',juntar=True)
            remover = int(input('Digite aqui o numero da opção: '))
            sleep(2)
            print('...')
            if remover > len(tarefas) or remover < 0:
                if remover != 999:
                    cor('Digite uma opção VALIDA!!','vermelho')
                    sleep(2)
                    continue
            else:
                tarefas.pop(remover - 1)
                sleep(2)
                break
        continue








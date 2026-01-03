def cor(texto = '',cor = "branco",fund = '',juntar = False):
    cores = {
    "branco": "\033[;m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "rosa": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
    "reset": "\033[m"

    }
    fundo = {
    "vermelho": "41m",
    "verde": "42m",
    "amarelo": "43m",
    "azul": "44m",
    "rosa": "45m",
    "ciano": "46m",
    "cinza": "47m",
    }


    if fund != '':
        cores = {
            "branco": "\033[;",
            "vermelho": "\033[31;",
            "verde": "\033[32;",
            "amarelo": "\033[33;",
            "azul": "\033[34;",
            "rosa": "\033[35;",
            "ciano": "\033[36;",
            "cinza": "\033[37;",
            "reset": "\033[m"
        }
        corn = f"{cores[cor]+fundo[fund]}"
        if juntar == False:
            return print(f'{corn}{texto}{cores["reset"]}')
        else:
             return print(f'{corn}{texto}{cores["reset"]}',end='')

    if juntar == True:
        return print(f'{cores[cor]}{texto}{cores["reset"]}',end='')
    else:
        return print(f'{cores[cor]}{texto}{cores["reset"]}')

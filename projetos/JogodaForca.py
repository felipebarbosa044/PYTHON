from random import randint
from pacote.cores import cor
import sys

print('JOGO DA FORCA'.center(99,'-'))

palavras = ['santos','jesus','toalha','computador','programaçao','chuva','moto','banana','python','mano','achocolatado','sermao','aurora']
sorteio = randint(0,len(palavras)-1)
for p,v in enumerate(palavras):
    if p == sorteio:
        tot = len(v)
palavra = []
palavraa = palavras[sorteio].replace('',' ').strip()
palavraa = palavraa.split()
y = 1
vidas = 10
while vidas > 0:
    print(f'Acerte a palavra,você tem {vidas} vidas'.center(99,'-'))
    print(f'Essa palavra contém {tot} letras')
    if y == 1:
        for c in range(0,tot):
            print('_ ',end='')
            palavra.append('_')
            y = 0
        print()
    else:
        print(palavra)
    letra = str(input('Digite uma letra: ')).lower().strip()
    if letra.isalpha() == False:
        cor('Digite uma letra!!',"vermelho")
        continue
    elif len(letra) > 1:
        cor('Porfavor digite só uma letra!!',"vermelho")
        continue
    if letra in palavras[sorteio]:
        cor("PARABENS! VOCÊ ACERTOU!!","verde")
        for i,v  in  enumerate(palavras[sorteio]):
            if v == letra:
                palavra[i] = letra
    else:
        cor('ERROU!!',"vermelho")
        cor('-1 vida',"vermelho")
        vidas-= 1
        cor(f'Agora você tem {vidas} restantes!',"vermelho")
    if palavra == palavraa:
        cor('FIM DE JOGO, VOCÊ VENCEU!', "verde", juntar=True)
        cor(f' A palavras era:', "branco", juntar=True)
        cor(f' {palavras[sorteio]}', "rosa")
        sys.exit()


cor('FIM DE JOGO, VOCÊ PERDEU!',"vermelho",juntar=True)
cor(f' A palavras era:',"branco",juntar=True)
cor(f' {palavras[sorteio]}',"rosa")






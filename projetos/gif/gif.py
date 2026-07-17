import imageio.v3 as iio

arquivos = ['nyan-cat1.png','nyan-cat2.png','nyan-cat3.png']
dados_imagens = []

for imagem in arquivos:
    dados_imagens.append(iio.imread(imagem))

iio.imwrite('nyan-cat.gif', dados_imagens, duration = 500, loop = 0)
from pacote.string import linha
class ArquivoSecreto:
    def __init__(self,senha,conteudo):
        self._verificar = False
        self.__senha = senha
        self._conteudo = conteudo

    @property
    def senha(self):
        return 'ACESSO DA SENHA NEGADO'

    @senha.setter
    def senha(self,novo):
        from pacote.cores import cor
        if len(novo) >= 8:
            self.__senha = novo
            self._verificar = True
            cor('Senha desboqueada com sucesso',"verde")
        else:
            from pacote.cores import cor
            cor('A SENHA TEM QUE TER PELO MENOS 8 CARACTERES',"vermelho")



    @property
    def conteudo(self):
        if self._verificar == False:
            return 'ACESSO DO CONTEUDO NEGADO'
        else:
            return f'CONTEUDO : {self._conteudo}'


msg = ArquivoSecreto('882606felipe04','Ola ninos')

print(msg.conteudo)
linha()
print(msg.senha)
linha()
msg.senha = '1234567'
print(msg.conteudo)
linha()
msg.senha = '12345678'
print(msg.conteudo)



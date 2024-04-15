import platform

class Plataforma:
    def __init__(self):
        self.__sistema = platform.system()
        self.__versao = platform.version()
        self.__arquitetura_sistema = platform.architecture()
        self.__informacoes = platform.uname()
    
    @property
    def sistema(self):
        return self.__sistema
    @property
    def versao(self):
        return self.__versao
    @property
    def arquitetura_sistema(self):
        return self.__arquitetura_sistema
    @property
    def informacoes(self):
        return self.__informacoes
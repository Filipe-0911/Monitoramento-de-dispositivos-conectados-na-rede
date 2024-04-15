import os
import re

class Leitura:
    def __init__(self, nome_arquivo):
        self.__pasta_raiz = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.__nome_arquivo = nome_arquivo
    
    @property
    def nome_arquivo(self):
        return self.__nome_arquivo
    
    @property
    def pasta_raiz(self):
        return self.__pasta_raiz
    
    def get_conteudo(self):
        lista_dispositivos = []
        with open(self.nome_arquivo) as arquivo:            
            conteudo = arquivo.read()
            padrao_mac_address = r'MAC Address: ([0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5}) \((.*?)\)'
            resultados = re.findall(padrao_mac_address, conteudo)

            for mac, fabricante in resultados:
                disp = {"nome":fabricante.title(), "mac_address":mac.lower()}
                lista_dispositivos.append(disp)

        return lista_dispositivos
